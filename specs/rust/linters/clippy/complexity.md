# Clippy Complexity Lints

Lints for overcomplicated code that can be simplified.

## bind_instead_of_map

Using and_then/or_else when map suffices.

```rust
// BAD
opt.and_then(|x| Some(x + 1))
result.or_else(|_| Err(default_err))

// GOOD
opt.map(|x| x + 1)
result.map_err(|_| default_err)
```

## bool_comparison

Comparing boolean to literal.

```rust
// BAD
if b == true { }
if b == false { }

// GOOD
if b { }
if !b { }
```

## borrow_deref_ref

Borrowing then dereferencing then referencing.

```rust
// BAD
let y = &*&x;

// GOOD
let y = &x;
```

## bytes_count_to_len

Using bytes().count() on string.

```rust
// BAD
s.bytes().count()

// GOOD
s.len()
```

## char_lit_as_u8

Casting char literal to u8.

```rust
// BAD
let b = 'a' as u8;

// GOOD
let b = b'a';
```

## clone_on_copy

Calling clone on Copy type.

```rust
// BAD
let y = x.clone();  // x: i32

// GOOD
let y = x;  // just copy
```

## crosspointer_transmute

Transmuting between pointer and non-pointer.

```rust
// BAD
let ptr: *const i32 = unsafe { std::mem::transmute(x) };

// GOOD
let ptr = &x as *const i32;
```

## derivable_impls

Implementation that could be derived.

```rust
// BAD
impl Default for Foo {
    fn default() -> Self {
        Self { x: 0, y: String::new() }
    }
}

// GOOD
#[derive(Default)]
struct Foo {
    x: i32,
    y: String,
}
```

## diverging_sub_expression

Diverging expression in non-diverging context.

```rust
// BAD
let x = if condition { 1 } else { panic!() };

// GOOD - make it clear this is intentional
let x = if condition { 1 } else { unreachable!() };
```

## double_comparisons

Redundant double comparisons.

```rust
// BAD
x < y || x == y

// GOOD
x <= y
```

## double_parens

Unnecessary double parentheses.

```rust
// BAD
((x))
foo((bar))

// GOOD
(x)
foo(bar)
```

## duration_subsec

Getting subsec then converting.

```rust
// BAD
duration.subsec_nanos() as u64 / 1_000_000

// GOOD
duration.subsec_millis()
```

## excessive_nesting

Too much nesting.

```rust
// BAD
fn foo() {
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

// GOOD - extract functions, use early returns
fn foo() {
    if !a || !b { return; }
    for x in items {
        process_item(x);
    }
}
```

## explicit_counter_loop

Manual counter in for loop.

```rust
// BAD
let mut i = 0;
for x in items {
    println!("{}: {}", i, x);
    i += 1;
}

// GOOD
for (i, x) in items.iter().enumerate() {
    println!("{}: {}", i, x);
}
```

## explicit_write

Using write! to stdout/stderr.

```rust
// BAD
write!(std::io::stdout(), "hello")?;
write!(std::io::stderr(), "error")?;

// GOOD
print!("hello");
eprint!("error");
```

## extra_unused_lifetimes

Unnecessary lifetime parameters.

```rust
// BAD
fn foo<'a>(x: &i32) -> &i32 { x }

// GOOD
fn foo(x: &i32) -> &i32 { x }
```

## extra_unused_type_parameters

Unnecessary type parameters.

```rust
// BAD
fn foo<T>(x: i32) -> i32 { x }

// GOOD
fn foo(x: i32) -> i32 { x }
```

## filter_map_bool_then

Using filter_map with bool::then.

```rust
// BAD
iter.filter_map(|x| (x > 0).then(|| x))

// GOOD
iter.filter(|x| *x > 0)
```

## filter_next

Using filter + next.

```rust
// BAD
iter.filter(|x| x.is_valid()).next()

// GOOD
iter.find(|x| x.is_valid())
```

## flat_map_identity

Using flat_map with identity.

```rust
// BAD
iter.flat_map(|x| x)

// GOOD
iter.flatten()
```

## get_first

Using get(0).

```rust
// BAD
vec.get(0)

// GOOD
vec.first()
```

## get_last_with_len

Using get(len - 1).

```rust
// BAD
vec.get(vec.len() - 1)

// GOOD
vec.last()
```

## identity_op

Identity operation.

