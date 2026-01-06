# prefer-arrow-callback

Require using arrow functions for callbacks

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowNamedFunctions](#allownamedfunctions)
  2. [allowUnboundThis](#allowunboundthis)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Arrow functions can be an attractive alternative to function expressions for callbacks or function arguments.

For example, arrow functions are automatically bound to their surrounding scope/context. This provides an alternative to the pre-ES6 standard of explicitly binding function expressions to achieve similar behavior.

Additionally, arrow functions are:

- 

less verbose, and easier to reason about.

- 

bound lexically regardless of where or when they are invoked.

## Rule Details

This rule locates function expressions used as callbacks or function arguments. An error will be produced for any that could be replaced by an arrow function without changing the result.

The following examples will be flagged:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1hcnJvdy1jYWxsYmFjazogXCJlcnJvclwiICovXG5cbmZvbyhmdW5jdGlvbihhKSB7IHJldHVybiBhOyB9KTsgLy8gRVJST1Jcbi8vIHByZWZlcjogZm9vKGEgPT4gYSlcblxuZm9vKGZ1bmN0aW9uKCkgeyByZXR1cm4gdGhpcy5hOyB9LmJpbmQodGhpcykpOyAvLyBFUlJPUlxuLy8gcHJlZmVyOiBmb28oKCkgPT4gdGhpcy5hKSJ9)

```
/* eslint prefer-arrow-callback: "error" */

foo(function(a) { return a; }); // ERROR
// prefer: foo(a => a)

foo(function() { return this.a; }.bind(this)); // ERROR
// prefer: foo(() => this.a)
1
2
3
4
5
6
7
```

Instances where an arrow function would not produce identical results will be ignored.

The following examples will not be flagged:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1hcnJvdy1jYWxsYmFjazogXCJlcnJvclwiICovXG5cbi8vIGFycm93IGZ1bmN0aW9uIGNhbGxiYWNrXG5mb28oYSA9PiBhKTsgLy8gT0tcblxuLy8gZ2VuZXJhdG9yIGFzIGNhbGxiYWNrXG5mb28oZnVuY3Rpb24qKCkgeyB5aWVsZDsgfSk7IC8vIE9LXG5cbi8vIGZ1bmN0aW9uIGV4cHJlc3Npb24gbm90IHVzZWQgYXMgY2FsbGJhY2sgb3IgZnVuY3Rpb24gYXJndW1lbnRcbmNvbnN0IGZvbyA9IGZ1bmN0aW9uIGZvbyhhKSB7IHJldHVybiBhOyB9OyAvLyBPS1xuXG4vLyB1bmJvdW5kIGZ1bmN0aW9uIGV4cHJlc3Npb24gY2FsbGJhY2tcbmZvbyhmdW5jdGlvbigpIHsgcmV0dXJuIHRoaXMuYTsgfSk7IC8vIE9LXG5cbi8vIHJlY3Vyc2l2ZSBuYW1lZCBmdW5jdGlvbiBjYWxsYmFja1xuZm9vKGZ1bmN0aW9uIGJhcihuKSB7IHJldHVybiBuICYmIG4gKyBiYXIobiAtIDEpOyB9KTsgLy8gT0sifQ==)

```
/* eslint prefer-arrow-callback: "error" */

// arrow function callback
foo(a => a); // OK

// generator as callback
foo(function*() { yield; }); // OK

// function expression not used as callback or function argument
const foo = function foo(a) { return a; }; // OK

// unbound function expression callback
foo(function() { return this.a; }); // OK

// recursive named function callback
foo(function bar(n) { return n && n + bar(n - 1); }); // OK
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

This rule additionally supports TypeScript type syntax.

Examples of incorrect TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBwcmVmZXItYXJyb3ctY2FsbGJhY2s6IFwiZXJyb3JcIiovXG5cbmZvbyhmdW5jdGlvbiBiYXIoYTogc3RyaW5nKSB7IGE7IH0pO1xuXG50ZXN0KCdmb28nLCBmdW5jdGlvbiAodGhpczogYW55KSB7fSk7In0=)

```
/*eslint prefer-arrow-callback: "error"*/

foo(function bar(a: string) { a; });

test('foo', function (this: any) {});
1
2
3
4
5
```

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBwcmVmZXItYXJyb3ctY2FsbGJhY2s6IFwiZXJyb3JcIiovXG5cbmZvbygoYTogc3RyaW5nKSA9PiBhKTtcblxuY29uc3QgZm9vID0gZnVuY3Rpb24gZm9vKGJhcjogYW55KSB7fTsifQ==)

```
/*eslint prefer-arrow-callback: "error"*/

foo((a: string) => a);

