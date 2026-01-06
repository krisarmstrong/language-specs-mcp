# func-names

Require or disallow named `function` expressions

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [as-needed](#as-needed)
  3. [never](#never)
  4. [generators](#generators)

3. [Compatibility](#compatibility)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

A pattern that’s becoming more common is to give function expressions names to aid in debugging. For example:

```
Foo.prototype.bar = function bar() {};
1
```

Copy code to clipboard

Adding the second `bar` in the above example is optional. If you leave off the function name then when the function throws an exception you are likely to get something similar to `anonymous function` in the stack trace. If you provide the optional name for a function expression then you will get the name of the function expression in the stack trace.

## Rule Details

This rule can enforce or disallow the use of named function expressions.

## Options

This rule has a string option:

- `"always"` (default) requires function expressions to have a name.
- `"as-needed"` requires function expressions to have a name, if the name isn’t assigned automatically per the ECMAScript specification.
- `"never"` disallows named function expressions, except in recursive functions, where a name is needed.

This rule has an object option:

- `"generators": "always" | "as-needed" | "never"`

  - `"always"` require named generators.
  - `"as-needed"` require named generators if the name isn’t assigned automatically per the ECMAScript specification.
  - `"never"` disallow named generators where possible.

When a value for `generators` is not provided the behavior for generator functions falls back to the base option.

Please note that `"always"` and `"as-needed"` require function expressions and function declarations in `export default` declarations to have a name.

### always

Examples of incorrect code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5Gb28ucHJvdG90eXBlLmJhciA9IGZ1bmN0aW9uKCkge307XG5cbmNvbnN0IGNhdCA9IHtcbiAgbWVvdzogZnVuY3Rpb24oKSB7fVxufVxuXG4oZnVuY3Rpb24oKSB7XG4gICAgLy8gLi4uXG59KCkpXG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uKCkge30ifQ==)

```
/*eslint func-names: ["error", "always"]*/

Foo.prototype.bar = function() {};

const cat = {
  meow: function() {}
}

(function() {
    // ...
}())

export default function() {}
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
```

Examples of correct code for this rule with the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5Gb28ucHJvdG90eXBlLmJhciA9IGZ1bmN0aW9uIGJhcigpIHt9O1xuXG5jb25zdCBjYXQgPSB7XG4gIG1lb3coKSB7fVxufVxuXG4oZnVuY3Rpb24gYmFyKCkge1xuICAgIC8vIC4uLlxufSgpKVxuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBmb28oKSB7fSJ9)

```
/*eslint func-names: ["error", "always"]*/

Foo.prototype.bar = function bar() {};

const cat = {
  meow() {}
}

(function bar() {
    // ...
}())

export default function foo() {}
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
```

### as-needed

ECMAScript 6 introduced a `name` property on all functions. The value of `name` is determined by evaluating the code around the function to see if a name can be inferred. For example, a function assigned to a variable will automatically have a `name` property equal to the name of the variable. The value of `name` is then used in stack traces for easier debugging.

Examples of incorrect code for this rule with the `"as-needed"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIl0qL1xuXG5Gb28ucHJvdG90eXBlLmJhciA9IGZ1bmN0aW9uKCkge307XG5cbihmdW5jdGlvbigpIHtcbiAgICAvLyAuLi5cbn0oKSlcblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24oKSB7fSJ9)

```
/*eslint func-names: ["error", "as-needed"]*/

Foo.prototype.bar = function() {};

(function() {
    // ...
}())

export default function() {}
1
2
3
4
5
6
7
8
9
```

Examples of correct code for this rule with the `"as-needed"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIl0qL1xuXG5jb25zdCBiYXIgPSBmdW5jdGlvbigpIHt9O1xuXG5jb25zdCBjYXQgPSB7XG4gIG1lb3c6IGZ1bmN0aW9uKCkge31cbn1cblxuY2xhc3MgQyB7XG4gICAgI2JhciA9IGZ1bmN0aW9uKCkge307XG4gICAgYmF6ID0gZnVuY3Rpb24oKSB7fTtcbn1cblxucXV1eCA/Pz0gZnVuY3Rpb24oKSB7fTtcblxuKGZ1bmN0aW9uIGJhcigpIHtcbiAgICAvLyAuLi5cbn0oKSlcblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gZm9vKCkge30ifQ==)

```
/*eslint func-names: ["error", "as-needed"]*/

const bar = function() {};

const cat = {
  meow: function() {}
}

class C {
    #bar = function() {};
    baz = function() {};
}

quux ??= function() {};

(function bar() {
    // ...
}())

export default function foo() {}
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
17
18
19
20
```

### never

Examples of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbkZvby5wcm90b3R5cGUuYmFyID0gZnVuY3Rpb24gYmFyKCkge307XG5cbihmdW5jdGlvbiBiYXIoKSB7XG4gICAgLy8gLi4uXG59KCkpIn0=)

