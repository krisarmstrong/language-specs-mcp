# no-misleading-character-class

Disallow characters which are made with multiple code points in character class syntax

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowEscape](#allowescape)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

Unicode includes characters which are made by multiple code points. RegExp character class syntax (`/[abc]/`) cannot handle characters which are made by multiple code points as a character; those characters will be dissolved to each code point. For example, `❇️` is made by `❇` (`U+2747`) and VARIATION SELECTOR-16 (`U+FE0F`). If this character is in a RegExp character class, it will match either `❇` (`U+2747`) or VARIATION SELECTOR-16 (`U+FE0F`) rather than `❇️`.

This rule reports regular expressions which include multiple code point characters in character class syntax. This rule considers the following characters as multiple code point characters.

A character with combining characters:

The combining characters are characters which belong to one of `Mc`, `Me`, and `Mn`[Unicode general categories](http://www.unicode.org/L2/L1999/UnicodeData.html#General%20Category).

```
/^[Á]$/u.test("Á"); //→ false
/^[❇️]$/u.test("❇️"); //→ false
1
2
```

Copy code to clipboard

A character with Emoji modifiers:

```
/^[👶🏻]$/u.test("👶🏻"); //→ false
/^[👶🏽]$/u.test("👶🏽"); //→ false
1
2
```

Copy code to clipboard

A pair of regional indicator symbols:

```
/^[🇯🇵]$/u.test("🇯🇵"); //→ false
1
```

Copy code to clipboard

Characters that ZWJ joins:

```
/^[👨‍👩‍👦]$/u.test("👨‍👩‍👦"); //→ false
1
```

Copy code to clipboard

A surrogate pair without Unicode flag:

```
/^[👍]$/.test("👍"); //→ false

// Surrogate pair is OK if with u flag.
/^[👍]$/u.test("👍"); //→ true
1
2
3
4
```

Copy code to clipboard

## Rule Details

This rule reports regular expressions which include multiple code point characters in character class syntax.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWlzbGVhZGluZy1jaGFyYWN0ZXItY2xhc3M6IGVycm9yICovXG5cbi9eW0HMgV0kL3U7XG4vXlvinYfvuI9dJC91O1xuL15b8J+RtvCfj7tdJC91O1xuL15b8J+Hr/Cfh7VdJC91O1xuL15b8J+RqOKAjfCfkanigI3wn5GmXSQvdTtcbi9eW/CfkY1dJC87XG5uZXcgUmVnRXhwKFwiW/CfjrVdXCIpOyJ9)

```
/*eslint no-misleading-character-class: error */

/^[Á]$/u;
/^[❇️]$/u;
/^[👶🏻]$/u;
/^[🇯🇵]$/u;
/^[👨‍👩‍👦]$/u;
/^[👍]$/;
new RegExp("[🎵]");
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWlzbGVhZGluZy1jaGFyYWN0ZXItY2xhc3M6IGVycm9yICovXG5cbi9eW2FiY10kLztcbi9eW/CfkY1dJC91O1xuL15bXFxxe/Cfkbbwn4+7fV0kL3Y7XG5uZXcgUmVnRXhwKFwiXltdJFwiKTtcbm5ldyBSZWdFeHAoYFtBzIEtJHt6fV1gLCBcInVcIik7IC8vIHZhcmlhYmxlIHBhdHRlcm4ifQ==)

```
/*eslint no-misleading-character-class: error */

/^[abc]$/;
/^[👍]$/u;
/^[\q{👶🏻}]$/v;
new RegExp("^[]$");
new RegExp(`[Á-${z}]`, "u"); // variable pattern
1
2
3
4
5
6
7
```

## Options

This rule has an object option:

- `"allowEscape"`: When set to `true`, the rule allows any grouping of code points inside a character class as long as they are written using escape sequences. This option only has effect on regular expression literals and on regular expressions created with the `RegExp` constructor with a literal argument as a pattern.

### allowEscape

Examples of incorrect code for this rule with the `{ "allowEscape": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLW1pc2xlYWRpbmctY2hhcmFjdGVyLWNsYXNzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dFc2NhcGVcIjogdHJ1ZSB9XSAqL1xuXG4vW1xc8J+RjV0vOyAvLyBiYWNrc2xhc2ggY2FuIGJlIG9taXR0ZWRcblxubmV3IFJlZ0V4cChcIltcXHVkODNkXCIgKyBcIlxcdWRjNGRdXCIpO1xuXG5jb25zdCBwYXR0ZXJuID0gXCJbXFx1ZDgzZFxcdWRjNGRdXCI7XG5uZXcgUmVnRXhwKHBhdHRlcm4pOyJ9)

```
/* eslint no-misleading-character-class: ["error", { "allowEscape": true }] */

/[\👍]/; // backslash can be omitted

new RegExp("[\ud83d" + "\udc4d]");

const pattern = "[\ud83d\udc4d]";
new RegExp(pattern);
1
2
3
4
5
6
7
8
```

Examples of correct code for this rule with the `{ "allowEscape": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLW1pc2xlYWRpbmctY2hhcmFjdGVyLWNsYXNzOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dFc2NhcGVcIjogdHJ1ZSB9XSAqL1xuXG4vW1xcdWQ4M2RcXHVkYzRkXS87XG4vW1xcdTAwQjdcXHUwMzAwLVxcdTAzNkZdL3U7XG4vW/CfkahcXHUyMDBk8J+RqV0vdTtcbm5ldyBSZWdFeHAoXCJbXFx4NDFcXHUwMzAxXVwiKTtcbm5ldyBSZWdFeHAoYFtcXHV7MUYxRUZ9XFx1ezFGMUY1fV1gLCBcInVcIik7XG5uZXcgUmVnRXhwKFwiW1xcXFx1ezFGMUVGfVxcXFx1ezFGMUY1fV1cIiwgXCJ1XCIpOyJ9)

```
/* eslint no-misleading-character-class: ["error", { "allowEscape": true }] */

/[\ud83d\udc4d]/;
/[\u00B7\u0300-\u036F]/u;
/[👨\u200d👩]/u;
new RegExp("[\x41\u0301]");
new RegExp(`[\u{1F1EF}\u{1F1F5}]`, "u");
new RegExp("[\\u{1F1EF}\\u{1F1F5}]", "u");
1
2
3
4
5
6
7
8
```

## When Not To Use It

You can turn this rule off if you don’t want to check RegExp character class syntax for multiple code point characters.

## Version

This rule was introduced in ESLint v5.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-misleading-character-class.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-misleading-character-class.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-misleading-character-class.md
                    
                
                )
