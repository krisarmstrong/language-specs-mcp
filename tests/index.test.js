import assert from "node:assert/strict";
import { test } from "node:test";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const fixturesDir = join(__dirname, "fixtures", "specs");
process.env.SPECS_DIR = fixturesDir;

const modulePath = new URL("../dist/index.js", import.meta.url);
const {
  getSpec,
  getLinterRule,
  listCategorySpecs,
  searchSpecs,
  resolveSpecPath,
} = await import(modulePath.href);

test("getSpec returns fixture content", async () => {
  const content = await getSpec("go", "spec", "spec");
  assert.match(content, /Go Spec Fixture/);
});

test("getSpec rejects unsupported language", async () => {
  const content = await getSpec("nolang", "spec", "spec");
  assert.match(content, /Unsupported language/);
});

test("getSpec blocks path traversal", async () => {
  const content = await getSpec("go", "spec", "../secret");
  assert.match(content, /Spec not found/);
});

test("getLinterRule returns fixture content", async () => {
  const content = await getLinterRule("go", "golangci-lint", "errcheck");
  assert.match(content, /Fixture linter rule content/);
});

test("listCategorySpecs returns linter entries", async () => {
  const listing = await listCategorySpecs("go", "linters");
  assert.match(listing, /golangci-lint\/errcheck/);
});

test("searchSpecs uses search index when available", async () => {
  const result = await searchSpecs("foobar");
  assert.match(result, /go\/spec\/spec/);
});

test("resolveSpecPath rejects escaping paths", () => {
  const resolved = resolveSpecPath("..", "secrets.md");
  assert.equal(resolved, null);
});
