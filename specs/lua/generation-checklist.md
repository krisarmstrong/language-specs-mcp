# Lua Generation Checklist

**Read this BEFORE writing Lua code. Understand tables—they're everything in Lua.**

## Critical: You Must Do These

### 1. Use `local` for All Variables
```lua
-- BAD - global by default (pollutes global namespace)
count = 0
function process()
    temp = count + 1  -- Also global!
    return temp
end

-- GOOD - explicit local
local count = 0
local function process()
    local temp = count + 1
    return temp
end
```

### 2. Check for nil Before Using Values
```lua
-- BAD - crashes on nil
local function get_name(user)
    return user.name:upper()  -- Errors if user or name is nil
end

-- GOOD - nil checks
local function get_name(user)
    if user and user.name then
        return user.name:upper()
    end
    return "Unknown"
end

-- GOOD - default values pattern
local function get_name(user)
    local name = user and user.name or "Unknown"
    return name:upper()
end
```

### 3. Use `ipairs` for Arrays, `pairs` for Tables
```lua
-- For array-like tables (integer keys 1, 2, 3...)
local items = {"apple", "banana", "cherry"}
for i, item in ipairs(items) do
    print(i, item)
end

-- For hash-like tables or mixed tables
local config = {name = "App", version = "1.0", debug = true}
for key, value in pairs(config) do
    print(key, value)
end

-- NOTE: ipairs stops at first nil, pairs doesn't guarantee order
```

### 4. Initialize Tables Properly
```lua
-- Array-like table
local list = {}
table.insert(list, "item1")
table.insert(list, "item2")

-- Or with literal
local list = {"item1", "item2", "item3"}

-- Hash-like table
local user = {
    name = "Alice",
    age = 30,
    active = true
}

-- Mixed (avoid if possible)
local mixed = {
    "first",           -- [1]
    "second",          -- [2]
    name = "config",   -- named key
}
```

### 5. Close File Handles
```lua
-- BAD - resource leak
local file = io.open("data.txt", "r")
local content = file:read("*all")
-- forgot to close!

-- GOOD - always close
local file = io.open("data.txt", "r")
if file then
    local content = file:read("*all")
    file:close()
end

-- GOOD - protected call pattern
local function read_file(path)
    local file, err = io.open(path, "r")
    if not file then
        return nil, err
    end
    local content = file:read("*all")
    file:close()
    return content
end
```

## Important: Strong Recommendations

### 6. Use Proper Error Handling
```lua
-- BAD - errors crash the program
local result = risky_function()

-- GOOD - pcall for protected call
local ok, result = pcall(risky_function)
if ok then
    print("Success:", result)
else
    print("Error:", result)
end

-- GOOD - xpcall with error handler
local function error_handler(err)
    print(debug.traceback("Error: " .. tostring(err)))
end

local ok, result = xpcall(risky_function, error_handler)
```

### 7. Use Metatables for OOP Patterns
```lua
-- GOOD - class-like pattern
local User = {}
User.__index = User

function User.new(name, email)
    local self = setmetatable({}, User)
    self.name = name
    self.email = email
    return self
end

function User:greet()
    return "Hello, " .. self.name
end

-- Usage
local user = User.new("Alice", "alice@test.com")
print(user:greet())  -- Note: colon syntax passes self
```

### 8. Use Colon Syntax for Methods
```lua
-- Colon automatically passes self
function User:greet()  -- Equivalent to User.greet(self)
    return "Hello, " .. self.name
end

-- Call with colon
user:greet()  -- Equivalent to user.greet(user)

-- Common mistake: mixing dot and colon
user.greet()  -- ERROR: self is nil!
User.greet(user)  -- OK, explicit self
```

### 9. Use String Methods Correctly
```lua
-- String methods use colon syntax
local s = "hello world"
print(s:upper())         -- HELLO WORLD
print(s:sub(1, 5))       -- hello
print(s:find("world"))   -- 7

-- Or with string library
print(string.upper(s))
print(string.sub(s, 1, 5))

-- Pattern matching (Lua's regex)
local word = s:match("(%w+)")  -- "hello"
for word in s:gmatch("%w+") do
    print(word)
end
```

### 10. Cache Global Functions for Performance
```lua
-- BAD in tight loops - global lookup each iteration
for i = 1, 1000000 do
    math.sin(i)  -- Looks up math.sin each time
end

-- GOOD - cache locally
local sin = math.sin
for i = 1, 1000000 do
    sin(i)  -- Direct local access
end

-- Common to cache at module top
local pairs = pairs
local ipairs = ipairs
local type = type
local tostring = tostring
```

## Tables Deep Dive

### 11. Understand Table Reference Semantics
```lua
-- Tables are passed by reference
local original = {1, 2, 3}
local reference = original
reference[1] = 999
print(original[1])  -- 999 (modified!)

-- GOOD - shallow copy
local function shallow_copy(t)
    local copy = {}
    for k, v in pairs(t) do
        copy[k] = v
    end
    return copy
end

local copy = shallow_copy(original)
copy[1] = 1  -- original unchanged
```

### 12. Use # Carefully for Length
```lua
-- # only works reliably for arrays without holes
local arr = {1, 2, 3}
print(#arr)  -- 3

-- With holes, behavior is undefined!
local sparse = {[1] = "a", [3] = "c"}
print(#sparse)  -- Could be 1 or 3!

-- GOOD - count explicitly for sparse tables
local function count_keys(t)
    local count = 0
    for _ in pairs(t) do
        count = count + 1
    end
    return count
end
```

### 13. Use Weak Tables for Caches
```lua
-- GOOD - weak values for cache (allows garbage collection)
local cache = setmetatable({}, {__mode = "v"})

function get_expensive(key)
    if cache[key] then
        return cache[key]
    end
    local result = expensive_computation(key)
    cache[key] = result
    return result
end
```

## Modules

### 14. Use Proper Module Pattern
```lua
-- mymodule.lua
local M = {}

-- Private
local function helper()
    return "helped"
end

-- Public
function M.public_function()
    return helper() .. " publicly"
end

return M

-- Usage
local mymodule = require("mymodule")
mymodule.public_function()
```

### 15. Avoid require in Loops
```lua
-- BAD - require called repeatedly
for i = 1, 100 do
    local json = require("json")
    json.decode(data[i])
end

-- GOOD - require once at top
local json = require("json")
for i = 1, 100 do
    json.decode(data[i])
end
```

---

**Quick Reference - Copy This Mental Model:**
- `local` for all variables
- Check for nil before using
- `ipairs` for arrays, `pairs` for tables
- Always close file handles
- `pcall`/`xpcall` for error handling
- Metatables for OOP patterns
- Colon syntax for methods (`:`)
- Cache globals for hot paths
- Tables are references (copy if needed)
- `#` only reliable for dense arrays
- Weak tables for caches
- Proper module pattern with `return M`
