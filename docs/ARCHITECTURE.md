# SpecForge MCP Architecture

## System Overview

SpecForge MCP is a Model Context Protocol server that provides LLMs with authoritative language specifications. The system consists of three main components:

```mermaid
flowchart TB
    subgraph "Data Pipeline (Python)"
        F[fetch.py] --> S[specs/]
        G[generate.py] --> I[index.json]
        V[versions.py] --> T[tools/versions.json]
    end

    subgraph "MCP Server (TypeScript)"
        M[index.ts] --> |reads| S
        M --> |reads| I
        M --> |reads| T
    end

    subgraph "Clients"
        C[Claude Desktop]
        CC[Claude Code]
        VS[VS Code]
    end

    C & CC & VS --> |MCP Protocol| M
```

## Component Details

### 1. Data Pipeline (Python)

The data pipeline fetches, transforms, and indexes language specifications.

```mermaid
flowchart LR
    subgraph Sources
        URL1[docs.python.org]
        URL2[eslint.org]
        URL3[rust-lang.org]
    end

    subgraph Pipeline
        SJ[sources.json] --> FP[fetch.py]
        FP --> |HTML/MD| SPEC[spec.md]
        SPEC --> GP[generate.py]
        GP --> IDX[search.json]
    end

    URL1 & URL2 & URL3 --> FP
```

#### Core Scripts

| Script | Purpose | Coverage |
|--------|---------|----------|
| `_common.py` | Shared utilities (fetch, parse, log) | 97% |
| `fetch.py` | Data-driven spec fetcher | 100% |
| `generate.py` | Search index generator | 100% |
| `validate.py` | JSON schema validation | 100% |
| `versions.py` | Tool version management | 100% |

### 2. MCP Server (TypeScript)

Single-file MCP server implementing the Model Context Protocol.

```mermaid
flowchart TB
    subgraph "MCP Server (src/index.ts)"
        LS[ListTools] --> |JSON| CLIENT
        GT[get_spec] --> |Markdown| CLIENT
        GLR[get_linter_rule] --> |Markdown| CLIENT
        SS[search_specs] --> |JSON| CLIENT
        LA[list_available] --> |JSON| CLIENT
    end

    subgraph "Data Layer"
        SPECS[(specs/)]
        IDX[(search.json)]
        VER[(versions.json)]
    end

    GT & GLR --> SPECS
    SS --> IDX
    LA --> SPECS

    CLIENT[MCP Client]
```

#### MCP Tools

| Tool | Input | Output | Use Case |
|------|-------|--------|----------|
| `get_checklist` | language | markdown | Pre-coding rules |
| `get_spec` | language, category, topic | markdown | Spec lookup |
| `get_linter_rule` | language, linter, rule | markdown | Rule explanation |
| `search_specs` | query | JSON array | Cross-spec search |
| `list_available` | language, category | JSON array | Topic discovery |

### 3. Data Structure

```mermaid
graph TD
    subgraph "specs/"
        subgraph "python/"
            PS[spec.md]
            PG[generation-checklist.md]
            subgraph "stdlib/"
                POS[os.md]
                PSYS[sys.md]
            end
            subgraph "linters/ruff/"
                RE001[E001.md]
                RE002[E002.md]
            end
        end
        subgraph "typescript/"
            TS[spec.md]
            TG[generation-checklist.md]
        end
    end

    SRC[sources.json] --> PS & TS
    IDX[search.json] --> PS & TS
```

## Data Flow

### Fetch Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as fetch.py
    participant S as sources.json
    participant W as Web
    participant D as specs/

    U->>F: npm run fetch:python
    F->>S: Read URLs
    S-->>F: [url1, url2, ...]
    loop Each URL
        F->>W: HTTP GET
        W-->>F: HTML/Markdown
        F->>F: Convert to Markdown
        F->>D: Write spec.md
    end
    F->>D: Write .fetched-at
```

### Query Flow

```mermaid
sequenceDiagram
    participant C as Claude
    participant M as MCP Server
    participant S as specs/
    participant I as search.json

    C->>M: get_spec(python, stdlib, os)
    M->>S: Read specs/python/stdlib/os.md
    S-->>M: Markdown content
    M-->>C: Formatted response

    C->>M: search_specs("error handling")
    M->>I: Search index
    I-->>M: Matching files
    M->>S: Read matched files
    S-->>M: Content snippets
    M-->>C: Search results
```

## Security Model

```mermaid
flowchart TB
    subgraph "Input Validation"
        PATH[Path Traversal Check]
        NULL[Null Byte Filter]
        LANG[Language Whitelist]
    end

    REQ[User Request] --> PATH
    PATH --> NULL
    NULL --> LANG
    LANG --> |Valid| RESOLVE[resolveSpecPath]
    LANG --> |Invalid| REJECT[Reject]
    RESOLVE --> |Safe Path| READ[Read File]
    RESOLVE --> |Escape Attempt| REJECT
```

## Deployment

### Local Development

```bash
git clone https://github.com/krisarmstrong/language-specs-mcp.git
cd language-specs-mcp
npm install
npm run build
npm run refresh
npm test
```

### Production (Claude Desktop)

```json
{
  "mcpServers": {
    "SpecForge": {
      "command": "node",
      "args": ["/path/to/specforge-mcp/dist/index.js"]
    }
  }
}
```

## Performance Considerations

| Metric | Value | Notes |
|--------|-------|-------|
| Startup time | <100ms | Lazy loading of specs |
| Query latency | <10ms | File system cache |
| Memory usage | ~50MB | Index in memory |
| Spec count | 8,600+ files | 35 languages |

## Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Runtime | Node.js | 20+ |
| MCP SDK | @modelcontextprotocol/sdk | latest |
| Data Pipeline | Python | 3.11+ |
| Linting (Python) | ruff | latest |
| Linting (TypeScript) | biome | latest |
| Testing | pytest, node:test | - |

## Quality Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Core Test Coverage | 95%+ | 97%+ |
| Linting Errors | 0 | 0 |
| URL Validity | 99%+ | 99.6% |
| Response Time | <50ms | <10ms |
