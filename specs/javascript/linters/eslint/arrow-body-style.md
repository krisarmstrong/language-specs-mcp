# arrow-body-style

Require braces around arrow function bodies

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [as-needed](#as-needed)

    1. [requireReturnForObjectLiteral](#requirereturnforobjectliteral)

  3. [never](#never)

3. [Version](#version)
4. [Resources](#resources)

Arrow functions have two syntactic forms for their function bodies. They may be defined with a block body (denoted by curly braces) `() => { ... }` or with a single expression `() => ...`, whose value is implicitly returned.

## Rule Details

This rule can enforce or disallow the use of braces around arrow function body.

## Options

The rule takes one or two options. The first is a string, which can be:

- `"always"` enforces braces around the function body
- `"as-needed"` enforces no braces where they can be omitted (default)
- `"never"` enforces no braces around the function body (constrains arrow functions to the role of returning an expression)

The second one is an object for more fine-grained configuration when the first option is `"as-needed"`. Currently, the only available option is `requireReturnForObjectLiteral`, a boolean property. It’s `false` by default. If set to `true`, it requires braces and an explicit return for object literals.

```
"arrow-body-style": ["error", "always"]
1
```

Copy code to clipboard

### always

Examples of incorrect code for this rule with the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5jb25zdCBmb28gPSAoKSA9PiAwOyJ9)

```
/*eslint arrow-body-style: ["error", "always"]*/

const foo = () => 0;
1
2
3
```

Examples of correct code for this rule with the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJhbHdheXNcIl0qL1xuXG5jb25zdCBmb28gPSAoKSA9PiB7XG4gICAgcmV0dXJuIDA7XG59O1xuXG5jb25zdCBiYXIgPSAocmV0diwgbmFtZSkgPT4ge1xuICAgIHJldHZbbmFtZV0gPSB0cnVlO1xuICAgIHJldHVybiByZXR2O1xufTsifQ==)

```
/*eslint arrow-body-style: ["error", "always"]*/

const foo = () => {
    return 0;
};

const bar = (retv, name) => {
    retv[name] = true;
    return retv;
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
10
```

### as-needed

Examples of incorrect code for this rule with the default `"as-needed"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIl0qL1xuXG5jb25zdCBmb28gPSAoKSA9PiB7XG4gICAgcmV0dXJuIDA7XG59O1xuXG5jb25zdCBiYXIgPSAoKSA9PiB7XG4gICAgcmV0dXJuIHtcbiAgICAgICBiYXI6IHtcbiAgICAgICAgICAgIGZvbzogMSxcbiAgICAgICAgICAgIGJhcjogMixcbiAgICAgICAgfVxuICAgIH07XG59OyJ9)

```
/*eslint arrow-body-style: ["error", "as-needed"]*/

const foo = () => {
    return 0;
};

const bar = () => {
    return {
       bar: {
            foo: 1,
            bar: 2,
        }
    };
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
10
11
12
13
14
```

Examples of correct code for this rule with the default `"as-needed"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIl0qL1xuXG5jb25zdCBmb28xID0gKCkgPT4gMDtcblxuY29uc3QgZm9vMiA9IChyZXR2LCBuYW1lKSA9PiB7XG4gICAgcmV0dltuYW1lXSA9IHRydWU7XG4gICAgcmV0dXJuIHJldHY7XG59O1xuXG5jb25zdCBmb28zID0gKCkgPT4gKHtcbiAgICBiYXI6IHtcbiAgICAgICAgZm9vOiAxLFxuICAgICAgICBiYXI6IDIsXG4gICAgfVxufSk7XG5cbmNvbnN0IGZvbzQgPSAoKSA9PiB7IGJhcigpOyB9O1xuY29uc3QgZm9vNSA9ICgpID0+IHt9O1xuY29uc3QgZm9vNiA9ICgpID0+IHsgLyogZG8gbm90aGluZyAqLyB9O1xuXG5jb25zdCBmb283ID0gKCkgPT4ge1xuICAgIC8vIGRvIG5vdGhpbmcuXG59O1xuXG5jb25zdCBmb284ID0gKCkgPT4gKHsgYmFyOiAwIH0pOyJ9)

```
/*eslint arrow-body-style: ["error", "as-needed"]*/

const foo1 = () => 0;

const foo2 = (retv, name) => {
    retv[name] = true;
    return retv;
};

const foo3 = () => ({
    bar: {
        foo: 1,
        bar: 2,
    }
});

const foo4 = () => { bar(); };
const foo5 = () => {};
const foo6 = () => { /* do nothing */ };

const foo7 = () => {
    // do nothing.
};

const foo8 = () => ({ bar: 0 });
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
```

#### requireReturnForObjectLiteral

This option is only applicable when used in conjunction with the `"as-needed"` option.

Examples of incorrect code for this rule with the `{ "requireReturnForObjectLiteral": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIiwgeyBcInJlcXVpcmVSZXR1cm5Gb3JPYmplY3RMaXRlcmFsXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmb28gPSAoKSA9PiAoe30pO1xuXG5jb25zdCBiYXIgPSAoKSA9PiAoeyBiYXI6IDAgfSk7In0=)

```
/*eslint arrow-body-style: ["error", "as-needed", { "requireReturnForObjectLiteral": true }]*/

const foo = () => ({});

const bar = () => ({ bar: 0 });
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "requireReturnForObjectLiteral": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJhcy1uZWVkZWRcIiwgeyBcInJlcXVpcmVSZXR1cm5Gb3JPYmplY3RMaXRlcmFsXCI6IHRydWUgfV0qL1xuXG5jb25zdCBmb28gPSAoKSA9PiB7fTtcblxuY29uc3QgYmFyID0gKCkgPT4geyByZXR1cm4geyBiYXI6IDAgfTsgfTsifQ==)

```
/*eslint arrow-body-style: ["error", "as-needed", { "requireReturnForObjectLiteral": true }]*/

const foo = () => {};

const bar = () => { return { bar: 0 }; };
1
2
3
4
5
```

### never

Examples of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbmNvbnN0IGZvbyA9ICgpID0+IHtcbiAgICByZXR1cm4gMDtcbn07XG5cbmNvbnN0IGJhciA9IChyZXR2LCBuYW1lKSA9PiB7XG4gICAgcmV0dltuYW1lXSA9IHRydWU7XG4gICAgcmV0dXJuIHJldHY7XG59OyJ9)

```
/*eslint arrow-body-style: ["error", "never"]*/

const foo = () => {
    return 0;
};

const bar = (retv, name) => {
    retv[name] = true;
    return retv;
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
10
```

Examples of correct code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYXJyb3ctYm9keS1zdHlsZTogW1wiZXJyb3JcIiwgXCJuZXZlclwiXSovXG5cbmNvbnN0IGZvbyA9ICgpID0+IDA7XG5cbmNvbnN0IGJhciA9ICgpID0+ICh7IGZvbzogMCB9KTsifQ==)

```
/*eslint arrow-body-style: ["error", "never"]*/

const foo = () => 0;

const bar = () => ({ foo: 0 });
1
2
3
4
5
```

## Version

This rule was introduced in ESLint v1.8.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/arrow-body-style.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/arrow-body-style.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/arrow-body-style.md
                    
                
                )
