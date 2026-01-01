# Clippy Correctness Lints

Lints that detect code that is likely wrong. Default: deny.

## approx_constant

Use standard math constants.

```rust
// BAD
let pi = 3.14159265358979;
let e = 2.71828;

// GOOD
use std::f64::consts::{PI, E};
let pi = PI;
let e = E;
```

## derive_ord_xor_partial_ord

Ord and PartialOrd must agree.

```rust
// BAD - derived Ord might differ from manual PartialOrd
#[derive(Ord, PartialEq, Eq)]
struct Foo {
    a: i32,
}

impl PartialOrd for Foo {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        // custom implementation
    }
}

// GOOD - derive both or implement both
#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Foo {
    a: i32,
}
```

## enum_clike_unportable_variant

C-like enum variants must fit in target int.

```rust
// BAD on 32-bit
#[repr(isize)]
enum Foo {
    A = 0x1_0000_0000,  // overflow on 32-bit
}

// GOOD
#[repr(i64)]
enum Foo {
    A = 0x1_0000_0000,
}
```

## eq_op

Comparing identical operands.

```rust
// BAD
if x == x { }
assert!(y != y);

// GOOD
if x == y { }
```

## erasing_op

Operation that always produces same result.

```rust
// BAD
let _ = x * 0;  // always 0
let _ = x & 0;  // always 0
let _ = x | !0; // always !0

// GOOD - if intentional, assign directly
let _ = 0;
```

## fn_address_comparisons

Comparing function pointers is unreliable.

```rust
// BAD
if foo as fn() == bar as fn() { }

// GOOD - use function identity some other way
```

## if_let_mutex

Lock held across await point.

```rust
// BAD
if let Some(x) = mutex.lock().unwrap().as_ref() {
    async_op().await;  // lock held during await!
}

// GOOD
let value = {
    let guard = mutex.lock().unwrap();
    guard.as_ref().cloned()
};
if let Some(x) = value {
    async_op().await;
}
```

## ifs_same_cond

Multiple if branches with same condition.

```rust
// BAD
if x > 0 {
    foo();
} else if x > 0 {  // same condition!
    bar();
}

// GOOD
if x > 0 {
    foo();
} else if x < 0 {
    bar();
}
```

## impl_hash_borrow_with_str_and_bytes

Hash implementations must be consistent.

```rust
// BAD - Hash and Borrow<str> disagree
impl Hash for Foo {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.0.as_bytes().hash(state);  // hashes bytes
    }
}

impl Borrow<str> for Foo {
    fn borrow(&self) -> &str {
        &self.0  // borrows as str - different hash!
    }
}
```

## impossible_comparisons

Comparison that's always true or false.

```rust
// BAD
let x: u32 = get_value();
if x < 0 { }  // always false - u32 can't be negative

// GOOD
let x: i32 = get_value();
if x < 0 { }
```

## ineffective_bit_mask

Bit mask has no effect.

```rust
// BAD
if (x & 1 == 2) { }  // impossible - x & 1 is 0 or 1

// GOOD
if (x & 2 == 2) { }
```

## infinite_iter

Iterator that never terminates.

```rust
// BAD
let _ = (0..).collect::<Vec<_>>();  // infinite!

// GOOD
let _ = (0..100).collect::<Vec<_>>();
```

## inherent_to_string_shadow_display

to_string() shadows Display.

```rust
// BAD
struct Foo;

impl Foo {
    fn to_string(&self) -> String {
        "foo".into()
    }
}

impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "different")  // this won't be used by to_string()!
    }
}

// GOOD - just implement Display
impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "foo")
    }
}
```

## invalid_regex

Invalid regular expression.

```rust
// BAD
Regex::new("(unclosed");
Regex::new("[invalid");

// GOOD
Regex::new(r"valid\s+regex")?;
```

## iter_next_loop

Using .next() in for loop.

```rust
// BAD - consumes extra element
for x in iter.next() { }

// GOOD
for x in iter { }
```

## iter_skip_next

.skip(n).next() should be .nth(n).

```rust
// BAD
iter.skip(5).next()

// GOOD
iter.nth(5)
```

## let_underscore_lock

Dropping lock guard immediately.

```rust
// BAD - lock released immediately!
let _ = mutex.lock().unwrap();
// critical section here is NOT protected

// GOOD - hold the guard
let _guard = mutex.lock().unwrap();
// critical section IS protected
```

