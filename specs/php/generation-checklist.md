# PHP Generation Checklist

**Read this BEFORE writing PHP code. These rules prevent the most common bugs.**

## Critical: You Must Do These

### 1. Use Strict Types
```php
<?php
// ALWAYS add at the top of every file
declare(strict_types=1);

// Now type mismatches throw TypeError instead of coercing
function add(int $a, int $b): int {
    return $a + $b;
}
add("1", "2");  // TypeError! Good.
```

### 2. Use `===` Not `==` for Comparisons
```php
// BAD - loose comparison has surprising behavior
0 == "foo"     // true! (string coerced to 0)
"10" == "1e1"  // true! (both become float 10)
null == false  // true!

// GOOD - strict comparison
0 === "foo"    // false
"10" === "1e1" // false
null === false // false
```

### 3. Use Null Coalescing Operator
```php
// BAD - verbose null check
$name = isset($user['name']) ? $user['name'] : 'Guest';

// GOOD - null coalescing
$name = $user['name'] ?? 'Guest';

// GOOD - null coalescing assignment (PHP 7.4+)
$user['name'] ??= 'Guest';
```

### 4. Use Prepared Statements for SQL
```php
// DANGEROUS - SQL injection
$stmt = $pdo->query("SELECT * FROM users WHERE id = $id");

// SAFE - prepared statement
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);

// SAFE - named parameters
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $id]);
```

### 5. Always Escape Output
```php
// DANGEROUS - XSS vulnerability
echo $userInput;
echo "<div>$userName</div>";

// SAFE - escape HTML
echo htmlspecialchars($userInput, ENT_QUOTES, 'UTF-8');

// GOOD - create a helper function
function h(string $str): string {
    return htmlspecialchars($str, ENT_QUOTES, 'UTF-8');
}
echo h($userInput);
```

## Important: Strong Recommendations

### 6. Use Type Declarations Everywhere
```php
// BAD - no type safety
function process($data) {
    return $data['value'];
}

// GOOD - fully typed (PHP 7.4+)
function process(array $data): string {
    return $data['value'];
}

// GOOD - with union types (PHP 8.0+)
function findUser(int|string $id): ?User {
    // ...
}
```

### 7. Use Constructor Property Promotion (PHP 8.0+)
```php
// BAD - verbose
class User {
    private string $name;
    private string $email;

    public function __construct(string $name, string $email) {
        $this->name = $name;
        $this->email = $email;
    }
}

// GOOD - promoted properties
class User {
    public function __construct(
        private string $name,
        private string $email,
    ) {}
}
```

### 8. Use `match` Instead of `switch` (PHP 8.0+)
```php
// BAD - switch falls through, loose comparison
switch ($status) {
    case 'active':
        $result = 1;
        break;
    case 'pending':
        $result = 2;
        break;
    default:
        $result = 0;
}

// GOOD - match is an expression, strict comparison
$result = match($status) {
    'active' => 1,
    'pending' => 2,
    default => 0,
};
```

### 9. Use Named Arguments for Clarity (PHP 8.0+)
```php
// BAD - unclear what booleans mean
createUser('Alice', 'alice@test.com', true, false, true);

// GOOD - self-documenting
createUser(
    name: 'Alice',
    email: 'alice@test.com',
    isAdmin: true,
    isVerified: false,
    sendWelcome: true,
);
```

### 10. Use Array Destructuring
```php
// BAD - manual extraction
$first = $array[0];
$second = $array[1];

// GOOD - destructuring
[$first, $second] = $array;

// GOOD - with keys
['name' => $name, 'email' => $email] = $user;
```

## Error Handling

### 11. Use Exceptions, Not Error Returns
```php
// BAD - error returns are easy to ignore
function divide($a, $b) {
    if ($b === 0) return false;  // Easy to miss!
    return $a / $b;
}

// GOOD - exceptions force handling
function divide(float $a, float $b): float {
    if ($b === 0.0) {
        throw new InvalidArgumentException('Division by zero');
    }
    return $a / $b;
}
```

### 12. Use Specific Exception Types
```php
// BAD - generic exception
throw new Exception('User not found');

// GOOD - specific exception
throw new UserNotFoundException($userId);

// Define custom exceptions
class UserNotFoundException extends RuntimeException {
    public function __construct(int $userId) {
        parent::__construct("User not found: $userId");
    }
}
```

## Modern PHP

### 13. Use Enums (PHP 8.1+)
```php
// BAD - string constants
const STATUS_PENDING = 'pending';
const STATUS_ACTIVE = 'active';

// GOOD - enum
enum Status: string {
    case Pending = 'pending';
    case Active = 'active';
    case Completed = 'completed';
}

function setStatus(Status $status): void { }
setStatus(Status::Active);
```

### 14. Use Readonly Properties (PHP 8.1+)
```php
// GOOD - immutable after construction
class User {
    public function __construct(
        public readonly string $name,
        public readonly string $email,
    ) {}
}
```

### 15. Use First-Class Callable Syntax (PHP 8.1+)
```php
// BAD - verbose
$fn = [$this, 'process'];
array_map([$this, 'transform'], $items);

// GOOD - first-class callable
$fn = $this->process(...);
array_map($this->transform(...), $items);
```

---

**Quick Reference - Copy This Mental Model:**
- `declare(strict_types=1);` at top
- `===` always, never `==`
- `??` for null coalescing
- Prepared statements for SQL
- `htmlspecialchars()` for output
- Type declarations everywhere
- Constructor property promotion
- `match` over `switch`
- Named arguments for clarity
- Exceptions over error returns
- Enums for fixed sets of values
