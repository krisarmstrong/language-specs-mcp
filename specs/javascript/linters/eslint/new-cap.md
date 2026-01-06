# new-cap

Require constructor names to begin with a capital letter

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [newIsCap](#newiscap)
  2. [capIsNew](#capisnew)
  3. [newIsCapExceptions](#newiscapexceptions)
  4. [newIsCapExceptionPattern](#newiscapexceptionpattern)
  5. [capIsNewExceptions](#capisnewexceptions)
  6. [capIsNewExceptionPattern](#capisnewexceptionpattern)
  7. [properties](#properties)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

The `new` operator in JavaScript creates a new instance of a particular type of object. That type of object is represented by a constructor function. Since constructor functions are just regular functions, the only defining characteristic is that `new` is being used as part of the call. Native JavaScript functions begin with an uppercase letter to distinguish those functions that are to be used as constructors from functions that are not. Many style guides recommend following this pattern to more easily determine which functions are to be used as constructors.

```
const friend = new Person();
1
```

Copy code to clipboard

## Rule Details

This rule requires constructor names to begin with a capital letter. Certain built-in identifiers are exempt from this rule. These identifiers are:

- `Array`
- `Boolean`
- `Date`
- `Error`
- `Function`
- `Number`
- `Object`
- `RegExp`
- `String`
- `Symbol`
- `BigInt`

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24gZm9vKGFyZykge1xuICAgIHJldHVybiBCb29sZWFuKGFyZyk7XG59In0=)

```
/*eslint new-cap: "error"*/

function foo(arg) {
    return Boolean(arg);
}
1
2
3
4
5
```

## Options

This rule has an object option:

- `"newIsCap": true` (default) requires all `new` operators to be called with uppercase-started functions.
- `"newIsCap": false` allows `new` operators to be called with lowercase-started or uppercase-started functions.
- `"capIsNew": true` (default) requires all uppercase-started functions to be called with `new` operators.
- `"capIsNew": false` allows uppercase-started functions to be called without `new` operators.
- `"newIsCapExceptions"` allows specified lowercase-started function names to be called with the `new` operator.
- `"newIsCapExceptionPattern"` allows any lowercase-started function names that match the specified regex pattern to be called with the `new` operator.
- `"capIsNewExceptions"` allows specified uppercase-started function names to be called without the `new` operator.
- `"capIsNewExceptionPattern"` allows any uppercase-started function names that match the specified regex pattern to be called without the `new` operator.
- `"properties": true` (default) enables checks on object properties.
- `"properties": false` disables checks on object properties.

### newIsCap

Examples of incorrect code for this rule with the default `{ "newIsCap": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcIm5ld0lzQ2FwXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmcmllbmQgPSBuZXcgcGVyc29uKCk7In0=)

```
/*eslint new-cap: ["error", { "newIsCap": true }]*/

const friend = new person();
1
2
3
```

Examples of correct code for this rule with the default `{ "newIsCap": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcIm5ld0lzQ2FwXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmcmllbmQgPSBuZXcgUGVyc29uKCk7In0=)

```
/*eslint new-cap: ["error", { "newIsCap": true }]*/

const friend = new Person();
1
2
3
```

Examples of correct code for this rule with the `{ "newIsCap": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcIm5ld0lzQ2FwXCI6IGZhbHNlIH1dKi9cblxuY29uc3QgZnJpZW5kID0gbmV3IHBlcnNvbigpOyJ9)

```
/*eslint new-cap: ["error", { "newIsCap": false }]*/

const friend = new person();
1
2
3
```

### capIsNew

Examples of incorrect code for this rule with the default `{ "capIsNew": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3XCI6IHRydWUgfV0qL1xuXG5jb25zdCBjb2xsZWFndWUgPSBQZXJzb24oKTsifQ==)

```
/*eslint new-cap: ["error", { "capIsNew": true }]*/

const colleague = Person();
1
2
3
```

Examples of correct code for this rule with the default `{ "capIsNew": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3XCI6IHRydWUgfV0qL1xuXG5jb25zdCBjb2xsZWFndWUgPSBuZXcgUGVyc29uKCk7In0=)

```
/*eslint new-cap: ["error", { "capIsNew": true }]*/

const colleague = new Person();
1
2
3
```

Examples of correct code for this rule with the `{ "capIsNew": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3XCI6IGZhbHNlIH1dKi9cblxuY29uc3QgY29sbGVhZ3VlID0gUGVyc29uKCk7In0=)

```
/*eslint new-cap: ["error", { "capIsNew": false }]*/

const colleague = Person();
1
2
3
```

### newIsCapExceptions

Examples of additional correct code for this rule with the `{ "newIsCapExceptions": ["events"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcIm5ld0lzQ2FwRXhjZXB0aW9uc1wiOiBbXCJldmVudHNcIl0gfV0qL1xuXG5jb25zdCBldmVudHMgPSByZXF1aXJlKCdldmVudHMnKTtcblxuY29uc3QgZW1pdHRlciA9IG5ldyBldmVudHMoKTsifQ==)

```
/*eslint new-cap: ["error", { "newIsCapExceptions": ["events"] }]*/

const events = require('events');

const emitter = new events();
1
2
3
4
5
```

### newIsCapExceptionPattern

Examples of additional correct code for this rule with the `{ "newIsCapExceptionPattern": "^person\\.." }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcIm5ld0lzQ2FwRXhjZXB0aW9uUGF0dGVyblwiOiBcIl5wZXJzb25cXFxcLi5cIiB9XSovXG5cbmNvbnN0IGZyaWVuZCA9IG5ldyBwZXJzb24uYWNxdWFpbnRhbmNlKCk7XG5cbmNvbnN0IGJlc3RGcmllbmQgPSBuZXcgcGVyc29uLmZyaWVuZCgpOyJ9)

```
/*eslint new-cap: ["error", { "newIsCapExceptionPattern": "^person\\.." }]*/

const friend = new person.acquaintance();

const bestFriend = new person.friend();
1
2
3
4
5
```

Examples of additional correct code for this rule with the `{ "newIsCapExceptionPattern": "\\.bar$" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcIm5ld0lzQ2FwRXhjZXB0aW9uUGF0dGVyblwiOiBcIlxcXFwuYmFyJFwiIH1dKi9cblxuY29uc3QgZnJpZW5kID0gbmV3IHBlcnNvbi5iYXIoKTsifQ==)

```
/*eslint new-cap: ["error", { "newIsCapExceptionPattern": "\\.bar$" }]*/

const friend = new person.bar();
1
2
3
```

### capIsNewExceptions

Examples of additional correct code for this rule with the `{ "capIsNewExceptions": ["Person"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3RXhjZXB0aW9uc1wiOiBbXCJQZXJzb25cIl0gfV0qL1xuXG5mdW5jdGlvbiBmb28oYXJnKSB7XG4gICAgcmV0dXJuIFBlcnNvbihhcmcpO1xufSJ9)

```
/*eslint new-cap: ["error", { "capIsNewExceptions": ["Person"] }]*/

function foo(arg) {
    return Person(arg);
}
1
2
3
4
5
```

### capIsNewExceptionPattern

Examples of additional correct code for this rule with the `{ "capIsNewExceptionPattern": "^person\\.." }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3RXhjZXB0aW9uUGF0dGVyblwiOiBcIl5wZXJzb25cXFxcLi5cIiB9XSovXG5cbmNvbnN0IGZyaWVuZCA9IHBlcnNvbi5BY3F1YWludGFuY2UoKTtcbmNvbnN0IGJlc3RGcmllbmQgPSBwZXJzb24uRnJpZW5kKCk7In0=)

```
/*eslint new-cap: ["error", { "capIsNewExceptionPattern": "^person\\.." }]*/

const friend = person.Acquaintance();
const bestFriend = person.Friend();
1
2
3
4
```

Examples of additional correct code for this rule with the `{ "capIsNewExceptionPattern": "\\.Bar$" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3RXhjZXB0aW9uUGF0dGVyblwiOiBcIlxcXFwuQmFyJFwiIH1dKi9cblxuZm9vLkJhcigpOyJ9)

```
/*eslint new-cap: ["error", { "capIsNewExceptionPattern": "\\.Bar$" }]*/

foo.Bar();
1
2
3
```

Examples of additional correct code for this rule with the `{ "capIsNewExceptionPattern": "^Foo" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcImNhcElzTmV3RXhjZXB0aW9uUGF0dGVyblwiOiBcIl5Gb29cIiB9XSovXG5cbmNvbnN0IHggPSBGb28oNDIpO1xuXG5jb25zdCB5ID0gRm9vYmFyKDQyKTtcblxuY29uc3QgeiA9IEZvby5CYXIoNDIpOyJ9)

```
/*eslint new-cap: ["error", { "capIsNewExceptionPattern": "^Foo" }]*/

const x = Foo(42);

const y = Foobar(42);

const z = Foo.Bar(42);
1
2
3
4
5
6
7
```

### properties

Examples of incorrect code for this rule with the default `{ "properties": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcInByb3BlcnRpZXNcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IGZyaWVuZCA9IG5ldyBwZXJzb24uYWNxdWFpbnRhbmNlKCk7In0=)

```
/*eslint new-cap: ["error", { "properties": true }]*/

const friend = new person.acquaintance();
1
2
3
```

Examples of correct code for this rule with the default `{ "properties": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcInByb3BlcnRpZXNcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IGZyaWVuZCA9IG5ldyBwZXJzb24uQWNxdWFpbnRhbmNlKCk7In0=)

```
/*eslint new-cap: ["error", { "properties": true }]*/

const friend = new person.Acquaintance();
1
2
3
```

Examples of correct code for this rule with the `{ "properties": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbmV3LWNhcDogW1wiZXJyb3JcIiwgeyBcInByb3BlcnRpZXNcIjogZmFsc2UgfV0qL1xuXG5jb25zdCBmcmllbmQgPSBuZXcgcGVyc29uLmFjcXVhaW50YW5jZSgpOyJ9)

```
/*eslint new-cap: ["error", { "properties": false }]*/

const friend = new person.acquaintance();
1
2
3
```

## When Not To Use It

If you have conventions that don’t require an uppercase letter for constructors, or don’t require capitalized functions be only used as constructors, turn this rule off.

## Version

This rule was introduced in ESLint v0.0.3-0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/new-cap.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/new-cap.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/new-cap.md
                    
                
                )
