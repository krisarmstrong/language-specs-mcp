# Clippy Style Lints

Code style and conventions.

## assertions_on_constants

Assert on constant condition.

```rust
// BAD
assert!(true);
debug_assert!(false);

// Remove or use compile-time check
const_assert!(CONDITION);
```

## assign_op_pattern

Manual compound assignment.

```rust
// BAD
x = x + 1;
x = x * 2;

// GOOD
x += 1;
x *= 2;
```

## bool_assert_comparison

Assert with bool comparison.

```rust
// BAD
assert_eq!(result, true);
assert_eq!(result, false);

// GOOD
assert!(result);
assert!(!result);
```

## blocks_in_conditions

Complex blocks in if conditions.

```rust
// BAD
if { let x = get(); x > 0 } { }

// GOOD
let x = get();
if x > 0 { }
```

## borrow_interior_mutable_const

Borrowing interior mutable const.

```rust
// BAD
const CELL: Cell<i32> = Cell::new(0);
let x = &CELL;  // each use gets fresh Cell!

// GOOD
static CELL: Cell<i32> = Cell::new(0);
let x = &CELL;  // same Cell each time
```

## builtin_type_shadow

Shadowing builtin types.

```rust
// BAD
fn foo<u32>(x: u32) { }  // u32 is type parameter, not primitive!

// GOOD
fn foo<T>(x: T) { }
fn foo(x: u32) { }  // actually uses primitive
```

## clone_on_ref_ptr

Calling clone() on Rc/Arc.

```rust
// BAD - looks like deep clone
let b = a.clone();

// GOOD - explicit reference clone
let b = Rc::clone(&a);
let b = Arc::clone(&a);
```

## cmp_null

Comparing to null pointer.

```rust
// BAD
if ptr == std::ptr::null() { }

// GOOD
if ptr.is_null() { }
```

## collapsible_if

Nested if can be combined.

```rust
// BAD
if a {
    if b {
        do_something();
    }
}

// GOOD
if a && b {
    do_something();
}
```

## collapsible_else_if

Else with only if inside.

```rust
// BAD
if a {
} else {
    if b {
    }
}

// GOOD
if a {
} else if b {
}
```

## comparison_to_empty

Comparing to empty collection.

```rust
// BAD
if s == "" { }
if v == vec![] { }

// GOOD
if s.is_empty() { }
if v.is_empty() { }
```

## default_trait_access

Using Default::default() when type has default().

```rust
// BAD
let x: Vec<i32> = Default::default();

// GOOD
let x: Vec<i32> = Vec::default();
let x = Vec::<i32>::default();

// Or just new() if available
let x: Vec<i32> = Vec::new();
```

## double_neg

Double negation.

```rust
// BAD
let x = --y;

// GOOD
let x = y;
```

## explicit_auto_deref

Explicit deref when auto-deref works.

```rust
// BAD
let x: &i32 = &*y;

// GOOD
let x: &i32 = y;
```

## explicit_iter_loop

Explicit iter() in for loop.

```rust
// BAD
for x in vec.iter() { }
for x in vec.iter_mut() { }

// GOOD
for x in &vec { }
for x in &mut vec { }
```

## field_reassign_with_default

Reassigning default fields.

```rust
// BAD
let mut x = Foo::default();
x.field1 = 1;
x.field2 = 2;

// GOOD
let x = Foo {
    field1: 1,
    field2: 2,
    ..Default::default()
};
```

## for_kv_map

Iterating map for keys or values only.

```rust
// BAD
for (k, _) in &map { }
for (_, v) in &map { }

// GOOD
for k in map.keys() { }
for v in map.values() { }
```

## from_over_into

Implementing Into instead of From.

```rust
// BAD
impl Into<String> for Foo {
    fn into(self) -> String { }
}

// GOOD
impl From<Foo> for String {
    fn from(foo: Foo) -> String { }
}
```

## implicit_clone

Using to_owned/to_vec for clone.

```rust
// BAD
let s = original.to_owned();
let v = original.to_vec();

// GOOD
let s = original.clone();
let v = original.clone();
```

