# SQL Generation Checklist

**Read this BEFORE writing SQL. Security and performance matter from the start.**

## Critical: You Must Do These

### 1. NEVER Concatenate User Input into Queries
```sql
-- DANGEROUS - SQL injection vulnerability
SELECT * FROM users WHERE id = ' + userId + '
SELECT * FROM users WHERE name = '" + userName + "'"

-- SAFE - Use parameterized queries (in application code)
-- Java: PreparedStatement
-- Python: cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
-- Node.js: pool.query("SELECT * FROM users WHERE id = $1", [userId])
```

### 2. Always Use Explicit Column Names in SELECT
```sql
-- BAD - fragile, unclear what's returned
SELECT * FROM users

-- GOOD - explicit columns
SELECT id, name, email, created_at
FROM users

-- Especially important in INSERT
INSERT INTO users (name, email, created_at)
VALUES ('Alice', 'alice@test.com', NOW())
```

### 3. Use Appropriate JOIN Types
```sql
-- Know your JOINs:
-- INNER JOIN - only matching rows from both tables
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id

-- LEFT JOIN - all from left, matching from right (or NULL)
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id

-- Never use implicit joins (comma syntax)
-- BAD
SELECT * FROM users, orders WHERE users.id = orders.user_id
```

### 4. Use Transactions for Multiple Related Operations
```sql
-- GOOD - atomic operations
BEGIN TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;

-- On error
ROLLBACK;
```

### 5. Always Have a WHERE Clause for UPDATE/DELETE
```sql
-- DANGEROUS - updates ALL rows!
UPDATE users SET status = 'inactive'

-- SAFE - specific condition
UPDATE users SET status = 'inactive'
WHERE last_login < DATE_SUB(NOW(), INTERVAL 1 YEAR)

-- Use LIMIT for safety during testing
DELETE FROM logs
WHERE created_at < '2020-01-01'
LIMIT 1000
```

## Important: Strong Recommendations

### 6. Use Meaningful Table Aliases
```sql
-- BAD - cryptic aliases
SELECT a.x, b.y FROM foo a JOIN bar b ON a.id = b.fid

-- GOOD - meaningful aliases
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
```

### 7. Use COALESCE for NULL Handling
```sql
-- BAD - NULL propagates unexpectedly
SELECT name, middle_name || ' ' || last_name AS full_name
-- If middle_name is NULL, entire expression is NULL

-- GOOD - handle NULLs explicitly
SELECT name,
       COALESCE(middle_name, '') || ' ' || last_name AS full_name
FROM users

-- GOOD - default values
SELECT COALESCE(discount, 0) AS discount
FROM products
```

### 8. Use EXISTS Instead of IN for Subqueries
```sql
-- BAD - IN with subquery (less efficient for large datasets)
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE status = 'active')

-- GOOD - EXISTS is often faster
SELECT * FROM orders o
WHERE EXISTS (
    SELECT 1 FROM users u
    WHERE u.id = o.user_id AND u.status = 'active'
)
```

### 9. Use CTEs for Complex Queries
```sql
-- BAD - deeply nested subqueries
SELECT * FROM (
    SELECT * FROM (
        SELECT user_id, SUM(amount) as total
        FROM orders
        GROUP BY user_id
    ) subq1
    WHERE total > 1000
) subq2

-- GOOD - CTEs are readable
WITH user_totals AS (
    SELECT user_id, SUM(amount) as total
    FROM orders
    GROUP BY user_id
),
high_value_users AS (
    SELECT * FROM user_totals
    WHERE total > 1000
)
SELECT u.name, hvp.total
FROM users u
JOIN high_value_users hvp ON u.id = hvp.user_id
```

### 10. Use CASE for Conditional Logic
```sql
-- GOOD - readable conditional logic
SELECT
    name,
    CASE
        WHEN score >= 90 THEN 'A'
        WHEN score >= 80 THEN 'B'
        WHEN score >= 70 THEN 'C'
        ELSE 'F'
    END AS grade
FROM students

-- GOOD - conditional aggregation
SELECT
    COUNT(*) AS total_orders,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed,
    SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) AS pending
FROM orders
```

## Performance

### 11. Index Columns Used in WHERE, JOIN, ORDER BY
```sql
-- Create indexes for frequently queried columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_created_at ON orders(created_at);

-- Composite index for multi-column conditions
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
```

### 12. Avoid Functions on Indexed Columns in WHERE
```sql
-- BAD - function prevents index use
SELECT * FROM users
WHERE YEAR(created_at) = 2024

-- GOOD - range query uses index
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01'

-- BAD
WHERE LOWER(email) = 'alice@test.com'

-- GOOD - store normalized, or use functional index
WHERE email = 'alice@test.com'
```

### 13. Use LIMIT for Large Result Sets
```sql
-- GOOD - paginated results
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 0   -- Page 1

-- For large offsets, use keyset pagination
SELECT * FROM orders
WHERE created_at < :last_seen_date
ORDER BY created_at DESC
LIMIT 20
```

### 14. Use EXPLAIN to Analyze Queries
```sql
-- Check query execution plan
EXPLAIN SELECT * FROM orders
WHERE user_id = 123 AND status = 'pending';

-- Look for: table scans, missing indexes, inefficient joins
```

## Data Integrity

### 15. Use Constraints
```sql
-- GOOD - enforce data integrity
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'inactive', 'suspended')),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Foreign key constraint
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    total DECIMAL(10,2) NOT NULL CHECK (total >= 0)
);
```

### 16. Use Appropriate Data Types
```sql
-- GOOD - correct types
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,        -- Not FLOAT for money!
    quantity INTEGER NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT true,
    metadata JSONB,                       -- PostgreSQL JSON
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
```

---

**Quick Reference - Copy This Mental Model:**
- NEVER concatenate user input (parameterize!)
- Explicit column names, not `SELECT *`
- Know your JOIN types
- Transactions for related operations
- Always WHERE on UPDATE/DELETE
- COALESCE for NULL handling
- EXISTS over IN for subqueries
- CTEs for complex queries
- Index WHERE/JOIN/ORDER columns
- No functions on indexed columns in WHERE
- LIMIT for large results
- EXPLAIN to analyze
- Constraints for integrity
- DECIMAL for money, not FLOAT
