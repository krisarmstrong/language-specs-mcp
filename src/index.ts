import { readdir, readFile, stat } from "node:fs/promises";
import { join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  ReadResourceRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const __dirname = fileURLToPath(new URL(".", import.meta.url));
const SPECS_DIR = join(__dirname, "..", "specs");

interface SpecFile {
  path: string;
  language: string;
  category: string;
  name: string;
}

type SupportedLanguage =
  | "assembly"
  | "basic"
  | "c"
  | "cpp"
  | "csharp"
  | "css"
  | "go"
  | "javascript"
  | "html"
  | "git"
  | "bash"
  | "batch"
  | "sql"
  | "powershell"
  | "java"
  | "kotlin"
  | "lua"
  | "python"
  | "rust"
  | "swift"
  | "typescript";

const LANGUAGES: SupportedLanguage[] = [
  "assembly",
  "basic",
  "bash",
  "batch",
  "c",
  "cpp",
  "csharp",
  "css",
  "go",
  "javascript",
  "html",
  "git",
  "java",
  "kotlin",
  "lua",
  "powershell",
  "python",
  "rust",
  "sql",
  "swift",
  "typescript",
];
const CATEGORIES = ["spec", "stdlib", "linters", "patterns", "formatters"] as const;

async function fileExists(path: string): Promise<boolean> {
  try {
    await stat(path);
    return true;
  } catch {
    return false;
  }
}

async function collectMarkdownFiles(dir: string, files: string[]): Promise<void> {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = join(dir, entry.name);
    if (entry.isDirectory()) {
      await collectMarkdownFiles(fullPath, files);
      continue;
    }
    if (entry.isFile() && entry.name.endsWith(".md")) {
      files.push(fullPath);
    }
  }
}

async function getAllSpecs(): Promise<SpecFile[]> {
  const specs: SpecFile[] = [];

  for (const language of LANGUAGES) {
    const langDir = join(SPECS_DIR, language);
    if (!(await fileExists(langDir))) {
      continue;
    }

    const files: string[] = [];
    await collectMarkdownFiles(langDir, files);

    for (const fullPath of files) {
      const relPath = relative(langDir, fullPath);
      const parts = relPath.split(/[/\\]/);
      const filename = parts[parts.length - 1] ?? "";
      const baseName = filename.replace(".md", "");
      const category = parts.length > 1 ? (parts[0] ?? "spec") : "spec";
      const name = parts.length > 1 ? parts.slice(1).join("/").replace(".md", "") : baseName;

      specs.push({
        path: fullPath,
        language,
        category,
        name,
      });
    }
  }

  return specs;
}

async function searchSpecs(query: string): Promise<string> {
  const specs = await getAllSpecs();
  const results: string[] = [];
  const queryLower = query.toLowerCase();

  for (const spec of specs) {
    try {
      const content = await readFile(spec.path, "utf-8");
      const lines = content.split("\n");
      const matches: string[] = [];

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line?.toLowerCase().includes(queryLower)) {
          const start = Math.max(0, i - 2);
          const end = Math.min(lines.length, i + 3);
          const context = lines.slice(start, end).join("\n");
          matches.push(`Line ${i + 1}:\n${context}`);

          if (matches.length >= 3) {
            break;
          }
        }
      }

      if (matches.length > 0) {
        results.push(
          `## ${spec.language}/${spec.category}/${spec.name}\n\n${matches.join("\n\n---\n\n")}`,
        );
      }
    } catch {}
  }

  if (results.length === 0) {
    return `No results found for: ${query}`;
  }

  return results.slice(0, 10).join("\n\n===\n\n");
}

async function getSpec(language: string, category: string, topic: string): Promise<string> {
  const categories = category === "stdlib" ? [category, "lib"] : [category];
  const possiblePaths = categories.flatMap((cat) => [
    join(SPECS_DIR, language, cat, `${topic}.md`),
    join(SPECS_DIR, language, `${cat}.md`),
    join(SPECS_DIR, language, cat, topic, "index.md"),
  ]);

  for (const path of possiblePaths) {
    if (await fileExists(path)) {
      return await readFile(path, "utf-8");
    }
  }

  const availableSpecs = await listCategorySpecs(language, category);
  return `Spec not found: ${language}/${category}/${topic}\n\nAvailable in ${category}:\n${availableSpecs}`;
}

async function listCategorySpecs(language: string, category: string): Promise<string> {
  const languageDir = join(SPECS_DIR, language);
  const fallbackCategory = category === "stdlib" ? "lib" : "";
  const categoryDir = join(languageDir, category);
  const fallbackDir = fallbackCategory ? join(languageDir, fallbackCategory) : "";

  if (!(await fileExists(categoryDir))) {
    if (category === "spec" && (await fileExists(languageDir))) {
      const entries = await readdir(languageDir, { withFileTypes: true });
      const items = entries
        .filter((e) => e.isFile() && e.name.endsWith(".md"))
        .map((e) => e.name.replace(".md", ""));
      return items.join("\n");
    }
    if (fallbackDir && (await fileExists(fallbackDir))) {
      const files: string[] = [];
      await collectMarkdownFiles(fallbackDir, files);
      const items = files
        .map((filePath) => relative(fallbackDir, filePath).replace(/\.md$/, ""))
        .map((relPath) => relPath.split(/[/\\]/).join("/"));
      return items.join("\n");
    }
    return `Category not found: ${language}/${category}`;
  }

  try {
    const files: string[] = [];
    await collectMarkdownFiles(categoryDir, files);
    const items = files
      .map((filePath) => relative(categoryDir, filePath).replace(/\.md$/, ""))
      .map((relPath) => relPath.split(/[/\\]/).join("/"));
    return items.join("\n");
  } catch {
    return "Unable to list specs";
  }
}

