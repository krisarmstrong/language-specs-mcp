# Rules Reference
Version: 9.39.2

Source: https://eslint.org/docs/latest/rules/


## Table of Contents

1. [Possible Problems](#possible-problems)
2. [Suggestions](#suggestions)
3. [Layout & Formatting](#layout--formatting)
4. [Deprecated](#deprecated)
5. [Removed](#removed)

Rules in ESLint are grouped by type to help you understand their purpose. Each rule has emojis denoting:

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

##  Possible Problems 

These rules relate to possible logic errors in code:[array-callback-return](/docs/latest/rules/array-callback-return)

Enforce `return` statements in callbacks of array methods

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[constructor-super](/docs/latest/rules/constructor-super)

Require `super()` calls in constructors

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[for-direction](/docs/latest/rules/for-direction)

Enforce `for` loop update clause moving the counter in the right direction

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[getter-return](/docs/latest/rules/getter-return)

Enforce `return` statements in getters

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-async-promise-executor](/docs/latest/rules/no-async-promise-executor)

Disallow using an async function as a Promise executor

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-await-in-loop](/docs/latest/rules/no-await-in-loop)

Disallow `await` inside of loops

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-class-assign](/docs/latest/rules/no-class-assign)

Disallow reassigning class members

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-compare-neg-zero](/docs/latest/rules/no-compare-neg-zero)

Disallow comparing against `-0`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-cond-assign](/docs/latest/rules/no-cond-assign)

Disallow assignment operators in conditional expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-const-assign](/docs/latest/rules/no-const-assign)

Disallow reassigning `const`, `using`, and `await using` variables

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-constant-binary-expression](/docs/latest/rules/no-constant-binary-expression)

Disallow expressions where the operation doesn’t affect the value

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-constant-condition](/docs/latest/rules/no-constant-condition)

Disallow constant expressions in conditions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-constructor-return](/docs/latest/rules/no-constructor-return)

Disallow returning value from constructor

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-control-regex](/docs/latest/rules/no-control-regex)

Disallow control characters in regular expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-debugger](/docs/latest/rules/no-debugger)

Disallow the use of `debugger`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-dupe-args](/docs/latest/rules/no-dupe-args)

Disallow duplicate arguments in `function` definitions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-dupe-class-members](/docs/latest/rules/no-dupe-class-members)

Disallow duplicate class members

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-dupe-else-if](/docs/latest/rules/no-dupe-else-if)

Disallow duplicate conditions in if-else-if chains

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-dupe-keys](/docs/latest/rules/no-dupe-keys)

Disallow duplicate keys in object literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-duplicate-case](/docs/latest/rules/no-duplicate-case)

Disallow duplicate case labels

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-duplicate-imports](/docs/latest/rules/no-duplicate-imports)

Disallow duplicate module imports

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-empty-character-class](/docs/latest/rules/no-empty-character-class)

Disallow empty character classes in regular expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-empty-pattern](/docs/latest/rules/no-empty-pattern)

Disallow empty destructuring patterns

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-ex-assign](/docs/latest/rules/no-ex-assign)

Disallow reassigning exceptions in `catch` clauses

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-fallthrough](/docs/latest/rules/no-fallthrough)

Disallow fallthrough of `case` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-func-assign](/docs/latest/rules/no-func-assign)

Disallow reassigning `function` declarations

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-import-assign](/docs/latest/rules/no-import-assign)

Disallow assigning to imported bindings

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-inner-declarations](/docs/latest/rules/no-inner-declarations)

Disallow variable or `function` declarations in nested blocks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-invalid-regexp](/docs/latest/rules/no-invalid-regexp)

Disallow invalid regular expression strings in `RegExp` constructors

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-irregular-whitespace](/docs/latest/rules/no-irregular-whitespace)

Disallow irregular whitespace

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-loss-of-precision](/docs/latest/rules/no-loss-of-precision)

Disallow literal numbers that lose precision

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-misleading-character-class](/docs/latest/rules/no-misleading-character-class)

Disallow characters which are made with multiple code points in character class syntax

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-new-native-nonconstructor](/docs/latest/rules/no-new-native-nonconstructor)

Disallow `new` operators with global non-constructor functions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-obj-calls](/docs/latest/rules/no-obj-calls)

Disallow calling global object properties as functions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-promise-executor-return](/docs/latest/rules/no-promise-executor-return)

Disallow returning values from Promise executor functions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-prototype-builtins](/docs/latest/rules/no-prototype-builtins)