```rust
// BAD
x + 0
x * 1
x / 1

// GOOD - remove the operation
x
```

## if_same_then_else

If branches with identical bodies.

```rust
// BAD
if condition {
    foo();
} else {
    foo();
}

// GOOD
foo();
```

## int_plus_one

Using n + 1 in comparison.

```rust
// BAD
if x >= y + 1 { }
if x + 1 <= y { }

// GOOD
if x > y { }
if x < y { }
```

## iter_count

Using iter().count() on collection.

```rust
// BAD
vec.iter().count()

// GOOD
vec.len()
```

## iter_kv_map

Iterating map for transformation.

```rust
// BAD
map.iter().map(|(k, _)| k.clone()).collect()

// GOOD
map.keys().cloned().collect()
```

## iter_skip_zero

Skipping zero elements.

```rust
// BAD
iter.skip(0)

// Remove the skip
iter
```

## manual_filter

Manual filter pattern.

```rust
// BAD
match opt {
    Some(x) if predicate(x) => Some(x),
    _ => None,
}

// GOOD
opt.filter(|x| predicate(x))
```

## manual_filter_map

Manual filter_map pattern.

```rust
// BAD
iter.filter(|x| x.is_some()).map(|x| x.unwrap())

// GOOD
iter.filter_map(|x| x)
iter.flatten()
```

## manual_find

Manual find pattern.

```rust
// BAD
for x in iter {
    if predicate(&x) {
        return Some(x);
    }
}
None

// GOOD
iter.find(|x| predicate(x))
```

## manual_find_map

Manual find_map pattern.

```rust
// BAD
for x in iter {
    if let Some(y) = transform(x) {
        return Some(y);
    }
}
None

// GOOD
iter.find_map(transform)
```

## manual_flatten

Manual flatten pattern.

```rust
// BAD
iter.filter_map(|x| x)

// GOOD
iter.flatten()
```

## manual_is_ascii_check

Manual ASCII check.

```rust
// BAD
c >= 'a' && c <= 'z'
c >= '0' && c <= '9'

// GOOD
c.is_ascii_lowercase()
c.is_ascii_digit()
```

## manual_is_finite

Manual finite check.

```rust
// BAD
!x.is_nan() && !x.is_infinite()

// GOOD
x.is_finite()
```

## manual_is_infinite

Manual infinite check.

```rust
// BAD
x == f64::INFINITY || x == f64::NEG_INFINITY

// GOOD
x.is_infinite()
```

## manual_main_separator_str

Manual path separator.

```rust
// BAD
#[cfg(windows)]
const SEP: &str = "\\";
#[cfg(not(windows))]
const SEP: &str = "/";

// GOOD
std::path::MAIN_SEPARATOR_STR
```

## manual_next_back

Manual reverse iteration.

```rust
// BAD
iter.rev().next()

// GOOD
iter.next_back()
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

## manual_range_patterns

Manual range check.

```rust
// BAD
matches!(x, 1 | 2 | 3 | 4 | 5)

// GOOD
matches!(x, 1..=5)
```

## manual_saturating_arithmetic

Manual saturating arithmetic.

```rust
// BAD
if x > i32::MAX - y { i32::MAX } else { x + y }

// GOOD
x.saturating_add(y)
```

## manual_slice_size_calculation

Manual slice size calculation.

```rust
// BAD
std::mem::size_of::<T>() * slice.len()

// GOOD
std::mem::size_of_val(slice)
```

## manual_split_once

Manual split_once pattern.

```rust
// BAD
let mut parts = s.splitn(2, '=');
let key = parts.next()?;
let value = parts.next()?;

// GOOD
let (key, value) = s.split_once('=')?;
```

## manual_str_repeat

Manual string repeat.

```rust
// BAD
let mut s = String::new();
for _ in 0..n {
    s.push_str("x");
}

// GOOD
let s = "x".repeat(n);
```

## manual_strip

Manual strip pattern.

```rust
// BAD
if s.starts_with("prefix") {
    &s["prefix".len()..]
}

// GOOD
s.strip_prefix("prefix")
```

## manual_try_fold

Manual try_fold pattern.

```rust
// BAD
let mut acc = init;
for x in iter {
    acc = f(acc, x)?;
}
Ok(acc)

// GOOD
iter.try_fold(init, f)
```

## manual_unwrap_or_default

Manual unwrap_or_default.

```rust
// BAD
match opt {
    Some(x) => x,
    None => Default::default(),
}

