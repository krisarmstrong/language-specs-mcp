# Java Collections Framework

## Interfaces Hierarchy

```
Collection
├── List (ordered, duplicates allowed)
├── Set (no duplicates)
│   └── SortedSet
│       └── NavigableSet
└── Queue
    └── Deque

Map (not Collection)
├── SortedMap
│   └── NavigableMap
```

## List Implementations

### ArrayList

Dynamic array. Fast random access, slow insert/delete in middle.

```java
List<String> list = new ArrayList<>();
List<String> sized = new ArrayList<>(100);  // initial capacity
List<String> from = new ArrayList<>(otherCollection);

// Operations - O(1) amortized
list.add("item");           // append
list.get(0);                // random access
list.set(0, "new");         // replace
list.size();

// Operations - O(n)
list.add(0, "first");       // insert at index
list.remove(0);             // remove at index
list.contains("item");      // search
list.indexOf("item");

// Bulk operations
list.addAll(otherList);
list.removeIf(s -> s.isEmpty());
list.replaceAll(String::toUpperCase);
list.sort(Comparator.naturalOrder());
```

### LinkedList

Doubly-linked list. Fast insert/delete, slow random access.

```java
LinkedList<String> list = new LinkedList<>();

// List operations
list.add("item");
list.get(0);                // O(n)!

// Deque operations (fast)
list.addFirst("first");     // O(1)
list.addLast("last");       // O(1)
list.removeFirst();         // O(1)
list.removeLast();          // O(1)
list.peekFirst();
list.peekLast();
```

### CopyOnWriteArrayList

Thread-safe, creates copy on modification.

```java
List<String> list = new CopyOnWriteArrayList<>();

// Thread-safe iteration (snapshot)
for (String s : list) {
    // safe even if another thread modifies
}

// Best for read-heavy, write-rare scenarios
```

## Set Implementations

### HashSet

Hash table. O(1) operations, no order guarantee.

```java
Set<String> set = new HashSet<>();
Set<String> sized = new HashSet<>(100);  // initial capacity
Set<String> from = new HashSet<>(collection);

set.add("item");            // O(1)
set.remove("item");         // O(1)
set.contains("item");       // O(1)
set.size();

// Set operations
set1.addAll(set2);          // union
set1.retainAll(set2);       // intersection
set1.removeAll(set2);       // difference
```

### LinkedHashSet

Hash table + linked list. Maintains insertion order.

```java
Set<String> set = new LinkedHashSet<>();
set.add("first");
set.add("second");
// Iteration order: first, second
```

### TreeSet

Red-black tree. Sorted order, O(log n) operations.

```java
Set<String> set = new TreeSet<>();
Set<String> custom = new TreeSet<>(comparator);
NavigableSet<String> nav = new TreeSet<>();

// Sorted operations
nav.first();                // smallest
nav.last();                 // largest
nav.lower("c");             // greatest element < "c"
nav.floor("c");             // greatest element <= "c"
nav.ceiling("c");           // smallest element >= "c"
nav.higher("c");            // smallest element > "c"
nav.headSet("c");           // elements < "c"
nav.tailSet("c");           // elements >= "c"
nav.subSet("a", "c");       // elements in [a, c)
nav.descendingSet();        // reverse order view
```

### EnumSet

Bit vector for enums. Very fast and compact.

```java
enum Day { MON, TUE, WED, THU, FRI, SAT, SUN }

Set<Day> weekend = EnumSet.of(Day.SAT, Day.SUN);
Set<Day> weekdays = EnumSet.range(Day.MON, Day.FRI);
Set<Day> all = EnumSet.allOf(Day.class);
Set<Day> none = EnumSet.noneOf(Day.class);
Set<Day> complement = EnumSet.complementOf(weekend);
```

## Map Implementations

### HashMap

Hash table. O(1) operations, no order guarantee.

```java
Map<String, Integer> map = new HashMap<>();
Map<String, Integer> sized = new HashMap<>(100);

// Basic operations
map.put("key", 42);
map.get("key");             // null if absent
map.getOrDefault("key", 0);
map.remove("key");
map.containsKey("key");
map.containsValue(42);
map.size();

// Compute operations
map.putIfAbsent("key", 42);
map.computeIfAbsent("key", k -> compute(k));
map.computeIfPresent("key", (k, v) -> v + 1);
map.compute("key", (k, v) -> v == null ? 1 : v + 1);
map.merge("key", 1, Integer::sum);

// Iteration
map.forEach((k, v) -> System.out.println(k + ": " + v));
for (Map.Entry<String, Integer> e : map.entrySet()) { }
for (String key : map.keySet()) { }
for (Integer value : map.values()) { }
```

### LinkedHashMap

Maintains insertion order or access order.