Disallow calling some `Object.prototype` methods directly on objects

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-self-assign](/docs/latest/rules/no-self-assign)

Disallow assignments where both sides are exactly the same

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-self-compare](/docs/latest/rules/no-self-compare)

Disallow comparisons where both sides are exactly the same

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-setter-return](/docs/latest/rules/no-setter-return)

Disallow returning values from setters

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-sparse-arrays](/docs/latest/rules/no-sparse-arrays)

Disallow sparse arrays

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-template-curly-in-string](/docs/latest/rules/no-template-curly-in-string)

Disallow template literal placeholder syntax in regular strings

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-this-before-super](/docs/latest/rules/no-this-before-super)

Disallow `this`/`super` before calling `super()` in constructors

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unassigned-vars](/docs/latest/rules/no-unassigned-vars)

Disallow `let` or `var` variables that are read but never assigned

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-undef](/docs/latest/rules/no-undef)

Disallow the use of undeclared variables unless mentioned in `/*global */` comments

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unexpected-multiline](/docs/latest/rules/no-unexpected-multiline)

Disallow confusing multiline expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unmodified-loop-condition](/docs/latest/rules/no-unmodified-loop-condition)

Disallow unmodified loop conditions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unreachable](/docs/latest/rules/no-unreachable)

Disallow unreachable code after `return`, `throw`, `continue`, and `break` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unreachable-loop](/docs/latest/rules/no-unreachable-loop)

Disallow loops with a body that allows only one iteration

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unsafe-finally](/docs/latest/rules/no-unsafe-finally)

Disallow control flow statements in `finally` blocks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unsafe-negation](/docs/latest/rules/no-unsafe-negation)

Disallow negating the left operand of relational operators

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unsafe-optional-chaining](/docs/latest/rules/no-unsafe-optional-chaining)

Disallow use of optional chaining in contexts where the `undefined` value is not allowed

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unused-private-class-members](/docs/latest/rules/no-unused-private-class-members)

Disallow unused private class members

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unused-vars](/docs/latest/rules/no-unused-vars)

Disallow unused variables

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-use-before-define](/docs/latest/rules/no-use-before-define)

Disallow the use of variables before they are defined

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-assignment](/docs/latest/rules/no-useless-assignment)

Disallow variable assignments when the value is not used

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-backreference](/docs/latest/rules/no-useless-backreference)

Disallow useless backreferences in regular expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[require-atomic-updates](/docs/latest/rules/require-atomic-updates)

Disallow assignments that can lead to race conditions due to usage of `await` or `yield`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[use-isnan](/docs/latest/rules/use-isnan)

Require calls to `isNaN()` when checking for `NaN`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[valid-typeof](/docs/latest/rules/valid-typeof)

Enforce comparing `typeof` expressions against valid strings

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

##  Suggestions 

These rules suggest alternate ways of doing things:[accessor-pairs](/docs/latest/rules/accessor-pairs)

Enforce getter and setter pairs in objects and classes

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[arrow-body-style](/docs/latest/rules/arrow-body-style)

 ❄️ Frozen

Require braces around arrow function bodies

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[block-scoped-var](/docs/latest/rules/block-scoped-var)

Enforce the use of variables within the scope they are defined

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[camelcase](/docs/latest/rules/camelcase)

 ❄️ Frozen

Enforce camelcase naming convention

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[capitalized-comments](/docs/latest/rules/capitalized-comments)

 ❄️ Frozen

Enforce or disallow capitalization of the first letter of a comment

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[class-methods-use-this](/docs/latest/rules/class-methods-use-this)

Enforce that class methods utilize `this`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[complexity](/docs/latest/rules/complexity)

Enforce a maximum cyclomatic complexity allowed in a program

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[consistent-return](/docs/latest/rules/consistent-return)

Require `return` statements to either always or never specify values

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[consistent-this](/docs/latest/rules/consistent-this)

 ❄️ Frozen

Enforce consistent naming when capturing the current execution context

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[curly](/docs/latest/rules/curly)

 ❄️ Frozen

Enforce consistent brace style for all control statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[default-case](/docs/latest/rules/default-case)

Require `default` cases in `switch` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[default-case-last](/docs/latest/rules/default-case-last)

Enforce `default` clauses in `switch` statements to be last

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[default-param-last](/docs/latest/rules/default-param-last)

 ❄️ Frozen

Enforce default parameters to be last

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[dot-notation](/docs/latest/rules/dot-notation)

 ❄️ Frozen

Enforce dot notation whenever possible

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[eqeqeq](/docs/latest/rules/eqeqeq)

