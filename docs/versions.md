# Tool Versions

This file records the pinned versions for key toolchains and formatters/linters.

Source of truth: `tools/versions.json`.

## Validate versions

```bash
npm run validate:versions
```

Typical flow:

```bash
npm run update:versions
npm run stamp:versions
npm run validate:versions
```

## Check latest versions (network)

```bash
npm run validate:versions:latest
```

## Update registry from upstream (network)

```bash
npm run update:versions
```

## Stamp versions into docs

```bash
npm run stamp:versions
```

## Version report

```bash
npm run report:versions
npm run report:versions:latest
```

Add new tools by editing `tools/versions.json` and adding file references that should contain the version string.
