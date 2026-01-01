# clang-tidy performance-* Checks

Performance optimization checks.

## performance-avoid-endl

Use '\n' instead of std::endl.

```cpp
// BAD - endl flushes buffer every time
std::cout << "line 1" << std::endl;
std::cout << "line 2" << std::endl;

// GOOD - '\n' doesn't flush
std::cout << "line 1\n";
std::cout << "line 2\n";

// Explicit flush when needed
std::cout << "prompt: " << std::flush;
```

## performance-faster-string-find

Use character overload for single-char find.

```cpp
// BAD - string overload, more overhead
str.find("x");
str.rfind("x");
str.find_first_of("x");
str.find_last_of("x");

// GOOD - character overload, faster
str.find('x');
str.rfind('x');
str.find_first_of('x');
str.find_last_of('x');
```

## performance-for-range-copy

Avoid unnecessary copies in range-based for.

```cpp
// BAD - copies every element
for (auto item : container) {
    use(item);
}

// GOOD - reference, no copy
for (const auto& item : container) {
    use(item);
}

// For modification
for (auto& item : container) {
    modify(item);
}
```

## performance-implicit-conversion-in-loop

Avoid implicit conversions in loops.

```cpp
// BAD - converts size_t to int every iteration
for (int i = 0; i < vec.size(); ++i) { }

// GOOD - matching types
for (size_t i = 0; i < vec.size(); ++i) { }

// BETTER - range-based
for (const auto& item : vec) { }
```

## performance-inefficient-algorithm

Use more efficient algorithm variants.

```cpp
// BAD - find + erase is O(n) + O(n)
auto it = std::find(v.begin(), v.end(), value);
if (it != v.end()) {
    v.erase(it);
}

// GOOD for unordered removal - O(n)
auto it = std::find(v.begin(), v.end(), value);
if (it != v.end()) {
    std::swap(*it, v.back());
    v.pop_back();
}

// For removing all matching elements
v.erase(std::remove(v.begin(), v.end(), value), v.end());
```

## performance-inefficient-string-concatenation

Avoid repeated string concatenation.

```cpp
// BAD - creates temporaries
std::string result = a + b + c + d;

// Also BAD in loops
std::string s;
for (const auto& item : items) {
    s = s + item;  // O(n²)
}

// GOOD - reserve and append
std::string s;
s.reserve(total_size);
for (const auto& item : items) {
    s += item;
}

// Or use stringstream
std::ostringstream oss;
for (const auto& item : items) {
    oss << item;
}
std::string s = oss.str();
```

## performance-inefficient-vector-operation

Reserve vector capacity before filling.

```cpp
// BAD - reallocates as it grows
std::vector<int> v;
for (int i = 0; i < 1000; ++i) {
    v.push_back(i);
}

// GOOD - single allocation
std::vector<int> v;
v.reserve(1000);
for (int i = 0; i < 1000; ++i) {
    v.push_back(i);
}

// BETTER if size known
std::vector<int> v(1000);
for (int i = 0; i < 1000; ++i) {
    v[i] = i;
}
```

## performance-move-const-arg

Don't move const objects.

```cpp
// BAD - const can't be moved, will copy
const std::string s = "hello";
func(std::move(s));  // actually copies

// GOOD
std::string s = "hello";
func(std::move(s));  // actually moves
```

## performance-move-constructor-init

Use std::move in constructor initializers.

```cpp
// BAD - copies parameter
class Foo {
    std::string name_;
public:
    Foo(std::string name) : name_(name) {}  // copies
};

// GOOD - moves parameter
class Foo {
    std::string name_;
public:
    Foo(std::string name) : name_(std::move(name)) {}
};
```

## performance-no-automatic-move

Ensure automatic move isn't prevented.

```cpp
// BAD - const prevents move
std::vector<int> getVector() {
    const std::vector<int> v = compute();
    return v;  // copies because const
}

// GOOD - non-const enables move
std::vector<int> getVector() {
    std::vector<int> v = compute();
    return v;  // moves
}
```

## performance-no-int-to-ptr

Avoid integer to pointer casts.

```cpp
// BAD
void* p = (void*)0x12345678;
int* ip = reinterpret_cast<int*>(addr);

// GOOD - if you really need this
void* p = reinterpret_cast<void*>(static_cast<uintptr_t>(0x12345678));
```

## performance-noexcept-destructor

Destructors should be noexcept.

```cpp
// BAD
class Foo {
    ~Foo() { }  // implicitly noexcept(true), but not explicit
};

// GOOD
class Foo {
    ~Foo() noexcept { }
};

// If destructor might throw (avoid this!)
class Foo {
    ~Foo() noexcept(false) { }  // explicit that it throws
};
```

## performance-noexcept-move-constructor

Move operations should be noexcept.

```cpp
// BAD - prevents optimizations
class Foo {
    Foo(Foo&& other) { }
    Foo& operator=(Foo&& other) { }
};

// GOOD - enables optimizations
class Foo {
    Foo(Foo&& other) noexcept { }
    Foo& operator=(Foo&& other) noexcept { }
};
```

**Why:** std::vector won't use move if it's not noexcept.

## performance-noexcept-swap

Swap should be noexcept.

```cpp
// BAD
void swap(Foo& a, Foo& b) {
    // ...
}

// GOOD
void swap(Foo& a, Foo& b) noexcept {
    // ...
}
```

## performance-trivially-destructible

Use trivially destructible types when possible.

```cpp
// BAD - non-trivial destructor
struct Point {
    int x, y;
    ~Point() { }  // unnecessary, prevents optimizations
};

// GOOD - trivially destructible
struct Point {
    int x, y;
    // no destructor needed
};
```

## performance-type-promotion-in-math-fn

Avoid unnecessary type promotion in math functions.

```cpp
// BAD - float promoted to double
float f = 3.14f;
float result = std::sin(f);  // calls sin(double)

// GOOD - use float overload
float f = 3.14f;
float result = std::sinf(f);  // or std::sin(f) in C++11
```

## performance-unnecessary-copy-initialization

Avoid unnecessary copies when initializing.

```cpp
// BAD - copies the result
const std::string& ref = getString();
auto copy = ref;  // unnecessary copy if only reading

// GOOD - use reference
const auto& copy = getString();

// Or if you need a copy, move from temporary
auto copy = getString();  // moves from temporary
```

## performance-unnecessary-value-param

Pass by const reference instead of value for read-only params.

```cpp
// BAD - copies the string
void process(std::string s) {
    std::cout << s;
}

// GOOD - no copy
void process(const std::string& s) {
    std::cout << s;
}

// Exception: if you need to store/modify, take by value and move
void store(std::string s) {
    member_ = std::move(s);
}
```
