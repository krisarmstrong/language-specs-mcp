# no-useless-computed-key

Disallow unnecessary computed property keys in objects and classes

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [enforceForClassMembers](#enforceforclassmembers)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

It’s unnecessary to use computed properties with literals such as:

```
const foo = {["a"]: "b"};
1
```

Copy code to clipboard

The code can be rewritten as:

```
const foo = {"a": "b"};
1
```

Copy code to clipboard

## Rule Details

This rule disallows unnecessary usage of computed property keys.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb21wdXRlZC1rZXk6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSB7IFsnMCddOiAwIH07XG5jb25zdCBiID0geyBbJzArMSwyMzQnXTogMCB9O1xuY29uc3QgYyA9IHsgWzBdOiAwIH07XG5jb25zdCBkID0geyBbJ3gnXTogMCB9O1xuY29uc3QgZSA9IHsgWyd4J10oKSB7fSB9O1xuXG5jb25zdCB7IFswXTogZm9vIH0gPSBvYmo7XG5jb25zdCB7IFsneCddOiBiYXIgfSA9IG9iajtcblxuY2xhc3MgRm9vIHtcbiAgICBbXCJmb29cIl0gPSBcImJhclwiO1xuXG4gICAgWzBdKCkge31cbiAgICBbJ2EnXSgpIHt9XG4gICAgZ2V0IFsnYiddKCkge31cbiAgICBzZXQgWydjJ10odmFsdWUpIHt9XG5cbiAgICBzdGF0aWMgW1wiZm9vXCJdID0gXCJiYXJcIjtcblxuICAgIHN0YXRpYyBbJ2EnXSgpIHt9XG59In0=)

```
/*eslint no-useless-computed-key: "error"*/

const a = { ['0']: 0 };
const b = { ['0+1,234']: 0 };
const c = { [0]: 0 };
const d = { ['x']: 0 };
const e = { ['x']() {} };

const { [0]: foo } = obj;
const { ['x']: bar } = obj;

class Foo {
    ["foo"] = "bar";

    [0]() {}
    ['a']() {}
    get ['b']() {}
    set ['c'](value) {}

    static ["foo"] = "bar";

    static ['a']() {}
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
20
21
22
23
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb21wdXRlZC1rZXk6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGEgPSB7ICdhJzogMCB9O1xuY29uc3QgYiA9IHsgMDogMCB9O1xuY29uc3QgYyA9IHsgeCgpIHt9IH07XG5jb25zdCBkID0geyBhOiAwIH07XG5jb25zdCBlID0geyAnMCsxLDIzNCc6IDAgfTtcblxuY29uc3QgeyAwOiBmb28gfSA9IG9iajtcbmNvbnN0IHsgJ3gnOiBiYXIgfSA9IG9iajtcblxuY2xhc3MgRm9vIHtcbiAgICBcImZvb1wiID0gXCJiYXJcIjtcblxuICAgIDAoKSB7fVxuICAgICdhJygpIHt9XG4gICAgZ2V0ICdiJygpIHt9XG4gICAgc2V0ICdjJyh2YWx1ZSkge31cblxuICAgIHN0YXRpYyBcImZvb1wiID0gXCJiYXJcIjtcblxuICAgIHN0YXRpYyAnYScoKSB7fVxufSJ9)

```
/*eslint no-useless-computed-key: "error"*/

const a = { 'a': 0 };
const b = { 0: 0 };
const c = { x() {} };
const d = { a: 0 };
const e = { '0+1,234': 0 };

const { 0: foo } = obj;
const { 'x': bar } = obj;

class Foo {
    "foo" = "bar";

    0() {}
    'a'() {}
    get 'b'() {}
    set 'c'(value) {}

    static "foo" = "bar";

