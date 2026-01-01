# Clippy Pedantic Lints

More opinionated lints. Default: allow. Enable with:

```rust
#![warn(clippy::pedantic)]
```

## bool_to_int_with_if

Converting bool to int with if.

```rust
// BAD
if condition { 1 } else { 0 }

// GOOD
i32::from(condition)
condition as i32
```

## borrow_as_ptr

Borrow then cast to pointer.

```rust
// BAD
let ptr = &x as *const _;

// GOOD
let ptr = std::ptr::addr_of!(x);
```

## case_sensitive_file_extension_comparisons

Case-sensitive extension comparison.

```rust
// BAD
path.extension() == Some("TXT")  // misses "txt"

// GOOD
path.extension()
    .map(|e| e.eq_ignore_ascii_case("txt"))
    .unwrap_or(false)
```

## cast_lossless

Cast that could be lossless.

```rust
// BAD
let x = small as u64;

// GOOD
let x = u64::from(small);
```

## cast_possible_truncation

Cast that may truncate.

```rust
// BAD
let x = big as u8;  // may truncate

// GOOD
let x = u8::try_from(big)?;
let x = big.try_into()?;
```

## cast_possible_wrap

Cast that may wrap.

```rust
// BAD
let signed = unsigned as i32;  // may wrap

// GOOD
let signed = i32::try_from(unsigned)?;
```

## cast_precision_loss

Float cast losing precision.

```rust
// BAD
let f = big_int as f32;  // loses precision for large values

// GOOD - be explicit about precision loss
#[allow(clippy::cast_precision_loss)]
let f = big_int as f32;
```

## cast_sign_loss

Cast losing sign.

```rust
// BAD
let unsigned = signed as u32;  // negative becomes large positive

// GOOD
let unsigned = u32::try_from(signed)?;
```

## checked_conversions

Unchecked numeric conversions.

```rust
// BAD
let y = x as u16;

// GOOD
let y = u16::try_from(x)?;
```

## cloned_instead_of_copied

Using cloned() on Copy type.

```rust
// BAD
iter.cloned()  // where items are Copy

// GOOD
iter.copied()
```

## cognitive_complexity

Function too complex.

```rust
// BAD - high cyclomatic/cognitive complexity
fn complex() {
    if a {
        if b {
            for x in items {
                if c {
                    match d {
                        // ...
                    }
                }
            }
        }
    }
}

// GOOD - extract functions
fn complex() {
    if a && b {
        process_items();
    }
}
```

## copy_iterator

Iterator implementing Copy.

```rust
// BAD - Copy iterators can be accidentally advanced
#[derive(Copy)]
struct MyIter { pos: usize }

// GOOD - iterators should be Clone, not Copy
#[derive(Clone)]
struct MyIter { pos: usize }
```

## doc_markdown

Code in docs without backticks.

```rust
// BAD
/// This function uses HashMap.

// GOOD
/// This function uses `HashMap`.
```

## empty_enum

Empty enum.

```rust
// BAD (unless intentional as never type)
enum Empty {}

// GOOD - use never type
fn never_returns() -> ! {
    loop {}
}
```

## enum_glob_use

Glob import of enum.

```rust
// BAD
use MyEnum::*;

// GOOD
use MyEnum::{Variant1, Variant2};
```

## expl_impl_clone_on_copy

Explicit Clone on Copy type.

```rust
// BAD
#[derive(Copy)]
struct Foo(i32);

impl Clone for Foo {
    fn clone(&self) -> Self {
        *self
    }
}

// GOOD
#[derive(Copy, Clone)]
struct Foo(i32);
```

## explicit_deref_methods

Calling deref() explicitly.

```rust
// BAD
(*x).deref()
x.deref().deref()

// GOOD
&**x
```

## explicit_into_iter_loop

Explicit into_iter() in loop.

```rust
// BAD
for x in vec.into_iter() { }

// GOOD
for x in vec { }
```

## filter_map_next

filter_map + next.

```rust
// BAD
iter.filter_map(f).next()

// GOOD
iter.find_map(f)
```

## fn_params_excessive_bools

Too many bool parameters.

```rust
// BAD
fn configure(a: bool, b: bool, c: bool, d: bool) { }

// GOOD - use struct or builder
struct Config { a: bool, b: bool, c: bool, d: bool }
fn configure(config: Config) { }
```

## if_not_else

if !condition with else.

```rust
// BAD
if !condition {
    foo();
} else {
    bar();
}

// GOOD
if condition {
    bar();
} else {
    foo();
}
```

## implicit_hasher

Generic over hasher but using default.

```rust
// BAD
fn foo(map: &HashMap<K, V>) { }

// GOOD - generic over hasher
fn foo<S: BuildHasher>(map: &HashMap<K, V, S>) { }
```

## inconsistent_struct_constructor

Struct fields in different order than definition.

```rust
struct Foo { a: i32, b: i32, c: i32 }

// BAD
Foo { c: 3, a: 1, b: 2 }

// GOOD
Foo { a: 1, b: 2, c: 3 }
```

## inefficient_to_string

Using to_string() on Display type.

