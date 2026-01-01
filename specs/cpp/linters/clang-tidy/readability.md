# clang-tidy readability-* Checks

Code readability and clarity improvements.

## readability-avoid-const-params-in-decls

Don't use const for pass-by-value params in declarations.

```cpp
// BAD - const in declaration is noise
void foo(const int x);  // declaration
void foo(const int x) { }  // definition - const is fine here

// GOOD
void foo(int x);  // declaration
void foo(const int x) { }  // definition - const prevents accidental modification
```

## readability-avoid-nested-conditional-operator

Avoid nested ternary operators.

```cpp
// BAD - hard to read
int x = a ? b ? c : d : e;

// GOOD - use if/else
int x;
if (a) {
    x = b ? c : d;
} else {
    x = e;
}
```

## readability-braces-around-statements

Require braces for if/for/while.

```cpp
// BAD
if (condition)
    doSomething();

for (int i = 0; i < n; i++)
    process(i);

// GOOD
if (condition) {
    doSomething();
}

for (int i = 0; i < n; i++) {
    process(i);
}
```

## readability-const-return-type

Don't return const values.

```cpp
// BAD - prevents move semantics
const std::string getName() { return name_; }

// GOOD
std::string getName() { return name_; }

// Const reference is fine
const std::string& getName() const { return name_; }
```

## readability-container-contains

Use contains() instead of count/find (C++20).

```cpp
// BAD
if (set.count(value) > 0) { }
if (set.find(value) != set.end()) { }
if (map.count(key)) { }

// GOOD (C++20)
if (set.contains(value)) { }
if (map.contains(key)) { }
```

## readability-container-data-pointer

Use data() instead of &container[0].

```cpp
// BAD
char* p = &str[0];
int* q = &vec[0];

// GOOD
char* p = str.data();
int* q = vec.data();
```

## readability-container-size-empty

Use empty() instead of size() == 0.

```cpp
// BAD
if (vec.size() == 0) { }
if (str.size() != 0) { }
if (0 == list.size()) { }

// GOOD
if (vec.empty()) { }
if (!str.empty()) { }
if (!list.empty()) { }
```

## readability-convert-member-functions-to-static

Make member functions static if they don't use this.

```cpp
// BAD - doesn't use any members
class Foo {
    int helper(int x) { return x * 2; }
};

// GOOD
class Foo {
    static int helper(int x) { return x * 2; }
};
```

## readability-delete-null-pointer

Don't check for null before delete.

```cpp
// BAD - delete handles null
if (ptr != nullptr) {
    delete ptr;
}

// GOOD
delete ptr;
```

## readability-duplicate-include

Remove duplicate #include.

```cpp
// BAD
#include <vector>
#include <string>
#include <vector>  // duplicate

// GOOD
#include <string>
#include <vector>
```

## readability-else-after-return

Don't use else after return.

```cpp
// BAD
if (condition) {
    return a;
} else {
    return b;
}

// GOOD
if (condition) {
    return a;
}
return b;
```

## readability-function-cognitive-complexity

Limit cognitive complexity of functions.

```cpp
// BAD - high cognitive complexity
void process(Data& d) {
    if (d.valid) {                    // +1
        for (auto& item : d.items) {  // +2 (nested)
            if (item.active) {        // +3 (nested)
                for (auto& sub : item.subs) {  // +4 (nested)
                    if (sub.check()) {  // +5 (nested)
                        // ...
                    }
                }
            }
        }
    }
}  // complexity: 15+

// GOOD - extract functions
void processItem(Item& item);
void processSub(Sub& sub);

void process(Data& d) {
    if (!d.valid) return;
    for (auto& item : d.items) {
        processItem(item);
    }
}
```

## readability-function-size

Limit function size (lines, statements, parameters, nesting).

```cpp
// Configuration
CheckOptions:
  - key: readability-function-size.LineThreshold
    value: 100
  - key: readability-function-size.StatementThreshold
    value: 50
  - key: readability-function-size.ParameterThreshold
    value: 6
  - key: readability-function-size.NestingThreshold
    value: 4
```

