# HLint

HLint is a tool for suggesting improvements to Haskell code.

Version: 3.8
Source: https://github.com/ndmitchell/hlint

## Installation

```bash
# cabal
cabal install hlint

# Stack
stack install hlint

# Homebrew
brew install hlint
```

## Usage

```bash
# Lint files
hlint src/

# With suggestions
hlint . --report

# Apply suggestions
hlint --refactor --refactor-options="--inplace" src/

# Generate default config
hlint --default > .hlint.yaml
```

## Configuration

Create `.hlint.yaml`:

```yaml
# Ignore specific hints
- ignore: {name: "Use camelCase"}

# Warn on specific patterns
- warn: {lhs: "map head (group x)", rhs: "nub x"}

# Custom hint
- hint: {lhs: "concat (map f x)", rhs: "concatMap f x"}

# Restrict functions
- functions:
  - {name: unsafePerformIO, within: []}
```

## Hint Categories

### I/O Operations
- Replace `putStrLn (show x)` with `print x`
- Replace `hGetChar stdin` with `getChar`

### List Operations
- Combine `concat` and `map` into `concatMap`
- Use `span`/`break` appropriately
- Simplify length checks with `null`
- Use `map` over explicit recursion

### Monoid Laws
- Eliminate redundant identity operations
- Simplify `mempty <>` patterns

### Functor/Applicative/Monad
- Use `fmap` consistently
- Apply monad laws for cleaner code
- Replace `fmap f . fmap g` with `fmap (f . g)`

### State Monad
- Use `gets` for state field access
- Use `asks` for reader field access

### Maybe/Either Handling
- Use `fromMaybe` for default values
- Use `mapMaybe` for filtering
- Simplify case expressions

### Function Composition
- Apply eta-reduction where appropriate
- Eliminate redundant identity functions
- Simplify lambda expressions

### Boolean Simplification
- Replace verbose conditionals
- Simplify negations
- Use guard patterns

## Severity Levels

- **Error**: Critical issues
- **Warning**: Recommended changes
- **Suggestion**: Optional improvements

## Inline Configuration

```haskell
{-# ANN module "HLint: ignore Use camelCase" #-}

{-# ANN functionName "HLint: ignore" #-}
```