```java
// Insertion order (default)
Map<String, Integer> map = new LinkedHashMap<>();

// Access order (for LRU cache)
Map<String, Integer> lru = new LinkedHashMap<>(16, 0.75f, true);

// LRU cache implementation
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int maxSize;
    
    LRUCache(int maxSize) {
        super(16, 0.75f, true);
        this.maxSize = maxSize;
    }
    
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > maxSize;
    }
}
```

### TreeMap

Red-black tree. Sorted keys, O(log n) operations.

```java
NavigableMap<String, Integer> map = new TreeMap<>();
NavigableMap<String, Integer> custom = new TreeMap<>(comparator);

// Sorted operations
map.firstKey();
map.lastKey();
map.lowerKey("c");
map.floorKey("c");
map.ceilingKey("c");
map.higherKey("c");
map.firstEntry();
map.pollFirstEntry();       // remove and return
map.headMap("c");
map.tailMap("c");
map.subMap("a", "c");
map.descendingMap();
```

### ConcurrentHashMap

Thread-safe, high concurrency.

```java
ConcurrentMap<String, Integer> map = new ConcurrentHashMap<>();

// Atomic operations
map.putIfAbsent("key", 42);
map.remove("key", 42);      // remove only if value matches
map.replace("key", 42, 43); // replace only if value matches
map.compute("key", (k, v) -> v == null ? 1 : v + 1);

// Bulk operations (parallel)
map.forEach(1000, (k, v) -> process(k, v));
long sum = map.reduceValues(1000, v -> (long) v, Long::sum);
```

### EnumMap

Array-backed map for enum keys.

```java
Map<Day, String> schedule = new EnumMap<>(Day.class);
schedule.put(Day.MON, "Work");
```

## Queue Implementations

### ArrayDeque

Resizable array deque. Fast at both ends.

```java
Deque<String> deque = new ArrayDeque<>();

// Queue operations (FIFO)
deque.offer("item");        // add to tail
deque.poll();               // remove from head
deque.peek();               // view head

// Stack operations (LIFO)
deque.push("item");         // add to head
deque.pop();                // remove from head

// Deque operations
deque.offerFirst("first");
deque.offerLast("last");
deque.pollFirst();
deque.pollLast();
```

### PriorityQueue

Binary heap. Elements ordered by comparator.

```java
Queue<Integer> minHeap = new PriorityQueue<>();
Queue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
Queue<Task> byPriority = new PriorityQueue<>(Comparator.comparing(Task::priority));

minHeap.offer(3);
minHeap.offer(1);
minHeap.offer(2);
minHeap.poll();             // returns 1 (smallest)

// O(log n) for offer/poll, O(1) for peek
```

### BlockingQueue

Thread-safe queues for producer-consumer.

```java
BlockingQueue<Task> queue = new LinkedBlockingQueue<>(100);  // bounded
BlockingQueue<Task> unbounded = new LinkedBlockingQueue<>();
BlockingQueue<Task> array = new ArrayBlockingQueue<>(100);

// Blocking operations
queue.put(task);            // blocks if full
Task t = queue.take();      // blocks if empty

// Timed operations
queue.offer(task, 1, TimeUnit.SECONDS);
Task t = queue.poll(1, TimeUnit.SECONDS);
```

## Utility Methods (Collections class)

```java
// Immutable wrappers
List<String> unmodifiable = Collections.unmodifiableList(list);
Map<K, V> unmodMap = Collections.unmodifiableMap(map);

// Synchronized wrappers
List<String> syncList = Collections.synchronizedList(list);

// Singleton collections
List<String> single = Collections.singletonList("item");
Set<String> singleSet = Collections.singleton("item");
Map<K, V> singleMap = Collections.singletonMap(key, value);

// Empty collections
List<String> empty = Collections.emptyList();
Set<String> emptySet = Collections.emptySet();
Map<K, V> emptyMap = Collections.emptyMap();

// Algorithms
Collections.sort(list);
Collections.sort(list, comparator);
Collections.reverse(list);
Collections.shuffle(list);
Collections.binarySearch(sortedList, key);
Collections.min(collection);
Collections.max(collection);
Collections.frequency(collection, element);
Collections.disjoint(c1, c2);  // true if no common elements
Collections.fill(list, value);
Collections.copy(dest, src);
Collections.nCopies(n, element);
```

## Immutable Collections (Java 9+)

```java
// Factory methods
List<String> list = List.of("a", "b", "c");
Set<String> set = Set.of("a", "b", "c");
Map<String, Integer> map = Map.of("a", 1, "b", 2);
Map<String, Integer> mapEntries = Map.ofEntries(
    Map.entry("a", 1),
    Map.entry("b", 2)
);

// Copy to immutable
List<String> copy = List.copyOf(mutableList);
Set<String> setCopy = Set.copyOf(mutableSet);
Map<K, V> mapCopy = Map.copyOf(mutableMap);

// Collectors
List<String> collected = stream.collect(Collectors.toUnmodifiableList());
Set<String> setCollected = stream.collect(Collectors.toUnmodifiableSet());
```