## infallible_destructuring_match

Match on infallible pattern.

```rust
// BAD
let Foo { x } = match foo {
    Foo { x } => Foo { x },
};

// GOOD
let Foo { x } = foo;
```

## inherent_to_string

Inherent to_string when Display exists.

```rust
// BAD
impl Foo {
    fn to_string(&self) -> String { }
}

// GOOD - just implement Display
impl Display for Foo {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result { }
}
```

## into_iter_on_ref

into_iter() on reference.

```rust
// BAD
(&vec).into_iter()

// GOOD
vec.iter()
```

## is_digit_ascii_radix

is_digit with ascii radix.

```rust
// BAD
c.is_digit(10)
c.is_digit(16)

// GOOD
c.is_ascii_digit()
c.is_ascii_hexdigit()
```

## just_underscores_and_digits

Variable name is only underscores and digits.

```rust
// BAD
let _1 = 1;
let __2__ = 2;

// GOOD
let count_1 = 1;
let value_2 = 2;
```

## len_without_is_empty

len() without is_empty().

```rust
// BAD
impl Foo {
    fn len(&self) -> usize { }
}

// GOOD
impl Foo {
    fn len(&self) -> usize { }
    fn is_empty(&self) -> bool {
        self.len() == 0
    }
}
```

## len_zero

Using len() == 0.

```rust
// BAD
if s.len() == 0 { }
if s.len() != 0 { }

// GOOD
if s.is_empty() { }
if !s.is_empty() { }
```

## let_and_return

Let then immediate return.

```rust
// BAD
let result = compute();
result

// GOOD
compute()
```

## manual_map

Manual Option/Result mapping.

```rust
// BAD
match opt {
    Some(x) => Some(x.len()),
    None => None,
}

// GOOD
opt.map(|x| x.len())
```

## manual_ok_or

Manual ok_or pattern.

```rust
// BAD
match opt {
    Some(x) => Ok(x),
    None => Err(e),
}

// GOOD
opt.ok_or(e)
```

## manual_range_contains

Manual range check.

```rust
// BAD
x >= 0 && x < 10

// GOOD
(0..10).contains(&x)
```

## manual_unwrap_or

Manual unwrap_or pattern.

```rust
// BAD
match opt {
    Some(x) => x,
    None => default,
}

// GOOD
opt.unwrap_or(default)
```

## match_bool

Match on bool.

```rust
// BAD
match condition {
    true => foo(),
    false => bar(),
}

// GOOD
if condition { foo() } else { bar() }
```

## match_like_matches_macro

Match that returns bool.

```rust
// BAD
match x {
    Some(_) => true,
    None => false,
}

// GOOD
matches!(x, Some(_))
```

## match_overlapping_arm

Match arms that overlap.

```rust
// BAD
match x {
    0..=10 => foo(),
    5..=15 => bar(),  // 5-10 overlaps!
    _ => baz(),
}
```

## match_ref_pats

Match with ref patterns.

```rust
// BAD
match &x {
    &Some(ref y) => { }
    _ => { }
}

// GOOD
match x {
    Some(ref y) => { }
    _ => { }
}
```

## match_result_ok

Match on Result to get Ok.

```rust
// BAD
match result {
    Ok(x) => Some(x),
    Err(_) => None,
}

// GOOD
result.ok()
```

## match_single_binding

Match with single binding.

```rust
// BAD
match (a, b) {
    (x, y) => foo(x, y),
}

// GOOD
let (x, y) = (a, b);
foo(x, y);
```

## match_wild_err_arm

Match with wildcard in Err arm.

```rust
// BAD
match result {
    Ok(x) => x,
    Err(_) => default,  // ignores error!
}

// GOOD
result.unwrap_or(default)
// Or handle the error
```

## needless_borrow

Unnecessary borrow.

```rust
// BAD
let x = &1;
takes_ref(&x);  // double reference

// GOOD
takes_ref(x);
```

## needless_return

Unnecessary return keyword.

