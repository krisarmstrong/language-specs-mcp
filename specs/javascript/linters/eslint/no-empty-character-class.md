# no-empty-character-class

Disallow empty character classes in regular expressions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [Version](#version)
4. [Resources](#resources)

Because empty character classes in regular expressions do not match anything, they might be typing mistakes.

```
const foo = /^abc[]/;
1
```

Copy code to clipboard

## Rule Details

This rule disallows empty character classes in regular expressions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktY2hhcmFjdGVyLWNsYXNzOiBcImVycm9yXCIqL1xuXG4vXmFiY1tdLy50ZXN0KFwiYWJjZGVmZ1wiKTsgLy8gZmFsc2VcblwiYWJjZGVmZ1wiLm1hdGNoKC9eYWJjW10vKTsgLy8gbnVsbFxuXG4vXmFiY1tbXV0vdi50ZXN0KFwiYWJjZGVmZ1wiKTsgLy8gZmFsc2VcblwiYWJjZGVmZ1wiLm1hdGNoKC9eYWJjW1tdXS92KTsgLy8gbnVsbFxuXG4vXmFiY1tbXS0tW3hdXS92LnRlc3QoXCJhYmNkZWZnXCIpOyAvLyBmYWxzZVxuXCJhYmNkZWZnXCIubWF0Y2goL15hYmNbW10tLVt4XV0vdik7IC8vIG51bGxcblxuL15hYmNbW2RdJiZbXV0vdi50ZXN0KFwiYWJjZGVmZ1wiKTsgLy8gZmFsc2VcblwiYWJjZGVmZ1wiLm1hdGNoKC9eYWJjW1tkXSYmW11dL3YpOyAvLyBudWxsXG5cbmNvbnN0IHJlZ2V4ID0gL15hYmNbZFtdXS92O1xucmVnZXgudGVzdChcImFiY2RlZmdcIik7IC8vIHRydWUsIHRoZSBuZXN0ZWQgYFtdYCBoYXMgbm8gZWZmZWN0XG5cImFiY2RlZmdcIi5tYXRjaChyZWdleCk7IC8vIFtcImFiY2RcIl1cbnJlZ2V4LnRlc3QoXCJhYmNlZmdcIik7IC8vIGZhbHNlLCB0aGUgbmVzdGVkIGBbXWAgaGFzIG5vIGVmZmVjdFxuXCJhYmNlZmdcIi5tYXRjaChyZWdleCk7IC8vIG51bGxcbnJlZ2V4LnRlc3QoXCJhYmNcIik7IC8vIGZhbHNlLCB0aGUgbmVzdGVkIGBbXWAgaGFzIG5vIGVmZmVjdFxuXCJhYmNcIi5tYXRjaChyZWdleCk7IC8vIG51bGwifQ==)

```
/*eslint no-empty-character-class: "error"*/

/^abc[]/.test("abcdefg"); // false
"abcdefg".match(/^abc[]/); // null

/^abc[[]]/v.test("abcdefg"); // false
"abcdefg".match(/^abc[[]]/v); // null

/^abc[[]--[x]]/v.test("abcdefg"); // false
"abcdefg".match(/^abc[[]--[x]]/v); // null

/^abc[[d]&&[]]/v.test("abcdefg"); // false
"abcdefg".match(/^abc[[d]&&[]]/v); // null

const regex = /^abc[d[]]/v;
regex.test("abcdefg"); // true, the nested `[]` has no effect
"abcdefg".match(regex); // ["abcd"]
regex.test("abcefg"); // false, the nested `[]` has no effect
"abcefg".match(regex); // null
regex.test("abc"); // false, the nested `[]` has no effect
"abc".match(regex); // null
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
21
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktY2hhcmFjdGVyLWNsYXNzOiBcImVycm9yXCIqL1xuXG4vXmFiYy8udGVzdChcImFiY2RlZmdcIik7IC8vIHRydWVcblwiYWJjZGVmZ1wiLm1hdGNoKC9eYWJjLyk7IC8vIFtcImFiY1wiXVxuXG4vXmFiY1thLXpdLy50ZXN0KFwiYWJjZGVmZ1wiKTsgLy8gdHJ1ZVxuXCJhYmNkZWZnXCIubWF0Y2goL15hYmNbYS16XS8pOyAvLyBbXCJhYmNkXCJdXG5cbi9eYWJjW15dLy50ZXN0KFwiYWJjZGVmZ1wiKTsgLy8gdHJ1ZVxuXCJhYmNkZWZnXCIubWF0Y2goL15hYmNbXl0vKTsgLy8gW1wiYWJjZFwiXSJ9)

```
/*eslint no-empty-character-class: "error"*/

/^abc/.test("abcdefg"); // true
"abcdefg".match(/^abc/); // ["abc"]

/^abc[a-z]/.test("abcdefg"); // true
"abcdefg".match(/^abc[a-z]/); // ["abcd"]

/^abc[^]/.test("abcdefg"); // true
"abcdefg".match(/^abc[^]/); // ["abcd"]
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

This rule does not report empty character classes in the string argument of calls to the `RegExp` constructor.

Example of a false negative when this rule reports correct code:

```
/*eslint no-empty-character-class: "error"*/

const abcNeverMatches = new RegExp("^abc[]");
1
2
3
```

Copy code to clipboard

## Version

This rule was introduced in ESLint v0.22.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-empty-character-class.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-empty-character-class.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-empty-character-class.md
                    
                
                )