// GOOD
opt.unwrap_or_default()
```

## manual_while_let_some

Manual while let Some.

```rust
// BAD
loop {
    let Some(x) = iter.next() else { break };
    // ...
}

// GOOD
while let Some(x) = iter.next() {
    // ...
}
```

## map_flatten

Using map + flatten.

```rust
// BAD
iter.map(f).flatten()

// GOOD
iter.flat_map(f)
```

## map_identity

Mapping with identity.

```rust
// BAD
iter.map(|x| x)

// Remove the map
iter
```

## match_as_ref

Match instead of as_ref.

```rust
// BAD
match opt {
    Some(ref x) => Some(x),
    None => None,
}

// GOOD
opt.as_ref()
```

## match_likelyhood_any_default

Match with all wildcards.

```rust
// BAD
match x {
    _ if condition => foo(),
    _ => bar(),
}

// GOOD
if condition { foo() } else { bar() }
```

## match_single_binding

Match with single binding.

```rust
// BAD
match (a, b) {
    (x, y) => x + y,
}

// GOOD
let (x, y) = (a, b);
x + y
```

## needless_arbitrary_self_type

Unnecessary explicit self type.

```rust
// BAD
fn foo(self: Self) { }
fn bar(self: &Self) { }
fn baz(self: &mut Self) { }

// GOOD
fn foo(self) { }
fn bar(&self) { }
fn baz(&mut self) { }
```

## needless_bool

Needless bool operations.

```rust
// BAD
if condition { true } else { false }
if condition { false } else { true }

// GOOD
condition
!condition
```

## needless_bool_assign

Needless bool assignment.

```rust
// BAD
if condition {
    x = true;
} else {
    x = false;
}

// GOOD
x = condition;
```

## needless_borrowed_reference

Needless borrowed reference.

```rust
// BAD
let &ref x = &y;

// GOOD
let x = &y;
```

## needless_if

Needless if.

```rust
// BAD
if condition { }

// Remove or add body
```

## needless_lifetimes

Unnecessary lifetime annotations.

```rust
// BAD
fn foo<'a>(x: &'a str) -> &'a str { x }

// GOOD - elision works
fn foo(x: &str) -> &str { x }
```

## needless_match

Needless match.

```rust
// BAD
match result {
    Ok(x) => Ok(x),
    Err(e) => Err(e),
}

// GOOD
result
```

## needless_option_as_deref

Needless as_deref on owned Option.

```rust
// BAD
Some(String::new()).as_deref()

// GOOD
Some(String::new()).as_ref().map(|s| s.as_str())
```

## needless_option_take

Needless take on owned Option.

```rust
// BAD
let x = opt.take();
// opt never used again

// GOOD
let x = opt;
```

## needless_question_mark

Unnecessary question mark.

```rust
// BAD
fn foo() -> Result<i32, Error> {
    Ok(bar()?)
}

// GOOD
fn foo() -> Result<i32, Error> {
    bar()
}
```

## needless_splitn

Splitn when split suffices.

```rust
// BAD
s.splitn(100, ',')

// GOOD
s.split(',')
```

## needless_update

Struct update with no actual update.

```rust
// BAD
Foo { x: 1, ..other }  // where other.x is overwritten

// GOOD
Foo { x: 1, y: other.y }
```

## neg_cmp_op_on_partial_ord

Negating comparison on partial ord.

```rust
// BAD
!(x < y)  // not same as x >= y for partial ord!

// GOOD
x >= y || x.partial_cmp(&y).is_none()
```

## no_effect

No effect statement.

```rust
// BAD
x + 1;  // discarded
0;

// Remove or use result
let _ = x + 1;
```

## nonminimal_bool

Non-minimal boolean expression.

```rust
// BAD
!a || !b
!(a && b && c)

// GOOD
!(a && b)
!a || !b || !c
```

## only_used_in_recursion

Parameter only used in recursive call.

```rust
// BAD
fn foo(x: i32, depth: i32) {
    foo(x, depth + 1);
}

// Consider removing or using the parameter
```

## option_as_ref_deref

Option as_ref then map deref.

```rust
// BAD
opt.as_ref().map(|x| x.as_str())

// GOOD
opt.as_deref()
```

## option_filter_map

Option filter then map.

```rust
// BAD
opt.filter(|x| predicate(x)).map(|x| transform(x))

