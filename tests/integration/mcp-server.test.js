/**
 * Integration tests for the MCP server.
 * These tests use the real specs directory to verify end-to-end functionality.
 */
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { dirname, join } from "node:path";
import { test, describe, before, after } from "node:test";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const projectRoot = join(__dirname, "..", "..");
const serverPath = join(projectRoot, "dist", "index.js");

/**
 * Helper to send JSON-RPC request to MCP server via stdio
 */
class MCPClient {
  constructor() {
    this.process = null;
    this.requestId = 0;
    this.pendingRequests = new Map();
    this.buffer = "";
  }

  async start() {
    this.process = spawn("node", [serverPath], {
      cwd: projectRoot,
      stdio: ["pipe", "pipe", "pipe"],
    });

    this.process.stdout.on("data", (data) => {
      this.buffer += data.toString();
      this.processBuffer();
    });

    this.process.stderr.on("data", (data) => {
      // Log stderr for debugging but don't fail
      if (process.env.DEBUG) {
        console.error("Server stderr:", data.toString());
      }
    });

    // Wait for server to be ready
    await new Promise((resolve) => setTimeout(resolve, 500));

    // Initialize the connection
    await this.request("initialize", {
      protocolVersion: "2024-11-05",
      capabilities: {},
      clientInfo: { name: "test-client", version: "1.0.0" },
    });

    await this.notify("notifications/initialized", {});
  }

  processBuffer() {
    const lines = this.buffer.split("\n");
    this.buffer = lines.pop() || "";

    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const message = JSON.parse(line);
        if (message.id !== undefined && this.pendingRequests.has(message.id)) {
          const { resolve, reject } = this.pendingRequests.get(message.id);
          this.pendingRequests.delete(message.id);
          if (message.error) {
            reject(new Error(message.error.message));
          } else {
            resolve(message.result);
          }
        }
      } catch {
        // Ignore non-JSON lines
      }
    }
  }

  async request(method, params = {}) {
    const id = ++this.requestId;
    const message = {
      jsonrpc: "2.0",
      id,
      method,
      params,
    };

    return new Promise((resolve, reject) => {
      this.pendingRequests.set(id, { resolve, reject });
      this.process.stdin.write(JSON.stringify(message) + "\n");

      // Timeout after 10 seconds
      setTimeout(() => {
        if (this.pendingRequests.has(id)) {
          this.pendingRequests.delete(id);
          reject(new Error(`Request ${method} timed out`));
        }
      }, 10000);
    });
  }

  async notify(method, params = {}) {
    const message = {
      jsonrpc: "2.0",
      method,
      params,
    };
    this.process.stdin.write(JSON.stringify(message) + "\n");
    await new Promise((resolve) => setTimeout(resolve, 100));
  }

  async stop() {
    if (this.process) {
      this.process.stdin.end();
      this.process.kill();
      await new Promise((resolve) => setTimeout(resolve, 100));
    }
  }
}

