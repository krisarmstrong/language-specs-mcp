# Clippy Suspicious Lints

Lints that detect very suspicious code patterns.

## almost_complete_range

Almost complete range.

```rust
// BAD
'a'..'z'  // missing 'z'!
'A'..'Z'

// GOOD
'a'..='z'
'A'..='Z'
```

## arc_with_non_send_sync

Arc with non-Send/Sync type.

```rust
// BAD - Arc is for thread-safe sharing
Arc::new(Rc::new(5));  // Rc is not Send/Sync

// GOOD
Arc::new(5);  // i32 is Send + Sync
```

## await_holding_lock

Holding lock across await.

```rust
// BAD
async fn foo(mutex: &Mutex<i32>) {
    let guard = mutex.lock().unwrap();
    bar().await;  // lock held during await!
}

// GOOD
async fn foo(mutex: &Mutex<i32>) {
    {
        let guard = mutex.lock().unwrap();
        // use guard
    }  // guard dropped
    bar().await;
}
```

## await_holding_refcell_ref

Holding RefCell borrow across await.

```rust
// BAD
async fn foo(cell: &RefCell<i32>) {
    let borrow = cell.borrow();
    bar().await;  // borrow held during await!
}

// GOOD
async fn foo(cell: &RefCell<i32>) {
    let value = *cell.borrow();
    bar().await;
}
```

## blanket_clippy_restriction_lints

Enabling all restriction lints.

```rust
// BAD - too aggressive
#![warn(clippy::restriction)]

// GOOD - enable specific ones
#![warn(clippy::unwrap_used)]
#![warn(clippy::expect_used)]
```

## cast_abs_to_unsigned

Casting abs() result to unsigned.

```rust
// BAD - abs(i32::MIN) overflows
let x = (value.abs()) as u32;

// GOOD
let x = value.unsigned_abs();
```

## cast_enum_constructor

Casting enum constructor.

```rust
// BAD
let f = Some as fn(i32) -> Option<i32>;

// GOOD
let f: fn(i32) -> Option<i32> = Some;
```

## cast_enum_truncation

Enum cast may truncate.

```rust
// BAD
#[repr(u32)]
enum Big { A = 1000 }
let x = Big::A as u8;  // truncates!

// GOOD
let x = Big::A as u32;
```

## cast_nan_to_int

Casting NaN to int.

```rust
// BAD
let x = f64::NAN as i32;  // undefined!

// GOOD
let x = if f.is_nan() { 0 } else { f as i32 };
```

## cast_slice_different_sizes

Casting slice to different-sized type.

```rust
// BAD
let bytes: &[u8] = &[1, 2, 3, 4];
let ints: &[u32] = unsafe { 
    std::slice::from_raw_parts(bytes.as_ptr() as *const u32, bytes.len())
};  // wrong length!

// GOOD - calculate correct length
let ints: &[u32] = unsafe {
    std::slice::from_raw_parts(
        bytes.as_ptr() as *const u32,
        bytes.len() / std::mem::size_of::<u32>()
    )
};
```

## compare_self

Comparing self to self.

```rust
// BAD
impl PartialEq for Foo {
    fn eq(&self, other: &Self) -> bool {
        self == self  // comparing to self!
    }
}

// GOOD
impl PartialEq for Foo {
    fn eq(&self, other: &Self) -> bool {
        self.value == other.value
    }
}
```

## const_is_empty

Using is_empty on const.

```rust
// BAD - always same result
const EMPTY: &str = "";
if EMPTY.is_empty() { }  // always true

// Remove the check or use runtime value
```

## crate_in_macro_def

Using $crate incorrectly.

```rust
// BAD
macro_rules! foo {
    () => { crate::bar() };  // breaks when used from other crates
}

// GOOD
macro_rules! foo {
    () => { $crate::bar() };
}
```

## drop_non_drop

Calling drop on non-Drop type.

```rust
// BAD - no effect
let x = 5;
drop(x);  // i32 doesn't implement Drop

// Just let it go out of scope
```

