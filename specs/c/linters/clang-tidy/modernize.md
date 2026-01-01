# clang-tidy modernize-* Checks

Modernize C++ code to newer standards (C++11/14/17/20/23).

## modernize-avoid-bind

Replace std::bind with lambdas.

```cpp
// BAD
auto f = std::bind(&Foo::bar, this, std::placeholders::_1);

// GOOD
auto f = [this](int x) { return bar(x); };
```

## modernize-avoid-c-arrays

Use std::array or std::vector instead of C arrays.

```cpp
// BAD
int arr[10];
int arr[] = {1, 2, 3};

// GOOD
std::array<int, 10> arr;
std::array arr = {1, 2, 3};  // C++17 CTAD
std::vector<int> arr = {1, 2, 3};
```

## modernize-concat-nested-namespaces

Use C++17 nested namespace syntax.

```cpp
// BAD
namespace foo {
namespace bar {
namespace baz {
}
}
}

// GOOD (C++17)
namespace foo::bar::baz {
}
```

## modernize-deprecated-headers

Replace deprecated C headers with C++ equivalents.

```cpp
// BAD
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

// GOOD
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdint>
```

## modernize-deprecated-ios-base-aliases

Replace deprecated iostream aliases.

```cpp
// BAD
std::ios_base::io_state
std::ios_base::open_mode
std::ios_base::seek_dir

// GOOD
std::ios_base::iostate
std::ios_base::openmode
std::ios_base::seekdir
```

## modernize-loop-convert

Convert for loops to range-based for.

```cpp
// BAD
for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
    std::cout << *it;
}

for (int i = 0; i < v.size(); ++i) {
    std::cout << v[i];
}

// GOOD
for (int x : v) {
    std::cout << x;
}

for (const auto& x : v) {
    std::cout << x;
}
```

## modernize-make-shared

Use std::make_shared instead of new.

```cpp
// BAD
std::shared_ptr<Foo> p(new Foo(1, 2));
std::shared_ptr<Foo> p = std::shared_ptr<Foo>(new Foo());

// GOOD
auto p = std::make_shared<Foo>(1, 2);
```

**Why:** Single allocation, exception safe.

## modernize-make-unique

Use std::make_unique instead of new.

```cpp
// BAD
std::unique_ptr<Foo> p(new Foo(1, 2));
std::unique_ptr<Foo[]> arr(new Foo[10]);

// GOOD
auto p = std::make_unique<Foo>(1, 2);
auto arr = std::make_unique<Foo[]>(10);
```

## modernize-pass-by-value

Pass by value and move for sink parameters.

```cpp
// BAD - copies even when caller has temporary
class Foo {
    std::string name_;
public:
    void setName(const std::string& name) {
        name_ = name;
    }
};

// GOOD - moves temporaries, copies lvalues
class Foo {
    std::string name_;
public:
    void setName(std::string name) {
        name_ = std::move(name);
    }
};
```

## modernize-raw-string-literal

Use raw string literals for complex escapes.

```cpp
// BAD
const char* regex = "\\d+\\.\\d+";
const char* path = "C:\\Users\\name\\file";
const char* json = "{\"key\": \"value\"}";

// GOOD
const char* regex = R"(\d+\.\d+)";
const char* path = R"(C:\Users\name\file)";
const char* json = R"({"key": "value"})";

// With delimiter for strings containing )
const char* s = R"delim(contains ) character)delim";
```

## modernize-redundant-void-arg

Remove redundant void in empty parameter lists.

```cpp
// BAD (C-style)
int foo(void);
int bar(void) { return 0; }

// GOOD (C++)
int foo();
int bar() { return 0; }
```

## modernize-replace-auto-ptr

Replace deprecated std::auto_ptr with std::unique_ptr.

```cpp
// BAD (removed in C++17)
std::auto_ptr<Foo> p(new Foo());

// GOOD
std::unique_ptr<Foo> p = std::make_unique<Foo>();
```

## modernize-replace-disallow-copy-and-assign-macro

Replace DISALLOW_COPY macro with deleted functions.

```cpp
// BAD
class Foo {
    DISALLOW_COPY_AND_ASSIGN(Foo);
};

// GOOD
class Foo {
    Foo(const Foo&) = delete;
    Foo& operator=(const Foo&) = delete;
};
```

## modernize-replace-random-shuffle

Replace std::random_shuffle with std::shuffle.

```cpp
// BAD (removed in C++17)
std::random_shuffle(v.begin(), v.end());

// GOOD
std::random_device rd;
std::mt19937 g(rd());
std::shuffle(v.begin(), v.end(), g);
```

## modernize-return-braced-init-list

Use braced init for return.

```cpp
// BAD
std::pair<int, int> foo() {
    return std::make_pair(1, 2);
}

// GOOD
std::pair<int, int> foo() {
    return {1, 2};
}
```

## modernize-shrink-to-fit

Use shrink_to_fit() instead of swap trick.

```cpp
// BAD
std::vector<int>(v).swap(v);

// GOOD
v.shrink_to_fit();
```

## modernize-unary-static-assert

Use single-argument static_assert (C++17).

```cpp
// BAD
static_assert(sizeof(int) == 4, "");

// GOOD (C++17)
static_assert(sizeof(int) == 4);
```

