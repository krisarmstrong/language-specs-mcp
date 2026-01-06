# radix

Enforce the consistent use of the radix argument when using `parseInt()`

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [as-needed](#as-needed)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

When using the `parseInt()` function it is common to omit the second argument, the radix, and let the function try to determine from the first argument what type of number it is. By default, `parseInt()` will autodetect decimal and hexadecimal (via `0x` prefix). Prior to ECMAScript 5, `parseInt()` also autodetected octal literals, which caused problems because many developers assumed a leading `0` would be ignored.

This confusion led to the suggestion that you always use the radix parameter to `parseInt()` to eliminate unintended consequences. So instead of doing this:

```
const num = parseInt("071");      // 57
1
```

Copy code to clipboard

Do this:

```
const num = parseInt("071", 10);  // 71
1
```

Copy code to clipboard

ECMAScript 5 changed the behavior of `parseInt()` so that it no longer autodetects octal literals and instead treats them as decimal literals. However, the differences between hexadecimal and decimal interpretation of the first parameter causes many developers to continue using the radix parameter to ensure the string is interpreted in the intended way.

On the other hand, if the code is targeting only ES5-compliant environments passing the radix `10` may be redundant. In such a case you might want to disallow using such a radix.

## Rule Details

This rule is aimed at preventing the unintended conversion of a string to a number of a different base than intended or at preventing the redundant `10` radix if targeting modern environments only.

## Options

There are two options for this rule:

- `"always"` enforces providing a radix (default)
- `"as-needed"` disallows providing the `10` radix

### always

Examples of incorrect code for the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmFkaXg6IFwiZXJyb3JcIiovXG5cbmNvbnN0IG51bSA9IHBhcnNlSW50KFwiMDcxXCIpO1xuXG5jb25zdCBudW0xID0gcGFyc2VJbnQoc29tZVZhbHVlKTtcblxuY29uc3QgbnVtMiA9IHBhcnNlSW50KFwiMDcxXCIsIFwiYWJjXCIpO1xuXG5jb25zdCBudW0zID0gcGFyc2VJbnQoXCIwNzFcIiwgMzcpO1xuXG5jb25zdCBudW00ID0gcGFyc2VJbnQoKTsifQ==)

```
/*eslint radix: "error"*/

const num = parseInt("071");

const num1 = parseInt(someValue);

const num2 = parseInt("071", "abc");

const num3 = parseInt("071", 37);

const num4 = parseInt();
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

Examples of correct code for the default `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmFkaXg6IFwiZXJyb3JcIiovXG5cbmNvbnN0IG51bSA9IHBhcnNlSW50KFwiMDcxXCIsIDEwKTtcblxuY29uc3QgbnVtMSA9IHBhcnNlSW50KFwiMDcxXCIsIDgpO1xuXG5jb25zdCBudW0yID0gcGFyc2VGbG9hdChzb21lVmFsdWUpOyJ9)

```
/*eslint radix: "error"*/

const num = parseInt("071", 10);

const num1 = parseInt("071", 8);

const num2 = parseFloat(someValue);
1
2
3
4
5
6
7
```

### as-needed

Examples of incorrect code for the `"as-needed"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmFkaXg6IFtcImVycm9yXCIsIFwiYXMtbmVlZGVkXCJdKi9cblxuY29uc3QgbnVtID0gcGFyc2VJbnQoXCIwNzFcIiwgMTApO1xuXG5jb25zdCBudW0xID0gcGFyc2VJbnQoXCIwNzFcIiwgXCJhYmNcIik7XG5cbmNvbnN0IG51bTIgPSBwYXJzZUludCgpOyJ9)

```
/*eslint radix: ["error", "as-needed"]*/

const num = parseInt("071", 10);

const num1 = parseInt("071", "abc");

const num2 = parseInt();
1
2
3
4
5
6
7
```

Examples of correct code for the `"as-needed"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmFkaXg6IFtcImVycm9yXCIsIFwiYXMtbmVlZGVkXCJdKi9cblxuY29uc3QgbnVtID0gcGFyc2VJbnQoXCIwNzFcIik7XG5cbmNvbnN0IG51bTEgPSBwYXJzZUludChcIjA3MVwiLCA4KTtcblxuY29uc3QgbnVtMiA9IHBhcnNlRmxvYXQoc29tZVZhbHVlKTsifQ==)

```
/*eslint radix: ["error", "as-needed"]*/

const num = parseInt("071");

const num1 = parseInt("071", 8);

const num2 = parseFloat(someValue);
1
2
3
4
5
6
7
```

## When Not To Use It

If you don’t want to enforce either presence or omission of the `10` radix value you can turn this rule off.

## Version

This rule was introduced in ESLint v0.0.7.

## Further Reading

[parseInt Radix](https://davidwalsh.name/parseint-radix)
 davidwalsh.name

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/radix.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/radix.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/radix.md
                    
                
                )
