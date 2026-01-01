# clang-tidy cert-* Checks

CERT Secure Coding Standards for C and C++.

## cert-dcl03-c / cert-dcl16-c

Use appropriate literal suffixes.

```cpp
// BAD
long x = 42l;  // lowercase L looks like 1
unsigned u = 42u;

// GOOD
long x = 42L;
unsigned u = 42U;
long long ll = 42LL;
unsigned long long ull = 42ULL;
```

## cert-dcl21-cpp

Postfix operator++ should return const.

```cpp
// BAD - allows (i++)++ which is undefined
Iterator operator++(int) {
    Iterator tmp = *this;
    ++*this;
    return tmp;
}

// GOOD
const Iterator operator++(int) {
    Iterator tmp = *this;
    ++*this;
    return tmp;
}
```

## cert-dcl50-cpp

Don't define C-style variadic functions.

```cpp
// BAD
void log(const char* fmt, ...) {
    va_list args;
    // ...
}

// GOOD - use variadic templates
template<typename... Args>
void log(const char* fmt, Args&&... args);
```

## cert-dcl58-cpp

Don't modify std namespace.

```cpp
// BAD
namespace std {
    template<>
    struct hash<MyType> { };  // UB in most cases
}

// GOOD - specialize in your namespace or use ADL
// For hash, this is actually allowed as an exception
```

## cert-env33-c

Don't call system().

```cpp
// BAD - command injection risk
system(userInput);
system("rm -rf " + path);

// GOOD - use exec family or specific APIs
execl("/bin/rm", "rm", path.c_str(), nullptr);

// Or use std::filesystem
std::filesystem::remove(path);
```

## cert-err33-c

Check return values for errors.

```cpp
// BAD
fopen(path, "r");  // return not checked
malloc(size);      // return not checked
fclose(file);      // return not checked

// GOOD
FILE* f = fopen(path, "r");
if (f == nullptr) {
    // handle error
}

void* p = malloc(size);
if (p == nullptr) {
    // handle error
}

if (fclose(file) != 0) {
    // handle error
}
```

## cert-err34-c

Check scanf return values.

```cpp
// BAD
scanf("%d", &x);

// GOOD
if (scanf("%d", &x) != 1) {
    // handle parse error
}
```

## cert-err52-cpp

Don't use setjmp/longjmp in C++.

```cpp
// BAD - doesn't call destructors
jmp_buf env;
if (setjmp(env) == 0) {
    // ...
    longjmp(env, 1);  // skips destructors!
}

// GOOD - use exceptions
try {
    // ...
    throw std::runtime_error("error");
} catch (const std::exception& e) {
    // handle
}
```

## cert-err58-cpp

Handle exceptions from static initializers.

```cpp
// BAD - exception terminates program
static std::vector<int> v = riskyInit();  // might throw

// GOOD - wrap in function
static std::vector<int>& getV() {
    static std::vector<int> v = []() {
        try {
            return riskyInit();
        } catch (...) {
            return std::vector<int>{};
        }
    }();
    return v;
}
```

## cert-err60-cpp

Exception objects must be nothrow copy constructible.

```cpp
// BAD
class MyException : public std::exception {
    std::string msg;  // copy might throw
public:
    MyException(std::string m) : msg(std::move(m)) {}
};

// GOOD - use shared_ptr for complex data
class MyException : public std::exception {
    std::shared_ptr<std::string> msg;  // copy is noexcept
public:
    MyException(std::string m) 
        : msg(std::make_shared<std::string>(std::move(m))) {}
};
```

## cert-fio38-c

Don't copy FILE objects.

```cpp
// BAD
FILE f1 = *fopen("file", "r");  // undefined behavior
FILE f2 = f1;                    // undefined behavior

// GOOD
FILE* f1 = fopen("file", "r");
// use f1 pointer, don't copy
```

## cert-flp30-c

Don't use floating-point for loop counters.

