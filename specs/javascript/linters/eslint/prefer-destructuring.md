# prefer-destructuring

Require destructuring from arrays and/or objects

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Options](#options)

    1. [enforceForRenamedProperties](#enforceforrenamedproperties)

2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

With JavaScript ES6, a new syntax was added for creating variables from an array index or object property, called [destructuring](#further-reading). This rule enforces usage of destructuring instead of accessing a property through a member expression.

## Rule Details

### Options

This rule takes two arguments, both of which are objects. The first object parameter determines what types of destructuring the rule applies to.

In the first object, there are two properties, `array` and `object`, that can be used to turn on or off the destructuring requirement for each of those types independently. By default, both are `true`.

```
{
  "rules": {
    "prefer-destructuring": ["error", {
      "array": true,
      "object": true
    }]
  }
}
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

For example, the following configuration enforces only object destructuring, but not array destructuring:

```
{
  "rules": {
    "prefer-destructuring": ["error", {"object": true, "array": false}]
  }
}
1
2
3
4
5
```

Copy code to clipboard

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1kZXN0cnVjdHVyaW5nOiBcImVycm9yXCIgKi9cblxuLy8gV2l0aCBgYXJyYXlgIGVuYWJsZWRcbmNvbnN0IGZvbyA9IGFycmF5WzBdO1xuYmFyLmJheiA9IGFycmF5WzBdO1xuXG4vLyBXaXRoIGBvYmplY3RgIGVuYWJsZWRcbmNvbnN0IHF1eCA9IG9iamVjdC5xdXg7XG5jb25zdCBxdXV4ID0gb2JqZWN0WydxdXV4J107In0=)

```
/* eslint prefer-destructuring: "error" */

// With `array` enabled
const foo = array[0];
bar.baz = array[0];

// With `object` enabled
const qux = object.qux;
const quux = object['quux'];
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1kZXN0cnVjdHVyaW5nOiBcImVycm9yXCIgKi9cblxuLy8gV2l0aCBgYXJyYXlgIGVuYWJsZWRcbmNvbnN0IFsgZm9vIF0gPSBhcnJheTtcbmNvbnN0IGFyciA9IGFycmF5W3NvbWVJbmRleF07XG5bYmFyLmJhel0gPSBhcnJheTtcblxuXG4vLyBXaXRoIGBvYmplY3RgIGVuYWJsZWRcbmNvbnN0IHsgYmF6IH0gPSBvYmplY3Q7XG5cbmNvbnN0IG9iaiA9IG9iamVjdC5iYXI7XG5cbmxldCBiYXI7XG4oeyBiYXIgfSA9IG9iamVjdCk7In0=)

```
/* eslint prefer-destructuring: "error" */

// With `array` enabled
const [ foo ] = array;
const arr = array[someIndex];
[bar.baz] = array;

// With `object` enabled
const { baz } = object;

const obj = object.bar;

let bar;
({ bar } = object);
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
```

Alternatively, you can use separate configurations for different assignment types. The first argument accepts two other keys instead of `array` and `object`.

One key is `VariableDeclarator` and the other is `AssignmentExpression`, which can be used to control the destructuring requirement for each of those types independently. Each property is an object containing two properties, `array` and `object`, which can be used to control the destructuring requirement for each of `array` and `object` independently for variable declarations and assignment expressions. By default, `array` and `object` are set to `true` for both `VariableDeclarator` and `AssignmentExpression`.

```
{
  "rules": {
    "prefer-destructuring": ["error", {
      "VariableDeclarator": {
        "array": true,
        "object": true
      },
      "AssignmentExpression": {
        "array": true,
        "object": true
      }
    }]
  }
}
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
```

Copy code to clipboard

Examples of correct code when object destructuring in `VariableDeclarator` is enforced:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1kZXN0cnVjdHVyaW5nOiBbXCJlcnJvclwiLCB7VmFyaWFibGVEZWNsYXJhdG9yOiB7b2JqZWN0OiB0cnVlfX1dICovXG5jb25zdCB7YmFyOiBmb299ID0gb2JqZWN0OyJ9)

```
/* eslint prefer-destructuring: ["error", {VariableDeclarator: {object: true}}] */
const {bar: foo} = object;
1
2
```

Examples of correct code when array destructuring in `AssignmentExpression` is enforced:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZWZlci1kZXN0cnVjdHVyaW5nOiBbXCJlcnJvclwiLCB7QXNzaWdubWVudEV4cHJlc3Npb246IHthcnJheTogdHJ1ZX19XSAqL1xuW2Jhcl0gPSBhcnJheTsifQ==)

