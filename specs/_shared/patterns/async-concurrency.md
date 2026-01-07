# Cross-Language Async & Concurrency Patterns

Universal principles for handling asynchronous operations and concurrency.

## Core Principles

1. **Prefer Async/Await** - More readable than callbacks or raw promises
2. **Handle All Errors** - Unhandled rejections crash applications
3. **Avoid Shared Mutable State** - Use message passing or immutability
4. **Use Cancellation** - Support timeouts and cancellation tokens
5. **Limit Concurrency** - Don't spawn unlimited parallel operations

## Language Implementations

### TypeScript/JavaScript

```typescript
// Parallel execution
async function fetchAll(ids: string[]): Promise<User[]> {
  const promises = ids.map((id) => fetchUser(id));
  return Promise.all(promises);
}

// Controlled concurrency
async function fetchAllLimited(ids: string[], limit = 5): Promise<User[]> {
  const results: User[] = [];

  for (let i = 0; i < ids.length; i += limit) {
    const batch = ids.slice(i, i + limit);
    const batchResults = await Promise.all(batch.map((id) => fetchUser(id)));
    results.push(...batchResults);
  }

  return results;
}

// With cancellation
async function fetchWithTimeout(url: string, timeoutMs: number): Promise<Response> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  try {
    return await fetch(url, { signal: controller.signal });
  } finally {
    clearTimeout(timeout);
  }
}

// Race pattern
async function fetchWithFallback(primary: string, fallback: string): Promise<Data> {
  try {
    return await Promise.race([fetchData(primary), timeout(5000)]);
  } catch {
    return fetchData(fallback);
  }
}
```

### Python

```python
import asyncio
from typing import TypeVar
from asyncio import Semaphore

T = TypeVar('T')

# Parallel execution
async def fetch_all(ids: list[str]) -> list[User]:
    tasks = [fetch_user(id) for id in ids]
    return await asyncio.gather(*tasks)

# Controlled concurrency with semaphore
async def fetch_all_limited(ids: list[str], limit: int = 5) -> list[User]:
    semaphore = Semaphore(limit)

    async def fetch_with_limit(id: str) -> User:
        async with semaphore:
            return await fetch_user(id)

    tasks = [fetch_with_limit(id) for id in ids]
    return await asyncio.gather(*tasks)

# With timeout
async def fetch_with_timeout(url: str, timeout: float) -> bytes:
    async with asyncio.timeout(timeout):
        return await fetch_data(url)

# Cancellation handling
async def long_running_task(cancel_event: asyncio.Event):
    while not cancel_event.is_set():
        await do_work()
        await asyncio.sleep(0.1)
```

### Go

```go
// Parallel execution with WaitGroup
func fetchAll(ids []string) ([]User, error) {
    var wg sync.WaitGroup
    users := make([]User, len(ids))
    errs := make([]error, len(ids))

    for i, id := range ids {
        wg.Add(1)
        go func(i int, id string) {
            defer wg.Done()
            users[i], errs[i] = fetchUser(id)
        }(i, id)
    }

    wg.Wait()

    for _, err := range errs {
        if err != nil {
            return nil, err
        }
    }
    return users, nil
}

// Controlled concurrency with worker pool
func fetchAllLimited(ctx context.Context, ids []string, limit int) ([]User, error) {
    sem := make(chan struct{}, limit)
    results := make(chan User, len(ids))
    errChan := make(chan error, 1)

    var wg sync.WaitGroup
    for _, id := range ids {
        wg.Add(1)
        go func(id string) {
            defer wg.Done()
            sem <- struct{}{}
            defer func() { <-sem }()

            user, err := fetchUser(ctx, id)
            if err != nil {
                select {
                case errChan <- err:
                default:
                }
                return
            }
            results <- user
        }(id)
    }

    go func() {
        wg.Wait()
        close(results)
    }()

    var users []User
    for user := range results {
        users = append(users, user)
    }

    select {
    case err := <-errChan:
        return nil, err
    default:
        return users, nil
    }
}

// With context cancellation
func fetchWithTimeout(ctx context.Context, url string, timeout time.Duration) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, timeout)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    return io.ReadAll(resp.Body)
}
```

### Rust

```rust
use tokio::sync::Semaphore;
use std::sync::Arc;

// Parallel execution
async fn fetch_all(ids: Vec<String>) -> Result<Vec<User>, Error> {
    let futures = ids.into_iter().map(|id| fetch_user(id));
    futures::future::try_join_all(futures).await
}

// Controlled concurrency
async fn fetch_all_limited(ids: Vec<String>, limit: usize) -> Result<Vec<User>, Error> {
    let semaphore = Arc::new(Semaphore::new(limit));
    let mut handles = Vec::new();

    for id in ids {
        let sem = semaphore.clone();
        let handle = tokio::spawn(async move {
            let _permit = sem.acquire().await.unwrap();
            fetch_user(id).await
        });
        handles.push(handle);
    }

    let mut results = Vec::new();
    for handle in handles {
        results.push(handle.await??);
    }
    Ok(results)
}

// With timeout
async fn fetch_with_timeout(url: &str, timeout: Duration) -> Result<Bytes, Error> {
    tokio::time::timeout(timeout, fetch_data(url))
        .await
        .map_err(|_| Error::Timeout)?
}
```

## Anti-Patterns

### Don't Block the Event Loop

```typescript
// BAD - Blocks event loop
function sleep(ms: number) {
  const end = Date.now() + ms;
  while (Date.now() < end) {} // Blocking!
}

// GOOD - Non-blocking
function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```

### Don't Ignore Errors in Fire-and-Forget

```python
# BAD - Unhandled rejection
async def save_metrics():
    await database.save(metrics)  # Error lost!

asyncio.create_task(save_metrics())

# GOOD - Handle errors
async def save_metrics():
    try:
        await database.save(metrics)
    except Exception as e:
        logger.error(f"Failed to save metrics: {e}")

asyncio.create_task(save_metrics())
```

### Don't Share Mutable State Without Synchronization

```go
// BAD - Race condition
var counter int

func increment() {
    counter++ // Not atomic!
}

// GOOD - Use atomic or mutex
var counter atomic.Int64

func increment() {
    counter.Add(1)
}
```