// GOOD (sometimes)
opt.and_then(|x| predicate(&x).then(|| transform(x)))
```

## option_map_or_none

Option map_or with None.

```rust
// BAD
opt.map_or(None, |x| Some(x + 1))

// GOOD
opt.map(|x| x + 1)
```

## option_map_unit_fn

Map returning unit.

```rust
// BAD
opt.map(|x| println!("{}", x));

// GOOD
if let Some(x) = opt {
    println!("{}", x);
}
```

## or_then_unwrap

or_else then unwrap.

```rust
// BAD
opt.or_else(|| Some(default)).unwrap()

// GOOD
opt.unwrap_or_else(|| default)
opt.unwrap_or(default)
```

## partialeq_ne_impl

Implementing ne when eq suffices.

```rust
// BAD
impl PartialEq for Foo {
    fn eq(&self, other: &Self) -> bool { self.x == other.x }
    fn ne(&self, other: &Self) -> bool { self.x != other.x }  // unnecessary
}

// GOOD - ne has default impl
impl PartialEq for Foo {
    fn eq(&self, other: &Self) -> bool { self.x == other.x }
}
```

## precedence

Precedence confusion.

```rust
// BAD
a << 1 + b  // means a << (1 + b)

// GOOD - explicit parens
(a << 1) + b
a << (1 + b)
```

## ptr_offset_with_cast

Pointer offset with cast.

```rust
// BAD
ptr.offset(n as isize)

// GOOD
ptr.add(n)  // for unsigned
ptr.sub(n)  // for subtraction
```

## range_minus_one

Range with minus one.

```rust
// BAD
for i in 0..n - 1 { }

// GOOD
for i in 0..n.saturating_sub(1) { }
for i in 0..=n.saturating_sub(1) { }
```

## range_plus_one

Range with plus one.

```rust
// BAD
for i in 0..n + 1 { }

// GOOD
for i in 0..=n { }
```

## range_zip_with_len

Zipping range with len.

```rust
// BAD
(0..vec.len()).zip(&vec)

// GOOD
vec.iter().enumerate()
```

## redundant_as_str

Redundant as_str.

```rust
// BAD
string.as_str().len()

// GOOD
string.len()
```

## redundant_async_block

Redundant async block.

```rust
// BAD
async { future.await }

// GOOD
future
```

## redundant_at_rest_pattern

Redundant @ rest pattern.

```rust
// BAD
let [first, rest @ ..] = slice;
// rest never used

// GOOD
let [first, ..] = slice;
```

## redundant_closure_call

Calling closure immediately.

```rust
// BAD
(|| 5)()

// GOOD
5
```

## redundant_else

Redundant else after control flow.

```rust
// BAD
if condition {
    return x;
} else {
    y
}

// GOOD
if condition {
    return x;
}
y
```

## redundant_guards

Redundant match guards.

```rust
// BAD
match x {
    y if y == 5 => { }
    _ => { }
}

// GOOD
match x {
    5 => { }
    _ => { }
}
```

## redundant_pattern

Redundant pattern.

```rust
// BAD
match x {
    Foo { a: a, b: b } => { }
}

// GOOD
match x {
    Foo { a, b } => { }
}
```

## redundant_slicing

Redundant slicing.

```rust
// BAD
&slice[..]
&*string

// GOOD
slice
&string
```

## ref_in_deref

Ref in deref.

```rust
// BAD
(*&x).foo()

// GOOD
x.foo()
```

## repeat_once

Repeat once.

```rust
// BAD
"x".repeat(1)
iter::repeat(x).take(1)

// GOOD
"x".to_string()
iter::once(x)
```

## reserve_after_initialization

Reserve after initialization.

```rust
// BAD
let mut vec = Vec::new();
vec.reserve(100);

// GOOD
let mut vec = Vec::with_capacity(100);
```

## result_filter_map

Result filter then map.

```rust
// BAD
result.ok().and_then(|x| predicate(&x).then(|| transform(x)))

// GOOD
result.ok().filter(predicate).map(transform)
```

## result_map_or_into_option

Result map_or into Option.

```rust
// BAD
result.map_or(None, Some)

// GOOD
result.ok()
```

## search_is_some

Search then is_some.

```rust
// BAD
iter.find(predicate).is_some()

// GOOD
iter.any(predicate)
```

## seek_from_current

Seek from current.

```rust
// BAD
file.seek(SeekFrom::Current(0))

