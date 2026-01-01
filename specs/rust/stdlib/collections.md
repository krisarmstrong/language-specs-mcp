# Rust Collections (std::collections)

## Vec<T>

Growable array. Most common collection.

```rust
// Create
let mut vec: Vec<i32> = Vec::new();
let vec = vec![1, 2, 3];
let vec = Vec::with_capacity(100);
let vec: Vec<i32> = (0..10).collect();

// Access
vec[0];                     // panics if out of bounds
vec.get(0);                 // Option<&T>
vec.get_mut(0);             // Option<&mut T>
vec.first();                // Option<&T>
vec.last();                 // Option<&T>

// Modify
vec.push(4);
vec.pop();                  // Option<T>
vec.insert(0, value);       // O(n)
vec.remove(0);              // O(n)
vec.swap_remove(0);         // O(1), doesn't preserve order
vec.clear();
vec.truncate(5);
vec.resize(10, default);
vec.extend([4, 5, 6]);

// Slicing
let slice = &vec[1..3];
vec.split_at(2);            // (&[T], &[T])
vec.split_first();          // Option<(&T, &[T])>
vec.chunks(2);              // iterator of slices
vec.windows(2);             // sliding window iterator

// Iteration
for item in &vec { }        // borrow
for item in &mut vec { }    // mutable borrow
for item in vec { }         // consume

// Sorting
vec.sort();                 // stable sort
vec.sort_unstable();        // faster, not stable
vec.sort_by(|a, b| b.cmp(a));  // custom comparator
vec.sort_by_key(|x| x.len());

// Searching
vec.contains(&value);
vec.binary_search(&value);  // Result<usize, usize>
vec.iter().position(|x| *x == value);
vec.iter().find(|x| **x > 5);

// Deduplication
vec.dedup();                // consecutive duplicates
vec.dedup_by_key(|x| x.id);

// Capacity
vec.len();
vec.is_empty();
vec.capacity();
vec.shrink_to_fit();
vec.reserve(100);
```

## HashMap<K, V>

Hash table. O(1) average operations.

```rust
use std::collections::HashMap;

// Create
let mut map: HashMap<String, i32> = HashMap::new();
let map = HashMap::with_capacity(100);
let map: HashMap<_, _> = vec![("a", 1), ("b", 2)].into_iter().collect();

// Access
map.get("key");             // Option<&V>
map.get_mut("key");         // Option<&mut V>
map["key"];                 // panics if missing
map.contains_key("key");

// Modify
map.insert("key", 42);      // Option<V> (old value)
map.remove("key");          // Option<V>
map.clear();

// Entry API (key-based modification)
map.entry("key").or_insert(0);
map.entry("key").or_insert_with(|| expensive_computation());
map.entry("key").and_modify(|v| *v += 1).or_insert(0);

*map.entry("word").or_insert(0) += 1;  // word counting

// Iteration
for (key, value) in &map { }
for (key, value) in &mut map { }
for key in map.keys() { }
for value in map.values() { }
for value in map.values_mut() { }
map.iter().filter(|(k, v)| v > &&0);

// Capacity
map.len();
map.is_empty();
map.capacity();
map.shrink_to_fit();
map.reserve(100);
```

## HashSet<T>

Hash set. Unique elements, O(1) operations.

```rust
use std::collections::HashSet;

// Create
let mut set: HashSet<i32> = HashSet::new();
let set: HashSet<_> = vec![1, 2, 3].into_iter().collect();

// Modify
set.insert(42);             // bool (true if new)
set.remove(&42);            // bool
set.take(&42);              // Option<T>
set.clear();

// Query
set.contains(&42);
set.get(&42);               // Option<&T>

// Set operations
let union = a.union(&b);
let intersection = a.intersection(&b);
let difference = a.difference(&b);
let symmetric_diff = a.symmetric_difference(&b);

a.is_subset(&b);
a.is_superset(&b);
a.is_disjoint(&b);
```

## BTreeMap<K, V> and BTreeSet<T>

Sorted collections. O(log n) operations.

```rust
use std::collections::{BTreeMap, BTreeSet};

let mut map: BTreeMap<String, i32> = BTreeMap::new();
let mut set: BTreeSet<i32> = BTreeSet::new();

// Same API as HashMap/HashSet plus:

// Range operations
for (k, v) in map.range("a".."z") { }
for (k, v) in map.range(..="m") { }

// First/Last
map.first_key_value();      // Option<(&K, &V)>
map.last_key_value();
map.pop_first();            // Option<(K, V)>
map.pop_last();

set.first();                // Option<&T>
set.last();
set.pop_first();            // Option<T>
set.pop_last();
```

## VecDeque<T>

Double-ended queue. O(1) push/pop at both ends.

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<i32> = VecDeque::new();
let deque = VecDeque::from([1, 2, 3]);

