# clang-tidy bugprone-* Checks

Bug-finding checks for common programming mistakes.

## bugprone-argument-comment

Checks that argument comments match parameter names.

```cpp
// BAD
void draw(int x, int y);
draw(/*y=*/10, /*x=*/20);  // swapped!

// GOOD
draw(/*x=*/10, /*y=*/20);
```

## bugprone-assert-side-effect

Finds assertions with side effects (removed in release builds).

```cpp
// BAD - side effect in assert
assert(i++ < 10);  // i not incremented in release!
assert(processItem());  // not called in release!

// GOOD
++i;
assert(i < 10);

bool result = processItem();
assert(result);
```

## bugprone-assignment-in-if-condition

Finds assignments in if conditions.

```cpp
// BAD - probably meant ==
if (x = 0) { }

// GOOD
if (x == 0) { }

// If intentional, be explicit
if ((x = getValue()) != 0) { }
```

## bugprone-bool-pointer-implicit-conversion

Finds implicit bool* to bool conversions.

```cpp
// BAD
bool* p = &flag;
if (p) { }  // checks if pointer is non-null, not the bool value

// GOOD
if (p && *p) { }  // check both
if (*p) { }       // if you know p is valid
```

## bugprone-branch-clone

Finds duplicated code in if/else branches.

```cpp
// BAD
if (condition) {
    doSomething();
    return 1;
} else {
    doSomething();  // duplicate!
    return 1;
}

// GOOD - remove branch or fix logic
doSomething();
return 1;
```

## bugprone-copy-constructor-init

Finds copy constructors that don't call base copy constructor.

```cpp
// BAD
class Derived : public Base {
    Derived(const Derived& other) : Base() { }  // should call Base(other)
};

// GOOD
class Derived : public Base {
    Derived(const Derived& other) : Base(other) { }
};
```

## bugprone-dangling-handle

Finds dangling references to temporary strings.

```cpp
// BAD
std::string_view sv = getString();  // getString() returns temporary
use(sv);  // dangling!

// GOOD
std::string s = getString();
std::string_view sv = s;
use(sv);
```

## bugprone-dynamic-static-initializers

Finds dynamic initialization of static variables.

```cpp
// BAD - initialization order undefined
static int x = someFunction();

// GOOD - use function-local static or constexpr
int getX() {
    static int x = someFunction();  // initialized on first call
    return x;
}
```

## bugprone-exception-escape

Finds functions that may throw but shouldn't.

```cpp
// BAD - destructor shouldn't throw
~MyClass() {
    throw std::runtime_error("oops");  // undefined behavior!
}

// GOOD
~MyClass() noexcept {
    try {
        cleanup();
    } catch (...) {
        // log but don't throw
    }
}
```

## bugprone-fold-init-type

Finds folds with wrong init type.

```cpp
// BAD - init is int, accumulator loses precision
auto sum = std::accumulate(v.begin(), v.end(), 0);  // v is vector<double>

// GOOD
auto sum = std::accumulate(v.begin(), v.end(), 0.0);
```

## bugprone-forwarding-reference-overload

Finds forwarding reference constructors that hide copy/move.

```cpp
// BAD - template catches everything
class Widget {
    template<typename T>
    Widget(T&& arg) { }  // catches Widget& too!
};

// GOOD - constrain the template
class Widget {
    template<typename T>
    requires (!std::same_as<std::remove_cvref_t<T>, Widget>)
    Widget(T&& arg) { }
};
```

## bugprone-implicit-widening-of-multiplication-result

Finds multiplication overflow before widening.

```cpp
// BAD - multiplication overflows before cast
int a = 1000000, b = 1000000;
long long result = a * b;  // overflow!

// GOOD - cast before multiplication
long long result = static_cast<long long>(a) * b;
```

## bugprone-incorrect-roundings

Finds incorrect rounding patterns.

```cpp
// BAD
int rounded = (int)(d + 0.5);  // wrong for negative numbers

// GOOD
int rounded = std::lround(d);
```

## bugprone-infinite-loop

Finds loops that never terminate.

```cpp
// BAD
while (true) {
    if (condition) continue;  // no break ever!
}

// GOOD
while (true) {
    if (condition) break;
}
```

## bugprone-integer-division

Finds integer division in floating-point context.

```cpp
// BAD
double ratio = count / total;  // integer division!

// GOOD
double ratio = static_cast<double>(count) / total;
```

## bugprone-macro-parentheses

Finds macros without proper parentheses.

```cpp
// BAD
#define DOUBLE(x) x * 2
int y = DOUBLE(1 + 2);  // expands to 1 + 2 * 2 = 5, not 6

// GOOD
#define DOUBLE(x) ((x) * 2)
```

## bugprone-macro-repeated-side-effects

Finds macros that evaluate arguments multiple times.

