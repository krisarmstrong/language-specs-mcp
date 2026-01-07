# C++ Generation Checklist

**Read this BEFORE writing C++ code. Modern C++ is memory-safe when used correctly.**

## Critical: You Must Do These

### 1. Use Smart Pointers, Not Raw `new`/`delete`
```cpp
// BAD - manual memory management
Widget* w = new Widget();
// ... forget to delete = leak
delete w;

// GOOD - automatic cleanup
auto w = std::make_unique<Widget>();
// or for shared ownership
auto w = std::make_shared<Widget>();
```

### 2. Use RAII for All Resources
```cpp
// BAD - manual resource management
void process() {
    FILE* f = fopen("data.txt", "r");
    if (error) return;  // Leak!
    fclose(f);
}

// GOOD - RAII wrapper
void process() {
    std::ifstream file("data.txt");
    if (error) return;  // Automatic cleanup
}
```

### 3. Prefer `std::string` Over C Strings
```cpp
// BAD - manual buffer management
char buf[256];
strcpy(buf, str);

// GOOD - automatic management
std::string s = str;
```

### 4. Use `nullptr` Not `NULL` or `0`
```cpp
// BAD - ambiguous
Widget* w = NULL;
Widget* w = 0;

// GOOD - type-safe
Widget* w = nullptr;
```

### 5. Initialize All Members in Constructors
```cpp
// BAD - uninitialized members
class Widget {
    int count;
    std::string name;
public:
    Widget() { }  // count is garbage!
};

// GOOD - member initializer list
class Widget {
    int count;
    std::string name;
public:
    Widget() : count(0), name() { }
};

// BETTER - default member initializers (C++11)
class Widget {
    int count = 0;
    std::string name;
};
```

## Important: Strong Recommendations

### 6. Use `const` Extensively
```cpp
// GOOD - const correctness
class Widget {
public:
    int getValue() const { return value; }  // const method
    void process(const std::string& s);     // const ref param
};
```

### 7. Pass by `const&` for Read-Only Objects
```cpp
// BAD - unnecessary copy
void process(std::string s);
void process(std::vector<int> v);

// GOOD - no copy
void process(const std::string& s);
void process(const std::vector<int>& v);
```

### 8. Use Range-Based For Loops
```cpp
// BAD - index-based
for (size_t i = 0; i < vec.size(); ++i) {
    process(vec[i]);
}

// GOOD - range-based
for (const auto& item : vec) {
    process(item);
}
```

### 9. Use `auto` for Complex Types
```cpp
// BAD - verbose, error-prone
std::map<std::string, std::vector<int>>::iterator it = map.begin();

// GOOD - cleaner
auto it = map.begin();
```

### 10. Prefer `std::array` Over C Arrays
```cpp
// BAD - decays to pointer, no size info
int arr[10];

// GOOD - knows its size, safer
std::array<int, 10> arr;
```

## Modern C++ (11/14/17/20)

### 11. Use `override` for Virtual Functions
```cpp
class Derived : public Base {
    // BAD - silent bug if signature doesn't match
    void process();

    // GOOD - compiler error if not overriding
    void process() override;
};
```

### 12. Use `= default` and `= delete`
```cpp
class Widget {
public:
    Widget() = default;                          // Use compiler default
    Widget(const Widget&) = delete;              // Prevent copying
    Widget& operator=(const Widget&) = delete;   // Prevent assignment
};
```

### 13. Use `std::optional` for Maybe-Values (C++17)
```cpp
// BAD - sentinel values or out params
int find(const std::vector<int>& v, int target);  // Returns -1 if not found?

// GOOD - explicit optionality
std::optional<int> find(const std::vector<int>& v, int target);
```

### 14. Use Structured Bindings (C++17)
```cpp
// BAD - verbose
std::pair<int, std::string> p = getPair();
int id = p.first;
std::string name = p.second;

// GOOD - clean
auto [id, name] = getPair();
```

### 15. Use `std::string_view` for Read-Only Strings (C++17)
```cpp
// BAD - forces allocation for string literals
void process(const std::string& s);

// GOOD - no allocation, works with string, char*, string_view
void process(std::string_view s);
```

## Concurrency

### 16. Use `std::mutex` with `std::lock_guard`
```cpp
// BAD - manual lock/unlock
mutex.lock();
// ... exception here = deadlock
mutex.unlock();

// GOOD - RAII locking
{
    std::lock_guard<std::mutex> lock(mutex);
    // Automatically unlocked on scope exit
}
```

### 17. Prefer `std::atomic` for Simple Shared State
```cpp
// BAD - data race
bool running = true;

// GOOD - atomic operations
std::atomic<bool> running{true};
```

---

**Quick Reference - Copy This Mental Model:**
- Smart pointers (unique_ptr, shared_ptr)
- RAII for all resources
- std::string not char[]
- nullptr not NULL
- Initialize all members
- const& for read-only params
- Range-based for loops
- auto for complex types
- override on virtual methods
- std::optional for maybe-values
- lock_guard for mutexes
