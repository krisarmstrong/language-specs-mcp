# no-useless-backreference

Disallow useless backreferences in regular expressions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

In JavaScript regular expressions, it’s syntactically valid to define a backreference to a group that belongs to another alternative part of the pattern, a backreference to a group that appears after the backreference, a backreference to a group that contains that backreference, or a backreference to a group that is inside a negative lookaround. However, by the specification, in any of these cases the backreference always ends up matching only zero-length (the empty string), regardless of the context in which the backreference and the group appear.

Backreferences that always successfully match zero-length and cannot match anything else are useless. They are basically ignored and can be removed without changing the behavior of the regular expression.

```
const regex = /^(?:(a)|\1b)$/;

regex.test("a"); // true
regex.test("b"); // true!
regex.test("ab"); // false

const equivalentRegex = /^(?:(a)|b)$/;

equivalentRegex.test("a"); // true
equivalentRegex.test("b"); // true
equivalentRegex.test("ab"); // false
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

Useless backreference is a possible error in the code. It usually indicates that the regular expression does not work as intended.

## Rule Details

This rule aims to detect and disallow the following backreferences in regular expression:

- Backreference to a group that is in another alternative, e.g., `/(a)|\1b/`. In such constructed regular expression, the backreference is expected to match what’s been captured in, at that point, a non-participating group.
- Backreference to a group that appears later in the pattern, e.g., `/\1(a)/`. The group hasn’t captured anything yet, and ECMAScript doesn’t support forward references. Inside lookbehinds, which match backward, the opposite applies and this rule disallows backreference to a group that appears before in the same lookbehind, e.g., `/(?<=(a)\1)b/`.
- Backreference to a group from within the same group, e.g., `/(\1)/`. Similar to the previous, the group hasn’t captured anything yet, and ECMAScript doesn’t support nested references.
- Backreference to a group that is in a negative lookaround, if the backreference isn’t in the same negative lookaround, e.g., `/a(?!(b)).\1/`. A negative lookaround (lookahead or lookbehind) succeeds only if its pattern cannot match, meaning that the group has failed.

By the ECMAScript specification, all backreferences listed above are valid, always succeed to match zero-length, and cannot match anything else. Consequently, they don’t produce parsing or runtime errors, but also don’t affect the behavior of their regular expressions. They are syntactically valid but useless.

This might be surprising to developers coming from other languages where some of these backreferences can be used in a meaningful way.

```
// in some other languages, this pattern would successfully match "aab"

/^(?:(a)(?=a)|\1b)+$/.test("aab"); // false
1
2
3
```

Copy code to clipboard

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1iYWNrcmVmZXJlbmNlOiBcImVycm9yXCIqL1xuXG4vXig/OihhKXxcXDFiKSQvOyAvLyByZWZlcmVuY2UgdG8gKGEpIGludG8gYW5vdGhlciBhbHRlcm5hdGl2ZVxuXG4vXig/OihhKXxiKD86Y3xcXDEpKSQvOyAvLyByZWZlcmVuY2UgdG8gKGEpIGludG8gYW5vdGhlciBhbHRlcm5hdGl2ZVxuXG4vXig/OmF8Yig/OihjKXxcXDEpKSQvOyAvLyByZWZlcmVuY2UgdG8gKGMpIGludG8gYW5vdGhlciBhbHRlcm5hdGl2ZVxuXG4vXFwxKGEpLzsgLy8gZm9yd2FyZCByZWZlcmVuY2UgdG8gKGEpXG5cblJlZ0V4cCgnKGEpXFxcXDIoYiknKTsgLy8gZm9yd2FyZCByZWZlcmVuY2UgdG8gKGIpXG5cbi8oPzphKShiKVxcMihjKS87IC8vIGZvcndhcmQgcmVmZXJlbmNlIHRvIChjKVxuXG4vXFxrPGZvbz4oPzxmb28+YSkvOyAvLyBmb3J3YXJkIHJlZmVyZW5jZSB0byAoPzxmb28+YSlcblxuLyg/PD0oYSlcXDEpYi87IC8vIGJhY2t3YXJkIHJlZmVyZW5jZSB0byAoYSkgZnJvbSB3aXRoaW4gdGhlIHNhbWUgbG9va2JlaGluZFxuXG4vKD88IShhKVxcMSliLzsgLy8gYmFja3dhcmQgcmVmZXJlbmNlIHRvIChhKSBmcm9tIHdpdGhpbiB0aGUgc2FtZSBsb29rYmVoaW5kXG5cbm5ldyBSZWdFeHAoJyhcXFxcMSknKTsgLy8gbmVzdGVkIHJlZmVyZW5jZSB0byAoXFwxKVxuXG4vXigoYSlcXDEpJC87IC8vIG5lc3RlZCByZWZlcmVuY2UgdG8gKChhKVxcMSlcblxuL2EoPzxmb28+KC4pYlxcMSkvOyAvLyBuZXN0ZWQgcmVmZXJlbmNlIHRvICg/PGZvbz4oLiliXFwxKVxuXG4vYSg/IShiKSkuXFwxLzsgLy8gcmVmZXJlbmNlIHRvIChiKSBpbnRvIGEgbmVnYXRpdmUgbG9va2FoZWFkXG5cbi8oPzwhKGEpKWJcXDEvOyAvLyByZWZlcmVuY2UgdG8gKGEpIGludG8gYSBuZWdhdGl2ZSBsb29rYmVoaW5kIn0=)

```
/*eslint no-useless-backreference: "error"*/

