# no-irregular-whitespace

Disallow irregular whitespace

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [skipStrings](#skipstrings)
  2. [skipComments](#skipcomments)
  3. [skipRegExps](#skipregexps)
  4. [skipTemplates](#skiptemplates)
  5. [skipJSXText](#skipjsxtext)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Invalid or irregular whitespace causes issues with ECMAScript 5 parsers and also makes code harder to debug in a similar nature to mixed tabs and spaces.

Various whitespace characters can be inputted by programmers by mistake for example from copying or keyboard shortcuts. Pressing Alt + Space on macOS adds in a non breaking space character for example.

A simple fix for this problem could be to rewrite the offending line from scratch. This might also be a problem introduced by the text editor: if rewriting the line does not fix it, try using a different editor.

Known issues these spaces cause:

- Ogham Space Mark 

  - Is a valid token separator, but is rendered as a visible glyph in most typefaces, which may be misleading in source code.

- Mongolian Vowel Separator 

  - Is no longer considered a space separator since Unicode 6.3. It will result in a syntax error in current parsers when used in place of a regular token separator.

- Line Separator and Paragraph Separator 

  - These have always been valid whitespace characters and line terminators, but were considered illegal in string literals prior to ECMAScript 2019.

- Zero Width Space 

  - Is NOT considered a separator for tokens and is often parsed as an `Unexpected token ILLEGAL`.
  - Is NOT shown in modern browsers making code repository software expected to resolve the visualization.

In JSON, none of the characters listed as irregular whitespace by this rule may appear outside of a string.

## Rule Details

This rule is aimed at catching invalid whitespace that is not a normal tab and space. Some of these characters may cause issues in modern browsers and others will be a debugging issue to spot.

This rule disallows the following characters except where the options allow:

```
\u000B - Line Tabulation (\v) - <VT>
\u000C - Form Feed (\f) - <FF>
\u0085 - Next Line - <NEL>
\u00A0 - No-Break Space - <NBSP>
\u1680 - Ogham Space Mark - <OGSP>
\u180E - Mongolian Vowel Separator - <MVS>
\u2000 - En Quad - <NQSP>
\u2001 - Em Quad - <MQSP>
\u2002 - En Space - <ENSP>
\u2003 - Em Space - <EMSP>
\u2004 - Three-Per-Em - <THPMSP> - <3/MSP>
\u2005 - Four-Per-Em - <FPMSP> - <4/MSP>
\u2006 - Six-Per-Em - <SPMSP> - <6/MSP>
\u2007 - Figure Space - <FSP>
\u2008 - Punctuation Space - <PUNCSP>
\u2009 - Thin Space - <THSP>
\u200A - Hair Space - <HSP>
\u200B - Zero Width Space - <ZWSP>
\u2028 - Line Separator - <LS> - <LSEP>
\u2029 - Paragraph Separator - <PS> - <PSEP>
\u202F - Narrow No-Break Space - <NNBSP>
\u205F - Medium Mathematical Space - <MMSP>
\u3000 - Ideographic Space - <IDSP>
\uFEFF - Zero Width No-Break Space - <BOM>
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
```

Copy code to clipboard

## Options

This rule has an object option for exceptions:

- `"skipStrings": true` (default) allows any whitespace characters in string literals
- `"skipComments": true` allows any whitespace characters in comments
- `"skipRegExps": true` allows any whitespace characters in regular expression literals
- `"skipTemplates": true` allows any whitespace characters in template literals
- `"skipJSXText": true` allows any whitespace characters in JSX text

### skipStrings

Examples of incorrect code for this rule with the default `{ "skipStrings": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXJyZWd1bGFyLXdoaXRlc3BhY2U6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHRoaW5nID0gZnVuY3Rpb24oKcKgLyo8TkJTUD4qL3tcbiAgICByZXR1cm4gJ3Rlc3QnO1xufVxuXG5jb25zdCBmb28gPSBmdW5jdGlvbijCoC8qPE5CU1A+Ki8pe1xuICAgIHJldHVybiAndGVzdCc7XG59XG5cbmNvbnN0IGJhciA9IGZ1bmN0aW9uwqAvKjxOQlNQPiovKCl7XG4gICAgcmV0dXJuICd0ZXN0Jztcbn1cblxuY29uc3QgYmF6ID0gZnVuY3Rpb27hmoAvKjxPZ2hhbSBTcGFjZSBNYXJrPiovKCl7XG4gICAgcmV0dXJuICd0ZXN0Jztcbn1cblxuY29uc3QgcXV4ID0gZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuICd0ZXN0JzvigIIvKjxFTlNQPiovXG59XG5cbmNvbnN0IHF1dXggPSBmdW5jdGlvbigpIHtcbiAgICByZXR1cm4gJ3Rlc3QnO8KgLyo8TkJTUD4qL1xufVxuXG5jb25zdCBpdGVtID0gZnVuY3Rpb24oKSB7XG4gICAgLy8gRGVzY3JpcHRpb27CoDxOQlNQPjogc29tZSBkZXNjcmlwdGl2ZSB0ZXh0XG59XG5cbi8qXG5EZXNjcmlwdGlvbsKgPE5CU1A+OiBzb21lIGRlc2NyaXB0aXZlIHRleHRcbiovXG5cbmNvbnN0IGZ1bmMgPSBmdW5jdGlvbigpIHtcbiAgICByZXR1cm4gL8KgPE5CU1A+cmVnZXhwLztcbn1cblxuY29uc3QgbXlGdW5jID0gZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuIGB0ZW1wbGF0ZeKAgjxOQlNQPnN0cmluZ2A7XG59In0=)

```
/*eslint no-irregular-whitespace: "error"*/

const thing = function() /*<NBSP>*/{
    return 'test';
}

const foo = function( /*<NBSP>*/){
    return 'test';
}

const bar = function /*<NBSP>*/(){
    return 'test';
}

const baz = function /*<Ogham Space Mark>*/(){
    return 'test';
}

const qux = function() {
    return 'test'; /*<ENSP>*/
}

const quux = function() {
    return 'test'; /*<NBSP>*/
}

const item = function() {
    // Description <NBSP>: some descriptive text
}

/*
Description <NBSP>: some descriptive text
*/

const func = function() {
    return / <NBSP>regexp/;
}

const myFunc = function() {
    return `template <NBSP>string`;
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
30
31
32
33
34
35
36
37
38
39
40
41
```

Examples of correct code for this rule with the default `{ "skipStrings": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXJyZWd1bGFyLXdoaXRlc3BhY2U6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHRoaW5nID0gZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuICfCoDxOQlNQPnRoaW5nJztcbn1cblxuY29uc3QgZm9vID0gZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuICfigIs8WldTUD50aGluZyc7XG59XG5cbmNvbnN0IGJhciA9IGZ1bmN0aW9uKCkge1xuICAgIHJldHVybiAndGjCoDxOQlNQPmluZyc7XG59In0=)

```
/*eslint no-irregular-whitespace: "error"*/

const thing = function() {
    return ' <NBSP>thing';
}

const foo = function() {
    return '​<ZWSP>thing';
}

const bar = function() {
    return 'th <NBSP>ing';
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
```

### skipComments

Examples of additional correct code for this rule with the `{ "skipComments": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXJyZWd1bGFyLXdoaXRlc3BhY2U6IFtcImVycm9yXCIsIHsgXCJza2lwQ29tbWVudHNcIjogdHJ1ZSB9XSovXG5cbmZ1bmN0aW9uIHRoaW5nKCkge1xuICAgIC8vIERlc2NyaXB0aW9uwqA8TkJTUD46IHNvbWUgZGVzY3JpcHRpdmUgdGV4dFxufVxuXG4vKlxuRGVzY3JpcHRpb27CoDxOQlNQPjogc29tZSBkZXNjcmlwdGl2ZSB0ZXh0XG4qLyJ9)

```
/*eslint no-irregular-whitespace: ["error", { "skipComments": true }]*/

function thing() {
    // Description <NBSP>: some descriptive text
}

/*
Description <NBSP>: some descriptive text
*/
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

### skipRegExps

Examples of additional correct code for this rule with the `{ "skipRegExps": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXJyZWd1bGFyLXdoaXRlc3BhY2U6IFtcImVycm9yXCIsIHsgXCJza2lwUmVnRXhwc1wiOiB0cnVlIH1dKi9cblxuZnVuY3Rpb24gdGhpbmcoKSB7XG4gICAgcmV0dXJuIC/CoDxOQlNQPnJlZ2V4cC87XG59In0=)

```
/*eslint no-irregular-whitespace: ["error", { "skipRegExps": true }]*/

function thing() {
    return / <NBSP>regexp/;
}
1
2
3
4
5
```

### skipTemplates

Examples of additional correct code for this rule with the `{ "skipTemplates": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXJyZWd1bGFyLXdoaXRlc3BhY2U6IFtcImVycm9yXCIsIHsgXCJza2lwVGVtcGxhdGVzXCI6IHRydWUgfV0qL1xuXG5mdW5jdGlvbiB0aGluZygpIHtcbiAgICByZXR1cm4gYHRlbXBsYXRl4oCCPE5CU1A+c3RyaW5nYDtcbn0ifQ==)

```
/*eslint no-irregular-whitespace: ["error", { "skipTemplates": true }]*/

function thing() {
    return `template <NBSP>string`;
}
1
2
3
4
5
```

### skipJSXText

Examples of additional correct code for this rule with the `{ "skipJSXText": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXJPcHRpb25zIjp7ImVjbWFGZWF0dXJlcyI6eyJqc3giOnRydWV9fX19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taXJyZWd1bGFyLXdoaXRlc3BhY2U6IFtcImVycm9yXCIsIHsgXCJza2lwSlNYVGV4dFwiOiB0cnVlIH1dKi9cblxuZnVuY3Rpb24gVGhpbmcoKSB7XG4gICAgcmV0dXJuIDxkaXY+dGV4dCBpbuKAgkpTWDwvZGl2PjsgLy8gPE5CU1A+IGJlZm9yZSBgSlNYYFxufSJ9)

```
/*eslint no-irregular-whitespace: ["error", { "skipJSXText": true }]*/

function Thing() {
    return <div>text in JSX</div>; // <NBSP> before `JSX`
}
1
2
3
4
5
```

## When Not To Use It

If you decide that you wish to use whitespace other than tabs and spaces outside of strings in your application.

## Version

This rule was introduced in ESLint v0.9.0.

## Further Reading

[Annotated ES5](https://es5.github.io/#x7.2)
 es5.github.io[JSON: The JavaScript subset that isn’t - Timeless](https://web.archive.org/web/20200414142829/http://timelessrepo.com/json-isnt-a-javascript-subset)
 web.archive.org[U+1680 OGHAM SPACE MARK:   – Unicode – Codepoints](https://codepoints.net/U+1680)
 codepoints.net

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-irregular-whitespace.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-irregular-whitespace.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-irregular-whitespace.md
                    
                
                )
