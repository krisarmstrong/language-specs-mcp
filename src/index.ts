import { readdir, readFile, stat } from "node:fs/promises";
import { join, relative, resolve, sep } from "node:path";
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
const SPECS_DIR = resolve(process.env.SPECS_DIR ?? join(__dirname, "..", "specs"));

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
  | "php"
  | "ruby"
  | "dart"
  | "r"
  | "julia"
  | "scala"
  | "elixir"
  | "clojure"
  | "haskell"
  | "zig"
  | "ocaml"
  | "markdown"
  | "yaml"
  | "dockerfile"
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
  "php",
  "ruby",
  "dart",
  "r",
  "julia",
  "scala",
  "elixir",
  "clojure",
  "haskell",
  "zig",
  "ocaml",
  "markdown",
  "yaml",
  "dockerfile",
  "powershell",
  "python",
  "rust",
  "sql",
  "swift",
  "typescript",
];
const CATEGORIES = ["spec", "stdlib", "linters", "patterns", "formatters"] as const;
const LANGUAGE_SET = new Set<SupportedLanguage>(LANGUAGES);
const CATEGORY_SET = new Set<(typeof CATEGORIES)[number]>(CATEGORIES);
const SPECS_CACHE_TTL_MS = 60_000;
const SEARCH_INDEX_CACHE_TTL_MS = 60_000;

const DEFAULT_RESOURCE_PAGE_SIZE = 250;
const MIN_RESOURCE_PAGE_SIZE = 25;
const MAX_RESOURCE_PAGE_SIZE = 1_000;

function normalizeResourcePageSize(raw?: string): number {
  const parsed = Number.parseInt(raw ?? "", 10);
  if (Number.isNaN(parsed)) {
    return DEFAULT_RESOURCE_PAGE_SIZE;
  }
  return Math.min(MAX_RESOURCE_PAGE_SIZE, Math.max(MIN_RESOURCE_PAGE_SIZE, parsed));
}

const RESOURCE_PAGE_SIZE = normalizeResourcePageSize(process.env.RESOURCE_PAGE_SIZE);

const SEARCH_FALLBACK_STRATEGIES = ["scan", "warn"] as const;
type SearchFallbackStrategy = (typeof SEARCH_FALLBACK_STRATEGIES)[number];

function normalizeSearchFallbackStrategy(raw?: string): SearchFallbackStrategy {
  const candidate = (raw ?? "scan").trim().toLowerCase();
  if ((SEARCH_FALLBACK_STRATEGIES as readonly string[]).includes(candidate)) {
    return candidate as SearchFallbackStrategy;
  }
  console.warn(
    `Invalid SEARCH_FALLBACK_STRATEGY=${raw}; defaulting to "scan". Set to "warn" to skip markdown fallbacks.`,
  );
  return "scan";
}

const SEARCH_FALLBACK_STRATEGY = normalizeSearchFallbackStrategy(
  process.env.SEARCH_FALLBACK_STRATEGY,
);
const SEARCH_FALLBACK_WARN_ONLY = SEARCH_FALLBACK_STRATEGY === "warn";

type SearchIndexEntry = {
  path: string;
  category: string;
  name: string;
  content: string;
};

type SearchIndexFile = {
  language: string;
  generatedAt: string;
  entries: SearchIndexEntry[];
};

type CachedSpecs = {
  items: SpecFile[];
  loadedAt: number;
};

const specsCache: CachedSpecs = {
  items: [],
  loadedAt: 0,
};

type CachedSearchIndex = {
  entries: SearchIndexEntry[];
  loadedAt: number;
};

const searchIndexCache = new Map<string, CachedSearchIndex>();

function isSupportedLanguage(value: string | undefined): value is SupportedLanguage {
  return !!value && LANGUAGE_SET.has(value as SupportedLanguage);
}

function isSupportedCategory(value: string | undefined): value is (typeof CATEGORIES)[number] {
  return !!value && CATEGORY_SET.has(value as (typeof CATEGORIES)[number]);
}

function isNonEmptyString(value: unknown): value is string {
  return typeof value === "string" && value.trim().length > 0;
}

