# Cross-Language Database Query Patterns

Safe, efficient database access patterns across languages.

## Parameterized Queries (SQL Injection Prevention)

### Python (SQLAlchemy)

```python
from sqlalchemy import select, text
from sqlalchemy.orm import Session

# ORM - Automatically parameterized
def get_user_by_email(session: Session, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    return session.scalars(stmt).first()

# Raw SQL - Use text() with bound parameters
def search_users(session: Session, name_pattern: str) -> list[User]:
    stmt = text("SELECT * FROM users WHERE name ILIKE :pattern")
    result = session.execute(stmt, {"pattern": f"%{name_pattern}%"})
    return result.fetchall()

# NEVER do this
query = f"SELECT * FROM users WHERE email = '{email}'"  # SQL INJECTION!
```

### TypeScript (Prisma)

```typescript
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

// Prisma - Automatically parameterized
async function getUserByEmail(email: string) {
  return prisma.user.findUnique({
    where: { email },
  })
}

// Raw queries - Use $queryRaw with template literal
async function searchUsers(namePattern: string) {
  return prisma.$queryRaw`
    SELECT * FROM users WHERE name ILIKE ${`%${namePattern}%`}
  `
}

// NEVER concatenate user input
const query = `SELECT * FROM users WHERE email = '${email}'` // SQL INJECTION!
```

### Go (database/sql)

```go
import (
    "database/sql"
    _ "github.com/lib/pq"
)

// Parameterized query with positional placeholders
func GetUserByEmail(db *sql.DB, email string) (*User, error) {
    var user User
    err := db.QueryRow(
        "SELECT id, email, name FROM users WHERE email = $1",
        email,
    ).Scan(&user.ID, &user.Email, &user.Name)
    if err == sql.ErrNoRows {
        return nil, nil
    }
    return &user, err
}

// Multiple parameters
func SearchUsers(db *sql.DB, name string, limit int) ([]User, error) {
    rows, err := db.Query(
        "SELECT id, email, name FROM users WHERE name ILIKE $1 LIMIT $2",
        "%"+name+"%",
        limit,
    )
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    var users []User
    for rows.Next() {
        var u User
        if err := rows.Scan(&u.ID, &u.Email, &u.Name); err != nil {
            return nil, err
        }
        users = append(users, u)
    }
    return users, rows.Err()
}
```

### Rust (sqlx)

```rust
use sqlx::{PgPool, FromRow};

#[derive(FromRow)]
struct User {
    id: i32,
    email: String,
    name: String,
}

// Compile-time checked queries
async fn get_user_by_email(pool: &PgPool, email: &str) -> Result<Option<User>, sqlx::Error> {
    sqlx::query_as!(
        User,
        "SELECT id, email, name FROM users WHERE email = $1",
        email
    )
    .fetch_optional(pool)
    .await
}

// Dynamic queries with query builder
async fn search_users(pool: &PgPool, name: &str, limit: i64) -> Result<Vec<User>, sqlx::Error> {
    sqlx::query_as::<_, User>(
        "SELECT id, email, name FROM users WHERE name ILIKE $1 LIMIT $2"
    )
    .bind(format!("%{}%", name))
    .bind(limit)
    .fetch_all(pool)
    .await
}
```

### Java (JDBC / JPA)

```java
// JDBC - PreparedStatement
public User getUserByEmail(Connection conn, String email) throws SQLException {
    String sql = "SELECT id, email, name FROM users WHERE email = ?";
    try (PreparedStatement stmt = conn.prepareStatement(sql)) {
        stmt.setString(1, email);
        try (ResultSet rs = stmt.executeQuery()) {
            if (rs.next()) {
                return new User(
                    rs.getLong("id"),
                    rs.getString("email"),
                    rs.getString("name")
                );
            }
            return null;
        }
    }
}

// JPA - Named parameters
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    @Query("SELECT u FROM User u WHERE u.email = :email")
    Optional<User> findByEmail(@Param("email") String email);

    @Query("SELECT u FROM User u WHERE u.name LIKE %:pattern%")
    List<User> searchByName(@Param("pattern") String pattern);
}
```

