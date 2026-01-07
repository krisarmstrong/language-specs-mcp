# Haskell Generation Checklist

**Read this BEFORE writing Haskell code. The type system is your friend—use it.**

## Critical: You Must Do These

### 1. Use Explicit Type Signatures
```haskell
-- BAD - missing type signature
greet name = "Hello, " ++ name

-- GOOD - explicit signature documents intent
greet :: String -> String
greet name = "Hello, " ++ name

-- GOOD - polymorphic with constraints
sum' :: Num a => [a] -> a
sum' = foldr (+) 0
```

### 2. Use `Maybe` Instead of Partial Functions
```haskell
-- BAD - partial function, crashes on empty
head []     -- *** Exception: empty list
head [1,2]  -- 1

-- GOOD - total function with Maybe
safeHead :: [a] -> Maybe a
safeHead []    = Nothing
safeHead (x:_) = Just x
```

### 3. Use `Either` for Error Handling
```haskell
-- BAD - using error or undefined
divide :: Int -> Int -> Int
divide _ 0 = error "Division by zero"
divide a b = a `div` b

-- GOOD - Either for explicit errors
divide :: Int -> Int -> Either String Int
divide _ 0 = Left "Division by zero"
divide a b = Right (a `div` b)
```

### 4. Use Pattern Matching Exhaustively
```haskell
-- BAD - non-exhaustive pattern
data Status = Active | Pending | Completed

describe :: Status -> String
describe Active = "Active"
describe Pending = "Pending"
-- Missing Completed!

-- GOOD - exhaustive patterns
describe :: Status -> String
describe Active    = "Active"
describe Pending   = "Pending"
describe Completed = "Completed"

-- Enable warning: -Wincomplete-patterns
```

### 5. Avoid Partial Record Field Access
```haskell
-- BAD - partial accessor
data User = Admin { name :: String } | Guest
name (Admin n) = n
name Guest     = error "no name"  -- Crash!

-- GOOD - use Maybe or different approach
data User = Admin { adminName :: String } | Guest

getName :: User -> Maybe String
getName (Admin n) = Just n
getName Guest     = Nothing
```

## Important: Strong Recommendations

### 6. Use `newtype` for Type Safety
```haskell
-- BAD - type synonyms don't prevent mixing
type UserId = Int
type ProductId = Int

findUser :: UserId -> Maybe User
findUser productId = ...  -- Compiles! Wrong!

-- GOOD - newtype prevents mixing
newtype UserId = UserId Int
newtype ProductId = ProductId Int

findUser :: UserId -> Maybe User
findUser (ProductId _) = ...  -- Compile error!
```

### 7. Use Record Syntax for Multiple Fields
```haskell
-- BAD - positional fields hard to read
data User = User String String Int Bool

-- GOOD - named fields
data User = User
  { userName  :: String
  , userEmail :: String
  , userAge   :: Int
  , userActive :: Bool
  }

-- Use with record update syntax
updateEmail :: String -> User -> User
updateEmail email user = user { userEmail = email }
```

### 8. Use `where` or `let` for Local Definitions
```haskell
-- GOOD - where clause
calculatePrice :: [Item] -> Price
calculatePrice items = subtotal + tax
  where
    subtotal = sum (map price items)
    tax      = subtotal * 0.1

-- GOOD - let for expression-local bindings
calculatePrice items =
  let subtotal = sum (map price items)
      tax      = subtotal * 0.1
  in  subtotal + tax
```

### 9. Prefer Function Composition
```haskell
-- BAD - nested calls
process x = toUpper (trim (normalize x))

-- GOOD - composition with (.)
process :: String -> String
process = toUpper . trim . normalize

-- GOOD - pointfree style where readable
lengths :: [[a]] -> [Int]
lengths = map length
```

### 10. Use Guards for Conditional Logic
```haskell
-- BAD - nested if-else
absolute x = if x < 0 then -x else x

-- GOOD - guards
absolute :: (Num a, Ord a) => a -> a
absolute x
  | x < 0     = -x
  | otherwise = x

-- GOOD - multiple conditions
grade :: Int -> String
grade score
  | score >= 90 = "A"
  | score >= 80 = "B"
  | score >= 70 = "C"
  | otherwise   = "F"
```

## Monads and Effects

### 11. Use `do` Notation for Monadic Code
```haskell
-- BAD - explicit bind chains
fetchUser id >>= \user ->
  fetchProfile (userId user) >>= \profile ->
    return (user, profile)

-- GOOD - do notation
fetchUserWithProfile :: UserId -> IO (User, Profile)
fetchUserWithProfile id = do
  user    <- fetchUser id
  profile <- fetchProfile (userId user)
  return (user, profile)
```

### 12. Use Applicative When Order Doesn't Matter
```haskell
-- When effects are independent, use Applicative
data User = User String String Int

-- GOOD - Applicative style
parseUser :: Parser User
parseUser = User <$> parseName <*> parseEmail <*> parseAge

-- Equivalent do-notation (more verbose for this case)
parseUser = do
  name  <- parseName
  email <- parseEmail
  age   <- parseAge
  return (User name email age)
```

### 13. Use `traverse` and `sequence`
```haskell
-- GOOD - traverse maps and sequences in one step
validateUsers :: [RawUser] -> Either Error [User]
validateUsers = traverse validateUser

-- GOOD - sequence turns [m a] into m [a]
fetchAll :: [UserId] -> IO [User]
fetchAll ids = sequence (map fetchUser ids)
-- Or: traverse fetchUser ids
```

### 14. Handle IO Errors with `try` or `catch`
```haskell
import Control.Exception

-- GOOD - handle exceptions
readFileSafe :: FilePath -> IO (Either IOException String)
readFileSafe path = try (readFile path)

-- GOOD - with specific handler
readConfig :: FilePath -> IO Config
readConfig path = readFile path `catch` handler
  where
    handler :: IOException -> IO Config
    handler _ = return defaultConfig
```

## Performance

### 15. Use Strict Fields When Appropriate
```haskell
-- BAD - lazy fields cause space leaks
data Stats = Stats { count :: Int, total :: Int }

-- GOOD - strict fields with BangPatterns
data Stats = Stats { count :: !Int, total :: !Int }

-- Or use StrictData extension for entire module
{-# LANGUAGE StrictData #-}
```

### 16. Use `Text` Instead of `String`
```haskell
-- BAD - String is slow (linked list of Char)
processName :: String -> String

-- GOOD - Text is efficient
import Data.Text (Text)
import qualified Data.Text as T

processName :: Text -> Text
processName = T.toUpper . T.strip
```

---

**Quick Reference - Copy This Mental Model:**
- Explicit type signatures
- `Maybe` for optional values
- `Either` for errors
- Exhaustive pattern matching
- `newtype` for type safety
- Record syntax for named fields
- Function composition (`.`)
- Guards over if-else
- `do` notation for monads
- Applicative for independent effects
- `traverse`/`sequence` for collections
- Strict fields to avoid space leaks
- `Text` over `String`
