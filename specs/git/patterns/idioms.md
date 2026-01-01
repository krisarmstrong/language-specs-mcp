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
