# cppcheck Error Checks

Critical bugs that will cause crashes or incorrect behavior.

## nullPointer

Null pointer dereference.

```cpp
// BAD
int* p = nullptr;
*p = 5;  // crash

int* getData();
int x = *getData();  // crash if getData returns null

// GOOD
int* p = getData();
if (p != nullptr) {
    *p = 5;
}
```

## nullPointerArithmetic

Arithmetic on null pointer.

```cpp
// BAD
int* p = nullptr;
int* q = p + 1;  // undefined behavior

// GOOD
int arr[10];
int* p = arr;
int* q = p + 1;  // OK
```

## nullPointerRedundantCheck

Redundant null check after dereference.

```cpp
// BAD - already dereferenced, check is too late
int x = *p;
if (p != nullptr) {  // redundant - would have crashed above
    use(x);
}

// GOOD - check before dereference
if (p != nullptr) {
    int x = *p;
    use(x);
}
```

## uninitvar

Use of uninitialized variable.

```cpp
// BAD
int x;
printf("%d", x);  // undefined value

int* p;
*p = 5;  // undefined behavior

// GOOD
int x = 0;
printf("%d", x);

int* p = nullptr;  // or point to valid memory
```

## uninitMemberVar

Uninitialized member variable.

```cpp
// BAD
class Foo {
    int x;  // never initialized
public:
    Foo() { }  // x is garbage
};

// GOOD
class Foo {
    int x = 0;
public:
    Foo() = default;
};

// Or
class Foo {
    int x;
public:
    Foo() : x(0) { }
};
```

## uninitStructMember

Uninitialized struct member.

```cpp
// BAD
struct Point { int x, y; };
Point p;
printf("%d", p.x);  // garbage

// GOOD
Point p = {0, 0};
Point p = {};  // zero-initialized
```

## memleak

Memory leak - allocated memory not freed.

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

// BETTER - use RAII in C++
void foo() {
    auto p = std::make_unique<char[]>(100);
    if (error) return;  // automatically freed
}
```

## resourceLeak

Resource leak - file handle, socket, etc not closed.

```cpp
// BAD
void foo() {
    FILE* f = fopen("file", "r");
    if (error) return;  // leak!
    fclose(f);
}

// GOOD
void foo() {
    FILE* f = fopen("file", "r");
    if (f == nullptr) return;
    if (error) {
        fclose(f);
        return;
    }
    fclose(f);
}
```

## deallocuse

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
p = nullptr;  // prevent accidental reuse
```

## doubleFree

Freeing memory twice.

```cpp
// BAD
char* p = malloc(100);
free(p);
free(p);  // double free!

// GOOD
char* p = malloc(100);
free(p);
p = nullptr;
// free(p);  // free(nullptr) is safe but unnecessary
```

## bufferAccessOutOfBounds

Buffer overrun.

```cpp
// BAD
char buf[10];
strcpy(buf, "this string is too long");  // overflow

int arr[5];
arr[5] = 0;  // out of bounds

// GOOD
char buf[32];
strncpy(buf, str, sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';

int arr[5];
arr[4] = 0;  // last valid index
```

## arrayIndexOutOfBounds

Array index out of bounds.

```cpp
// BAD
int arr[10];
for (int i = 0; i <= 10; i++) {  // off by one
    arr[i] = 0;
}

// GOOD
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}
```

## negativeIndex

Negative array index.

```cpp
// BAD
int arr[10];
int i = -1;
arr[i] = 0;  // undefined behavior

// GOOD
if (i >= 0 && i < 10) {
    arr[i] = 0;
}
```

## invalidIterator

Use of invalid iterator.

```cpp
// BAD
std::vector<int> v = {1, 2, 3};
auto it = v.begin();
v.push_back(4);  // may invalidate iterators
*it = 0;  // undefined behavior!

// GOOD
std::vector<int> v = {1, 2, 3};
v.push_back(4);
auto it = v.begin();  // get iterator after modification
*it = 0;
```

## danglingReference

Dangling reference.

```cpp
// BAD
int& getRef() {
    int x = 42;
    return x;  // dangling reference!
}

// BAD
std::string_view sv = getString();  // temporary destroyed

// GOOD
int& getRef() {
    static int x = 42;
    return x;
}

std::string s = getString();
std::string_view sv = s;  // s must outlive sv
```

## invalidContainer

Invalid container operation.

```cpp
// BAD
std::vector<int> v;
v.front();  // undefined - empty container

// GOOD
std::vector<int> v;
if (!v.empty()) {
    v.front();
}
```

## mismatchAllocDealloc

Mismatched allocation/deallocation.

```cpp
// BAD
int* p = new int;
free(p);  // should use delete

int* arr = new int[10];
delete arr;  // should use delete[]

// GOOD
int* p = new int;
delete p;

int* arr = new int[10];
delete[] arr;

void* m = malloc(100);
free(m);
```

## deallocDealloc

Deallocation of already deallocated memory.

```cpp
// BAD
int* p = new int;
delete p;
delete p;  // double delete!

// GOOD
int* p = new int;
delete p;
p = nullptr;
```

## zerodiv

Division by zero.

```cpp
// BAD
int x = 10 / 0;  // undefined behavior

int divisor = getValue();
int result = 100 / divisor;  // might be zero

// GOOD
int divisor = getValue();
if (divisor != 0) {
    int result = 100 / divisor;
}
```

## shiftTooManyBits

Shift by too many bits.

```cpp
// BAD
int x = 1 << 32;  // undefined for 32-bit int
int y = 1 << -1;  // undefined

// GOOD
int x = 1 << 31;  // max safe shift for 32-bit signed
unsigned u = 1U << 31;
```

## integerOverflow

Integer overflow.

```cpp
// BAD
int x = INT_MAX;
x = x + 1;  // undefined behavior (signed overflow)

// GOOD
int x = INT_MAX;
if (x < INT_MAX) {
    x = x + 1;
}

// Or use unsigned (wraps defined)
unsigned u = UINT_MAX;
u = u + 1;  // wraps to 0, defined behavior
```

## signConversion

Suspicious sign conversion.

```cpp
// BAD
int x = -1;
unsigned u = x;  // large positive value
if (u < 10) { }  // always false!

// GOOD
int x = -1;
if (x >= 0) {
    unsigned u = x;
}
```