// GOOD
file.stream_position()
```

## seek_to_start_instead_of_rewind

Seek to start.

```rust
// BAD
file.seek(SeekFrom::Start(0))

// GOOD
file.rewind()
```

## short_circuit_statement

Short circuit in statement.

```rust
// BAD
condition && foo();
condition || bar();

// GOOD
if condition { foo(); }
if !condition { bar(); }
```

## single_element_loop

Loop over single element.

```rust
// BAD
for x in [only_one] { }
for x in std::iter::once(only_one) { }

// GOOD
let x = only_one;
```

## skip_while_next

skip_while + next.

```rust
// BAD
iter.skip_while(f).next()

// GOOD
iter.find(|x| !f(x))
```

## string_extend_chars

Extending string with chars.

```rust
// BAD
string.extend(other.chars())

// GOOD
string.push_str(&other)
```

## strlen_on_c_strings

strlen on CString.

```rust
// BAD
unsafe { libc::strlen(cstring.as_ptr()) }

// GOOD
cstring.as_bytes().len()
```

## temporary_assignment

Assignment to temporary.

```rust
// BAD
Foo::default().x = 5;  // immediately dropped

// GOOD
let mut foo = Foo::default();
foo.x = 5;
```

## too_many_arguments

Too many function arguments.

```rust
// BAD (default threshold: 7)
fn foo(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32, g: i32, h: i32) { }

// GOOD - use struct
struct Config { a: i32, b: i32, ... }
fn foo(config: Config) { }
```

## transmute_bytes_to_str

Transmute bytes to str.

```rust
// BAD
unsafe { std::mem::transmute::<&[u8], &str>(bytes) }

// GOOD
std::str::from_utf8(bytes)?
std::str::from_utf8_unchecked(bytes)  // if guaranteed valid
```

## transmute_float_to_int

Transmute float to int.

```rust
// BAD
unsafe { std::mem::transmute::<f32, u32>(f) }

// GOOD
f.to_bits()
```

## transmute_int_to_bool

Transmute int to bool.

```rust
// BAD
unsafe { std::mem::transmute::<u8, bool>(x) }

// GOOD
x != 0
```

## transmute_int_to_char

Transmute int to char.

```rust
// BAD
unsafe { std::mem::transmute::<u32, char>(x) }

// GOOD
char::from_u32(x)?
char::from_u32_unchecked(x)  // if guaranteed valid
```

## transmute_int_to_float

Transmute int to float.

```rust
// BAD
unsafe { std::mem::transmute::<u32, f32>(x) }

// GOOD
f32::from_bits(x)
```

## transmute_num_to_bytes

Transmute number to bytes.

```rust
// BAD
unsafe { std::mem::transmute::<i32, [u8; 4]>(x) }

// GOOD
x.to_ne_bytes()
```

## transmute_ptr_to_ref

Transmute pointer to reference.

```rust
// BAD
unsafe { std::mem::transmute::<*const T, &T>(ptr) }

// GOOD
unsafe { &*ptr }
```

## transmuting_null

Transmuting null.

```rust
// BAD
let null: &T = unsafe { std::mem::transmute(std::ptr::null::<T>()) };

// This is UB - don't create null references
```

## trim_split_whitespace

Trim then split_whitespace.

```rust
// BAD
s.trim().split_whitespace()

// GOOD - split_whitespace already ignores leading/trailing
s.split_whitespace()
```

## type_complexity

Type too complex.

```rust
// BAD
fn foo() -> Box<dyn Fn(&mut HashMap<String, Vec<Option<Result<i32, Error>>>>) -> bool> { }

// GOOD - use type alias
type Handler = Box<dyn Fn(&mut State) -> bool>;
fn foo() -> Handler { }
```

## unit_arg

Unit argument.

```rust
// BAD
foo(())
bar(println!("hello"))

// GOOD
foo()
println!("hello");
bar()
```

## unnecessary_cast

Unnecessary cast.

```rust
// BAD
let x = 5i32 as i32;

// GOOD
let x = 5i32;
```

## unnecessary_filter_map

filter_map when filter or map suffices.

```rust
// BAD
iter.filter_map(|x| if x > 0 { Some(x) } else { None })

// GOOD
iter.filter(|x| *x > 0)
```

## unnecessary_find_map

find_map when find or map suffices.

```rust
// BAD
iter.find_map(|x| if x > 0 { Some(x) } else { None })

