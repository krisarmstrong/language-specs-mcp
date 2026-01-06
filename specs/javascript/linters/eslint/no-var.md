# no-var

Require `let` or `const` instead of `var`

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

ECMAScript 6 allows programmers to create variables with block scope instead of function scope using the `let` and `const` keywords. Block scope is common in many other programming languages and helps programmers avoid mistakes such as:

```
var count = people.length;
var enoughFood = sandwiches.length >= count;

if (enoughFood) {
    var count = sandwiches.length; // accidentally overriding the count variable
    console.log("We have " + count + " sandwiches for everyone. Plenty for all!");
}

// our count variable is no longer accurate
console.log("We have " + count + " people and " + sandwiches.length + " sandwiches!");
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

Copy code to clipboard

## Rule Details

This rule is aimed at discouraging the use of `var` and encouraging the use of `const` or `let` instead.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdmFyOiBcImVycm9yXCIqL1xuXG52YXIgeCA9IFwieVwiO1xudmFyIENPTkZJRyA9IHt9OyJ9)

```
/*eslint no-var: "error"*/

var x = "y";
var CONFIG = {};
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdmFyOiBcImVycm9yXCIqL1xuXG5sZXQgeCA9IFwieVwiO1xuY29uc3QgQ09ORklHID0ge307In0=)

```
/*eslint no-var: "error"*/

let x = "y";
const CONFIG = {};
1
2
3
4
```

This rule additionally supports TypeScript type syntax. There are multiple ways to declare global variables in TypeScript. Only using `var` works for all cases. See this [TypeScript playground](https://www.typescriptlang.org/play/?#code/PQgEB4CcFMDNpgOwMbVAGwJYCMC8AiAEwHsBbfUYAPgFgAoew6ZdAQxlAHN1jtX1QAb3qhRGaABdQAGUkAuUAGcJkTIk4ixAN3agAauwXLV6+ptFqJCWK1SgA6mpIB3IebGjHiIyrUa6HgC+9MEMdGDcvPygtqiKivSyEvQGkPReZuHAoM5OxK6ckvS5iC4AdEnFec5lqVWl+WUZYWAlLkpFdG2NSaC4oADkA-XlqX2Dw13VTWrjQ5kRPHzoACoAFpiKXJ2Ry+ubFTtL-PuKtez0uycbZ830i1GrNx3JdFdPB73982-HH2djb6Td6nGaIOaTe7ZRTQdCwbavGFww6I2Gwc5pOhI9F3LIdOEvejYlEQolojGkrHkryU+jQAAeAAdiJApIJAkA) for reference.

Examples of incorrect TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby12YXI6IFwiZXJyb3JcIiovXG5cbmRlY2xhcmUgdmFyIHg6IG51bWJlclxuXG5kZWNsYXJlIG5hbWVzcGFjZSBucyB7XG5cdHZhciB4OiBudW1iZXJcbn1cblxuZGVjbGFyZSBtb2R1bGUgJ21vZHVsZScge1xuXHR2YXIgeDogbnVtYmVyXG59In0=)

```
/*eslint no-var: "error"*/

declare var x: number

declare namespace ns {
	var x: number
}

declare module 'module' {
	var x: number
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
```

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby12YXI6IFwiZXJyb3JcIiovXG5cbmRlY2xhcmUgZ2xvYmFsIHtcbiAgICBkZWNsYXJlIHZhciB4OiBudW1iZXJcbn0ifQ==)

```
/*eslint no-var: "error"*/

declare global {
    declare var x: number
}
1
2
3
4
5
```

## When Not To Use It

In addition to non-ES6 environments, existing JavaScript projects that are beginning to introduce ES6 into their codebase may not want to apply this rule if the cost of migrating from `var` to `let` is too costly.

## Version

This rule was introduced in ESLint v0.12.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-var.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-var.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-var.md
                    
                
                )
