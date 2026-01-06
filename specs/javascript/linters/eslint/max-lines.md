# max-lines

Enforce a maximum number of lines per file

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [max](#max)
  2. [skipBlankLines](#skipblanklines)
  3. [skipComments](#skipcomments)

3. [When Not To Use It](#when-not-to-use-it)
4. [Compatibility](#compatibility)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Further Reading](#further-reading)
8. [Resources](#resources)

Some people consider large files a code smell. Large files tend to do a lot of things and can make it hard following what’s going. While there is not an objective maximum number of lines considered acceptable in a file, most people would agree it should not be in the thousands. Recommendations usually range from 100 to 500 lines.

## Rule Details

This rule enforces a maximum number of lines per file, in order to aid in maintainability and reduce complexity.

Please note that most editors show an additional empty line at the end if the file ends with a line break. This rule does not count that extra line.

## Options

This rule has a number or object option:

- 

`"max"` (default `300`) enforces a maximum number of lines in a file.

- 

`"skipBlankLines": true` ignore lines made up purely of whitespace.

- 

`"skipComments": true` ignore lines containing just comments.

### max

Examples of incorrect code for this rule with a max value of `3`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCAzXSovXG5sZXQgYSxcbiAgICBiLFxuICAgIGM7In0=)

```
/*eslint max-lines: ["error", 3]*/
let a,
    b,
    c;
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCAzXSovXG5cbmxldCBhLFxuICAgIGIsYzsifQ==)

```
/*eslint max-lines: ["error", 3]*/

let a,
    b,c;
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCAzXSovXG4vLyBhIGNvbW1lbnRcbmxldCBhLFxuICAgIGIsYzsifQ==)

```
/*eslint max-lines: ["error", 3]*/
// a comment
let a,
    b,c;
1
2
3
4
```

Examples of correct code for this rule with a max value of `3`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCAzXSovXG5sZXQgYSxcbiAgICBiLCBjOyJ9)

```
/*eslint max-lines: ["error", 3]*/
let a,
    b, c;
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCAzXSovXG5cbmxldCBhLCBiLCBjOyJ9)

```
/*eslint max-lines: ["error", 3]*/

let a, b, c;
1
2
3
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCAzXSovXG4vLyBhIGNvbW1lbnRcbmxldCBhLCBiLCBjOyJ9)

```
/*eslint max-lines: ["error", 3]*/
// a comment
let a, b, c;
1
2
3
```

### skipBlankLines

Examples of incorrect code for this rule with the `{ "skipBlankLines": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCB7XCJtYXhcIjogMywgXCJza2lwQmxhbmtMaW5lc1wiOiB0cnVlfV0qL1xuXG5sZXQgYSxcbiAgICBiLFxuICAgIGM7In0=)

```
/*eslint max-lines: ["error", {"max": 3, "skipBlankLines": true}]*/

let a,
    b,
    c;
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "skipBlankLines": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCB7XCJtYXhcIjogMywgXCJza2lwQmxhbmtMaW5lc1wiOiB0cnVlfV0qL1xuXG5sZXQgYSxcbiAgICBiLCBjOyJ9)

```
/*eslint max-lines: ["error", {"max": 3, "skipBlankLines": true}]*/

let a,
    b, c;
1
2
3
4
```

### skipComments

Examples of incorrect code for this rule with the `{ "skipComments": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCB7XCJtYXhcIjogMiwgXCJza2lwQ29tbWVudHNcIjogdHJ1ZX1dKi9cbi8vIGEgY29tbWVudFxubGV0IGEsXG4gICAgYixcbiAgICBjOyJ9)

```
/*eslint max-lines: ["error", {"max": 2, "skipComments": true}]*/
// a comment
let a,
    b,
    c;
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "skipComments": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWxpbmVzOiBbXCJlcnJvclwiLCB7XCJtYXhcIjogMiwgXCJza2lwQ29tbWVudHNcIjogdHJ1ZX1dKi9cbi8vIGEgY29tbWVudFxubGV0IGEsXG4gICAgYiwgYzsifQ==)

```
/*eslint max-lines: ["error", {"max": 2, "skipComments": true}]*/
// a comment
let a,
    b, c;
1
2
3
4
```

## When Not To Use It

You can turn this rule off if you are not concerned with the number of lines in your files.

## Compatibility

- JSCS: [maximumNumberOfLines](https://jscs-dev.github.io/rule/maximumNumberOfLines)

## Related Rules

- [complexity](/docs/latest/rules/complexity)
- [max-depth](/docs/latest/rules/max-depth)
- [max-lines-per-function](/docs/latest/rules/max-lines-per-function)
- [max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)
- [max-params](/docs/latest/rules/max-params)
- [max-statements](/docs/latest/rules/max-statements)

## Version

This rule was introduced in ESLint v2.12.0.

## Further Reading

[Software Module size and file size](https://web.archive.org/web/20160725154648/http://www.mind2b.com/component/content/article/24-software-module-size-and-file-size)
 web.archive.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-lines.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-lines.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-lines.md
                    
                
                )