## readability-identifier-length

Enforce minimum identifier length.

```cpp
// BAD - too short
int n;
for (int i; ...) { }
auto f = []() { };

// GOOD
int count;
for (int index; ...) { }
auto filter = []() { };

// Exceptions often configured for i, j, k, x, y, etc.
```

## readability-identifier-naming

Enforce naming conventions.

```cpp
// Configuration example
CheckOptions:
  - key: readability-identifier-naming.ClassCase
    value: CamelCase
  - key: readability-identifier-naming.FunctionCase
    value: camelBack
  - key: readability-identifier-naming.VariableCase
    value: lower_case
  - key: readability-identifier-naming.ConstantCase
    value: UPPER_CASE
  - key: readability-identifier-naming.MemberPrefix
    value: m_
  - key: readability-identifier-naming.PrivateMemberSuffix
    value: _
```

## readability-implicit-bool-conversion

Avoid implicit bool conversions.

```cpp
// BAD
int x = 5;
if (x) { }  // implicit conversion to bool
bool b = x;  // implicit conversion

// GOOD
if (x != 0) { }
bool b = (x != 0);

// Pointers are OK
int* p = getPointer();
if (p) { }  // common idiom
```

## readability-inconsistent-declaration-parameter-name

Parameter names should match across declarations.

```cpp
// BAD
void foo(int x, int y);  // declaration
void foo(int a, int b) { }  // definition - different names

// GOOD
void foo(int x, int y);  // declaration
void foo(int x, int y) { }  // definition - same names
```

## readability-isolate-declaration

One declaration per statement.

```cpp
// BAD
int x, y, z;
int* p, q;  // q is not a pointer!

// GOOD
int x;
int y;
int z;
int* p;
int* q;
```

## readability-magic-numbers

Avoid magic numbers.

```cpp
// BAD
if (age >= 18) { }
for (int i = 0; i < 86400; i++) { }
double area = 3.14159 * r * r;

// GOOD
constexpr int ADULT_AGE = 18;
constexpr int SECONDS_PER_DAY = 86400;
constexpr double PI = 3.14159;

if (age >= ADULT_AGE) { }
for (int i = 0; i < SECONDS_PER_DAY; i++) { }
double area = PI * r * r;
```

## readability-make-member-function-const

Make member functions const if they don't modify state.

```cpp
// BAD
class Foo {
    int x_;
    int getX() { return x_; }  // doesn't modify, should be const
};

// GOOD
class Foo {
    int x_;
    int getX() const { return x_; }
};
```

## readability-misleading-indentation

Catch misleading indentation.

```cpp
// BAD
if (condition)
    foo();
    bar();  // looks like it's in the if, but isn't!

// GOOD
if (condition) {
    foo();
}
bar();
```

## readability-misplaced-array-index

Prefer arr[index] over index[arr].

```cpp
// BAD (but valid C/C++)
int x = 5[arr];  // same as arr[5]

// GOOD
int x = arr[5];
```

## readability-named-parameter

Give names to function parameters.

```cpp
// BAD
void process(int, std::string, bool);

// GOOD
void process(int id, std::string name, bool verbose);

// If intentionally unused, use comment
void callback(int /*unused*/, std::string name);
```

## readability-non-const-parameter

Make pointer parameters const if not modified.

```cpp
// BAD
void print(int* data, size_t size);  // doesn't modify data

// GOOD
void print(const int* data, size_t size);
```

## readability-qualified-auto

Use auto* and auto& explicitly.

```cpp
// BAD - unclear if pointer
auto p = getPointer();

// GOOD - explicit pointer
auto* p = getPointer();

// BAD - unclear if reference
auto r = getReference();

// GOOD - explicit reference
auto& r = getReference();
```

## readability-redundant-access-specifiers

Remove redundant access specifiers.

```cpp
// BAD
class Foo {
public:
    void foo();
public:  // redundant
    void bar();
};

// GOOD
class Foo {
public:
    void foo();
    void bar();
};
```