Require the use of `===` and `!==`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[func-name-matching](/docs/latest/rules/func-name-matching)

 ❄️ Frozen

Require function names to match the name of the variable or property to which they are assigned

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[func-names](/docs/latest/rules/func-names)

Require or disallow named `function` expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[func-style](/docs/latest/rules/func-style)

 ❄️ Frozen

Enforce the consistent use of either `function` declarations or expressions assigned to variables

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[grouped-accessor-pairs](/docs/latest/rules/grouped-accessor-pairs)

Require grouped accessor pairs in object literals and classes

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[guard-for-in](/docs/latest/rules/guard-for-in)

Require `for-in` loops to include an `if` statement

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[id-denylist](/docs/latest/rules/id-denylist)

 ❄️ Frozen

Disallow specified identifiers

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[id-length](/docs/latest/rules/id-length)

 ❄️ Frozen

Enforce minimum and maximum identifier lengths

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[id-match](/docs/latest/rules/id-match)

 ❄️ Frozen

Require identifiers to match a specified regular expression

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[init-declarations](/docs/latest/rules/init-declarations)

 ❄️ Frozen

Require or disallow initialization in variable declarations

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[logical-assignment-operators](/docs/latest/rules/logical-assignment-operators)

 ❄️ Frozen

Require or disallow logical assignment operator shorthand

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-classes-per-file](/docs/latest/rules/max-classes-per-file)

Enforce a maximum number of classes per file

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-depth](/docs/latest/rules/max-depth)

Enforce a maximum depth that blocks can be nested

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-lines](/docs/latest/rules/max-lines)

Enforce a maximum number of lines per file

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-lines-per-function](/docs/latest/rules/max-lines-per-function)

Enforce a maximum number of lines of code in a function

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)

Enforce a maximum depth that callbacks can be nested

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-params](/docs/latest/rules/max-params)

Enforce a maximum number of parameters in function definitions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[max-statements](/docs/latest/rules/max-statements)

Enforce a maximum number of statements allowed in function blocks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[new-cap](/docs/latest/rules/new-cap)

Require constructor names to begin with a capital letter

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-alert](/docs/latest/rules/no-alert)

Disallow the use of `alert`, `confirm`, and `prompt`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-array-constructor](/docs/latest/rules/no-array-constructor)

Disallow `Array` constructors

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-bitwise](/docs/latest/rules/no-bitwise)

Disallow bitwise operators

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-caller](/docs/latest/rules/no-caller)

Disallow the use of `arguments.caller` or `arguments.callee`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-case-declarations](/docs/latest/rules/no-case-declarations)

Disallow lexical declarations in case clauses

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-console](/docs/latest/rules/no-console)

Disallow the use of `console`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-continue](/docs/latest/rules/no-continue)

 ❄️ Frozen

Disallow `continue` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-delete-var](/docs/latest/rules/no-delete-var)

Disallow deleting variables

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-div-regex](/docs/latest/rules/no-div-regex)

 ❄️ Frozen

Disallow equal signs explicitly at the beginning of regular expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-else-return](/docs/latest/rules/no-else-return)

 ❄️ Frozen

Disallow `else` blocks after `return` statements in `if` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-empty](/docs/latest/rules/no-empty)

Disallow empty block statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-empty-function](/docs/latest/rules/no-empty-function)

Disallow empty functions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-empty-static-block](/docs/latest/rules/no-empty-static-block)

Disallow empty static blocks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-eq-null](/docs/latest/rules/no-eq-null)

Disallow `null` comparisons without type-checking operators

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-eval](/docs/latest/rules/no-eval)

Disallow the use of `eval()`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-extend-native](/docs/latest/rules/no-extend-native)

Disallow extending native types

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-extra-bind](/docs/latest/rules/no-extra-bind)

Disallow unnecessary calls to `.bind()`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-extra-boolean-cast](/docs/latest/rules/no-extra-boolean-cast)

 ❄️ Frozen

Disallow unnecessary boolean casts

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-extra-label](/docs/latest/rules/no-extra-label)

 ❄️ Frozen

Disallow unnecessary labels

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-global-assign](/docs/latest/rules/no-global-assign)

Disallow assignments to native objects or read-only global variables

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-implicit-coercion](/docs/latest/rules/no-implicit-coercion)

 ❄️ Frozen

Disallow shorthand type conversions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-implicit-globals](/docs/latest/rules/no-implicit-globals)

Disallow declarations in the global scope

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-implied-eval](/docs/latest/rules/no-implied-eval)

