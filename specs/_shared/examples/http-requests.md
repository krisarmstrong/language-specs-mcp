# HTTP Request Examples

Common patterns for making HTTP requests across languages.

## GET Request

### TypeScript/JavaScript

```typescript
// Using fetch (browser/Node 18+)
async function getUser(id: string): Promise<User> {
  const response = await fetch(`https://api.example.com/users/${id}`);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }
  return response.json();
}

// With headers and error handling
async function fetchWithAuth(url: string, token: string): Promise<unknown> {
  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Request failed: ${error}`);
  }

  return response.json();
}
```

### Python

```python
import httpx

async def get_user(user_id: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status()
        return response.json()

# Synchronous version
def get_user_sync(user_id: str) -> dict:
    response = httpx.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

# With authentication
async def fetch_with_auth(url: str, token: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers={"Authorization": f"Bearer {token}"}
        )
        response.raise_for_status()
        return response.json()
```

### Go

```go
import (
    "encoding/json"
    "fmt"
    "io"
    "net/http"
)

func GetUser(id string) (*User, error) {
    resp, err := http.Get(fmt.Sprintf("https://api.example.com/users/%s", id))
    if err != nil {
        return nil, fmt.Errorf("request failed: %w", err)
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        body, _ := io.ReadAll(resp.Body)
        return nil, fmt.Errorf("HTTP %d: %s", resp.StatusCode, body)
    }

    var user User
    if err := json.NewDecoder(resp.Body).Decode(&user); err != nil {
        return nil, fmt.Errorf("decode response: %w", err)
    }

    return &user, nil
}

// With context and custom client
func FetchWithAuth(ctx context.Context, url, token string) ([]byte, error) {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }
    req.Header.Set("Authorization", "Bearer "+token)

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
use reqwest::Client;
use serde::Deserialize;

#[derive(Deserialize)]
struct User {
    id: String,
    name: String,
}

async fn get_user(id: &str) -> Result<User, reqwest::Error> {
    let url = format!("https://api.example.com/users/{}", id);
    let user = reqwest::get(&url).await?.json::<User>().await?;
    Ok(user)
}

// With custom client and headers
async fn fetch_with_auth(url: &str, token: &str) -> Result<String, reqwest::Error> {
    let client = Client::new();
    let response = client
        .get(url)
        .header("Authorization", format!("Bearer {}", token))
        .send()
        .await?
        .text()
        .await?;
    Ok(response)
}
```

## POST Request

### TypeScript

```typescript
async function createUser(data: CreateUserInput): Promise<User> {
  const response = await fetch("https://api.example.com/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error(`Failed to create user: ${response.statusText}`);
  }

  return response.json();
}
```

### Python

```python
async def create_user(data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.example.com/users",
            json=data
        )
        response.raise_for_status()
        return response.json()
```

### Go

```go
func CreateUser(data CreateUserInput) (*User, error) {
    body, err := json.Marshal(data)
    if err != nil {
        return nil, err
    }

    resp, err := http.Post(
        "https://api.example.com/users",
        "application/json",
        bytes.NewReader(body),
    )
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    var user User
    if err := json.NewDecoder(resp.Body).Decode(&user); err != nil {
        return nil, err
    }

    return &user, nil
}
```

## With Retry Logic

### TypeScript

```typescript
async function fetchWithRetry(
  url: string,
  maxRetries = 3,
  delayMs = 1000
): Promise<Response> {
  let lastError: Error | undefined;

  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url);
      if (response.ok || response.status < 500) {
        return response;
      }
      throw new Error(`HTTP ${response.status}`);
    } catch (error) {
      lastError = error as Error;
      if (i < maxRetries - 1) {
        await new Promise((resolve) => setTimeout(resolve, delayMs * (i + 1)));
      }
    }
  }

  throw lastError;
}
```

### Python

```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
async def fetch_with_retry(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
```

### Go

```go
func FetchWithRetry(ctx context.Context, url string, maxRetries int) ([]byte, error) {
    var lastErr error

    for i := 0; i < maxRetries; i++ {
        req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
        if err != nil {
            return nil, err
        }

        resp, err := http.DefaultClient.Do(req)
        if err != nil {
            lastErr = err
            time.Sleep(time.Duration(i+1) * time.Second)
            continue
        }

        body, err := io.ReadAll(resp.Body)
        resp.Body.Close()

        if resp.StatusCode < 500 {
            return body, nil
        }

        lastErr = fmt.Errorf("HTTP %d", resp.StatusCode)
        time.Sleep(time.Duration(i+1) * time.Second)
    }

    return nil, fmt.Errorf("max retries exceeded: %w", lastErr)
}
```
