# Java Concurrency (java.util.concurrent)

## Executors

### ExecutorService

```java
// Fixed thread pool
ExecutorService fixed = Executors.newFixedThreadPool(4);

// Cached (grows as needed)
ExecutorService cached = Executors.newCachedThreadPool();

// Single thread
ExecutorService single = Executors.newSingleThreadExecutor();

// Scheduled
ScheduledExecutorService scheduled = Executors.newScheduledThreadPool(2);

// Virtual threads (Java 21+)
ExecutorService virtual = Executors.newVirtualThreadPerTaskExecutor();

// Custom
ExecutorService custom = new ThreadPoolExecutor(
    4,                      // core pool size
    8,                      // max pool size
    60L, TimeUnit.SECONDS,  // keep-alive time
    new LinkedBlockingQueue<>(100),  // work queue
    new ThreadPoolExecutor.CallerRunsPolicy()  // rejection policy
);

// Submit tasks
executor.submit(() -> doWork());
Future<String> future = executor.submit(() -> compute());

// Shutdown
executor.shutdown();                    // graceful
executor.shutdownNow();                 // interrupt all
executor.awaitTermination(60, TimeUnit.SECONDS);
```

### Future

```java
Future<String> future = executor.submit(() -> compute());

// Check status
future.isDone();
future.isCancelled();

// Get result (blocking)
String result = future.get();
String result = future.get(5, TimeUnit.SECONDS);  // with timeout

// Cancel
future.cancel(true);  // may interrupt
```

### CompletableFuture

```java
// Create
CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> fetch());
CompletableFuture<Void> cf = CompletableFuture.runAsync(() -> doWork());
CompletableFuture<String> cf = CompletableFuture.completedFuture("value");

// Transform
cf.thenApply(s -> s.toUpperCase())
  .thenAccept(System.out::println)
  .thenRun(() -> cleanup());

// Async variants (run in executor)
cf.thenApplyAsync(s -> process(s), executor);

// Compose (flatMap)
cf.thenCompose(user -> fetchOrders(user));

// Combine
cf1.thenCombine(cf2, (r1, r2) -> combine(r1, r2));
cf1.thenAcceptBoth(cf2, (r1, r2) -> use(r1, r2));
cf1.runAfterBoth(cf2, () -> afterBoth());

// Either (whichever completes first)
cf1.applyToEither(cf2, s -> process(s));
cf1.acceptEither(cf2, s -> use(s));
cf1.runAfterEither(cf2, () -> afterEither());

// Exception handling
cf.exceptionally(ex -> defaultValue)
  .handle((result, ex) -> ex != null ? defaultValue : result)
  .whenComplete((result, ex) -> log(result, ex));

// Combine multiple
CompletableFuture.allOf(cf1, cf2, cf3).join();
CompletableFuture.anyOf(cf1, cf2, cf3).thenAccept(first -> use(first));
```

## Synchronizers

### CountDownLatch

Wait for N events.

```java
CountDownLatch latch = new CountDownLatch(3);

// Workers count down
executor.submit(() -> {
    doWork();
    latch.countDown();
});

// Main thread waits
latch.await();
latch.await(5, TimeUnit.SECONDS);
```

### CyclicBarrier

Wait for N threads, then release all. Reusable.

```java
CyclicBarrier barrier = new CyclicBarrier(3, () -> {
    // Action when all threads arrive
    System.out.println("All threads ready");
});

// Each thread waits at barrier
barrier.await();

// Can be reused for next phase
barrier.await();
```

### Semaphore

Limit concurrent access.

```java
Semaphore semaphore = new Semaphore(3);  // 3 permits

semaphore.acquire();        // blocks if no permits
try {
    accessResource();
} finally {
    semaphore.release();
}

// Try acquire (non-blocking)
if (semaphore.tryAcquire()) {
    try { accessResource(); }
    finally { semaphore.release(); }
}
```

### Phaser

Flexible barrier for phased computations.

```java
Phaser phaser = new Phaser(3);  // 3 parties

// Each thread
phaser.arriveAndAwaitAdvance();  // phase 1
doPhase1Work();
phaser.arriveAndAwaitAdvance();  // phase 2
doPhase2Work();
phaser.arriveAndDeregister();    // done
```

### Exchanger

Exchange data between two threads.

