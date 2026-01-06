# clj-kondo Rules Reference

Complete list of clj-kondo linting rules.

Source: https://github.com/clj-kondo/clj-kondo/blob/master/doc/linters.md

## Namespace Rules

### :aliased-namespace-symbol
Warns when qualified symbol has defined alias.

### :aliased-namespace-var-usage
Warns on vars from `:as-alias` namespaces.

### :conflicting-alias
Detects conflicting namespace aliases.

### :consistent-alias
Enforces consistent aliases per namespace.

### :self-requiring-namespace
Warns when namespace requires itself.

### :unresolved-namespace
Detects missing requires.

### :unresolved-symbol
Catches undefined symbols.

### :unresolved-var
Warns on unresolved qualified vars.

### :unused-namespace
Identifies unused requires.

### :unused-import
Detects unused Java imports.

### :underscore-in-namespace
Discourages underscores in namespace names.

## Variable Rules

### :redefined-var
Warns on var redefinition.

### :unused-binding
Catches unused local bindings.

### :unused-private-var
Flags unused private definitions.

### :unused-referred-var
Identifies unused referred symbols.

### :shadowed-var
Warns when locals shadow outer vars.

### :uninitialized-var
Catches def without initial value.

## Arity Rules

### :invalid-arity
Detects wrong argument counts.

### :conflicting-fn-arity
Flags duplicate arities.

### :type-mismatch
Warns on type incompatibilities.

### :protocol-method-varargs
Disallows varargs in protocols.

## Control Flow Rules

### :cond-else
Enforces `:else` in cond forms.

### :missing-else-branch
Warns on incomplete if expressions.

### :unreachable-code
Detects dead code paths.

### :unexpected-recur
Flags recur outside loops.

### :loop-without-recur
Warns on loops without recur.

## Function Rules

### :def-fn
Suggests defn over def+fn combinations.

### :do-template
Validates clojure.template/do-template usage.

### :redundant-fn-wrapper
Eliminates unnecessary fn wrappers.

### :redundant-call
Removes redundant function calls.

### :redundant-let
Detects nested let expressions.

## Comparison Rules

### :equals-nil
Prefers nil? over (= nil x).

### :equals-true
Prefers true? over (= true x).

### :equals-false
Prefers false? over (= false x).

### :equals-float
Warns on float equality checks.

### :single-operand-comparison
Flags incomplete comparisons.

### :single-logical-operand
Detects single-arg and/or usage.

## Case Rules

### :case-duplicate-test
Identifies duplicate test constants.

### :case-quoted-test
Warns on quoted case tests.

### :case-symbol-test
Optional warning on symbol tests.

## Docstring Rules

### :missing-docstring
Warns on undocumented public vars.

### :docstring-blank
Detects empty docstrings.

### :docstring-no-summary
Enforces sentence-form summaries.

### :docstring-leading-trailing-whitespace
Removes extra spacing.

### :misplaced-docstring
Catches post-vector docstrings.

## Import Rules

### :refer
Discourages :refer usage.

### :refer-all
Disallows `:refer :all`.

### :use
Warns on deprecated :use syntax.

### :duplicate-require
Flags repeated requires.

### :unsorted-imports
Enforces alphabetical sorting.

### :unsorted-required-namespaces
Sorts namespace declarations.

## Collection Rules

### :duplicate-map-key
Detects repeated map keys.

### :duplicate-set-key
Catches set duplicates.

### :duplicate-field-name
Flags duplicate record fields.

### :duplicate-key-args
Warns on repeated assoc keys.

### :missing-map-value
Catches uneven key-value pairs.

### :unbound-destructuring-default
Validates :or bindings.

## Deprecation Rules

### :deprecated-var
Warns on marked-obsolete functions.

### :deprecated-namespace
Cautions against old namespaces.

### :discouraged-var
Customizable warnings on specific vars.

### :discouraged-namespace
Configurable namespace warnings.

### :discouraged-java-method
Flags problematic Java calls.

### :discouraged-tag
Warns on disfavored tagged literals.

## Protocol Rules

### :missing-protocol-method
Detects incomplete implementations.

### :unresolved-protocol-method
Catches extra methods.

## Dynamic Variable Rules

### :dynamic-var-not-earmuffed
Prefers *name* convention.

### :earmuffed-var-not-dynamic
Flags mislabeled vars.

## Advanced Rules

### :datalog-syntax
Validates Datalog query syntax.

### :schema-misplaced-return
Corrects Schema placement.

### :warn-on-reflection
Monitors reflection warnings.

### :java-static-field-call
Fixes static field access.

## Testing Rules

### :missing-test-assertion
Detects assertion-free tests.

### :missing-body-in-when
Catches when without body.

### :missing-clause-in-try
Validates try structures.

## Optimization Rules

### :not-empty?
Prefers seq over (not (empty? x)).

### :plus-one
Suggests inc over (+ x 1).

### :minus-one
Suggests dec over (- x 1).

### :redundant-str-call
Removes unnecessary str wrapping.

### :redundant-primitive-coercion
Eliminates type conversions.

### :reduce-without-init
Warns on unsafe reduce calls.

## Configuration Rules

### :clj-kondo-config
Validates .clj-kondo/config.edn files.

### :unknown-ns-option
Catches invalid ns declarations.

### :unknown-require-option
Flags malformed requires.

### :namespace-name-mismatch
Enforces file/ns correspondence.

## Miscellaneous Rules

### :condition-always-true
Detects tautological conditions.

### :file
Reports file reading errors.

### :format
Validates format string arguments.

### :inline-def
Discourages non-toplevel definitions.

### :keyword-binding
Warns on keyword destructuring.

### :locking-suspicious-lock
Validates locking patterns.

### :main-without-gen-class
Checks -main function setup.

### :private-call
Prevents private var access.

### :redundant-do
Removes redundant do blocks.

### :redundant-ignore
Eliminates unnecessary suppress directives.

### :redundant-let-binding
Catches self-assignments.

### :redundant-nested-call
Removes duplicate operations.

### :shadowed-fn-param
Flags duplicate parameter names.

### :single-key-in
Simplifies single-key path operations.

### :static-field-call
Corrects static member access.

### :syntax
Reports parse errors.

### :used-underscored-binding
Warns on "unused" vars actually used.

### :unused-value
Detects discarded results.

### :line-length
Enforces line width limits.
