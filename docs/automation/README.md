# Automation Templates

This folder contains default automation templates to refresh data on a schedule.

## Cron

- Template: `docs/automation/cron.txt`
- Customize the repo path as needed.
- Uses `./scripts/automation/refresh.sh` (loads `.env` if present).

## Launchd (macOS)

- Template: `docs/automation/com.specforge.refresh.plist`
- Install with:

```bash
cp docs/automation/com.specforge.refresh.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.specforge.refresh.plist
```

The install script `scripts/automation/install.sh` will replace `__SPECFORGE_ROOT__`
with your local repo path and load the agent automatically.

## Environment

If you need `GITHUB_TOKEN`, place it in `.env` (see `.env.example`). The `.env`
file is ignored by git.

## Tokens

Create a token in GitHub Settings → Developer settings → Personal access tokens.
No scopes are required for public data. If you already use GitHub CLI, `gh auth token`
prints a usable token.
