# max-params

Enforce a maximum number of parameters in function definitions

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [max](#max)
  2. [countVoidThis (TypeScript only)](#countvoidthis-typescript-only)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Functions that take numerous parameters can be difficult to read and write because it requires the memorization of what each parameter is, its type, and the order they should appear in. As a result, many coders adhere to a convention that caps the number of parameters a function can take.

```
function foo (bar, baz, qux, qxx) { // four parameters, may be too many
    doSomething();
}
1
2
3
```

Copy code to clipboard

## Rule Details

This rule enforces a maximum number of parameters allowed in function definitions.

## Options

This rule has a number or object option:

- `"max"` (default `3`) enforces a maximum number of parameters in function definitions
- `"countVoidThis"` (default `false`) counts a `this` declaration when the type is `void` (TypeScript only)

Deprecated: The object property `maximum` is deprecated; please use the object property `max` instead.

### max

Examples of incorrect code for this rule with the default `{ "max": 3 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LXBhcmFtczogW1wiZXJyb3JcIiwgM10qL1xuXG5mdW5jdGlvbiBmb28xIChiYXIsIGJheiwgcXV4LCBxeHgpIHtcbiAgICBkb1NvbWV0aGluZygpO1xufVxuXG5sZXQgZm9vMiA9IChiYXIsIGJheiwgcXV4LCBxeHgpID0+IHtcbiAgICBkb1NvbWV0aGluZygpO1xufTsifQ==)

```
/*eslint max-params: ["error", 3]*/

function foo1 (bar, baz, qux, qxx) {
    doSomething();
}

let foo2 = (bar, baz, qux, qxx) => {
    doSomething();
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

Examples of correct code for this rule with the default `{ "max": 3 }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LXBhcmFtczogW1wiZXJyb3JcIiwgM10qL1xuXG5mdW5jdGlvbiBmb28xIChiYXIsIGJheiwgcXV4KSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn1cblxubGV0IGZvbzIgPSAoYmFyLCBiYXosIHF1eCkgPT4ge1xuICAgIGRvU29tZXRoaW5nKCk7XG59OyJ9)

```
/*eslint max-params: ["error", 3]*/

function foo1 (bar, baz, qux) {
    doSomething();
}

let foo2 = (bar, baz, qux) => {
    doSomething();
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

### countVoidThis (TypeScript only)

This rule has a TypeScript-specific option `countVoidThis` that allows you to count a `this` declaration when the type is `void`.

Examples of correct TypeScript code for this rule with the default `{ "countVoidThis": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBtYXgtcGFyYW1zOiBbXCJlcnJvclwiLCB7IFwibWF4XCI6IDIsIFwiY291bnRWb2lkVGhpc1wiOiBmYWxzZSB9XSovXG5cbmZ1bmN0aW9uIGhhc05vVGhpcyh0aGlzOiB2b2lkLCBmaXJzdDogc3RyaW5nLCBzZWNvbmQ6IHN0cmluZykge1xuXHQvLyAuLi5cbn0ifQ==)

```
/*eslint max-params: ["error", { "max": 2, "countVoidThis": false }]*/

function hasNoThis(this: void, first: string, second: string) {
	// ...
}
1
2
3
4
5
```

Examples of incorrect TypeScript code for this rule with the default `{ "countVoidThis": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBtYXgtcGFyYW1zOiBbXCJlcnJvclwiLCB7IFwibWF4XCI6IDIsIFwiY291bnRWb2lkVGhpc1wiOiBmYWxzZSB9XSovXG5cbmZ1bmN0aW9uIGhhc05vVGhpcyh0aGlzOiB2b2lkLCBmaXJzdDogc3RyaW5nLCBzZWNvbmQ6IHN0cmluZywgdGhpcmQ6IHN0cmluZykge1xuXHQvLyAuLi5cbn0ifQ==)

```
/*eslint max-params: ["error", { "max": 2, "countVoidThis": false }]*/

function hasNoThis(this: void, first: string, second: string, third: string) {
	// ...
}
1
2
3
4
5
```

Examples of correct TypeScript code for this rule with the `{ "countVoidThis": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBtYXgtcGFyYW1zOiBbXCJlcnJvclwiLCB7IFwibWF4XCI6IDIsIFwiY291bnRWb2lkVGhpc1wiOiB0cnVlIH1dKi9cblxuZnVuY3Rpb24gaGFzTm9UaGlzKHRoaXM6IHZvaWQsIGZpcnN0OiBzdHJpbmcpIHtcblx0Ly8gLi4uXG59In0=)

```
/*eslint max-params: ["error", { "max": 2, "countVoidThis": true }]*/

function hasNoThis(this: void, first: string) {
	// ...
}
1
2
3
4
5
```

Examples of incorrect TypeScript code for this rule with the `{ "countVoidThis": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBtYXgtcGFyYW1zOiBbXCJlcnJvclwiLCB7IFwibWF4XCI6IDIsIFwiY291bnRWb2lkVGhpc1wiOiB0cnVlIH1dKi9cblxuZnVuY3Rpb24gaGFzTm9UaGlzKHRoaXM6IHZvaWQsIGZpcnN0OiBzdHJpbmcsIHNlY29uZDogc3RyaW5nKSB7XG5cdC8vIC4uLlxufSJ9)

```
/*eslint max-params: ["error", { "max": 2, "countVoidThis": true }]*/

function hasNoThis(this: void, first: string, second: string) {
	// ...
}
1
2
3
4
5
```

## Related Rules

- [complexity](/docs/latest/rules/complexity)
- [max-depth](/docs/latest/rules/max-depth)
- [max-len](/docs/latest/rules/max-len)
- [max-lines](/docs/latest/rules/max-lines)
- [max-lines-per-function](/docs/latest/rules/max-lines-per-function)
- [max-nested-callbacks](/docs/latest/rules/max-nested-callbacks)
- [max-statements](/docs/latest/rules/max-statements)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-params.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-params.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-params.md
                    
                
                )
