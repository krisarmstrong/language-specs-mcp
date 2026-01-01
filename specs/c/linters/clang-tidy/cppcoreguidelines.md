# clang-tidy cppcoreguidelines-* Checks

Checks based on the C++ Core Guidelines (https://isocpp.github.io/CppCoreGuidelines/).

## cppcoreguidelines-avoid-c-arrays

Use std::array or std::vector instead of C arrays.

```cpp
// BAD
int arr[10];
void foo(int arr[]);

// GOOD
std::array<int, 10> arr;
void foo(std::span<int> arr);  // C++20
void foo(int* arr, size_t size);  // pre-C++20
```

## cppcoreguidelines-avoid-const-or-ref-data-members

Avoid const or reference data members.

```cpp
// BAD - makes class non-assignable
class Foo {
    const int id;           // can't reassign
    std::string& name_ref;  // can't reassign
};

// GOOD
class Foo {
    int id;                 // can reassign
    std::string* name_ptr;  // can reassign (or use accessor)
    
    // If immutable ID needed, make it private with getter only
    int getId() const { return id_; }
private:
    int id_;
};
```

## cppcoreguidelines-avoid-do-while

Avoid do-while loops.

```cpp
// BAD - condition at end, harder to reason about
do {
    process();
} while (condition);

// GOOD - condition at start
while (true) {
    process();
    if (!condition) break;
}

// Or restructure
process();
while (condition) {
    process();
}
```

## cppcoreguidelines-avoid-goto

Don't use goto.

```cpp
// BAD
if (error) goto cleanup;
// ...
cleanup:
    free(resources);

// GOOD - RAII
{
    auto guard = make_scope_guard([] { free(resources); });
    if (error) return;
    // ...
}  // guard cleans up
```

## cppcoreguidelines-avoid-magic-numbers

Same as readability-magic-numbers.

## cppcoreguidelines-avoid-non-const-global-variables

Avoid non-const global variables.

```cpp
// BAD
int globalCounter = 0;
std::string globalConfig;

// GOOD - const is OK
const int MAX_SIZE = 100;
constexpr double PI = 3.14159;

// GOOD - encapsulate in function
int& getCounter() {
    static int counter = 0;
    return counter;
}
```

## cppcoreguidelines-avoid-reference-coroutine-parameters

Don't pass by reference to coroutines.

```cpp
// BAD - reference may dangle
task<void> process(const std::string& s) {
    co_await something();
    use(s);  // s may be dangling!
}

// GOOD - pass by value
task<void> process(std::string s) {
    co_await something();
    use(s);  // s is owned by coroutine
}
```

## cppcoreguidelines-c-copy-assignment-signature

Copy assignment should return reference to *this.

```cpp
// BAD
void operator=(const Foo& other);
Foo operator=(const Foo& other);

// GOOD
Foo& operator=(const Foo& other) {
    // ...
    return *this;
}
```

## cppcoreguidelines-init-variables

Initialize variables on declaration.

```cpp
// BAD
int x;
double* p;

// GOOD
int x = 0;
double* p = nullptr;

// C++11 brace initialization
int x{};
double* p{};
```

## cppcoreguidelines-interfaces-global-init

Avoid global initializer order issues.

```cpp
// BAD - initialization order undefined
// file1.cpp
std::string config = getConfig();

// file2.cpp
extern std::string config;
Logger logger(config);  // config might not be initialized yet!

// GOOD - lazy initialization
const std::string& getConfig() {
    static std::string config = loadConfig();
    return config;
}
```

## cppcoreguidelines-macro-usage

Avoid macros for constants/functions.

```cpp
// BAD
#define PI 3.14159
#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// GOOD
constexpr double PI = 3.14159;

template<typename T>
constexpr T square(T x) { return x * x; }

template<typename T>
constexpr T max(T a, T b) { return a > b ? a : b; }
```

## cppcoreguidelines-misleading-capture-default-by-value

Warn about capturing this by value default.

```cpp
// BAD - [=] captures this by value, not *this
class Foo {
    int x;
    void bar() {
        auto f = [=] { return x; };  // captures this pointer
    }
};

// GOOD - explicit capture
class Foo {
    int x;
    void bar() {
        auto f = [this] { return x; };     // explicit this pointer
        auto g = [*this] { return x; };    // copies *this (C++17)
        auto h = [x = x] { return x; };    // capture by value
    }
};
```

## cppcoreguidelines-missing-std-forward

Use std::forward with forwarding references.

```cpp
// BAD - loses rvalue-ness
template<typename T>
void wrapper(T&& arg) {
    inner(arg);  // always lvalue
}

// GOOD
template<typename T>
void wrapper(T&& arg) {
    inner(std::forward<T>(arg));
}
```

## cppcoreguidelines-narrowing-conversions

Avoid narrowing conversions.

```cpp
// BAD
int i = 3.14;           // narrowing
char c = 1000;          // narrowing, overflow
float f = 1e100;        // narrowing, overflow

// GOOD
int i = static_cast<int>(3.14);  // explicit
auto i = static_cast<int>(3.14);

// Or use gsl::narrow
int i = gsl::narrow<int>(3.14);  // throws on data loss
int i = gsl::narrow_cast<int>(3.14);  // asserts in debug
```

## cppcoreguidelines-no-malloc

Don't use malloc/free.

```cpp
// BAD
int* p = (int*)malloc(sizeof(int) * 10);
free(p);

// GOOD
auto p = std::make_unique<int[]>(10);

// Or std::vector for dynamic arrays
std::vector<int> v(10);
```

## cppcoreguidelines-owning-memory

Use gsl::owner for raw owning pointers.

```cpp
// BAD - unclear ownership
int* create() {
    return new int(42);  // caller must delete?
}

// GOOD - explicit ownership
gsl::owner<int*> create() {
    return new int(42);  // caller must delete
}

// BETTER - use smart pointers
std::unique_ptr<int> create() {
    return std::make_unique<int>(42);
}
```

## cppcoreguidelines-prefer-member-initializer

Initialize members in member initializer list.

```cpp
// BAD
class Foo {
    int x;
    std::string name;
public:
    Foo() {
        x = 0;        // assignment, not initialization
        name = "";    // assignment, not initialization
    }
};

// GOOD
class Foo {
    int x;
    std::string name;
public:
    Foo() : x(0), name("") {}
};

// BETTER - default member initializers
class Foo {
    int x = 0;
    std::string name;
public:
    Foo() = default;
};
```

## cppcoreguidelines-pro-bounds-array-to-pointer-decay

Avoid array-to-pointer decay.

```cpp
// BAD - loses size information
void foo(int* arr);
int arr[10];
foo(arr);  // decays to pointer

// GOOD
void foo(std::span<int> arr);  // C++20
void foo(int* arr, size_t size);

template<size_t N>
void foo(int (&arr)[N]);  // preserves size
```

## cppcoreguidelines-pro-bounds-constant-array-index

Use gsl::at() or bounds-checked access.

```cpp
// BAD - no bounds checking
arr[i];
vec[i];

// GOOD
gsl::at(arr, i);  // throws if out of bounds
vec.at(i);        // throws if out of bounds
```

## cppcoreguidelines-pro-bounds-pointer-arithmetic

Avoid pointer arithmetic.

```cpp
// BAD
p++;
p + n;
p[n];

// GOOD - use std::span or iterators
for (int x : std::span(p, size)) { }
for (auto it = vec.begin(); it != vec.end(); ++it) { }
```

## cppcoreguidelines-pro-type-const-cast

Don't use const_cast.

```cpp
// BAD
const_cast<int*>(ptr);

// GOOD - fix the design
// If you need non-const, don't make it const
// If API requires const, don't cast it away
```

## cppcoreguidelines-pro-type-cstyle-cast

Don't use C-style casts.

```cpp
// BAD
int x = (int)3.14;
void* p = (void*)ptr;

// GOOD
int x = static_cast<int>(3.14);
void* p = static_cast<void*>(ptr);
```

## cppcoreguidelines-pro-type-member-init

Initialize all members.

```cpp
// BAD
class Foo {
    int x;      // uninitialized
    int* ptr;   // uninitialized
};

// GOOD
class Foo {
    int x = 0;
    int* ptr = nullptr;
};
```

## cppcoreguidelines-pro-type-reinterpret-cast

Don't use reinterpret_cast.

```cpp
// BAD
int* p = reinterpret_cast<int*>(addr);

// GOOD - use std::bit_cast (C++20)
auto p = std::bit_cast<int*>(addr);

// Or design to not need it
```

## cppcoreguidelines-pro-type-static-cast-downcast

Use dynamic_cast for downcasting.

```cpp
// BAD - no runtime check
Derived* d = static_cast<Derived*>(base);

// GOOD - runtime checked
Derived* d = dynamic_cast<Derived*>(base);
if (d) {
    // safe to use
}
```

## cppcoreguidelines-pro-type-union-access

Don't access union members directly.

```cpp
// BAD
union U {
    int i;
    float f;
};
U u;
u.i = 1;
float f = u.f;  // undefined behavior

// GOOD - use std::variant
std::variant<int, float> v = 1;
int i = std::get<int>(v);
```

## cppcoreguidelines-pro-type-vararg

Don't use C-style varargs.

```cpp
// BAD
void log(const char* fmt, ...);

// GOOD - use variadic templates
template<typename... Args>
void log(std::format_string<Args...> fmt, Args&&... args) {
    std::cout << std::format(fmt, std::forward<Args>(args)...);
}
```

## cppcoreguidelines-rvalue-reference-param-not-moved

Move from rvalue reference parameters.

```cpp
// BAD - takes rvalue but copies
void foo(std::string&& s) {
    member_ = s;  // copies!
}

// GOOD
void foo(std::string&& s) {
    member_ = std::move(s);
}
```

## cppcoreguidelines-slicing

Avoid object slicing.

```cpp
// BAD
Derived d;
Base b = d;  // slices off Derived part

void foo(Base b);
foo(Derived());  // sliced on copy

// GOOD
Base& b = d;              // reference preserves type
void foo(const Base& b);  // reference parameter
void foo(Base* b);        // pointer parameter
```

## cppcoreguidelines-special-member-functions

Follow rule of zero/five.

```cpp
// BAD - violates rule of 5
class Foo {
    int* data;
public:
    ~Foo() { delete data; }  // only destructor
    // missing: copy ctor, copy assign, move ctor, move assign
};

// GOOD - rule of 5
class Foo {
    int* data;
public:
    ~Foo() { delete data; }
    Foo(const Foo& other);
    Foo& operator=(const Foo& other);
    Foo(Foo&& other) noexcept;
    Foo& operator=(Foo&& other) noexcept;
};

// BETTER - rule of 0
class Foo {
    std::unique_ptr<int> data;
    // compiler generates correct special members
};
```

## cppcoreguidelines-virtual-class-destructor

Virtual classes need virtual destructor.

```cpp
// BAD
class Base {
    virtual void foo();
    ~Base();  // non-virtual!
};

delete basePtr;  // undefined if points to Derived

// GOOD
class Base {
    virtual void foo();
    virtual ~Base() = default;
};
```
