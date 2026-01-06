# no-void

Disallow `void` operators

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowAsStatement](#allowasstatement)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

The `void` operator takes an operand and returns `undefined`: `void expression` will evaluate `expression` and return `undefined`. It can be used to ignore any side effects `expression` may produce:

The common case of using `void` operator is to get a “pure” `undefined` value as prior to ES5 the `undefined` variable was mutable:

```
// will always return undefined
(function(){
    return void 0;
})();

// will return 1 in ES3 and undefined in ES5+
(function(){
    undefined = 1;
    return undefined;
})();

// will throw TypeError in ES5+
(function(){
    'use strict';
    undefined = 1;
})();
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

Copy code to clipboard

Another common case is to minify code as `void 0` is shorter than `undefined`:

```
foo = void 0;
foo = undefined;
1
2
```

Copy code to clipboard

When used with IIFE (immediately-invoked function expression), `void` can be used to force the function keyword to be treated as an expression instead of a declaration:

```
let foo = 1;
void function(){ foo = 1; }() // will assign foo a value of 1
+function(){ foo = 1; }() // same as above
1
2
3
```

Copy code to clipboard

```
function(){ foo = 1; }() // will throw SyntaxError
1
```

Copy code to clipboard

Some code styles prohibit `void` operator, marking it as non-obvious and hard to read.

## Rule Details

This rule aims to eliminate use of `void` operator.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdm9pZDogXCJlcnJvclwiKi9cblxudm9pZCBmb29cbnZvaWQgc29tZUZ1bmN0aW9uKCk7XG5cbmNvbnN0IGZvbyA9IHZvaWQgYmFyKCk7XG5mdW5jdGlvbiBiYXooKSB7XG4gICAgcmV0dXJuIHZvaWQgMDtcbn0ifQ==)

```
/*eslint no-void: "error"*/

void foo
void someFunction();

const foo = void bar();
function baz() {
    return void 0;
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
```

## Options

This rule has an object option:

- `allowAsStatement` set to `true` allows the `void` operator to be used as a statement (Default `false`).

### allowAsStatement

When `allowAsStatement` is set to true, the rule will not error on cases that the `void` operator is used as a statement, i.e. when it’s not used in an expression position, like in a variable assignment or a function return.

Examples of incorrect code for `{ "allowAsStatement": true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdm9pZDogW1wiZXJyb3JcIiwgeyBcImFsbG93QXNTdGF0ZW1lbnRcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IGZvbyA9IHZvaWQgYmFyKCk7XG5mdW5jdGlvbiBiYXooKSB7XG4gICAgcmV0dXJuIHZvaWQgMDtcbn0ifQ==)

```
/*eslint no-void: ["error", { "allowAsStatement": true }]*/

const foo = void bar();
function baz() {
    return void 0;
}
1
2
3
4
5
6
```

Examples of correct code for `{ "allowAsStatement": true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdm9pZDogW1wiZXJyb3JcIiwgeyBcImFsbG93QXNTdGF0ZW1lbnRcIjogdHJ1ZSB9XSovXG5cbnZvaWQgZm9vO1xudm9pZCBzb21lRnVuY3Rpb24oKTsifQ==)

```
/*eslint no-void: ["error", { "allowAsStatement": true }]*/

void foo;
void someFunction();
1
2
3
4
```

## When Not To Use It

If you intentionally use the `void` operator then you can disable this rule.

## Related Rules

- [no-undef-init](/docs/latest/rules/no-undef-init)
- [no-undefined](/docs/latest/rules/no-undefined)

## Version

This rule was introduced in ESLint v0.8.0.

## Further Reading

[void operator - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)
 developer.mozilla.org[O’Reilly Media - Technology and Business Training](https://oreilly.com/javascript/excerpts/javascript-good-parts/bad-parts.html)
 oreilly.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-void.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-void.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-void.md
                    
                
                )
