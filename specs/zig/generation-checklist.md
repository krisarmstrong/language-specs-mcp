# Zig Generation Checklist

**Read this BEFORE writing Zig code. Safety and explicit behavior are core values.**

## Critical: You Must Do These

### 1. Handle All Errors Explicitly
```zig
// BAD - ignoring error
const file = std.fs.cwd().openFile("data.txt", .{}) catch unreachable;

// GOOD - handle error explicitly
const file = std.fs.cwd().openFile("data.txt", .{}) catch |err| {
    std.debug.print("Failed to open file: {}\n", .{err});
    return err;
};
defer file.close();

// GOOD - propagate with try
const file = try std.fs.cwd().openFile("data.txt", .{});

// GOOD - with error union return type
fn readConfig() !Config {
    const file = try std.fs.cwd().openFile("config.txt", .{});
    defer file.close();
    // ...
}
```

### 2. Use `defer` for Cleanup
```zig
// BAD - might forget to clean up
fn process() !void {
    const allocator = std.heap.page_allocator;
    const buffer = try allocator.alloc(u8, 1024);

    if (condition) return;  // Memory leak!

    allocator.free(buffer);
}

// GOOD - defer ensures cleanup
fn process() !void {
    const allocator = std.heap.page_allocator;
    const buffer = try allocator.alloc(u8, 1024);
    defer allocator.free(buffer);

    if (condition) return;  // Still freed!
    // ... use buffer ...
}
```

### 3. Use Proper Allocators
```zig
// BAD - using page allocator for small allocations
const allocator = std.heap.page_allocator;
const small = try allocator.alloc(u8, 16);  // Wasteful!

// GOOD - choose appropriate allocator
// For general purpose:
var gpa = std.heap.GeneralPurposeAllocator(.{}){};
defer _ = gpa.deinit();
const allocator = gpa.allocator();

// For arena (bulk allocation, single free):
var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
defer arena.deinit();
const allocator = arena.allocator();

// Accept allocator as parameter for flexibility
fn createBuffer(allocator: std.mem.Allocator, size: usize) ![]u8 {
    return try allocator.alloc(u8, size);
}
```

### 4. Initialize All Variables
```zig
// BAD - undefined value
var x: i32 = undefined;
if (condition) x = 5;
std.debug.print("{}", .{x});  // Undefined behavior if !condition

// GOOD - initialize or use optional
var x: i32 = 0;
if (condition) x = 5;

// GOOD - use optional for "maybe has value"
var x: ?i32 = null;
if (condition) x = 5;
if (x) |value| {
    std.debug.print("{}", .{value});
}
```

### 5. Check Slice Bounds
```zig
// BAD - trusting index
fn getItem(items: []const Item, index: usize) Item {
    return items[index];  // Panics if out of bounds!
}

// GOOD - return optional or error
fn getItem(items: []const Item, index: usize) ?Item {
    if (index >= items.len) return null;
    return items[index];
}

// GOOD - use slice range safely
fn getSlice(data: []const u8, start: usize, end: usize) ?[]const u8 {
    if (start > end or end > data.len) return null;
    return data[start..end];
}
```

## Important: Strong Recommendations

### 6. Prefer Slices Over Pointers
```zig
// BAD - raw pointer loses length info
fn process(ptr: [*]u8, len: usize) void { ... }

// GOOD - slice includes length
fn process(data: []u8) void { ... }

// GOOD - const slice for read-only
fn analyze(data: []const u8) void { ... }
```

### 7. Use Comptime for Zero-Cost Abstractions
```zig
// GOOD - compile-time evaluation
fn multiplyMatrices(comptime N: usize, a: [N][N]f32, b: [N][N]f32) [N][N]f32 {
    var result: [N][N]f32 = undefined;
    inline for (0..N) |i| {
        inline for (0..N) |j| {
            var sum: f32 = 0;
            inline for (0..N) |k| {
                sum += a[i][k] * b[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}

// GOOD - comptime string formatting
const message = std.fmt.comptimePrint("Version {}.{}", .{ 1, 0 });
```

