# Bash Generation Checklist

**Read this BEFORE writing shell scripts. Bash will betray you otherwise.**

## Critical: You Must Do These

### 1. ALWAYS Quote Variables (SC2086)
```bash
# BAD - word splitting and globbing
rm $file
cp $src $dest

# GOOD - always quote
rm "$file"
cp "$src" "$dest"
```
This is the #1 most violated rule. When in doubt, quote it.

### 2. ALWAYS Quote Command Substitutions (SC2046)
```bash
# BAD - word splitting on output
files=$(find . -name "*.txt")
process $files

# GOOD - quote the substitution
files="$(find . -name "*.txt")"
# Or better, use arrays/while loops
```

### 3. Use `[[ ]]` Not `[ ]` for Tests
```bash
# BAD - POSIX but error-prone
if [ $var = "value" ]; then

# GOOD - bash extended test, safer
if [[ "$var" == "value" ]]; then
```

### 4. Use `$()` Not Backticks
```bash
# BAD - hard to nest, hard to read
result=`command`

# GOOD - modern, nestable
result="$(command)"
```

### 5. Start Scripts with Strict Mode
```bash
#!/usr/bin/env bash
set -euo pipefail

# -e: exit on error
# -u: error on undefined variables
# -o pipefail: catch errors in pipes
```

## Important: Strong Recommendations

### 6. Use `readonly` for Constants
```bash
# BAD - can be accidentally modified
CONFIG_PATH="/etc/myapp/config"

# GOOD - immutable
readonly CONFIG_PATH="/etc/myapp/config"
```

### 7. Use `local` in Functions
```bash
# BAD - pollutes global scope
my_func() {
    result="something"
}

# GOOD - local scope
my_func() {
    local result="something"
}
```

### 8. Check Commands Exist Before Using
```bash
# BAD - cryptic error if missing
jq '.key' file.json

# GOOD - clear error message
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed" >&2
    exit 1
fi
```

### 9. Use Arrays for Lists, Not Strings
```bash
# BAD - breaks on spaces/special chars
files="file1.txt file2.txt"
for f in $files; do

# GOOD - proper array
files=("file1.txt" "file2.txt" "file with spaces.txt")
for f in "${files[@]}"; do
```

### 10. Prefer `printf` Over `echo`
```bash
# BAD - behavior varies across systems
echo -e "line1\nline2"

# GOOD - consistent behavior
printf '%s\n' "line1" "line2"
```

## File Operations: Be Careful

### 11. Quote Paths in Redirections (SC2094)
```bash
# BAD - globbing can occur
cat file > $output

# GOOD - quoted
cat file > "$output"
```

### 12. Use `mktemp` for Temp Files
```bash
# BAD - predictable, race conditions
tmpfile="/tmp/myapp.tmp"

# GOOD - secure, unique
tmpfile="$(mktemp)"
trap 'rm -f "$tmpfile"' EXIT
```

### 13. Always Clean Up with `trap`
```bash
# GOOD - cleanup on exit
cleanup() {
    rm -f "$tmpfile"
}
trap cleanup EXIT
```

## Conditionals: Common Mistakes

### 14. String Comparison Uses `==` Not `=`
```bash
# Works but confusing (POSIX)
if [[ "$a" = "$b" ]]; then

# GOOD - clearer intent
if [[ "$a" == "$b" ]]; then
```

### 15. Integer Comparison Uses `-eq` Not `==`
```bash
# BAD - string comparison
if [[ "$count" == "5" ]]; then

# GOOD - numeric comparison
if [[ "$count" -eq 5 ]]; then
```

### 16. Check If Variable Is Set
```bash
# BAD - fails if unset with set -u
if [[ "$var" == "" ]]; then

# GOOD - proper empty/unset check
if [[ -z "${var:-}" ]]; then
```

## Security: Never Do These

### 17. Never Put Variables in Command Position Unquoted
```bash
# DANGEROUS - command injection
$user_command

# If you must run dynamic commands, validate first
```

### 18. Validate All External Input
```bash
# BAD - trusts input
rm -rf "$1"

# BETTER - validate
if [[ "$1" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    rm -rf "$1"
fi
```

### 19. Use `--` to End Option Parsing
```bash
# BAD - filename starting with - breaks this
rm $filename

# GOOD - -- signals end of options
rm -- "$filename"
```

---

**Quick Reference - Copy This Mental Model:**
- Quote EVERYTHING: `"$var"`, `"$(cmd)"`, `"${array[@]}"`
- Use `[[ ]]` for tests
- Use `$()` not backticks
- Start with `set -euo pipefail`
- Use `local` in functions
- Use arrays for lists
- Use `mktemp` + `trap` for temp files
- Use `--` before filenames from variables
