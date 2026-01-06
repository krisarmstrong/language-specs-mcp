# sort-vars

Require variables within the same declaration block to be sorted

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [ignoreCase](#ignorecase)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

When declaring multiple variables within the same block, some developers prefer to sort variable names alphabetically to be able to find necessary variable easier at the later time. Others feel that it adds complexity and becomes burden to maintain.

## Rule Details

This rule checks all variable declaration blocks and verifies that all variables are sorted alphabetically. The default configuration of the rule is case-sensitive.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC12YXJzOiBcImVycm9yXCIqL1xuXG5sZXQgYiwgYTtcblxubGV0IGMsIEQsIGU7XG5cbmxldCBmLCBGOyJ9)

```
/*eslint sort-vars: "error"*/

let b, a;

let c, D, e;

let f, F;
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC12YXJzOiBcImVycm9yXCIqL1xuXG5sZXQgYSwgYiwgYywgZDtcblxubGV0IF9hID0gMTA7XG5sZXQgX2IgPSAyMDtcblxubGV0IEUsIGU7XG5cbmxldCBHLCBmLCBoOyJ9)

```
/*eslint sort-vars: "error"*/

let a, b, c, d;

let _a = 10;
let _b = 20;

let E, e;

let G, f, h;
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

Alphabetical list is maintained starting from the first variable and excluding any that are considered problems. So the following code will produce two problems:

```
/*eslint sort-vars: "error"*/

let c, d, a, b;
1
2
3
```

Copy code to clipboard

But this one, will only produce one:

```
/*eslint sort-vars: "error"*/

let c, d, a, e;
1
2
3
```

Copy code to clipboard

## Options

This rule has an object option:

- `"ignoreCase": true` (default `false`) ignores the case-sensitivity of the variables order

### ignoreCase

Examples of correct code for this rule with the `{ "ignoreCase": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgc29ydC12YXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2FzZVwiOiB0cnVlIH1dKi9cblxubGV0IGEsIEE7XG5cbmxldCBjLCBELCBlOyJ9)

```
/*eslint sort-vars: ["error", { "ignoreCase": true }]*/

let a, A;

let c, D, e;
1
2
3
4
5
```

## When Not To Use It

This rule is a formatting preference and not following it won’t negatively affect the quality of your code. If you alphabetizing variables isn’t a part of your coding standards, then you can leave this rule off.

## Related Rules

- [sort-keys](/docs/latest/rules/sort-keys)
- [sort-imports](/docs/latest/rules/sort-imports)

## Version

This rule was introduced in ESLint v0.2.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/sort-vars.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/sort-vars.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/sort-vars.md
                    
                
                )