```java
Exchanger<String> exchanger = new Exchanger<>();

// Thread 1
String data = exchanger.exchange("from thread 1");

// Thread 2
String data = exchanger.exchange("from thread 2");
```

## Locks

### ReentrantLock

```java
ReentrantLock lock = new ReentrantLock();
ReentrantLock fair = new ReentrantLock(true);  // fair ordering

lock.lock();
try {
    // critical section
} finally {
    lock.unlock();
}

// Try lock
if (lock.tryLock()) {
    try { /* ... */ }
    finally { lock.unlock(); }
}

// Timed try
if (lock.tryLock(1, TimeUnit.SECONDS)) {
    try { /* ... */ }
    finally { lock.unlock(); }
}

// Interruptible
lock.lockInterruptibly();
```

### ReadWriteLock

```java
ReadWriteLock rwLock = new ReentrantReadWriteLock();
Lock readLock = rwLock.readLock();
Lock writeLock = rwLock.writeLock();

// Multiple readers allowed
readLock.lock();
try { return data; }
finally { readLock.unlock(); }

// Exclusive write
writeLock.lock();
try { data = newValue; }
finally { writeLock.unlock(); }
```

### StampedLock (Java 8+)

Optimistic read support.

```java
StampedLock lock = new StampedLock();

// Optimistic read (no blocking)
long stamp = lock.tryOptimisticRead();
double x = this.x, y = this.y;
if (!lock.validate(stamp)) {
    // Optimistic read failed, use pessimistic
    stamp = lock.readLock();
    try {
        x = this.x;
        y = this.y;
    } finally {
        lock.unlockRead(stamp);
    }
}

// Write lock
long stamp = lock.writeLock();
try {
    this.x = newX;
    this.y = newY;
} finally {
    lock.unlockWrite(stamp);
}
```

## Atomic Variables

```java
AtomicInteger counter = new AtomicInteger(0);
counter.get();
counter.set(10);
counter.incrementAndGet();      // ++counter
counter.getAndIncrement();      // counter++
counter.addAndGet(5);           // counter += 5
counter.compareAndSet(10, 20);  // CAS

AtomicLong longCounter = new AtomicLong();
AtomicBoolean flag = new AtomicBoolean();
AtomicReference<String> ref = new AtomicReference<>("initial");

// Update with function
counter.updateAndGet(x -> x * 2);
counter.accumulateAndGet(5, Integer::sum);

// LongAdder (better for high contention)
LongAdder adder = new LongAdder();
adder.increment();
adder.add(5);
long sum = adder.sum();

// LongAccumulator (custom operation)
LongAccumulator max = new LongAccumulator(Long::max, Long.MIN_VALUE);
max.accumulate(42);
long result = max.get();
```

## Concurrent Collections

```java
// ConcurrentHashMap
ConcurrentMap<String, Integer> map = new ConcurrentHashMap<>();
map.putIfAbsent("key", 1);
map.compute("key", (k, v) -> v == null ? 1 : v + 1);

// CopyOnWriteArrayList
List<String> list = new CopyOnWriteArrayList<>();

// CopyOnWriteArraySet
Set<String> set = new CopyOnWriteArraySet<>();

// ConcurrentLinkedQueue
Queue<String> queue = new ConcurrentLinkedQueue<>();

// ConcurrentLinkedDeque
Deque<String> deque = new ConcurrentLinkedDeque<>();

// ConcurrentSkipListMap (sorted, concurrent TreeMap)
NavigableMap<String, Integer> skipMap = new ConcurrentSkipListMap<>();

// ConcurrentSkipListSet (sorted, concurrent TreeSet)
NavigableSet<String> skipSet = new ConcurrentSkipListSet<>();
```

## Virtual Threads (Java 21+)

```java
// Start virtual thread
Thread vt = Thread.startVirtualThread(() -> doWork());

// Create with builder
Thread vt = Thread.ofVirtual()
    .name("my-virtual-thread")
    .start(() -> doWork());

// Executor with virtual threads
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> doWork());
}

// Structured concurrency (preview)
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Future<User> user = scope.fork(() -> fetchUser());
    Future<List<Order>> orders = scope.fork(() -> fetchOrders());
    
    scope.join();           // wait for both
    scope.throwIfFailed();  // propagate exceptions
    
    return new Response(user.resultNow(), orders.resultNow());
}
```