/^(?:(a)|\1b)$/; // reference to (a) into another alternative

/^(?:(a)|b(?:c|\1))$/; // reference to (a) into another alternative

/^(?:a|b(?:(c)|\1))$/; // reference to (c) into another alternative

/\1(a)/; // forward reference to (a)

RegExp('(a)\\2(b)'); // forward reference to (b)

/(?:a)(b)\2(c)/; // forward reference to (c)

/\k<foo>(?<foo>a)/; // forward reference to (?<foo>a)

/(?<=(a)\1)b/; // backward reference to (a) from within the same lookbehind

/(?<!(a)\1)b/; // backward reference to (a) from within the same lookbehind

new RegExp('(\\1)'); // nested reference to (\1)

/^((a)\1)$/; // nested reference to ((a)\1)

/a(?<foo>(.)b\1)/; // nested reference to (?<foo>(.)b\1)

/a(?!(b)).\1/; // reference to (b) into a negative lookahead

/(?<!(a))b\1/; // reference to (a) into a negative lookbehind
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
22
23
24
25
26
27
28
29
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1iYWNrcmVmZXJlbmNlOiBcImVycm9yXCIqL1xuXG4vXig/OihhKXwoYilcXDIpJC87IC8vIHJlZmVyZW5jZSB0byAoYilcblxuLyhhKVxcMS87IC8vIHJlZmVyZW5jZSB0byAoYSlcblxuUmVnRXhwKCcoYSlcXFxcMShiKScpOyAvLyByZWZlcmVuY2UgdG8gKGEpXG5cbi8oYSkoYilcXDIoYykvOyAvLyByZWZlcmVuY2UgdG8gKGIpXG5cbi8oPzxmb28+YSlcXGs8Zm9vPi87IC8vIHJlZmVyZW5jZSB0byAoPzxmb28+YSlcblxuLyg/PD1cXDEoYSkpYi87IC8vIHJlZmVyZW5jZSB0byAoYSksIGNvcnJlY3RseSBiZWZvcmUgdGhlIGdyb3VwIGFzIHRoZXkncmUgaW4gdGhlIHNhbWUgbG9va2JlaGluZFxuXG4vKD88PShhKSliXFwxLzsgLy8gcmVmZXJlbmNlIHRvIChhKSwgY29ycmVjdGx5IGFmdGVyIHRoZSBncm91cCBhcyB0aGUgYmFja3JlZmVyZW5jZSBpc24ndCBpbiB0aGUgbG9va2JlaGluZFxuXG5uZXcgUmVnRXhwKCcoLilcXFxcMScpOyAvLyByZWZlcmVuY2UgdG8gKC4pXG5cbi9eKD86KGEpXFwxKSQvOyAvLyByZWZlcmVuY2UgdG8gKGEpXG5cbi9eKChhKVxcMikkLzsgLy8gcmVmZXJlbmNlIHRvIChhKVxuXG4vYSg/PGZvbz4oLiliXFwyKS87IC8vIHJlZmVyZW5jZSB0byAoLilcblxuL2EoPyEoYnxjKVxcMSkuLzsgLy8gcmVmZXJlbmNlIHRvIChifGMpLCBjb3JyZWN0IGFzIGl0J3MgZnJvbSB3aXRoaW4gdGhlIHNhbWUgbmVnYXRpdmUgbG9va2FoZWFkXG5cbi8oPzwhXFwxKGEpKWIvOyAvLyByZWZlcmVuY2UgdG8gKGEpLCBjb3JyZWN0IGFzIGl0J3MgZnJvbSB3aXRoaW4gdGhlIHNhbWUgbmVnYXRpdmUgbG9va2JlaGluZCJ9)

