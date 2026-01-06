# no-undefined

Disallow the use of `undefined` as an identifier

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

The `undefined` variable in JavaScript is actually a property of the global object. As such, in ECMAScript 3 it was possible to overwrite the value of `undefined`. While ECMAScript 5 disallows overwriting `undefined`, it’s still possible to shadow `undefined`, such as:

```
function doSomething(data) {
    const undefined = "hi";

    // doesn't do what you think it does
    if (data === undefined) {
        // ...
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
```

Copy code to clipboard

Because `undefined` can be overwritten or shadowed, reading `undefined` can give an unexpected value. (This is not the case for `null`, which is a keyword that always produces the same value.) To guard against this, you can avoid all uses of `undefined`, which is what some style guides recommend and what this rule enforces. Those style guides then also recommend:

- Variables that should be `undefined` are simply left uninitialized. (All uninitialized variables automatically get the value of `undefined` in JavaScript.)
- Checking if a value is `undefined` should be done with `typeof`.
- Using the `void` operator to generate the value of `undefined` if necessary.

As an alternative, you can use the [no-global-assign](no-global-assign) and [no-shadow-restricted-names](no-shadow-restricted-names) rules to prevent `undefined` from being shadowed or assigned a different value. This ensures that `undefined` will always hold its original, expected value.

## Rule Details

This rule aims to eliminate the use of `undefined`, and as such, generates a warning whenever it is used.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWZpbmVkOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSB1bmRlZmluZWQ7XG5cbmNvbnN0IHVuZGVmaW5lZCA9IFwiZm9vXCI7XG5cbmlmIChmb28gPT09IHVuZGVmaW5lZCkge1xuICAgIC8vIC4uLlxufVxuXG5mdW5jdGlvbiBiYXoodW5kZWZpbmVkKSB7XG4gICAgLy8gLi4uXG59XG5cbmJhcih1bmRlZmluZWQsIFwibG9yZW1cIik7In0=)

```
/*eslint no-undefined: "error"*/

const foo = undefined;

const undefined = "foo";

if (foo === undefined) {
    // ...
}

function baz(undefined) {
    // ...
}

bar(undefined, "lorem");
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5kZWZpbmVkOiBcImVycm9yXCIqL1xuXG5jb25zdCBmb28gPSB2b2lkIDA7XG5cbmNvbnN0IFVuZGVmaW5lZCA9IFwiZm9vXCI7XG5cbmlmICh0eXBlb2YgZm9vID09PSBcInVuZGVmaW5lZFwiKSB7XG4gICAgLy8gLi4uXG59XG5cbmdsb2JhbC51bmRlZmluZWQgPSBcImZvb1wiO1xuXG5iYXIodm9pZCAwLCBcImxvcmVtXCIpOyJ9)

```
/*eslint no-undefined: "error"*/

const foo = void 0;

const Undefined = "foo";

if (typeof foo === "undefined") {
    // ...
}

global.undefined = "foo";

bar(void 0, "lorem");
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

## When Not To Use It

If you want to allow the use of `undefined` in your code, then you can safely turn this rule off.

## Related Rules

- [no-undef-init](/docs/latest/rules/no-undef-init)
- [no-void](/docs/latest/rules/no-void)
- [no-shadow-restricted-names](/docs/latest/rules/no-shadow-restricted-names)
- [no-global-assign](/docs/latest/rules/no-global-assign)

## Version

This rule was introduced in ESLint v0.7.1.

## Further Reading

[undefined - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 developer.mozilla.org[Understanding JavaScript’s ‘undefined’](https://javascriptweblog.wordpress.com/2010/08/16/understanding-undefined-and-preventing-referenceerrors/)
 javascriptweblog.wordpress.com[Annotated ES5](https://es5.github.io/#x15.1.1.3)
 es5.github.io

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-undefined.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-undefined.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-undefined.md
                    
                
                )
