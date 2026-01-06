# no-magic-numbers

Disallow magic numbers

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [ignore](#ignore)
  2. [ignoreArrayIndexes](#ignorearrayindexes)
  3. [ignoreDefaultValues](#ignoredefaultvalues)
  4. [ignoreClassFieldInitialValues](#ignoreclassfieldinitialvalues)
  5. [enforceConst](#enforceconst)
  6. [detectObjects](#detectobjects)
  7. [ignoreEnums (TypeScript only)](#ignoreenums-typescript-only)
  8. [ignoreNumericLiteralTypes (TypeScript only)](#ignorenumericliteraltypes-typescript-only)
  9. [ignoreReadonlyClassProperties (TypeScript only)](#ignorereadonlyclassproperties-typescript-only)
  10. [ignoreTypeIndexes (TypeScript only)](#ignoretypeindexes-typescript-only)

3. [Version](#version)
4. [Resources](#resources)

‘Magic numbers’ are numbers that occur multiple times in code without an explicit meaning. They should preferably be replaced by named constants.

```
const now = Date.now(),
    inOneHour = now + (60 * 60 * 1000);
1
2
```

Copy code to clipboard

## Rule Details

The `no-magic-numbers` rule aims to make code more readable and refactoring easier by ensuring that special numbers are declared as constants to make their meaning explicit.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogXCJlcnJvclwiKi9cblxuY29uc3QgZHV0eUZyZWVQcmljZSA9IDEwMCxcbiAgICBmaW5hbFByaWNlID0gZHV0eUZyZWVQcmljZSArIChkdXR5RnJlZVByaWNlICogMC4yNSk7In0=)

```
/*eslint no-magic-numbers: "error"*/

const dutyFreePrice = 100,
    finalPrice = dutyFreePrice + (dutyFreePrice * 0.25);
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogXCJlcnJvclwiKi9cblxuY29uc3QgZGF0YSA9IFsnZm9vJywgJ2JhcicsICdiYXonXTtcblxuY29uc3QgZGF0YUxhc3QgPSBkYXRhWzJdOyJ9)

```
/*eslint no-magic-numbers: "error"*/

const data = ['foo', 'bar', 'baz'];

const dataLast = data[2];
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogXCJlcnJvclwiKi9cblxubGV0IFNFQ09ORFM7XG5cblNFQ09ORFMgPSA2MDsifQ==)

```
/*eslint no-magic-numbers: "error"*/

let SECONDS;

SECONDS = 60;
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogXCJlcnJvclwiKi9cblxuY29uc3QgVEFYID0gMC4yNTtcblxuY29uc3QgZHV0eUZyZWVQcmljZSA9IDEwMCxcbiAgICBmaW5hbFByaWNlID0gZHV0eUZyZWVQcmljZSArIChkdXR5RnJlZVByaWNlICogVEFYKTsifQ==)

```
/*eslint no-magic-numbers: "error"*/

const TAX = 0.25;

const dutyFreePrice = 100,
    finalPrice = dutyFreePrice + (dutyFreePrice * TAX);
1
2
3
4
5
6
```

## Options

### ignore

An array of numbers to ignore. It’s set to `[]` by default. If provided, it must be an `Array`.

The array can contain values of `number` and `string` types. If it’s a string, the text must be parsed as `bigint` literal (e.g., `"100n"`).

Examples of correct code for the sample `{ "ignore": [1] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZVwiOiBbMV0gfV0qL1xuXG5jb25zdCBkYXRhID0gWydmb28nLCAnYmFyJywgJ2JheiddO1xuY29uc3QgZGF0YUxhc3QgPSBkYXRhLmxlbmd0aCAmJiBkYXRhW2RhdGEubGVuZ3RoIC0gMV07In0=)

```
/*eslint no-magic-numbers: ["error", { "ignore": [1] }]*/

const data = ['foo', 'bar', 'baz'];
const dataLast = data.length && data[data.length - 1];
1
2
3
4
```

Examples of correct code for the sample `{ "ignore": ["1n"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZVwiOiBbXCIxblwiXSB9XSovXG5cbmZvbygxbik7In0=)

```
/*eslint no-magic-numbers: ["error", { "ignore": ["1n"] }]*/

foo(1n);
1
2
3
```

### ignoreArrayIndexes

A boolean to specify if numbers used in the context of array indexes (e.g., `data[2]`) are considered okay. `false` by default.

This option allows only valid array indexes: numbers that will be coerced to one of `"0"`, `"1"`, `"2"` … `"4294967294"`.

Arrays are objects, so they can have property names such as `"-1"` or `"2.5"`. However, those are just “normal” object properties that don’t represent array elements. They don’t influence the array’s `length`, and they are ignored by array methods like `.map` or `.forEach`.

Additionally, since the maximum [array length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length) is 232 - 1, all values above 232 - 2 also represent just normal property names and are thus not considered to be array indexes.

Examples of correct code for the `{ "ignoreArrayIndexes": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZUFycmF5SW5kZXhlc1wiOiB0cnVlIH1dKi9cblxuY29uc3QgaXRlbSA9IGRhdGFbMl07XG5cbmRhdGFbMTAwXSA9IGE7XG5cbmYoZGF0YVswXSk7XG5cbmEgPSBkYXRhWy0wXTsgLy8gc2FtZSBhcyBkYXRhWzBdLCAtMCB3aWxsIGJlIGNvZXJjZWQgdG8gXCIwXCJcbmEgPSBkYXRhWysxXTsgLy8gc2FtZSBhcyBkYXRhWzFdLCArMSB3aWxsIGJlIGNvZXJjZWQgdG8gXCIxXCJcblxuYSA9IGRhdGFbMHhBQl07XG5cbmEgPSBkYXRhWzUuNmUxXTtcblxuYSA9IGRhdGFbMTBuXTsgLy8gc2FtZSBhcyBkYXRhWzEwXSwgMTBuIHdpbGwgYmUgY29lcmNlZCB0byBcIjEwXCJcblxuYSA9IGRhdGFbNDI5NDk2NzI5NF07IC8vIG1heCBhcnJheSBpbmRleCJ9)

```
/*eslint no-magic-numbers: ["error", { "ignoreArrayIndexes": true }]*/

const item = data[2];

data[100] = a;

f(data[0]);

a = data[-0]; // same as data[0], -0 will be coerced to "0"
a = data[+1]; // same as data[1], +1 will be coerced to "1"

a = data[0xAB];

a = data[5.6e1];

a = data[10n]; // same as data[10], 10n will be coerced to "10"

a = data[4294967294]; // max array index
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
```

Examples of incorrect code for the `{ "ignoreArrayIndexes": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZUFycmF5SW5kZXhlc1wiOiB0cnVlIH1dKi9cblxuZigyKTsgLy8gbm90IHVzZWQgYXMgYXJyYXkgaW5kZXhcblxuYSA9IGRhdGFbLTFdO1xuXG5hID0gZGF0YVsyLjVdO1xuXG5hID0gZGF0YVs1LjY3ZTFdO1xuXG5hID0gZGF0YVstMTBuXTtcblxuYSA9IGRhdGFbNDI5NDk2NzI5NV07IC8vIGFib3ZlIHRoZSBtYXggYXJyYXkgaW5kZXhcblxuYSA9IGRhdGFbMWU1MDBdOyAvLyBzYW1lIGFzIGRhdGFbXCJJbmZpbml0eVwiXSJ9)

```
/*eslint no-magic-numbers: ["error", { "ignoreArrayIndexes": true }]*/

f(2); // not used as array index

a = data[-1];

a = data[2.5];

a = data[5.67e1];

a = data[-10n];

a = data[4294967295]; // above the max array index

a = data[1e500]; // same as data["Infinity"]
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
```

### ignoreDefaultValues

A boolean to specify if numbers used in default value assignments are considered okay. `false` by default.

Examples of correct code for the `{ "ignoreDefaultValues": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZURlZmF1bHRWYWx1ZXNcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IHsgdGF4ID0gMC4yNSB9ID0gYWNjb3VudGFuY3k7XG5cbmZ1bmN0aW9uIG1hcFBhcmFsbGVsKGNvbmN1cnJlbmN5ID0gMykgeyAvKioqLyB9In0=)

```
/*eslint no-magic-numbers: ["error", { "ignoreDefaultValues": true }]*/

const { tax = 0.25 } = accountancy;

function mapParallel(concurrency = 3) { /***/ }
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZURlZmF1bHRWYWx1ZXNcIjogdHJ1ZSB9XSovXG5cbmxldCBoZWFkO1xuW2hlYWQgPSAxMDBdID0gW10ifQ==)

```
/*eslint no-magic-numbers: ["error", { "ignoreDefaultValues": true }]*/

let head;
[head = 100] = []
1
2
3
4
```

### ignoreClassFieldInitialValues

A boolean to specify if numbers used as initial values of class fields are considered okay. `false` by default.

Examples of correct code for the `{ "ignoreClassFieldInitialValues": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZUNsYXNzRmllbGRJbml0aWFsVmFsdWVzXCI6IHRydWUgfV0qL1xuXG5jbGFzcyBDIHtcbiAgICBmb28gPSAyO1xuICAgIGJhciA9IC0zO1xuICAgIHR1eCA9ICsxO1xuICAgICNiYXogPSA0O1xuICAgIHN0YXRpYyBxdXggPSA1O1xufSJ9)

```
/*eslint no-magic-numbers: ["error", { "ignoreClassFieldInitialValues": true }]*/

class C {
    foo = 2;
    bar = -3;
    tux = +1;
    #baz = 4;
    static qux = 5;
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
```

Examples of incorrect code for the `{ "ignoreClassFieldInitialValues": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImlnbm9yZUNsYXNzRmllbGRJbml0aWFsVmFsdWVzXCI6IHRydWUgfV0qL1xuXG5jbGFzcyBDIHtcbiAgICBmb28gPSAyICsgMztcbn1cblxuY2xhc3MgRCB7XG4gICAgMjtcbn0ifQ==)

```
/*eslint no-magic-numbers: ["error", { "ignoreClassFieldInitialValues": true }]*/

class C {
    foo = 2 + 3;
}

class D {
    2;
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
```

### enforceConst

A boolean to specify if we should check for the const keyword in variable declaration of numbers. `false` by default.

Examples of incorrect code for the `{ "enforceConst": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImVuZm9yY2VDb25zdFwiOiB0cnVlIH1dKi9cblxubGV0IFRBWCA9IDAuMjU7XG5cbmxldCBkdXR5RnJlZVByaWNlID0gMTAwLFxuICAgIGZpbmFsUHJpY2UgPSBkdXR5RnJlZVByaWNlICsgKGR1dHlGcmVlUHJpY2UgKiBUQVgpOyJ9)

```
/*eslint no-magic-numbers: ["error", { "enforceConst": true }]*/

let TAX = 0.25;

let dutyFreePrice = 100,
    finalPrice = dutyFreePrice + (dutyFreePrice * TAX);
1
2
3
4
5
6
```

### detectObjects

A boolean to specify if we should detect numbers when setting object properties for example. `false` by default.

Examples of incorrect code for the `{ "detectObjects": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImRldGVjdE9iamVjdHNcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IG1hZ2ljID0ge1xuICB0YXg6IDAuMjVcbn07XG5cbmNvbnN0IGR1dHlGcmVlUHJpY2UgPSAxMDAsXG4gICAgZmluYWxQcmljZSA9IGR1dHlGcmVlUHJpY2UgKyAoZHV0eUZyZWVQcmljZSAqIG1hZ2ljLnRheCk7In0=)

```
/*eslint no-magic-numbers: ["error", { "detectObjects": true }]*/

const magic = {
  tax: 0.25
};

const dutyFreePrice = 100,
    finalPrice = dutyFreePrice + (dutyFreePrice * magic.tax);
1
2
3
4
5
6
7
8
```

Examples of correct code for the `{ "detectObjects": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbWFnaWMtbnVtYmVyczogW1wiZXJyb3JcIiwgeyBcImRldGVjdE9iamVjdHNcIjogdHJ1ZSB9XSovXG5cbmNvbnN0IFRBWCA9IDAuMjU7XG5cbmNvbnN0IG1hZ2ljID0ge1xuICB0YXg6IFRBWFxufTtcblxuY29uc3QgZHV0eUZyZWVQcmljZSA9IDEwMCxcbiAgICBmaW5hbFByaWNlID0gZHV0eUZyZWVQcmljZSArIChkdXR5RnJlZVByaWNlICogbWFnaWMudGF4KTsifQ==)

```
/*eslint no-magic-numbers: ["error", { "detectObjects": true }]*/

const TAX = 0.25;

const magic = {
  tax: TAX
};

const dutyFreePrice = 100,
    finalPrice = dutyFreePrice + (dutyFreePrice * magic.tax);
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

### ignoreEnums (TypeScript only)

Whether enums used in TypeScript are considered okay. `false` by default.

Examples of incorrect code for the `{ "ignoreEnums": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlRW51bXNcIjogZmFsc2UgfV0qL1xuXG5lbnVtIGZvbyB7XG4gIFNFQ09ORCA9IDEwMDAsXG59In0=)

```
/*eslint no-magic-numbers: ["error", { "ignoreEnums": false }]*/

enum foo {
  SECOND = 1000,
}
1
2
3
4
5
```

Examples of correct code for the `{ "ignoreEnums": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlRW51bXNcIjogdHJ1ZSB9XSovXG5cbmVudW0gZm9vIHtcbiAgU0VDT05EID0gMTAwMCxcbn0ifQ==)

```
/*eslint no-magic-numbers: ["error", { "ignoreEnums": true }]*/

enum foo {
  SECOND = 1000,
}
1
2
3
4
5
```

### ignoreNumericLiteralTypes (TypeScript only)

Whether numbers used in TypeScript numeric literal types are considered okay. `false` by default.

Examples of incorrect code for the `{ "ignoreNumericLiteralTypes": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTnVtZXJpY0xpdGVyYWxUeXBlc1wiOiBmYWxzZSB9XSovXG5cbnR5cGUgRm9vID0gMSB8IDIgfCAzOyJ9)

```
/*eslint no-magic-numbers: ["error", { "ignoreNumericLiteralTypes": false }]*/

type Foo = 1 | 2 | 3;
1
2
3
```

Examples of correct code for the `{ "ignoreNumericLiteralTypes": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlTnVtZXJpY0xpdGVyYWxUeXBlc1wiOiB0cnVlIH1dKi9cblxudHlwZSBGb28gPSAxIHwgMiB8IDM7In0=)

```
/*eslint no-magic-numbers: ["error", { "ignoreNumericLiteralTypes": true }]*/

type Foo = 1 | 2 | 3;
1
2
3
```

### ignoreReadonlyClassProperties (TypeScript only)

Whether numbers used in TypeScript readonly class properties are considered okay. `false` by default.

Examples of incorrect code for the `{ "ignoreReadonlyClassProperties": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlUmVhZG9ubHlDbGFzc1Byb3BlcnRpZXNcIjogZmFsc2UgfV0qL1xuXG5jbGFzcyBGb28ge1xuICByZWFkb25seSBBID0gMTtcbiAgcmVhZG9ubHkgQiA9IDI7XG4gIHB1YmxpYyBzdGF0aWMgcmVhZG9ubHkgQyA9IDE7XG4gIHN0YXRpYyByZWFkb25seSBEID0gMTtcbn0ifQ==)

```
/*eslint no-magic-numbers: ["error", { "ignoreReadonlyClassProperties": false }]*/

class Foo {
  readonly A = 1;
  readonly B = 2;
  public static readonly C = 1;
  static readonly D = 1;
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

Examples of correct code for the `{ "ignoreReadonlyClassProperties": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlUmVhZG9ubHlDbGFzc1Byb3BlcnRpZXNcIjogdHJ1ZSB9XSovXG5cbmNsYXNzIEZvbyB7XG4gIHJlYWRvbmx5IEEgPSAxO1xuICByZWFkb25seSBCID0gMjtcbiAgcHVibGljIHN0YXRpYyByZWFkb25seSBDID0gMTtcbiAgc3RhdGljIHJlYWRvbmx5IEQgPSAxO1xufSJ9)

```
/*eslint no-magic-numbers: ["error", { "ignoreReadonlyClassProperties": true }]*/

class Foo {
  readonly A = 1;
  readonly B = 2;
  public static readonly C = 1;
  static readonly D = 1;
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

### ignoreTypeIndexes (TypeScript only)

Whether numbers used to index types are okay. `false` by default.

Examples of incorrect code for the `{ "ignoreTypeIndexes": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlVHlwZUluZGV4ZXNcIjogZmFsc2UgfV0qL1xuXG50eXBlIEZvbyA9IEJhclswXTtcbnR5cGUgQmF6ID0gUGFyYW1ldGVyczxGb28+WzJdOyJ9)

```
/*eslint no-magic-numbers: ["error", { "ignoreTypeIndexes": false }]*/

type Foo = Bar[0];
type Baz = Parameters<Foo>[2];
1
2
3
4
```

Examples of correct code for the `{ "ignoreTypeIndexes": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1tYWdpYy1udW1iZXJzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlVHlwZUluZGV4ZXNcIjogdHJ1ZSB9XSovXG5cbnR5cGUgRm9vID0gQmFyWzBdO1xudHlwZSBCYXogPSBQYXJhbWV0ZXJzPEZvbz5bMl07In0=)

```
/*eslint no-magic-numbers: ["error", { "ignoreTypeIndexes": true }]*/

type Foo = Bar[0];
type Baz = Parameters<Foo>[2];
1
2
3
4
```

## Version

This rule was introduced in ESLint v1.7.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-magic-numbers.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-magic-numbers.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-magic-numbers.md
                    
                
                )