```
/* eslint prefer-destructuring: ["error", {AssignmentExpression: {array: true}}] */
[bar] = array;
1
2
```

#### enforceForRenamedProperties

The rule has a second object argument with a single key, `enforceForRenamedProperties`, which determines whether the `object` destructuring applies to renamed variables.

```
{
  "rules": {
    "prefer-destructuring": ["error",
    {
      "object": true
    },
    {
      "enforceForRenamedProperties": true
    }]
  }
}
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

Copy code to clipboard

Examples of incorrect code when `enforceForRenamedProperties` is enabled:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IFwicHJlZmVyLWRlc3RydWN0dXJpbmdcIjogW1wiZXJyb3JcIiwgeyBcIm9iamVjdFwiOiB0cnVlIH0sIHsgXCJlbmZvcmNlRm9yUmVuYW1lZFByb3BlcnRpZXNcIjogdHJ1ZSB9XSAqL1xuY29uc3QgZm9vID0gb2JqZWN0LmJhcjsifQ==)

```
/* eslint "prefer-destructuring": ["error", { "object": true }, { "enforceForRenamedProperties": true }] */
const foo = object.bar;
1
2
```

Examples of correct code when `enforceForRenamedProperties` is enabled:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IFwicHJlZmVyLWRlc3RydWN0dXJpbmdcIjogW1wiZXJyb3JcIiwgeyBcIm9iamVjdFwiOiB0cnVlIH0sIHsgXCJlbmZvcmNlRm9yUmVuYW1lZFByb3BlcnRpZXNcIjogdHJ1ZSB9XSAqL1xuY29uc3QgeyBiYXI6IGZvbyB9ID0gb2JqZWN0OyJ9)

```
/* eslint "prefer-destructuring": ["error", { "object": true }, { "enforceForRenamedProperties": true }] */
const { bar: foo } = object;
1
2
```

Examples of additional correct code when `enforceForRenamedProperties` is enabled:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IFwicHJlZmVyLWRlc3RydWN0dXJpbmdcIjogW1wiZXJyb3JcIiwgeyBcIm9iamVjdFwiOiB0cnVlIH0sIHsgXCJlbmZvcmNlRm9yUmVuYW1lZFByb3BlcnRpZXNcIjogdHJ1ZSB9XSAqL1xuY2xhc3MgQyB7XG4gICAgI3g7XG4gICAgZm9vKCkge1xuICAgICAgICBjb25zdCBiYXIgPSB0aGlzLiN4OyAvLyBwcml2YXRlIGlkZW50aWZpZXJzIGFyZSBub3QgYWxsb3dlZCBpbiBkZXN0cnVjdHVyaW5nXG4gICAgfVxufSJ9)

```
/* eslint "prefer-destructuring": ["error", { "object": true }, { "enforceForRenamedProperties": true }] */
class C {
    #x;
    foo() {
        const bar = this.#x; // private identifiers are not allowed in destructuring
    }
}
1
2
3
4
5
6
7
```

Note: It is not possible to determine if a variable will be referring to an object or an array at runtime. This rule therefore guesses the assignment type by checking whether the key being accessed is an integer. This can lead to the following possibly confusing situations:

- Accessing an object property whose key is an integer will fall under the category `array` destructuring.
- Accessing an array element through a computed index will fall under the category `object` destructuring.

The `--fix` option on the command line fixes only problems reported in variable declarations, and among them only those that fall under the category `object` destructuring. Furthermore, the name of the declared variable has to be the same as the name used for non-computed member access in the initializer. For example, `const foo = object.foo` can be automatically fixed by this rule. Problems that involve computed member access (e.g., `const foo = object[foo]`) or renamed properties (e.g., `const foo = object.bar`) are not automatically fixed.

## When Not To Use It

If you want to be able to access array indices or object properties directly, you can either configure the rule to your tastes or disable the rule entirely.

Additionally, if you intend to access large array indices directly, like:

```
const foo = array[100];
1
```

Copy code to clipboard

Then the `array` part of this rule is not recommended, as destructuring does not match this use case very well.

Or for non-iterable ‘array-like’ objects:

```
const $ = require('jquery');
const foo = $('body')[0];
const [bar] = $('body'); // fails with a TypeError
1
2
3
```

Copy code to clipboard

## Version

This rule was introduced in ESLint v3.13.0.

## Further Reading

[Destructuring assignment - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
 developer.mozilla.org[Destructuring and parameter handling in ECMAScript 6](https://2ality.com/2015/01/es6-destructuring.html)
 2ality.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-destructuring.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-destructuring.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-destructuring.md
                    
                
                )
