# Cross-Language API Design Patterns

Universal principles for designing clean, maintainable APIs.

## Core Principles

1. **Consistency** - Use consistent naming, patterns, and return types
2. **Least Surprise** - API should behave as users expect
3. **Fail Explicitly** - Return errors rather than null/undefined
4. **Immutability** - Prefer returning new objects over mutation
5. **Composability** - Design for chaining and combination

## Naming Conventions

| Operation    | Verb Prefix | Example                    |
| ------------ | ----------- | -------------------------- |
| Read single  | `get`       | `getUser(id)`              |
| Read list    | `list`      | `listUsers(filter)`        |
| Create       | `create`    | `createUser(data)`         |
| Update       | `update`    | `updateUser(id, data)`     |
| Delete       | `delete`    | `deleteUser(id)`           |
| Check state  | `is`/`has`  | `isActive()`, `hasAccess()`|
| Transform    | `to`        | `toJSON()`, `toString()`   |
| Find/Search  | `find`      | `findByEmail(email)`       |

## Return Types

### TypeScript

```typescript
// Nullable returns - use undefined, not null
function findUser(id: string): User | undefined {
  return users.get(id);
}

// Error cases - use Result type or throw
type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };

function parseConfig(path: string): Result<Config> {
  try {
    const content = fs.readFileSync(path, "utf-8");
    return { ok: true, value: JSON.parse(content) };
  } catch (error) {
    return { ok: false, error: error as Error };
  }
}

// Collections - return empty array, not null
function listUsers(): User[] {
  return users.values() ?? [];
}
```

### Python

```python
from typing import Optional

# Use Optional for nullable
def find_user(user_id: str) -> Optional[User]:
    return users.get(user_id)

# Collections - return empty, not None
def list_users() -> list[User]:
    return list(users.values())

# Complex results - use dataclass or NamedTuple
@dataclass
class SearchResult:
    items: list[User]
    total: int
    has_more: bool

def search_users(query: str, limit: int = 20) -> SearchResult:
    results = database.search(query, limit + 1)
    return SearchResult(
        items=results[:limit],
        total=database.count(query),
        has_more=len(results) > limit
    )
```

### Go

```go
// Multiple returns for errors
func GetUser(id string) (*User, error) {
    user, err := db.FindUser(id)
    if err != nil {
        return nil, fmt.Errorf("get user %s: %w", id, err)
    }
    return user, nil
}

// Boolean returns for existence checks
func (s *Store) Has(key string) bool {
    _, exists := s.data[key]
    return exists
}

// Slices - return empty slice, not nil
func ListUsers() []User {
    if len(users) == 0 {
        return []User{}
    }
    return users
}
```

## Builder Pattern

### TypeScript

```typescript
class QueryBuilder {
  private filters: Filter[] = [];
  private orderBy?: string;
  private limitValue?: number;

  where(field: string, op: string, value: unknown): this {
    this.filters.push({ field, op, value });
    return this;
  }

  order(field: string): this {
    this.orderBy = field;
    return this;
  }

  limit(n: number): this {
    this.limitValue = n;
    return this;
  }

  build(): Query {
    return new Query(this.filters, this.orderBy, this.limitValue);
  }
}

// Usage
const query = new QueryBuilder()
  .where("status", "=", "active")
  .where("age", ">", 18)
  .order("name")
  .limit(10)
  .build();
```

### Python

```python
from dataclasses import dataclass, field
from typing import Self

@dataclass
class QueryBuilder:
    _filters: list[tuple] = field(default_factory=list)
    _order_by: str | None = None
    _limit: int | None = None

    def where(self, field: str, op: str, value: Any) -> Self:
        self._filters.append((field, op, value))
        return self

    def order(self, field: str) -> Self:
        self._order_by = field
        return self

    def limit(self, n: int) -> Self:
        self._limit = n
        return self

    def build(self) -> Query:
        return Query(self._filters, self._order_by, self._limit)

# Usage
query = (QueryBuilder()
    .where("status", "=", "active")
    .where("age", ">", 18)
    .order("name")
    .limit(10)
    .build())
```

## Options Pattern

### Go

```go
// Functional options pattern
type ServerOption func(*Server)

func WithPort(port int) ServerOption {
    return func(s *Server) {
        s.port = port
    }
}

func WithTimeout(d time.Duration) ServerOption {
    return func(s *Server) {
        s.timeout = d
    }
}

func NewServer(opts ...ServerOption) *Server {
    s := &Server{
        port:    8080,    // default
        timeout: 30 * time.Second,
    }
    for _, opt := range opts {
        opt(s)
    }
    return s
}

// Usage
server := NewServer(
    WithPort(3000),
    WithTimeout(60 * time.Second),
)
```

### TypeScript

```typescript
interface ServerOptions {
  port?: number;
  timeout?: number;
  maxConnections?: number;
}

class Server {
  private port: number;
  private timeout: number;
  private maxConnections: number;

  constructor(options: ServerOptions = {}) {
    this.port = options.port ?? 8080;
    this.timeout = options.timeout ?? 30000;
    this.maxConnections = options.maxConnections ?? 100;
  }
}

// Usage
const server = new Server({ port: 3000, timeout: 60000 });
```

## Anti-Patterns

### Don't Return Different Types

```typescript
// BAD - Inconsistent return type
function getUser(id: string): User | string | null {
  if (!id) return "Invalid ID"; // String error
  const user = users.get(id);
  return user ?? null;
}

// GOOD - Consistent return type
function getUser(id: string): User | undefined {
  if (!id) throw new ValidationError("ID required");
  return users.get(id);
}
```

### Don't Use Boolean Parameters

```python
# BAD - What does True mean?
def fetch_users(True, False, True):
    pass

# GOOD - Named parameters or options
def fetch_users(
    include_inactive: bool = False,
    include_deleted: bool = False,
    fetch_relations: bool = True
):
    pass
```

### Don't Mutate Input Parameters

```go
// BAD - Mutates input
func ProcessItems(items []Item) {
    for i := range items {
        items[i].Processed = true  // Modifies original!
    }
}

// GOOD - Return new slice
func ProcessItems(items []Item) []Item {
    result := make([]Item, len(items))
    for i, item := range items {
        result[i] = Item{
            ID:        item.ID,
            Processed: true,
        }
    }
    return result
}
```
