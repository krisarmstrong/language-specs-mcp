# require-unicode-regexp

Enforce the use of `u` or `v` flag on regular expressions

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [requireFlag: “u”](#requireflag-u)
  2. [requireFlag: “v”](#requireflag-v)

3. [When Not To Use It](#when-not-to-use-it)

  1. [Note on i flag and \w](#note-on-i-flag-and-w)

4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

RegExp `u` flag has two effects:

1. 

Make the regular expression handling UTF-16 surrogate pairs correctly.

Especially, character range syntax gets the correct behavior.

```
/^[👍]$/.test("👍") //→ false
/^[👍]$/u.test("👍") //→ true
1
2
```

Copy code to clipboard
2. 

Make the regular expression throwing syntax errors early as disabling [Annex B extensions](https://www.ecma-international.org/ecma-262/6.0/#sec-regular-expressions-patterns).

Because of historical reason, JavaScript regular expressions are tolerant of syntax errors. For example, `/\w{1, 2/` is a syntax error, but JavaScript doesn’t throw the error. It matches strings such as `"a{1, 2"` instead. Such a recovering logic is defined in Annex B.

The `u` flag disables the recovering logic Annex B defined. As a result, you can find errors early. This is similar to [the strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode).

The RegExp `v` flag, introduced in ECMAScript 2024, is a superset of the `u` flag, and offers two more features:

1. 

Unicode properties of strings

With the Unicode property escape, you can use properties of strings.

```
const re = /^\p{RGI_Emoji}$/v;

// Match an emoji that consists of just 1 code point:
re.test('⚽'); // '\u26BD'
// → true ✅

// Match an emoji that consists of multiple code points:
re.test('👨🏾‍⚕️'); // '\u{1F468}\u{1F3FE}\u200D\u2695\uFE0F'
// → true ✅
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
2. 

Set notation

It allows for set operations between character classes.

```
const re = /[\p{White_Space}&&\p{ASCII}]/v;
re.test('\n'); // → true
re.test('\u2028'); // → false
1
2
3
```

Copy code to clipboard

Therefore, the `u` and `v` flags let us work better with regular expressions.

## Rule Details

This rule aims to enforce the use of `u` or `v` flag on regular expressions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS11bmljb2RlLXJlZ2V4cDogZXJyb3IgKi9cblxuY29uc3QgYSA9IC9hYWEvXG5jb25zdCBiID0gL2JiYi9naVxuY29uc3QgYyA9IG5ldyBSZWdFeHAoXCJjY2NcIilcbmNvbnN0IGQgPSBuZXcgUmVnRXhwKFwiZGRkXCIsIFwiZ2lcIikifQ==)

```
/*eslint require-unicode-regexp: error */

const a = /aaa/
const b = /bbb/gi
const c = new RegExp("ccc")
const d = new RegExp("ddd", "gi")
1
2
3
4
5
6
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS11bmljb2RlLXJlZ2V4cDogZXJyb3IgKi9cblxuY29uc3QgYSA9IC9hYWEvdVxuY29uc3QgYiA9IC9iYmIvZ2l1XG5jb25zdCBjID0gbmV3IFJlZ0V4cChcImNjY1wiLCBcInVcIilcbmNvbnN0IGQgPSBuZXcgUmVnRXhwKFwiZGRkXCIsIFwiZ2l1XCIpXG5cbmNvbnN0IGUgPSAvYWFhL3ZcbmNvbnN0IGYgPSAvYmJiL2dpdlxuY29uc3QgZyA9IG5ldyBSZWdFeHAoXCJjY2NcIiwgXCJ2XCIpXG5jb25zdCBoID0gbmV3IFJlZ0V4cChcImRkZFwiLCBcImdpdlwiKVxuXG4vLyBUaGlzIHJ1bGUgaWdub3JlcyBSZWdFeHAgY2FsbHMgaWYgdGhlIGZsYWdzIGNvdWxkIG5vdCBiZSBldmFsdWF0ZWQgdG8gYSBzdGF0aWMgdmFsdWUuXG5mdW5jdGlvbiBpKGZsYWdzKSB7XG4gICAgcmV0dXJuIG5ldyBSZWdFeHAoXCJlZWVcIiwgZmxhZ3MpXG59In0=)

```
/*eslint require-unicode-regexp: error */

const a = /aaa/u
const b = /bbb/giu
const c = new RegExp("ccc", "u")
const d = new RegExp("ddd", "giu")

const e = /aaa/v
const f = /bbb/giv
const g = new RegExp("ccc", "v")
const h = new RegExp("ddd", "giv")

// This rule ignores RegExp calls if the flags could not be evaluated to a static value.
function i(flags) {
    return new RegExp("eee", flags)
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
15
16
```

## Options

This rule has one object option:

- `"requireFlag": "u"|"v"` requires a particular Unicode regex flag

### requireFlag: “u”

The `u` flag may be preferred in environments that do not support the `v` flag.

Examples of incorrect code for this rule with the `{ "requireFlag": "u" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS11bmljb2RlLXJlZ2V4cDogW1wiZXJyb3JcIiwgeyBcInJlcXVpcmVGbGFnXCI6IFwidVwiIH1dICovXG5cbmNvbnN0IGZvb0VtcHR5ID0gL2Zvby87XG5cbmNvbnN0IGZvb0VtcHR5UmVnZXhwID0gbmV3IFJlZ0V4cCgnZm9vJyk7XG5cbmNvbnN0IGZvbyA9IC9mb28vdjtcblxuY29uc3QgZm9vUmVnZXhwID0gbmV3IFJlZ0V4cCgnZm9vJywgJ3YnKTsifQ==)

```
/*eslint require-unicode-regexp: ["error", { "requireFlag": "u" }] */

const fooEmpty = /foo/;

const fooEmptyRegexp = new RegExp('foo');

const foo = /foo/v;

const fooRegexp = new RegExp('foo', 'v');
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

Examples of correct code for this rule with the `{ "requireFlag": "u" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS11bmljb2RlLXJlZ2V4cDogW1wiZXJyb3JcIiwgeyBcInJlcXVpcmVGbGFnXCI6IFwidVwiIH1dICovXG5cbmNvbnN0IGZvbyA9IC9mb28vdTtcblxuY29uc3QgZm9vUmVnZXhwID0gbmV3IFJlZ0V4cCgnZm9vJywgJ3UnKTsifQ==)

```
/*eslint require-unicode-regexp: ["error", { "requireFlag": "u" }] */

const foo = /foo/u;

const fooRegexp = new RegExp('foo', 'u');
1
2
3
4
5
```

### requireFlag: “v”

The `v` flag may be a better choice when it is supported because it has more features than the `u` flag (e.g., the ability to test Unicode properties of strings). It does have a stricter syntax, however (e.g., the need to escape certain characters within character classes).

Examples of incorrect code for this rule with the `{ "requireFlag": "v" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS11bmljb2RlLXJlZ2V4cDogW1wiZXJyb3JcIiwgeyBcInJlcXVpcmVGbGFnXCI6IFwidlwiIH1dICovXG5cbmNvbnN0IGZvb0VtcHR5ID0gL2Zvby87XG5cbmNvbnN0IGZvb0VtcHR5UmVnZXhwID0gbmV3IFJlZ0V4cCgnZm9vJyk7XG5cbmNvbnN0IGZvbyA9IC9mb28vdTtcblxuY29uc3QgZm9vUmVnZXhwID0gbmV3IFJlZ0V4cCgnZm9vJywgJ3UnKTsifQ==)

```
/*eslint require-unicode-regexp: ["error", { "requireFlag": "v" }] */

const fooEmpty = /foo/;

const fooEmptyRegexp = new RegExp('foo');

const foo = /foo/u;

const fooRegexp = new RegExp('foo', 'u');
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

Examples of correct code for this rule with the `{ "requireFlag": "v" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcmVxdWlyZS11bmljb2RlLXJlZ2V4cDogW1wiZXJyb3JcIiwgeyBcInJlcXVpcmVGbGFnXCI6IFwidlwiIH1dICovXG5cbmNvbnN0IGZvbyA9IC9mb28vdjtcblxuY29uc3QgZm9vUmVnZXhwID0gbmV3IFJlZ0V4cCgnZm9vJywgJ3YnKTsifQ==)

```
/*eslint require-unicode-regexp: ["error", { "requireFlag": "v" }] */

const foo = /foo/v;

const fooRegexp = new RegExp('foo', 'v');
1
2
3
4
5
```

## When Not To Use It

If you don’t want to warn on regular expressions without either a `u` or a `v` flag, then it’s safe to disable this rule.

### Note on `i` flag and `\w`

In some cases, adding the `u` flag to a regular expression using both the `i` flag and the `\w` character class can change its behavior due to Unicode case folding.

For example:

```
const regexWithoutU = /^\w+$/i;
const regexWithU = /^\w+$/iu;

const str = "\u017f\u212a"; // Example Unicode characters

console.log(regexWithoutU.test(str)); // false
console.log(regexWithU.test(str)); // true
1
2
3
4
5
6
7
```

Copy code to clipboard

If you prefer to use a non-Unicode-aware regex in this specific case, you can disable this rule using an `eslint-disable` comment:

```
/* eslint-disable require-unicode-regexp */
const regex = /^\w+$/i;
/* eslint-enable require-unicode-regexp */
1
2
3
```

Copy code to clipboard

## Version

This rule was introduced in ESLint v5.3.0.

## Further Reading

[GitHub - tc39/proposal-regexp-v-flag: UTS18 set notation in regular expressions](https://github.com/tc39/proposal-regexp-v-flag)
 github.com[RegExp v flag with set notation and properties of strings · V8](https://v8.dev/features/regexp-v-flag)
 v8.dev

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/require-unicode-regexp.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/require-unicode-regexp.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/require-unicode-regexp.md
                    
                
                )