const foo = function foo(bar: any) {};
1
2
3
4
5
```

## Options

Access further control over this rule’s behavior via an options object.

Default: `{ allowNamedFunctions: false, allowUnboundThis: true }`

### allowNamedFunctions

By default `{ "allowNamedFunctions": false }`, this `boolean` option prohibits using named functions as callbacks or function arguments.

Changing this value to `true` will reverse this option’s behavior by allowing use of named functions without restriction.

`{ "allowNamedFunctions": true }`will not flag the following example:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1hcnJvdy1jYWxsYmFjazogWyBcImVycm9yXCIsIHsgXCJhbGxvd05hbWVkRnVuY3Rpb25zXCI6IHRydWUgfSBdICovXG5cbmZvbyhmdW5jdGlvbiBiYXIoKSB7fSk7In0=)

```
/* eslint prefer-arrow-callback: [ "error", { "allowNamedFunctions": true } ] */

foo(function bar() {});
1
2
3
```

Examples of incorrect TypeScript code for this rule with `{ "allowNamedFunctions": true }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgcHJlZmVyLWFycm93LWNhbGxiYWNrOiBbIFwiZXJyb3JcIiwgeyBcImFsbG93TmFtZWRGdW5jdGlvbnNcIjogdHJ1ZSB9IF0gKi9cblxuZm9vKGZ1bmN0aW9uKGE6IHN0cmluZykge30pOyJ9)

```
/* eslint prefer-arrow-callback: [ "error", { "allowNamedFunctions": true } ] */

foo(function(a: string) {});
1
2
3
```

Examples of correct TypeScript code for this rule with `{ "allowNamedFunctions": true }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgcHJlZmVyLWFycm93LWNhbGxiYWNrOiBbIFwiZXJyb3JcIiwgeyBcImFsbG93TmFtZWRGdW5jdGlvbnNcIjogdHJ1ZSB9IF0gKi9cblxuZm9vKGZ1bmN0aW9uIGJhcihhOiBzdHJpbmcpIHt9KTsifQ==)

```
/* eslint prefer-arrow-callback: [ "error", { "allowNamedFunctions": true } ] */

foo(function bar(a: string) {});
1
2
3
```

### allowUnboundThis

By default `{ "allowUnboundThis": true }`, this `boolean` option allows function expressions containing `this` to be used as callbacks, as long as the function in question has not been explicitly bound.

When set to `false` this option prohibits the use of function expressions as callbacks or function arguments entirely, without exception.

`{ "allowUnboundThis": false }`will flag the following examples:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1hcnJvdy1jYWxsYmFjazogWyBcImVycm9yXCIsIHsgXCJhbGxvd1VuYm91bmRUaGlzXCI6IGZhbHNlIH0gXSAqL1xuXG5mb28oZnVuY3Rpb24oKSB7IHRoaXMuYTsgfSk7XG5cbmZvbyhmdW5jdGlvbigpIHsgKCgpID0+IHRoaXMpOyB9KTtcblxuc29tZUFycmF5Lm1hcChmdW5jdGlvbihpdGVtKSB7IHJldHVybiB0aGlzLmRvU29tZXRoaW5nKGl0ZW0pOyB9LCBzb21lT2JqZWN0KTsifQ==)

```
/* eslint prefer-arrow-callback: [ "error", { "allowUnboundThis": false } ] */

foo(function() { this.a; });

foo(function() { (() => this); });

someArray.map(function(item) { return this.doSomething(item); }, someObject);
1
2
3
4
5
6
7
```

Examples of incorrect TypeScript code for this rule with `{ "allowUnboundThis": false }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgcHJlZmVyLWFycm93LWNhbGxiYWNrOiBbIFwiZXJyb3JcIiwgeyBcImFsbG93VW5ib3VuZFRoaXNcIjogZmFsc2UgfSBdICovXG5cbmZvbyhmdW5jdGlvbihhOiBzdHJpbmcpIHsgdGhpczsgfSk7XG5cbmZvbyhmdW5jdGlvbihhOiBzdHJpbmcpIHsgKCgpID0+IHRoaXMpOyB9KTsifQ==)

```
/* eslint prefer-arrow-callback: [ "error", { "allowUnboundThis": false } ] */

foo(function(a: string) { this; });

foo(function(a: string) { (() => this); });
1
2
3
4
5
```

## When Not To Use It

- 

In environments that have not yet adopted ES6 language features (ES3/5).

- 

In ES6+ environments that allow the use of function expressions when describing callbacks or function arguments.

## Version

This rule was introduced in ESLint v1.2.0.

## Further Reading

[Arrow function expressions - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-arrow-callback.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-arrow-callback.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-arrow-callback.md
                    
                
                )