function parseBoolean(value: unknown): boolean | undefined {
  if (typeof value === "boolean") {
    return value;
  }
  if (typeof value === "string") {
    const normalized = value.trim().toLowerCase();
    if (normalized === "true") {
      return true;
    }
    if (normalized === "false") {
      return false;
    }
  }
  return undefined;
}

function parseString(value: unknown): string {
  return typeof value === "string" ? value : "";
}

function hasTraversal(segment: string): boolean {
  return segment.split(/[\\/]+/).some((part) => part === "..");
}

function resolveSpecPath(...segments: string[]): string | null {
  if (segments.some((segment) => segment.includes("\0") || hasTraversal(segment))) {
    return null;
  }
  const resolved = resolve(SPECS_DIR, ...segments);
  if (resolved === SPECS_DIR || resolved.startsWith(`${SPECS_DIR}${sep}`)) {
    return resolved;
  }
  return null;
}

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

async function getAllSpecsCached(): Promise<SpecFile[]> {
  const now = Date.now();
  if (specsCache.items.length > 0 && now - specsCache.loadedAt < SPECS_CACHE_TTL_MS) {
    return specsCache.items;
  }
  const specs = await getAllSpecs();
  specsCache.items = specs;
  specsCache.loadedAt = now;
  return specs;
}

function extractLineMatches(content: string, queryLower: string): string[] {
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

  return matches;
}

async function loadSearchIndex(language: string): Promise<SearchIndexEntry[] | null> {
  const cached = searchIndexCache.get(language);
  const now = Date.now();
  if (cached && now - cached.loadedAt < SEARCH_INDEX_CACHE_TTL_MS) {
    return cached.entries;
  }
  const searchPath = resolveSpecPath(language, "search.json");
  if (!searchPath || !(await fileExists(searchPath))) {
    return null;
  }
  try {
    const raw = await readFile(searchPath, "utf-8");
    const index = JSON.parse(raw) as SearchIndexFile;
    searchIndexCache.set(language, { entries: index.entries, loadedAt: now });
    return index.entries;
  } catch (error) {
    console.error("Search index load failed:", language, error);
    return null;
  }
}

type SearchOptions = {
  allowFallback?: boolean;
};

type SearchContext = {
  queryLower: string;
  allowFallback: boolean;
  results: string[];
  missingIndexLanguages: string[];
  fallbackWarnings: string[];
  fallbackLanguages: Set<string>;
};

function formatSearchResult(
  language: string,
  category: string,
  name: string,
  matches: string[],
): string {
  return `## ${language}/${category}/${name}\n\n${matches.join("\n\n---\n\n")}`;
}

function buildFallbackSummary(warnings: string[]): string {
  return warnings.length ? `Search fallback notes:\n${warnings.join("\n")}` : "";
}

function buildNoResultsMessage(query: string, ctx: SearchContext, fallbackSummary: string): string {
  const warning =
    !ctx.allowFallback && ctx.missingIndexLanguages.length > 0
      ? `\n\nSearch fallback skipped; missing indexes for: ${ctx.missingIndexLanguages.join(", ")}`
      : "";
  const summarySuffix = fallbackSummary ? `\n\n${fallbackSummary}` : "";
  return `No results found for: ${query}${warning}${summarySuffix}`;
}

function buildFinalOutput(ctx: SearchContext, fallbackSummary: string): string {
  let output = ctx.results.slice(0, 10).join("\n\n===\n\n");
  if (!ctx.allowFallback && ctx.missingIndexLanguages.length > 0) {
    output += `\n\n===\n\nSearch fallback skipped; missing indexes for: ${ctx.missingIndexLanguages.join(", ")}`;
  }
  if (fallbackSummary) {
    output += `\n\n===\n\n${fallbackSummary}`;
  }
  return output;
}