Disallow the use of `eval()`-like methods

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-inline-comments](/docs/latest/rules/no-inline-comments)

 ❄️ Frozen

Disallow inline comments after code

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-invalid-this](/docs/latest/rules/no-invalid-this)

Disallow use of `this` in contexts where the value of `this` is `undefined`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-iterator](/docs/latest/rules/no-iterator)

Disallow the use of the `__iterator__` property

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-label-var](/docs/latest/rules/no-label-var)

 ❄️ Frozen

Disallow labels that share a name with a variable

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-labels](/docs/latest/rules/no-labels)

 ❄️ Frozen

Disallow labeled statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-lone-blocks](/docs/latest/rules/no-lone-blocks)

Disallow unnecessary nested blocks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-lonely-if](/docs/latest/rules/no-lonely-if)

 ❄️ Frozen

Disallow `if` statements as the only statement in `else` blocks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-loop-func](/docs/latest/rules/no-loop-func)

Disallow function declarations that contain unsafe references inside loop statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-magic-numbers](/docs/latest/rules/no-magic-numbers)

 ❄️ Frozen

Disallow magic numbers

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-multi-assign](/docs/latest/rules/no-multi-assign)

Disallow use of chained assignment expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-multi-str](/docs/latest/rules/no-multi-str)

 ❄️ Frozen

Disallow multiline strings

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-negated-condition](/docs/latest/rules/no-negated-condition)

 ❄️ Frozen

Disallow negated conditions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-nested-ternary](/docs/latest/rules/no-nested-ternary)

 ❄️ Frozen

Disallow nested ternary expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-new](/docs/latest/rules/no-new)

Disallow `new` operators outside of assignments or comparisons

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-new-func](/docs/latest/rules/no-new-func)

Disallow `new` operators with the `Function` object

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-new-wrappers](/docs/latest/rules/no-new-wrappers)

Disallow `new` operators with the `String`, `Number`, and `Boolean` objects

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-nonoctal-decimal-escape](/docs/latest/rules/no-nonoctal-decimal-escape)

Disallow `\8` and `\9` escape sequences in string literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-object-constructor](/docs/latest/rules/no-object-constructor)

Disallow calls to the `Object` constructor without an argument

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-octal](/docs/latest/rules/no-octal)

Disallow octal literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-octal-escape](/docs/latest/rules/no-octal-escape)

Disallow octal escape sequences in string literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-param-reassign](/docs/latest/rules/no-param-reassign)

Disallow reassigning function parameters

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-plusplus](/docs/latest/rules/no-plusplus)

 ❄️ Frozen

Disallow the unary operators `++` and `--`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-proto](/docs/latest/rules/no-proto)

Disallow the use of the `__proto__` property

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-redeclare](/docs/latest/rules/no-redeclare)

Disallow variable redeclaration

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-regex-spaces](/docs/latest/rules/no-regex-spaces)

Disallow multiple spaces in regular expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-restricted-exports](/docs/latest/rules/no-restricted-exports)

Disallow specified names in exports

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-restricted-globals](/docs/latest/rules/no-restricted-globals)

Disallow specified global variables

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-restricted-imports](/docs/latest/rules/no-restricted-imports)

Disallow specified modules when loaded by `import`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-restricted-properties](/docs/latest/rules/no-restricted-properties)

Disallow certain properties on certain objects

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-restricted-syntax](/docs/latest/rules/no-restricted-syntax)

Disallow specified syntax

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-return-assign](/docs/latest/rules/no-return-assign)

Disallow assignment operators in `return` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-script-url](/docs/latest/rules/no-script-url)

Disallow `javascript:` URLs

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-sequences](/docs/latest/rules/no-sequences)

Disallow comma operators

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-shadow](/docs/latest/rules/no-shadow)

Disallow variable declarations from shadowing variables declared in the outer scope

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-shadow-restricted-names](/docs/latest/rules/no-shadow-restricted-names)

Disallow identifiers from shadowing restricted names

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-ternary](/docs/latest/rules/no-ternary)

 ❄️ Frozen

Disallow ternary operators

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-throw-literal](/docs/latest/rules/no-throw-literal)

Disallow throwing literals as exceptions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-undef-init](/docs/latest/rules/no-undef-init)

 ❄️ Frozen

Disallow initializing variables to `undefined`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-undefined](/docs/latest/rules/no-undefined)

 ❄️ Frozen

Disallow the use of `undefined` as an identifier

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-underscore-dangle](/docs/latest/rules/no-underscore-dangle)

 ❄️ Frozen

