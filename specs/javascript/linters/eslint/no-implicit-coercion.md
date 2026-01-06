# no-implicit-coercion

Disallow shorthand type conversions

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [boolean](#boolean)
  2. [number](#number)
  3. [string](#string)
  4. [disallowTemplateShorthand](#disallowtemplateshorthand)
  5. [allow](#allow)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

In JavaScript, there are a lot of different ways to convert value types. Some of them might be hard to read and understand.

Such as:

```
const b = !!foo;
const b1 = ~foo.indexOf(".");
const n = +foo;
const n1 = -(-foo);
const n2 = foo - 0;
const n3 = 1 * foo;
const s = "" + foo;
foo += ``;
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

Those can be replaced with the following code:

```
const b = Boolean(foo);
const b1 = foo.indexOf(".") !== -1;
const n = Number(foo);
const n1 = Number(foo);
const n2 = Number(foo);
const n3 = Number(foo);
const s = String(foo);
foo = String(foo);
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

This rule is aimed to flag shorter notations for the type conversion, then suggest a more self-explanatory notation.

## Options

This rule has three main options and one override option to allow some coercions as required.

- `"boolean"` (`true` by default) - When this is `true`, this rule warns shorter type conversions for `boolean` type.
- `"number"` (`true` by default) - When this is `true`, this rule warns shorter type conversions for `number` type.
- `"string"` (`true` by default) - When this is `true`, this rule warns shorter type conversions for `string` type.
- `"disallowTemplateShorthand"` (`false` by default) - When this is `true`, this rule warns `string` type conversions using `${expression}` form.
- `"allow"` (`empty` by default) - Each entry in this array can be one of `~`, `!!`, `+`, `- -`, `-`, or `*` that are to be allowed.

Note that operator `+` in `allow` list would allow `+foo` (number coercion) as well as `"" + foo` (string coercion).

### boolean

Examples of incorrect code for the default `{ "boolean": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IGIgPSAhIWZvbztcbmNvbnN0IGIxID0gfmZvby5pbmRleE9mKFwiLlwiKTtcbi8vIGJpdHdpc2Ugbm90IGlzIGluY29ycmVjdCBvbmx5IHdpdGggYGluZGV4T2ZgL2BsYXN0SW5kZXhPZmAgbWV0aG9kIGNhbGxpbmcuIn0=)

```
/*eslint no-implicit-coercion: "error"*/

const b = !!foo;
const b1 = ~foo.indexOf(".");
// bitwise not is incorrect only with `indexOf`/`lastIndexOf` method calling.
1
2
3
4
5
```

Examples of correct code for the default `{ "boolean": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IGIgPSBCb29sZWFuKGZvbyk7XG5jb25zdCBiMSA9IGZvby5pbmRleE9mKFwiLlwiKSAhPT0gLTE7XG5cbmNvbnN0IG4gPSB+Zm9vOyAvLyBUaGlzIGlzIGEganVzdCBiaXR3aXNlIG5vdC4ifQ==)

```
/*eslint no-implicit-coercion: "error"*/

const b = Boolean(foo);
const b1 = foo.indexOf(".") !== -1;

const n = ~foo; // This is a just bitwise not.
1
2
3
4
5
6
```

### number

Examples of incorrect code for the default `{ "number": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IG4gPSArZm9vO1xuY29uc3QgbjEgPSAtKC1mb28pO1xuY29uc3QgbjIgPSBmb28gLSAwO1xuY29uc3QgbjMgPSAxICogZm9vOyJ9)

```
/*eslint no-implicit-coercion: "error"*/

const n = +foo;
const n1 = -(-foo);
const n2 = foo - 0;
const n3 = 1 * foo;
1
2
3
4
5
6
```

Examples of correct code for the default `{ "number": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IG4gPSBOdW1iZXIoZm9vKTtcbmNvbnN0IG4xID0gcGFyc2VGbG9hdChmb28pO1xuY29uc3QgbjIgPSBwYXJzZUludChmb28sIDEwKTtcblxuY29uc3QgbjMgPSBmb28gKiAxLzQ7IC8vIGAqIDFgIGlzIGFsbG93ZWQgd2hlbiBmb2xsb3dlZCBieSB0aGUgYC9gIG9wZXJhdG9yIn0=)

```
/*eslint no-implicit-coercion: "error"*/

const n = Number(foo);
const n1 = parseFloat(foo);
const n2 = parseInt(foo, 10);

const n3 = foo * 1/4; // `* 1` is allowed when followed by the `/` operator
1
2
3
4
5
6
7
```

### string

Examples of incorrect code for the default `{ "string": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IHMgPSBcIlwiICsgZm9vO1xuY29uc3QgczEgPSBgYCArIGZvbztcbmZvbyArPSBcIlwiO1xuZm9vICs9IGBgOyJ9)

```
/*eslint no-implicit-coercion: "error"*/

const s = "" + foo;
const s1 = `` + foo;
foo += "";
foo += ``;
1
2
3
4
5
6
```

Examples of correct code for the default `{ "string": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IHMgPSBTdHJpbmcoZm9vKTtcbmZvbyA9IFN0cmluZyhmb28pOyJ9)

```
/*eslint no-implicit-coercion: "error"*/

const s = String(foo);
foo = String(foo);
1
2
3
4
```

### disallowTemplateShorthand

This option is not affected by the `string` option.

Examples of incorrect code for the `{ "disallowTemplateShorthand": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFtcImVycm9yXCIsIHsgXCJkaXNhbGxvd1RlbXBsYXRlU2hvcnRoYW5kXCI6IHRydWUgfV0qL1xuXG5jb25zdCBzID0gYCR7Zm9vfWA7In0=)

```
/*eslint no-implicit-coercion: ["error", { "disallowTemplateShorthand": true }]*/

const s = `${foo}`;
1
2
3
```

Examples of correct code for the `{ "disallowTemplateShorthand": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFtcImVycm9yXCIsIHsgXCJkaXNhbGxvd1RlbXBsYXRlU2hvcnRoYW5kXCI6IHRydWUgfV0qL1xuXG5jb25zdCBzID0gU3RyaW5nKGZvbyk7XG5cbmNvbnN0IHMxID0gYGEke2Zvb31gO1xuXG5jb25zdCBzMiA9IGAke2Zvb31iYDtcblxuY29uc3QgczMgPSBgJHtmb299JHtiYXJ9YDtcblxuY29uc3QgczQgPSB0YWdgJHtmb299YDsifQ==)

```
/*eslint no-implicit-coercion: ["error", { "disallowTemplateShorthand": true }]*/

const s = String(foo);

const s1 = `a${foo}`;

const s2 = `${foo}b`;

const s3 = `${foo}${bar}`;

const s4 = tag`${foo}`;
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

Examples of correct code for the default `{ "disallowTemplateShorthand": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFtcImVycm9yXCIsIHsgXCJkaXNhbGxvd1RlbXBsYXRlU2hvcnRoYW5kXCI6IGZhbHNlIH1dKi9cblxuY29uc3QgcyA9IGAke2Zvb31gOyJ9)

```
/*eslint no-implicit-coercion: ["error", { "disallowTemplateShorthand": false }]*/

const s = `${foo}`;
1
2
3
```

### allow

Using `allow` list, we can override and allow specific operators.

Examples of correct code for the sample `{ "allow": ["!!", "~"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtY29lcmNpb246IFsyLCB7IFwiYWxsb3dcIjogW1wiISFcIiwgXCJ+XCJdIH0gXSovXG5cbmNvbnN0IGIgPSAhIWZvbztcbmNvbnN0IGIxID0gfmZvby5pbmRleE9mKFwiLlwiKTsifQ==)

```
/*eslint no-implicit-coercion: [2, { "allow": ["!!", "~"] } ]*/

const b = !!foo;
const b1 = ~foo.indexOf(".");
1
2
3
4
```

## When Not To Use It

If you don’t want to be notified about shorter notations for the type conversion, you can safely disable this rule.

## Version

This rule was introduced in ESLint v1.0.0-rc-2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-implicit-coercion.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-implicit-coercion.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-implicit-coercion.md
                    
                
                )
