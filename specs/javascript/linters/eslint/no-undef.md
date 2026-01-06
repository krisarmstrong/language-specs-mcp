# no-undef

Disallow the use of undeclared variables unless mentioned in `/*global */` comments

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [typeof](#typeof)

3. [When Not To Use It](#when-not-to-use-it)
4. [Compatibility](#compatibility)
5. [Handled by TypeScript](#handled_by_typescript)
6. [Related Rules](#related-rules)
7. [Version](#version)
8. [Resources](#resources)

This rule can help you locate potential ReferenceErrors resulting from misspellings of variable and parameter names, or accidental implicit globals (for example, from forgetting the `var` keyword in a `for` loop initializer).

## Rule Details

Any reference to an undeclared variable causes a warning, unless the variable is explicitly mentioned in a `/*global ...*/` comment, or specified in the [globals key in the configuration file](../use/configure/language-options#specifying-globals). A common use case for these is if you intentionally use globals that are defined elsewhere (e.g. in a script sourced from HTML).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWY6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IHNvbWVGdW5jdGlvbigpO1xuY29uc3QgYmFyID0gYSArIDE7In0=)

```
/*eslint no-undef: "error"*/

const foo = someFunction();
const bar = a + 1;
1
2
3
4
```

Examples of correct code for this rule with `global` declaration:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgc29tZUZ1bmN0aW9uLCBhKi9cbi8qZXNsaW50IG5vLXVuZGVmOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSBzb21lRnVuY3Rpb24oKTtcbmNvbnN0IGJhciA9IGEgKyAxOyJ9)

```
/*global someFunction, a*/
/*eslint no-undef: "error"*/

const foo = someFunction();
const bar = a + 1;
1
2
3
4
5
```

Note that this rule does not disallow assignments to read-only global variables. See [no-global-assign](no-global-assign) if you also want to disallow those assignments.

This rule also does not disallow redeclarations of global variables. See [no-redeclare](no-redeclare) if you also want to disallow those redeclarations.

## Options

- `typeof` set to true will warn for variables used inside typeof check (Default false).

### typeof

Examples of correct code for the default `{ "typeof": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWY6IFwiZXJyb3JcIiovXG5cbmlmICh0eXBlb2YgVW5kZWZpbmVkSWRlbnRpZmllciA9PT0gXCJ1bmRlZmluZWRcIikge1xuICAgIC8vIGRvIHNvbWV0aGluZyAuLi5cbn0ifQ==)

```
/*eslint no-undef: "error"*/

if (typeof UndefinedIdentifier === "undefined") {
    // do something ...
}
1
2
3
4
5
```

You can use this option if you want to prevent `typeof` check on a variable which has not been declared.

Examples of incorrect code for the `{ "typeof": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWY6IFtcImVycm9yXCIsIHsgXCJ0eXBlb2ZcIjogdHJ1ZSB9XSAqL1xuXG5pZih0eXBlb2YgYSA9PT0gXCJzdHJpbmdcIil7fSJ9)

```
/*eslint no-undef: ["error", { "typeof": true }] */

if(typeof a === "string"){}
1
2
3
```

Examples of correct code for the `{ "typeof": true }` option with `global` declaration:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgYSovXG4vKmVzbGludCBuby11bmRlZjogW1wiZXJyb3JcIiwgeyBcInR5cGVvZlwiOiB0cnVlIH1dICovXG5cbmlmKHR5cGVvZiBhID09PSBcInN0cmluZ1wiKXt9In0=)

```
/*global a*/
/*eslint no-undef: ["error", { "typeof": true }] */

if(typeof a === "string"){}
1
2
3
4
```

## When Not To Use It

If explicit declaration of global variables is not to your taste.

## Compatibility

This rule provides compatibility with treatment of global variables in [JSHint](http://jshint.com/) and [JSLint](http://www.jslint.com).

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Related Rules

- [no-global-assign](/docs/latest/rules/no-global-assign)
- [no-redeclare](/docs/latest/rules/no-redeclare)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-undef.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-undef.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-undef.md
                    
                
                )