```rust
// BAD
fn foo() -> i32 {
    return 42;
}

// GOOD
fn foo() -> i32 {
    42
}
```

## new_ret_no_self

new() that doesn't return Self.

```rust
// BAD
impl Foo {
    fn new() -> Bar { }
}

// GOOD
impl Foo {
    fn new() -> Self { }
    fn new() -> Foo { }
}
```

## new_without_default

new() without Default impl.

```rust
// BAD
impl Foo {
    fn new() -> Self { }
}

// GOOD
impl Foo {
    fn new() -> Self { }
}

impl Default for Foo {
    fn default() -> Self {
        Self::new()
    }
}
```

## op_ref

Reference operand.

```rust
// BAD
let x = &a + &b;

// GOOD
let x = a + b;
```

## option_map_unit_fn

map() returning unit.

```rust
// BAD
opt.map(|x| println!("{}", x));

// GOOD
if let Some(x) = opt {
    println!("{}", x);
}
```

## ptr_arg

&Vec or &String as argument.

```rust
// BAD
fn foo(v: &Vec<i32>) { }
fn bar(s: &String) { }

// GOOD
fn foo(v: &[i32]) { }
fn bar(s: &str) { }
```

## question_mark

Manual ? operator pattern.

```rust
// BAD
match opt {
    Some(x) => x,
    None => return None,
}

// GOOD
opt?
```

## redundant_closure

Closure that just calls function.

```rust
// BAD
iter.map(|x| foo(x))

// GOOD
iter.map(foo)
```

## redundant_field_names

Redundant field name in struct literal.

```rust
// BAD
Foo { x: x, y: y }

// GOOD
Foo { x, y }
```

## redundant_pattern_matching

Unnecessary pattern matching.

```rust
// BAD
if let Some(_) = opt { }
if let Ok(_) = result { }

// GOOD
if opt.is_some() { }
if result.is_ok() { }
```

## redundant_static_lifetimes

Unnecessary 'static lifetime.

```rust
// BAD
const S: &'static str = "hello";
static S: &'static str = "hello";

// GOOD
const S: &str = "hello";
static S: &str = "hello";
```

## self_named_constructors

Constructor named new_self.

```rust
// BAD
impl Foo {
    fn new_foo() -> Foo { }
}

// GOOD
impl Foo {
    fn new() -> Self { }
}
```

## single_match

Single-arm match.

```rust
// BAD
match opt {
    Some(x) => foo(x),
    _ => { }
}

// GOOD
if let Some(x) = opt {
    foo(x);
}
```

## string_lit_as_bytes

String literal to bytes.

```rust
// BAD
"hello".as_bytes()

// GOOD
b"hello"
```

## tabs_in_doc_comments

Tabs in documentation.

```rust
// BAD (contains tab)
/// 	indented with tab

// GOOD
///     indented with spaces
```

## to_digit_is_some

to_digit().is_some() instead of is_digit().

```rust
// BAD
c.to_digit(10).is_some()

// GOOD
c.is_digit(10)
```

## toplevel_ref_arg

ref in top-level pattern.

```rust
// BAD
fn foo(ref x: String) { }

// GOOD
fn foo(x: &String) { }
```

## unnecessary_fold

fold that could be a specialized method.

```rust
// BAD
iter.fold(0, |acc, x| acc + x)
iter.fold(true, |acc, x| acc && x)

// GOOD
iter.sum()
iter.all(|x| x)
```

## unnecessary_mut_passed

Mutable reference passed to function that doesn't need it.

```rust
// BAD
fn foo(x: &i32) { }
foo(&mut value);

// GOOD
foo(&value);
```

## wrong_self_convention

Self convention violation.

```rust
// BAD - is_* should take &self
fn is_empty(self) -> bool { }

// BAD - to_* should take &self  
fn to_string(&mut self) -> String { }

// BAD - into_* should take self
fn into_vec(&self) -> Vec<T> { }

// GOOD
fn is_empty(&self) -> bool { }
fn to_string(&self) -> String { }
fn into_vec(self) -> Vec<T> { }
```
