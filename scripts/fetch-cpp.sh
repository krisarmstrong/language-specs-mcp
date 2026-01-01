#!/bin/bash
# Fetch C++ specs from authoritative sources

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$SCRIPT_DIR/../specs/cpp"

echo "=== Fetching C++ Specs ==="

mkdir -p "$SPECS_DIR"/{stdlib/headers,patterns,formatters,linters/{clang-tidy,cppcheck}}

# C++ standard reference (cppreference is authoritative community resource)
echo "Note: ISO C++ spec is copyrighted. Using cppreference as authoritative source."

# Core C++ patterns
cat > "$SPECS_DIR/patterns/idioms.md" << 'EOF'
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
EOF

# clang-tidy checks
echo "Fetching clang-tidy checks..."
curl -sL "https://clang.llvm.org/extra/clang-tidy/checks/list.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/clang-tidy/overview.md" 2>/dev/null || \
  echo "# clang-tidy Checks\n\nSee: https://clang.llvm.org/extra/clang-tidy/checks/list.html" > "$SPECS_DIR/linters/clang-tidy/overview.md"

CLANG_TIDY_CHECKS=$(curl -sL "https://clang.llvm.org/extra/clang-tidy/checks/list.html" | \
  grep -oE 'checks/[a-zA-Z0-9_-]+\\.html' | \
  sed 's#.*/##;s/\\.html$//' | sort -u)

for check in $CLANG_TIDY_CHECKS; do
  echo "  - clang-tidy/$check"
  curl -sL "https://clang.llvm.org/extra/clang-tidy/checks/${check}.html" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/linters/clang-tidy/${check}.md" 2>/dev/null || \
    echo "# ${check}\n\nSee: https://clang.llvm.org/extra/clang-tidy/checks/${check}.html" > "$SPECS_DIR/linters/clang-tidy/${check}.md"
done

# cppcheck checks
curl -sL "https://cppcheck.sourceforge.io/manual.html" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/linters/cppcheck/overview.md" 2>/dev/null || \
  echo "# cppcheck Manual\n\nSee: https://cppcheck.sourceforge.io/manual.html" > "$SPECS_DIR/linters/cppcheck/overview.md"

# C++ formatters
cat > "$SPECS_DIR/formatters/overview.md" << 'EOF'
# C++ Formatters

## clang-format

See: https://clang.llvm.org/docs/ClangFormat.html
EOF

echo "Fetching C++ standard library headers..."
curl -sL "https://en.cppreference.com/w/cpp/header" | \
  sed -n '/<main/,/<\/main>/p' | \
  pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/headers/index.md" 2>/dev/null || \
  echo "# C++ Standard Library Headers\n\nSee: https://en.cppreference.com/w/cpp/header" > "$SPECS_DIR/stdlib/headers/index.md"

CPP_HEADERS=$(curl -sL "https://en.cppreference.com/w/cpp/header" | \
  grep -oE '/w/cpp/header/[a-zA-Z0-9_.]+' | \
  sed 's#.*/##' | sort -u)

for hdr in $CPP_HEADERS; do
  echo "  - cpp/$hdr"
  curl -sL "https://en.cppreference.com/w/cpp/header/${hdr}" | \
    sed -n '/<main/,/<\/main>/p' | \
    pandoc -f html -t markdown -o "$SPECS_DIR/stdlib/headers/${hdr}.md" 2>/dev/null || \
    echo "# ${hdr}\n\nSee: https://en.cppreference.com/w/cpp/header/${hdr}" > "$SPECS_DIR/stdlib/headers/${hdr}.md"
done

cat > "$SPECS_DIR/formatters/clang-format.md" << 'EOF'
# clang-format Options

See: https://clang.llvm.org/docs/ClangFormatStyleOptions.html
EOF

# Standard library overview
cat > "$SPECS_DIR/stdlib/overview.md" << 'EOF'
# Modern C++ Standard Library

## Core Headers

| Header | Purpose |
|--------|---------|
| `<memory>` | Smart pointers |
| `<string>` | String class |
| `<string_view>` | Non-owning string reference |
| `<vector>` | Dynamic array |
| `<array>` | Fixed-size array |
| `<map>` / `<unordered_map>` | Associative containers |
| `<optional>` | Nullable values |
| `<variant>` | Type-safe union |
| `<expected>` | Result type (C++23) |
| `<span>` | Non-owning view |
| `<ranges>` | Range algorithms |
| `<format>` | Type-safe formatting |
| `<filesystem>` | File operations |
| `<thread>` | Threading |
| `<mutex>` | Synchronization |
| `<chrono>` | Time utilities |

## Smart Pointers

```cpp
#include <memory>

// Unique ownership
std::unique_ptr<T> ptr = std::make_unique<T>(args...);

// Shared ownership
std::shared_ptr<T> ptr = std::make_shared<T>(args...);

// Non-owning observer
std::weak_ptr<T> weak = shared;
```

## Containers

```cpp
std::vector<T> vec;           // Dynamic array
std::array<T, N> arr;         // Fixed array
std::map<K, V> map;           // Ordered map
std::unordered_map<K, V> um;  // Hash map
std::set<T> set;              // Ordered set
std::deque<T> dq;             // Double-ended queue
```

## Algorithms

```cpp
#include <algorithm>
#include <ranges>

// Classic
std::sort(vec.begin(), vec.end());
auto it = std::find(vec.begin(), vec.end(), value);

// Ranges (C++20)
std::ranges::sort(vec);
auto it = std::ranges::find(vec, value);

// Projections
std::ranges::sort(people, {}, &Person::name);
```
EOF

echo "=== C++ specs complete ==="