    static 'a'() {}
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
20
21
22
23
```

Examples of additional correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb21wdXRlZC1rZXk6IFwiZXJyb3JcIiovXG5cbmNvbnN0IGMgPSB7XG4gICAgXCJfX3Byb3RvX19cIjogZm9vLCAvLyBkZWZpbmVzIG9iamVjdCdzIHByb3RvdHlwZVxuXG4gICAgW1wiX19wcm90b19fXCJdOiBiYXIgLy8gZGVmaW5lcyBhIHByb3BlcnR5IG5hbWVkIFwiX19wcm90b19fXCJcbn07XG5cbmNsYXNzIEZvbyB7XG4gICAgW1wiY29uc3RydWN0b3JcIl07IC8vIGluc3RhbmNlIGZpZWxkIG5hbWVkIFwiY29uc3RydWN0b3JcIlxuXG4gICAgXCJjb25zdHJ1Y3RvclwiKCkge30gLy8gdGhlIGNvbnN0cnVjdG9yIG9mIHRoaXMgY2xhc3NcblxuICAgIFtcImNvbnN0cnVjdG9yXCJdKCkge30gLy8gbWV0aG9kIG5hbWVkIFwiY29uc3RydWN0b3JcIlxuXG4gICAgc3RhdGljIFtcImNvbnN0cnVjdG9yXCJdOyAvLyBzdGF0aWMgZmllbGQgbmFtZWQgXCJjb25zdHJ1Y3RvclwiXG5cbiAgICBzdGF0aWMgW1wicHJvdG90eXBlXCJdOyAvLyBydW50aW1lIGVycm9yLCBpdCB3b3VsZCBiZSBhIHBhcnNpbmcgZXJyb3Igd2l0aG91dCBgW11gXG59In0=)

```
/*eslint no-useless-computed-key: "error"*/

const c = {
    "__proto__": foo, // defines object's prototype

    ["__proto__"]: bar // defines a property named "__proto__"
};

class Foo {
    ["constructor"]; // instance field named "constructor"

    "constructor"() {} // the constructor of this class

    ["constructor"]() {} // method named "constructor"

    static ["constructor"]; // static field named "constructor"

    static ["prototype"]; // runtime error, it would be a parsing error without `[]`
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

- `enforceForClassMembers` set to `false` disables this rule for class members (Default `true`).

### enforceForClassMembers

By default, this rule also checks class declarations and class expressions, as the default value for `enforceForClassMembers` is `true`.

When `enforceForClassMembers` is set to `false`, the rule will allow unnecessary computed keys inside of class fields, class methods, class getters, and class setters.

Examples of incorrect code for this rule with the `{ "enforceForClassMembers": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb21wdXRlZC1rZXk6IFtcImVycm9yXCIsIHsgXCJlbmZvcmNlRm9yQ2xhc3NNZW1iZXJzXCI6IGZhbHNlIH1dKi9cblxuY29uc3Qgb2JqID0ge1xuICAgIFtcImZvb1wiXTogXCJiYXJcIixcbiAgICBbNDJdOiBcImJhelwiLFxuXG4gICAgWydhJ10oKSB7fSxcbiAgICBnZXQgWydiJ10oKSB7fSxcbiAgICBzZXQgWydjJ10odmFsdWUpIHt9XG59OyJ9)

```
/*eslint no-useless-computed-key: ["error", { "enforceForClassMembers": false }]*/

const obj = {
    ["foo"]: "bar",
    [42]: "baz",

    ['a']() {},
    get ['b']() {},
    set ['c'](value) {}
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

Examples of correct code for this rule with the `{ "enforceForClassMembers": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1jb21wdXRlZC1rZXk6IFtcImVycm9yXCIsIHsgXCJlbmZvcmNlRm9yQ2xhc3NNZW1iZXJzXCI6IGZhbHNlIH1dKi9cblxuY2xhc3MgU29tZUNsYXNzIHtcbiAgICBbXCJmb29cIl0gPSBcImJhclwiO1xuICAgIFs0Ml0gPSBcImJhelwiO1xuXG4gICAgWydhJ10oKSB7fVxuICAgIGdldCBbJ2InXSgpIHt9XG4gICAgc2V0IFsnYyddKHZhbHVlKSB7fVxuXG4gICAgc3RhdGljIFtcImZvb1wiXSA9IFwiYmFyXCI7XG4gICAgc3RhdGljIFsnYmF6J10oKSB7fVxufSJ9)

```
/*eslint no-useless-computed-key: ["error", { "enforceForClassMembers": false }]*/

class SomeClass {
    ["foo"] = "bar";
    [42] = "baz";

    ['a']() {}
    get ['b']() {}
    set ['c'](value) {}

    static ["foo"] = "bar";
    static ['baz']() {}
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
```

## When Not To Use It

If you don’t want to be notified about unnecessary computed property keys, you can safely disable this rule.

## Version

This rule was introduced in ESLint v2.9.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-computed-key.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-computed-key.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-computed-key.md
                    
                
                )
