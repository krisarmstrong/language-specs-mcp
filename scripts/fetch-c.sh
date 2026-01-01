#!/bin/bash
# Fetch C specs from authoritative sources

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/c"

echo "=== Fetching C Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/headers,patterns,formatters,linters/{clang-tidy,cppcheck}}

# C standard draft (ISO C is copyrighted, but drafts are available)
echo "Fetching C standard draft..."
curl -sL "https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3096.pdf" \
  -o "$SPECS_DIR/c23-draft.pdf" 2>/dev/null || \
  echo "C23 draft PDF requires manual download from open-std.org"

# Core C patterns
cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
# C Idiomatic Patterns

## Memory Management

### Always check malloc returns

```c
// BAD
char *buf = malloc(size);
strcpy(buf, src);  // crash if malloc failed

// GOOD
char *buf = malloc(size);
if (buf == NULL) {
    return -1;  // or handle error
}
strcpy(buf, src);
```

### Free in reverse order of allocation

```c
char *a = malloc(10);
char *b = malloc(20);
// use a and b
free(b);
free(a);
```

### Set pointers to NULL after free

```c
free(ptr);
ptr = NULL;
```

## Error Handling

### Return error codes consistently

```c
// 0 = success, negative = error
int do_something(void) {
    if (error_condition) {
        return -1;
    }
    return 0;
}
```

### Use errno for system calls

```c
#include <errno.h>

int fd = open(path, O_RDONLY);
if (fd < 0) {
    fprintf(stderr, "open failed: %s\n", strerror(errno));
    return -1;
}
```

## String Safety

### Use snprintf, not sprintf

```c
// BAD - buffer overflow risk
sprintf(buf, "%s", user_input);

// GOOD
snprintf(buf, sizeof(buf), "%s", user_input);
```

### Use strncpy with explicit null termination

```c
strncpy(dest, src, sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';
```

## Resource Management

### Use RAII-style cleanup with goto

```c
int process_file(const char *path) {
    int ret = -1;
    FILE *f = NULL;
    char *buf = NULL;
    
    f = fopen(path, "r");
    if (f == NULL) {
        goto cleanup;
    }
    
    buf = malloc(BUFSIZE);
    if (buf == NULL) {
        goto cleanup;
    }
    
    // do work
    ret = 0;
    
cleanup:
    free(buf);
    if (f) fclose(f);
    return ret;
}
```

## Header Guards

```c
#ifndef PROJECT_MODULE_H
#define PROJECT_MODULE_H

// declarations

#endif /* PROJECT_MODULE_H */
```

## Const Correctness

```c
// Pointer to const data - can't modify data
void print(const char *str);

// Const pointer - can't change pointer
char *const ptr = buf;

// Both
const char *const ptr = "literal";
```
EOF

# C formatters
cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# C Formatters

## clang-format

See: https://clang.llvm.org/docs/ClangFormat.html
EOF

echo "Fetching C standard library headers..."
curl -sL "https://en.cppreference.com/w/c/header" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/headers/index.md" 2>/dev/null || \
  echo "# C Standard Library Headers\n\nSee: https://en.cppreference.com/w/c/header" > "$SPECS_DIR/stdlib/headers/index.md"

C_HEADERS=$(curl -sL "https://en.cppreference.com/w/c/header" | \
  grep -oE '/w/c/header/[a-zA-Z0-9_.]+' | \
  sed 's#.*/##' | sort -u)

for hdr in $C_HEADERS; do
  echo "  - c/$hdr"
  curl -sL "https://en.cppreference.com/w/c/header/${hdr}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/headers/${hdr}.md" 2>/dev/null || \
    echo "# ${hdr}\n\nSee: https://en.cppreference.com/w/c/header/${hdr}" > "$SPECS_DIR/stdlib/headers/${hdr}.md"
done

cat > "$SPECS_DIR/formatters/clang-format.md" << 'EOF'
# clang-format Options

See: https://clang.llvm.org/docs/ClangFormatStyleOptions.html
EOF

# Standard library reference
cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF'
# C Standard Library Overview

## Headers

| Header | Purpose |
|--------|---------|
| `<stdio.h>` | Input/output |
| `<stdlib.h>` | General utilities, memory |
| `<string.h>` | String manipulation |
| `<stdint.h>` | Fixed-width integers |
| `<stdbool.h>` | Boolean type |
| `<stddef.h>` | Common definitions |
| `<errno.h>` | Error codes |
| `<limits.h>` | Implementation limits |
| `<math.h>` | Math functions |
| `<time.h>` | Time functions |
| `<assert.h>` | Assertions |

## Common Functions

### Memory

```c
void *malloc(size_t size);
void *calloc(size_t nmemb, size_t size);
void *realloc(void *ptr, size_t size);
void free(void *ptr);
void *memcpy(void *dest, const void *src, size_t n);
void *memset(void *s, int c, size_t n);
```

### Strings

```c
size_t strlen(const char *s);
char *strcpy(char *dest, const char *src);
char *strncpy(char *dest, const char *src, size_t n);
int strcmp(const char *s1, const char *s2);
char *strcat(char *dest, const char *src);
char *strstr(const char *haystack, const char *needle);
```

### I/O

```c
FILE *fopen(const char *path, const char *mode);
int fclose(FILE *stream);
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
int fprintf(FILE *stream, const char *format, ...);
int snprintf(char *str, size_t size, const char *format, ...);
```
EOF

# clang-tidy checks
echo "Fetching clang-tidy checks..."
curl -sL "https://clang.llvm.org/extra/clang-tidy/checks/list.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/clang-tidy/overview.md" 2>/dev/null || \
  echo "# clang-tidy Checks\n\nSee: https://clang.llvm.org/extra/clang-tidy/checks/list.html" > "$SPECS_DIR/linters/clang-tidy/overview.md"

CLANG_TIDY_CHECKS=$(curl -sL "https://clang.llvm.org/extra/clang-tidy/checks/list.html" | \
  grep -oE 'checks/[a-zA-Z0-9_-]+\\.html' | \
  sed 's#.*/##;s/\\.html$//' | sort -u)

for check in $CLANG_TIDY_CHECKS; do
  echo "  - clang-tidy/$check"
  curl -sL "https://clang.llvm.org/extra/clang-tidy/checks/${check}.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/clang-tidy/${check}.md" 2>/dev/null || \
    echo "# ${check}\n\nSee: https://clang.llvm.org/extra/clang-tidy/checks/${check}.html" > "$SPECS_DIR/linters/clang-tidy/${check}.md"
done

# cppcheck checks
curl -sL "https://cppcheck.sourceforge.io/manual.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/cppcheck/overview.md" 2>/dev/null || \
  echo "# cppcheck Manual\n\nSee: https://cppcheck.sourceforge.io/manual.html" > "$SPECS_DIR/linters/cppcheck/overview.md"

echo "=== C specs complete ==="