// Both ends
deque.push_front(0);
deque.push_back(4);
deque.pop_front();          // Option<T>
deque.pop_back();           // Option<T>
deque.front();              // Option<&T>
deque.back();               // Option<&T>

// Random access
deque[0];
deque.get(0);

// Rotation
deque.rotate_left(2);
deque.rotate_right(2);

// Convert
let vec: Vec<i32> = deque.into();
let (front, back) = deque.as_slices();
deque.make_contiguous();    // &mut [T]
```

## BinaryHeap<T>

Max-heap / priority queue.

```rust
use std::collections::BinaryHeap;

let mut heap = BinaryHeap::new();
let heap = BinaryHeap::from([3, 1, 4, 1, 5]);

heap.push(42);
heap.pop();                 // Option<T> - removes max
heap.peek();                // Option<&T> - view max
heap.peek_mut();            // Option<PeekMut<T>>

// Drain in sorted order
while let Some(max) = heap.pop() {
    println!("{}", max);
}

// Min-heap using Reverse
use std::cmp::Reverse;
let mut min_heap = BinaryHeap::new();
min_heap.push(Reverse(5));
min_heap.push(Reverse(1));
let Reverse(min) = min_heap.pop().unwrap();  // 1
```

## LinkedList<T>

Doubly-linked list. Rarely needed (Vec usually better).

```rust
use std::collections::LinkedList;

let mut list = LinkedList::new();

list.push_front(1);
list.push_back(2);
list.pop_front();
list.pop_back();
list.front();
list.back();

// Append another list
list.append(&mut other);

// Split
let second_half = list.split_off(5);
```

## String

UTF-8 encoded growable string.

```rust
// Create
let mut s = String::new();
let s = String::from("hello");
let s = "hello".to_string();
let s = format!("{} {}", "hello", "world");
let s = String::with_capacity(100);

// Modify
s.push('!');
s.push_str(" world");
s.insert(0, 'H');
s.insert_str(0, "Hello ");
s.pop();                    // Option<char>
s.remove(0);                // char (panics if not char boundary)
s.truncate(5);
s.clear();
s += " suffix";

// Access
s.len();                    // bytes, not chars!
s.is_empty();
s.chars().count();          // character count
s.as_str();                 // &str
s.as_bytes();               // &[u8]
s.chars();                  // iterator of char
s.bytes();                  // iterator of u8

// Slicing (must be at char boundaries!)
&s[0..5];                   // panics if not valid UTF-8 boundary

// Searching
s.contains("ell");
s.starts_with("He");
s.ends_with("lo");
s.find("ll");               // Option<usize>
s.rfind("l");
s.matches("l").count();

// Transformations
s.to_uppercase();
s.to_lowercase();
s.trim();
s.trim_start();
s.trim_end();
s.replace("old", "new");
s.replacen("old", "new", 2);

// Splitting
s.split(' ');               // iterator
s.split_whitespace();
s.lines();
s.split_once(':');          // Option<(&str, &str)>

// Parsing
let n: i32 = s.parse().unwrap();
let n: i32 = s.parse()?;    // in function returning Result
```

## Iterators

```rust
// Creating iterators
vec.iter();                 // &T
vec.iter_mut();             // &mut T
vec.into_iter();            // T (consumes)

// Adapters
iter.map(|x| x * 2)
    .filter(|x| *x > 5)
    .take(10)
    .skip(2)
    .enumerate()            // (index, value)
    .zip(other)
    .chain(other)
    .flatten()              // Iterator<Item=Iterator<T>> -> Iterator<T>
    .flat_map(|x| vec![x, x])
    .peekable()
    .skip_while(|x| **x < 5)
    .take_while(|x| **x < 10)
    .step_by(2)
    .rev()                  // requires DoubleEndedIterator
    .cycle()                // infinite
    .cloned()               // &T -> T (if T: Clone)
    .copied()               // &T -> T (if T: Copy)
    .inspect(|x| println!("{:?}", x))
    .fuse();                // stops after first None

// Consumers
iter.collect::<Vec<_>>();
iter.count();
iter.sum::<i32>();
iter.product::<i32>();
iter.fold(0, |acc, x| acc + x);
iter.reduce(|a, b| a + b);  // Option<T>
iter.for_each(|x| println!("{}", x));
iter.any(|x| x > 5);
iter.all(|x| x > 0);
iter.find(|x| **x > 5);     // Option<&T>
iter.position(|x| *x > 5);  // Option<usize>
iter.max();
iter.min();
iter.max_by_key(|x| x.len());
iter.partition::<Vec<_>, _>(|x| *x > 5);

// Comparison
iter.eq(other);
iter.cmp(other);
iter.partial_cmp(other);
```