### 8. Use Enums and Tagged Unions
```zig
// GOOD - enum for fixed set of values
const Status = enum {
    pending,
    active,
    completed,
    failed,
};

// GOOD - tagged union for variants with data
const Result = union(enum) {
    success: Data,
    err: Error,
    pending: void,
};

fn process(result: Result) void {
    switch (result) {
        .success => |data| handleSuccess(data),
        .err => |e| handleError(e),
        .pending => {},
    }
}
```

### 9. Use `std.ArrayList` for Dynamic Arrays
```zig
// GOOD - ArrayList for growing collections
var list = std.ArrayList(Item).init(allocator);
defer list.deinit();

try list.append(item1);
try list.append(item2);

for (list.items) |item| {
    processItem(item);
}
```

### 10. Prefer `orelse` for Optionals
```zig
// GOOD - orelse for default values
const value = maybe_value orelse default_value;

// GOOD - orelse with block for complex fallback
const config = loadConfig() orelse {
    std.debug.print("Using default config\n", .{});
    return defaultConfig();
};

// GOOD - .? for unwrap when you're sure (use sparingly)
const definitely_has_value = optional.?;
```

## Testing

### 11. Write Tests in the Same File
```zig
fn add(a: i32, b: i32) i32 {
    return a + b;
}

// Tests are part of the module
test "add positive numbers" {
    try std.testing.expectEqual(@as(i32, 5), add(2, 3));
}

test "add negative numbers" {
    try std.testing.expectEqual(@as(i32, -5), add(-2, -3));
}

test "add mixed" {
    try std.testing.expectEqual(@as(i32, 1), add(-2, 3));
}

// Run with: zig build test
```

### 12. Use Testing Allocator
```zig
test "no memory leaks" {
    var allocator = std.testing.allocator;

    const buffer = try allocator.alloc(u8, 100);
    defer allocator.free(buffer);

    // Test code...
    // Testing allocator will fail if any memory is not freed
}
```

## Safety and Performance

### 13. Use `@intCast` Carefully
```zig
// BAD - assuming value fits
const small: u8 = @intCast(big_value);  // Undefined behavior if > 255!

// GOOD - check first or use saturating/wrapping
const small: u8 = std.math.cast(u8, big_value) orelse {
    return error.ValueTooLarge;
};

// Or use saturating cast
const small: u8 = @truncate(@min(big_value, 255));
```

### 14. Prefer Explicit Over Implicit
```zig
// Zig philosophy: be explicit

// Explicit error handling
const result = try riskyOperation();

// Explicit null handling
if (optional) |value| { ... }

// Explicit type conversion
const float: f32 = @floatFromInt(integer);

// Explicit overflow behavior
const sum = @addWithOverflow(a, b);
if (sum[1] != 0) return error.Overflow;
```

### 15. Use `packed struct` Sparingly
```zig
// Regular struct - better alignment, faster access
const Normal = struct {
    a: u8,
    b: u32,
    c: u8,
};  // Size: 12 bytes (with padding)

// Packed struct - exact layout, may be slower
const Packed = packed struct {
    a: u8,
    b: u32,
    c: u8,
};  // Size: 6 bytes (no padding)

// Use packed only when you need:
// - Exact memory layout for FFI
// - Bit-level field access
// - Memory-mapped I/O
```

---

**Quick Reference - Copy This Mental Model:**
- Handle all errors with `try` or `catch`
- `defer` for cleanup
- Choose appropriate allocator
- Initialize all variables (no `undefined` leaking)
- Check slice bounds
- Slices over raw pointers
- Comptime for zero-cost abstractions
- Tagged unions for variants
- `ArrayList` for dynamic arrays
- `orelse` for optional defaults
- Tests in the same file
- Testing allocator catches leaks
- Explicit type conversions
- Check overflow explicitly
