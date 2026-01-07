# C++ Anti-Patterns

Common mistakes and code smells to avoid in C++ code.

## Raw Pointers for Ownership

```cpp
// BAD - Manual memory management
class Container {
    int* data;
public:
    Container() : data(new int[100]) {}
    ~Container() { delete[] data; }  // Easy to forget
};

// GOOD - Smart pointers
class Container {
    std::unique_ptr<int[]> data;
public:
    Container() : data(std::make_unique<int[]>(100)) {}
    // Destructor automatically handles cleanup
};
```

## Not Following Rule of Three/Five/Zero

```cpp
// BAD - Missing copy/move operations
class Resource {
    int* ptr;
public:
    Resource() : ptr(new int(42)) {}
    ~Resource() { delete ptr; }
    // Missing: copy constructor, copy assignment,
    // move constructor, move assignment
};

Resource a;
Resource b = a;  // Double-free bug!

// GOOD - Rule of Zero with smart pointer
class Resource {
    std::unique_ptr<int> ptr;
public:
    Resource() : ptr(std::make_unique<int>(42)) {}
    // Compiler generates correct copy/move operations
};
```

## Using C-Style Arrays

```cpp
// BAD - No bounds checking, size not tracked
int arr[100];
arr[150] = 42;  // Buffer overflow, undefined behavior

// GOOD - std::array or std::vector
std::array<int, 100> arr;
arr.at(150) = 42;  // Throws std::out_of_range

std::vector<int> vec(100);
vec.at(150) = 42;  // Throws std::out_of_range
```

## Returning Reference to Local Variable

```cpp
// BAD - Undefined behavior
std::string& getName() {
    std::string name = "John";
    return name;  // Reference to destroyed object!
}

// GOOD - Return by value (move semantics)
std::string getName() {
    std::string name = "John";
    return name;  // Moved, not copied (RVO)
}
```

## Not Using const Correctness

```cpp
// BAD - Can't call on const objects
class Data {
    int value;
public:
    int getValue() { return value; }  // Non-const
};

void process(const Data& d) {
    d.getValue();  // Error! Can't call non-const method
}

// GOOD - const-correct
class Data {
    int value;
public:
    int getValue() const { return value; }
};
```

## Using new/delete Directly

```cpp
// BAD - Memory leaks if exception thrown
void process() {
    int* data = new int[1000];
    riskyOperation();  // If throws, memory leaked
    delete[] data;
}

// GOOD - RAII with smart pointers
void process() {
    auto data = std::make_unique<int[]>(1000);
    riskyOperation();  // data cleaned up even if throws
}
```

## Catching by Value

```cpp
// BAD - Slicing and unnecessary copy
try {
    throw DerivedError("message");
} catch (BaseError e) {  // Sliced to BaseError!
    // ...
}

// GOOD - Catch by reference
try {
    throw DerivedError("message");
} catch (const BaseError& e) {
    // Polymorphism preserved
}
```

## Using NULL Instead of nullptr

```cpp
// BAD - NULL is just 0, ambiguous
void func(int);
void func(int*);
func(NULL);  // Calls func(int), not func(int*)!

// GOOD - nullptr is type-safe
func(nullptr);  // Calls func(int*)
```

## Virtual Destructor Missing

```cpp
// BAD - Undefined behavior on delete
class Base {
public:
    ~Base() { }  // Non-virtual
};

class Derived : public Base {
    int* data;
public:
    ~Derived() { delete data; }
};

Base* ptr = new Derived();
delete ptr;  // Only Base destructor called! Memory leak

// GOOD - Virtual destructor
class Base {
public:
    virtual ~Base() = default;
};
```

## Using std::endl Instead of '\n'

```cpp
// BAD - Flushes buffer each time (slow)
for (int i = 0; i < 1000; i++) {
    std::cout << i << std::endl;  // 1000 flushes
}

// GOOD - Use '\n', flush when needed
for (int i = 0; i < 1000; i++) {
    std::cout << i << '\n';
}
std::cout << std::flush;  // One flush at end
```

## String Comparison with ==

```cpp
// BAD (C-style strings) - Compares pointers!
const char* a = "hello";
const char* b = "hello";
if (a == b) { }  // Compares addresses, not content

// GOOD for C-style - Use strcmp
if (strcmp(a, b) == 0) { }

// BETTER - Use std::string
std::string a = "hello";
std::string b = "hello";
if (a == b) { }  // Works correctly
```

## Implicit Conversions

```cpp
// BAD - Implicit conversion surprises
class FilePath {
public:
    FilePath(const std::string& path) { }  // Implicit
};

void process(const FilePath& path);
process("file.txt");  // Implicit conversion

// GOOD - Explicit constructors
class FilePath {
public:
    explicit FilePath(const std::string& path) { }
};

process("file.txt");  // Error!
process(FilePath("file.txt"));  // OK - explicit
```

## Not Using override Keyword

```cpp
// BAD - Silent bug if signature doesn't match
class Base {
public:
    virtual void process(int x) { }
};

class Derived : public Base {
public:
    void process(int x) const { }  // Oops! New method, not override
};

// GOOD - Compiler catches mismatch
class Derived : public Base {
public:
    void process(int x) const override { }  // Error! Signature mismatch
};
```

## Using Magic Numbers

```cpp
// BAD - What does 86400 mean?
sleep(86400);

// GOOD - Named constants
constexpr int SECONDS_PER_DAY = 86400;
sleep(SECONDS_PER_DAY);

// OR use chrono
using namespace std::chrono_literals;
std::this_thread::sleep_for(24h);
```

## Including Entire Namespace

```cpp
// BAD - Namespace pollution
using namespace std;
// Now count could be std::count or your count

// GOOD - Specific using declarations
using std::string;
using std::vector;

// OR use qualified names
std::vector<std::string> items;
```