Disallow dangling underscores in identifiers

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unneeded-ternary](/docs/latest/rules/no-unneeded-ternary)

 ❄️ Frozen

Disallow ternary operators when simpler alternatives exist

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unused-expressions](/docs/latest/rules/no-unused-expressions)

Disallow unused expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-unused-labels](/docs/latest/rules/no-unused-labels)

Disallow unused labels

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-call](/docs/latest/rules/no-useless-call)

Disallow unnecessary calls to `.call()` and `.apply()`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-catch](/docs/latest/rules/no-useless-catch)

Disallow unnecessary `catch` clauses

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-computed-key](/docs/latest/rules/no-useless-computed-key)

 ❄️ Frozen

Disallow unnecessary computed property keys in objects and classes

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-concat](/docs/latest/rules/no-useless-concat)

 ❄️ Frozen

Disallow unnecessary concatenation of literals or template literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-constructor](/docs/latest/rules/no-useless-constructor)

Disallow unnecessary constructors

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-escape](/docs/latest/rules/no-useless-escape)

Disallow unnecessary escape characters

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-rename](/docs/latest/rules/no-useless-rename)

Disallow renaming import, export, and destructured assignments to the same name

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-useless-return](/docs/latest/rules/no-useless-return)

Disallow redundant return statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-var](/docs/latest/rules/no-var)

Require `let` or `const` instead of `var`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-void](/docs/latest/rules/no-void)

 ❄️ Frozen

Disallow `void` operators

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-warning-comments](/docs/latest/rules/no-warning-comments)

 ❄️ Frozen

Disallow specified warning terms in comments

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[no-with](/docs/latest/rules/no-with)

Disallow `with` statements

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[object-shorthand](/docs/latest/rules/object-shorthand)

 ❄️ Frozen

Require or disallow method and property shorthand syntax for object literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[one-var](/docs/latest/rules/one-var)

 ❄️ Frozen

Enforce variables to be declared either together or separately in functions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[operator-assignment](/docs/latest/rules/operator-assignment)

 ❄️ Frozen

Require or disallow assignment operator shorthand where possible

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-arrow-callback](/docs/latest/rules/prefer-arrow-callback)

 ❄️ Frozen

Require using arrow functions for callbacks

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-const](/docs/latest/rules/prefer-const)

Require `const` declarations for variables that are never reassigned after declared

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-destructuring](/docs/latest/rules/prefer-destructuring)

 ❄️ Frozen

Require destructuring from arrays and/or objects

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-exponentiation-operator](/docs/latest/rules/prefer-exponentiation-operator)

 ❄️ Frozen

Disallow the use of `Math.pow` in favor of the `**` operator

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-named-capture-group](/docs/latest/rules/prefer-named-capture-group)

Enforce using named capture group in regular expression

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-numeric-literals](/docs/latest/rules/prefer-numeric-literals)

 ❄️ Frozen

Disallow `parseInt()` and `Number.parseInt()` in favor of binary, octal, and hexadecimal literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-object-has-own](/docs/latest/rules/prefer-object-has-own)

Disallow use of `Object.prototype.hasOwnProperty.call()` and prefer use of `Object.hasOwn()`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-object-spread](/docs/latest/rules/prefer-object-spread)

 ❄️ Frozen

Disallow using `Object.assign` with an object literal as the first argument and prefer the use of object spread instead

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-promise-reject-errors](/docs/latest/rules/prefer-promise-reject-errors)

Require using Error objects as Promise rejection reasons

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-regex-literals](/docs/latest/rules/prefer-regex-literals)

Disallow use of the `RegExp` constructor in favor of regular expression literals

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-rest-params](/docs/latest/rules/prefer-rest-params)

Require rest parameters instead of `arguments`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-spread](/docs/latest/rules/prefer-spread)

 ❄️ Frozen

Require spread operators instead of `.apply()`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[prefer-template](/docs/latest/rules/prefer-template)

 ❄️ Frozen

Require template literals instead of string concatenation

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[preserve-caught-error](/docs/latest/rules/preserve-caught-error)

Disallow losing originally caught error when re-throwing custom errors

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[radix](/docs/latest/rules/radix)

Enforce the consistent use of the radix argument when using `parseInt()`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[require-await](/docs/latest/rules/require-await)

Disallow async functions which have no `await` expression

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[require-unicode-regexp](/docs/latest/rules/require-unicode-regexp)

Enforce the use of `u` or `v` flag on regular expressions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[require-yield](/docs/latest/rules/require-yield)

