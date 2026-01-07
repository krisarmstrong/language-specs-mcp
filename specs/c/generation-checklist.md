# C Generation Checklist

**Read this BEFORE writing C code. Memory safety is your responsibility.**

## Critical: You Must Do These

### 1. Always Check Return Values
```c
// BAD - ignores failure
FILE *f = fopen("data.txt", "r");
fread(buffer, 1, size, f);

// GOOD - check every call that can fail
FILE *f = fopen("data.txt", "r");
if (f == NULL) {
    perror("fopen");
    return -1;
}
```

### 2. Always Free Allocated Memory
```c
// BAD - memory leak
char *buf = malloc(256);
if (condition) return;  // Leak!

// GOOD - free before every exit path
char *buf = malloc(256);
if (buf == NULL) return -1;
if (condition) {
    free(buf);
    return 0;
}
// ... use buf ...
free(buf);
```

### 3. Initialize All Variables
```c
// BAD - undefined behavior
int count;
int *ptr;
printf("%d\n", count);  // Garbage value

// GOOD - always initialize
int count = 0;
int *ptr = NULL;
```

### 4. Check malloc Returns NULL
```c
// BAD - assumes success
char *buf = malloc(size);
memcpy(buf, src, size);  // Crash if NULL

// GOOD - always check
char *buf = malloc(size);
if (buf == NULL) {
    return -1;
}
```

### 5. Use Safe String Functions
```c
// DANGEROUS - buffer overflow
char buf[64];
strcpy(buf, user_input);   // Overflow risk
sprintf(buf, "%s", input); // Overflow risk

// SAFE - bounded versions
char buf[64];
strncpy(buf, user_input, sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';
snprintf(buf, sizeof(buf), "%s", input);
```

## Important: Strong Recommendations

### 6. Use `const` for Read-Only Parameters
```c
// BAD - unclear intent
void process(char *str);

// GOOD - documents immutability
void process(const char *str);
```

### 7. Use `sizeof` on the Variable, Not the Type
```c
// BAD - error-prone if type changes
int *arr = malloc(100 * sizeof(int));

// GOOD - always correct
int *arr = malloc(100 * sizeof(*arr));
```

### 8. Use `static` for File-Local Functions
```c
// BAD - pollutes global namespace
void helper_function(void) { }

// GOOD - limits visibility
static void helper_function(void) { }
```

### 9. Prefer `size_t` for Sizes and Array Indices
```c
// BAD - can be negative, overflow issues
int len = strlen(str);
for (int i = 0; i < len; i++) { }

// GOOD - correct type for sizes
size_t len = strlen(str);
for (size_t i = 0; i < len; i++) { }
```

### 10. Use Enum for Related Constants
```c
// BAD - magic numbers
if (status == 1) { }

// GOOD - named constants
typedef enum {
    STATUS_OK = 0,
    STATUS_ERROR = 1,
    STATUS_PENDING = 2
} Status;

if (status == STATUS_ERROR) { }
```

## Memory Safety

### 11. Set Pointers to NULL After Free
```c
// BAD - dangling pointer
free(ptr);
// ptr is now dangling

// GOOD - prevent use-after-free
free(ptr);
ptr = NULL;
```

### 12. Don't Return Pointers to Local Variables
```c
// BAD - undefined behavior
char *get_greeting(void) {
    char buf[64] = "Hello";
    return buf;  // Stack memory!
}

// GOOD - static, malloc, or caller-provided buffer
char *get_greeting(void) {
    char *buf = malloc(64);
    if (buf) strcpy(buf, "Hello");
    return buf;  // Caller must free
}
```

### 13. Use Valgrind During Development
```bash
# Run your program under Valgrind
valgrind --leak-check=full ./your_program
```

## Security

### 14. Never Use gets()
```c
// BANNED - always buffer overflow
char buf[64];
gets(buf);  // Never use!

// SAFE - use fgets
char buf[64];
if (fgets(buf, sizeof(buf), stdin)) {
    buf[strcspn(buf, "\n")] = '\0';  // Remove newline
}
```

### 15. Validate Array Bounds
```c
// BAD - out-of-bounds access
void get_item(int arr[], int index) {
    return arr[index];  // No bounds check!
}

// GOOD - check bounds
int get_item(int arr[], size_t arr_len, size_t index) {
    if (index >= arr_len) {
        return -1;  // Error
    }
    return arr[index];
}
```

### 16. Use Format String Safely
```c
// DANGEROUS - format string vulnerability
printf(user_input);

// SAFE - always use format specifier
printf("%s", user_input);
```

---

**Quick Reference - Copy This Mental Model:**
- Check ALL return values
- Free ALL allocated memory
- Initialize ALL variables
- Use bounded string functions (strncpy, snprintf)
- sizeof(*ptr) not sizeof(type)
- const for read-only params
- size_t for sizes
- NULL after free
- Never return local pointers
- Validate array bounds
- printf("%s", str) not printf(str)
