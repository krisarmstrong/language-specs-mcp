# Modern C++ Idiomatic Patterns (C++17/20/23)

## Memory Management

### Use smart pointers, not raw new/delete

```cpp
// BAD
Widget* w = new Widget();
// ... forget to delete

// GOOD
auto w = std::make_unique<Widget>();
// automatically deleted

// Shared ownership
auto shared = std::make_shared<Widget>();
```

### Rule of Zero/Five

```cpp
// Rule of Zero: Use RAII wrappers, no manual resource management
class Good {
    std::string name;
    std::vector<int> data;
    // No destructor, copy/move ops needed
};

// Rule of Five: If you define one, define all
class Manual {
    int* data;
public:
    ~Manual();
    Manual(const Manual&);
    Manual& operator=(const Manual&);
    Manual(Manual&&) noexcept;
    Manual& operator=(Manual&&) noexcept;
};
```

## Use auto (but not everywhere)

```cpp
// GOOD - obvious type
auto it = container.begin();
auto ptr = std::make_unique<Widget>();

// GOOD - complex type
auto lambda = [](int x) { return x * 2; };

// BAD - hides important type info
auto config = getConfig();  // What type is this?

// BETTER
Config config = getConfig();
```

## Range-based for

```cpp
// BAD
for (size_t i = 0; i < vec.size(); ++i) {
    process(vec[i]);
}

// GOOD
for (const auto& item : vec) {
    process(item);
}

// Modify in place
for (auto& item : vec) {
    item.update();
}
```

## Use constexpr

```cpp
// Compile-time computation
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

constexpr int fact5 = factorial(5);  // computed at compile time
```

## std::optional for nullable values

```cpp
// BAD
Widget* find(int id);  // nullptr if not found

// GOOD
std::optional<Widget> find(int id);

// Usage
if (auto w = find(42)) {
    w->doSomething();
}
```

## std::variant for type-safe unions

```cpp
using Result = std::variant<Success, Error>;

Result doSomething() {
    if (failed) {
        return Error{"something went wrong"};
    }
    return Success{data};
}

// Visit pattern
std::visit([](auto&& arg) {
    using T = std::decay_t<decltype(arg)>;
    if constexpr (std::is_same_v<T, Success>) {
        handle(arg.data);
    } else {
        log(arg.message);
    }
}, result);
```

## Structured bindings

```cpp
std::map<std::string, int> map;

// BAD
for (const auto& pair : map) {
    std::cout << pair.first << ": " << pair.second;
}

// GOOD
for (const auto& [key, value] : map) {
    std::cout << key << ": " << value;
}
```

## Use [[nodiscard]]

```cpp
[[nodiscard]] Error doSomething();

doSomething();  // Warning: ignoring return value
```

## String views

```cpp
// BAD - unnecessary copy
void process(const std::string& s);

// GOOD - no copy for literals or string views
void process(std::string_view s);
```

## Concepts (C++20)

```cpp
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template<Numeric T>
T add(T a, T b) {
    return a + b;
}
```
