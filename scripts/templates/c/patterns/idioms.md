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
