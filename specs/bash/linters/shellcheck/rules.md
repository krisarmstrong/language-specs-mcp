# ShellCheck Rules

## Quoting

### SC2086 - Double quote to prevent globbing and word splitting

```bash
# BAD
echo $var
rm $files
cmd $args

# GOOD
echo "$var"
rm "$files"
cmd "$args"

# Array expansion
cmd "${array[@]}"
```

### SC2046 - Quote command substitution to prevent word splitting

```bash
# BAD
files=$(ls)
echo $files

# GOOD
files="$(ls)"
echo "$files"

# Or use array
mapfile -t files < <(ls)
```

### SC2048 - Use "$@" (with quotes) to prevent whitespace problems

```bash
# BAD
for arg in $@; do
for arg in $*; do

# GOOD
for arg in "$@"; do
```

### SC2066 - Since you double quoted this, it won't glob

```bash
# BAD
for file in "*.txt"; do    # Quotes prevent globbing

# GOOD
for file in *.txt; do
```

### SC2027 - String concatenation

```bash
# BAD (missing quotes in parts)
echo "Hello "$name""

# GOOD
echo "Hello $name"
echo "Hello ${name}"
```

### SC2016 - Single quotes prevent expansion

```bash
# BAD (if you want expansion)
echo 'Hello $USER'    # Outputs literal $USER

# GOOD
echo "Hello $USER"
```

## Variables

### SC2034 - Unused variable

```bash
# BAD
unused_var="value"  # Never used

# GOOD
export USED_VAR="value"
# or
# shellcheck disable=SC2034
UNUSED_BUT_INTENTIONAL="value"
```

### SC2154 - Variable referenced but not assigned

```bash
# BAD
echo "$undefined_var"

# GOOD
undefined_var=""
echo "$undefined_var"

# Or with default
echo "${undefined_var:-default}"
```

### SC2155 - Declare and assign separately

```bash
# BAD
local var=$(command)    # Masks exit code

# GOOD
local var
var=$(command)
```

### SC2229 - This does not read 'var'

```bash
# BAD
read foo$bar    # Trying to build variable name

# GOOD
read -r "$foo$bar"  # If intentional
```

### SC2163 - Exporting specific variables

```bash
# BAD
export foo=$bar    # May not work as expected

# GOOD
foo="$bar"
export foo
```

## Control Flow

### SC2015 - Use if instead of && ||

```bash
# BAD
[[ condition ]] && echo "yes" || echo "no"  # If echo fails, "no" runs

# GOOD
if [[ condition ]]; then
    echo "yes"
else
    echo "no"
fi
```

### SC2181 - Check exit code directly

```bash
# BAD
command
if [[ $? -eq 0 ]]; then

# GOOD
if command; then
```

### SC2143 - Use grep -q instead of comparing output

```bash
# BAD
if [[ $(grep pattern file) ]]; then

# GOOD
if grep -q pattern file; then
```

### SC2072/SC2071 - Use arithmetic operators for numbers

```bash
# BAD
[[ $a > $b ]]     # String comparison!

# GOOD
[[ $a -gt $b ]]   # Numeric comparison
(( a > b ))       # Arithmetic
```

### SC2194 - Constant in case condition

```bash
# BAD
case "fixed" in
    pattern) ;;
esac

# GOOD
case "$variable" in
    pattern) ;;
esac
```

## Commands

### SC2164 - Use cd ... || exit

```bash
# BAD
cd /some/dir
command         # Runs even if cd failed

# GOOD
cd /some/dir || exit 1
command

# Or
cd /some/dir || { echo "Failed to cd" >&2; exit 1; }
```

### SC2162 - Use read -r

```bash
# BAD
read line       # Backslashes interpreted

# GOOD
read -r line
```

### SC2002 - Useless cat

```bash
# BAD
cat file | grep pattern

# GOOD
grep pattern file
grep pattern < file
```

### SC2012 - Use find instead of ls

```bash
# BAD
for file in $(ls); do    # Breaks on spaces

# GOOD
for file in *; do
# Or
find . -maxdepth 1 -type f -print0 | while IFS= read -r -d '' file; do
```

### SC2006 - Use $() instead of backticks

```bash
# BAD
result=`command`

# GOOD
result=$(command)
```

### SC2001 - Use parameter expansion