## Transaction Management

### Python

```python
from sqlalchemy.orm import Session
from contextlib import contextmanager

@contextmanager
def transaction(session: Session):
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise

# Usage
def transfer_funds(session: Session, from_id: int, to_id: int, amount: Decimal):
    with transaction(session):
        from_account = session.get(Account, from_id)
        to_account = session.get(Account, to_id)

        if from_account.balance < amount:
            raise InsufficientFundsError()

        from_account.balance -= amount
        to_account.balance += amount
```

### TypeScript (Prisma)

```typescript
async function transferFunds(fromId: string, toId: string, amount: number) {
  return prisma.$transaction(async (tx) => {
    const fromAccount = await tx.account.findUniqueOrThrow({
      where: { id: fromId },
    })

    if (fromAccount.balance < amount) {
      throw new InsufficientFundsError()
    }

    await tx.account.update({
      where: { id: fromId },
      data: { balance: { decrement: amount } },
    })

    await tx.account.update({
      where: { id: toId },
      data: { balance: { increment: amount } },
    })
  })
}
```

### Go

```go
func TransferFunds(db *sql.DB, fromID, toID int64, amount float64) error {
    tx, err := db.Begin()
    if err != nil {
        return err
    }
    defer tx.Rollback() // No-op if committed

    var balance float64
    err = tx.QueryRow("SELECT balance FROM accounts WHERE id = $1 FOR UPDATE", fromID).Scan(&balance)
    if err != nil {
        return err
    }

    if balance < amount {
        return ErrInsufficientFunds
    }

    _, err = tx.Exec("UPDATE accounts SET balance = balance - $1 WHERE id = $2", amount, fromID)
    if err != nil {
        return err
    }

    _, err = tx.Exec("UPDATE accounts SET balance = balance + $1 WHERE id = $2", amount, toID)
    if err != nil {
        return err
    }

    return tx.Commit()
}
```

### Rust

```rust
async fn transfer_funds(
    pool: &PgPool,
    from_id: i64,
    to_id: i64,
    amount: Decimal,
) -> Result<(), AppError> {
    let mut tx = pool.begin().await?;

    let from_balance: Decimal = sqlx::query_scalar(
        "SELECT balance FROM accounts WHERE id = $1 FOR UPDATE"
    )
    .bind(from_id)
    .fetch_one(&mut *tx)
    .await?;

    if from_balance < amount {
        return Err(AppError::InsufficientFunds);
    }

    sqlx::query("UPDATE accounts SET balance = balance - $1 WHERE id = $2")
        .bind(amount)
        .bind(from_id)
        .execute(&mut *tx)
        .await?;

    sqlx::query("UPDATE accounts SET balance = balance + $1 WHERE id = $2")
        .bind(amount)
        .bind(to_id)
        .execute(&mut *tx)
        .await?;

    tx.commit().await?;
    Ok(())
}
```

## Connection Pooling

### Python (SQLAlchemy)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    DATABASE_URL,
    pool_size=5,           # Base connections
    max_overflow=10,       # Extra connections when needed
    pool_timeout=30,       # Wait time for connection
    pool_recycle=1800,     # Recycle connections after 30 min
    pool_pre_ping=True,    # Verify connection before use
)

SessionLocal = sessionmaker(bind=engine)
```

### TypeScript (Prisma)

```typescript
// Prisma handles pooling internally, configure in DATABASE_URL
// postgresql://user:pass@host:5432/db?connection_limit=5&pool_timeout=30

const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL,
    },
  },
})
```

### Go

```go
import (
    "database/sql"
    "time"
)