async function searchIndexForLanguage(language: string, ctx: SearchContext): Promise<boolean> {
  const entries = await loadSearchIndex(language);
  if (!entries) {
    ctx.missingIndexLanguages.push(language);
    ctx.fallbackLanguages.add(language);
    if (!ctx.allowFallback || SEARCH_FALLBACK_WARN_ONLY) {
      const reason = !ctx.allowFallback
        ? "allow_fallback=false"
        : `SEARCH_FALLBACK_STRATEGY=${SEARCH_FALLBACK_STRATEGY}`;
      ctx.fallbackWarnings.push(
        `Search index missing for ${language}; skipping markdown fallback (${reason}).`,
      );
    }
    return false;
  }
  for (const entry of entries) {
    if (!entry.content.toLowerCase().includes(ctx.queryLower)) continue;
    const matches = extractLineMatches(entry.content, ctx.queryLower);
    if (matches.length === 0) continue;
    ctx.results.push(formatSearchResult(language, entry.category, entry.name, matches));
    if (ctx.results.length >= 10) return true;
  }
  return false;
}

async function searchFallbackSpecs(specs: SpecFile[], ctx: SearchContext): Promise<void> {
  if (!ctx.allowFallback || SEARCH_FALLBACK_WARN_ONLY || ctx.fallbackLanguages.size === 0) return;
  for (const spec of specs) {
    if (!ctx.fallbackLanguages.has(spec.language) || ctx.results.length >= 10) continue;
    try {
      const content = await readFile(spec.path, "utf-8");
      const matches = extractLineMatches(content, ctx.queryLower);
      if (matches.length > 0) {
        ctx.results.push(formatSearchResult(spec.language, spec.category, spec.name, matches));
      }
    } catch (error) {
      console.error("Search read failed:", spec.path, error);
    }
  }
}

async function searchSpecs(query: string, options: SearchOptions = {}): Promise<string> {
  if (!isNonEmptyString(query)) {
    return "Query must be a non-empty string.";
  }
  const ctx: SearchContext = {
    queryLower: query.toLowerCase(),
    allowFallback: options.allowFallback ?? true,
    results: [],
    missingIndexLanguages: [],
    fallbackWarnings: [],
    fallbackLanguages: new Set<string>(),
  };

  for (const language of LANGUAGES) {
    const earlyExit = await searchIndexForLanguage(language, ctx);
    if (earlyExit) return ctx.results.join("\n\n===\n\n");
  }

  const specs = await getAllSpecsCached();
  await searchFallbackSpecs(specs, ctx);

  const fallbackSummary = buildFallbackSummary(ctx.fallbackWarnings);
  if (ctx.results.length === 0) {
    return buildNoResultsMessage(query, ctx, fallbackSummary);
  }
  return buildFinalOutput(ctx, fallbackSummary);
}

async function getSpec(language: string, category: string, topic: string): Promise<string> {
  if (!isSupportedLanguage(language)) {
    return `Unsupported language: ${language}`;
  }
  if (!isSupportedCategory(category)) {
    return `Unsupported category: ${category}`;
  }
  if (!isNonEmptyString(topic)) {
    return "Topic must be a non-empty string.";
  }
  const categories = category === "stdlib" ? [category, "lib"] : [category];
  const allowCategoryRoot = topic === category;
  const possiblePaths = categories.flatMap((cat) => [
    resolveSpecPath(language, cat, `${topic}.md`),
    ...(allowCategoryRoot ? [resolveSpecPath(language, `${cat}.md`)] : []),
    resolveSpecPath(language, cat, topic, "index.md"),
  ]);
  if (category === "spec") {
    possiblePaths.push(resolveSpecPath(language, `${topic}.md`));
  }

  for (const specPath of possiblePaths) {
    if (specPath && (await fileExists(specPath))) {
      return await readFile(specPath, "utf-8");
    }
  }

  const availableSpecs = await listCategorySpecs(language, category);
  return `Spec not found: ${language}/${category}/${topic}\n\nAvailable in ${category}:\n${availableSpecs}`;
}

