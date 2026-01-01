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
