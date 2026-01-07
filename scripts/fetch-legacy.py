#!/usr/bin/env python3
"""Fetch language specs and tooling references."""

from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

from _common import (
    FetchError,
    SPECS_DIR,
    _simple_html_to_markdown,
    extract_main,
    fetch_bytes,
    fetch_markdown_or_html,
    fetch_markdown,
    fetch_section,
    fetch_url,
    find_unique,
    join_lines,
    log,
    stamp_versions,
    write_fetched_at,
    write_stub,
    write_template,
    write_text,
)


def _extract_markdown_table(markdown: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        code, description = cells[0], cells[1]
        if code and description:
            entries.setdefault(code, description)
    return entries


def _extract_markdown_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            if current and buffer:
                sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
            continue
        if current:
            if line.strip():
                buffer.append(line)
    if current and buffer:
        sections[current] = "\n".join(buffer).strip()
    return sections


def _extract_golangci_lint_descriptions(
    html_text: str, linter_names: list[str]
) -> dict[str, str]:
    cleaned = re.sub(r"<(script|style)[^>]*>.*?</\\1>", " ", html_text, flags=re.I | re.S)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    cleaned = html.unescape(cleaned)
    cleaned = re.sub(r"\\s+", " ", cleaned).strip()
    marker = cleaned.find("All Linters")
    if marker != -1:
        cleaned = cleaned[marker:]

    if not linter_names:
        return {}

    pattern = re.compile(r"\\b(" + "|".join(re.escape(name) for name in linter_names) + r")\\b")
    matches = [(match.start(), match.group(1)) for match in pattern.finditer(cleaned)]
    matches.sort()

    seen: set[str] = set()
    ordered: list[tuple[int, str]] = []
    for position, name in matches:
        if name in seen:
            continue
        seen.add(name)
        ordered.append((position, name))

    descriptions: dict[str, str] = {}
    for idx, (position, name) in enumerate(ordered):
        next_position = ordered[idx + 1][0] if idx + 1 < len(ordered) else len(cleaned)
        section = cleaned[position + len(name) : next_position].strip()
        if section.lower().startswith(name.lower()):
            section = section[len(name) :].strip()
        if section:
            descriptions[name] = section
    return descriptions


def fetch_assembly() -> None:
    specs_dir = SPECS_DIR / "assembly"
    log("=== Fetching Assembly Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching x86-64 instruction reference...")
        fetch_markdown(
            "https://www.felixcloutier.com/x86/",
            specs_dir / "x86-64.md",
            "x86-64 Instruction Set Reference",
        )

        log("Fetching AArch64 (ARMv8-A) reference...")
        fetch_markdown(
            "https://developer.arm.com/documentation/ddi0487/latest",
            specs_dir / "aarch64.md",
            "AArch64 Architecture Reference Manual (ARMv8-A)",
        )

        log("Fetching ARM32 (ARMv7-A) reference...")
        fetch_markdown(
            "https://developer.arm.com/documentation/ddi0406/latest",
            specs_dir / "arm32.md",
            "ARM Architecture Reference Manual (ARMv7-A)",
        )

        log("Fetching RISC-V specification...")
        fetch_markdown(
            "https://riscv.org/technical/specifications/",
            specs_dir / "riscv.md",
            "RISC-V Specifications",
        )

        log("Fetching WebAssembly core spec...")
        fetch_markdown(
            "https://webassembly.github.io/spec/core/",
            specs_dir / "wasm.md",
            "WebAssembly Core Specification",
        )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Assembly ABI and Platform References",
                    "",
                    "Assembly has no standard library, but ABI and calling convention references are essential.",
                    "",
                    "## System V AMD64 ABI (Linux/macOS)",
                    "",
                    "See: https://refspecs.linuxfoundation.org/elf/x86_64-abi-0.99.pdf",
                    "",
                    "## Microsoft x64 Calling Convention",
                    "",
                    "See: https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention",
                ]
            ),
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Assembly Linting",
                    "",
                    "There is no widely adopted, language-agnostic linter for assembly.",
                    "",
                    "## Recommendations",
                    "",
                    "- Enable strict warnings in your assembler (NASM/YASM/GAS/LLVM).",
                    "- Use disassemblers and static analysis tools for verification.",
                    "- Consider formatters like asmfmt for consistent style.",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Assembly Idioms",
                    "",
                    "## Follow the ABI",
                    "",
                    "- Preserve callee-saved registers.",
                    "- Keep the stack aligned per ABI requirements.",
                    "- Use the correct calling convention for the platform.",
                    "",
                    "## Prefer Clear Register Usage",
                    "",
                    "- Minimize register aliasing.",
                    "- Use comments to document register roles in non-trivial routines.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Assembly Formatters",
                    "",
                    "There is no widely adopted formatter for assembly across architectures.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Assembly specs complete ===")