```
/*eslint no-useless-backreference: "error"*/

/^(?:(a)|(b)\2)$/; // reference to (b)

/(a)\1/; // reference to (a)

RegExp('(a)\\1(b)'); // reference to (a)

/(a)(b)\2(c)/; // reference to (b)

/(?<foo>a)\k<foo>/; // reference to (?<foo>a)

/(?<=\1(a))b/; // reference to (a), correctly before the group as they're in the same lookbehind

/(?<=(a))b\1/; // reference to (a), correctly after the group as the backreference isn't in the lookbehind

new RegExp('(.)\\1'); // reference to (.)

/^(?:(a)\1)$/; // reference to (a)

/^((a)\2)$/; // reference to (a)

/a(?<foo>(.)b\2)/; // reference to (.)

/a(?!(b|c)\1)./; // reference to (b|c), correct as it's from within the same negative lookahead

/(?<!\1(a))b/; // reference to (a), correct as it's from within the same negative lookbehind
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
22
23
24
25
26
27
```

Please note that this rule does not aim to detect and disallow a potentially erroneous use of backreference syntax in regular expressions, like the use in character classes or an attempt to reference a group that doesn’t exist. Depending on the context, a `\1`…`\9` sequence that is not a syntactically valid backreference may produce syntax error, or be parsed as something else (e.g., as a legacy octal escape sequence).

Examples of additional correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1iYWNrcmVmZXJlbmNlOiBcImVycm9yXCIqL1xuXG4vLyBjb21tZW50cyBkZXNjcmliZSBiZWhhdmlvciBpbiBhIGJyb3dzZXJcblxuL15bXFwxXShhKSQvLnRlc3QoXCJcXHgwMWFcIik7IC8vIHRydWUuIEluIGEgY2hhcmFjdGVyIGNsYXNzLCBcXDEgaXMgdHJlYXRlZCBhcyBhbiBvY3RhbCBlc2NhcGUgc2VxdWVuY2UuXG4vXlxcMSQvLnRlc3QoXCJcXHgwMVwiKTsgLy8gdHJ1ZS4gU2luY2UgdGhlIGdyb3VwIDEgZG9lc24ndCBleGlzdCwgXFwxIGlzIHRyZWF0ZWQgYXMgYW4gb2N0YWwgZXNjYXBlIHNlcXVlbmNlLlxuL14oYSlcXDFcXDIkLy50ZXN0KFwiYWFcXHgwMlwiKTsgLy8gdHJ1ZS4gSW4gdGhpcyBjYXNlLCBcXDEgaXMgYSBiYWNrcmVmZXJlbmNlLCBcXDIgaXMgYW4gb2N0YWwgZXNjYXBlIHNlcXVlbmNlLiJ9)

```
/*eslint no-useless-backreference: "error"*/

// comments describe behavior in a browser

/^[\1](a)$/.test("\x01a"); // true. In a character class, \1 is treated as an octal escape sequence.
/^\1$/.test("\x01"); // true. Since the group 1 doesn't exist, \1 is treated as an octal escape sequence.
/^(a)\1\2$/.test("aa\x02"); // true. In this case, \1 is a backreference, \2 is an octal escape sequence.
1
2
3
4
5
6
7
```

## Related Rules

- [no-control-regex](/docs/latest/rules/no-control-regex)
- [no-empty-character-class](/docs/latest/rules/no-empty-character-class)
- [no-invalid-regexp](/docs/latest/rules/no-invalid-regexp)

## Version

This rule was introduced in ESLint v7.0.0-alpha.0.

## Further Reading

[Regular expressions - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-backreference.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-backreference.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-backreference.md
                    
                
                )
