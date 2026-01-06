# prefer-named-capture-group

Enforce using named capture group in regular expression

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

## Rule Details

With the landing of ECMAScript 2018, named capture groups can be used in regular expressions, which can improve their readability. This rule is aimed at using named capture groups instead of numbered capture groups in regular expressions:

```
const regex = /(?<year>[0-9]{4})/;
1
```

Copy code to clipboard

Alternatively, if your intention is not to capture the results, but only express the alternative, use a non-capturing group:

```
const regex = /(?:cauli|sun)flower/;
1
```

Copy code to clipboard

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW5hbWVkLWNhcHR1cmUtZ3JvdXA6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IC8oYmFbcnpdKS87XG5jb25zdCBiYXIgPSBuZXcgUmVnRXhwKCcoYmFbcnpdKScpO1xuY29uc3QgYmF6ID0gUmVnRXhwKCcoYmFbcnpdKScpO1xuXG5mb28uZXhlYygnYmFyJylbMV07IC8vIFJldHJpZXZlIHRoZSBncm91cCByZXN1bHQuIn0=)

```
/*eslint prefer-named-capture-group: "error"*/

const foo = /(ba[rz])/;
const bar = new RegExp('(ba[rz])');
const baz = RegExp('(ba[rz])');

foo.exec('bar')[1]; // Retrieve the group result.
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW5hbWVkLWNhcHR1cmUtZ3JvdXA6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGZvbyA9IC8oPzxpZD5iYVtyel0pLztcbmNvbnN0IGJhciA9IG5ldyBSZWdFeHAoJyg/PGlkPmJhW3J6XSknKTtcbmNvbnN0IGJheiA9IFJlZ0V4cCgnKD88aWQ+YmFbcnpdKScpO1xuY29uc3QgeHl6ID0gL3h5eig/Onp5fGFiYykvO1xuXG5mb28uZXhlYygnYmFyJykuZ3JvdXBzLmlkOyAvLyBSZXRyaWV2ZSB0aGUgZ3JvdXAgcmVzdWx0LiJ9)

```
/*eslint prefer-named-capture-group: "error"*/

const foo = /(?<id>ba[rz])/;
const bar = new RegExp('(?<id>ba[rz])');
const baz = RegExp('(?<id>ba[rz])');
const xyz = /xyz(?:zy|abc)/;

foo.exec('bar').groups.id; // Retrieve the group result.
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

If you are targeting ECMAScript 2017 and/or older environments, you should not use this rule, because this ECMAScript feature is only supported in ECMAScript 2018 and/or newer environments.

## Related Rules

- [no-invalid-regexp](/docs/latest/rules/no-invalid-regexp)

## Version

This rule was introduced in ESLint v5.15.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-named-capture-group.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-named-capture-group.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-named-capture-group.md
                    
                
                )