async function listCategorySpecs(language: string, category: string): Promise<string> {
  if (!isSupportedLanguage(language)) {
    return `Unsupported language: ${language}`;
  }
  if (!isSupportedCategory(category)) {
    return `Unsupported category: ${category}`;
  }
  const languageDir = resolveSpecPath(language);
  if (!languageDir) {
    return `Invalid language path: ${language}`;
  }
  const fallbackCategory = category === "stdlib" ? "lib" : "";
  const categoryDir = resolveSpecPath(language, category);
  const fallbackDir = fallbackCategory ? resolveSpecPath(language, fallbackCategory) : "";

  if (!categoryDir || !(await fileExists(categoryDir))) {
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
  if (!isSupportedLanguage(language)) {
    return `Unsupported language: ${language}`;
  }
  if (!isNonEmptyString(linter) || !isNonEmptyString(rule)) {
    return "Linter and rule must be non-empty strings.";
  }
  const path = resolveSpecPath(language, "linters", linter, `${rule}.md`);

  if (path && (await fileExists(path))) {
    return await readFile(path, "utf-8");
  }

  const altPath = resolveSpecPath(language, "linters", `${rule}.md`);
  if (altPath && (await fileExists(altPath))) {
    return await readFile(altPath, "utf-8");
  }

  return `Linter rule not found: ${language}/${linter}/${rule}`;
}

const server = new Server(
  {
    name: "SpecForge",
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
          allow_fallback: {
            type: "boolean",
            description: "When false, only use search indexes and skip file scanning fallback",
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
  const typedArgs = args as Record<string, unknown>;

  switch (name) {
    case "get_spec": {
      const language = parseString(typedArgs.language);
      const category = parseString(typedArgs.category);
      const topic = parseString(typedArgs.topic);
      if (!isSupportedLanguage(language) || !isSupportedCategory(category)) {
        return {
          content: [
            {
              type: "text",
              text: `Invalid language or category. language=${language}, category=${category}`,
            },
          ],
        };
      }
      const content = await getSpec(language, category, topic);
      return { content: [{ type: "text", text: content }] };
    }

    case "get_linter_rule": {
      const language = parseString(typedArgs.language);
      const linter = parseString(typedArgs.linter);
      const rule = parseString(typedArgs.rule);
      if (!isSupportedLanguage(language)) {
        return {
          content: [
            {
              type: "text",
              text: `Invalid language: ${language}`,
            },
          ],
        };
      }
      const content = await getLinterRule(language, linter, rule);
      return { content: [{ type: "text", text: content }] };
    }

    case "search_specs": {
      const allowFallback = parseBoolean(typedArgs.allow_fallback);
      const content = await searchSpecs(parseString(typedArgs.query), {
        allowFallback,
      });
      return { content: [{ type: "text", text: content }] };
    }

    case "list_available": {
      const language = parseString(typedArgs.language);
      const category = parseString(typedArgs.category) || "spec";
      if (!isSupportedLanguage(language) || !isSupportedCategory(category)) {
        return {
          content: [
            {
              type: "text",
              text: `Invalid language or category. language=${language}, category=${category}`,
            },
          ],
        };
      }
      const content = await listCategorySpecs(language, category);
      return { content: [{ type: "text", text: content }] };
    }

    default:
      return { content: [{ type: "text", text: `Unknown tool: ${name}` }] };
  }
});

server.setRequestHandler(ListResourcesRequestSchema, async (request) => {
  const cursorRaw = request.params?.cursor;
  const cursorValue = Number.parseInt(cursorRaw ?? "0", 10);
  const offset = Number.isFinite(cursorValue) && cursorValue >= 0 ? cursorValue : 0;
  const specs = await getAllSpecsCached();
  const page = specs.slice(offset, offset + RESOURCE_PAGE_SIZE);
  return {
    resources: page.map((spec) => ({
      uri: `spec://${spec.language}/${spec.category}/${spec.name}`,
      name: `${spec.language}/${spec.category}/${spec.name}`,
      mimeType: "text/markdown",
    })),
    nextCursor:
      offset + RESOURCE_PAGE_SIZE < specs.length ? String(offset + RESOURCE_PAGE_SIZE) : undefined,
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

const isEntrypoint =
  !!process.argv[1] && fileURLToPath(import.meta.url) === resolve(process.argv[1]);

if (isEntrypoint) {
  main().catch((error: unknown) => {
    console.error("Fatal error:", error);
    process.exit(1);
  });
}

export {
  getSpec,
  getLinterRule,
  listCategorySpecs,
  searchSpecs,
  resolveSpecPath,
  isSupportedLanguage,
  isSupportedCategory,
};
