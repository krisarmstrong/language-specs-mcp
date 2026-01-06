# default-param-last

Enforce default parameters to be last

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Resources](#resources)

Putting default parameter at last allows function calls to omit optional tail arguments.

```
// Correct: optional argument can be omitted
function createUser(id, isAdmin = false) {}
createUser("tabby")

// Incorrect: optional argument can **not** be omitted
function createUser(isAdmin = false, id) {}
createUser(undefined, "tabby")
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

This rule enforces default parameters to be the last of parameters.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGRlZmF1bHQtcGFyYW0tbGFzdDogW1wiZXJyb3JcIl0gKi9cblxuZnVuY3Rpb24gZihhID0gMCwgYikge31cblxuZnVuY3Rpb24gZyhhLCBiID0gMCwgYykge30ifQ==)

```
/* eslint default-param-last: ["error"] */

function f(a = 0, b) {}

function g(a, b = 0, c) {}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IGRlZmF1bHQtcGFyYW0tbGFzdDogW1wiZXJyb3JcIl0gKi9cblxuZnVuY3Rpb24gZihhLCBiID0gMCkge31cblxuZnVuY3Rpb24gZyhhLCBiID0gMCwgYyA9IDApIHt9In0=)

```
/* eslint default-param-last: ["error"] */

function f(a, b = 0) {}

function g(a, b = 0, c = 0) {}
1
2
3
4
5
```

This rule additionally supports TypeScript type syntax.

Examples of incorrect TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgZGVmYXVsdC1wYXJhbS1sYXN0OiBbXCJlcnJvclwiXSAqL1xuXG5mdW5jdGlvbiBoKGEgPSAwLCBiOiBudW1iZXIpIHt9In0=)

```
/* eslint default-param-last: ["error"] */

function h(a = 0, b: number) {}
1
2
3
```

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgZGVmYXVsdC1wYXJhbS1sYXN0OiBbXCJlcnJvclwiXSAqL1xuXG5mdW5jdGlvbiBoKGEgPSAwLCBiPzogbnVtYmVyKSB7fSJ9)

```
/* eslint default-param-last: ["error"] */

function h(a = 0, b?: number) {}
1
2
3
```

## Version

This rule was introduced in ESLint v6.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/default-param-last.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/default-param-last.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/default-param-last.md
                    
                
                )