```rust
// BAD
format!("{}", x).len()

// GOOD
x.to_string().len()
```

## inline_always

Using #[inline(always)].

```rust
// BAD - usually let compiler decide
#[inline(always)]
fn small() { }

// GOOD
#[inline]
fn small() { }
```

## items_after_statements

Items after statements.

```rust
// BAD
fn foo() {
    let x = 1;
    struct Bar;  // item after statement
}

// GOOD
fn foo() {
    struct Bar;
    let x = 1;
}
```

## iter_not_returning_iterator

iter() not returning Iterator.

```rust
// BAD
impl Foo {
    fn iter(&self) -> Vec<&Item> { }
}

// GOOD
impl Foo {
    fn iter(&self) -> impl Iterator<Item = &Item> { }
}
```

## large_digit_groups

Large digit groups.

```rust
// BAD
let x = 1_000_0000;

// GOOD
let x = 10_000_000;
```

## large_types_passed_by_value

Large types passed by value.

```rust
// BAD
fn process(data: [u8; 1024]) { }

// GOOD
fn process(data: &[u8; 1024]) { }
```

## linkedlist

Using LinkedList.

```rust
// BAD - usually slower than Vec
let list: LinkedList<T> = LinkedList::new();

// GOOD - prefer Vec or VecDeque
let vec: Vec<T> = Vec::new();
let deque: VecDeque<T> = VecDeque::new();
```

## manual_assert

Manual panic with condition.

```rust
// BAD
if !condition {
    panic!("message");
}

// GOOD
assert!(condition, "message");
```

## manual_instant_elapsed

Manual instant elapsed calculation.

```rust
// BAD
let elapsed = Instant::now().duration_since(start);

// GOOD
let elapsed = start.elapsed();
```

## manual_let_else

Manual let else pattern.

```rust
// BAD
let x = match opt {
    Some(x) => x,
    None => return,
};

// GOOD (Rust 1.65+)
let Some(x) = opt else { return };
```

## manual_string_new

Manual String::new().

```rust
// BAD
let s = String::from("");
let s = "".to_string();

// GOOD
let s = String::new();
```

## map_unwrap_or

map + unwrap_or.

```rust
// BAD
opt.map(f).unwrap_or(default)

// GOOD
opt.map_or(default, f)
```

## match_bool

Match on boolean.

```rust
// BAD
match b {
    true => foo(),
    false => bar(),
}

// GOOD
if b { foo() } else { bar() }
```

## match_on_vec_items

Matching on Vec items by index.

```rust
// BAD
match vec[0] {
    x => { }
}

// GOOD
match vec.first() {
    Some(x) => { }
    None => { }
}
```

## match_same_arms

Match arms with same body.

```rust
// BAD
match x {
    A => foo(),
    B => foo(),
    C => bar(),
}

// GOOD
match x {
    A | B => foo(),
    C => bar(),
}
```

## match_wildcard_for_single_variants

Wildcard for single remaining variant.

```rust
// BAD
match opt {
    Some(x) => x,
    _ => 0,  // only None left
}

// GOOD
match opt {
    Some(x) => x,
    None => 0,
}
```

## maybe_infinite_iter

Potentially infinite iterator.

```rust
// BAD
(0..).filter(f).collect::<Vec<_>>();  // may never terminate

// GOOD
(0..100).filter(f).collect::<Vec<_>>();
```

## missing_const_for_fn

Function could be const.

```rust
// BAD
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// GOOD
const fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

## missing_errors_doc

Missing # Errors in doc.

```rust
// BAD
/// Does something.
fn fallible() -> Result<(), Error> { }

// GOOD
/// Does something.
///
/// # Errors
/// Returns `Err` if something fails.
fn fallible() -> Result<(), Error> { }
```

## missing_panics_doc

Missing # Panics in doc.

```rust
// BAD
/// Gets value.
fn get(idx: usize) -> &T {
    &self.data[idx]  // may panic
}

// GOOD
/// Gets value.
///
/// # Panics
/// Panics if index is out of bounds.
fn get(idx: usize) -> &T {
    &self.data[idx]
}
```

## module_name_repetitions

Type name repeats module name.

```rust
// BAD
mod foo {
    struct FooBar;
}

// GOOD
mod foo {
    struct Bar;
}
```

## must_use_candidate

Function should be #[must_use].

```rust
// BAD
fn compute() -> i32 { 42 }

// GOOD
#[must_use]
fn compute() -> i32 { 42 }
```

## needless_continue

Unnecessary continue.

```rust
// BAD
for x in iter {
    if condition {
        foo();
    } else {
        continue;
    }
}

// GOOD
for x in iter {
    if condition {
        foo();
    }
}
```

## needless_for_each

Unnecessary for_each.

```rust
// BAD
iter.for_each(|x| println!("{}", x));

// GOOD
for x in iter {
    println!("{}", x);
}
```

## needless_pass_by_value

Unnecessary ownership.

```rust
// BAD
fn foo(s: String) {
    println!("{}", s);
}

// GOOD
fn foo(s: &str) {
    println!("{}", s);
}
```

## no_effect_underscore_binding

Binding with no effect.

```rust
// BAD
let _x = expensive();  // computed but unused