```bash
# BAD
echo "$var" | sed 's/foo/bar/'

# GOOD
echo "${var/foo/bar}"
```

### SC2028 - echo may not expand escape sequences

```bash
# BAD
echo "Line1\nLine2"    # May not work

# GOOD
printf 'Line1\nLine2\n'
echo -e "Line1\nLine2"  # Bash
echo $'Line1\nLine2'    # Bash
```

### SC2009 - Use pgrep instead of grep ps

```bash
# BAD
ps aux | grep nginx

# GOOD
pgrep nginx
pgrep -f nginx
```

### SC2185 - Arithmetic in command

```bash
# BAD
result=$[1+2]      # Old syntax

# GOOD
result=$((1+2))
```

## Arrays

### SC2128 - Expanding an array without an index

```bash
# BAD
echo $array         # Only first element

# GOOD
echo "${array[@]}"  # All elements
echo "${array[0]}"  # First element
```

### SC2199 - Arrays implicitly concatenate

```bash
# BAD
[[ ${array[@]} = "something" ]]  # Wrong comparison

# GOOD
[[ "${array[*]}" = "something" ]]  # Join and compare
```

### SC2206 - Quote to prevent word splitting

```bash
# BAD
array=($string)     # Splits on whitespace

# GOOD
IFS=' ' read -ra array <<< "$string"
mapfile -t array <<< "$string"
```

### SC2207 - Prefer mapfile for command output

```bash
# BAD
array=($(command))  # Word splitting issues

# GOOD
mapfile -t array < <(command)
readarray -t array < <(command)
```

## Testing

### SC2070 - -n doesn't work with unquoted arguments

```bash
# BAD
[ -n $var ]

# GOOD
[ -n "$var" ]
[[ -n "$var" ]]
```

### SC2166 - Prefer [[ ]] over [ ]

```bash
# BAD
[ "$a" == "$b" -a "$c" == "$d" ]

# GOOD
[[ "$a" == "$b" && "$c" == "$d" ]]
```

### SC2010 - Don't use ls | grep

```bash
# BAD
ls | grep pattern

# GOOD
find . -name 'pattern'
for f in *pattern*; do
```

### SC2236 - Use -z instead of ! -n

```bash
# BAD
[[ ! -n "$var" ]]

# GOOD
[[ -z "$var" ]]
```

### SC2237 - Use -n instead of ! -z

```bash
# BAD
[[ ! -z "$var" ]]

# GOOD
[[ -n "$var" ]]
```

## Compatibility

### SC3xxx - Shell compatibility warnings

```bash
# SC3010 - [[ is not POSIX
# SC3020 - (( is not POSIX
# SC3030 - Arrays are not POSIX
# SC3037 - echo -n is not POSIX
# SC3043 - local is not POSIX (use in functions only)
# SC3054 - Array references are not POSIX

# For POSIX compliance, use:
[ "$var" = "value" ]    # Instead of [[ ]]
test "$var" = "value"   # Test command
expr 1 + 1              # Instead of $(())
```

## Functions

### SC2120/SC2119 - Function arguments not used/passed

```bash
# SC2119 warning
foo() {
    echo "Args: $1 $2"
}
foo   # No args passed

# Fix
foo "arg1" "arg2"
```

### SC2168 - local outside function

```bash
# BAD
local var="value"   # Outside function

# GOOD
my_func() {
    local var="value"
}
```

## Deprecated

### SC2050 - Expression is always true/false

```bash
# BAD
if [[ "string" ]]; then    # Always true

# GOOD
if [[ -n "$variable" ]]; then
```

### SC1035/SC2088 - Tilde doesn't expand in quotes

```bash
# BAD
path="~/dir"   # Literal ~

# GOOD
path=~"/dir"
path="$HOME/dir"
```

### SC2129 - Consider grouping writes

```bash
# BAD
echo "line1" >> file
echo "line2" >> file
echo "line3" >> file

# GOOD
{
    echo "line1"
    echo "line2"
    echo "line3"
} >> file
```

### SC2103 - Use pushd/popd with care

```bash
# BAD
cd dir
# ... commands ...
cd ..   # May not return to original

# GOOD
pushd dir > /dev/null || exit 1
# ... commands ...
popd > /dev/null

# Or
(
    cd dir || exit 1
    # ... commands ...
)
```
