# SpecForge MCP API Reference

SpecForge MCP exposes 5 tools and a resource-based interface for accessing language specifications.

## Tools

### `get_spec`

Get authoritative language specification, documentation, or style guide.

**Use Case**: Call this BEFORE writing code to ensure correctness. Access language specs, stdlib documentation, patterns, and formatter guides.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `language` | string | Yes | Programming language (see [Supported Languages](#supported-languages)) |
| `category` | string | Yes | Type of documentation: `spec`, `stdlib`, `linters`, `patterns`, `formatters` |
| `topic` | string | Yes | Specific topic (e.g., `error-handling`, `fmt`, `os`) |

**Example**:
```json
{
  "language": "python",
  "category": "stdlib",
  "topic": "asyncio"
}
```

**Response**: Markdown content of the specification.

---

### `get_linter_rule`

Get detailed explanation of a specific linter rule.

**Use Case**: Understand WHY a lint rule exists and HOW to satisfy it. Use when encountering linter errors or configuring linter rules.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `language` | string | Yes | Programming language |
| `linter` | string | Yes | Linter name (e.g., `ruff`, `eslint`, `golangci-lint`) |
| `rule` | string | Yes | Rule identifier (e.g., `E501`, `no-unused-vars`, `errcheck`) |

**Example**:
```json
{
  "language": "python",
  "linter": "ruff",
  "rule": "E501"
}
```

**Response**: Markdown with rule explanation, problematic/correct examples, and configuration options.

---

### `search_specs`

Search across all language specs for a term or concept.

**Use Case**: Find information when you don't know the exact location. Cross-language concept discovery.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search term |
| `allow_fallback` | boolean | No | When `false`, only use search indexes (faster). Default: `true` |

**Example**:
```json
{
  "query": "async await",
  "allow_fallback": false
}
```

**Response**: Up to 10 matching results with context snippets.

---

### `list_available`

List all available specs for a language and category.

**Use Case**: Discover what documentation is available. Browse specs before requesting specific content.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `language` | string | Yes | Programming language |
| `category` | string | No | Category to list. Default: `spec` |

**Example**:
```json
{
  "language": "go",
  "category": "stdlib"
}
```

**Response**: Newline-separated list of available topics.

---

### `get_checklist`

Get the generation checklist for a language.

**Use Case**: Call BEFORE writing code to ensure you follow best practices and avoid common mistakes. Returns critical rules, security guidelines, and anti-patterns.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `language` | string | Yes | Programming language |

**Example**:
```json
{
  "language": "rust"
}
```

**Response**: Markdown checklist with language-specific best practices.

---

## Resources

SpecForge exposes specs as MCP resources with the URI format:

```
spec://{language}/{category}/{name}
```

### Listing Resources

Resources are paginated (default: 250 per page). Configure with `RESOURCE_PAGE_SIZE` environment variable (range: 25-1000).

### Reading Resources

Request a specific resource by URI:
```
spec://python/stdlib/os
spec://typescript/linters/biome/noExplicitAny
spec://go/patterns/error-handling
```

---

## Supported Languages

| Language | ID |
|----------|-----|
| Assembly | `assembly` |
| Bash | `bash` |
| Batch | `batch` |
| BASIC | `basic` |
| C | `c` |
| C++ | `cpp` |
| C# | `csharp` |
| Clojure | `clojure` |
| CSS | `css` |
| Dart | `dart` |
| Dockerfile | `dockerfile` |
| Elixir | `elixir` |
| Git | `git` |
| Go | `go` |
| Haskell | `haskell` |
| HTML | `html` |
| Java | `java` |
| JavaScript | `javascript` |
| Julia | `julia` |
| Kotlin | `kotlin` |
| Lua | `lua` |
| Markdown | `markdown` |
| OCaml | `ocaml` |
| PHP | `php` |
| PowerShell | `powershell` |
| Python | `python` |
| R | `r` |
| Ruby | `ruby` |
| Rust | `rust` |
| Scala | `scala` |
| SQL | `sql` |
| Swift | `swift` |
| TypeScript | `typescript` |
| YAML | `yaml` |
| Zig | `zig` |

---

## Categories

| Category | Description | Example Topics |
|----------|-------------|----------------|
| `spec` | Language specification, syntax, semantics | `spec`, `syntax`, `types` |
| `stdlib` | Standard library documentation | `os`, `fmt`, `json`, `http` |
| `linters` | Linter rules and configuration | `ruff/E501`, `eslint/no-unused-vars` |
| `patterns` | Design patterns and idioms | `error-handling`, `concurrency` |
| `formatters` | Code formatter configuration | `black`, `prettier`, `gofmt` |

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SPECS_DIR` | Path to specs directory | `./specs` |
| `RESOURCE_PAGE_SIZE` | Resources per page (25-1000) | `250` |
| `SEARCH_FALLBACK_STRATEGY` | `scan` or `warn` for missing indexes | `scan` |

---

## Error Handling

Tools return helpful error messages:

- **Invalid language**: `Unsupported language: {language}`
- **Invalid category**: `Unsupported category: {category}`
- **Not found**: `Spec not found: {language}/{category}/{topic}` with list of available specs
- **Empty query**: `Query must be a non-empty string.`

---

## Examples

### Get Python asyncio documentation
```json
{"tool": "get_spec", "arguments": {"language": "python", "category": "stdlib", "topic": "asyncio"}}
```

### Find all Go error handling patterns
```json
{"tool": "search_specs", "arguments": {"query": "error handling go"}}
```

### List TypeScript linter rules
```json
{"tool": "list_available", "arguments": {"language": "typescript", "category": "linters"}}
```

### Get ESLint rule explanation
```json
{"tool": "get_linter_rule", "arguments": {"language": "javascript", "linter": "eslint", "rule": "no-unused-vars"}}
```

### Get Rust best practices checklist
```json
{"tool": "get_checklist", "arguments": {"language": "rust"}}
```