def fetch_javascript() -> None:
    specs_dir = SPECS_DIR / "javascript"
    log("=== Fetching JavaScript Specs ===")
    for subdir in [
        "stdlib/node",
        "stdlib/web",
        "linters/eslint",
        "linters/standardjs",
        "linters/xo",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching ECMAScript spec...")
        fetch_markdown(
            "https://tc39.es/ecma262/",
            specs_dir / "spec.md",
            "ECMAScript Language Specification",
        )

    if fetch_section("stdlib"):
        log("Fetching JavaScript reference...")
        fetch_markdown(
            "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference",
            specs_dir / "stdlib" / "overview.md",
            "JavaScript Reference",
        )

        log("Fetching Web API overview...")
        fetch_markdown(
            "https://developer.mozilla.org/en-US/docs/Web/API",
            specs_dir / "stdlib" / "web" / "overview.md",
            "Web API Reference",
        )

        try:
            web_html = fetch_url("https://developer.mozilla.org/en-US/docs/Web/API")
            web_apis = find_unique(web_html, r"/Web/API/([A-Za-z0-9_%-]+)")
        except FetchError as exc:
            log(f"Failed to fetch Web API list: {exc}")
            web_apis = []

        web_api_overrides = {
            "contributors": join_lines(
                [
                    "# contributors",
                    "",
                    "This MDN page lists contributors to the Web API documentation, not a Web API surface.",
                    "",
                    "Source: https://developer.mozilla.org/en-US/docs/Web/API/contributors",
                ]
            ),
        }

        for api in web_apis:
            log(f"  - web/{api}")
            override = web_api_overrides.get(api)
            if override:
                write_text(specs_dir / "stdlib" / "web" / f"{api}.md", override)
                continue
            fetch_markdown(
                f"https://developer.mozilla.org/en-US/docs/Web/API/{api}",
                specs_dir / "stdlib" / "web" / f"{api}.md",
                api,
            )

        log("Fetching Node.js API index...")
        fetch_markdown(
            "https://nodejs.org/api/",
            specs_dir / "stdlib" / "node" / "overview.md",
            "Node.js API Reference",
        )

        try:
            node_html = fetch_url("https://nodejs.org/api/")
            node_modules = find_unique(node_html, r'href="([a-zA-Z0-9_-]+)\\.html"')
        except FetchError as exc:
            log(f"Failed to fetch Node.js module list: {exc}")
            node_modules = []

        for mod in node_modules:
            log(f"  - node/{mod}")
            fetch_markdown(
                f"https://nodejs.org/api/{mod}.html",
                specs_dir / "stdlib" / "node" / f"{mod}.md",
                f"Node.js {mod} Module",
            )

    if fetch_section("linters"):
        log("Fetching ESLint rules...")
        fetch_markdown(
            "https://eslint.org/docs/latest/rules/",
            specs_dir / "linters" / "eslint" / "overview.md",
            "ESLint Rules",
        )

        try:
            eslint_html = fetch_url("https://eslint.org/docs/latest/rules/")
            eslint_rules = find_unique(eslint_html, r"/docs/latest/rules/([a-zA-Z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch ESLint rule list: {exc}")
            eslint_rules = []

        for rule in eslint_rules:
            log(f"  - eslint/{rule}")
            fetch_markdown(
                f"https://eslint.org/docs/latest/rules/{rule}",
                specs_dir / "linters" / "eslint" / f"{rule}.md",
                rule,
            )

        fetch_markdown(
            "https://standardjs.com/rules.html",
            specs_dir / "linters" / "standardjs" / "overview.md",
            "JavaScript Standard Style Rules",
        )
        try:
            standard_html = fetch_url("https://standardjs.com/rules.html")
            standard_rules = find_unique(standard_html, r"#([a-z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch StandardJS rules: {exc}")
            standard_rules = []

        for rule in standard_rules:
            if rule == "rules":
                continue
            log(f"  - standardjs/{rule}")
            fetch_markdown(
                f"https://standardjs.com/rules.html#{rule}",
                specs_dir / "linters" / "standardjs" / f"{rule}.md",
                rule,
            )

        fetch_markdown(
            "https://github.com/xojs/xo",
            specs_dir / "linters" / "xo" / "overview.md",
            "XO Rules",
        )
        try:
            xo_config = fetch_url(
                "https://raw.githubusercontent.com/xojs/eslint-config-xo/main/index.js"
            )
            xo_rules = find_unique(
                xo_config, r"['\"]([a-z][a-z0-9-]+(?:/[a-z0-9-]+)?)['\"]\\s*:"
            )
        except FetchError as exc:
            log(f"Failed to fetch XO rules: {exc}")
            xo_rules = []

        plugin_docs = {
            "unicorn": "https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/{name}.md",
            "import": "https://github.com/import-js/eslint-plugin-import/blob/main/docs/rules/{name}.md",
            "n": "https://github.com/eslint-community/eslint-plugin-n/blob/master/docs/rules/{name}.md",
            "promise": "https://github.com/eslint-community/eslint-plugin-promise/blob/master/docs/rules/{name}.md",
            "ava": "https://github.com/avajs/eslint-plugin-ava/blob/main/docs/rules/{name}.md",
        }

        for rule in xo_rules:
            if rule in {"rules", "overrides", "env", "parserOptions", "settings", "plugins", "extends"}:
                continue
            log(f"  - xo/{rule}")
            if "/" in rule:
                prefix, name = rule.split("/", 1)
                doc_url = plugin_docs.get(prefix)
                if doc_url:
                    url = doc_url.format(name=name)
                else:
                    url = "https://github.com/xojs/xo"
            else:
                url = f"https://eslint.org/docs/latest/rules/{rule}"
            fetch_markdown(
                url,
                specs_dir / "linters" / "xo" / f"{rule}.md",
                rule,
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# JavaScript Formatters",
                    "",
                    "JavaScript formatting typically uses Prettier or Biome. Both format JS/TS/JSON and support modern syntax.",
                    "",
                    "## Prettier",
                    "- Opinionated formatting with broad ecosystem support.",
                    "",
                    "## Biome Format",
                    "- Fast formatter with integrated linting for JS/TS/JSON/CSS.",
                ]
            ),
        )
        fetch_markdown(
            "https://prettier.io/docs/en/options.html",
            specs_dir / "formatters" / "prettier.md",
            "Prettier Options",
        )
        fetch_markdown(
            "https://biomejs.dev/formatter/",
            specs_dir / "formatters" / "biome.md",
            "Biome Formatter Options",
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# JavaScript Idioms",
                    "",
                    "## Prefer const/let over var",
                    "",
                    "```javascript",
                    'const id = "abc";',
                    "let count = 0;",
                    "```",
                    "",
                    "## Use async/await for async control flow",
                    "",
                    "```javascript",
                    "const data = await fetch(url).then((res) => res.json());",
                    "```",
                    "",
                    "## Avoid implicit globals",
                    "",
                    "```javascript",
                    '"use strict";',
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== JavaScript specs complete ===")


def fetch_typescript() -> None:
    specs_dir = SPECS_DIR / "typescript"
    log("=== Fetching TypeScript Specs ===")
    for subdir in ["lib", "linters/biome", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching TypeScript handbook...")
        handbook_pages = [
            "basic-types",
            "interfaces",
            "functions",
            "classes",
            "generics",
            "enums",
            "type-inference",
            "type-compatibility",
        ]
        for page in handbook_pages:
            log(f"  - {page}")
            fetch_markdown(
                f"https://www.typescriptlang.org/docs/handbook/{page}.html",
                specs_dir / "lib" / f"{page}.md",
                page,
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# TypeScript Idiomatic Patterns",
                    "",
                    "## Use explicit types for function signatures",
                    "",
                    "```typescript",
                    "// BAD",
                    "function process(data) {",
                    "  return data.map(x => x.value);",
                    "}",
                    "",
                    "// GOOD",
                    "function process(data: Item[]): string[] {",
                    "  return data.map((x) => x.value);",
                    "}",
                    "```",
                    "",
                    "## Never use `any`",
                    "",
                    "```typescript",
                    "// BAD",
                    "const data: any = response.body;",
                    "",
                    "// GOOD",
                    "interface ResponseBody {",
                    "  items: Item[];",
                    "  total: number;",
                    "}",
                    "const data: ResponseBody = response.body;",
                    "",
                    "// If truly unknown, use `unknown` and narrow",
                    "const data: unknown = response.body;",
                    "if (isResponseBody(data)) {",
                    "  // data is now ResponseBody",
                    "}",
                    "```",
                    "",
                    "## Use `readonly` for immutable data",
                    "",
                    "```typescript",
                    "interface Config {",
                    "  readonly apiUrl: string;",
                    "  readonly timeout: number;",
                    "}",
                    "```",
                    "",
                    "## Prefer interfaces over type aliases for objects",
                    "",
                    "```typescript",
                    "// Prefer",
                    "interface User {",
                    "  id: string;",
                    "  name: string;",
                    "}",
                    "",
                    "// Over",
                    "type User = {",
                    "  id: string;",
                    "  name: string;",
                    "};",
                    "```",
                    "",
                    "## Use discriminated unions",
                    "",
                    "```typescript",
                    "interface Success {",
                    '  kind: "success";',
                    "  data: Data;",
                    "}",
                    "",
                    "interface Failure {",
                    '  kind: "failure";',
                    "  error: Error;",
                    "}",
                    "",
                    "type Result = Success | Failure;",
                    "",
                    "function handle(result: Result) {",
                    "  switch (result.kind) {",
                    '    case "success":',
                    "      return result.data;",
                    '    case "failure":',
                    "      throw result.error;",
                    "  }",
                    "}",
                    "```",
                    "",
                    "## Use `satisfies` for type checking without widening",
                    "",
                    "```typescript",
                    "const config = {",
                    '  apiUrl: "https://api.example.com",',
                    "  timeout: 5000,",
                    "} satisfies Config;",
                    "```",
                    "",
                    "## Prefer `for...of` over `forEach`",
                    "",
                    "```typescript",
                    "// BAD - can't break, can't await properly",
                    "items.forEach((item) => {",
                    "  process(item);",
                    "});",
                    "",
                    "// GOOD",
                    "for (const item of items) {",
                    "  await process(item);",
                    "}",
                    "```",
                    "",
                    "## Use type guards",
                    "",
                    "```typescript",
                    "function isString(value: unknown): value is string {",
                    '  return typeof value === "string";',
                    "}",
                    "",
                    "function isUser(value: unknown): value is User {",
                    "  return (",
                    '    typeof value === "object" &&',
                    "    value !== null &&",
                    '    "id" in value &&',
                    '    "name" in value',
                    "  );",
                    "}",
                    "```",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# TypeScript Formatters",
                    "",
                    "## Prettier",
                    "",
                    "See: https://prettier.io/docs/en/",
                    "",
                    "## Biome Format",
                    "",
                    "See: https://biomejs.dev/formatter/",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "prettier.md",
            join_lines(
                [
                    "# Prettier Options",
                    "",
                    "See: https://prettier.io/docs/en/options.html",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "biome.md",
            join_lines(
                [
                    "# Biome Formatter Options",
                    "",
                    "See: https://biomejs.dev/formatter/",
                ]
            ),
        )

    if fetch_section("linters"):
        log("Fetching Biome rule docs...")
        write_text(
            specs_dir / "linters" / "biome" / "overview.md",
            join_lines(
                [
                    "# Biome Linter - Complete Rules Reference",
                    "",
                    "**Source:** https://biomejs.dev/linter/",
                    "",
                    "Biome is a fast formatter and linter for JavaScript, TypeScript, JSX, JSON, CSS.",
                    "",
                    "## Rule Categories",
                    "",
                    "| Category | Purpose |",
                    "|----------|---------|",
                    "| correctness | Prevent bugs and incorrect behavior |",
                    "| suspicious | Potentially problematic patterns |",
                    "| style | Code style consistency |",
                    "| complexity | Reduce cognitive complexity |",
                    "| performance | Optimize runtime performance |",
                    "| security | Prevent security vulnerabilities |",
                    "| a11y | Accessibility in JSX |",
                    "| nursery | Experimental rules |",
                    "",
                    "## Severity Levels",
                    "",
                    "- `error`: Fails CI, must fix",
                    "- `warn`: Warning, should fix",
                    "- `off`: Disabled",
                    "",
                    "## Configuration",
                    "",
                    "```json",
                    "{",
                    '  "$schema": "https://biomejs.dev/schemas/2.3.10/schema.json",',
                    '  "linter": {',
                    '    "enabled": true,',
                    '    "rules": {',
                    '      "recommended": true,',
                    '      "correctness": {',
                    '        "noUnusedVariables": "error"',
                    "      }",
                    "    }",
                    "  }",
                    "}",
                    "```",
                ]
            ),
        )

        write_text(
            specs_dir / "linters" / "biome" / "noExplicitAny.md",
            join_lines(
                [
                    "# noExplicitAny",
                    "",
                    "Disallow the `any` type usage.",
                    "",
                    "## Why",
                    "",
                    "The `any` type disables type checking and should be avoided.",
                    "",
                    "## Invalid",
                    "",
                    "```typescript",
                    "let x: any;",
                    "function fn(param: any): any {}",
                    "```",
                    "",
                    "## Valid",
                    "",
                    "```typescript",
                    "let x: unknown;",
                    "function fn(param: unknown): string {}",
                    "```",
                    "",
                    "## Fix",
                    "",
                    "1. Use a specific type if known",
                    "2. Use `unknown` and narrow with type guards",
                    "3. Use generics for flexible typing",
                ]
            ),
        )

        write_text(
            specs_dir / "linters" / "biome" / "noNonNullAssertion.md",
            join_lines(
                [
                    "# noNonNullAssertion",
                    "",
                    "Disallow non-null assertions using the `!` postfix operator.",
                    "",
                    "## Why",
                    "",
                    "Non-null assertions bypass TypeScript's strict null checks and can cause runtime errors.",
                    "",
                    "## Invalid",
                    "",
                    "```typescript",
                    "const value = maybeNull!;",
                    "obj.property!.method();",
                    "```",
                    "",
                    "## Valid",
                    "",
                    "```typescript",
                    "if (maybeNull !== null) {",
                    "  const value = maybeNull;",
                    "}",
                    "",
                    "// Or use optional chaining",
                    "obj.property?.method();",
                    "```",
                ]
            ),
        )

        write_text(
            specs_dir / "linters" / "biome" / "schema.md",
            join_lines(
                [
                    "# Biome Schema Reference",
                    "",
                    "Latest schema:",
                    "",
                    "https://biomejs.dev/schemas/2.3.10/schema.json",
                ]
            ),
        )

        try:
            biome_html = fetch_url("https://biomejs.dev/linter/")
            biome_rules = find_unique(biome_html, r"/linter/rules/([a-z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch Biome rule list: {exc}")
            biome_rules = []

        for rule in biome_rules:
            log(f"  - biome/{rule}")
            fetch_markdown(
                f"https://biomejs.dev/linter/rules/{rule}",
                specs_dir / "linters" / "biome" / f"{rule}.md",
                rule,
            )

        write_text(
            specs_dir / "linters" / "biome" / "noUnusedVariables.md",
            join_lines(
                [
                    "# noUnusedVariables",
                    "",
                    "Disallow unused variables.",
                    "",
                    "## Why",
                    "",
                    "Unused variables are dead code and should be removed.",
                    "",
                    "## Invalid",
                    "",
                    "```typescript",
                    "const unused = 5;",
                    "",
                    "function fn(unusedParam: string) {",
                    '  return "hello";',
                    "}",
                    "```",
                    "",
                    "## Valid",
                    "",
                    "```typescript",
                    "const used = 5;",
                    "console.info(used);",
                    "",
                    "function fn(_ignoredParam: string) {",
                    '  return "hello";',
                    "}",
                    "```",
                    "",
                    "## Note",
                    "",
                    "Prefix with underscore `_` to indicate intentionally unused.",
                ]
            ),
        )

        write_text(
            specs_dir / "linters" / "biome" / "noConsole.md",
            join_lines(
                [
                    "# noConsole",
                    "",
                    "Disallow the use of `console`.",
                    "",
                    "## Why",
                    "",
                    "Console statements are typically used for debugging and should not be in production code.",
                    "",
                    "## Invalid",
                    "",
                    "```typescript",
                    'console.log("debug");',
                    "```",
                    "",
                    "## Valid",
                    "",
                    "```typescript",
                    'console.error("Error occurred");',
                    'console.warn("Warning");',
                    'console.info("Info message");',
                    "",
                    "// Or use a proper logger",
                    'logger.debug("debug");',
                    "```",
                    "",
                    "## Configuration",
                    "",
                    "Allow specific methods:",
                    "",
                    "```json",
                    "{",
                    '  "noConsole": {',
                    '    "level": "warn",',
                    '    "options": {',
                    '      "allow": ["warn", "error", "info", "debug"]',
                    "    }",
                    "  }",
                    "}",
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== TypeScript specs complete ===")


def fetch_go() -> None:
    specs_dir = SPECS_DIR / "go"
    log("=== Fetching Go Specs ===")
    for subdir in ["stdlib", "linters/golangci-lint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Go spec...")
        fetch_markdown_or_html(
            "https://go.dev/ref/spec",
            specs_dir / "spec.md",
            specs_dir / "spec.html",
            "Go Language Specification",
        )

    if fetch_section("patterns"):
        log("Fetching Effective Go...")
        fetch_markdown_or_html(
            "https://go.dev/doc/effective_go",
            specs_dir / "effective-go.md",
            specs_dir / "effective-go.html",
            "Effective Go",
        )
        write_text(
            specs_dir / "patterns" / "proverbs.md",
            join_lines(
                [
                    "# Go Proverbs",
                    "",
                    "By Rob Pike",
                    "",
                    "- Don't communicate by sharing memory, share memory by communicating.",
                    "- Concurrency is not parallelism.",
                    "- Channels orchestrate; mutexes serialize.",
                    "- The bigger the interface, the weaker the abstraction.",
                    "- Make the zero value useful.",
                    "- interface{} says nothing.",
                    "- Gofmt's style is no one's favorite, yet gofmt is everyone's favorite.",
                    "- A little copying is better than a little dependency.",
                    "- Syscall must always be guarded with build tags.",
                    "- Cgo must always be guarded with build tags.",
                    "- Cgo is not Go.",
                    "- With the unsafe package there are no guarantees.",
                    "- Clear is better than clever.",
                    "- Reflection is never clear.",
                    "- Errors are values.",
                    "- Don't just check errors, handle them gracefully.",
                    "- Design the architecture, name the components, document the details.",
                    "- Documentation is for users.",
                    "- Don't panic.",
                ]
            ),
        )
        write_text(
            specs_dir / "patterns" / "error-handling.md",
            join_lines(
                [
                    "# Go Error Handling Patterns",
                    "",
                    "## Basic Pattern",
                    "",
                    "```go",
                    "result, err := doSomething()",
                    "if err != nil {",
                    '    return fmt.Errorf("doing something: %w", err)',
                    "}",
                    "```",
                    "",
                    "## NEVER ignore errors",
                    "",
                    "```go",
                    "// BAD - fails errcheck",
                    "result, _ := doSomething()",
                    "",
                    "// GOOD",
                    "result, err := doSomething()",
                    "if err != nil {",
                    "    return err",
                    "}",
                    "```",
                    "",
                    "## Error wrapping (Go 1.13+)",
                    "",
                    "```go",
                    "// Wrap with context",
                    "if err != nil {",
                    '    return fmt.Errorf("failed to process %s: %w", name, err)',
                    "}",
                    "",
                    "// Check wrapped errors",
                    "if errors.Is(err, os.ErrNotExist) {",
                    "    // handle not found",
                    "}",
                    "",
                    "// Type assert wrapped errors",
                    "var pathErr *os.PathError",
                    "if errors.As(err, &pathErr) {",
                    "    // handle path error",
                    "}",
                    "```",
                    "",
                    "## Sentinel errors",
                    "",
                    "```go",
                    "// Define at package level",
                    'var ErrNotFound = errors.New("not found")',
                    "",
                    "// Use errors.Is to check",
                    "if errors.Is(err, ErrNotFound) {",
                    "    // handle",
                    "}",
                    "```",
                    "",
                    "## Custom error types",
                    "",
                    "```go",
                    "type ValidationError struct {",
                    "    Field string",
                    "    Msg   string",
                    "}",
                    "",
                    "func (e *ValidationError) Error() string {",
                    '    return fmt.Sprintf("%s: %s", e.Field, e.Msg)',
                    "}",
                    "```",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Go Formatters",
                    "",
                    "Go formatting is centered on `gofmt`, with additional tools for imports and line wrapping.",
                    "",
                    "## gofmt",
                    "- Canonical formatter shipped with Go.",
                    "",
                    "## goimports",
                    "- Formats and fixes imports to match standard layout.",
                    "",
                    "## gofumpt",
                    "- Stricter `gofmt` with additional style rules.",
                    "",
                    "## golines",
                    "- Wraps long lines to configured widths.",
                ]
            ),
        )
        fetch_markdown(
            "https://pkg.go.dev/cmd/gofmt",
            specs_dir / "formatters" / "gofmt.md",
            "gofmt Options",
        )
        fetch_markdown(
            "https://pkg.go.dev/golang.org/x/tools/cmd/goimports",
            specs_dir / "formatters" / "goimports.md",
            "goimports Options",
        )
        fetch_markdown(
            "https://github.com/mvdan/gofumpt",
            specs_dir / "formatters" / "gofumpt.md",
            "gofumpt Options",
        )
        fetch_markdown(
            "https://github.com/segmentio/golines",
            specs_dir / "formatters" / "golines.md",
            "golines Options",
        )

    if fetch_section("stdlib"):
        log("Fetching stdlib docs...")
        stdlib_packages: list[str]
        try:
            completed = subprocess.run(
                ["go", "list", "std"],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
            )
            stdlib_packages = [line for line in completed.stdout.splitlines() if line.strip()]
        except OSError:
            stdlib_packages = []
        if not stdlib_packages:
            stdlib_packages = [
                "fmt",
                "errors",
                "io",
                "os",
                "net/http",
                "encoding/json",
                "context",
                "sync",
                "time",
                "strings",
                "bytes",
            ]

        for package in stdlib_packages:
            filename = package.replace("/", "-")
            log(f"  - {package}")
            output = specs_dir / "stdlib" / f"{filename}.md"
            try:
                completed = subprocess.run(
                    ["go", "doc", "-all", package],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.DEVNULL,
                    text=True,
                )
                write_text(output, completed.stdout)
            except (OSError, subprocess.SubprocessError):
                log("    (skipped)")

    if fetch_section("linters"):
        log("Fetching golangci-lint rule docs...")
        config_url = (
            "https://raw.githubusercontent.com/maratori/golangci-lint-config/main/.golangci.yml"
        )
        config_path = SPECS_DIR.parent / ".golangci.yml"

        if not config_path.exists():
            try:
                config_path.write_text(fetch_url(config_url), encoding="utf-8")
            except FetchError:
                config_path.write_text("", encoding="utf-8")

        enabled_rules: list[str] = []
        optional_rules: list[str] = []
        disabled_rules: list[str] = []
        section = "enabled"
        in_linters = False
        in_enable = False

        for raw_line in config_path.read_text(encoding="utf-8").splitlines():
            trimmed = raw_line.lstrip()
            if trimmed == "linters:":
                in_linters = True
                continue
            if in_linters and trimmed == "enable:":
                in_enable = True
                continue
            if in_enable and trimmed == "settings:":
                break
            if not in_enable:
                continue
            if trimmed.startswith("## ") and "you may want to enable" in trimmed:
                section = "optional"
                continue
            if trimmed.startswith("## ") and "disabled" in trimmed:
                section = "disabled"
                continue
            if trimmed.startswith("- "):
                name = trimmed[2:].strip().split()[0]
                if section == "enabled":
                    enabled_rules.append(name)
                elif section == "optional":
                    optional_rules.append(name)
                else:
                    disabled_rules.append(name)
            elif trimmed.startswith("#-"):
                name = trimmed[2:].strip().split()[0]
                if section == "disabled":
                    disabled_rules.append(name)
                else:
                    optional_rules.append(name)

        all_rules = sorted({*enabled_rules, *optional_rules, *disabled_rules, "embeddedstructfieldcheck"})

        linter_index_url = "https://golangci-lint.run/docs/linters/"
        linter_descriptions: dict[str, str] = {}
        try:
            linter_html = fetch_url(linter_index_url)
            linter_descriptions = _extract_golangci_lint_descriptions(linter_html, all_rules)
        except FetchError as exc:
            log(f"Failed to fetch golangci-lint index: {exc}")

        for rule in all_rules:
            log(f"  - {rule}")
            description = linter_descriptions.get(rule, "").strip()
            if description:
                write_text(
                    specs_dir / "linters" / "golangci-lint" / f"{rule}.md",
                    join_lines(
                        [
                            f"# {rule}",
                            "",
                            description,
                            "",
                            f"Source: {linter_index_url}#{rule}",
                        ]
                    ),
                )
            else:
                fetch_markdown(
                    f"{linter_index_url}#{rule}",
                    specs_dir / "linters" / "golangci-lint" / f"{rule}.md",
                    rule,
                )

        write_text(
            specs_dir / "linters" / "golangci-lint" / "overview.md",
            join_lines(
                [
                    "# golangci-lint Rules (from .golangci.yml)",
                    "",
                    f"Source: {config_url}",
                    "",
                    "## Enabled",
                    *[f"- {name}" for name in sorted(set(enabled_rules))],
                    "",
                    "## Optional",
                    *[f"- {name}" for name in sorted(set(optional_rules))],
                    "",
                    "## Disabled",
                    *[f"- {name}" for name in sorted(set(disabled_rules))],
                ]
            ),
        )

        write_text(
            specs_dir / "linters" / "golangci-lint" / "config.md",
            join_lines(
                [
                    "# golangci-lint Config (.golangci.yml)",
                    "",
                    f"Source: {config_url}",
                    "",
                    "```yaml",
                    config_path.read_text(encoding="utf-8").rstrip(),
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Go specs complete ===")


def fetch_java() -> None:
    specs_dir = SPECS_DIR / "java"
    log("=== Fetching Java Specs ===")
    for subdir in [
        "stdlib/packages",
        "linters/error-prone",
        "linters/spotbugs",
        "linters/checkstyle",
        "linters/pmd",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Java Language Specification (SE 21)...")
        fetch_markdown(
            "https://docs.oracle.com/javase/specs/jls/se21/html/jls-1.html",
            specs_dir / "spec.md",
            "Java Language Specification (SE 21)",
        )

    if fetch_section("stdlib"):
        log("Fetching Java SE API reference...")
        fetch_markdown(
            "https://docs.oracle.com/en/java/javase/21/docs/api/index.html",
            specs_dir / "stdlib" / "overview.md",
            "Java SE API Reference",
        )

        log("Fetching Java package index...")
        fetch_markdown(
            "https://docs.oracle.com/en/java/javase/21/docs/api/allpackages-index.html",
            specs_dir / "stdlib" / "packages" / "index.md",
            "Java Packages",
        )

        try:
            packages_html = fetch_url(
                "https://docs.oracle.com/en/java/javase/21/docs/api/allpackages-index.html"
            )
            packages = find_unique(
                packages_html,
                r'href="([a-zA-Z0-9_./-]+)/package-summary.html"',
            )
        except FetchError as exc:
            log(f"Failed to fetch Java package list: {exc}")
            packages = []

        for pkg in packages:
            pkg_name = pkg.replace("/", ".")
            log(f"  - java/{pkg_name}")
            fetch_markdown(
                f"https://docs.oracle.com/en/java/javase/21/docs/api/{pkg}/package-summary.html",
                specs_dir / "stdlib" / "packages" / f"{pkg_name}.md",
                pkg_name,
            )

    if fetch_section("linters"):
        log("Fetching Error Prone bug patterns...")
        fetch_markdown(
            "https://errorprone.info/bugpatterns",
            specs_dir / "linters" / "error-prone" / "overview.md",
            "Error Prone Bug Patterns",
        )

        try:
            errorprone_html = fetch_url("https://errorprone.info/bugpatterns")
            errorprone_rules = find_unique(errorprone_html, r"/bugpattern/([A-Za-z0-9_]+)")
        except FetchError as exc:
            log(f"Failed to fetch Error Prone rule list: {exc}")
            errorprone_rules = []

        for rule in errorprone_rules:
            log(f"  - error-prone/{rule}")
            fetch_markdown(
                f"https://errorprone.info/bugpattern/{rule}",
                specs_dir / "linters" / "error-prone" / f"{rule}.md",
                rule,
            )

        log("Fetching SpotBugs bug descriptions...")
        fetch_markdown(
            "https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html",
            specs_dir / "linters" / "spotbugs" / "overview.md",
            "SpotBugs Bug Descriptions",
        )

        log("Fetching PMD rules...")
        fetch_markdown(
            "https://docs.pmd-code.org/latest/pmd_rules_java.html",
            specs_dir / "linters" / "pmd" / "overview.md",
            "PMD Java Rules",
        )
        try:
            pmd_html = fetch_url("https://docs.pmd-code.org/latest/pmd_rules_java.html")
            pmd_rules = find_unique(pmd_html, r"pmd_rules_java.html#([a-zA-Z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch PMD rule list: {exc}")
            pmd_rules = []

        for rule in pmd_rules:
            log(f"  - pmd/{rule}")
            write_text(
                specs_dir / "linters" / "pmd" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://docs.pmd-code.org/latest/pmd_rules_java.html#{rule}",
                    ]
                ),
            )

        log("Fetching Checkstyle checks...")
        fetch_markdown(
            "https://checkstyle.sourceforge.io/checks.html",
            specs_dir / "linters" / "checkstyle" / "overview.md",
            "Checkstyle Checks",
        )

        try:
            checkstyle_html = fetch_url("https://checkstyle.sourceforge.io/checks.html")
            checkstyle_rules = find_unique(
                checkstyle_html, r"checks/([a-zA-Z0-9_/-]+)\\.html"
            )
        except FetchError as exc:
            log(f"Failed to fetch Checkstyle rule list: {exc}")
            checkstyle_rules = []

        for rule in checkstyle_rules:
            log(f"  - checkstyle/{rule}")
            fetch_markdown(
                f"https://checkstyle.sourceforge.io/checks/{rule}.html",
                specs_dir / "linters" / "checkstyle" / f"{rule}.md",
                rule,
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Java Idioms",
                    "",
                    "## Prefer try-with-resources",
                    "",
                    "```java",
                    "try (var input = Files.newInputStream(path)) {",
                    "    // use input",
                    "}",
                    "```",
                    "",
                    "## Use records for simple data carriers",
                    "",
                    "```java",
                    "public record User(String id, String name) {}",
                    "```",
                    "",
                    "## Prefer standard collections interfaces",
                    "",
                    "Use `List`, `Set`, and `Map` in APIs instead of concrete types.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Java Formatters",
                    "",
                    "## google-java-format",
                    "",
                    "See: https://github.com/google/google-java-format",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "google-java-format.md",
            join_lines(
                [
                    "# google-java-format Options",
                    "",
                    "See: https://github.com/google/google-java-format",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Java specs complete ===")


def fetch_python() -> None:
    specs_dir = SPECS_DIR / "python"
    log("=== Fetching Python 3.14 Specs ===")
    for subdir in [
        "stdlib/modules",
        "linters/ruff",
        "linters/pylint",
        "linters/flake8",
        "linters/mypy",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    python_version = "3.14"

    if fetch_section("patterns"):
        write_text(
            specs_dir / "pep8.md",
            join_lines(
                [
                    "# PEP 8 - Python Style Guide (Summary)",
                    "",
                    "## Indentation",
                    "",
                    "- Use 4 spaces per indentation level",
                    "- Never mix tabs and spaces",
                    "",
                    "## Maximum Line Length",
                    "",
                    "- Limit lines to 79 characters (code)",
                    "- Limit lines to 72 characters (docstrings/comments)",
                    "- Can extend to 99 for teams that agree",
                    "",
                    "## Imports",
                    "",
                    "```python",
                    "# Standard library",
                    "import os",
                    "import sys",
                    "",
                    "# Third party",
                    "import numpy as np",
                    "import pandas as pd",
                    "",
                    "# Local",
                    "from mypackage import mymodule",
                    "```",
                    "",
                    "- One import per line",
                    "- Absolute imports preferred",
                    "- Avoid wildcard imports (`from x import *`)",
                    "",
                    "## Whitespace",
                    "",
                    "```python",
                    "# GOOD",
                    "spam(ham[1], {eggs: 2})",
                    "foo = (0,)",
                    "if x == 4: print(x, y); x, y = y, x",
                    "",
                    "# BAD",
                    "spam( ham[ 1 ], { eggs: 2 } )",
                    "foo = (0, )",
                    "if x == 4 : print(x , y) ; x , y = y , x",
                    "```",
                    "",
                    "## Naming Conventions",
                    "",
                    "| Type | Convention |",
                    "|------|------------|",
                    "| Modules | `lowercase_with_underscores` |",
                    "| Classes | `CapWords` |",
                    "| Functions | `lowercase_with_underscores` |",
                    "| Variables | `lowercase_with_underscores` |",
                    "| Constants | `UPPERCASE_WITH_UNDERSCORES` |",
                    "| Private | `_single_leading_underscore` |",
                    "| \"Mangled\" | `__double_leading_underscore` |",
                    "",
                    "## Type Hints (PEP 484)",
                    "",
                    "```python",
                    "def greeting(name: str) -> str:",
                    "    return f\"Hello, {name}\"",
                    "",
                    "def process(items: list[int]) -> dict[str, int]:",
                    "    return {\"count\": len(items)}",
                    "```",
                ]
            ),
        )
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Python Idiomatic Patterns (3.10+)",
                    "",
                    "## Type Hints (Always Use)",
                    "",
                    "```python",
                    "# BAD",
                    "def process(data):",
                    "    return data.get(\"value\")",
                    "",
                    "# GOOD",
                    "def process(data: dict[str, Any]) -> str | None:",
                    "    return data.get(\"value\")",
                    "```",
                    "",
                    "## Match Statements (3.10+)",
                    "",
                    "```python",
                    "def handle_response(response: Response) -> str:",
                    "    match response.status:",
                    "        case 200:",
                    "            return response.body",
                    "        case 404:",
                    "            raise NotFoundError()",
                    "        case 500:",
                    "            raise ServerError()",
                    "        case _:",
                    "            raise UnknownError(response.status)",
                    "```",
                    "",
                    "## Dataclasses",
                    "",
                    "```python",
                    "from dataclasses import dataclass",
                    "",
                    "# BAD - boilerplate",
                    "class User:",
                    "    def __init__(self, name: str, age: int):",
                    "        self.name = name",
                    "        self.age = age",
                    "    ",
                    "    def __repr__(self):",
                    "        return f\"User(name={self.name!r}, age={self.age})\"",
                    "",
                    "# GOOD",
                    "@dataclass",
                    "class User:",
                    "    name: str",
                    "    age: int",
                    "```",
                    "",
                    "## Context Managers",
                    "",
                    "```python",
                    "# File handling",
                    "with open(\"file.txt\") as f:",
                    "    content = f.read()",
                    "",
                    "# Multiple contexts",
                    "with (",
                    "    open(\"input.txt\") as infile,",
                    "    open(\"output.txt\", \"w\") as outfile,",
                    "):",
                    "    outfile.write(infile.read())",
                    "",
                    "# Custom context manager",
                    "from contextlib import contextmanager",
                    "",
                    "@contextmanager",
                    "def timer():",
                    "    start = time.time()",
                    "    yield",
                    "    print(f\"Elapsed: {time.time() - start:.2f}s\")",
                    "```",
                    "",
                    "## List/Dict/Set Comprehensions",
                    "",
                    "```python",
                    "# List",
                    "squares = [x**2 for x in range(10)]",
                    "",
                    "# Dict",
                    "counts = {word: len(word) for word in words}",
                    "",
                    "# Set",
                    "unique_lengths = {len(word) for word in words}",
                    "",
                    "# Generator (memory efficient)",
                    "squares_gen = (x**2 for x in range(10))",
                    "```",
                    "",
                    "## Walrus Operator (3.8+)",
                    "",
                    "```python",
                    "# Read until empty",
                    "while (line := file.readline()):",
                    "    process(line)",
                    "",
                    "# Check and use",
                    "if (match := pattern.search(text)):",
                    "    print(match.group())",
                    "```",
                    "",
                    "## f-strings (Always Use)",
                    "",
                    "```python",
                    "# BAD",
                    "\"Hello, \" + name + \"!\"",
                    "\"Hello, {}!\".format(name)",
                    "\"Hello, %s!\" % name",
                    "",
                    "# GOOD",
                    "f\"Hello, {name}!\"",
                    "f\"Value: {value:.2f}\"",
                    "f\"Debug: {obj=}\"  # Shows 'obj=<value>'",
                    "```",
                    "",
                    "## Exception Handling",
                    "",
                    "```python",
                    "# Specific exceptions",
                    "try:",
                    "    value = data[\"key\"]",
                    "except KeyError:",
                    "    value = default",
                    "",
                    "# Exception groups (3.11+)",
                    "try:",
                    "    async with asyncio.TaskGroup() as tg:",
                    "        tg.create_task(task1())",
                    "        tg.create_task(task2())",
                    "except* ValueError as eg:",
                    "    for exc in eg.exceptions:",
                    "        handle(exc)",
                    "```",
                    "",
                    "## Pathlib (Not os.path)",
                    "",
                    "```python",
                    "# BAD",
                    "import os",
                    "path = os.path.join(base, \"subdir\", \"file.txt\")",
                    "if os.path.exists(path):",
                    "    with open(path) as f:",
                    "        pass",
                    "",
                    "# GOOD",
                    "from pathlib import Path",
                    "path = Path(base) / \"subdir\" / \"file.txt\"",
                    "if path.exists():",
                    "    content = path.read_text()",
                    "```",
                    "",
                    "## Enum",
                    "",
                    "```python",
                    "from enum import Enum, auto",
                    "",
                    "class Status(Enum):",
                    "    PENDING = auto()",
                    "    RUNNING = auto()",
                    "    COMPLETE = auto()",
                    "    FAILED = auto()",
                    "",
                    "def handle(status: Status) -> None:",
                    "    match status:",
                    "        case Status.PENDING:",
                    "            start()",
                    "        case Status.COMPLETE:",
                    "            cleanup()",
                    "```",
                    "",
                    "## functools",
                    "",
                    "```python",
                    "from functools import cache, lru_cache, partial",
                    "",
                    "@cache  # Unbounded cache",
                    "def fibonacci(n: int) -> int:",
                    "    if n < 2:",
                    "        return n",
                    "    return fibonacci(n - 1) + fibonacci(n - 2)",
                    "",
                    "@lru_cache(maxsize=128)  # Bounded cache",
                    "def expensive(x: int) -> int:",
                    "    return compute(x)",
                    "```",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Python Formatters",
                    "",
                    "Python formatting is typically handled by `black` (opinionated formatting) or `ruff format` (fast formatting with lint integration).",
                    "",
                    "## black",
                    "- Opinionated, stable formatting with minimal configuration.",
                    "",
                    "## ruff format",
                    "- Formatter backed by the Ruff toolchain, aligned with Ruff lint rules.",
                ]
            ),
        )
        fetch_markdown(
            "https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html",
            specs_dir / "formatters" / "black.md",
            "black Options",
        )
        fetch_markdown(
            "https://docs.astral.sh/ruff/formatter/",
            specs_dir / "formatters" / "ruff.md",
            "ruff format Options",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "ruff" / "overview.md",
            join_lines(
                [
                    "# Ruff Linter Rules",
                    "",
                    "Ruff implements rules from:",
                    "- Pyflakes (F)",
                    "- pycodestyle (E, W)",
                    "- isort (I)",
                    "- pep8-naming (N)",
                    "- pyupgrade (UP)",
                    "- flake8-* plugins",
                    "- pylint (PL)",
                    "- ruff-specific (RUF)",
                    "",
                    "## Essential Rules",
                    "",
                    "| Code | Rule | Fix |",
                    "|------|------|-----|",
                    "| F401 | Unused import | Remove |",
                    "| F841 | Unused variable | Remove or prefix with _ |",
                    "| E501 | Line too long | Break line |",
                    "| E711 | Comparison to None | Use `is None` |",
                    "| E712 | Comparison to True/False | Use truthiness |",
                    "| UP006 | Use `list` instead of `List` | Modernize |",
                    "| UP007 | Use `X | Y` instead of `Union` | Modernize |",
                    "",
                    "## Configuration",
                    "",
                    "```toml",
                    "# pyproject.toml",
                    "[tool.ruff]",
                    "line-length = 100",
                    "target-version = \"py312\"",
                    "",
                    "[tool.ruff.lint]",
                    "select = [",
                    "    \"E\",   # pycodestyle errors",
                    "    \"W\",   # pycodestyle warnings",
                    "    \"F\",   # pyflakes",
                    "    \"I\",   # isort",
                    "    \"UP\",  # pyupgrade",
                    "    \"N\",   # pep8-naming",
                    "    \"RUF\", # ruff-specific",
                    "]",
                    "ignore = [\"E501\"]  # if you want longer lines",
                    "```",
                ]
            ),
        )

        try:
            ruff_html = fetch_url("https://docs.astral.sh/ruff/rules/")
            ruff_rules = find_unique(ruff_html, r"/ruff/rules/([a-z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch Ruff rule list: {exc}")
            ruff_rules = []

        for rule in ruff_rules:
            log(f"  - ruff/{rule}")
            fetch_markdown(
                f"https://docs.astral.sh/ruff/rules/{rule}/",
                specs_dir / "linters" / "ruff" / f"{rule}.md",
                rule,
            )

        log("Fetching pylint messages...")
        fetch_markdown(
            "https://pylint.readthedocs.io/en/stable/user_guide/messages/index.html",
            specs_dir / "linters" / "pylint" / "overview.md",
            "Pylint Messages",
        )

        try:
            pylint_html = fetch_url(
                "https://pylint.readthedocs.io/en/stable/user_guide/messages/index.html"
            )
            pylint_messages = find_unique(
                pylint_html, r"/user_guide/messages/([a-z0-9_-]+)\\.html"
            )
        except FetchError as exc:
            log(f"Failed to fetch Pylint message list: {exc}")
            pylint_messages = []

        for msg in pylint_messages:
            log(f"  - pylint/{msg}")
            fetch_markdown(
                f"https://pylint.readthedocs.io/en/stable/user_guide/messages/{msg}.html",
                specs_dir / "linters" / "pylint" / f"{msg}.md",
                msg,
            )

        flake8_url = "https://flake8.pycqa.org/en/latest/user/error-codes.html"
        fetch_markdown(
            flake8_url,
            specs_dir / "linters" / "flake8" / "overview.md",
            "Flake8 Error Codes",
        )
        try:
            flake8_html = fetch_url(flake8_url)
            flake8_codes = find_unique(flake8_html, r"\b([A-Z][0-9]{3})\b")
            flake8_md = _simple_html_to_markdown(extract_main(flake8_html))
            flake8_table = _extract_markdown_table(flake8_md)
        except FetchError as exc:
            log(f"Failed to fetch Flake8 error codes: {exc}")
            flake8_codes = []
            flake8_table = {}

        for code in flake8_codes:
            log(f"  - flake8/{code}")
            description = flake8_table.get(code, "").strip()
            if description:
                write_text(
                    specs_dir / "linters" / "flake8" / f"{code}.md",
                    join_lines(
                        [
                            f"# {code}",
                            "",
                            description,
                            "",
                            f"Source: {flake8_url}",
                        ]
                    ),
                )
            else:
                write_text(
                    specs_dir / "linters" / "flake8" / f"{code}.md",
                    join_lines(
                        [
                            f"# {code}",
                            "",
                            f"Source: {flake8_url}",
                        ]
                    ),
                )

        mypy_url = "https://mypy.readthedocs.io/en/stable/error_code_list.html"
        fetch_markdown(
            mypy_url,
            specs_dir / "linters" / "mypy" / "overview.md",
            "mypy Error Codes",
        )
        try:
            mypy_html = fetch_url(mypy_url)
            mypy_codes = find_unique(mypy_html, r"error_code_list.html#([a-z0-9-]+)")
            mypy_md = _simple_html_to_markdown(extract_main(mypy_html))
            mypy_sections = _extract_markdown_sections(mypy_md)
            mypy_table = _extract_markdown_table(mypy_md)
        except FetchError as exc:
            log(f"Failed to fetch mypy error codes: {exc}")
            mypy_codes = []
            mypy_sections = {}
            mypy_table = {}

        for code in mypy_codes:
            log(f"  - mypy/{code}")
            description = mypy_table.get(code) or mypy_sections.get(code) or ""
            description = description.strip()
            if description:
                write_text(
                    specs_dir / "linters" / "mypy" / f"{code}.md",
                    join_lines(
                        [
                            f"# {code}",
                            "",
                            description,
                            "",
                            f"Source: {mypy_url}#{code}",
                        ]
                    ),
                )
            else:
                write_text(
                    specs_dir / "linters" / "mypy" / f"{code}.md",
                    join_lines(
                        [
                            f"# {code}",
                            "",
                            f"Source: {mypy_url}#{code}",
                        ]
                    ),
                )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Python Standard Library Quick Reference",
                    "",
                    "## Essential Modules",
                    "",
                    "| Module | Purpose |",
                    "|--------|---------|",
                    "| `pathlib` | File paths (use over os.path) |",
                    "| `json` | JSON encoding/decoding |",
                    "| `dataclasses` | Data containers |",
                    "| `typing` | Type hints |",
                    "| `collections` | Specialized containers |",
                    "| `itertools` | Iterator utilities |",
                    "| `functools` | Higher-order functions |",
                    "| `contextlib` | Context manager utilities |",
                    "| `asyncio` | Async I/O |",
                    "| `logging` | Logging facility |",
                    "| `re` | Regular expressions |",
                    "| `datetime` | Date and time |",
                    "| `enum` | Enumerations |",
                    "| `abc` | Abstract base classes |",
                    "",
                    "## Type Hints (typing module)",
                    "",
                    "```python",
                    "from typing import Any, TypeVar, Generic",
                    "from collections.abc import Callable, Iterator, Mapping",
                    "",
                    "# Basic",
                    "x: int = 1",
                    "y: str | None = None",
                    "z: list[int] = [1, 2, 3]",
                    "",
                    "# Callable",
                    "Handler = Callable[[Request], Response]",
                    "",
                    "# Generic",
                    "T = TypeVar(\"T\")",
                    "",
                    "class Stack(Generic[T]):",
                    "    def push(self, item: T) -> None: ...",
                    "    def pop(self) -> T: ...",
                    "```",
                    "",
                    "## Collections",
                    "",
                    "```python",
                    "from collections import defaultdict, Counter, deque, namedtuple",
                    "",
                    "# defaultdict - auto-initialize missing keys",
                    "counts = defaultdict(int)",
                    "counts[\"a\"] += 1",
                    "",
                    "# Counter - count occurrences",
                    "c = Counter(\"abracadabra\")",
                    "c.most_common(3)  # [('a', 5), ('b', 2), ('r', 2)]",
                    "",
                    "# deque - efficient double-ended queue",
                    "d = deque(maxlen=3)",
                    "d.append(1)",
                    "d.appendleft(0)",
                    "",
                    "# namedtuple (prefer dataclass for new code)",
                    "Point = namedtuple(\"Point\", [\"x\", \"y\"])",
                    "```",
                ]
            ),
        )

        log("Fetching Python stdlib modules...")
        try:
            stdlib_html = fetch_url(f"https://docs.python.org/{python_version}/library/")
            stdlib_modules = find_unique(stdlib_html, r"/library/([a-zA-Z0-9_]+)\\.html")
        except FetchError as exc:
            log(f"Failed to fetch stdlib modules: {exc}")
            stdlib_modules = []

        for mod in stdlib_modules:
            log(f"  - python/{mod}")
            fetch_markdown(
                f"https://docs.python.org/{python_version}/library/{mod}.html",
                specs_dir / "stdlib" / "modules" / f"{mod}.md",
                mod,
            )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Python specs complete ===")


def fetch_basic() -> None:
    specs_dir = SPECS_DIR / "basic"
    log("=== Fetching BASIC Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)
    reference_url = "https://en.wikibooks.org/wiki/QBasic"

    if fetch_section("spec"):
        log("Fetching QBasic reference...")
        fetch_markdown(
            reference_url,
            specs_dir / "spec.md",
            "BASIC Language Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            reference_url,
            specs_dir / "stdlib" / "overview.md",
            "BASIC Standard Library Reference",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# BASIC Linting",
                    "",
                    "There is no widely used, modern linter ecosystem for classic BASIC dialects.",
                    "",
                    "## Recommendations",
                    "",
                    "- Use compiler/interpreter warnings where available.",
                    "- Prefer structured programming constructs to avoid spaghetti control flow.",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# BASIC Idioms",
                    "",
                    "## Prefer Structured Control Flow",
                    "",
                    "- Use `IF...ELSE` and `SELECT CASE` over `GOTO`.",
                    "- Keep procedures short and single-purpose.",
                    "",
                    "## Use Explicit Declarations",
                    "",
                    "- Use `DIM` for clarity instead of relying on implicit typing.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# BASIC Formatters",
                    "",
                    "There is no widely adopted formatter for classic BASIC dialects.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== BASIC specs complete ===")


def fetch_batch() -> None:
    specs_dir = SPECS_DIR / "batch"
    log("=== Fetching Batch Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching CMD command reference...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands",
            specs_dir / "spec.md",
            "Windows Command Reference",
        )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Windows CMD Built-in Commands",
                    "",
                    "See: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands",
                ]
            ),
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Batch Linting",
                    "",
                    "There is no widely adopted modern linter for Windows Batch scripts.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Batch Formatters",
                    "",
                    "No widely adopted formatter for Windows Batch scripts.",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Batch Idioms",
                    "",
                    "## Use SetLocal",
                    "",
                    "```bat",
                    "@echo off",
                    "setlocal EnableExtensions EnableDelayedExpansion",
                    "```",
                    "",
                    "## Quote paths",
                    "",
                    "```bat",
                    "if exist \"%~f0\" echo Running",
                    "```",
                    "",
                    "## Prefer CALL for subroutines",
                    "",
                    "```bat",
                    "call :do_work",
                    "exit /b",
                    "",
                    ":do_work",
                    "  echo Work",
                    "  exit /b",
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Batch specs complete ===")


def fetch_bash() -> None:
    specs_dir = SPECS_DIR / "bash"
    log("=== Fetching Bash Specs ===")
    for subdir in ["stdlib", "linters/shellcheck", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Bash reference manual...")
        fetch_markdown(
            "https://www.gnu.org/software/bash/manual/bash.html",
            specs_dir / "spec.md",
            "Bash Reference Manual",
        )

    if fetch_section("stdlib"):
        log("Fetching Bash builtins reference...")
        fetch_markdown(
            "https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins",
            specs_dir / "stdlib" / "builtins.md",
            "Bash Builtins",
        )
        log("Fetching Bash reserved words...")
        fetch_markdown(
            "https://www.gnu.org/software/bash/manual/bash.html#Reserved-Words",
            specs_dir / "stdlib" / "reserved-words.md",
            "Bash Reserved Words",
        )
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Bash Reference",
                    "",
                    "See: https://www.gnu.org/software/bash/manual/bash.html",
                ]
            ),
        )

    if fetch_section("linters"):
        log("Fetching ShellCheck rules...")
        fetch_markdown(
            "https://www.shellcheck.net/wiki/",
            specs_dir / "linters" / "shellcheck" / "overview.md",
            "ShellCheck Rules",
        )
        try:
            shellcheck_html = fetch_url("https://www.shellcheck.net/wiki/")
            shellcheck_rules = find_unique(shellcheck_html, r"(SC[0-9]{4})")
        except FetchError as exc:
            log(f"Failed to fetch ShellCheck rules: {exc}")
            shellcheck_rules = []
        for rule in shellcheck_rules:
            log(f"  - shellcheck/{rule}")
            write_text(
                specs_dir / "linters" / "shellcheck" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://www.shellcheck.net/wiki/{rule}",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Bash Formatters",
                    "",
                    "## shfmt",
                    "",
                    "See: https://github.com/mvdan/sh",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "shfmt.md",
            join_lines(
                [
                    "# shfmt Options",
                    "",
                    "See: https://github.com/mvdan/sh#shfmt",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Bash Idioms",
                    "",
                    "## Strict mode",
                    "",
                    "```bash",
                    "set -euo pipefail",
                    "IFS=$'\\n\\t'",
                    "```",
                    "",
                    "## Prefer [[ ]] tests",
                    "",
                    "```bash",
                    "if [[ -f \"$path\" ]]; then",
                    "  echo \"exists\"",
                    "fi",
                    "```",
                    "",
                    "## Quote variables",
                    "",
                    "```bash",
                    "echo \"$var\"",
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Bash specs complete ===")


def fetch_css() -> None:
    specs_dir = SPECS_DIR / "css"
    log("=== Fetching CSS Specs ===")
    for subdir in ["stdlib", "linters/stylelint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching CSS Snapshot...")
        fetch_markdown(
            "https://www.w3.org/TR/css-2023/",
            specs_dir / "spec.md",
            "CSS Snapshot",
        )

    if fetch_section("stdlib"):
        log("Fetching CSS reference...")
        fetch_markdown(
            "https://developer.mozilla.org/en-US/docs/Web/CSS/Reference",
            specs_dir / "stdlib" / "overview.md",
            "CSS Reference",
        )

    if fetch_section("linters"):
        log("Fetching stylelint rules...")
        fetch_markdown(
            "https://stylelint.io/user-guide/rules",
            specs_dir / "linters" / "stylelint" / "overview.md",
            "stylelint Rules",
        )
        try:
            stylelint_html = fetch_url("https://stylelint.io/user-guide/rules")
            stylelint_rules = find_unique(stylelint_html, r"/user-guide/rules/([a-z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch stylelint rules: {exc}")
            stylelint_rules = []

        for rule in stylelint_rules:
            log(f"  - stylelint/{rule}")
            write_text(
                specs_dir / "linters" / "stylelint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://stylelint.io/user-guide/rules/{rule}",
                    ]
                ),
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# CSS Idioms",
                    "",
                    "## Prefer modern layout",
                    "",
                    "- Use Flexbox and Grid over floats.",
                    "",
                    "## Use custom properties for theming",
                    "",
                    "```css",
                    ":root { --brand-color: #0b5fff; }",
                    ".button { color: var(--brand-color); }",
                    "```",
                    "",
                    "## Avoid overly specific selectors",
                    "",
                    "Keep selectors short and maintainable.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# CSS Formatters",
                    "",
                    "## Prettier",
                    "",
                    "See: https://prettier.io/docs/en/",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "prettier.md",
            join_lines(
                [
                    "# Prettier Options",
                    "",
                    "See: https://prettier.io/docs/en/options.html",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== CSS specs complete ===")


def fetch_html() -> None:
    specs_dir = SPECS_DIR / "html"
    log("=== Fetching HTML Specs ===")
    for subdir in ["stdlib", "linters/html-validate", "linters/htmlhint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching HTML Living Standard...")
        fetch_markdown(
            "https://html.spec.whatwg.org/",
            specs_dir / "spec.md",
            "HTML Living Standard",
        )

    if fetch_section("stdlib"):
        log("Fetching HTML element reference...")
        fetch_markdown(
            "https://developer.mozilla.org/en-US/docs/Web/HTML/Element",
            specs_dir / "stdlib" / "overview.md",
            "HTML Element Reference",
        )

    if fetch_section("linters"):
        log("Fetching HTML-validate rules...")
        fetch_markdown(
            "https://html-validate.org/rules/",
            specs_dir / "linters" / "html-validate" / "overview.md",
            "HTML-validate Rules",
        )
        try:
            html_validate_html = fetch_url("https://html-validate.org/rules/")
            html_validate_rules = find_unique(
                html_validate_html,
                r"/rules/([a-z0-9-]+(?:/[a-z0-9-]+)?)\\.html",
            )
        except FetchError as exc:
            log(f"Failed to fetch html-validate rules: {exc}")
            html_validate_rules = []

        for rule in html_validate_rules:
            log(f"  - html-validate/{rule}")
            write_text(
                specs_dir / "linters" / "html-validate" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://html-validate.org/rules/{rule}.html",
                    ]
                ),
            )

        fetch_markdown(
            "https://htmlhint.com/docs/user-guide/rules/",
            specs_dir / "linters" / "htmlhint" / "overview.md",
            "HTMLHint Rules",
        )
        try:
            htmlhint_html = fetch_url("https://htmlhint.com/docs/user-guide/rules/")
            htmlhint_rules = find_unique(htmlhint_html, r"#([a-z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch HTMLHint rules: {exc}")
            htmlhint_rules = []

        for rule in htmlhint_rules:
            if rule == "rules":
                continue
            log(f"  - htmlhint/{rule}")
            write_text(
                specs_dir / "linters" / "htmlhint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://htmlhint.com/docs/user-guide/rules/#{rule}",
                    ]
                ),
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# HTML Idioms",
                    "",
                    "## Use semantic elements",
                    "",
                    "Prefer `header`, `main`, `nav`, `section`, `article`, and `footer`.",
                    "",
                    "## Keep accessibility in mind",
                    "",
                    "- Provide `alt` text for images.",
                    "- Ensure form controls have labels.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# HTML Formatters",
                    "",
                    "## Prettier",
                    "",
                    "See: https://prettier.io/docs/en/",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "prettier.md",
            join_lines(
                [
                    "# Prettier Options",
                    "",
                    "See: https://prettier.io/docs/en/options.html",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== HTML specs complete ===")


def fetch_git() -> None:
    specs_dir = SPECS_DIR / "git"
    log("=== Fetching Git Specs ===")
    for subdir in [
        "stdlib",
        "linters/gitlint",
        "linters/commitlint",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Git reference...")
        fetch_markdown(
            "https://git-scm.com/docs",
            specs_dir / "spec.md",
            "Git Reference",
        )

    if fetch_section("stdlib"):
        log("Fetching Git command reference...")
        fetch_markdown(
            "https://git-scm.com/docs/git",
            specs_dir / "stdlib" / "overview.md",
            "Git Command Reference",
        )

    if fetch_section("linters"):
        log("Fetching gitlint rules...")
        fetch_markdown(
            "https://jorisroovers.com/gitlint/rules/",
            specs_dir / "linters" / "gitlint" / "overview.md",
            "gitlint Rules",
        )
        log("Fetching commitlint rules...")
        fetch_markdown(
            "https://commitlint.js.org/#/reference-rules",
            specs_dir / "linters" / "commitlint" / "overview.md",
            "commitlint Rules",
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Git Formatters",
                    "",
                    "There is no widely adopted code formatter for Git itself.",
                    "",
                    "## Commit message formatting tools",
                    "",
                    "- commitlint: https://commitlint.js.org/",
                    "- commitizen: https://commitizen-tools.github.io/commitizen/",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Git Idioms",
                    "",
                    "## Keep commits atomic",
                    "",
                    "One logical change per commit.",
                    "",
                    "## Prefer rebase for local history cleanup",
                    "",
                    "```bash",
                    "git fetch origin",
                    "git rebase origin/main",
                    "```",
                    "",
                    "## Use conventional commit messages",
                    "",
                    "```",
                    "feat(parser): add streaming mode",
                    "fix(api): handle nil response",
                    "```",
                    "",
                    "## Avoid rewriting shared history",
                    "",
                    "Do not force-push to shared branches unless agreed.",
                ]
            ),
        )
        write_text(
            specs_dir / "patterns" / "conventions.md",
            join_lines(
                [
                    "# Git Conventions",
                    "",
                    "## Conventional Commits",
                    "",
                    "Specification: https://www.conventionalcommits.org/en/v1.0.0/",
                    "",
                    "## Branching",
                    "",
                    "- Trunk-based development: https://trunkbaseddevelopment.com/",
                    "- GitHub Flow: https://docs.github.com/en/get-started/quickstart/github-flow",
                    "- GitFlow (legacy): https://nvie.com/posts/a-successful-git-branching-model/",
                    "",
                    "## Releases and Changelogs",
                    "",
                    "- Keep a Changelog: https://keepachangelog.com/en/1.1.0/",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Git specs complete ===")


def fetch_rust() -> None:
    specs_dir = SPECS_DIR / "rust"
    log("=== Fetching Rust Specs ===")
    for subdir in ["stdlib/modules", "linters/clippy", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Rust Reference...")
        fetch_markdown(
            "https://doc.rust-lang.org/reference/",
            specs_dir / "spec.md",
            "Rust Reference",
        )

    if fetch_section("stdlib"):
        log("Fetching Rust standard library docs...")
        fetch_markdown(
            "https://doc.rust-lang.org/std/",
            specs_dir / "stdlib" / "overview.md",
            "Rust Standard Library",
        )
        try:
            std_html = fetch_url("https://doc.rust-lang.org/std/all.html")
            rust_modules = find_unique(std_html, r"std::([a-zA-Z0-9_]+)")
        except FetchError as exc:
            log(f"Failed to fetch Rust module list: {exc}")
            rust_modules = []

        for mod in rust_modules:
            log(f"  - rust/{mod}")
            write_text(
                specs_dir / "stdlib" / "modules" / f"{mod}.md",
                join_lines(
                    [
                        f"# std::{mod}",
                        "",
                        f"See: https://doc.rust-lang.org/std/{mod}/index.html",
                    ]
                ),
            )

    if fetch_section("linters"):
        log("Fetching Clippy lints...")
        fetch_markdown(
            "https://rust-lang.github.io/rust-clippy/master/",
            specs_dir / "linters" / "clippy" / "overview.md",
            "Clippy Lints",
        )
        try:
            clippy_html = fetch_url("https://rust-lang.github.io/rust-clippy/master/")
            clippy_lints = find_unique(clippy_html, r'href="#([a-z0-9_]+)"')
        except FetchError as exc:
            log(f"Failed to fetch Clippy lint list: {exc}")
            clippy_lints = []
        for lint in clippy_lints:
            log(f"  - clippy/{lint}")
            write_text(
                specs_dir / "linters" / "clippy" / f"{lint}.md",
                join_lines(
                    [
                        f"# {lint}",
                        "",
                        f"See: https://rust-lang.github.io/rust-clippy/master/#{lint}",
                    ]
                ),
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Rust Idioms",
                    "",
                    "## Prefer iterators over indexing",
                    "",
                    "```rust",
                    "for item in items.iter() {",
                    "    // ...",
                    "}",
                    "```",
                    "",
                    "## Use `Result` and `?` for error propagation",
                    "",
                    "```rust",
                    "let data = read_to_string(path)?;",
                    "```",
                    "",
                    "## Favor borrowing over cloning",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Rust Formatters",
                    "",
                    "## rustfmt",
                    "",
                    "See: https://github.com/rust-lang/rustfmt",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "rustfmt.md",
            join_lines(
                [
                    "# rustfmt Options",
                    "",
                    "See: https://github.com/rust-lang/rustfmt/blob/master/Configurations.md",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Rust specs complete ===")


def fetch_sql() -> None:
    specs_dir = SPECS_DIR / "sql"
    log("=== Fetching SQL Specs ===")
    for subdir in [
        "stdlib/postgres",
        "stdlib/mysql",
        "stdlib/sqlite",
        "stdlib/sqlserver",
        "linters/sqlfluff",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        write_text(
            specs_dir / "spec.md",
            join_lines(
                [
                    "# SQL Overview",
                    "",
                    "The SQL standard is copyrighted; use vendor references for authoritative details.",
                    "",
                    "- PostgreSQL: https://www.postgresql.org/docs/current/sql.html",
                    "- MySQL: https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html",
                    "- SQLite: https://www.sqlite.org/lang.html",
                    "- SQL Server (T-SQL): https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver16",
                ]
            ),
        )

    if fetch_section("stdlib"):
        log("Fetching PostgreSQL references...")
        fetch_markdown(
            "https://www.postgresql.org/docs/current/sql.html",
            specs_dir / "stdlib" / "postgres" / "commands.md",
            "PostgreSQL SQL Commands",
        )
        fetch_markdown(
            "https://www.postgresql.org/docs/current/functions.html",
            specs_dir / "stdlib" / "postgres" / "functions.md",
            "PostgreSQL Functions and Operators",
        )

        log("Fetching MySQL references...")
        fetch_markdown(
            "https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html",
            specs_dir / "stdlib" / "mysql" / "commands.md",
            "MySQL SQL Statements",
        )
        fetch_markdown(
            "https://dev.mysql.com/doc/refman/8.0/en/functions.html",
            specs_dir / "stdlib" / "mysql" / "functions.md",
            "MySQL Functions and Operators",
        )

        log("Fetching SQLite references...")
        fetch_markdown(
            "https://www.sqlite.org/lang.html",
            specs_dir / "stdlib" / "sqlite" / "commands.md",
            "SQLite SQL Language",
        )
        fetch_markdown(
            "https://www.sqlite.org/lang_corefunc.html",
            specs_dir / "stdlib" / "sqlite" / "functions-core.md",
            "SQLite Core Functions",
        )
        fetch_markdown(
            "https://www.sqlite.org/lang_aggfunc.html",
            specs_dir / "stdlib" / "sqlite" / "functions-aggregate.md",
            "SQLite Aggregate Functions",
        )
        fetch_markdown(
            "https://www.sqlite.org/lang_datefunc.html",
            specs_dir / "stdlib" / "sqlite" / "functions-date.md",
            "SQLite Date and Time Functions",
        )

        log("Fetching SQL Server references...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver16",
            specs_dir / "stdlib" / "sqlserver" / "commands.md",
            "SQL Server T-SQL Reference",
        )
        fetch_markdown(
            "https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16",
            specs_dir / "stdlib" / "sqlserver" / "functions.md",
            "SQL Server Functions",
        )

    if fetch_section("linters"):
        log("Fetching sqlfluff rules...")
        fetch_markdown(
            "https://docs.sqlfluff.com/en/stable/rules.html",
            specs_dir / "linters" / "sqlfluff" / "overview.md",
            "sqlfluff Rules",
        )
        try:
            sqlfluff_html = fetch_url("https://docs.sqlfluff.com/en/stable/rules.html")
            sqlfluff_rules = find_unique(sqlfluff_html, r"rule-(L[0-9]{3})")
        except FetchError as exc:
            log(f"Failed to fetch sqlfluff rules: {exc}")
            sqlfluff_rules = []
        for rule in sqlfluff_rules:
            log(f"  - sqlfluff/{rule}")
            write_text(
                specs_dir / "linters" / "sqlfluff" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://docs.sqlfluff.com/en/stable/rules.html#rule-{rule}",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# SQL Formatters",
                    "",
                    "## sqlfluff",
                    "",
                    "See: https://docs.sqlfluff.com/en/stable/formatter.html",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "sqlfluff.md",
            join_lines(
                [
                    "# sqlfluff Formatter Options",
                    "",
                    "See: https://docs.sqlfluff.com/en/stable/configuration.html",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# SQL Idioms",
                    "",
                    "## Explicit column lists",
                    "",
                    "```sql",
                    "SELECT id, name FROM users;",
                    "```",
                    "",
                    "## Use parameterized queries",
                    "",
                    "Avoid string concatenation for user input.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== SQL specs complete ===")


def fetch_swift() -> None:
    specs_dir = SPECS_DIR / "swift"
    log("=== Fetching Swift Specs ===")
    for subdir in ["stdlib/modules", "linters/swiftlint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching The Swift Programming Language...")
        fetch_markdown(
            "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/",
            specs_dir / "spec.md",
            "The Swift Programming Language",
        )

    if fetch_section("stdlib"):
        log("Fetching Swift standard library reference...")
        fetch_markdown(
            "https://developer.apple.com/documentation/swift/swift_standard_library",
            specs_dir / "stdlib" / "overview.md",
            "Swift Standard Library",
        )
        try:
            swift_html = fetch_url("https://developer.apple.com/documentation/swift")
            swift_modules = find_unique(swift_html, r"/documentation/swift/([A-Za-z0-9_]+)")
        except FetchError as exc:
            log(f"Failed to fetch Swift module list: {exc}")
            swift_modules = []

        for mod in swift_modules:
            log(f"  - swift/{mod}")
            fetch_markdown(
                f"https://developer.apple.com/documentation/swift/{mod}",
                specs_dir / "stdlib" / "modules" / f"{mod}.md",
                mod,
            )

    if fetch_section("linters"):
        log("Fetching SwiftLint rule directory...")
        fetch_markdown(
            "https://realm.github.io/SwiftLint/rule-directory.html",
            specs_dir / "linters" / "swiftlint" / "overview.md",
            "SwiftLint Rules",
        )
        try:
            swiftlint_html = fetch_url("https://realm.github.io/SwiftLint/rule-directory.html")
            swiftlint_rules = find_unique(swiftlint_html, r'href="#([a-zA-Z0-9_-]+)"')
        except FetchError as exc:
            log(f"Failed to fetch SwiftLint rules: {exc}")
            swiftlint_rules = []
        for rule in swiftlint_rules:
            log(f"  - swiftlint/{rule}")
            write_text(
                specs_dir / "linters" / "swiftlint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://realm.github.io/SwiftLint/rule-directory.html#{rule}",
                    ]
                ),
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Swift Idioms",
                    "",
                    "## Prefer value types",
                    "",
                    "Use structs by default; use classes when identity is required.",
                    "",
                    "## Use optionals explicitly",
                    "",
                    "```swift",
                    "let value: String?",
                    "```",
                    "",
                    "## Favor protocol-oriented design",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Swift Formatters",
                    "",
                    "## swift-format",
                    "",
                    "See: https://github.com/apple/swift-format",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "swift-format.md",
            join_lines(
                [
                    "# swift-format Options",
                    "",
                    "See: https://github.com/apple/swift-format/blob/main/Documentation/Configuration.md",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Swift specs complete ===")


def fetch_powershell() -> None:
    specs_dir = SPECS_DIR / "powershell"
    log("=== Fetching PowerShell Specs ===")
    for subdir in [
        "stdlib/cmdlets",
        "linters/psscriptanalyzer",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching PowerShell language specification...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/powershell/scripting/lang-spec/chapter-01",
            specs_dir / "spec.md",
            "PowerShell Language Specification",
        )

    if fetch_section("stdlib"):
        log("Fetching PowerShell cmdlet reference...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4",
            specs_dir / "stdlib" / "overview.md",
            "PowerShell Cmdlet Reference",
        )
        try:
            cmdlet_html = fetch_url(
                "https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4"
            )
            cmdlets = find_unique(cmdlet_html, r"/powershell/module/([A-Za-z0-9_.-]+)")
        except FetchError as exc:
            log(f"Failed to fetch PowerShell cmdlet list: {exc}")
            cmdlets = []
        for mod in cmdlets:
            log(f"  - powershell/{mod}")
            fetch_markdown(
                f"https://learn.microsoft.com/en-us/powershell/module/{mod}?view=powershell-7.4",
                specs_dir / "stdlib" / "cmdlets" / f"{mod}.md",
                mod,
            )

    if fetch_section("linters"):
        log("Fetching PSScriptAnalyzer rules...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/overview?view=ps-modules",
            specs_dir / "linters" / "psscriptanalyzer" / "overview.md",
            "PSScriptAnalyzer",
        )
        fetch_markdown(
            "https://github.com/PowerShell/PSScriptAnalyzer/blob/master/docs/Rules/README.md",
            specs_dir / "linters" / "psscriptanalyzer" / "rules.md",
            "PSScriptAnalyzer Rules",
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# PowerShell Formatters",
                    "",
                    "PowerShell has built-in formatting cmdlets, but no widely adopted code formatter.",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# PowerShell Idioms",
                    "",
                    "## Prefer cmdlets over aliases",
                    "",
                    "```powershell",
                    "Get-ChildItem",
                    "```",
                    "",
                    "## Use splatting for readability",
                    "",
                    "```powershell",
                    "$params = @{ Path = $path; Recurse = $true }",
                    "Get-ChildItem @params",
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== PowerShell specs complete ===")


def fetch_c() -> None:
    specs_dir = SPECS_DIR / "c"
    log("=== Fetching C Specs ===")
    for subdir in ["stdlib/headers", "patterns", "formatters", "linters/clang-tidy", "linters/cppcheck"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching C standard draft...")
        try:
            data = fetch_bytes("https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3096.pdf")
            (specs_dir / "c23-draft.pdf").write_bytes(data)
        except FetchError as exc:
            log(f"Failed to fetch C23 draft: {exc}")

    if fetch_section("patterns"):
        template = Path(__file__).resolve().parent / "templates" / "c" / "patterns" / "idioms.md"
        write_template(template, specs_dir / "patterns" / "idioms.md")

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# C Formatters",
                    "",
                    "## clang-format",
                    "",
                    "See: https://clang.llvm.org/docs/ClangFormat.html",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "clang-format.md",
            join_lines(
                [
                    "# clang-format Options",
                    "",
                    "See: https://clang.llvm.org/docs/ClangFormatStyleOptions.html",
                ]
            ),
        )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# C Standard Library Overview",
                    "",
                    "## Headers",
                    "",
                    "| Header | Purpose |",
                    "|--------|---------|",
                    "| `<stdio.h>` | Input/output |",
                    "| `<stdlib.h>` | General utilities, memory |",
                    "| `<string.h>` | String manipulation |",
                    "| `<stdint.h>` | Fixed-width integers |",
                    "| `<stdbool.h>` | Boolean type |",
                    "| `<stddef.h>` | Common definitions |",
                    "| `<errno.h>` | Error codes |",
                    "| `<limits.h>` | Implementation limits |",
                    "| `<math.h>` | Math functions |",
                    "| `<time.h>` | Time functions |",
                    "| `<assert.h>` | Assertions |",
                    "",
                    "## Common Functions",
                    "",
                    "### Memory",
                    "",
                    "```c",
                    "void *malloc(size_t size);",
                    "void *calloc(size_t nmemb, size_t size);",
                    "void *realloc(void *ptr, size_t size);",
                    "void free(void *ptr);",
                    "void *memcpy(void *dest, const void *src, size_t n);",
                    "void *memset(void *s, int c, size_t n);",
                    "```",
                    "",
                    "### Strings",
                    "",
                    "```c",
                    "size_t strlen(const char *s);",
                    "char *strcpy(char *dest, const char *src);",
                    "char *strncpy(char *dest, const char *src, size_t n);",
                    "int strcmp(const char *s1, const char *s2);",
                    "char *strcat(char *dest, const char *src);",
                    "char *strstr(const char *haystack, const char *needle);",
                    "```",
                    "",
                    "### I/O",
                    "",
                    "```c",
                    "FILE *fopen(const char *path, const char *mode);",
                    "int fclose(FILE *stream);",
                    "size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);",
                    "size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);",
                    "int fprintf(FILE *stream, const char *format, ...);",
                    "int snprintf(char *str, size_t size, const char *format, ...);",
                    "```",
                ]
            ),
        )

    if fetch_section("linters"):
        log("Fetching clang-tidy checks...")
        fetch_markdown(
            "https://clang.llvm.org/extra/clang-tidy/checks/list.html",
            specs_dir / "linters" / "clang-tidy" / "overview.md",
            "clang-tidy Checks",
        )
        try:
            tidy_html = fetch_url("https://clang.llvm.org/extra/clang-tidy/checks/list.html")
            tidy_checks = find_unique(tidy_html, r"checks/([a-zA-Z0-9_-]+)\\.html")
        except FetchError as exc:
            log(f"Failed to fetch clang-tidy checks: {exc}")
            tidy_checks = []
        for check in tidy_checks:
            log(f"  - clang-tidy/{check}")
            fetch_markdown(
                f"https://clang.llvm.org/extra/clang-tidy/checks/{check}.html",
                specs_dir / "linters" / "clang-tidy" / f"{check}.md",
                check,
            )

        fetch_markdown(
            "https://cppcheck.sourceforge.io/manual.html",
            specs_dir / "linters" / "cppcheck" / "overview.md",
            "cppcheck Manual",
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== C specs complete ===")


def fetch_cpp() -> None:
    specs_dir = SPECS_DIR / "cpp"
    log("=== Fetching C++ Specs ===")
    for subdir in ["stdlib/headers", "patterns", "formatters", "linters/clang-tidy", "linters/cppcheck"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("patterns"):
        template = Path(__file__).resolve().parent / "templates" / "cpp" / "patterns" / "idioms.md"
        write_template(template, specs_dir / "patterns" / "idioms.md")

    if fetch_section("linters"):
        log("Fetching clang-tidy checks...")
        fetch_markdown(
            "https://clang.llvm.org/extra/clang-tidy/checks/list.html",
            specs_dir / "linters" / "clang-tidy" / "overview.md",
            "clang-tidy Checks",
        )
        try:
            tidy_html = fetch_url("https://clang.llvm.org/extra/clang-tidy/checks/list.html")
            tidy_checks = find_unique(tidy_html, r"checks/([a-zA-Z0-9_-]+)\\.html")
        except FetchError as exc:
            log(f"Failed to fetch clang-tidy checks: {exc}")
            tidy_checks = []
        for check in tidy_checks:
            log(f"  - clang-tidy/{check}")
            fetch_markdown(
                f"https://clang.llvm.org/extra/clang-tidy/checks/{check}.html",
                specs_dir / "linters" / "clang-tidy" / f"{check}.md",
                check,
            )

        fetch_markdown(
            "https://cppcheck.sourceforge.io/manual.html",
            specs_dir / "linters" / "cppcheck" / "overview.md",
            "cppcheck Manual",
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# C++ Formatters",
                    "",
                    "## clang-format",
                    "",
                    "See: https://clang.llvm.org/docs/ClangFormat.html",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "clang-format.md",
            join_lines(
                [
                    "# clang-format Options",
                    "",
                    "See: https://clang.llvm.org/docs/ClangFormatStyleOptions.html",
                ]
            ),
        )

    if fetch_section("stdlib"):
        log("Fetching C++ standard library headers...")
        fetch_markdown(
            "https://en.cppreference.com/w/cpp/header",
            specs_dir / "stdlib" / "headers" / "index.md",
            "C++ Standard Library Headers",
        )
        try:
            header_html = fetch_url("https://en.cppreference.com/w/cpp/header")
            headers = find_unique(header_html, r"/w/cpp/header/([a-zA-Z0-9_.]+)")
        except FetchError as exc:
            log(f"Failed to fetch C++ headers: {exc}")
            headers = []
        for hdr in headers:
            log(f"  - cpp/{hdr}")
            fetch_markdown(
                f"https://en.cppreference.com/w/cpp/header/{hdr}",
                specs_dir / "stdlib" / "headers" / f"{hdr}.md",
                hdr,
            )

        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Modern C++ Standard Library",
                    "",
                    "## Core Headers",
                    "",
                    "| Header | Purpose |",
                    "|--------|---------|",
                    "| `<memory>` | Smart pointers |",
                    "| `<string>` | String class |",
                    "| `<string_view>` | Non-owning string reference |",
                    "| `<vector>` | Dynamic array |",
                    "| `<array>` | Fixed-size array |",
                    "| `<map>` / `<unordered_map>` | Associative containers |",
                    "| `<optional>` | Nullable values |",
                    "| `<variant>` | Type-safe union |",
                    "| `<expected>` | Result type (C++23) |",
                    "| `<span>` | Non-owning view |",
                    "| `<ranges>` | Range algorithms |",
                    "| `<format>` | Type-safe formatting |",
                    "| `<filesystem>` | File operations |",
                    "| `<thread>` | Threading |",
                    "| `<mutex>` | Synchronization |",
                    "| `<chrono>` | Time utilities |",
                    "",
                    "## Smart Pointers",
                    "",
                    "```cpp",
                    "#include <memory>",
                    "",
                    "// Unique ownership",
                    "std::unique_ptr<T> ptr = std::make_unique<T>(args...);",
                    "",
                    "// Shared ownership",
                    "std::shared_ptr<T> ptr = std::make_shared<T>(args...);",
                    "",
                    "// Non-owning observer",
                    "std::weak_ptr<T> weak = shared;",
                    "```",
                    "",
                    "## Containers",
                    "",
                    "```cpp",
                    "std::vector<T> vec;           // Dynamic array",
                    "std::array<T, N> arr;         // Fixed array",
                    "std::map<K, V> map;           // Ordered map",
                    "std::unordered_map<K, V> um;  // Hash map",
                    "std::set<T> set;              // Ordered set",
                    "std::deque<T> dq;             // Double-ended queue",
                    "```",
                    "",
                    "## Algorithms",
                    "",
                    "```cpp",
                    "#include <algorithm>",
                    "#include <ranges>",
                    "",
                    "// Classic",
                    "std::sort(vec.begin(), vec.end());",
                    "auto it = std::find(vec.begin(), vec.end(), value);",
                    "",
                    "// Ranges (C++20)",
                    "std::ranges::sort(vec);",
                    "auto it = std::ranges::find(vec, value);",
                    "",
                    "// Projections",
                    "std::ranges::sort(people, {}, &Person::name);",
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== C++ specs complete ===")


def fetch_csharp() -> None:
    specs_dir = SPECS_DIR / "csharp"
    log("=== Fetching C# Specs ===")
    for subdir in [
        "stdlib/namespaces",
        "linters/dotnet-analyzers",
        "linters/stylecop",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching C# language specification...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/",
            specs_dir / "spec.md",
            "C# Language Specification",
        )

    if fetch_section("stdlib"):
        log("Fetching .NET API reference...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/dotnet/api/",
            specs_dir / "stdlib" / "overview.md",
            ".NET API Reference",
        )
        log("Fetching .NET namespaces...")
        try:
            ns_html = fetch_url("https://learn.microsoft.com/en-us/dotnet/api/?view=net-8.0")
            namespaces = find_unique(ns_html, r"/dotnet/api/([A-Za-z0-9_.]+)")
        except FetchError as exc:
            log(f"Failed to fetch .NET namespaces: {exc}")
            namespaces = []
        for ns in namespaces:
            log(f"  - dotnet/{ns}")
            fetch_markdown(
                f"https://learn.microsoft.com/en-us/dotnet/api/{ns}?view=net-8.0",
                specs_dir / "stdlib" / "namespaces" / f"{ns}.md",
                ns,
            )

    if fetch_section("linters"):
        log("Fetching .NET analyzers overview...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview",
            specs_dir / "linters" / "dotnet-analyzers" / "overview.md",
            ".NET Code Analysis Overview",
        )
        log("Fetching .NET analyzer rules...")
        fetch_markdown(
            "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/",
            specs_dir / "linters" / "dotnet-analyzers" / "quality-rules.md",
            ".NET Quality Rules",
        )
        try:
            rules_html = fetch_url(
                "https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/"
            )
            dotnet_rules = find_unique(
                rules_html, r"/dotnet/fundamentals/code-analysis/quality-rules/(ca[0-9]{4})"
            )
        except FetchError as exc:
            log(f"Failed to fetch .NET analyzer rules: {exc}")
            dotnet_rules = []
        for rule in dotnet_rules:
            log(f"  - dotnet-analyzers/{rule}")
            fetch_markdown(
                f"https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/{rule}",
                specs_dir / "linters" / "dotnet-analyzers" / f"{rule}.md",
                rule,
            )

        log("Fetching StyleCop analyzers...")
        try:
            stylecop_text = fetch_url(
                "https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/DOCUMENTATION.md"
            )
            write_text(specs_dir / "linters" / "stylecop" / "overview.md", stylecop_text)
            stylecop_rules = find_unique(stylecop_text, r"(SA[0-9]{4})\\.md")
        except FetchError as exc:
            log(f"Failed to fetch StyleCop rules: {exc}")
            write_text(
                specs_dir / "linters" / "stylecop" / "overview.md",
                join_lines(
                    [
                        "# StyleCop Analyzers",
                        "",
                        "See: https://github.com/DotNetAnalyzers/StyleCopAnalyzers",
                    ]
                ),
            )
            stylecop_rules = []

        for rule in stylecop_rules:
            log(f"  - stylecop/{rule}")
            try:
                rule_text = fetch_url(
                    f"https://raw.githubusercontent.com/DotNetAnalyzers/StyleCopAnalyzers/master/documentation/{rule}.md"
                )
                write_text(specs_dir / "linters" / "stylecop" / f"{rule}.md", rule_text)
            except FetchError:
                write_text(
                    specs_dir / "linters" / "stylecop" / f"{rule}.md",
                    join_lines(
                        [
                            f"# {rule}",
                            "",
                            "See: https://github.com/DotNetAnalyzers/StyleCopAnalyzers/blob/master/documentation/",
                        ]
                    ),
                )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# C# Idioms",
                    "",
                    "## Use async/await for I/O",
                    "",
                    "Prefer async APIs for network and disk operations.",
                    "",
                    "## Prefer `using` declarations for disposal",
                    "",
                    "```csharp",
                    "using var stream = File.OpenRead(path);",
                    "```",
                    "",
                    "## Embrace nullable reference types",
                    "",
                    "Enable nullable and use `string?` when values can be null.",
                    "",
                    "## Use records for immutable data",
                    "",
                    "```csharp",
                    "public record User(string Id, string Name);",
                    "```",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# C# Formatters",
                    "",
                    "## dotnet format",
                    "",
                    "See: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "dotnet-format.md",
            join_lines(
                [
                    "# dotnet format Options",
                    "",
                    "See: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== C# specs complete ===")


def fetch_kotlin() -> None:
    specs_dir = SPECS_DIR / "kotlin"
    log("=== Fetching Kotlin Specs ===")
    for subdir in [
        "stdlib/packages",
        "linters/detekt",
        "linters/ktlint",
        "formatters",
        "patterns",
    ]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Kotlin specification...")
        fetch_markdown(
            "https://kotlinlang.org/spec/",
            specs_dir / "spec.md",
            "Kotlin Language Specification",
        )

    if fetch_section("stdlib"):
        log("Fetching Kotlin stdlib reference...")
        fetch_markdown(
            "https://kotlinlang.org/api/core/kotlin-stdlib/",
            specs_dir / "stdlib" / "overview.md",
            "Kotlin Standard Library",
        )
        log("Fetching Kotlin package index...")
        fetch_markdown(
            "https://kotlinlang.org/api/core/kotlin-stdlib/",
            specs_dir / "stdlib" / "packages" / "index.md",
            "Kotlin Packages",
        )
        try:
            packages_html = fetch_url("https://kotlinlang.org/api/core/kotlin-stdlib/")
            packages = find_unique(
                packages_html, r'href="([a-zA-Z0-9_./-]+)/package-summary.html"'
            )
        except FetchError as exc:
            log(f"Failed to fetch Kotlin packages: {exc}")
            packages = []
        for pkg in packages:
            pkg_name = pkg.replace("/", ".")
            log(f"  - kotlin/{pkg_name}")
            fetch_markdown(
                f"https://kotlinlang.org/api/latest/jvm/stdlib/{pkg}/package-summary.html",
                specs_dir / "stdlib" / "packages" / f"{pkg_name}.md",
                pkg_name,
            )

    if fetch_section("linters"):
        log("Fetching detekt rules...")
        fetch_markdown(
            "https://detekt.dev/docs/rules/",
            specs_dir / "linters" / "detekt" / "overview.md",
            "detekt Rules",
        )
        try:
            detekt_html = fetch_url("https://detekt.dev/docs/rules/")
            detekt_rulesets = find_unique(detekt_html, r"/docs/rules/([a-zA-Z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch detekt rulesets: {exc}")
            detekt_rulesets = []
        for ruleset in detekt_rulesets:
            log(f"  - detekt/{ruleset}")
            fetch_markdown(
                f"https://detekt.dev/docs/rules/{ruleset}",
                specs_dir / "linters" / "detekt" / f"{ruleset}.md",
                ruleset,
            )

        log("Fetching ktlint rules...")
        fetch_markdown(
            "https://pinterest.github.io/ktlint/latest/rules/",
            specs_dir / "linters" / "ktlint" / "overview.md",
            "ktlint Rules",
        )
        try:
            ktlint_html = fetch_url("https://pinterest.github.io/ktlint/latest/rules/")
            ktlint_rules = find_unique(ktlint_html, r'href="#([a-z0-9-]+)"')
        except FetchError as exc:
            log(f"Failed to fetch ktlint rules: {exc}")
            ktlint_rules = []
        for rule in ktlint_rules:
            log(f"  - ktlint/{rule}")
            write_text(
                specs_dir / "linters" / "ktlint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://pinterest.github.io/ktlint/latest/rules/#{rule}",
                    ]
                ),
            )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Kotlin Idioms",
                    "",
                    "## Prefer data classes for simple models",
                    "",
                    "```kotlin",
                    "data class User(val id: String, val name: String)",
                    "```",
                    "",
                    "## Use sealed classes for closed hierarchies",
                    "",
                    "```kotlin",
                    "sealed interface Result",
                    "data class Success(val value: String) : Result",
                    "data class Failure(val error: Throwable) : Result",
                    "```",
                    "",
                    "## Use `let`, `apply`, and `also` for scoped operations",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Kotlin Formatters",
                    "",
                    "## ktlint",
                    "",
                    "See: https://pinterest.github.io/ktlint/latest/rules/",
                    "",
                    "## ktfmt",
                    "",
                    "See: https://github.com/facebook/ktfmt",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "ktfmt.md",
            join_lines(
                [
                    "# ktfmt Options",
                    "",
                    "See: https://github.com/facebook/ktfmt",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Kotlin specs complete ===")


def fetch_lua() -> None:
    specs_dir = SPECS_DIR / "lua"
    log("=== Fetching Lua Specs ===")
    for subdir in ["stdlib", "linters/luacheck", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        log("Fetching Lua 5.4 manual...")
        fetch_markdown(
            "https://www.lua.org/manual/5.4/",
            specs_dir / "spec.md",
            "Lua 5.4 Reference Manual",
        )

    if fetch_section("stdlib"):
        log("Fetching Lua standard libraries...")
        fetch_markdown(
            "https://www.lua.org/manual/5.4/manual.html#6",
            specs_dir / "stdlib" / "overview.md",
            "Lua Standard Libraries",
        )

    if fetch_section("linters"):
        log("Fetching luacheck rules...")
        fetch_markdown(
            "https://luacheck.readthedocs.io/en/stable/warnings.html",
            specs_dir / "linters" / "luacheck" / "overview.md",
            "luacheck Warnings",
        )
        try:
            luacheck_html = fetch_url("https://luacheck.readthedocs.io/en/stable/warnings.html")
            luacheck_codes = find_unique(luacheck_html, r"(W[0-9]{3})")
        except FetchError as exc:
            log(f"Failed to fetch luacheck warnings: {exc}")
            luacheck_codes = []
        for code in luacheck_codes:
            log(f"  - luacheck/{code}")
            write_text(
                specs_dir / "linters" / "luacheck" / f"{code}.md",
                join_lines(
                    [
                        f"# {code}",
                        "",
                        f"See: https://luacheck.readthedocs.io/en/stable/warnings.html#{code}",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Lua Formatters",
                    "",
                    "## stylua",
                    "",
                    "See: https://github.com/JohnnyMorganz/StyLua",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "stylua.md",
            join_lines(
                [
                    "# stylua Options",
                    "",
                    "See: https://github.com/JohnnyMorganz/StyLua#configuration",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Lua Idioms",
                    "",
                    "## Use local scope",
                    "",
                    "```lua",
                    "local count = 0",
                    "```",
                    "",
                    "## Prefer ipairs/pairs",
                    "",
                    "```lua",
                    "for i, v in ipairs(items) do",
                    "  print(i, v)",
                    "end",
                    "```",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Lua specs complete ===")

def fetch_php() -> None:
    specs_dir = SPECS_DIR / "php"
    log("=== Fetching PHP Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://www.php.net/manual/en/langref.php",
            specs_dir / "spec.md",
            "PHP Language Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://www.php.net/manual/en/funcref.php",
            specs_dir / "stdlib" / "overview.md",
            "PHP Function Reference",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# PHP Linters",
                    "",
                    "PHP has no single official linter; popular choices include PHPStan and Psalm.",
                    "",
                    "See:",
                    "- https://phpstan.org/",
                    "- https://psalm.dev/",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# PHP Formatters",
                    "",
                    "There is no official formatter; a common choice is PHP-CS-Fixer.",
                    "",
                    "See: https://cs.symfony.com/",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# PHP Idioms",
                    "",
                    "## Prefer strict types",
                    "",
                    "Use `declare(strict_types=1);` in modern codebases.",
                    "",
                    "## Use typed properties and return types",
                    "",
                    "They improve clarity and static analysis.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== PHP specs complete ===")


def fetch_ruby() -> None:
    specs_dir = SPECS_DIR / "ruby"
    log("=== Fetching Ruby Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://docs.ruby-lang.org/en/3.3/doc/syntax_rdoc.html",
            specs_dir / "spec.md",
            "Ruby Syntax Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://docs.ruby-lang.org/en/3.3/",
            specs_dir / "stdlib" / "overview.md",
            "Ruby Standard Library",
        )

    if fetch_section("linters"):
        fetch_markdown(
            "https://docs.rubocop.org/rubocop/",
            specs_dir / "linters" / "overview.md",
            "RuboCop Overview",
        )

    if fetch_section("formatters"):
        fetch_markdown(
            "https://docs.rubocop.org/rubocop/",
            specs_dir / "formatters" / "overview.md",
            "RuboCop Formatting",
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Ruby Idioms",
                    "",
                    "## Prefer `each` and iterators",
                    "",
                    "Use collection iterators instead of indexed loops.",
                    "",
                    "## Use symbols for identifiers",
                    "",
                    "Symbols are efficient for keys and labels.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Ruby specs complete ===")


def fetch_dart() -> None:
    specs_dir = SPECS_DIR / "dart"
    log("=== Fetching Dart Specs ===")
    for subdir in ["stdlib", "linters/dart-linter", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://dart.dev/guides/language/spec",
            specs_dir / "spec.md",
            "Dart Language Specification",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://api.dart.dev/stable/",
            specs_dir / "stdlib" / "overview.md",
            "Dart API Reference",
        )

    if fetch_section("linters"):
        fetch_markdown(
            "https://dart.dev/tools/linter-rules",
            specs_dir / "linters" / "dart-linter" / "overview.md",
            "Dart Linter Rules",
        )
        try:
            rules_html = fetch_url("https://dart.dev/tools/linter-rules")
            rules = find_unique(rules_html, r"/tools/linter-rules/([A-Za-z0-9_-]+)")
        except FetchError as exc:
            log(f"Failed to fetch Dart linter rules: {exc}")
            rules = []

        for rule in rules:
            log(f"  - dart-linter/{rule}")
            write_text(
                specs_dir / "linters" / "dart-linter" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://dart.dev/tools/linter-rules/{rule}",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "dart-format.md",
            join_lines(
                [
                    "# dart format",
                    "",
                    "See: https://dart.dev/tools/dart-format",
                ]
            ),
        )
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Dart Formatters",
                    "",
                    "- dart format",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Dart Idioms",
                    "",
                    "## Prefer collection literals",
                    "",
                    "Use list/map/set literals over constructors.",
                    "",
                    "## Use async/await for futures",
                    "",
                    "Prefer async/await to chained `then` calls.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Dart specs complete ===")


def fetch_r() -> None:
    specs_dir = SPECS_DIR / "r"
    log("=== Fetching R Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://cran.r-project.org/doc/manuals/r-release/R-lang.html",
            specs_dir / "spec.md",
            "R Language Definition",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://cran.r-project.org/manuals.html",
            specs_dir / "stdlib" / "overview.md",
            "R Manuals and Standard Library",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# R Linters",
                    "",
                    "There is no official linter; common tooling includes lintr.",
                    "",
                    "See: https://github.com/r-lib/lintr",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# R Formatters",
                    "",
                    "Common formatters include styler.",
                    "",
                    "See: https://styler.r-lib.org/",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# R Idioms",
                    "",
                    "## Prefer vectorized operations",
                    "",
                    "Use vectorized functions instead of explicit loops.",
                    "",
                    "## Use explicit column names",
                    "",
                    "Avoid positional indexing for data frames.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== R specs complete ===")


def fetch_julia() -> None:
    specs_dir = SPECS_DIR / "julia"
    log("=== Fetching Julia Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://docs.julialang.org/en/v1/",
            specs_dir / "spec.md",
            "Julia Manual",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/",
            specs_dir / "stdlib" / "overview.md",
            "Julia Standard Library",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Julia Linters",
                    "",
                    "There is no official linter; JET and StaticLint are common.",
                    "",
                    "See:",
                    "- https://github.com/aviatesk/JET.jl",
                    "- https://github.com/julia-vscode/StaticLint.jl",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Julia Formatters",
                    "",
                    "A common formatter is JuliaFormatter.",
                    "",
                    "See: https://github.com/domluna/JuliaFormatter.jl",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Julia Idioms",
                    "",
                    "## Prefer dot broadcasting",
                    "",
                    "Use dot syntax for element-wise operations.",
                    "",
                    "## Type-stable functions",
                    "",
                    "Avoid type instability in hot paths.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Julia specs complete ===")


def fetch_scala() -> None:
    specs_dir = SPECS_DIR / "scala"
    log("=== Fetching Scala Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://docs.scala-lang.org/scala3/reference/",
            specs_dir / "spec.md",
            "Scala 3 Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://www.scala-lang.org/api/",
            specs_dir / "stdlib" / "overview.md",
            "Scala Standard Library API",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Scala Linters",
                    "",
                    "Common tools include Scalafix and WartRemover.",
                    "",
                    "See:",
                    "- https://scalacenter.github.io/scalafix/",
                    "- https://www.wartremover.org/",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Scala Formatters",
                    "",
                    "Scalafmt is the standard formatter.",
                    "",
                    "See: https://scalameta.org/scalafmt/",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Scala Idioms",
                    "",
                    "## Prefer immutable collections",
                    "",
                    "Use immutable collections for safer code.",
                    "",
                    "## Use pattern matching",
                    "",
                    "Pattern matching is idiomatic for branching logic.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Scala specs complete ===")


def fetch_elixir() -> None:
    specs_dir = SPECS_DIR / "elixir"
    log("=== Fetching Elixir Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://hexdocs.pm/elixir/syntax-reference.html",
            specs_dir / "spec.md",
            "Elixir Syntax Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://hexdocs.pm/elixir/api-reference.html",
            specs_dir / "stdlib" / "overview.md",
            "Elixir Standard Library",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Elixir Linters",
                    "",
                    "Common tools include Credo.",
                    "",
                    "See: https://hexdocs.pm/credo/",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Elixir Formatters",
                    "",
                    "Use the built-in formatter.",
                    "",
                    "See: https://hexdocs.pm/mix/Mix.Tasks.Format.html",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Elixir Idioms",
                    "",
                    "## Prefer pattern matching",
                    "",
                    "Use pattern matching in function heads and case statements.",
                    "",
                    "## Keep functions pure",
                    "",
                    "Avoid side effects in core logic.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Elixir specs complete ===")


def fetch_clojure() -> None:
    specs_dir = SPECS_DIR / "clojure"
    log("=== Fetching Clojure Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://clojure.org/reference/reader",
            specs_dir / "spec.md",
            "Clojure Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://clojure.github.io/clojure/",
            specs_dir / "stdlib" / "overview.md",
            "Clojure API Reference",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Clojure Linters",
                    "",
                    "Common linters include clj-kondo and eastwood.",
                    "",
                    "See:",
                    "- https://github.com/clj-kondo/clj-kondo",
                    "- https://github.com/jonase/eastwood",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Clojure Formatters",
                    "",
                    "A common formatter is zprint.",
                    "",
                    "See: https://github.com/kkinnear/zprint",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Clojure Idioms",
                    "",
                    "## Prefer immutable data",
                    "",
                    "Use persistent data structures by default.",
                    "",
                    "## Compose with threading macros",
                    "",
                    "Use `->` and `->>` for readable pipelines.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Clojure specs complete ===")


def fetch_haskell() -> None:
    specs_dir = SPECS_DIR / "haskell"
    log("=== Fetching Haskell Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        try:
            data = fetch_bytes("https://www.haskell.org/definition/haskell2010.pdf")
            (specs_dir / "haskell2010.pdf").write_bytes(data)
            write_text(
                specs_dir / "spec.md",
                join_lines(
                    [
                        "# Haskell 2010 Report",
                        "",
                        "See: https://www.haskell.org/definition/haskell2010.pdf",
                    ]
                ),
            )
        except FetchError as exc:
            log(f"Failed to fetch Haskell report: {exc}")
            write_stub(
                specs_dir / "spec.md",
                "Haskell 2010 Report",
                "https://www.haskell.org/definition/haskell2010.pdf",
            )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://hackage.haskell.org/package/base/docs/",
            specs_dir / "stdlib" / "overview.md",
            "Haskell Base Library",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Haskell Linters",
                    "",
                    "HLint is the most common linter.",
                    "",
                    "See: https://github.com/ndmitchell/hlint",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Haskell Formatters",
                    "",
                    "Common formatters include fourmolu and ormolu.",
                    "",
                    "See:",
                    "- https://github.com/fourmolu/fourmolu",
                    "- https://github.com/tweag/ormolu",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Haskell Idioms",
                    "",
                    "## Prefer pure functions",
                    "",
                    "Keep side effects in the IO layer.",
                    "",
                    "## Use pattern matching",
                    "",
                    "Pattern matching is a core idiom.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Haskell specs complete ===")


def fetch_zig() -> None:
    specs_dir = SPECS_DIR / "zig"
    log("=== Fetching Zig Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://ziglang.org/documentation/master/",
            specs_dir / "spec.md",
            "Zig Language Reference",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://ziglang.org/documentation/master/std/",
            specs_dir / "stdlib" / "overview.md",
            "Zig Standard Library",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# Zig Linters",
                    "",
                    "There is no official linter; rely on the compiler and zig fmt.",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Zig Formatters",
                    "",
                    "Use the built-in formatter.",
                    "",
                    "See: https://ziglang.org/documentation/master/#Formatting",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Zig Idioms",
                    "",
                    "## Prefer explicit error handling",
                    "",
                    "Use `try` and `catch` to propagate errors.",
                    "",
                    "## Use `defer` for cleanup",
                    "",
                    "Keep resource management explicit.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Zig specs complete ===")


def fetch_ocaml() -> None:
    specs_dir = SPECS_DIR / "ocaml"
    log("=== Fetching OCaml Specs ===")
    for subdir in ["stdlib", "linters", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://ocaml.org/manual/",
            specs_dir / "spec.md",
            "OCaml Manual",
        )

    if fetch_section("stdlib"):
        fetch_markdown(
            "https://ocaml.org/manual/stdlib.html",
            specs_dir / "stdlib" / "overview.md",
            "OCaml Standard Library",
        )

    if fetch_section("linters"):
        write_text(
            specs_dir / "linters" / "overview.md",
            join_lines(
                [
                    "# OCaml Linters",
                    "",
                    "A common linter is ocamlformat (formatting) and odoclint.",
                    "",
                    "See:",
                    "- https://github.com/ocaml-ppx/ocamlformat",
                    "- https://github.com/ocaml/odoc",
                ]
            ),
        )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# OCaml Formatters",
                    "",
                    "ocamlformat is the standard formatter.",
                    "",
                    "See: https://github.com/ocaml-ppx/ocamlformat",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# OCaml Idioms",
                    "",
                    "## Prefer pattern matching",
                    "",
                    "Use pattern matching for algebraic data types.",
                    "",
                    "## Use immutable data",
                    "",
                    "Favor immutability in core logic.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== OCaml specs complete ===")


def fetch_markdown_lang() -> None:
    specs_dir = SPECS_DIR / "markdown"
    log("=== Fetching Markdown Specs ===")
    for subdir in ["stdlib", "linters/markdownlint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://spec.commonmark.org/0.30/",
            specs_dir / "spec.md",
            "CommonMark Specification",
        )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Markdown Standard Library",
                    "",
                    "Markdown has no standard library.",
                ]
            ),
        )

    if fetch_section("linters"):
        fetch_markdown(
            "https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md",
            specs_dir / "linters" / "markdownlint" / "overview.md",
            "markdownlint Rules",
        )
        try:
            rules_md = fetch_url(
                "https://raw.githubusercontent.com/DavidAnson/markdownlint/main/doc/Rules.md"
            )
            rules = find_unique(rules_md, r"\b(MD[0-9]{3})\b")
        except FetchError as exc:
            log(f"Failed to fetch markdownlint rules: {exc}")
            rules = []

        for rule in rules:
            log(f"  - markdownlint/{rule}")
            write_text(
                specs_dir / "linters" / "markdownlint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        "See: https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Markdown Formatters",
                    "",
                    "Common formatters include Prettier and markdownfmt.",
                    "",
                    "See:",
                    "- https://prettier.io/",
                    "- https://github.com/shurcooL/markdownfmt",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Markdown Idioms",
                    "",
                    "## Keep headings hierarchical",
                    "",
                    "Avoid skipping heading levels.",
                    "",
                    "## Use blank lines for separation",
                    "",
                    "Separate blocks with blank lines for readability.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Markdown specs complete ===")


def fetch_yaml() -> None:
    specs_dir = SPECS_DIR / "yaml"
    log("=== Fetching YAML Specs ===")
    for subdir in ["stdlib", "linters/yamllint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://yaml.org/spec/1.2.2/",
            specs_dir / "spec.md",
            "YAML 1.2.2 Specification",
        )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# YAML Standard Library",
                    "",
                    "YAML has no standard library.",
                ]
            ),
        )

    if fetch_section("linters"):
        fetch_markdown(
            "https://yamllint.readthedocs.io/en/stable/rules.html",
            specs_dir / "linters" / "yamllint" / "overview.md",
            "yamllint Rules",
        )
        try:
            rules_html = fetch_url("https://yamllint.readthedocs.io/en/stable/rules.html")
            rules = find_unique(rules_html, r"rules\.html#([a-z0-9-]+)")
        except FetchError as exc:
            log(f"Failed to fetch yamllint rules: {exc}")
            rules = []

        for rule in rules:
            log(f"  - yamllint/{rule}")
            write_text(
                specs_dir / "linters" / "yamllint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        f"See: https://yamllint.readthedocs.io/en/stable/rules.html#{rule}",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# YAML Formatters",
                    "",
                    "Common formatters include Prettier and yamlfix.",
                    "",
                    "See:",
                    "- https://prettier.io/",
                    "- https://github.com/lyz-code/yamlfix",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# YAML Idioms",
                    "",
                    "## Use explicit quoting",
                    "",
                    "Quote strings that look like booleans or numbers.",
                    "",
                    "## Keep indentation consistent",
                    "",
                    "Use two spaces and avoid tabs.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== YAML specs complete ===")


def fetch_dockerfile() -> None:
    specs_dir = SPECS_DIR / "dockerfile"
    log("=== Fetching Dockerfile Specs ===")
    for subdir in ["stdlib", "linters/hadolint", "formatters", "patterns"]:
        (specs_dir / subdir).mkdir(parents=True, exist_ok=True)

    if fetch_section("spec"):
        fetch_markdown(
            "https://docs.docker.com/engine/reference/builder/",
            specs_dir / "spec.md",
            "Dockerfile Reference",
        )

    if fetch_section("stdlib"):
        write_text(
            specs_dir / "stdlib" / "overview.md",
            join_lines(
                [
                    "# Dockerfile Standard Library",
                    "",
                    "Dockerfile has no standard library.",
                ]
            ),
        )

    if fetch_section("linters"):
        fetch_markdown(
            "https://github.com/hadolint/hadolint#rules",
            specs_dir / "linters" / "hadolint" / "overview.md",
            "Hadolint Rules",
        )
        try:
            rules_md = fetch_url("https://raw.githubusercontent.com/hadolint/hadolint/master/README.md")
            rules = find_unique(rules_md, r"\b(DL[0-9]{4})\b")
        except FetchError as exc:
            log(f"Failed to fetch hadolint rules: {exc}")
            rules = []

        for rule in rules:
            log(f"  - hadolint/{rule}")
            write_text(
                specs_dir / "linters" / "hadolint" / f"{rule}.md",
                join_lines(
                    [
                        f"# {rule}",
                        "",
                        "See: https://github.com/hadolint/hadolint#rules",
                    ]
                ),
            )

    if fetch_section("formatters"):
        write_text(
            specs_dir / "formatters" / "overview.md",
            join_lines(
                [
                    "# Dockerfile Formatters",
                    "",
                    "There is no official formatter; use linting and consistent style.",
                ]
            ),
        )

    if fetch_section("patterns"):
        write_text(
            specs_dir / "patterns" / "idioms.md",
            join_lines(
                [
                    "# Dockerfile Idioms",
                    "",
                    "## Use multi-stage builds",
                    "",
                    "Keep runtime images minimal.",
                    "",
                    "## Pin base images",
                    "",
                    "Prefer explicit tags or digests.",
                ]
            ),
        )

    write_fetched_at(specs_dir)
    stamp_versions()
    log("=== Dockerfile specs complete ===")


# Additional language fetchers are appended below.


FETCHERS = {
    "assembly": fetch_assembly,
    "basic": fetch_basic,
    "bash": fetch_bash,
    "batch": fetch_batch,
    "c": fetch_c,
    "cpp": fetch_cpp,
    "csharp": fetch_csharp,
    "css": fetch_css,
    "git": fetch_git,
    "html": fetch_html,
    "javascript": fetch_javascript,
    "typescript": fetch_typescript,
    "go": fetch_go,
    "java": fetch_java,
    "kotlin": fetch_kotlin,
    "lua": fetch_lua,
    "php": fetch_php,
    "ruby": fetch_ruby,
    "dart": fetch_dart,
    "r": fetch_r,
    "julia": fetch_julia,
    "scala": fetch_scala,
    "elixir": fetch_elixir,
    "clojure": fetch_clojure,
    "haskell": fetch_haskell,
    "zig": fetch_zig,
    "ocaml": fetch_ocaml,
    "markdown": fetch_markdown_lang,
    "yaml": fetch_yaml,
    "dockerfile": fetch_dockerfile,
    "python": fetch_python,
    "powershell": fetch_powershell,
    "rust": fetch_rust,
    "sql": fetch_sql,
    "swift": fetch_swift,
}


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: fetch.py <language>")
    language = sys.argv[1]
    fetcher = FETCHERS.get(language)
    if fetcher:
        fetcher()
        return
    raise SystemExit(f"Unsupported language: {language}")


if __name__ == "__main__":
    main()