## match_ref_pats

Match on reference with ref patterns.

```rust
// BAD
match &x {
    &Some(ref y) => { }
    &None => { }
}

// GOOD
match x {
    Some(ref y) => { }
    None => { }
}

// Or match on reference directly
match &x {
    Some(y) => { }  // y is &T
    None => { }
}
```

## min_max

min/max with swapped arguments.

```rust
// BAD
std::cmp::min(10, std::cmp::max(x, 10))  // always 10

// GOOD - clamp
x.clamp(5, 10)
```

## misrefactored_assign_op

Assignment operator misuse.

```rust
// BAD - probably meant +=
a = a + b;

// GOOD
a += b;
```

## modulo_one

Modulo 1 is always 0.

```rust
// BAD
let remainder = x % 1;  // always 0

// Remove or fix the operation
```

## never_loop

Loop that never loops.

```rust
// BAD
loop {
    break;  // only runs once
}

// GOOD
if condition {
    do_something();
}
```

## non_octal_unix_permissions

Invalid unix permissions.

```rust
// BAD
fs::set_permissions(path, Permissions::from_mode(644));  // not octal!

// GOOD
fs::set_permissions(path, Permissions::from_mode(0o644));
```

## nonsensical_open_options

Conflicting file open options.

```rust
// BAD
File::options()
    .read(true)
    .truncate(true)  // truncate requires write!
    .open(path)?;

// GOOD
File::options()
    .write(true)
    .truncate(true)
    .open(path)?;
```

## not_unsafe_ptr_arg_deref

Dereferencing pointer in safe function.

```rust
// BAD
fn foo(ptr: *const i32) {
    unsafe { *ptr }  // caller can't guarantee validity
}

// GOOD - mark function unsafe
unsafe fn foo(ptr: *const i32) -> i32 {
    *ptr
}
```

## option_env_unwrap

Panicking on missing env var.

```rust
// BAD - panics if not set at compile time
let key = option_env!("API_KEY").unwrap();

// GOOD - handle missing
let key = option_env!("API_KEY").unwrap_or("default");

// Or use env! if required
let key = env!("API_KEY");  // compile error if missing
```

## out_of_bounds_indexing

Index out of bounds.

```rust
// BAD
let arr = [1, 2, 3];
let x = arr[3];  // out of bounds!

// GOOD
let x = arr.get(3);  // returns None
```

## panicking_unwrap

Unwrap on value that's guaranteed to panic.

```rust
// BAD
let x: Option<i32> = None;
x.unwrap();  // guaranteed panic

// GOOD
let x: Option<i32> = Some(5);
x.unwrap();  // OK
```

## recursive_format_impl

Infinite recursion in format implementation.

```rust
// BAD
impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "{}", self)  // infinite recursion!
    }
}

// GOOD
impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "{}", self.value)
    }
}
```

## size_of_in_element_count

Wrong use of size_of in allocation.

```rust
// BAD
let ptr = alloc(Layout::from_size_align(
    n * std::mem::size_of::<T>() * std::mem::size_of::<T>(),  // doubled!
    align
)?);

// GOOD
let ptr = alloc(Layout::from_size_align(
    n * std::mem::size_of::<T>(),
    align
)?);
```

## transmute_null

Transmuting null.

```rust
// BAD
let null: *const i32 = std::mem::transmute(0usize);

// GOOD
let null: *const i32 = std::ptr::null();
```

## unit_cmp

Comparing unit values.

```rust
// BAD
if foo() == bar() { }  // both return ()

// GOOD
foo();
bar();
```

## unit_hash

Hashing unit type.

```rust
// BAD
let mut hasher = DefaultHasher::new();
().hash(&mut hasher);  // useless
```

## while_immutable_condition

Condition never changes in loop.

```rust
// BAD
let cond = true;
while cond {  // infinite loop!
    do_something();
}

// GOOD
let mut cond = true;
while cond {
    do_something();
    cond = check();
}
```

## wrong_transmute

Transmute between incompatible types.

```rust
// BAD
let x: i32 = std::mem::transmute([0u8; 2]);  // size mismatch!

// GOOD
let x: i32 = std::mem::transmute([0u8; 4]);
```

## zst_offset

Offset on zero-sized type.

```rust
// BAD
let ptr: *const () = &();
let ptr2 = ptr.offset(1);  // meaningless for ZST

// Don't use offset with ZSTs
```
