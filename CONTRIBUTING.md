# Contributing

Thanks for contributing. This repo is a curated collection of language specs, stdlib references, linters, formatters, and patterns delivered through an MCP server.

## Principles

- Prefer authoritative sources.
- Keep fetch scripts deterministic and idempotent.
- Preserve existing file naming conventions.

## Updating Specs

Use the fetch scripts to refresh content:

```bash
npm run fetch:all
```

Notes:
- Fetch scripts overwrite files they generate; they do not delete extra files.
- Some sources change HTML structure; if a scrape breaks, add a fallback link.

## Adding a New Language

1. Add the language to `src/index.ts` (`SupportedLanguage` and `LANGUAGES`).
2. Create `scripts/fetch-<language>.sh`.
3. Add the script to `package.json`.
4. Update `README.md` supported language table.

## Adding Linters/Formatters

1. Create `specs/<language>/linters/<tool>/`.
2. Update the fetch script to populate the linter rules.
3. Add `specs/<language>/formatters/overview.md` (and option docs where available).

## Git Standards

- Use Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
- Keep commits atomic and focused.
- Update `CHANGELOG.md` for user-facing changes.

### Commitlint (Enforcement)

Install dependencies and enable hooks:

```bash
npm install
npm run prepare
```

Manual check:

```bash
npm run commitlint
```

## Issues and PRs

- Use the GitHub issue templates.
- Link PRs to issues when possible.
- Run `npm run lint` and `npm run build` before opening a PR.

## Notes on Scope Scripts

`fetch:stdlib`, `fetch:linters`, and `fetch:formatters` currently call `fetch:all`.
They are placeholders to allow future scope-specific fetches without changing user workflows.
