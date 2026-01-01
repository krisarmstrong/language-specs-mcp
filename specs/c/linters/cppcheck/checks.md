# cppcheck Error Checks

Critical bugs that are always reported.

## Memory Errors

### memleak

Memory allocated but not freed.

```cpp
// BAD
void foo() {
    char* p = malloc(100);
    if (error) return;  // leak!
    free(p);
}

// GOOD
void foo() {
    char* p = malloc(100);
    if (error) {
        free(p);
        return;
    }
    free(p);
}
```

### resourceLeak

File/resource opened but not closed.

```cpp
// BAD
void foo() {
    FILE* f = fopen("file", "r");
    if (error) return;  // leak!
    fclose(f);
}

// GOOD - use RAII in C++
void foo() {
    std::ifstream f("file");
    if (error) return;  // automatically closed
}
```

### deallocuse / useAfterFree

Use after free.

```cpp
// BAD
char* p = malloc(100);
free(p);
strcpy(p, "hello");  // use after free!

// GOOD
char* p = malloc(100);
strcpy(p, "hello");
free(p);
p = NULL;  // prevent reuse
```

### doubleFree

Freeing memory twice.

```cpp
// BAD
free(p);
free(p);  // double free!

// GOOD
free(p);
p = NULL;
```

### deallocDealloc

Dealloc mismatch.

```cpp
// BAD
int* p = new int;
free(p);  // should be delete!

int* a = new int[10];
delete a;  // should be delete[]!

// GOOD
int* p = new int;
delete p;

int* a = new int[10];
delete[] a;
```

### memleakOnRealloc

Leak when realloc fails.

```cpp
// BAD
p = realloc(p, new_size);  // if fails, p is lost!

// GOOD
void* tmp = realloc(p, new_size);
if (tmp == NULL) {
    free(p);  // free original
    return ERROR;
}
p = tmp;
```

## Null Pointer Errors

### nullPointer

Null pointer dereference.

```cpp
// BAD
int* p = NULL;
*p = 5;  // crash!

// GOOD
int* p = malloc(sizeof(int));
if (p != NULL) {
    *p = 5;
}
```

### nullPointerRedundantCheck

Check after dereference.

```cpp
// BAD
*p = 5;  // dereference
if (p == NULL) {  // too late!
    return;
}

// GOOD
if (p == NULL) {
    return;
}
*p = 5;
```

## Buffer Errors

### arrayIndexOutOfBounds

Array access out of bounds.

```cpp
// BAD
int arr[10];
arr[10] = 5;  // out of bounds!

// GOOD
int arr[10];
arr[9] = 5;
```

### bufferAccessOutOfBounds

Buffer overflow.

```cpp
// BAD
char buf[10];
strcpy(buf, "this is too long");  // overflow!

// GOOD
char buf[10];
strncpy(buf, "this is too long", sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';
```

### negativeIndex

Negative array index.

```cpp
// BAD
int arr[10];
int i = -1;
arr[i] = 5;  // negative index!
```

### stringLiteralWrite

Writing to string literal.

```cpp
// BAD
char* s = "hello";
s[0] = 'H';  // undefined behavior!

// GOOD
char s[] = "hello";
s[0] = 'H';
```

## Uninitialized Variables

### uninitvar

Using uninitialized variable.

```cpp
// BAD
int x;
printf("%d", x);  // uninitialized!

// GOOD
int x = 0;
printf("%d", x);
```

### uninitdata

Using uninitialized data.

```cpp
// BAD
struct S { int a; int b; };
struct S s;
printf("%d", s.a);  // uninitialized!

// GOOD
struct S s = {0};
printf("%d", s.a);
```

### uninitMemberVar

Using uninitialized member.

```cpp
// BAD
class Foo {
    int x;
public:
    int getX() { return x; }  // x not initialized!
};

// GOOD
class Foo {
    int x = 0;
public:
    int getX() { return x; }
};
```

## Division Errors

### zerodiv

Division by zero.

```cpp
// BAD
int x = 5 / 0;

// GOOD
if (divisor != 0) {
    int x = 5 / divisor;
}
```

### zerodivcond

Division by zero in condition.

```cpp
// BAD
if (x != 0) { }
y = z / x;  // x might be 0 here!

// GOOD
if (x != 0) {
    y = z / x;
}
```

## Control Flow Errors

### unreachableCode

Code that can never execute.

```cpp
// BAD
return 0;
printf("never reached");  // unreachable!
```

### duplicateBreak

Duplicate break.

```cpp
// BAD
case 1:
    break;
    break;  // duplicate!
```

### identicalConditionAfterEarlyExit

Redundant condition.

```cpp
// BAD
if (x > 0) return;
if (x > 0) {  // always false here!
    // ...
}
```

## Misc Errors

### invalidPrintfArgType_*

Wrong printf format specifier.

```cpp
// BAD
printf("%d", "string");  // wrong type!
printf("%s", 42);        // wrong type!

// GOOD
printf("%s", "string");
printf("%d", 42);
```

### wrongPrintfScanfArgNum

Wrong number of printf/scanf arguments.

```cpp
// BAD
printf("%d %d", x);  // missing argument!

// GOOD
printf("%d %d", x, y);
```

### invalidScanfArgType_*

Wrong scanf argument type.

```cpp
// BAD
int x;
scanf("%s", x);  // should be pointer!

// GOOD
char buf[100];
scanf("%s", buf);
```

### leakReturnValNotUsed

Return value leak.

```cpp
// BAD
malloc(100);  // leak - return value ignored!
strdup("hello");  // leak!

// GOOD
char* p = malloc(100);
// use p
free(p);
```

### selfAssignment

Self assignment.

```cpp
// BAD
x = x;

// Just remove it
```

### redundantAssignment

Redundant assignment.

```cpp
// BAD
x = 1;
x = 2;  // first assignment wasted

// GOOD
x = 2;
```

### unreadVariable

Variable assigned but never read.

```cpp
// BAD
int x = 5;  // never used

// Remove it or use it
```

### unusedVariable

Variable declared but never used.

```cpp
// BAD
int unused;

// Remove it
```

### constParameter

Parameter could be const.

```cpp
// BAD
void foo(int* p) {
    printf("%d", *p);  // doesn't modify
}

// GOOD
void foo(const int* p) {
    printf("%d", *p);
}
```

### constVariable

Variable could be const.

```cpp
// BAD
int x = 5;
printf("%d", x);  // x never modified

// GOOD
const int x = 5;
printf("%d", x);
```
