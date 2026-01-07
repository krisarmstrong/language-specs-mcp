# Scripts Refactor Plan

## Current State

21 Python scripts totaling ~7,800 lines, with `fetch.py` alone at 5,017 lines.

## Problem

`fetch.py` has **35 hardcoded language functions** with embedded URLs and parsing logic. This is:
- Not maintainable
- Not DRY
- Ignores the `sources.json` files we created

## Consolidation Plan

### Scripts to KEEP (as-is)

| Script | Lines | Purpose | Notes |
|--------|-------|---------|-------|
| `_common.py` | 561 | Shared utilities | Core dependency |
| `refresh.py` | 78 | Orchestrator | Clean, simple |
| `doctor.py` | 180 | Health checks | Useful diagnostics |
| `validate-urls.py` | 421 | URL validation | Complex but necessary |
| `fix-urls.py` | 206 | URL fixes | Companion to validate |
| `generate-health.py` | 224 | Dashboard data | Works well |
| `stamp-versions.py` | 127 | Version stamping | Needed for specs |

### Scripts to MERGE

#### 1. Version Scripts → `versions.py`

Merge these 4 scripts into one with subcommands:
- `report-versions.py` (57 lines)
- `update-versions.py` (38 lines)
- `validate-versions.py` (89 lines)

New interface:
```bash
python scripts/versions.py report      # Show versions table
python scripts/versions.py update      # Update from upstream
python scripts/versions.py validate    # Validate against specs
```

#### 2. Generate Scripts → `generate.py`

Merge these 3 scripts:
- `generate-index.py` (112 lines)
- `generate-manifests.py` (67 lines)
- `generate-search-index.py` (79 lines)

New interface:
```bash
python scripts/generate.py index       # Generate specs index
python scripts/generate.py manifests   # Generate provenance
python scripts/generate.py search      # Generate search index
python scripts/generate.py all         # All of the above
```

#### 3. Validate Scripts → `validate.py`

Merge these 2 scripts:
- `validate-freshness.py` (50 lines)
- `validate-stubs.py` (65 lines)

Keep `validate-urls.py` separate (too complex).

New interface:
```bash
python scripts/validate.py freshness   # Check spec freshness
python scripts/validate.py stubs       # Check for stub files
```

#### 4. Diagnostics → Merge into `doctor.py`

Absorb `diagnose-fetch.py` (63 lines) into `doctor.py`:
```bash
python scripts/doctor.py               # Full health check
python scripts/doctor.py --network     # Include network diagnostics
```

### Scripts to REWRITE

#### `fetch.py` + `fetch-parallel.py` → New Data-Driven Fetcher

**Current**: 5,017 + 165 = 5,182 lines
**Target**: ~300 lines

## New Fetch Architecture

### Design Principles

1. **Data-driven**: Read URLs from `sources.json`, not hardcoded
2. **Generic fetchers**: One function per content type, not per language
3. **Parallel by default**: Built-in concurrency
4. **Delta mode**: Only fetch stale specs

### New `fetch.py` Structure

```python
#!/usr/bin/env python3
"""Data-driven spec fetcher."""

from __future__ import annotations
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from _common import fetch_url, write_text, log

SPECS_DIR = Path("specs")

# Content type handlers
FETCHERS = {
    "markdown": fetch_markdown,
    "html": fetch_html_to_markdown,
    "json": fetch_json,
    "raw": fetch_raw,
}


def load_sources(language: str) -> dict:
    """Load sources.json for a language."""
    path = SPECS_DIR / language / "sources.json"
    if not path.exists():
        return {"files": []}
    return json.loads(path.read_text())


def fetch_file(language: str, file_spec: dict) -> bool:
    """Fetch a single file based on its spec."""
    path = file_spec["path"]
    urls = file_spec.get("urls", [])
    content_type = file_spec.get("type", "markdown")

    if not urls:
        return False  # No URLs to fetch

    fetcher = FETCHERS.get(content_type, fetch_raw)

    for url in urls:
        try:
            content = fetcher(url)
            if content:
                output_path = SPECS_DIR / language / path
                output_path.parent.mkdir(parents=True, exist_ok=True)
                write_text(output_path, content)
                return True
        except Exception as e:
            log(f"Failed to fetch {url}: {e}", level="warning")
            continue

    return False


def fetch_language(language: str) -> dict:
    """Fetch all specs for a language."""
    sources = load_sources(language)
    results = {"success": 0, "failed": 0, "skipped": 0}

    for file_spec in sources.get("files", []):
        if not file_spec.get("urls"):
            results["skipped"] += 1
            continue

        if fetch_file(language, file_spec):
            results["success"] += 1
        else:
            results["failed"] += 1

    return results


def main():
    """Fetch all languages in parallel."""
    languages = [d.name for d in SPECS_DIR.iterdir()
                 if d.is_dir() and not d.name.startswith("_")]

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(fetch_language, lang): lang
                   for lang in languages}

        for future in as_completed(futures):
            lang = futures[future]
            result = future.result()
            log(f"{lang}: {result}")


if __name__ == "__main__":
    main()
```

### Key Changes

| Aspect | Old | New |
|--------|-----|-----|
| URLs | Hardcoded in 35 functions | Read from `sources.json` |
| Lines | 5,017 | ~300 |
| Languages | Add new function per language | Add `sources.json` file |
| Fetchers | Per-language logic | Generic by content type |
| Parallelism | Separate script | Built-in |

## Migration Steps

1. **Wait for URL validation** to complete
2. **Merge valid fetch.py URLs** into `sources.json` files
3. **Test new fetcher** on one language
4. **Roll out** to all languages
5. **Delete old fetch.py** once verified
6. **Consolidate other scripts** per plan above

## Scripts After Refactor

| Script | Purpose |
|--------|---------|
| `_common.py` | Shared utilities |
| `fetch.py` | Data-driven fetcher (~300 lines) |
| `refresh.py` | Orchestrator |
| `doctor.py` | Health + network diagnostics |
| `versions.py` | Version management (report/update/validate) |
| `generate.py` | Index/manifest/search generation |
| `validate.py` | Freshness/stubs validation |
| `validate-urls.py` | URL validation (kept separate) |
| `fix-urls.py` | URL auto-fixes |
| `generate-health.py` | Dashboard data |
| `stamp-versions.py` | Version stamping |
| `backfill-stubs.py` | Stub replacement |
| `dashboard.py` | Local dashboard server |

**Before**: 21 scripts, ~7,800 lines
**After**: 13 scripts, ~2,500 lines (estimated)

## Timeline

1. URL validation completes → Review results
2. Decide on URL sources (fetch.py vs sources.json)
3. Implement new data-driven fetch.py
4. Consolidate version/generate/validate scripts
5. Update npm scripts in package.json
6. Test full refresh cycle
7. Clean up old code
