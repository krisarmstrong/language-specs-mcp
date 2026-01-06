# no-dupe-args

Disallow duplicate arguments in `function` definitions

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Handled by TypeScript](#handled_by_typescript)
3. [Version](#version)
4. [Resources](#resources)

If more than one parameter has the same name in a function definition, the last occurrence “shadows” the preceding occurrences. A duplicated name might be a typing error.

## Rule Details

This rule disallows duplicate parameter names in function declarations or expressions. It does not apply to arrow functions or class methods, because the parser reports the error.

If ESLint parses code in strict mode, the parser (instead of this rule) reports the error.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1hcmdzOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBmb28oYSwgYiwgYSkge1xuICAgIGNvbnNvbGUubG9nKFwidmFsdWUgb2YgdGhlIHNlY29uZCBhOlwiLCBhKTtcbn1cblxuY29uc3QgYmFyID0gZnVuY3Rpb24gKGEsIGIsIGEpIHtcbiAgICBjb25zb2xlLmxvZyhcInZhbHVlIG9mIHRoZSBzZWNvbmQgYTpcIiwgYSk7XG59OyJ9)

```
/*eslint no-dupe-args: "error"*/

function foo(a, b, a) {
    console.log("value of the second a:", a);
}

const bar = function (a, b, a) {
    console.log("value of the second a:", a);
};
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

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1hcmdzOiBcImVycm9yXCIqL1xuXG5mdW5jdGlvbiBmb28oYSwgYiwgYykge1xuICAgIGNvbnNvbGUubG9nKGEsIGIsIGMpO1xufVxuXG5jb25zdCBiYXIgPSBmdW5jdGlvbiAoYSwgYiwgYykge1xuICAgIGNvbnNvbGUubG9nKGEsIGIsIGMpO1xufTsifQ==)

```
/*eslint no-dupe-args: "error"*/

function foo(a, b, c) {
    console.log(a, b, c);
}

const bar = function (a, b, c) {
    console.log(a, b, c);
};
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

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v0.16.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-dupe-args.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-dupe-args.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-dupe-args.md
                    
                
                )
