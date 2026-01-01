# Bash Idioms

## Strict mode

```bash
set -euo pipefail
IFS=$'\n\t'
```

## Prefer [[ ]] tests

```bash
if [[ -f "$path" ]]; then
  echo "exists"
fi
```

## Quote variables

```bash
echo "$var"
```