```cpp
// BAD - accumulating error
for (float f = 0.0f; f < 1.0f; f += 0.1f) {
    // f may never exactly equal 1.0
}

// GOOD
for (int i = 0; i < 10; ++i) {
    float f = i * 0.1f;
}
```

## cert-mem57-cpp

Provide aligned new for over-aligned types.

```cpp
// BAD - over-aligned without operator new
struct alignas(64) CacheLine {
    char data[64];
};
auto p = new CacheLine;  // may not be aligned in C++14

// GOOD - C++17 aligned allocation
auto p = new CacheLine;  // C++17 handles it

// Or provide aligned new (pre-C++17)
struct alignas(64) CacheLine {
    char data[64];
    void* operator new(size_t size) {
        return aligned_alloc(64, size);
    }
    void operator delete(void* p) {
        free(p);
    }
};
```

## cert-msc30-c / cert-msc50-cpp

Don't use rand() for security.

```cpp
// BAD - predictable
int token = rand();
srand(time(nullptr));

// GOOD - use <random>
std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<> dis(1, 100);
int token = dis(gen);

// For security-critical (tokens, keys)
#include <openssl/rand.h>
unsigned char token[32];
RAND_bytes(token, sizeof(token));
```

## cert-msc32-c / cert-msc51-cpp

Properly seed random number generators.

```cpp
// BAD - predictable seed
srand(time(nullptr));  // time is predictable
std::mt19937 gen(42);  // constant seed

// GOOD
std::random_device rd;
std::mt19937 gen(rd());

// For reproducible tests, document the seed
std::mt19937 gen(KNOWN_SEED);  // for testing only
```

## cert-oop11-cpp

Don't return rvalue reference.

```cpp
// BAD
std::string&& getName() {
    return std::move(name_);  // dangling reference!
}

// GOOD
std::string getName() {
    return name_;  // copy
}

std::string getName() && {
    return std::move(name_);  // move from expiring object
}
```

## cert-oop54-cpp

Gracefully handle self-assignment.

```cpp
// BAD
Foo& operator=(const Foo& other) {
    delete ptr;
    ptr = new int(*other.ptr);  // crash if this == &other
    return *this;
}

// GOOD - check for self-assignment
Foo& operator=(const Foo& other) {
    if (this != &other) {
        delete ptr;
        ptr = new int(*other.ptr);
    }
    return *this;
}

// BETTER - copy and swap
Foo& operator=(Foo other) {  // by value
    swap(*this, other);
    return *this;
}
```

## cert-oop57-cpp

Prefer special member functions over memcpy/memmove.

```cpp
// BAD - may not work for non-trivial types
Foo a, b;
memcpy(&a, &b, sizeof(Foo));  // UB if Foo is non-trivial

// GOOD
Foo a, b;
a = b;  // uses copy assignment
```

## cert-oop58-cpp

Copy operations should provide strong exception safety.

```cpp
// BAD - not exception safe
Foo& operator=(const Foo& other) {
    delete ptr;  // point of no return
    ptr = new int(*other.ptr);  // if this throws, object is invalid
    return *this;
}

// GOOD - copy and swap (strong guarantee)
Foo& operator=(const Foo& other) {
    Foo tmp(other);  // if this throws, *this unchanged
    swap(*this, tmp);
    return *this;
}
```

## cert-pos44-c

Don't use signals for thread sync.

```cpp
// BAD - data race
volatile sig_atomic_t flag = 0;

void handler(int) {
    flag = 1;
}

void thread() {
    while (!flag) { }  // spin on flag
}

// GOOD - use atomics or mutexes
std::atomic<bool> flag{false};

void thread() {
    while (!flag.load()) { }
}
```

## cert-str34-c

Cast characters to unsigned before widening.

```cpp
// BAD - sign extension
char c = getchar();
int i = c;  // if c is negative, i is negative

// GOOD
char c = getchar();
int i = static_cast<unsigned char>(c);

// Or use unsigned char from start
unsigned char c = getchar();
```