```
/*eslint func-names: ["error", "never"]*/

Foo.prototype.bar = function bar() {};

(function bar() {
    // ...
}())
1
2
3
4
5
6
7
```

Examples of correct code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbkZvby5wcm90b3R5cGUuYmFyID0gZnVuY3Rpb24oKSB7fTtcblxuKGZ1bmN0aW9uKCkge1xuICAgIC8vIC4uLlxufSgpKSJ9)

```
/*eslint func-names: ["error", "never"]*/

Foo.prototype.bar = function() {};

(function() {
    // ...
}())
1
2
3
4
5
6
7
```

### generators

Examples of incorrect code for this rule with the `"always", { "generators": "as-needed" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImdlbmVyYXRvcnNcIjogXCJhcy1uZWVkZWRcIiB9XSovXG5cbihmdW5jdGlvbiooKSB7XG4gICAgLy8gLi4uXG59KCkpIn0=)

```
/*eslint func-names: ["error", "always", { "generators": "as-needed" }]*/

(function*() {
    // ...
}())
1
2
3
4
5
```

Examples of correct code for this rule with the `"always", { "generators": "as-needed" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImdlbmVyYXRvcnNcIjogXCJhcy1uZWVkZWRcIiB9XSovXG5cbmNvbnN0IGZvbyA9IGZ1bmN0aW9uKigpIHt9OyJ9)

```
/*eslint func-names: ["error", "always", { "generators": "as-needed" }]*/

const foo = function*() {};
1
2
3
```

Examples of incorrect code for this rule with the `"always", { "generators": "never" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImdlbmVyYXRvcnNcIjogXCJuZXZlclwiIH1dKi9cblxuY29uc3QgZm9vID0gYmFyKGZ1bmN0aW9uICpiYXooKSB7fSk7In0=)

```
/*eslint func-names: ["error", "always", { "generators": "never" }]*/

const foo = bar(function *baz() {});
1
2
3
```

Examples of correct code for this rule with the `"always", { "generators": "never" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImdlbmVyYXRvcnNcIjogXCJuZXZlclwiIH1dKi9cblxuY29uc3QgZm9vID0gYmFyKGZ1bmN0aW9uICooKSB7fSk7In0=)

```
/*eslint func-names: ["error", "always", { "generators": "never" }]*/

const foo = bar(function *() {});
1
2
3
```

Examples of incorrect code for this rule with the `"as-needed", { "generators": "never" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIiwgeyBcImdlbmVyYXRvcnNcIjogXCJuZXZlclwiIH1dKi9cblxuY29uc3QgZm9vID0gYmFyKGZ1bmN0aW9uICpiYXooKSB7fSk7In0=)

```
/*eslint func-names: ["error", "as-needed", { "generators": "never" }]*/

const foo = bar(function *baz() {});
1
2
3
```

Examples of correct code for this rule with the `"as-needed", { "generators": "never" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIiwgeyBcImdlbmVyYXRvcnNcIjogXCJuZXZlclwiIH1dKi9cblxuY29uc3QgZm9vID0gYmFyKGZ1bmN0aW9uICooKSB7fSk7In0=)

```
/*eslint func-names: ["error", "as-needed", { "generators": "never" }]*/

const foo = bar(function *() {});
1
2
3
```

Examples of incorrect code for this rule with the `"never", { "generators": "always" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJuZXZlclwiLCB7IFwiZ2VuZXJhdG9yc1wiOiBcImFsd2F5c1wiIH1dKi9cblxuY29uc3QgZm9vID0gYmFyKGZ1bmN0aW9uICooKSB7fSk7In0=)

```
/*eslint func-names: ["error", "never", { "generators": "always" }]*/

const foo = bar(function *() {});
1
2
3
```

Examples of correct code for this rule with the `"never", { "generators": "always" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZnVuYy1uYW1lczogW1wiZXJyb3JcIiwgXCJuZXZlclwiLCB7IFwiZ2VuZXJhdG9yc1wiOiBcImFsd2F5c1wiIH1dKi9cblxuY29uc3QgZm9vID0gYmFyKGZ1bmN0aW9uICpiYXooKSB7fSk7In0=)

```
/*eslint func-names: ["error", "never", { "generators": "always" }]*/

const foo = bar(function *baz() {});
1
2
3
```

## Compatibility

- JSCS: [requireAnonymousFunctions](https://jscs-dev.github.io/rule/requireAnonymousFunctions)
- JSCS: [disallowAnonymousFunctions](https://jscs-dev.github.io/rule/disallowAnonymousFunctions)

## Version

This rule was introduced in ESLint v0.4.0.

## Further Reading

[Functions Explained - Mark Daggett’s Blog](https://web.archive.org/web/20201112040809/http://markdaggett.com/blog/2013/02/15/functions-explained/)
 web.archive.org[The names of functions in ES6](https://2ality.com/2015/09/function-names-es6.html)
 2ality.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/func-names.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/func-names.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/func-names.md
                    
                
                )