## readability-redundant-control-flow

Remove redundant control flow.

```cpp
// BAD
void foo() {
    doSomething();
    return;  // redundant
}

for (...) {
    if (condition) {
        continue;  // at end of loop, redundant
    }
}

// GOOD
void foo() {
    doSomething();
}

for (...) {
    if (!condition) {
        // work
    }
}
```

## readability-redundant-declaration

Remove redundant declarations.

```cpp
// BAD
extern int x;
extern int x;  // redundant

// GOOD
extern int x;
```

## readability-redundant-member-init

Remove redundant member initializers.

```cpp
// BAD
class Foo {
    int x = 0;
    std::string s = "";
public:
    Foo() : x(0), s("") {}  // redundant - same as defaults
};

// GOOD
class Foo {
    int x = 0;
    std::string s;  // default-initialized to ""
public:
    Foo() = default;
};
```

## readability-redundant-preprocessor

Remove redundant preprocessor directives.

```cpp
// BAD
#ifndef FOO
#ifndef FOO  // redundant
#define FOO
#endif
#endif

// GOOD
#ifndef FOO
#define FOO
#endif
```

## readability-redundant-smartptr-get

Remove redundant smart pointer get().

```cpp
// BAD
if (ptr.get() != nullptr) { }
if (ptr.get()) { }
*ptr.get();

// GOOD
if (ptr != nullptr) { }
if (ptr) { }
*ptr;
```

## readability-redundant-string-cstr

Remove redundant c_str() calls.

```cpp
// BAD
std::string s = str.c_str();
printf("%s", str.c_str());  // needed for C functions

// GOOD
std::string s = str;
std::cout << str;  // no c_str() needed
```

## readability-redundant-string-init

Remove redundant string initialization.

```cpp
// BAD
std::string s = "";
std::string s("");
std::string s{""};

// GOOD
std::string s;  // default is empty
```

## readability-simplify-boolean-expr

Simplify boolean expressions.

```cpp
// BAD
if (condition == true) { }
if (condition == false) { }
bool b = condition ? true : false;
return condition ? true : false;

// GOOD
if (condition) { }
if (!condition) { }
bool b = condition;
return condition;
```

## readability-simplify-subscript-expr

Simplify subscript expressions.

```cpp
// BAD
str.data()[0];
vec.data()[i];

// GOOD
str[0];
vec[i];
```

## readability-static-accessed-through-instance

Access static members through class name.

```cpp
// BAD
Foo foo;
foo.staticMethod();
foo.STATIC_CONSTANT;

// GOOD
Foo::staticMethod();
Foo::STATIC_CONSTANT;
```

## readability-string-compare

Use comparison operators for strings.

```cpp
// BAD
if (str.compare("other") == 0) { }
if (str.compare("other") != 0) { }

// GOOD
if (str == "other") { }
if (str != "other") { }
```

## readability-suspicious-call-argument

Finds likely argument swaps.

```cpp
// BAD
void setRect(int x, int y, int width, int height);
setRect(width, height, x, y);  // suspicious - names suggest swap

// GOOD
setRect(x, y, width, height);
```

## readability-uniqueptr-delete-release

Use reset() instead of delete + release().

```cpp
// BAD
delete ptr.release();

// GOOD
ptr.reset();
```

## readability-uppercase-literal-suffix

Use uppercase literal suffixes.

```cpp
// BAD
long x = 42l;      // l looks like 1
float f = 3.14f;   // inconsistent
unsigned u = 42u;

// GOOD
long x = 42L;
float f = 3.14F;
unsigned u = 42U;
long long ll = 42LL;
```

## readability-use-anyofallof

Use std::any_of/all_of/none_of.

```cpp
// BAD
bool found = false;
for (const auto& item : items) {
    if (item.matches()) {
        found = true;
        break;
    }
}

// GOOD
bool found = std::any_of(items.begin(), items.end(),
    [](const auto& item) { return item.matches(); });

// C++20 ranges
bool found = std::ranges::any_of(items, &Item::matches);
```
