# Clippy Performance Lints

Lints that detect slow code.

## box_collection

Boxing a Vec or String is unnecessary.

```rust
// BAD
let v: Box<Vec<i32>> = Box::new(vec![1, 2, 3]);
let s: Box<String> = Box::new("hello".into());

// GOOD - already heap allocated
let v: Vec<i32> = vec![1, 2, 3];
let s: String = "hello".into();

// Use Box<[T]> or Box<str> if you want fixed size
let v: Box<[i32]> = vec![1, 2, 3].into_boxed_slice();
let s: Box<str> = "hello".into();
```

## boxed_local

Boxing a local that doesn't escape.

```rust
// BAD
fn foo() {
    let boxed = Box::new(5);
    println!("{}", boxed);
}

// GOOD
fn foo() {
    let value = 5;
    println!("{}", value);
}
```

## cmp_owned

Creating owned value for comparison.

```rust
// BAD
if s.to_string() == "hello" { }
if s.to_lowercase() == "hello" { }

// GOOD
if s == "hello" { }
if s.eq_ignore_ascii_case("hello") { }
```

## collapsible_str_replace

Multiple str::replace calls.

```rust
// BAD
let s = s.replace("a", "").replace("b", "").replace("c", "");

// GOOD - single pass with array (Rust 1.58+)
let s = s.replace(['a', 'b', 'c'], "");
```

## expect_fun_call

Dynamic string in expect().

```rust
// BAD - allocates even on success
opt.expect(&format!("failed for {}", id));

// GOOD
opt.unwrap_or_else(|| panic!("failed for {}", id));
```

## extend_with_drain

Using extend with drain.

```rust
// BAD
v1.extend(v2.drain(..));

// GOOD
v1.append(&mut v2);
```

## filter_map_identity

filter_map with identity.

```rust
// BAD
iter.filter_map(|x| x)

// GOOD
iter.flatten()
```

## flat_map_option

flat_map on Option.

```rust
// BAD
iter.flat_map(|x| x.ok())

// GOOD
iter.filter_map(|x| x.ok())
```

## iter_nth

Iterating to get nth element.

```rust
// BAD
let x = iter.skip(5).next();

// GOOD
let x = iter.nth(5);
```

## iter_overeager_cloned

Clone before filtering.

```rust
// BAD - clones everything including filtered
iter.cloned().filter(|x| x.is_some())

// GOOD - only clone what passes filter
iter.filter(|x| x.is_some()).cloned()
```

## large_const_arrays

Large array as const.

```rust
// BAD - duplicated at each use site
const BIG: [u8; 1000000] = [0; 1000000];

// GOOD - single copy in static
static BIG: [u8; 1000000] = [0; 1000000];
```

## large_enum_variant

Enum with significantly different variant sizes.

```rust
// BAD
enum Foo {
    Small(i32),
    Large([u8; 1000]),  // makes all Foos 1000+ bytes
}

// GOOD - box the large variant
enum Foo {
    Small(i32),
    Large(Box<[u8; 1000]>),
}
```

## manual_memcpy

Manual byte-by-byte copy.

```rust
// BAD
for i in 0..len {
    dst[i] = src[i];
}

// GOOD
dst[..len].copy_from_slice(&src[..len]);
```

## manual_str_repeat

Manual string repetition.

```rust
// BAD
let mut s = String::new();
for _ in 0..n {
    s.push_str("hello");
}

// GOOD
let s = "hello".repeat(n);
```

## map_entry

Map lookup then insert.

```rust
// BAD
if !map.contains_key(&key) {
    map.insert(key, value);
}

// GOOD
map.entry(key).or_insert(value);

// With computation
map.entry(key).or_insert_with(|| compute_value());
```

## missing_spin_loop

Busy loop without spin_loop_hint.

```rust
// BAD - wastes CPU
while flag.load(Ordering::Relaxed) {
    // busy wait
}

// GOOD
while flag.load(Ordering::Relaxed) {
    std::hint::spin_loop();
}
```

## needless_collect

Collecting iterator just to iterate again.

```rust
// BAD
let v: Vec<_> = iter.collect();
for x in v { }

// GOOD
for x in iter { }
```

## or_fun_call

Expensive call in or().

```rust
// BAD - always allocates
opt.or(Some(String::new()))

// GOOD - lazy evaluation
opt.or_else(|| Some(String::new()))
```

## redundant_allocation

Redundant wrapper like Rc<Box<T>>.

```rust
// BAD
let x: Rc<Box<i32>> = Rc::new(Box::new(5));
let y: Box<Rc<i32>> = Box::new(Rc::new(5));

// GOOD
let x: Rc<i32> = Rc::new(5);
let y: Box<i32> = Box::new(5);
```

## redundant_clone

Cloning value that doesn't need it.

```rust
// BAD
let s = s.clone();
drop(s);

// GOOD
drop(s);  // can drop without clone if not used after
```

## single_char_pattern

String pattern for single char.

```rust
// BAD
s.contains("x");
s.split("x");
s.starts_with("x");

// GOOD
s.contains('x');
s.split('x');
s.starts_with('x');
```

## slow_vector_initialization

Slow vector initialization pattern.

```rust
// BAD
let mut v = Vec::with_capacity(n);
for _ in 0..n {
    v.push(0);
}

// GOOD
let v = vec![0; n];

// Or
let v: Vec<i32> = std::iter::repeat(0).take(n).collect();
```

## stable_sort_primitive

Stable sort on primitives.

```rust
// BAD - stable sort is slower
let mut v: Vec<i32> = vec![3, 1, 2];
v.sort();

// GOOD - unstable is fine for primitives
v.sort_unstable();
```

## to_string_in_format_args

to_string in format macro.

```rust
// BAD - unnecessary allocation
println!("{}", x.to_string());

// GOOD
println!("{}", x);
```

## unnecessary_to_owned

Unnecessary to_owned/to_string.

```rust
// BAD
let s = string.to_owned();
takes_ref(&s);

// GOOD
takes_ref(&string);
```

## useless_vec

Vec where array/slice works.

```rust
// BAD
for x in vec![1, 2, 3] { }

// GOOD
for x in [1, 2, 3] { }
for x in &[1, 2, 3] { }
```

## vec_init_then_push

Init empty Vec then push.

```rust
// BAD
let mut v = Vec::new();
v.push(1);
v.push(2);
v.push(3);

// GOOD
let v = vec![1, 2, 3];
```

## waker_clone_wake

Clone then wake Waker.

```rust
// BAD
waker.clone().wake();

// GOOD
waker.wake_by_ref();
// or
waker.wake();  // if you're done with it
```

## write_with_newline

write! with trailing newline.

```rust
// BAD
write!(f, "hello\n")?;

// GOOD
writeln!(f, "hello")?;
```
