# C Language Specification Summary

Based on C23 (ISO/IEC 9899:2024)

## Keywords

```c
auto        break       case        char        const
continue    default     do          double      else
enum        extern      float       for         goto
if          inline      int         long        register
restrict    return      short       signed      sizeof
static      struct      switch      typedef     typeof
typeof_unqual union     unsigned    void        volatile
while       _Alignas    _Alignof    _Atomic     _BitInt
_Bool       _Complex    _Decimal128 _Decimal32  _Decimal64
_Generic    _Imaginary  _Noreturn   _Static_assert
_Thread_local
```

## C23 Contextual Keywords

```c
true        false       nullptr     alignas     alignof
bool        static_assert           thread_local
```

## Types

### Basic Types

```c
char                    // at least 8 bits
signed char             // at least 8 bits, signed
unsigned char           // at least 8 bits, unsigned

short                   // at least 16 bits
unsigned short

int                     // at least 16 bits
unsigned int

long                    // at least 32 bits
unsigned long

long long               // at least 64 bits
unsigned long long

float                   // single precision
double                  // double precision
long double             // extended precision

_Bool / bool            // boolean
void                    // no value
```

### Fixed-Width Types (stdint.h)

```c
int8_t      int16_t     int32_t     int64_t
uint8_t     uint16_t    uint32_t    uint64_t
intptr_t    uintptr_t
size_t      ptrdiff_t
```

### Type Qualifiers

```c
const       // read-only
volatile    // may change unexpectedly
restrict    // pointer is only reference to object
_Atomic     // atomic access
```

## Declarations

### Variables

```c
int x;                  // uninitialized
int x = 0;              // initialized
const int x = 0;        // constant
static int x = 0;       // static storage duration
extern int x;           // external linkage
```

### Arrays

```c
int arr[10];            // fixed size
int arr[] = {1, 2, 3};  // size from initializer
int arr[3] = {0};       // all zeros

// Variable-length arrays (VLA) - C99+
int n = 10;
int vla[n];
```

### Pointers

```c
int *p;                 // pointer to int
int **pp;               // pointer to pointer
int *const p;           // const pointer
const int *p;           // pointer to const
int (*fp)(int);         // function pointer
int (*arr)[10];         // pointer to array
```

### Structs

```c
struct Point {
    int x;
    int y;
};

struct Point p = {0, 0};
struct Point p = {.x = 0, .y = 0};  // designated initializer
```

### Unions

```c
union Data {
    int i;
    float f;
    char str[20];
};
```

### Enums

```c
enum Color { RED, GREEN, BLUE };
enum Color { RED = 1, GREEN = 2, BLUE = 4 };
```

### Typedefs

```c
typedef unsigned long size_t;
typedef struct Node Node;
typedef int (*Comparator)(const void*, const void*);
```

## Functions

### Declaration

```c
int add(int a, int b);              // declaration
int add(int, int);                  // also valid

int add(int a, int b) {             // definition
    return a + b;
}
```

### Function Pointers

```c
int (*operation)(int, int);
operation = add;
int result = operation(1, 2);

// As parameter
void sort(void *arr, size_t n, int (*cmp)(const void*, const void*));
```

### Variadic Functions

```c
#include <stdarg.h>

int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    va_end(args);
    return total;
}
```

### Inline Functions (C99+)

```c
static inline int max(int a, int b) {
    return a > b ? a : b;
}
```

## Control Flow

### If-Else

```c
if (condition) {
    // ...
} else if (other) {
    // ...
} else {
    // ...
}
```

### Switch

```c
switch (x) {
    case 1:
        // ...
        break;
    case 2:
    case 3:
        // fall through
        break;
    default:
        // ...
}
```

### Loops

```c
// For
for (int i = 0; i < n; i++) {
    // ...
}

// While
while (condition) {
    // ...
}

// Do-While
do {
    // ...
} while (condition);
```

### Jump Statements

```c
break;          // exit loop/switch
continue;       // next iteration
return value;   // return from function
goto label;     // jump to label (use sparingly)
```

## Preprocessor

### Includes

```c
#include <stdio.h>      // system header
#include "myheader.h"   // local header
```

### Macros

```c
#define PI 3.14159
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define SQUARE(x) ((x) * (x))

// Stringification
#define STR(x) #x

// Token pasting
#define CONCAT(a, b) a##b
```

### Conditionals

```c
#if defined(__linux__)
    // Linux code
#elif defined(_WIN32)
    // Windows code
#else
    // Other
#endif

#ifdef DEBUG
    // Debug code
#endif

#ifndef HEADER_H
#define HEADER_H
// Header content
#endif
```

### Pragmas

```c
#pragma once                    // include guard
#pragma pack(push, 1)           // struct packing
#pragma pack(pop)
```

## Memory Management

### Stack Allocation

```c
int x;                          // automatic storage
char buffer[1024];
```

### Heap Allocation

```c
#include <stdlib.h>

void *malloc(size_t size);
void *calloc(size_t nmemb, size_t size);
void *realloc(void *ptr, size_t size);
void free(void *ptr);

// Example
int *arr = malloc(10 * sizeof(int));
if (arr == NULL) {
    // handle error
}
// use arr
free(arr);
arr = NULL;  // prevent use-after-free
```

## C23 New Features

### Type Inference

```c
auto x = 42;            // int
auto y = 3.14;          // double
```

### nullptr

```c
int *p = nullptr;       // preferred over NULL
```

### constexpr

```c
constexpr int size = 100;
int arr[size];          // compile-time constant
```

### Attributes

```c
[[nodiscard]] int must_use(void);
[[deprecated]] void old_func(void);
[[maybe_unused]] int x;
[[noreturn]] void abort_handler(void);
```

### typeof

```c
int x = 5;
typeof(x) y = 10;       // y is int
```

### Binary Literals

```c
int flags = 0b10101010;
```

### Digit Separators

```c
int big = 1'000'000;
```

### Empty Initializer

```c
struct Point p = {};    // zero-initialize
```
