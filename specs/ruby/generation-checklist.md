# Ruby Generation Checklist

**Read this BEFORE writing Ruby code. These rules prevent the most common bugs.**

## Critical: You Must Do These

### 1. Use `frozen_string_literal` Magic Comment
```ruby
# BAD - mutable strings by default
str = "hello"
str << " world"  # Mutates original

# GOOD - add to top of every file
# frozen_string_literal: true
str = "hello"
str << " world"  # Raises FrozenError
str = str + " world"  # Creates new string (correct)
```

### 2. Use Safe Navigation Operator for Nil Checks
```ruby
# BAD - NoMethodError if nil
user.address.city

# GOOD - returns nil if any part is nil
user&.address&.city

# GOOD - with default
user&.address&.city || "Unknown"
```

### 3. Use `fetch` for Hash Access When Key Must Exist
```ruby
# BAD - silently returns nil
value = hash[:key]

# GOOD - raises if key missing
value = hash.fetch(:key)

# GOOD - with default
value = hash.fetch(:key, "default")
value = hash.fetch(:key) { calculate_default }
```

### 4. Use Symbols for Hash Keys
```ruby
# BAD - string keys waste memory
user = { "name" => "Alice", "age" => 30 }

# GOOD - symbol keys
user = { name: "Alice", age: 30 }
```

### 5. Always Handle Exceptions Specifically
```ruby
# BAD - catches everything including syntax errors
begin
  risky_operation
rescue
  # Swallows all errors
end

# GOOD - catch specific exceptions
begin
  risky_operation
rescue NetworkError => e
  logger.error("Network failed: #{e.message}")
  retry_with_backoff
rescue ValidationError => e
  return { error: e.message }
end
```

## Important: Strong Recommendations

### 6. Prefer `each` Over `for`
```ruby
# BAD - for loop leaks variable
for item in items
  process(item)
end
puts item  # Still accessible!

# GOOD - each with block
items.each do |item|
  process(item)
end
```

### 7. Use Guard Clauses for Early Returns
```ruby
# BAD - deep nesting
def process(user)
  if user
    if user.active?
      if user.verified?
        # do work
      end
    end
  end
end

# GOOD - guard clauses
def process(user)
  return unless user
  return unless user.active?
  return unless user.verified?

  # do work
end
```

### 8. Use `%w` and `%i` for Word/Symbol Arrays
```ruby
# BAD - verbose
statuses = ["pending", "active", "completed"]
fields = [:name, :email, :age]

# GOOD - cleaner
statuses = %w[pending active completed]
fields = %i[name email age]
```

### 9. Use Enumerable Methods Instead of Manual Loops
```ruby
# BAD - manual accumulation
names = []
users.each do |user|
  names << user.name if user.active?
end

# GOOD - functional style
names = users.select(&:active?).map(&:name)
```

### 10. Use `||=` for Memoization
```ruby
# BAD - recalculates every time
def expensive_data
  calculate_expensive_thing
end

# GOOD - memoize result
def expensive_data
  @expensive_data ||= calculate_expensive_thing
end
```

## Ruby Idioms

### 11. Use Keyword Arguments for Clarity
```ruby
# BAD - positional args unclear at call site
def create_user(name, email, admin, verified)
create_user("Alice", "a@b.com", false, true)  # What do false, true mean?

# GOOD - keyword args are self-documenting
def create_user(name:, email:, admin: false, verified: false)
create_user(name: "Alice", email: "a@b.com", verified: true)
```

### 12. Use `tap` for Method Chaining Setup
```ruby
# GOOD - configure and return
def build_user
  User.new.tap do |user|
    user.name = "Alice"
    user.email = "alice@example.com"
    user.save!
  end
end
```

### 13. Use `then` / `yield_self` for Pipeline Transformations
```ruby
# GOOD - pipeline style (Ruby 2.6+)
result = input
  .then { |x| validate(x) }
  .then { |x| transform(x) }
  .then { |x| format(x) }
```

### 14. Prefer Single-Quoted Strings When No Interpolation
```ruby
# GOOD - no interpolation, use single quotes
name = 'Alice'

# GOOD - with interpolation, use double quotes
greeting = "Hello, #{name}!"
```

## Security

### 15. Use Parameterized Queries for SQL
```ruby
# DANGEROUS - SQL injection
User.where("name = '#{params[:name]}'")

# SAFE - parameterized
User.where(name: params[:name])
User.where("name = ?", params[:name])
```

### 16. Sanitize HTML Output
```ruby
# DANGEROUS - XSS vulnerability
<%= user_input %>  # In older Rails or raw output

# SAFE - Rails auto-escapes, but be explicit
<%= sanitize(user_input) %>
<%= h(user_input) %>
```

### 17. Use Strong Parameters in Rails
```ruby
# DANGEROUS - mass assignment vulnerability
User.create(params[:user])

# SAFE - whitelist allowed params
def user_params
  params.require(:user).permit(:name, :email)
end
User.create(user_params)
```

---

**Quick Reference - Copy This Mental Model:**
- `# frozen_string_literal: true` at top
- Safe navigation `&.` for nil
- `fetch` for required hash keys
- Symbol keys in hashes
- Catch specific exceptions
- Guard clauses, not nesting
- `%w[]` and `%i[]` for arrays
- Enumerable methods over loops
- `||=` for memoization
- Keyword arguments for clarity
- Parameterized SQL queries
- Strong parameters in Rails