Require generator functions to contain `yield`

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[sort-imports](/docs/latest/rules/sort-imports)

 ❄️ Frozen

Enforce sorted `import` declarations within modules

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[sort-keys](/docs/latest/rules/sort-keys)

 ❄️ Frozen

Require object keys to be sorted

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[sort-vars](/docs/latest/rules/sort-vars)

 ❄️ Frozen

Require variables within the same declaration block to be sorted

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[strict](/docs/latest/rules/strict)

Require or disallow strict mode directives

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[symbol-description](/docs/latest/rules/symbol-description)

Require symbol descriptions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[vars-on-top](/docs/latest/rules/vars-on-top)

 ❄️ Frozen

Require `var` declarations be placed at the top of their containing scope

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

[yoda](/docs/latest/rules/yoda)

 ❄️ Frozen

Require or disallow “Yoda” conditions

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

##  Layout & Formatting 

These rules care about how the code looks rather than how it executes:[unicode-bom](/docs/latest/rules/unicode-bom)

Require or disallow Unicode byte order mark (BOM)

Categories:

 ✅ Extends

 🔧 Fix

 💡 Suggestions

## Deprecated

These rules have been deprecated in accordance with the [deprecation policy](/docs/latest/use/rule-deprecation), and replaced by newer rules:

 array-bracket-newline deprecated