```cpp
// BAD
#define MAX(a, b) ((a) > (b) ? (a) : (b))
int x = MAX(i++, j++);  // incremented twice!

// GOOD - use inline function
template<typename T>
constexpr T max(T a, T b) { return a > b ? a : b; }
```

## bugprone-misplaced-operator-in-strlen-in-alloc

Finds strlen() + 1 mistakes.

```cpp
// BAD
char* copy = malloc(strlen(s + 1));  // wrong - s+1 passed to strlen

// GOOD
char* copy = malloc(strlen(s) + 1);  // +1 outside strlen
```

## bugprone-misplaced-widening-cast

Finds casts that should be done earlier.

```cpp
// BAD - multiplication already overflowed
long long result = (long long)(a * b);

// GOOD - cast before operation
long long result = (long long)a * b;
```

## bugprone-move-forwarding-reference

Finds std::move on forwarding references.

```cpp
// BAD - should use std::forward
template<typename T>
void foo(T&& arg) {
    bar(std::move(arg));  // wrong!
}

// GOOD
template<typename T>
void foo(T&& arg) {
    bar(std::forward<T>(arg));
}
```

## bugprone-multiple-statement-macro

Finds multi-statement macros without braces.

```cpp
// BAD
#define DO_BOTH do_a(); do_b()
if (cond) DO_BOTH;  // only do_a is conditional!

// GOOD
#define DO_BOTH do { do_a(); do_b(); } while(0)
```

## bugprone-narrowing-conversions

Finds implicit narrowing conversions.

```cpp
// BAD
int x = 3.14;      // loses .14
char c = 1000;     // overflow
float f = 1e100;   // overflow

// GOOD - explicit conversion
int x = static_cast<int>(3.14);
```

## bugprone-not-null-terminated-result

Finds string operations that may not null-terminate.

```cpp
// BAD
char buf[10];
strncpy(buf, src, sizeof(buf));  // may not null-terminate

// GOOD
strncpy(buf, src, sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';

// BETTER - use strlcpy or snprintf
snprintf(buf, sizeof(buf), "%s", src);
```

## bugprone-parent-virtual-call

Finds calls to parent virtual through wrong type.

```cpp
// BAD
class Derived : public Base {
    void foo() override {
        Base::foo();       // OK
        this->Base::foo(); // OK
        ((Base*)this)->foo(); // calls Derived::foo! infinite recursion
    }
};
```

## bugprone-signed-char-misuse

Finds signed char used where unsigned expected.

```cpp
// BAD - char may be negative
char c = getchar();
if (c == 255) { }  // never true if char is signed!

// GOOD
int c = getchar();  // getchar returns int
if (c == 255) { }
```

## bugprone-sizeof-container

Finds sizeof() on containers.

```cpp
// BAD
std::vector<int> v;
size_t bytes = sizeof(v);  // size of vector struct, not contents!

// GOOD
size_t bytes = v.size() * sizeof(int);
size_t elements = v.size();
```

## bugprone-sizeof-expression

Finds suspicious sizeof expressions.

```cpp
// BAD
int* arr = malloc(10);
memset(arr, 0, sizeof(arr));  // only clears pointer size!

// GOOD
int* arr = malloc(10 * sizeof(int));
memset(arr, 0, 10 * sizeof(int));
```

## bugprone-string-constructor

Finds suspicious string constructor calls.

```cpp
// BAD - creates string of 'x' characters, not "x" string
std::string s('x', 50);  // wrong order!

// GOOD
std::string s(50, 'x');  // 50 copies of 'x'
std::string s("x");      // string "x"
```

## bugprone-string-literal-with-embedded-nul

Finds strings with embedded NUL characters.

```cpp
// BAD - NUL in middle, string truncated
std::string s = "hello\0world";  // s is "hello"

// GOOD - if intentional, use constructor
std::string s("hello\0world", 11);  // includes NUL
```

## bugprone-suspicious-enum-usage

Finds suspicious enum operations.

```cpp
// BAD - mixing enum values
enum Color { Red, Green, Blue };
enum Size { Small, Medium, Large };
if (color == Small) { }  // comparing different enums

// GOOD - use enum class
enum class Color { Red, Green, Blue };
enum class Size { Small, Medium, Large };
// if (color == Size::Small) { }  // error!
```

## bugprone-suspicious-include

Finds includes with implementation file extensions.

```cpp
// BAD
#include "file.cpp"  // probably wrong
#include "file.c"

// GOOD
#include "file.h"
#include "file.hpp"
```

## bugprone-suspicious-memory-comparison

Finds memcmp on non-trivially-comparable types.

```cpp
// BAD - padding bytes may differ
struct S { char a; int b; };  // has padding
S s1, s2;
memcmp(&s1, &s2, sizeof(S));  // compares padding too!

// GOOD
s1.a == s2.a && s1.b == s2.b
```