## modernize-use-auto

Use auto where type is obvious.

```cpp
// BAD
std::vector<int>::iterator it = v.begin();
std::unique_ptr<Foo> p = std::make_unique<Foo>();
Widget* w = new Widget();

// GOOD
auto it = v.begin();
auto p = std::make_unique<Foo>();
auto* w = new Widget();  // auto* makes pointer explicit
```

## modernize-use-bool-literals

Use true/false instead of integer literals.

```cpp
// BAD
bool b = 1;
bool c = 0;
function(1);  // where param is bool

// GOOD
bool b = true;
bool c = false;
function(true);
```

## modernize-use-default-member-init

Use default member initializers.

```cpp
// BAD
class Foo {
    int x;
    std::string name;
public:
    Foo() : x(0), name("default") {}
};

// GOOD
class Foo {
    int x = 0;
    std::string name = "default";
public:
    Foo() = default;
};
```

## modernize-use-emplace

Use emplace instead of push_back with temporaries.

```cpp
// BAD
v.push_back(Foo(1, 2));
v.push_back(std::make_pair(1, 2));

// GOOD
v.emplace_back(1, 2);
```

## modernize-use-equals-default

Use = default for trivial special members.

```cpp
// BAD
class Foo {
public:
    Foo() {}
    ~Foo() {}
    Foo(const Foo& other) : x(other.x) {}
};

// GOOD
class Foo {
public:
    Foo() = default;
    ~Foo() = default;
    Foo(const Foo&) = default;
};
```

## modernize-use-equals-delete

Use = delete instead of private undefined.

```cpp
// BAD (C++03 style)
class Foo {
private:
    Foo(const Foo&);  // undefined
    Foo& operator=(const Foo&);  // undefined
};

// GOOD
class Foo {
public:
    Foo(const Foo&) = delete;
    Foo& operator=(const Foo&) = delete;
};
```

## modernize-use-nodiscard

Add [[nodiscard]] where appropriate.

```cpp
// BAD
bool isEmpty() const { return size_ == 0; }
Error validate() const { return check(); }

// GOOD
[[nodiscard]] bool isEmpty() const { return size_ == 0; }
[[nodiscard]] Error validate() const { return check(); }
```

## modernize-use-noexcept

Use noexcept instead of throw().

```cpp
// BAD
void foo() throw();
void bar() throw(std::exception);

// GOOD
void foo() noexcept;
void bar();  // may throw
```

## modernize-use-nullptr

Use nullptr instead of NULL or 0.

```cpp
// BAD
int* p = NULL;
int* q = 0;
if (p == NULL) {}

// GOOD
int* p = nullptr;
int* q = nullptr;
if (p == nullptr) {}
if (!p) {}  // also fine
```

## modernize-use-override

Use override for virtual function overrides.

```cpp
// BAD
class Derived : public Base {
    virtual void foo();  // override? new virtual?
    void bar();          // override? non-virtual?
};

// GOOD
class Derived : public Base {
    void foo() override;     // definitely overrides
    void bar() override;     // compiler error if Base::bar not virtual
};
```

## modernize-use-starts-ends-with

Use starts_with/ends_with (C++20).

```cpp
// BAD
if (s.find("prefix") == 0) {}
if (s.rfind("suffix") == s.size() - 6) {}
if (s.substr(0, 6) == "prefix") {}

// GOOD (C++20)
if (s.starts_with("prefix")) {}
if (s.ends_with("suffix")) {}
```

## modernize-use-std-print

Use std::print instead of printf (C++23).

```cpp
// BAD
printf("Hello %s, you are %d\n", name, age);
std::cout << "Hello " << name << ", you are " << age << "\n";

// GOOD (C++23)
std::print("Hello {}, you are {}\n", name, age);
std::println("Hello {}, you are {}", name, age);
```

## modernize-use-trailing-return-type

Use trailing return type syntax.

```cpp
// Traditional
int foo();
std::vector<int> bar();

// Trailing (useful for templates, decltype)
auto foo() -> int;
auto bar() -> std::vector<int>;

// Required for some cases
template<typename T, typename U>
auto add(T t, U u) -> decltype(t + u);
```

## modernize-use-transparent-functors

Use transparent comparators.

```cpp
// BAD - requires exact key type
std::map<std::string, int> m;
m.find("key");  // constructs temporary std::string

// GOOD - heterogeneous lookup
std::map<std::string, int, std::less<>> m;
m.find("key");  // compares directly with const char*
```

## modernize-use-uncaught-exceptions

Use std::uncaught_exceptions (plural).

```cpp
// BAD (deprecated in C++17, removed in C++20)
bool throwing = std::uncaught_exception();

// GOOD
int count = std::uncaught_exceptions();
bool throwing = count > 0;
```

## modernize-use-using

Use using instead of typedef.

```cpp
// BAD
typedef std::vector<int> IntVector;
typedef int (*FuncPtr)(int, int);
typedef std::map<std::string, std::vector<int>> StringToInts;

// GOOD
using IntVector = std::vector<int>;
using FuncPtr = int (*)(int, int);
using StringToInts = std::map<std::string, std::vector<int>>;

// Template aliases only work with using
template<typename T>
using Vec = std::vector<T>;
```
