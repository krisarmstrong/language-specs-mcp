# C++ Language Specification Summary
Version: c++23

Source: https://en.cppreference.com/w/cpp


Based on C++23 (ISO/IEC 14882:2024)

## Keywords (C++23)

```cpp
alignas         alignof         and             and_eq
asm             auto            bitand          bitor
bool            break           case            catch
char            char8_t         char16_t        char32_t
class           compl           concept         const
consteval       constexpr       constinit       const_cast
continue        co_await        co_return       co_yield
decltype        default         delete          do
double          dynamic_cast    else            enum
explicit        export          extern          false
float           for             friend          goto
if              inline          int             long
mutable         namespace       new             noexcept
not             not_eq          nullptr         operator
or              or_eq           private         protected
public          register        reinterpret_cast requires
return          short           signed          sizeof
static          static_assert   static_cast     struct
switch          template        this            thread_local
throw           true            try             typedef
typeid          typename        union           unsigned
using           virtual         void            volatile
wchar_t         while           xor             xor_eq
```

## Types

### Fundamental Types

```cpp
// Boolean
bool                    // true or false

// Characters
char                    // at least 8 bits
wchar_t                 // wide character
char8_t                 // UTF-8 (C++20)
char16_t                // UTF-16
char32_t                // UTF-32

// Integers
short                   // at least 16 bits
int                     // at least 16 bits
long                    // at least 32 bits
long long               // at least 64 bits

// Floating point
float                   // single precision
double                  // double precision
long double             // extended precision

// Void
void                    // no type/value

// Null pointer
std::nullptr_t          // type of nullptr
```

### Fixed-Width Types

```cpp
#include <cstdint>

int8_t      int16_t     int32_t     int64_t
uint8_t     uint16_t    uint32_t    uint64_t
intptr_t    uintptr_t
size_t      ptrdiff_t
```

### Type Aliases

```cpp
using IntPtr = int*;
using Callback = void(*)(int);
using StringVector = std::vector<std::string>;

// Template alias
template<typename T>
using Vec = std::vector<T>;
```

## Auto and Decltype

```cpp
// Type inference
auto x = 42;            // int
auto y = 3.14;          // double
auto z = "hello";       // const char*
auto v = std::vector{1, 2, 3};  // std::vector<int>

// Decltype
int x = 0;
decltype(x) y = 1;      // int
decltype(auto) z = x;   // int (preserves value category)

// Trailing return type
auto add(int a, int b) -> int {
    return a + b;
}

// C++14: return type deduction
auto add(int a, int b) {
    return a + b;
}
```

## Classes

### Basic Class

```cpp
class Widget {
public:
    Widget();                           // default constructor
    Widget(int value);                  // parameterized constructor
    Widget(const Widget& other);        // copy constructor
    Widget(Widget&& other) noexcept;    // move constructor
    ~Widget();                          // destructor
    
    Widget& operator=(const Widget& other);     // copy assignment
    Widget& operator=(Widget&& other) noexcept; // move assignment
    
    int getValue() const;
    void setValue(int value);
    
private:
    int value_;
    std::string name_;
};
```

### Rule of Zero/Five

```cpp
// Rule of Zero: Use RAII, no manual resource management
class Good {
    std::string name;
    std::vector<int> data;
    std::unique_ptr<Resource> resource;
    // No destructor, copy/move ops needed
};

// Rule of Five: If you define one, define all
class Manual {
    int* data;
public:
    Manual() : data(new int[100]) {}
    ~Manual() { delete[] data; }
    Manual(const Manual& other);
    Manual& operator=(const Manual& other);
    Manual(Manual&& other) noexcept;
    Manual& operator=(Manual&& other) noexcept;
};
```

### Inheritance

```cpp
class Base {
public:
    virtual void method() = 0;      // pure virtual
    virtual void other() {}         // virtual with default
    void concrete() {}              // non-virtual
    virtual ~Base() = default;      // virtual destructor
};

class Derived : public Base {
public:
    void method() override;         // override
    void other() final;             // can't be overridden further
};
```

## Templates

### Function Templates

```cpp
template<typename T>
T max(T a, T b) {
    return a > b ? a : b;
}

// With concepts (C++20)
template<typename T>
requires std::integral<T>
T gcd(T a, T b) {
    return b == 0 ? a : gcd(b, a % b);
}

// Abbreviated function template (C++20)
auto add(auto a, auto b) {
    return a + b;
}
```

### Class Templates

```cpp
template<typename T, size_t N>
class Array {
    T data[N];
public:
    T& operator[](size_t i) { return data[i]; }
    constexpr size_t size() const { return N; }
};

// Deduction guides (C++17)
template<typename T, typename... Args>
Array(T, Args...) -> Array<T, 1 + sizeof...(Args)>;
```

### Concepts (C++20)

```cpp
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template<typename T>
concept Printable = requires(T t) {
    { std::cout << t } -> std::same_as<std::ostream&>;
};

template<Numeric T>
T square(T x) {
    return x * x;
}
```

### Variadic Templates