## bugprone-suspicious-memset-usage

Finds suspicious memset patterns.

```cpp
// BAD
memset(buf, sizeof(buf), 0);  // args swapped!

// GOOD
memset(buf, 0, sizeof(buf));
```

## bugprone-suspicious-missing-comma

Finds string literals missing comma.

```cpp
// BAD
const char* arr[] = {
    "one",
    "two"   // missing comma
    "three" // concatenated with "two"!
};

// GOOD
const char* arr[] = {
    "one",
    "two",
    "three"
};
```

## bugprone-suspicious-semicolon

Finds suspicious semicolons.

```cpp
// BAD
if (condition);  // empty if body!
{
    doSomething();  // always runs
}

// GOOD
if (condition) {
    doSomething();
}
```

## bugprone-suspicious-string-compare

Finds suspicious string comparisons.

```cpp
// BAD - strcmp returns 0 for equal!
if (strcmp(a, b)) {
    // strings are NOT equal here
}

// GOOD
if (strcmp(a, b) == 0) {
    // strings are equal
}
```

## bugprone-swapped-arguments

Finds likely swapped function arguments.

```cpp
// BAD
memset(buf, sizeof(buf), 0);  // size and value swapped

// GOOD
memset(buf, 0, sizeof(buf));
```

## bugprone-terminating-continue

Finds continue that terminates loop.

```cpp
// BAD
do {
    continue;  // loop runs once!
} while (false);
```

## bugprone-throw-keyword-missing

Finds missing throw keyword.

```cpp
// BAD
if (error) {
    std::runtime_error("oops");  // creates and discards!
}

// GOOD
if (error) {
    throw std::runtime_error("oops");
}
```

## bugprone-too-small-loop-variable

Finds loop variables that may overflow.

```cpp
// BAD
for (char i = 0; i < size; i++) { }  // char may overflow

// GOOD
for (size_t i = 0; i < size; i++) { }
```

## bugprone-undefined-memory-manipulation

Finds memset/memcpy on non-trivial types.

```cpp
// BAD
std::string s;
memset(&s, 0, sizeof(s));  // undefined behavior!

// GOOD
std::string s;
s.clear();
```

## bugprone-undelegated-constructor

Finds constructor calls that don't delegate.

```cpp
// BAD
class Foo {
    Foo() { }
    Foo(int x) {
        Foo();  // creates temporary, doesn't delegate!
    }
};

// GOOD
class Foo {
    Foo() { }
    Foo(int x) : Foo() { }  // C++11 delegating constructor
};
```

## bugprone-unhandled-exception-at-new

Finds new expressions that may throw.

```cpp
// BAD
int* p = new int[size];  // may throw std::bad_alloc

// GOOD
int* p = new (std::nothrow) int[size];
if (!p) { /* handle */ }

// BETTER - use smart pointer
auto p = std::make_unique<int[]>(size);
```

## bugprone-unhandled-self-assignment

Finds copy assignment without self-assignment check.

```cpp
// BAD
Foo& operator=(const Foo& other) {
    delete ptr;
    ptr = new int(*other.ptr);  // crashes if this == &other
    return *this;
}

// GOOD
Foo& operator=(const Foo& other) {
    if (this != &other) {
        delete ptr;
        ptr = new int(*other.ptr);
    }
    return *this;
}

// BETTER - copy and swap
Foo& operator=(Foo other) {  // by value
    swap(*this, other);
    return *this;
}
```

## bugprone-unused-raii

Finds RAII objects created and immediately destroyed.

```cpp
// BAD
{
    std::lock_guard<std::mutex>(mutex);  // unnamed - destroyed immediately!
    // critical section not protected
}

// GOOD
{
    std::lock_guard<std::mutex> lock(mutex);  // named - lives until scope end
    // critical section protected
}
```

## bugprone-unused-return-value

Finds ignored return values.

```cpp
// BAD
std::remove(v.begin(), v.end(), value);  // doesn't erase!
empty();  // return value ignored

// GOOD
v.erase(std::remove(v.begin(), v.end(), value), v.end());
if (empty()) { }
```

## bugprone-use-after-move

Finds use of moved-from objects.

```cpp
// BAD
std::vector<int> v = {1, 2, 3};
auto v2 = std::move(v);
v.push_back(4);  // undefined behavior!

// GOOD
std::vector<int> v = {1, 2, 3};
auto v2 = std::move(v);
v.clear();  // now safe to reuse
v.push_back(4);
```

## bugprone-virtual-near-miss

Finds methods that almost override.

```cpp
// BAD - typo in override
class Base {
    virtual void doWork();
};

class Derived : public Base {
    void dowork();  // lowercase 'w' - doesn't override!
};

// GOOD
class Derived : public Base {
    void doWork() override;  // compiler catches mismatches
};
```
