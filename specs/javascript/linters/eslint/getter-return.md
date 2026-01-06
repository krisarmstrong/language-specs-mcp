# getter-return

Enforce `return` statements in getters

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Handled by TypeScript](#handled_by_typescript)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

The get syntax binds an object property to a function that will be called when that property is looked up. It was first introduced in ECMAScript 5:

```
const p = {
    get name(){
        return "nicholas";
    }
};

Object.defineProperty(p, "age", {
    get: function (){
        return 17;
    }
});
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

Copy code to clipboard

Note that every `getter` is expected to return a value.

## Rule Details

This rule enforces that a return statement is present in property getters.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ2V0dGVyLXJldHVybjogXCJlcnJvclwiKi9cblxuY29uc3QgcCA9IHtcbiAgICBnZXQgbmFtZSgpe1xuICAgICAgICAvLyBubyByZXR1cm5zLlxuICAgIH1cbn07XG5cbk9iamVjdC5kZWZpbmVQcm9wZXJ0eShwLCBcImFnZVwiLCB7XG4gICAgZ2V0OiBmdW5jdGlvbiAoKXtcbiAgICAgICAgLy8gbm8gcmV0dXJucy5cbiAgICB9XG59KTtcblxuY2xhc3MgUHtcbiAgICBnZXQgbmFtZSgpe1xuICAgICAgICAvLyBubyByZXR1cm5zLlxuICAgIH1cbn0ifQ==)

```
/*eslint getter-return: "error"*/

const p = {
    get name(){
        // no returns.
    }
};

Object.defineProperty(p, "age", {
    get: function (){
        // no returns.
    }
});

class P{
    get name(){
        // no returns.
    }
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ2V0dGVyLXJldHVybjogXCJlcnJvclwiKi9cblxuY29uc3QgcCA9IHtcbiAgICBnZXQgbmFtZSgpe1xuICAgICAgICByZXR1cm4gXCJuaWNob2xhc1wiO1xuICAgIH1cbn07XG5cbk9iamVjdC5kZWZpbmVQcm9wZXJ0eShwLCBcImFnZVwiLCB7XG4gICAgZ2V0OiBmdW5jdGlvbiAoKXtcbiAgICAgICAgcmV0dXJuIDE4O1xuICAgIH1cbn0pO1xuXG5jbGFzcyBQe1xuICAgIGdldCBuYW1lKCl7XG4gICAgICAgIHJldHVybiBcIm5pY2hvbGFzXCI7XG4gICAgfVxufSJ9)

```
/*eslint getter-return: "error"*/

const p = {
    get name(){
        return "nicholas";
    }
};

Object.defineProperty(p, "age", {
    get: function (){
        return 18;
    }
});

class P{
    get name(){
        return "nicholas";
    }
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
```

## Options

This rule has an object option:

- `"allowImplicit": false` (default) disallows implicitly returning `undefined` with a `return` statement.

Examples of correct code for the `{ "allowImplicit": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ2V0dGVyLXJldHVybjogW1wiZXJyb3JcIiwgeyBhbGxvd0ltcGxpY2l0OiB0cnVlIH1dKi9cbmNvbnN0IHAgPSB7XG4gICAgZ2V0IG5hbWUoKXtcbiAgICAgICAgcmV0dXJuOyAvLyByZXR1cm4gdW5kZWZpbmVkIGltcGxpY2l0bHkuXG4gICAgfVxufTsifQ==)

```
/*eslint getter-return: ["error", { allowImplicit: true }]*/
const p = {
    get name(){
        return; // return undefined implicitly.
    }
};
1
2
3
4
5
6
```

## When Not To Use It

If your project will not be using ES5 property getters you do not need this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v4.2.0.

## Further Reading

[getter - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 developer.mozilla.org[Read Understanding ECMAScript 6 | Leanpub](https://leanpub.com/understandinges6/read/#leanpub-auto-accessor-properties)
 leanpub.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/getter-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/getter-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/getter-return.md
                    
                
                )