## duplicate_mod

Duplicate module declaration.

```rust
// BAD
mod foo;
mod foo;  // duplicate

// GOOD
mod foo;
```

## empty_loop

Empty loop body.

```rust
// BAD - busy loop
loop {}

// GOOD - hint or yield
loop {
    std::hint::spin_loop();
}
```

## float_equality_without_abs

Float comparison without abs.

```rust
// BAD
(a - b) < f64::EPSILON  // wrong if a < b

// GOOD
(a - b).abs() < f64::EPSILON
```

## for_loops_over_fallibles

Looping over Option/Result.

```rust
// BAD
for x in Some(5) { }
for x in Ok::<_, ()>(5) { }

// GOOD
if let Some(x) = opt { }
if let Ok(x) = result { }
```

## from_raw_with_void_ptr

from_raw with void pointer.

```rust
// BAD
let boxed = unsafe { Box::from_raw(ptr as *mut ()) };

// Cast to correct type
let boxed = unsafe { Box::from_raw(ptr as *mut Actual) };
```

## get_unwrap

Using get().unwrap().

```rust
// BAD
let x = vec.get(0).unwrap();
let x = map.get(&key).unwrap();

// GOOD
let x = &vec[0];
let x = &map[&key];

// Or handle None
let x = vec.get(0)?;
```

## ineffective_open_options

Open options that cancel out.

```rust
// BAD
File::options()
    .write(true)
    .write(false)  // cancels previous!
    .open(path)?;
```

## iter_out_of_bounds

Iterator index out of bounds.

```rust
// BAD
let arr = [1, 2, 3];
arr.iter().skip(10).next();  // always None
```

## let_underscore_future

Dropping future without awaiting.

```rust
// BAD
let _ = async_fn();  // never runs!

// GOOD
async_fn().await;
```

## let_underscore_must_use

Dropping must_use value.

```rust
// BAD
let _ = mutex.lock();  // lock immediately dropped!

// GOOD
let _guard = mutex.lock();
```

## mismatched_target_os

Wrong target_os value.

```rust
// BAD
#[cfg(target_os = "linux")]  // lowercase
#[cfg(target_os = "MacOS")]  // should be "macos"

// GOOD
#[cfg(target_os = "linux")]
#[cfg(target_os = "macos")]
```

## multi_assignments

Multiple assignments in one statement.

```rust
// BAD
a = b = c;  // confusing

// GOOD
b = c;
a = b;
```

## mut_from_ref

Mutable from immutable reference.

```rust
// BAD
fn foo(&self) -> &mut T {
    unsafe { &mut *self.ptr }  // suspicious
}

// GOOD - if mutation needed, take &mut self
fn foo(&mut self) -> &mut T {
    unsafe { &mut *self.ptr }
}
```

## mutable_key_type

Mutable type as map key.

```rust
// BAD - mutating key breaks map
let mut map: HashMap<Vec<i32>, i32> = HashMap::new();

// GOOD - use immutable key type
let mut map: HashMap<String, i32> = HashMap::new();
```

## no_effect

Statement with no effect.

```rust
// BAD
0;
x + 1;  // result discarded

// GOOD
let _ = x + 1;  // explicitly discard
x += 1;  // or modify
```

## no_mangle_with_rust_abi

#[no_mangle] with Rust ABI.

```rust
// BAD - Rust ABI is unstable
#[no_mangle]
fn foo() { }

// GOOD - specify C ABI for FFI
#[no_mangle]
extern "C" fn foo() { }
```

## non_canonical_clone_impl

Clone impl that doesn't use clone.

```rust
// BAD
impl Clone for Foo {
    fn clone(&self) -> Self {
        Self { x: self.x }  // manual copy
    }
}

// GOOD
impl Clone for Foo {
    fn clone(&self) -> Self {
        *self  // or derive
    }
}
```

## non_canonical_partial_ord_impl

PartialOrd without using cmp.

