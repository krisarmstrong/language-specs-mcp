# dot-notation

Enforce dot notation whenever possible

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowKeywords](#allowkeywords)
  2. [allowPattern](#allowpattern)

3. [Version](#version)
4. [Resources](#resources)

In JavaScript, one can access properties using the dot notation (`foo.bar`) or square-bracket notation (`foo["bar"]`). However, the dot notation is often preferred because it is easier to read, less verbose, and works better with aggressive JavaScript minimizers.

```
foo["bar"];
1
```

Copy code to clipboard

## Rule Details

This rule is aimed at maintaining code consistency and improving code readability by encouraging use of the dot notation style whenever possible. As such, it will warn when it encounters an unnecessary use of square-bracket notation.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZG90LW5vdGF0aW9uOiBcImVycm9yXCIqL1xuXG5jb25zdCB4ID0gZm9vW1wiYmFyXCJdOyJ9)

```
/*eslint dot-notation: "error"*/

const x = foo["bar"];
1
2
3
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZG90LW5vdGF0aW9uOiBcImVycm9yXCIqL1xuXG5jb25zdCB4ID0gZm9vLmJhcjtcblxuY29uc3QgeSA9IGZvb1tiYXJdOyAgICAvLyBQcm9wZXJ0eSBuYW1lIGlzIGEgdmFyaWFibGUsIHNxdWFyZS1icmFja2V0IG5vdGF0aW9uIHJlcXVpcmVkIn0=)

```
/*eslint dot-notation: "error"*/

const x = foo.bar;

const y = foo[bar];    // Property name is a variable, square-bracket notation required
1
2
3
4
5
```

## Options

This rule accepts a single options argument:

- Set the `allowKeywords` option to `false` (default is `true`) to follow ECMAScript version 3 compatible style, avoiding dot notation for reserved word properties.
- Set the `allowPattern` option to a regular expression string to allow bracket notation for property names that match a pattern (by default, no pattern is tested).

### allowKeywords

Examples of correct code for the `{ "allowKeywords": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZG90LW5vdGF0aW9uOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dLZXl3b3Jkc1wiOiBmYWxzZSB9XSovXG5cbmNvbnN0IGZvbyA9IHsgXCJjbGFzc1wiOiBcIkNTIDEwMVwiIH1cbmNvbnN0IHggPSBmb29bXCJjbGFzc1wiXTsgLy8gUHJvcGVydHkgbmFtZSBpcyBhIHJlc2VydmVkIHdvcmQsIHNxdWFyZS1icmFja2V0IG5vdGF0aW9uIHJlcXVpcmVkIn0=)

```
/*eslint dot-notation: ["error", { "allowKeywords": false }]*/

const foo = { "class": "CS 101" }
const x = foo["class"]; // Property name is a reserved word, square-bracket notation required
1
2
3
4
```

Examples of additional correct code for the `{ "allowKeywords": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZG90LW5vdGF0aW9uOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dLZXl3b3Jkc1wiOiBmYWxzZSB9XSovXG5cbmNsYXNzIEMge1xuICAgICNpbjtcbiAgICBmb28oKSB7XG4gICAgICAgIHRoaXMuI2luOyAvLyBEb3Qgbm90YXRpb24gaXMgcmVxdWlyZWQgZm9yIHByaXZhdGUgaWRlbnRpZmllcnNcbiAgICB9XG59In0=)

```
/*eslint dot-notation: ["error", { "allowKeywords": false }]*/

class C {
    #in;
    foo() {
        this.#in; // Dot notation is required for private identifiers
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
```

### allowPattern

For example, when preparing data to be sent to an external API, it is often required to use property names that include underscores. If the `camelcase` rule is in effect, these [snake case](https://en.wikipedia.org/wiki/Snake_case) properties would not be allowed. By providing an `allowPattern` to the `dot-notation` rule, these snake case properties can be accessed with bracket notation.

Examples of incorrect code for the sample `{ "allowPattern": "^[a-z]+(_[a-z]+)+$" }` (pattern to find snake case named properties) option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZG90LW5vdGF0aW9uOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dQYXR0ZXJuXCI6IFwiXlthLXpdKyhfW2Etel0rKSskXCIgfV0qL1xuXG5jb25zdCBkYXRhID0ge307XG5kYXRhW1wiZm9vQmFyXCJdID0gNDI7In0=)

```
/*eslint dot-notation: ["error", { "allowPattern": "^[a-z]+(_[a-z]+)+$" }]*/

const data = {};
data["fooBar"] = 42;
1
2
3
4
```

Examples of correct code for the sample `{ "allowPattern": "^[a-z]+(_[a-z]+)+$" }` (pattern to find snake case named properties) option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZG90LW5vdGF0aW9uOiBbXCJlcnJvclwiLCB7IFwiYWxsb3dQYXR0ZXJuXCI6IFwiXlthLXpdKyhfW2Etel0rKSskXCIgfV0qL1xuXG5jb25zdCBkYXRhID0ge307XG5kYXRhW1wiZm9vX2JhclwiXSA9IDQyOyJ9)

```
/*eslint dot-notation: ["error", { "allowPattern": "^[a-z]+(_[a-z]+)+$" }]*/

const data = {};
data["foo_bar"] = 42;
1
2
3
4
```

## Version

This rule was introduced in ESLint v0.0.7.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/dot-notation.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/dot-notation.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/dot-notation.md
                    
                
                )