func NewDB(dsn string) (*sql.DB, error) {
    db, err := sql.Open("postgres", dsn)
    if err != nil {
        return nil, err
    }

    db.SetMaxOpenConns(25)              // Max open connections
    db.SetMaxIdleConns(5)               // Max idle connections
    db.SetConnMaxLifetime(5 * time.Minute)  // Connection lifetime
    db.SetConnMaxIdleTime(1 * time.Minute)  // Idle timeout

    if err := db.Ping(); err != nil {
        return nil, err
    }

    return db, nil
}
```

## Pagination Patterns

### Offset-Based (Simple, but slow for large offsets)

```python
# Python
def get_users_page(session: Session, page: int, page_size: int) -> list[User]:
    offset = (page - 1) * page_size
    stmt = select(User).order_by(User.id).offset(offset).limit(page_size)
    return list(session.scalars(stmt))
```

```typescript
// TypeScript (Prisma)
async function getUsersPage(page: number, pageSize: number) {
  return prisma.user.findMany({
    skip: (page - 1) * pageSize,
    take: pageSize,
    orderBy: { id: 'asc' },
  })
}
```

### Cursor-Based (Efficient for large datasets)

```python
# Python
def get_users_after(session: Session, cursor_id: int | None, limit: int) -> list[User]:
    stmt = select(User).order_by(User.id).limit(limit)
    if cursor_id:
        stmt = stmt.where(User.id > cursor_id)
    return list(session.scalars(stmt))
```

```typescript
// TypeScript (Prisma)
async function getUsersAfter(cursorId: string | null, limit: number) {
  return prisma.user.findMany({
    take: limit,
    ...(cursorId && {
      skip: 1, // Skip the cursor
      cursor: { id: cursorId },
    }),
    orderBy: { id: 'asc' },
  })
}
```

```go
// Go
func GetUsersAfter(db *sql.DB, cursorID int64, limit int) ([]User, error) {
    query := "SELECT id, email, name FROM users WHERE id > $1 ORDER BY id LIMIT $2"
    rows, err := db.Query(query, cursorID, limit)
    // ... process rows
}
```

## N+1 Query Prevention

### Python (SQLAlchemy - Eager Loading)

```python
from sqlalchemy.orm import joinedload, selectinload

# BAD - N+1 queries
def get_posts_with_authors_bad(session: Session) -> list[Post]:
    posts = session.scalars(select(Post)).all()
    for post in posts:
        print(post.author.name)  # Separate query for each post!
    return posts

# GOOD - Single query with join
def get_posts_with_authors(session: Session) -> list[Post]:
    stmt = select(Post).options(joinedload(Post.author))
    return list(session.scalars(stmt))

# GOOD - Two queries (better for large result sets)
def get_posts_with_comments(session: Session) -> list[Post]:
    stmt = select(Post).options(selectinload(Post.comments))
    return list(session.scalars(stmt))
```

### TypeScript (Prisma - Include)

```typescript
// BAD - N+1 queries
const posts = await prisma.post.findMany()
for (const post of posts) {
  const author = await prisma.user.findUnique({
    where: { id: post.authorId },
  }) // Separate query each time!
}

// GOOD - Single query with include
const posts = await prisma.post.findMany({
  include: {
    author: true,
    comments: {
      include: { user: true },
    },
  },
})
```

### Go (Manual Batch Loading)

```go
// BAD - N+1
func GetPostsWithAuthors(db *sql.DB) ([]PostWithAuthor, error) {
    posts, _ := GetAllPosts(db)
    for i := range posts {
        author, _ := GetUserByID(db, posts[i].AuthorID)  // N queries!
        posts[i].Author = author
    }
    return posts, nil
}

// GOOD - Batch load with JOIN or IN clause
func GetPostsWithAuthors(db *sql.DB) ([]PostWithAuthor, error) {
    rows, err := db.Query(`
        SELECT p.id, p.title, p.content, u.id, u.name, u.email
        FROM posts p
        JOIN users u ON p.author_id = u.id
    `)
    // ... single query gets all data
}
```
