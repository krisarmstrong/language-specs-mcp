# clj-kondo

clj-kondo is a linter for Clojure, ClojureScript, and EDN with over 100 linting rules.

Version: 2024.11.14
Source: https://github.com/clj-kondo/clj-kondo

## Installation

```bash
# macOS
brew install borkdude/brew/clj-kondo

# Linux
bash < <(curl -s https://raw.githubusercontent.com/clj-kondo/clj-kondo/master/script/install-clj-kondo)

# npm
npm install -g clj-kondo
```

## Usage

```bash
# Lint files
clj-kondo --lint src

# Lint with config
clj-kondo --lint src --config '{:linters {:unused-namespace {:level :warning}}}'
```

## Configuration

Create `.clj-kondo/config.edn`:

```clojure
{:linters
 {:unused-namespace {:level :warning}
  :unresolved-symbol {:level :error}
  :missing-docstring {:level :off}}

 :lint-as {my.lib/defn clojure.core/defn}}
```

## Rule Categories

### Namespace & Import Issues
- `:unresolved-namespace` - Missing requires
- `:unresolved-symbol` - Undefined symbols
- `:unused-namespace` - Unused requires
- `:unused-import` - Unused Java imports
- `:conflicting-alias` - Conflicting namespace aliases
- `:consistent-alias` - Enforce consistent aliases

### Variable Definition & Usage
- `:redefined-var` - Var redefinition warnings
- `:unused-binding` - Unused local bindings
- `:unused-private-var` - Unused private definitions
- `:shadowed-var` - Locals shadowing outer vars

### Type & Arity Issues
- `:invalid-arity` - Wrong argument counts
- `:type-mismatch` - Type incompatibilities

### Control Flow
- `:cond-else` - Missing `:else` in cond
- `:unreachable-code` - Dead code paths
- `:loop-without-recur` - Loops without recur

### Docstrings
- `:missing-docstring` - Undocumented public vars
- `:docstring-blank` - Empty docstrings

### Import Patterns
- `:refer-all` - Disallow `:refer :all`
- `:duplicate-require` - Repeated requires

### Maps & Collections
- `:duplicate-map-key` - Repeated map keys
- `:duplicate-set-key` - Set duplicates
- `:missing-map-value` - Uneven key-value pairs

### Deprecated & Discouraged
- `:deprecated-var` - Obsolete functions
- `:discouraged-var` - Configurable warnings

## Disabling Linters

```clojure
;; Inline suppression
#_{:clj-kondo/ignore [:unused-binding]}
(let [x 1] nil)

;; File-level
{:clj-kondo/config {:linters {:unused-binding {:level :off}}}}
```
