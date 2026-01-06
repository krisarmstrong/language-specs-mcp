# no-shadow-restricted-names

Disallow identifiers from shadowing restricted names

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [reportGlobalThis](#reportglobalthis)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

ES2020 §18.1 Value Properties of the Global Object (`globalThis`, `NaN`, `Infinity`, `undefined`) as well as strict mode restricted identifiers `eval` and `arguments` are considered to be restricted names in JavaScript. Defining them to mean something else can have unintended consequences and confuse others reading the code. For example, there’s nothing preventing you from writing:

```
const undefined = "foo";
1
```

Copy code to clipboard

Then any code used within the same scope would not get the global `undefined`, but rather the local version with a very different meaning.

## Rule Details

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIE5hTigpe31cblxuIWZ1bmN0aW9uKEluZmluaXR5KXt9O1xuXG5jb25zdCB1bmRlZmluZWQgPSA1O1xuXG50cnkge30gY2F0Y2goZXZhbCl7fSJ9)

```
/*eslint no-shadow-restricted-names: "error"*/

function NaN(){}

!function(Infinity){};

const undefined = 5;

try {} catch(eval){}
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFwiZXJyb3JcIiovXG5cbmltcG9ydCBOYU4gZnJvbSBcImZvb1wiO1xuXG5pbXBvcnQgeyB1bmRlZmluZWQgfSBmcm9tIFwiYmFyXCI7XG5cbmNsYXNzIEluZmluaXR5IHt9In0=)

```
/*eslint no-shadow-restricted-names: "error"*/

import NaN from "foo";

import { undefined } from "bar";

class Infinity {}
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFwiZXJyb3JcIiovXG5cbmxldCBPYmplY3Q7XG5cbmZ1bmN0aW9uIGYoYSwgYil7fVxuXG4vLyBFeGNlcHRpb246IGB1bmRlZmluZWRgIG1heSBiZSBzaGFkb3dlZCBpZiB0aGUgdmFyaWFibGUgaXMgbmV2ZXIgYXNzaWduZWQgYSB2YWx1ZS5cbmxldCB1bmRlZmluZWQ7In0=)

```
/*eslint no-shadow-restricted-names: "error"*/

let Object;

function f(a, b){}

// Exception: `undefined` may be shadowed if the variable is never assigned a value.
let undefined;
1
2
3
4
5
6
7
8
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFwiZXJyb3JcIiovXG5cbmltcG9ydCB7IHVuZGVmaW5lZCBhcyB1bmRlZiB9IGZyb20gXCJiYXJcIjsifQ==)

```
/*eslint no-shadow-restricted-names: "error"*/

import { undefined as undef } from "bar";
1
2
3
```

## Options

This rule has an object option:

- `"reportGlobalThis"`: `true` (default `false`) reports declarations of `globalThis`.

### reportGlobalThis

Examples of incorrect code for the `{ "reportGlobalThis": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRHbG9iYWxUaGlzXCI6IHRydWUgfV0qL1xuXG5jb25zdCBnbG9iYWxUaGlzID0gXCJmb29cIjsifQ==)

```
/*eslint no-shadow-restricted-names: ["error", { "reportGlobalThis": true }]*/

const globalThis = "foo";
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRHbG9iYWxUaGlzXCI6IHRydWUgfV0qL1xuXG5mdW5jdGlvbiBnbG9iYWxUaGlzKCkge30ifQ==)

```
/*eslint no-shadow-restricted-names: ["error", { "reportGlobalThis": true }]*/

function globalThis() {}
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRHbG9iYWxUaGlzXCI6IHRydWUgfV0qL1xuXG5pbXBvcnQgeyBnbG9iYWxUaGlzIH0gZnJvbSBcImJhclwiOyJ9)

```
/*eslint no-shadow-restricted-names: ["error", { "reportGlobalThis": true }]*/

import { globalThis } from "bar";
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRHbG9iYWxUaGlzXCI6IHRydWUgfV0qL1xuXG5jbGFzcyBnbG9iYWxUaGlzIHt9In0=)

```
/*eslint no-shadow-restricted-names: ["error", { "reportGlobalThis": true }]*/

class globalThis {}
1
2
3
```

Examples of correct code for the `{ "reportGlobalThis": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2hhZG93LXJlc3RyaWN0ZWQtbmFtZXM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRHbG9iYWxUaGlzXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmb28gPSBnbG9iYWxUaGlzO1xuXG5mdW5jdGlvbiBiYXIoKSB7XG4gICAgcmV0dXJuIGdsb2JhbFRoaXM7XG59XG5cbmltcG9ydCB7IGdsb2JhbFRoaXMgYXMgYmF6IH0gZnJvbSBcImZvb1wiOyJ9)

```
/*eslint no-shadow-restricted-names: ["error", { "reportGlobalThis": true }]*/

const foo = globalThis;

function bar() {
    return globalThis;
}

import { globalThis as baz } from "foo";
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

## Related Rules

- [no-shadow](/docs/latest/rules/no-shadow)

## Version

This rule was introduced in ESLint v0.1.4.

## Further Reading

[ECMAScript® 2020 Language Specification](https://262.ecma-international.org/11.0/#sec-value-properties-of-the-global-object)
 262.ecma-international.org[ECMAScript® 2020 Language Specification](https://262.ecma-international.org/11.0/#sec-strict-mode-of-ecmascript)
 262.ecma-international.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-shadow-restricted-names.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-shadow-restricted-names.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-shadow-restricted-names.md
                    
                
                )