```rust
// BAD
impl PartialOrd for Foo {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        if self.x < other.x { Some(Ordering::Less) }
        else if self.x > other.x { Some(Ordering::Greater) }
        else { Some(Ordering::Equal) }
    }
}

// GOOD
impl PartialOrd for Foo {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.x.partial_cmp(&other.x)
    }
}
```

## path_ends_with_ext

Path ends_with for extension.

```rust
// BAD
path.to_str().unwrap().ends_with(".txt")

// GOOD
path.extension() == Some(OsStr::new("txt"))
```

## print_in_format_impl

Printing in format implementation.

```rust
// BAD
impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        println!("debug");  // side effect in formatting!
        write!(f, "{}", self.x)
    }
}

// GOOD - no side effects
impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "{}", self.x)
    }
}
```

## suspicious_arithmetic_impl

Suspicious arithmetic trait impl.

```rust
// BAD
impl Add for Foo {
    fn add(self, other: Self) -> Self {
        Self { x: self.x - other.x }  // subtraction in Add!
    }
}

// GOOD
impl Add for Foo {
    fn add(self, other: Self) -> Self {
        Self { x: self.x + other.x }
    }
}
```

## suspicious_assignment_formatting

Suspicious spacing around assignment.

```rust
// BAD - looks like ==
if a =b { }

// GOOD
if a = b { }  // (though this is also suspicious)
if a == b { }
```

## suspicious_command_arg_space

Space in command argument.

```rust
// BAD
Command::new("ls").arg("-la /tmp");  // one arg with space

// GOOD
Command::new("ls").args(["-la", "/tmp"]);  // separate args
```

## suspicious_doc_comments

Suspicious doc comment position.

```rust
// BAD
fn foo() {
    /// This documents nothing
    let x = 5;
}

// GOOD
/// This documents foo
fn foo() {
    // This is a regular comment
    let x = 5;
}
```

## suspicious_else_formatting

Suspicious else formatting.

```rust
// BAD
if a {
}
else {  // else on separate line
}

// GOOD
if a {
} else {
}
```

## suspicious_map

Suspicious map usage.

```rust
// BAD
opt.map(|_| foo());  // map for side effect

// GOOD
if opt.is_some() {
    foo();
}
```

## suspicious_op_assign_impl

Suspicious op-assign implementation.

```rust
// BAD
impl AddAssign for Foo {
    fn add_assign(&mut self, other: Self) {
        *self = Self { x: self.x - other.x };  // subtraction!
    }
}

// GOOD
impl AddAssign for Foo {
    fn add_assign(&mut self, other: Self) {
        self.x += other.x;
    }
}
```

## suspicious_to_owned

Suspicious to_owned call.

```rust
// BAD
let s: String = string.to_owned().to_owned();

// GOOD
let s: String = string.to_owned();
```

## suspicious_unary_op_formatting

Suspicious unary op formatting.

```rust
// BAD
let x =- 1;  // looks like x = -1, but is x -= 1 typo?

// GOOD
let x = -1;
```

## swap_ptr_to_ref

Swapping via pointers.

```rust
// BAD
unsafe {
    let temp = *a;
    *a = *b;
    *b = temp;
}

// GOOD
std::mem::swap(a, b);
```

## type_id_on_box

Calling type_id on Box.

```rust
// BAD
let id = box_any.type_id();  // type_id of Box, not contents

// GOOD
let id = (*box_any).type_id();
```

## unconditional_recursion

Function always recurses.

```rust
// BAD
fn foo() {
    foo();  // infinite recursion
}

// Add base case
fn foo(n: u32) {
    if n == 0 { return; }
    foo(n - 1);
}
```

## unnecessary_result_map_or_else

Unnecessary result mapping.

```rust
// BAD
result.map_or_else(|e| Err(e), |v| Ok(v))

// GOOD
result
```

## unusual_byte_groupings

Unusual numeric groupings.

```rust
// BAD
let x = 0x1_23_456;  // inconsistent grouping

// GOOD
let x = 0x12_34_56;  // consistent pairs
let x = 0x123_456;   // consistent triplets
```
