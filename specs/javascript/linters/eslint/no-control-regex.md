# no-control-regex

Disallow control characters in regular expressions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Control characters are special, invisible characters in the ASCII range 0-31. These characters are rarely used in JavaScript strings so a regular expression containing elements that explicitly match these characters is most likely a mistake.

## Rule Details

This rule disallows control characters and some escape sequences that match control characters in regular expressions.

The following elements of regular expression patterns are considered possible errors in typing and are therefore disallowed by this rule:

- Hexadecimal character escapes from `\x00` to `\x1F`.
- Unicode character escapes from `\u0000` to `\u001F`.
- Unicode code point escapes from `\u{0}` to `\u{1F}`.
- Unescaped raw characters from U+0000 to U+001F.

Control escapes such as `\t` and `\n` are allowed by this rule.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29udHJvbC1yZWdleDogXCJlcnJvclwiKi9cblxuY29uc3QgcGF0dGVybjEgPSAvXFx4MDAvO1xuY29uc3QgcGF0dGVybjIgPSAvXFx4MEMvO1xuY29uc3QgcGF0dGVybjMgPSAvXFx4MUYvO1xuY29uc3QgcGF0dGVybjQgPSAvXFx1MDAwQy87XG5jb25zdCBwYXR0ZXJuNSA9IC9cXHV7Q30vdTtcbmNvbnN0IHBhdHRlcm42ID0gbmV3IFJlZ0V4cChcIlxceDBDXCIpOyAvLyByYXcgVSswMDBDIGNoYXJhY3RlciBpbiB0aGUgcGF0dGVyblxuY29uc3QgcGF0dGVybjcgPSBuZXcgUmVnRXhwKFwiXFxcXHgwQ1wiKTsgLy8gXFx4MEMgcGF0dGVybiJ9)

```
/*eslint no-control-regex: "error"*/

const pattern1 = /\x00/;
const pattern2 = /\x0C/;
const pattern3 = /\x1F/;
const pattern4 = /\u000C/;
const pattern5 = /\u{C}/u;
const pattern6 = new RegExp("\x0C"); // raw U+000C character in the pattern
const pattern7 = new RegExp("\\x0C"); // \x0C pattern
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29udHJvbC1yZWdleDogXCJlcnJvclwiKi9cblxuY29uc3QgcGF0dGVybjEgPSAvXFx4MjAvO1xuY29uc3QgcGF0dGVybjIgPSAvXFx1MDAyMC87XG5jb25zdCBwYXR0ZXJuMyA9IC9cXHV7MjB9L3U7XG5jb25zdCBwYXR0ZXJuNCA9IC9cXHQvO1xuY29uc3QgcGF0dGVybjUgPSAvXFxuLztcbmNvbnN0IHBhdHRlcm42ID0gbmV3IFJlZ0V4cChcIlxceDIwXCIpO1xuY29uc3QgcGF0dGVybjcgPSBuZXcgUmVnRXhwKFwiXFxcXHRcIik7XG5jb25zdCBwYXR0ZXJuOCA9IG5ldyBSZWdFeHAoXCJcXFxcblwiKTsifQ==)

```
/*eslint no-control-regex: "error"*/

const pattern1 = /\x20/;
const pattern2 = /\u0020/;
const pattern3 = /\u{20}/u;
const pattern4 = /\t/;
const pattern5 = /\n/;
const pattern6 = new RegExp("\x20");
const pattern7 = new RegExp("\\t");
const pattern8 = new RegExp("\\n");
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
```

## Known Limitations

When checking `RegExp` constructor calls, this rule examines evaluated regular expression patterns. Therefore, although this rule intends to allow syntax such as `\t`, it doesn’t allow `new RegExp("\t")` since the evaluated pattern (string value of `"\t"`) contains a raw control character (the TAB character).

```
/*eslint no-control-regex: "error"*/

new RegExp("\t"); // disallowed since the pattern is: <TAB>

new RegExp("\\t"); // allowed since the pattern is: \t
1
2
3
4
5
```

Copy code to clipboard

There is no difference in behavior between `new RegExp("\t")` and `new RegExp("\\t")`, and the intention to match the TAB character is clear in both cases. They are equally valid for the purpose of this rule, but it only allows `new RegExp("\\t")`.

## When Not To Use It

If you need to use control character pattern matching, then you should turn this rule off.

## Related Rules

- [no-div-regex](/docs/latest/rules/no-div-regex)
- [no-regex-spaces](/docs/latest/rules/no-regex-spaces)

## Version

This rule was introduced in ESLint v0.1.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-control-regex.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-control-regex.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-control-regex.md
                    
                
                )