// GOOD
let _ = expensive();  // if intentionally discarding
// Or remove if not needed
```

## option_option

Option<Option<T>>.

```rust
// BAD
fn foo() -> Option<Option<i32>> { }

// GOOD - flatten or use different representation
fn foo() -> Option<i32> { }
```

## range_minus_one

Range with minus one.

```rust
// BAD
for i in 0..len - 1 { }

// GOOD
for i in 0..len.saturating_sub(1) { }
for i in 0..=len.saturating_sub(1) { }
```

## range_plus_one

Range with plus one.

```rust
// BAD
for i in 0..len + 1 { }

// GOOD
for i in 0..=len { }
```

## redundant_closure_for_method_calls

Redundant closure for method.

```rust
// BAD
iter.map(|x| x.to_string())

// GOOD
iter.map(ToString::to_string)
```

## ref_binding_to_reference

Ref binding on reference.

```rust
// BAD
let ref x = &y;

// GOOD
let x = &y;
```

## return_self_not_must_use

Builder method not #[must_use].

```rust
// BAD
fn with_name(mut self, name: &str) -> Self {
    self.name = name.into();
    self
}

// GOOD
#[must_use]
fn with_name(mut self, name: &str) -> Self {
    self.name = name.into();
    self
}
```

## semicolon_if_nothing_returned

Missing semicolon on unit return.

```rust
// BAD
fn foo() {
    bar()  // returns (), missing semicolon
}

// GOOD
fn foo() {
    bar();
}
```

## similar_names

Similar variable names.

```rust
// BAD
let item = get();
let items = vec![];

// GOOD - more distinct names
let current_item = get();
let all_items = vec![];
```

## single_match_else

Single match with else.

```rust
// BAD
match opt {
    Some(x) => foo(x),
    _ => bar(),
}

// GOOD
if let Some(x) = opt {
    foo(x);
} else {
    bar();
}
```

## string_add_assign

Using + for string append.

```rust
// BAD
s = s + &other;

// GOOD
s += &other;
s.push_str(&other);
```

## struct_excessive_bools

Struct with many bools.

```rust
// BAD
struct Config {
    a: bool,
    b: bool,
    c: bool,
    d: bool,
}

// GOOD - use bitflags or enum
bitflags! {
    struct ConfigFlags: u32 {
        const A = 1;
        const B = 2;
        const C = 4;
        const D = 8;
    }
}
```

## too_many_arguments

Too many function arguments.

```rust
// BAD
fn configure(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32, g: i32) { }

// GOOD
struct Config { a: i32, b: i32, c: i32, d: i32, e: i32, f: i32, g: i32 }
fn configure(config: Config) { }
```

## too_many_lines

Function too long.

```rust
// Keep functions under ~100 lines
// Extract helper functions
```

## trivially_copy_pass_by_ref

Copy type passed by reference.

```rust
// BAD
fn foo(x: &i32) { }

// GOOD - small Copy types by value
fn foo(x: i32) { }
```

## type_repetition_in_bounds

Repeated type in bounds.

```rust
// BAD
fn foo<T: Clone + Clone>() { }

// GOOD
fn foo<T: Clone>() { }
```

## unicode_not_nfc

Non-NFC unicode.

```rust
// BAD
let s = "café";  // might use combining characters

// GOOD - normalize
let s = "café";  // precomposed é
```

## uninlined_format_args

Format args not inlined.

```rust
// BAD
println!("{}", x);
format!("{}", y);

// GOOD (Rust 1.58+)
println!("{x}");
format!("{y}");
```

## unnecessary_join

Unnecessary join.

```rust
// BAD
["a", "b"].join("")

// GOOD
["a", "b"].concat()
```

## unnecessary_wraps

Unnecessary Option/Result wrapping.

```rust
// BAD - always returns Some/Ok
fn foo() -> Option<i32> {
    Some(42)
}

// GOOD
fn foo() -> i32 {
    42
}
```

## unnested_or_patterns

Un-nested or patterns.

```rust
// BAD
match x {
    A(a) | B(a) => { }
}

// GOOD
match x {
    A(a) | B(a) => { }
}
```

## unreadable_literal

Large number without separators.

```rust
// BAD
let x = 1000000;

// GOOD
let x = 1_000_000;
```

## unused_async

Async function without await.

```rust
// BAD
async fn foo() {
    sync_operation();
}

// GOOD
fn foo() {
    sync_operation();
}
```

## unused_self

Unused self parameter.

```rust
// BAD
impl Foo {
    fn bar(&self) {
        println!("hello");
    }
}

// GOOD - make it associated function
impl Foo {
    fn bar() {
        println!("hello");
    }
}
```

## used_underscore_binding

Using underscore binding.

```rust
// BAD
let _x = 5;
println!("{}", _x);  // underscore prefix means unused!

// GOOD
let x = 5;
println!("{}", x);
```

## wildcard_imports

Wildcard imports.

```rust
// BAD
use std::collections::*;

// GOOD
use std::collections::{HashMap, HashSet};
```
