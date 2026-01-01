#!/bin/bash
# Fetch Git references, command docs, linters, formatters, and patterns

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/git"

echo "=== Fetching Git Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib,linters/{gitlint,commitlint},formatters,patterns}

echo "Fetching Git reference..."
curl -sL "https://git-scm.com/docs" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/spec.md" 2>/dev/null || \
  echo "# Git Reference\n\nSee: https://git-scm.com/docs" > "$SPECS_DIR/spec.md"

echo "Fetching Git command reference..."
curl -sL "https://git-scm.com/docs/git" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/overview.md" 2>/dev/null || \
  echo "# Git Command Reference\n\nSee: https://git-scm.com/docs/git" > "$SPECS_DIR/stdlib/overview.md"

echo "Fetching gitlint rules..."
curl -sL "https://jorisroovers.com/gitlint/rules/" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/gitlint/overview.md" 2>/dev/null || \
  echo "# gitlint Rules\n\nSee: https://jorisroovers.com/gitlint/rules/" > "$SPECS_DIR/linters/gitlint/overview.md"

echo "Fetching commitlint rules..."
curl -sL "https://commitlint.js.org/#/reference-rules" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/commitlint/overview.md" 2>/dev/null || \
  echo "# commitlint Rules\n\nSee: https://commitlint.js.org/#/reference-rules" > "$SPECS_DIR/linters/commitlint/overview.md"

cat > "$SPECS_DIR/formatters/overview.md" << 'EOF_FMT'
# Git Formatters

There is no widely adopted code formatter for Git itself.

## Commit message formatting tools

- commitlint: https://commitlint.js.org/
- commitizen: https://commitizen-tools.github.io/commitizen/
EOF_FMT

cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF_PAT'
# Git Idioms

## Keep commits atomic

One logical change per commit.

## Prefer rebase for local history cleanup

```bash
git fetch origin
git rebase origin/main
```

## Use conventional commit messages

```
feat(parser): add streaming mode
fix(api): handle nil response
```

## Avoid rewriting shared history

Do not force-push to shared branches unless agreed.
EOF_PAT

cat > "$SPECS_DIR/patterns/conventions.md" << 'EOF_CONV'
# Git Conventions

## Conventional Commits

Specification: https://www.conventionalcommits.org/en/v1.0.0/

## Branching

- Trunk-based development: https://trunkbaseddevelopment.com/
- GitHub Flow: https://docs.github.com/en/get-started/quickstart/github-flow
- GitFlow (legacy): https://nvie.com/posts/a-successful-git-branching-model/

## Releases and Changelogs

- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
EOF_CONV

echo "=== Git specs complete ==="
