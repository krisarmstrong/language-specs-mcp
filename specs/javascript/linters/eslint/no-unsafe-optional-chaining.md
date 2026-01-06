# no-unsafe-optional-chaining

Disallow use of optional chaining in contexts where the `undefined` value is not allowed

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [disallowArithmeticOperators](#disallowarithmeticoperators)

3. [Version](#version)
4. [Resources](#resources)

The optional chaining (`?.`) expression can short-circuit with a return value of `undefined`. Therefore, treating an evaluated optional chaining expression as a function, object, number, etc., can cause TypeError or unexpected results. For example:

```
const obj = undefined;

1 in obj?.foo;  // TypeError
with (obj?.foo);  // TypeError
for (bar of obj?.foo);  // TypeError
bar instanceof obj?.foo;  // TypeError
const { bar } = obj?.foo;  // TypeError
1
2
3
4
5
6
7
```

Copy code to clipboard

Also, parentheses limit the scope of short-circuiting in chains. For example:

```
const obj = undefined;

(obj?.foo)(); // TypeError
(obj?.foo).bar; // TypeError
1
2
3
4
```

Copy code to clipboard

## Rule Details

This rule aims to detect some cases where the use of optional chaining doesn’t prevent runtime errors. In particular, it flags optional chaining expressions in positions where short-circuiting to `undefined` causes throwing a TypeError afterward.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW9wdGlvbmFsLWNoYWluaW5nOiBcImVycm9yXCIqL1xuXG4ob2JqPy5mb28pKCk7XG5cbihvYmo/LmZvbykuYmFyO1xuXG4oZm9vPy4oKSkuYmFyO1xuXG4oZm9vPy4oKSkuYmFyKCk7XG5cbihvYmo/LmZvbyA/PyBvYmo/LmJhcikoKTtcblxuKGZvbyB8fCBvYmo/LmZvbykoKTtcblxuKG9iaj8uZm9vICYmIGZvbykoKTtcblxuKGZvbyA/IG9iaj8uZm9vIDogYmFyKSgpO1xuXG4oZm9vLCBvYmo/LmJhcikuYmF6O1xuXG4ob2JqPy5mb28pYHRlbXBsYXRlYDtcblxubmV3IChvYmo/LmZvbykoKTtcblxuWy4uLm9iaj8uZm9vXTtcblxuYmFyKC4uLm9iaj8uZm9vKTtcblxuMSBpbiBvYmo/LmZvbztcblxuYmFyIGluc3RhbmNlb2Ygb2JqPy5mb287XG5cbmZvciAoYmFyIG9mIG9iaj8uZm9vKTtcblxuY29uc3QgeyBiYXIgfSA9IG9iaj8uZm9vO1xuXG5beyBiYXIgfSA9IG9iaj8uZm9vXSA9IFtdO1xuXG53aXRoIChvYmo/LmZvbyk7XG5cbmNsYXNzIEEgZXh0ZW5kcyBvYmo/LmZvbyB7fVxuXG5jb25zdCBhID0gY2xhc3MgQSBleHRlbmRzIG9iaj8uZm9vIHt9O1xuXG5hc3luYyBmdW5jdGlvbiBmb28gKCkge1xuICAgIGNvbnN0IHsgYmFyIH0gPSBhd2FpdCBvYmo/LmZvbztcbiAgIChhd2FpdCBvYmo/LmZvbykoKTtcbiAgIChhd2FpdCBvYmo/LmZvbykuYmFyO1xufSJ9)

```
/*eslint no-unsafe-optional-chaining: "error"*/

(obj?.foo)();

(obj?.foo).bar;

(foo?.()).bar;

(foo?.()).bar();

(obj?.foo ?? obj?.bar)();

(foo || obj?.foo)();

(obj?.foo && foo)();

(foo ? obj?.foo : bar)();

(foo, obj?.bar).baz;

(obj?.foo)`template`;

new (obj?.foo)();

[...obj?.foo];

bar(...obj?.foo);

1 in obj?.foo;

bar instanceof obj?.foo;

for (bar of obj?.foo);

const { bar } = obj?.foo;

[{ bar } = obj?.foo] = [];

with (obj?.foo);

class A extends obj?.foo {}

const a = class A extends obj?.foo {};

async function foo () {
    const { bar } = await obj?.foo;
   (await obj?.foo)();
   (await obj?.foo).bar;
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
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW9wdGlvbmFsLWNoYWluaW5nOiBcImVycm9yXCIqL1xuXG4ob2JqPy5mb28pPy4oKTtcblxub2JqPy5mb28oKTtcblxuKG9iaj8uZm9vID8/IGJhcikoKTtcblxub2JqPy5mb28uYmFyO1xuXG5vYmouZm9vPy5iYXI7XG5cbmZvbz8uKCk/LmJhcjtcblxuKG9iaj8uZm9vID8/IGJhcilgdGVtcGxhdGVgO1xuXG5uZXcgKG9iaj8uZm9vID8/IGJhcikoKTtcblxuY29uc3QgYmF6ID0gey4uLm9iaj8uZm9vfTtcblxuY29uc3QgeyBiYXIgfSA9IG9iaj8uZm9vIHx8IGJhejtcblxuYXN5bmMgZnVuY3Rpb24gZm9vICgpIHtcbiAgY29uc3QgeyBiYXIgfSA9IGF3YWl0IG9iaj8uZm9vIHx8IGJhejtcbiAgIChhd2FpdCBvYmo/LmZvbyk/LigpO1xuICAgKGF3YWl0IG9iaj8uZm9vKT8uYmFyO1xufSJ9)

```
/*eslint no-unsafe-optional-chaining: "error"*/

(obj?.foo)?.();

obj?.foo();

(obj?.foo ?? bar)();

obj?.foo.bar;

obj.foo?.bar;

foo?.()?.bar;

(obj?.foo ?? bar)`template`;

new (obj?.foo ?? bar)();

const baz = {...obj?.foo};

const { bar } = obj?.foo || baz;

async function foo () {
  const { bar } = await obj?.foo || baz;
   (await obj?.foo)?.();
   (await obj?.foo)?.bar;
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
24
25
26
27
```

## Options

This rule has an object option:

- `disallowArithmeticOperators`: Disallow arithmetic operations on optional chaining expressions (Default `false`). If this is `true`, this rule warns arithmetic operations on optional chaining expressions, which possibly result in `NaN`.

### disallowArithmeticOperators

With this option set to `true` the rule is enforced for:

- Unary operators: `-`, `+`
- Arithmetic operators: `+`, `-`, `/`, `*`, `%`, `**`
- Assignment operators: `+=`, `-=`, `/=`, `*=`, `%=`, `**=`

Examples of additional incorrect code for this rule with the `{ "disallowArithmeticOperators": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5zYWZlLW9wdGlvbmFsLWNoYWluaW5nOiBbXCJlcnJvclwiLCB7IFwiZGlzYWxsb3dBcml0aG1ldGljT3BlcmF0b3JzXCI6IHRydWUgfV0qL1xuXG4rb2JqPy5mb287XG4tb2JqPy5mb287XG5cbm9iaj8uZm9vICsgYmFyO1xub2JqPy5mb28gLSBiYXI7XG5vYmo/LmZvbyAvIGJhcjtcbm9iaj8uZm9vICogYmFyO1xub2JqPy5mb28gJSBiYXI7XG5vYmo/LmZvbyAqKiBiYXI7XG5cbmJheiArPSBvYmo/LmZvbztcbmJheiAtPSBvYmo/LmZvbztcbmJheiAvPSBvYmo/LmZvbztcbmJheiAqPSBvYmo/LmZvbztcbmJheiAlPSBvYmo/LmZvbztcbmJheiAqKj0gb2JqPy5mb287XG5cbmFzeW5jIGZ1bmN0aW9uIGZvbyAoKSB7XG4gICthd2FpdCBvYmo/LmZvbztcbiAgYXdhaXQgb2JqPy5mb28gKyBiYXI7XG4gIGJheiArPSBhd2FpdCBvYmo/LmZvbztcbn0ifQ==)

```
/*eslint no-unsafe-optional-chaining: ["error", { "disallowArithmeticOperators": true }]*/

+obj?.foo;
-obj?.foo;

obj?.foo + bar;
obj?.foo - bar;
obj?.foo / bar;
obj?.foo * bar;
obj?.foo % bar;
obj?.foo ** bar;

baz += obj?.foo;
baz -= obj?.foo;
baz /= obj?.foo;
baz *= obj?.foo;
baz %= obj?.foo;
baz **= obj?.foo;

async function foo () {
  +await obj?.foo;
  await obj?.foo + bar;
  baz += await obj?.foo;
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
24
```

## Version

This rule was introduced in ESLint v7.15.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unsafe-optional-chaining.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unsafe-optional-chaining.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unsafe-optional-chaining.md
                    
                
                )
