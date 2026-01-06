# prefer-object-spread

Disallow using `Object.assign` with an object literal as the first argument and prefer the use of object spread instead

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Resources](#resources)

When `Object.assign` is called using an object literal as the first argument, this rule requires using the object spread syntax instead. This rule also warns on cases where an `Object.assign` call is made using a single argument that is an object literal, in this case, the `Object.assign` call is not needed.

Introduced in ES2018, object spread is a declarative alternative which may perform better than the more dynamic, imperative `Object.assign`.

## Rule Details

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW9iamVjdC1zcHJlYWQ6IFwiZXJyb3JcIiovXG5cbk9iamVjdC5hc3NpZ24oe30sIGZvbyk7XG5cbk9iamVjdC5hc3NpZ24oe30sIHtmb286ICdiYXInfSk7XG5cbk9iamVjdC5hc3NpZ24oeyBmb286ICdiYXInfSwgYmF6KTtcblxuT2JqZWN0LmFzc2lnbih7fSwgYmF6LCB7IGZvbzogJ2JhcicgfSk7XG5cbk9iamVjdC5hc3NpZ24oe30sIHsgLi4uYmF6IH0pO1xuXG4vLyBPYmplY3QuYXNzaWduIHdpdGggYSBzaW5nbGUgYXJndW1lbnQgdGhhdCBpcyBhbiBvYmplY3QgbGl0ZXJhbFxuT2JqZWN0LmFzc2lnbih7fSk7XG5cbk9iamVjdC5hc3NpZ24oeyBmb286IGJhciB9KTsifQ==)

```
/*eslint prefer-object-spread: "error"*/

Object.assign({}, foo);

Object.assign({}, {foo: 'bar'});

Object.assign({ foo: 'bar'}, baz);

Object.assign({}, baz, { foo: 'bar' });

Object.assign({}, { ...baz });

// Object.assign with a single argument that is an object literal
Object.assign({});

Object.assign({ foo: bar });
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgcHJlZmVyLW9iamVjdC1zcHJlYWQ6IFwiZXJyb3JcIiovXG5cbih7IC4uLmZvbyB9KTtcblxuKHsgLi4uYmF6LCBmb286ICdiYXInIH0pO1xuXG4vLyBBbnkgT2JqZWN0LmFzc2lnbiBjYWxsIHdpdGhvdXQgYW4gb2JqZWN0IGxpdGVyYWwgYXMgdGhlIGZpcnN0IGFyZ3VtZW50XG5PYmplY3QuYXNzaWduKGZvbywgeyBiYXI6IGJheiB9KTtcblxuT2JqZWN0LmFzc2lnbihmb28sIGJhcik7XG5cbk9iamVjdC5hc3NpZ24oZm9vLCB7IGJhciwgYmF6IH0pO1xuXG5PYmplY3QuYXNzaWduKGZvbywgeyAuLi5iYXogfSk7In0=)

```
/*eslint prefer-object-spread: "error"*/

({ ...foo });

({ ...baz, foo: 'bar' });

// Any Object.assign call without an object literal as the first argument
Object.assign(foo, { bar: baz });

Object.assign(foo, bar);

Object.assign(foo, { bar, baz });

Object.assign(foo, { ...baz });
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

## When Not To Use It

This rule should not be used unless ES2018 is supported in your codebase.

## Version

This rule was introduced in ESLint v5.0.0-alpha.3.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/prefer-object-spread.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/prefer-object-spread.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/prefer-object-spread.md
                    
                
                )
