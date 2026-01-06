# no-unsafe-negation

Disallow negating the left operand of relational operators

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Exception](#exception)

2. [Options](#options)

  1. [enforceForOrderingRelations](#enforcefororderingrelations)

3. [When Not To Use It](#when-not-to-use-it)
4. [Handled by TypeScript](#handled_by_typescript)
5. [Version](#version)
6. [Resources](#resources)

Just as developers might type `-a + b` when they mean `-(a + b)` for the negative of a sum, they might type `!key in object` by mistake when they almost certainly mean `!(key in object)` to test that a key is not in an object. `!obj instanceof Ctor` is similar.

## Rule Details

This rule disallows negating the left operand of the following relational operators:

- [in operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in).
- [instanceof operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW5lZ2F0aW9uOiBcImVycm9yXCIqL1xuXG5pZiAoIWtleSBpbiBvYmplY3QpIHtcbiAgICAvLyBvcGVyYXRvciBwcmVjZWRlbmNlIG1ha2VzIGl0IGVxdWl2YWxlbnQgdG8gKCFrZXkpIGluIG9iamVjdFxuICAgIC8vIGFuZCB0eXBlIGNvbnZlcnNpb24gbWFrZXMgaXQgZXF1aXZhbGVudCB0byAoa2V5ID8gXCJmYWxzZVwiIDogXCJ0cnVlXCIpIGluIG9iamVjdFxufVxuXG5pZiAoIW9iaiBpbnN0YW5jZW9mIEN0b3IpIHtcbiAgICAvLyBvcGVyYXRvciBwcmVjZWRlbmNlIG1ha2VzIGl0IGVxdWl2YWxlbnQgdG8gKCFvYmopIGluc3RhbmNlb2YgQ3RvclxuICAgIC8vIGFuZCBpdCBlcXVpdmFsZW50IHRvIGFsd2F5cyBmYWxzZSBzaW5jZSBib29sZWFuIHZhbHVlcyBhcmUgbm90IG9iamVjdHMuXG59In0=)

```
/*eslint no-unsafe-negation: "error"*/

if (!key in object) {
    // operator precedence makes it equivalent to (!key) in object
    // and type conversion makes it equivalent to (key ? "false" : "true") in object
}

if (!obj instanceof Ctor) {
    // operator precedence makes it equivalent to (!obj) instanceof Ctor
    // and it equivalent to always false since boolean values are not objects.
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW5lZ2F0aW9uOiBcImVycm9yXCIqL1xuXG5pZiAoIShrZXkgaW4gb2JqZWN0KSkge1xuICAgIC8vIGtleSBpcyBub3QgaW4gb2JqZWN0XG59XG5cbmlmICghKG9iaiBpbnN0YW5jZW9mIEN0b3IpKSB7XG4gICAgLy8gb2JqIGlzIG5vdCBhbiBpbnN0YW5jZSBvZiBDdG9yXG59In0=)

```
/*eslint no-unsafe-negation: "error"*/

if (!(key in object)) {
    // key is not in object
}

if (!(obj instanceof Ctor)) {
    // obj is not an instance of Ctor
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

### Exception

For rare situations when negating the left operand is intended, this rule allows an exception. If the whole negation is explicitly wrapped in parentheses, the rule will not report a problem.

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW5lZ2F0aW9uOiBcImVycm9yXCIqL1xuXG5pZiAoKCFmb28pIGluIG9iamVjdCkge1xuICAgIC8vIGFsbG93ZWQsIGJlY2F1c2UgdGhlIG5lZ2F0aW9uIGlzIGV4cGxpY2l0bHkgd3JhcHBlZCBpbiBwYXJlbnRoZXNlc1xuICAgIC8vIGl0IGlzIGVxdWl2YWxlbnQgdG8gKGZvbyA/IFwiZmFsc2VcIiA6IFwidHJ1ZVwiKSBpbiBvYmplY3RcbiAgICAvLyB0aGlzIGlzIGFsbG93ZWQgYXMgYW4gZXhjZXB0aW9uIGZvciByYXJlIHNpdHVhdGlvbnMgd2hlbiB0aGF0IGlzIHRoZSBpbnRlbmRlZCBtZWFuaW5nXG59XG5cbmlmKChcIlwiICsgIWZvbykgaW4gb2JqZWN0KSB7XG4gICAgLy8geW91IGNhbiBhbHNvIG1ha2UgdGhlIGludGVudGlvbiBtb3JlIGV4cGxpY2l0LCB3aXRoIHR5cGUgY29udmVyc2lvblxufSJ9)

```
/*eslint no-unsafe-negation: "error"*/

if ((!foo) in object) {
    // allowed, because the negation is explicitly wrapped in parentheses
    // it is equivalent to (foo ? "false" : "true") in object
    // this is allowed as an exception for rare situations when that is the intended meaning
}

if(("" + !foo) in object) {
    // you can also make the intention more explicit, with type conversion
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

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW5lZ2F0aW9uOiBcImVycm9yXCIqL1xuXG5pZiAoIShmb28pIGluIG9iamVjdCkge1xuICAgIC8vIHRoaXMgaXMgbm90IGFuIGFsbG93ZWQgZXhjZXB0aW9uXG59In0=)

```
/*eslint no-unsafe-negation: "error"*/

if (!(foo) in object) {
    // this is not an allowed exception
}
1
2
3
4
5
```

## Options

This rule has an object option:

- `"enforceForOrderingRelations": false` (default) allows negation of the left-hand side of ordering relational operators (`<`, `>`, `<=`, `>=`)
- `"enforceForOrderingRelations": true` disallows negation of the left-hand side of ordering relational operators

### enforceForOrderingRelations

With this option set to `true` the rule is additionally enforced for:

- `<` operator.
- `>` operator.
- `<=` operator.
- `>=` operator.

The purpose is to avoid expressions such as `! a < b` (which is equivalent to `(a ? 0 : 1) < b`) when what is really intended is `!(a < b)`.

Examples of additional incorrect code for this rule with the `{ "enforceForOrderingRelations": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW5lZ2F0aW9uOiBbXCJlcnJvclwiLCB7IFwiZW5mb3JjZUZvck9yZGVyaW5nUmVsYXRpb25zXCI6IHRydWUgfV0qL1xuXG5pZiAoISBhIDwgYikge31cblxud2hpbGUgKCEgYSA+IGIpIHt9XG5cbmZvbyA9ICEgYSA8PSBiO1xuXG5mb28gPSAhIGEgPj0gYjsifQ==)

```
/*eslint no-unsafe-negation: ["error", { "enforceForOrderingRelations": true }]*/

if (! a < b) {}

while (! a > b) {}

foo = ! a <= b;

foo = ! a >= b;
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

If you don’t want to notify unsafe logical negations, then it’s safe to disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v3.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unsafe-negation.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unsafe-negation.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unsafe-negation.md
                    
                
                )