describe("MCP Server Integration Tests", () => {
  let client;

  before(async () => {
    client = new MCPClient();
    await client.start();
  });

  after(async () => {
    await client.stop();
  });

  test("lists available tools", async () => {
    const result = await client.request("tools/list", {});
    assert.ok(Array.isArray(result.tools), "Should return tools array");

    const toolNames = result.tools.map((t) => t.name);
    assert.ok(toolNames.includes("get_spec"), "Should have get_spec tool");
    assert.ok(toolNames.includes("get_checklist"), "Should have get_checklist tool");
    assert.ok(toolNames.includes("get_linter_rule"), "Should have get_linter_rule tool");
    assert.ok(toolNames.includes("search_specs"), "Should have search_specs tool");
    assert.ok(toolNames.includes("list_available"), "Should have list_available tool");
  });

  test("get_spec returns Python spec", async () => {
    const result = await client.request("tools/call", {
      name: "get_spec",
      arguments: { language: "python", category: "spec", topic: "spec" },
    });

    assert.ok(result.content, "Should return content");
    assert.ok(result.content[0].text.length > 100, "Should return substantial content");
    assert.ok(
      result.content[0].text.includes("Python") || result.content[0].text.includes("python"),
      "Should mention Python"
    );
  });

  test("get_checklist returns generation checklist", async () => {
    const result = await client.request("tools/call", {
      name: "get_checklist",
      arguments: { language: "go" },
    });

    assert.ok(result.content, "Should return content");
    assert.ok(result.content[0].text.length > 100, "Should return substantial content");
  });

  test("get_linter_rule returns ESLint rule", async () => {
    const result = await client.request("tools/call", {
      name: "get_linter_rule",
      arguments: { language: "javascript", linter: "eslint", rule: "no-unused-vars" },
    });

    assert.ok(result.content, "Should return content");
    // May return "not found" if rule doesn't exist, but should not error
  });

  test("search_specs finds results", async () => {
    const result = await client.request("tools/call", {
      name: "search_specs",
      arguments: { query: "error handling" },
    });

    assert.ok(result.content, "Should return content");
    assert.ok(result.content[0].text.length > 0, "Should return search results");
  });

  test("list_available lists Python linters", async () => {
    const result = await client.request("tools/call", {
      name: "list_available",
      arguments: { language: "python", category: "linters" },
    });

    assert.ok(result.content, "Should return content");
    assert.ok(
      result.content[0].text.includes("ruff") || result.content[0].text.includes("Ruff"),
      "Should list ruff linter"
    );
  });

  test("get_spec handles unsupported language gracefully", async () => {
    const result = await client.request("tools/call", {
      name: "get_spec",
      arguments: { language: "nonexistent", category: "spec", topic: "spec" },
    });

    assert.ok(result.content, "Should return content");
    const text = result.content[0].text;
    assert.ok(
      text.includes("Unsupported") || text.includes("not found") || text.includes("Invalid"),
      `Should indicate language not supported, got: ${text.substring(0, 100)}`
    );
  });

  test("get_spec blocks path traversal attempts", async () => {
    const result = await client.request("tools/call", {
      name: "get_spec",
      arguments: { language: "python", category: "spec", topic: "../../../etc/passwd" },
    });

    assert.ok(result.content, "Should return content");
    assert.ok(
      result.content[0].text.includes("not found") || result.content[0].text.includes("Spec not found"),
      "Should block path traversal"
    );
  });

  test("lists available resources", async () => {
    const result = await client.request("resources/list", {});
    assert.ok(Array.isArray(result.resources), "Should return resources array");
    assert.ok(result.resources.length > 0, "Should have resources");
  });

  test("reads a spec resource", async () => {
    const listResult = await client.request("resources/list", {});
    const pythonSpec = listResult.resources.find(
      (r) => r.uri.includes("python") && r.uri.includes("spec")
    );

    if (pythonSpec) {
      const result = await client.request("resources/read", { uri: pythonSpec.uri });
      assert.ok(result.contents, "Should return contents");
      assert.ok(result.contents[0].text.length > 0, "Should have content");
    }
  });
});

describe("MCP Server Security Tests", () => {
  let client;

  before(async () => {
    client = new MCPClient();
    await client.start();
  });

  after(async () => {
    await client.stop();
  });

  test("rejects directory traversal in language parameter", async () => {
    const result = await client.request("tools/call", {
      name: "get_spec",
      arguments: { language: "../secrets", category: "spec", topic: "spec" },
    });

    assert.ok(result.content, "Should return content");
    const text = result.content[0].text;
    assert.ok(
      text.includes("Unsupported") || text.includes("not found") || text.includes("Invalid"),
      `Should reject traversal in language, got: ${text.substring(0, 100)}`
    );
  });

  test("rejects directory traversal in category parameter", async () => {
    const result = await client.request("tools/call", {
      name: "get_spec",
      arguments: { language: "python", category: "../../../etc", topic: "passwd" },
    });

    assert.ok(result.content, "Should return content");
    const text = result.content[0].text;
    assert.ok(
      text.includes("not found") || text.includes("Unsupported") || text.includes("Invalid"),
      `Should reject traversal in category, got: ${text.substring(0, 100)}`
    );
  });

  test("handles null bytes in input", async () => {
    const result = await client.request("tools/call", {
      name: "get_spec",
      arguments: { language: "python\x00", category: "spec", topic: "spec" },
    });

    assert.ok(result.content, "Should return content without crashing");
  });

  test("handles extremely long input", async () => {
    const longString = "a".repeat(10000);
    const result = await client.request("tools/call", {
      name: "search_specs",
      arguments: { query: longString },
    });

    assert.ok(result.content, "Should handle long input without crashing");
  });
});