```cpp
template<typename... Args>
void print(Args... args) {
    (std::cout << ... << args) << '\n';  // fold expression
}

// Pack expansion
template<typename... Ts>
auto sum(Ts... args) {
    return (args + ...);  // unary right fold
}
```

## Smart Pointers

```cpp
#include <memory>

// Unique ownership
std::unique_ptr<Widget> p1 = std::make_unique<Widget>();
auto p2 = std::make_unique<Widget[]>(10);  // array

// Shared ownership
std::shared_ptr<Widget> p3 = std::make_shared<Widget>();
std::shared_ptr<Widget> p4 = p3;  // both own

// Weak reference (doesn't extend lifetime)
std::weak_ptr<Widget> w = p3;
if (auto p = w.lock()) {
    // use p
}
```

## Move Semantics

```cpp
class Buffer {
    std::unique_ptr<char[]> data_;
    size_t size_;
    
public:
    // Move constructor
    Buffer(Buffer&& other) noexcept
        : data_(std::move(other.data_))
        , size_(std::exchange(other.size_, 0))
    {}
    
    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        data_ = std::move(other.data_);
        size_ = std::exchange(other.size_, 0);
        return *this;
    }
};

// Perfect forwarding
template<typename T, typename... Args>
std::unique_ptr<T> make(Args&&... args) {
    return std::make_unique<T>(std::forward<Args>(args)...);
}
```

## Lambda Expressions

```cpp
// Basic lambda
auto add = [](int a, int b) { return a + b; };

// With capture
int x = 10;
auto addX = [x](int a) { return a + x; };      // capture by value
auto addX = [&x](int a) { return a + x; };     // capture by reference
auto addX = [=](int a) { return a + x; };      // capture all by value
auto addX = [&](int a) { return a + x; };      // capture all by reference

// Mutable lambda
auto counter = [n = 0]() mutable { return ++n; };

// Generic lambda (C++14)
auto add = [](auto a, auto b) { return a + b; };

// Template lambda (C++20)
auto add = []<typename T>(T a, T b) { return a + b; };
```

## Ranges (C++20)

```cpp
#include <ranges>

std::vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

// Views
auto even = v | std::views::filter([](int n) { return n % 2 == 0; });
auto squared = v | std::views::transform([](int n) { return n * n; });

// Chained
auto result = v 
    | std::views::filter([](int n) { return n % 2 == 0; })
    | std::views::transform([](int n) { return n * n; })
    | std::views::take(3);

// Range algorithms
std::ranges::sort(v);
auto it = std::ranges::find(v, 5);
```

## Coroutines (C++20)

```cpp
#include <coroutine>
#include <generator>  // C++23

// Generator
std::generator<int> range(int start, int end) {
    for (int i = start; i < end; ++i) {
        co_yield i;
    }
}

// Usage
for (int i : range(0, 10)) {
    std::cout << i << '\n';
}
```

## Modules (C++20)

```cpp
// math.ixx (module interface)
export module math;

export int add(int a, int b) {
    return a + b;
}

// main.cpp
import math;

int main() {
    return add(1, 2);
}
```

## Structured Bindings (C++17)

```cpp
// With arrays
int arr[] = {1, 2, 3};
auto [a, b, c] = arr;

// With structs
struct Point { int x, y; };
Point p{10, 20};
auto [x, y] = p;

// With maps
std::map<std::string, int> m;
for (const auto& [key, value] : m) {
    std::cout << key << ": " << value << '\n';
}
```

## std::optional, variant, expected

```cpp
// Optional (C++17)
std::optional<int> find(const std::vector<int>& v, int target) {
    auto it = std::find(v.begin(), v.end(), target);
    if (it != v.end()) return *it;
    return std::nullopt;
}

// Variant (C++17)
std::variant<int, std::string, double> v = "hello";
std::visit([](auto&& arg) { std::cout << arg; }, v);

// Expected (C++23)
std::expected<int, std::string> divide(int a, int b) {
    if (b == 0) return std::unexpected("division by zero");
    return a / b;
}
```

## Constexpr and Consteval

```cpp
// Constexpr: may be evaluated at compile time
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

constexpr int f5 = factorial(5);  // compile-time
int runtime_n = get_value();
int fn = factorial(runtime_n);    // runtime OK too

// Consteval (C++20): must be evaluated at compile time
consteval int square(int n) {
    return n * n;
}

constexpr int s = square(5);   // OK: compile-time
int x = 5;
int y = square(x);             // ERROR: not compile-time

// Constinit (C++20): must be constant initialized
constinit int global = 42;     // OK
constinit int bad = get();     // ERROR if get() not constexpr
```

## Attributes

```cpp
[[nodiscard]] int compute();
[[nodiscard("reason")]] int compute2();  // C++20

[[deprecated]] void old_func();
[[deprecated("use new_func")]] void old_func2();

[[maybe_unused]] void callback(int x);

[[noreturn]] void terminate();

[[likely]] if (condition) { }   // C++20
[[unlikely]] if (error) { }     // C++20

[[assume(x > 0)]]  // C++23
```