// GOOD
iter.find(|x| *x > 0)
```

## unnecessary_fold

Fold when specialized method exists.

```rust
// BAD
iter.fold(true, |acc, x| acc && predicate(x))
iter.fold(false, |acc, x| acc || predicate(x))

// GOOD
iter.all(predicate)
iter.any(predicate)
```

## unnecessary_lazy_evaluations

Lazy evaluation when not needed.

```rust
// BAD
opt.unwrap_or_else(|| 5)
result.unwrap_or_else(|_| default)

// GOOD
opt.unwrap_or(5)
result.unwrap_or(default)
```

## unnecessary_literal_unwrap

Unwrapping literal.

```rust
// BAD
Some(5).unwrap()
Ok::<_, ()>(5).unwrap()

// GOOD
5
```

## unnecessary_map_on_constructor

Map on constructor.

```rust
// BAD
Some(x).map(Some)
Ok(x).map(Ok)

// GOOD
Some(Some(x))
Ok(Ok(x))
```

## unnecessary_operation

Operation with no effect.

```rust
// BAD
x + 0
x * 1

// GOOD - remove operation
x
```

## unnecessary_sort_by

Unnecessary sort_by.

```rust
// BAD
vec.sort_by(|a, b| a.cmp(b))

// GOOD
vec.sort()
```

## unnecessary_to_owned

Unnecessary to_owned.

```rust
// BAD
s.to_owned().as_str()

// GOOD
s
```

## unnecessary_unwrap

Unnecessary unwrap after is_some.

```rust
// BAD
if opt.is_some() {
    let x = opt.unwrap();
}

// GOOD
if let Some(x) = opt {
}
```

## unneeded_wildcard_pattern

Unneeded wildcard.

```rust
// BAD
let (x, _) = (1, 2);  // if _ never used

// GOOD
let (x, ..) = (1, 2);
```

## unusable_partial_ord_impl

PartialOrd not usable.

```rust
// BAD
impl PartialOrd for Foo {
    fn partial_cmp(&self, _: &Self) -> Option<Ordering> {
        None  // always None is useless
    }
}
```

## unused_format_specs

Unused format specs.

```rust
// BAD
format!("{:?}", 5)  // :? has no effect on integers

// GOOD
format!("{}", 5)
```

## unused_io_amount

Ignoring IO amount.

```rust
// BAD
file.read(&mut buf)?;  // doesn't check how much was read

// GOOD
let n = file.read(&mut buf)?;
// or use read_exact
file.read_exact(&mut buf)?;
```

## useless_asref

Useless as_ref.

```rust
// BAD
opt.as_ref().cloned()

// GOOD
opt.clone()
```

## useless_conversion

Useless type conversion.

```rust
// BAD
let s: String = String::from(s);

// GOOD
let s = s;
```

## useless_format

Useless format!.

```rust
// BAD
format!("{}", s)

// GOOD
s.to_string()
```

## useless_transmute

Useless transmute.

```rust
// BAD
unsafe { std::mem::transmute::<i32, i32>(x) }

// GOOD
x
```

## useless_vec

Vec where array works.

```rust
// BAD
vec![1, 2, 3].into_iter()

// GOOD
[1, 2, 3].into_iter()
```

## vec_box

Vec of Box.

```rust
// BAD
Vec<Box<T>>

// GOOD - Box adds unnecessary indirection
Vec<T>
```

## vec_init_then_push

Init then push.

```rust
// BAD
let mut v = Vec::new();
v.push(1);
v.push(2);

// GOOD
let v = vec![1, 2];
```

## verbose_bit_mask

Verbose bit mask.

```rust
// BAD
x & 0b1111 == 0

// GOOD
x.trailing_zeros() >= 4
```

## while_let_on_iterator

while let on iterator.

```rust
// BAD
while let Some(x) = iter.next() { }

// GOOD
for x in iter { }
```

## wildcard_in_or_patterns

Wildcard in or pattern.

```rust
// BAD
match x {
    A | B | _ => { }
}

// GOOD
match x {
    _ => { }
}
```

## zero_divided_by_something

Zero divided by something.

```rust
// BAD
0 / x

// GOOD
0
```

## zero_prefixed_literal

Zero-prefixed literal.

```rust
// BAD
let x = 0123;  // not octal in Rust!

// GOOD
let x = 123;   // decimal
let x = 0o123; // octal
```
