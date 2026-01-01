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
