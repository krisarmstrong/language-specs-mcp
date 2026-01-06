# no-array-constructor

Disallow `Array` constructors

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Use of the `Array` constructor to construct a new array is generally discouraged in favor of array literal notation because of the single-argument pitfall and because the `Array` global may be redefined. The exception is when the `Array` constructor is used to intentionally create sparse arrays of a specified size by giving the constructor a single numeric argument.

## Rule Details

This rule disallows `Array` constructors.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYXJyYXktY29uc3RydWN0b3I6IFwiZXJyb3JcIiovXG5cbkFycmF5KCk7XG5cbkFycmF5KDAsIDEsIDIpO1xuXG5uZXcgQXJyYXkoMCwgMSwgMik7XG5cbkFycmF5KC4uLmFyZ3MpOyJ9)

```
/*eslint no-array-constructor: "error"*/

Array();

Array(0, 1, 2);

new Array(0, 1, 2);

Array(...args);
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tYXJyYXktY29uc3RydWN0b3I6IFwiZXJyb3JcIiovXG5cbkFycmF5KDUwMCk7XG5cbm5ldyBBcnJheShzb21lT3RoZXJBcnJheS5sZW5ndGgpO1xuXG5bMCwgMSwgMl07XG5cbmNvbnN0IGNyZWF0ZUFycmF5ID0gQXJyYXkgPT4gbmV3IEFycmF5KCk7In0=)

```
/*eslint no-array-constructor: "error"*/

Array(500);

new Array(someOtherArray.length);

[0, 1, 2];

const createArray = Array => new Array();
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

This rule additionally supports TypeScript type syntax.

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1hcnJheS1jb25zdHJ1Y3RvcjogXCJlcnJvclwiKi9cblxubmV3IEFycmF5PG51bWJlcj4oMSwgMiwgMyk7XG5cbm5ldyBBcnJheTxGb28+KCk7XG5cbkFycmF5PG51bWJlcj4oMSwgMiwgMyk7XG5cbkFycmF5PEZvbz4oKTtcblxuQXJyYXk/LmZvbygpOyJ9)

```
/*eslint no-array-constructor: "error"*/

new Array<number>(1, 2, 3);

new Array<Foo>();

Array<number>(1, 2, 3);

Array<Foo>();

Array?.foo();
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

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1hcnJheS1jb25zdHJ1Y3RvcjogXCJlcnJvclwiKi9cblxubmV3IEFycmF5KCk7XG5cbm5ldyBBcnJheSgwLCAxLCAyKTtcblxuQXJyYXk/Lih4LCB5KTtcblxuQXJyYXk/LigwLCAxLCAyKTsifQ==)

```
/*eslint no-array-constructor: "error"*/

new Array();

new Array(0, 1, 2);

Array?.(x, y);

Array?.(0, 1, 2);
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

## When Not To Use It

This rule enforces a nearly universal stylistic concern. That being said, this rule may be disabled if the constructor style is preferred.

## Related Rules

- [no-new-wrappers](/docs/latest/rules/no-new-wrappers)
- [no-object-constructor](/docs/latest/rules/no-object-constructor)

## Version

This rule was introduced in ESLint v0.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-array-constructor.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-array-constructor.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-array-constructor.md
                    
                
                )