Replaced by [array-bracket-newline](https://eslint.style/rules/array-bracket-newline) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 array-bracket-spacing deprecated

Replaced by [array-bracket-spacing](https://eslint.style/rules/array-bracket-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 array-element-newline deprecated

Replaced by [array-element-newline](https://eslint.style/rules/array-element-newline) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 arrow-parens deprecated

Replaced by [arrow-parens](https://eslint.style/rules/arrow-parens) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 arrow-spacing deprecated

Replaced by [arrow-spacing](https://eslint.style/rules/arrow-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 block-spacing deprecated

Replaced by [block-spacing](https://eslint.style/rules/block-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 brace-style deprecated

Replaced by [brace-style](https://eslint.style/rules/brace-style) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 callback-return deprecated

Replaced by [callback-return](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/callback-return.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 comma-dangle deprecated

Replaced by [comma-dangle](https://eslint.style/rules/comma-dangle) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 comma-spacing deprecated

Replaced by [comma-spacing](https://eslint.style/rules/comma-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 comma-style deprecated

Replaced by [comma-style](https://eslint.style/rules/comma-style) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 computed-property-spacing deprecated

Replaced by [computed-property-spacing](https://eslint.style/rules/computed-property-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 dot-location deprecated

Replaced by [dot-location](https://eslint.style/rules/dot-location) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 eol-last deprecated

Replaced by [eol-last](https://eslint.style/rules/eol-last) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 func-call-spacing deprecated

Replaced by [function-call-spacing](https://eslint.style/rules/function-call-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 function-call-argument-newline deprecated

Replaced by [function-call-argument-newline](https://eslint.style/rules/function-call-argument-newline) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 function-paren-newline deprecated

Replaced by [function-paren-newline](https://eslint.style/rules/function-paren-newline) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 generator-star-spacing deprecated

Replaced by [generator-star-spacing](https://eslint.style/rules/generator-star-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 global-require deprecated

Replaced by [global-require](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/global-require.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 handle-callback-err deprecated

Replaced by [handle-callback-err](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/handle-callback-err.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 id-blacklist deprecated

Replaced by [id-denylist](id-denylist)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 implicit-arrow-linebreak deprecated

Replaced by [implicit-arrow-linebreak](https://eslint.style/rules/implicit-arrow-linebreak) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 indent deprecated

Replaced by [indent](https://eslint.style/rules/indent) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 indent-legacy deprecated

Replaced by [indent](https://eslint.style/rules/indent) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 jsx-quotes deprecated

Replaced by [jsx-quotes](https://eslint.style/rules/jsx-quotes) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 key-spacing deprecated

Replaced by [key-spacing](https://eslint.style/rules/key-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 keyword-spacing deprecated

Replaced by [keyword-spacing](https://eslint.style/rules/keyword-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 line-comment-position deprecated

Replaced by [line-comment-position](https://eslint.style/rules/line-comment-position) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 linebreak-style deprecated

Replaced by [linebreak-style](https://eslint.style/rules/linebreak-style) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 lines-around-comment deprecated

Replaced by [lines-around-comment](https://eslint.style/rules/lines-around-comment) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 lines-around-directive deprecated

Replaced by [padding-line-between-statements](https://eslint.style/rules/padding-line-between-statements) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 lines-between-class-members deprecated

Replaced by [lines-between-class-members](https://eslint.style/rules/lines-between-class-members) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 max-len deprecated

Replaced by [max-len](https://eslint.style/rules/max-len) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 max-statements-per-line deprecated

Replaced by [max-statements-per-line](https://eslint.style/rules/max-statements-per-line) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 multiline-comment-style deprecated

Replaced by [multiline-comment-style](https://eslint.style/rules/multiline-comment-style) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 multiline-ternary deprecated

Replaced by [multiline-ternary](https://eslint.style/rules/multiline-ternary) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 new-parens deprecated

Replaced by [new-parens](https://eslint.style/rules/new-parens) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 newline-after-var deprecated

Replaced by [padding-line-between-statements](https://eslint.style/rules/padding-line-between-statements) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 newline-before-return deprecated

Replaced by [padding-line-between-statements](https://eslint.style/rules/padding-line-between-statements) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 newline-per-chained-call deprecated

Replaced by [newline-per-chained-call](https://eslint.style/rules/newline-per-chained-call) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-buffer-constructor deprecated

Replaced by [no-deprecated-api](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-deprecated-api.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-catch-shadow deprecated

Replaced by [no-shadow](no-shadow)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-confusing-arrow deprecated

Replaced by [no-confusing-arrow](https://eslint.style/rules/no-confusing-arrow) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-extra-parens deprecated

Replaced by [no-extra-parens](https://eslint.style/rules/no-extra-parens) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-extra-semi deprecated

Replaced by [no-extra-semi](https://eslint.style/rules/no-extra-semi) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-floating-decimal deprecated

Replaced by [no-floating-decimal](https://eslint.style/rules/no-floating-decimal) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-mixed-operators deprecated

Replaced by [no-mixed-operators](https://eslint.style/rules/no-mixed-operators) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-mixed-requires deprecated

Replaced by [no-mixed-requires](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-mixed-requires.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-mixed-spaces-and-tabs deprecated

Replaced by [no-mixed-spaces-and-tabs](https://eslint.style/rules/no-mixed-spaces-and-tabs) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-multi-spaces deprecated

Replaced by [no-multi-spaces](https://eslint.style/rules/no-multi-spaces) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-multiple-empty-lines deprecated

Replaced by [no-multiple-empty-lines](https://eslint.style/rules/no-multiple-empty-lines) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-native-reassign deprecated

Replaced by [no-global-assign](no-global-assign)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-negated-in-lhs deprecated

Replaced by [no-unsafe-negation](no-unsafe-negation)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-new-object deprecated

Replaced by [no-object-constructor](no-object-constructor)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-new-require deprecated

Replaced by [no-new-require](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-new-require.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-new-symbol deprecated

Replaced by [no-new-native-nonconstructor](no-new-native-nonconstructor)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-path-concat deprecated

Replaced by [no-path-concat](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-path-concat.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-process-env deprecated

Replaced by [no-process-env](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-process-env.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-process-exit deprecated

Replaced by [no-process-exit](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-process-exit.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-restricted-modules deprecated

Replaced by [no-restricted-require](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-restricted-require.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-return-await deprecated

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-spaced-func deprecated

Replaced by [function-call-spacing](https://eslint.style/rules/function-call-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-sync deprecated

Replaced by [no-sync](https://github.com/eslint-community/eslint-plugin-n/tree/master/docs/rules/no-sync.md) in [eslint-plugin-n](https://github.com/eslint-community/eslint-plugin-n)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-tabs deprecated

Replaced by [no-tabs](https://eslint.style/rules/no-tabs) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-trailing-spaces deprecated

Replaced by [no-trailing-spaces](https://eslint.style/rules/no-trailing-spaces) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 no-whitespace-before-property deprecated

Replaced by [no-whitespace-before-property](https://eslint.style/rules/no-whitespace-before-property) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 nonblock-statement-body-position deprecated

Replaced by [nonblock-statement-body-position](https://eslint.style/rules/nonblock-statement-body-position) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 object-curly-newline deprecated

Replaced by [object-curly-newline](https://eslint.style/rules/object-curly-newline) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 object-curly-spacing deprecated

Replaced by [object-curly-spacing](https://eslint.style/rules/object-curly-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 object-property-newline deprecated

Replaced by [object-property-newline](https://eslint.style/rules/object-property-newline) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 one-var-declaration-per-line deprecated

Replaced by [one-var-declaration-per-line](https://eslint.style/rules/one-var-declaration-per-line) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 operator-linebreak deprecated

Replaced by [operator-linebreak](https://eslint.style/rules/operator-linebreak) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 padded-blocks deprecated

Replaced by [padded-blocks](https://eslint.style/rules/padded-blocks) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 padding-line-between-statements deprecated

Replaced by [padding-line-between-statements](https://eslint.style/rules/padding-line-between-statements) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 prefer-reflect deprecated

Categories:

❌

 🔧 Fix

 💡 Suggestions

 quote-props deprecated

Replaced by [quote-props](https://eslint.style/rules/quote-props) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 quotes deprecated

Replaced by [quotes](https://eslint.style/rules/quotes) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 rest-spread-spacing deprecated

Replaced by [rest-spread-spacing](https://eslint.style/rules/rest-spread-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 semi deprecated

Replaced by [semi](https://eslint.style/rules/semi) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 semi-spacing deprecated

Replaced by [semi-spacing](https://eslint.style/rules/semi-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 semi-style deprecated

Replaced by [semi-style](https://eslint.style/rules/semi-style) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 space-before-blocks deprecated

Replaced by [space-before-blocks](https://eslint.style/rules/space-before-blocks) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 space-before-function-paren deprecated

Replaced by [space-before-function-paren](https://eslint.style/rules/space-before-function-paren) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 space-in-parens deprecated

Replaced by [space-in-parens](https://eslint.style/rules/space-in-parens) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 space-infix-ops deprecated

Replaced by [space-infix-ops](https://eslint.style/rules/space-infix-ops) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 space-unary-ops deprecated

Replaced by [space-unary-ops](https://eslint.style/rules/space-unary-ops) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 spaced-comment deprecated

Replaced by [spaced-comment](https://eslint.style/rules/spaced-comment) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 switch-colon-spacing deprecated

Replaced by [switch-colon-spacing](https://eslint.style/rules/switch-colon-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 template-curly-spacing deprecated

Replaced by [template-curly-spacing](https://eslint.style/rules/template-curly-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 template-tag-spacing deprecated

Replaced by [template-tag-spacing](https://eslint.style/rules/template-tag-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 wrap-iife deprecated

Replaced by [wrap-iife](https://eslint.style/rules/wrap-iife) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 wrap-regex deprecated

Replaced by [wrap-regex](https://eslint.style/rules/wrap-regex) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

 yield-star-spacing deprecated

Replaced by [yield-star-spacing](https://eslint.style/rules/yield-star-spacing) in [@stylistic/eslint-plugin](https://eslint.style)

Categories:

❌

 🔧 Fix

 💡 Suggestions

## Removed

These rules from older versions of ESLint (before the [deprecation policy](/docs/latest/use/rule-deprecation) existed) have been replaced by newer rules:

 generator-star removed

Replaced by [generator-star-spacing](generator-star-spacing)

 global-strict removed

Replaced by [strict](strict)

 no-arrow-condition removed

Replaced by [no-confusing-arrow](no-confusing-arrow) or 
[no-constant-condition](no-constant-condition)

 no-comma-dangle removed

Replaced by [comma-dangle](comma-dangle)

 no-empty-class removed

Replaced by [no-empty-character-class](no-empty-character-class)

 no-empty-label removed

Replaced by [no-labels](no-labels)

 no-extra-strict removed

Replaced by [strict](strict)

 no-reserved-keys removed

Replaced by [quote-props](quote-props)

 no-space-before-semi removed

Replaced by [semi-spacing](semi-spacing)

 no-wrap-func removed

Replaced by [no-extra-parens](no-extra-parens)

 space-after-function-name removed

Replaced by [space-before-function-paren](space-before-function-paren)

 space-after-keywords removed

Replaced by [keyword-spacing](keyword-spacing)

 space-before-function-parentheses removed

Replaced by [space-before-function-paren](space-before-function-paren)

 space-before-keywords removed

Replaced by [keyword-spacing](keyword-spacing)

 space-in-brackets removed

Replaced by [object-curly-spacing](object-curly-spacing) or 
[array-bracket-spacing](array-bracket-spacing) or 
[computed-property-spacing](computed-property-spacing)

 space-return-throw-case removed

Replaced by [keyword-spacing](keyword-spacing)

 space-unary-word-ops removed

Replaced by [space-unary-ops](space-unary-ops)

 spaced-line-comment removed

Replaced by [spaced-comment](spaced-comment)

 valid-jsdoc removed

 require-jsdoc removed

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/pages/rules.md
                    
                
                )
