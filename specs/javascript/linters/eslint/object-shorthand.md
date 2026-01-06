# object-shorthand

Require or disallow method and property shorthand syntax for object literals

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [avoidQuotes](#avoidquotes)
  2. [ignoreConstructors](#ignoreconstructors)
  3. [methodsIgnorePattern](#methodsignorepattern)
  4. [avoidExplicitReturnArrows](#avoidexplicitreturnarrows)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

ECMAScript 6 provides a concise form for defining object literal methods and properties. This syntax can make defining complex object literals much cleaner.

Here are a few common examples using the ES5 syntax:

```
// properties
const foo = {
    x: x,
    y: y,
    z: z,
};

// methods
const bar = {
    a: function() {},
    b: function() {}
};
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
```

Copy code to clipboard

Now here are ES6 equivalents:

```
// properties
const foo = {x, y, z};

// methods
const bar = {
    a() {},
    b() {}
};
1
2
3
4
5
6
7
8
```

Copy code to clipboard

## Rule Details

This rule enforces the use of the shorthand syntax. This applies to all methods (including generators) defined in object literals and any properties defined where the key name matches name of the assigned variable.

Each of the following properties would warn:

```
/*eslint object-shorthand: "error"*/

const foo = {
    w: function() {},
    x: function *() {},
    [y]: function() {},
    z: z
};
1
2
3
4
5
6
7
8
```

Copy code to clipboard

In that case the expected syntax would have been:

```
/*eslint object-shorthand: "error"*/

const foo = {
    w() {},
    *x() {},
    [y]() {},
    z
};
1
2
3
4
5
6
7
8
```

Copy code to clipboard

This rule does not flag arrow functions inside of object literals. The following will not warn:

```
/*eslint object-shorthand: "error"*/

const foo = {
    x: (y) => y
};
1
2
3
4
5
```

Copy code to clipboard

## Options

The rule takes an option which specifies when it should be applied. It can be set to one of the following values:

- `"always"` (default) expects that the shorthand will be used whenever possible.
- `"methods"` ensures the method shorthand is used (also applies to generators).
- `"properties"` ensures the property shorthand is used (where the key and variable name match).
- `"never"` ensures that no property or method shorthand is used in any object literal.
- `"consistent"` ensures that either all shorthand or all long-form will be used in an object literal.
- `"consistent-as-needed"` ensures that either all shorthand or all long-form will be used in an object literal, but ensures all shorthand whenever possible.

You can set the option in configuration like this:

```
{
    "object-shorthand": ["error", "always"]
}
1
2
3
```

Copy code to clipboard

Additionally, the rule takes an optional object configuration:

- `"avoidQuotes": true` indicates that long-form syntax is preferred whenever the object key is a string literal (default: `false`). Note that this option can only be enabled when the string option is set to `"always"`, `"methods"`, or `"properties"`.
- `"ignoreConstructors": true` can be used to prevent the rule from reporting errors for constructor functions. (By default, the rule treats constructors the same way as other functions.) Note that this option can only be enabled when the string option is set to `"always"` or `"methods"`.
- `"methodsIgnorePattern"` (`string`) for methods whose names match this regex pattern, the method shorthand will not be enforced. Note that this option can only be used when the string option is set to `"always"` or `"methods"`.
- `"avoidExplicitReturnArrows": true` indicates that methods are preferred over explicit-return arrow functions for function properties. (By default, the rule allows either of these.) Note that this option can only be enabled when the string option is set to `"always"` or `"methods"`.

### avoidQuotes

```
{
    "object-shorthand": ["error", "always", { "avoidQuotes": true }]
}
1
2
3
```

Copy code to clipboard

Example of incorrect code for this rule with the `"always", { "avoidQuotes": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImF2b2lkUXVvdGVzXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgXCJiYXItYmF6XCIoKSB7fVxufTsifQ==)

```
/*eslint object-shorthand: ["error", "always", { "avoidQuotes": true }]*/

const foo = {
    "bar-baz"() {}
};
1
2
3
4
5
```

Example of correct code for this rule with the `"always", { "avoidQuotes": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImF2b2lkUXVvdGVzXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgXCJiYXItYmF6XCI6IGZ1bmN0aW9uKCkge30sXG4gICAgXCJxdXhcIjogcXV4XG59OyJ9)

```
/*eslint object-shorthand: ["error", "always", { "avoidQuotes": true }]*/

const foo = {
    "bar-baz": function() {},
    "qux": qux
};
1
2
3
4
5
6
```

### ignoreConstructors

```
{
    "object-shorthand": ["error", "always", { "ignoreConstructors": true }]
}
1
2
3
```

Copy code to clipboard

Example of correct code for this rule with the `"always", { "ignoreConstructors": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImlnbm9yZUNvbnN0cnVjdG9yc1wiOiB0cnVlIH1dKi9cblxuY29uc3QgZm9vID0ge1xuICAgIENvbnN0cnVjdG9yRnVuY3Rpb246IGZ1bmN0aW9uKCkge31cbn07In0=)

```
/*eslint object-shorthand: ["error", "always", { "ignoreConstructors": true }]*/

const foo = {
    ConstructorFunction: function() {}
};
1
2
3
4
5
```

### methodsIgnorePattern

Example of correct code for this rule with the `"always", { "methodsIgnorePattern": "^bar$" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcIm1ldGhvZHNJZ25vcmVQYXR0ZXJuXCI6IFwiXmJhciRcIiB9XSovXG5cbmNvbnN0IGZvbyA9IHtcbiAgICBiYXI6IGZ1bmN0aW9uKCkge31cbn07In0=)

```
/*eslint object-shorthand: ["error", "always", { "methodsIgnorePattern": "^bar$" }]*/

const foo = {
    bar: function() {}
};
1
2
3
4
5
```

### avoidExplicitReturnArrows

```
{
    "object-shorthand": ["error", "always", { "avoidExplicitReturnArrows": true }]
}
1
2
3
```

Copy code to clipboard

Example of incorrect code for this rule with the `"always", { "avoidExplicitReturnArrows": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImF2b2lkRXhwbGljaXRSZXR1cm5BcnJvd3NcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IGZvbyA9IHtcbiAgZm9vOiAoYmFyLCBiYXopID0+IHtcbiAgICByZXR1cm4gYmFyICsgYmF6O1xuICB9LFxuXG4gIHF1eDogKGZvb2JhcikgPT4ge1xuICAgIHJldHVybiBmb29iYXIgKiAyO1xuICB9XG59OyJ9)

```
/*eslint object-shorthand: ["error", "always", { "avoidExplicitReturnArrows": true }]*/

const foo = {
  foo: (bar, baz) => {
    return bar + baz;
  },

  qux: (foobar) => {
    return foobar * 2;
  }
};
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
```

Example of correct code for this rule with the `"always", { "avoidExplicitReturnArrows": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogW1wiZXJyb3JcIiwgXCJhbHdheXNcIiwgeyBcImF2b2lkRXhwbGljaXRSZXR1cm5BcnJvd3NcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IGZvbyA9IHtcbiAgZm9vKGJhciwgYmF6KSB7XG4gICAgcmV0dXJuIGJhciArIGJhejtcbiAgfSxcblxuICBxdXg6IGZvb2JhciA9PiBmb29iYXIgKiAyXG59OyJ9)

```
/*eslint object-shorthand: ["error", "always", { "avoidExplicitReturnArrows": true }]*/

const foo = {
  foo(bar, baz) {
    return bar + baz;
  },

  qux: foobar => foobar * 2
};
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

Example of incorrect code for this rule with the `"consistent"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogWzIsIFwiY29uc2lzdGVudFwiXSovXG5cbmNvbnN0IGZvbyA9IHtcbiAgICBhLFxuICAgIGI6IFwiZm9vXCIsXG59OyJ9)

```
/*eslint object-shorthand: [2, "consistent"]*/

const foo = {
    a,
    b: "foo",
};
1
2
3
4
5
6
```

Examples of correct code for this rule with the `"consistent"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogWzIsIFwiY29uc2lzdGVudFwiXSovXG5cbmNvbnN0IGZvbyA9IHtcbiAgICBhOiBhLFxuICAgIGI6IFwiZm9vXCJcbn07XG5cbmNvbnN0IGJhciA9IHtcbiAgICBhLFxuICAgIGIsXG59OyJ9)

```
/*eslint object-shorthand: [2, "consistent"]*/

const foo = {
    a: a,
    b: "foo"
};

const bar = {
    a,
    b,
};
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
```

Example of incorrect code with the `"consistent-as-needed"` option, which is very similar to `"consistent"`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgb2JqZWN0LXNob3J0aGFuZDogWzIsIFwiY29uc2lzdGVudC1hcy1uZWVkZWRcIl0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgYTogYSxcbiAgICBiOiBiLFxufTsifQ==)

```
/*eslint object-shorthand: [2, "consistent-as-needed"]*/

const foo = {
    a: a,
    b: b,
};
1
2
3
4
5
6
```

## When Not To Use It

Anyone not yet in an ES6 environment would not want to apply this rule. Others may find the terseness of the shorthand syntax harder to read and may not want to encourage it with this rule.

## Related Rules

- [no-useless-rename](/docs/latest/rules/no-useless-rename)

## Version

This rule was introduced in ESLint v0.20.0.

## Further Reading

[Object initializer - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/object-shorthand.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/object-shorthand.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/object-shorthand.md
                    
                
                )