async function getLinterRule(language: string, linter: string, rule: string): Promise<string> {
  const path = join(SPECS_DIR, language, "linters", linter, `${rule}.md`);

  if (await fileExists(path)) {
    return await readFile(path, "utf-8");
  }

  const altPath = join(SPECS_DIR, language, "linters", `${rule}.md`);
  if (await fileExists(altPath)) {
    return await readFile(altPath, "utf-8");
  }

  return `Linter rule not found: ${language}/${linter}/${rule}`;
}

const server = new Server(
  {
    name: "language-specs",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      resources: {},
    },
  },
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "get_spec",
      description:
        "Get authoritative language specification, documentation, or style guide. Use this BEFORE writing code to ensure correctness.",
      inputSchema: {
        type: "object" as const,
        properties: {
          language: {
            type: "string",
            enum: LANGUAGES,
            description: "Programming language",
          },
          category: {
            type: "string",
            enum: CATEGORIES,
            description: "Type of documentation: spec, stdlib, linters, patterns, formatters",
          },
          topic: {
            type: "string",
            description: "Specific topic (e.g., 'error-handling', 'fmt', 'errcheck')",
          },
        },
        required: ["language", "category", "topic"],
      },
    },
    {
      name: "get_linter_rule",
      description:
        "Get detailed explanation of a specific linter rule. Use this when you need to understand WHY a lint rule exists and HOW to satisfy it.",
      inputSchema: {
        type: "object" as const,
        properties: {
          language: {
            type: "string",
            enum: LANGUAGES,
            description: "Programming language",
          },
          linter: {
            type: "string",
            description: "Linter name (e.g., 'golangci-lint', 'biome', 'pylint')",
          },
          rule: {
            type: "string",
            description: "Rule name (e.g., 'errcheck', 'noExplicitAny')",
          },
        },
        required: ["language", "linter", "rule"],
      },
    },
    {
      name: "search_specs",
      description: "Search across all language specs for a term or concept",
      inputSchema: {
        type: "object" as const,
        properties: {
          query: {
            type: "string",
            description: "Search term",
          },
        },
        required: ["query"],
      },
    },
    {
      name: "list_available",
      description: "List all available specs for a language and category",
      inputSchema: {
        type: "object" as const,
        properties: {
          language: {
            type: "string",
            enum: LANGUAGES,
            description: "Programming language",
          },
          category: {
            type: "string",
            enum: CATEGORIES,
            description: "Category to list",
          },
        },
        required: ["language"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  const typedArgs = args as Record<string, string>;

  switch (name) {
    case "get_spec": {
      const content = await getSpec(typedArgs.language, typedArgs.category, typedArgs.topic);
      return { content: [{ type: "text", text: content }] };
    }

    case "get_linter_rule": {
      const content = await getLinterRule(typedArgs.language, typedArgs.linter, typedArgs.rule);
      return { content: [{ type: "text", text: content }] };
    }

    case "search_specs": {
      const content = await searchSpecs(typedArgs.query);
      return { content: [{ type: "text", text: content }] };
    }

    case "list_available": {
      const category = typedArgs.category ?? "spec";
      const content = await listCategorySpecs(typedArgs.language, category);
      return { content: [{ type: "text", text: content }] };
    }

    default:
      return { content: [{ type: "text", text: `Unknown tool: ${name}` }] };
  }
});

server.setRequestHandler(ListResourcesRequestSchema, async () => {
  const specs = await getAllSpecs();
  return {
    resources: specs.map((spec) => ({
      uri: `spec://${spec.language}/${spec.category}/${spec.name}`,
      name: `${spec.language}/${spec.category}/${spec.name}`,
      mimeType: "text/markdown",
    })),
  };
});

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const uri = request.params.uri;
  const match = uri.match(/^spec:\/\/(\w+)\/(\w+)\/(.+)$/);

  if (!match) {
    return { contents: [{ uri, mimeType: "text/plain", text: "Invalid URI format" }] };
  }

  const [, language, category, topic] = match;

  if (!language || !category || !topic) {
    return { contents: [{ uri, mimeType: "text/plain", text: "Invalid URI format" }] };
  }

  const content = await getSpec(language, category, topic);
  return { contents: [{ uri, mimeType: "text/markdown", text: content }] };
});

async function main(): Promise<void> {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Language Specs MCP Server running");
}

main().catch((error: unknown) => {
  console.error("Fatal error:", error);
  process.exit(1);
});
