# no-constant-binary-expression

Disallow expressions where the operation doesn't affect the value

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Related Rules](#related-rules)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

Comparisons which will always evaluate to true or false and logical expressions (`||`, `&&`, `??`) which either always short-circuit or never short-circuit are both likely indications of programmer error.

These errors are especially common in complex expressions where operator precedence is easy to misjudge. For example:

```
// One might think this would evaluate as `a + (b ?? c)`:
const x = a + b ?? c;

// But it actually evaluates as `(a + b) ?? c`. Since `a + b` can never be null,
// the `?? c` has no effect.
1
2
3
4
5
```

Copy code to clipboard

Additionally, this rule detects comparisons to newly constructed objects/arrays/functions/etc. In JavaScript, where objects are compared by reference, a newly constructed object can never`===` any other value. This can be surprising for programmers coming from languages where objects are compared by value.

```
// Programmers coming from a language where objects are compared by value might expect this to work:
const isEmpty = x === [];

// However, this will always result in `isEmpty` being `false`.
1
2
3
4
```

Copy code to clipboard

## Rule Details

This rule identifies `==` and `===` comparisons which, based on the semantics of the JavaScript language, will always evaluate to `true` or `false`.

It also identifies `||`, `&&` and `??` logical expressions which will either always or never short-circuit.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtYmluYXJ5LWV4cHJlc3Npb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IHZhbHVlMSA9ICt4ID09IG51bGw7XG5cbmNvbnN0IHZhbHVlMiA9IGNvbmRpdGlvbiA/IHggOiB7fSB8fCBERUZBVUxUO1xuXG5jb25zdCB2YWx1ZTMgPSAhZm9vID09IG51bGw7XG5cbmNvbnN0IHZhbHVlNCA9IG5ldyBCb29sZWFuKGZvbykgPT09IHRydWU7XG5cbmNvbnN0IG9iaklzRW1wdHkgPSBzb21lT2JqID09PSB7fTtcblxuY29uc3QgYXJySXNFbXB0eSA9IHNvbWVBcnIgPT09IFtdO1xuXG5jb25zdCBzaG9ydENpcmN1aXQxID0gY29uZGl0aW9uMSAmJiBmYWxzZSAmJiBjb25kaXRpb24yO1xuXG5jb25zdCBzaG9ydENpcmN1aXQyID0gY29uZGl0aW9uMSB8fCB0cnVlIHx8IGNvbmRpdGlvbjI7XG5cbmNvbnN0IHNob3J0Q2lyY3VpdDMgPSBjb25kaXRpb24xID8/IFwibm9uLW51bGxpc2hcIiA/PyBjb25kaXRpb24yOyJ9)

```
/*eslint no-constant-binary-expression: "error"*/

const value1 = +x == null;

const value2 = condition ? x : {} || DEFAULT;

const value3 = !foo == null;

const value4 = new Boolean(foo) === true;

const objIsEmpty = someObj === {};

const arrIsEmpty = someArr === [];

const shortCircuit1 = condition1 && false && condition2;

const shortCircuit2 = condition1 || true || condition2;

const shortCircuit3 = condition1 ?? "non-nullish" ?? condition2;
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tY29uc3RhbnQtYmluYXJ5LWV4cHJlc3Npb246IFwiZXJyb3JcIiovXG5cbmNvbnN0IHZhbHVlMSA9IHggPT0gbnVsbDtcblxuY29uc3QgdmFsdWUyID0gKGNvbmRpdGlvbiA/IHggOiB7fSkgfHwgREVGQVVMVDtcblxuY29uc3QgdmFsdWUzID0gIShmb28gPT0gbnVsbCk7XG5cbmNvbnN0IHZhbHVlNCA9IEJvb2xlYW4oZm9vKSA9PT0gdHJ1ZTtcblxuY29uc3Qgb2JqSXNFbXB0eSA9IE9iamVjdC5rZXlzKHNvbWVPYmopLmxlbmd0aCA9PT0gMDtcblxuY29uc3QgYXJySXNFbXB0eSA9IHNvbWVBcnIubGVuZ3RoID09PSAwOyJ9)

```
/*eslint no-constant-binary-expression: "error"*/

const value1 = x == null;

const value2 = (condition ? x : {}) || DEFAULT;

const value3 = !(foo == null);

const value4 = Boolean(foo) === true;

const objIsEmpty = Object.keys(someObj).length === 0;

const arrIsEmpty = someArr.length === 0;
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

## Related Rules

- [no-constant-condition](/docs/latest/rules/no-constant-condition)

## Version

This rule was introduced in ESLint v8.14.0.

## Further Reading

[Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2022/07/interesting-bugs-caught-by-no-constant-binary-expression/)
 eslint.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-constant-binary-expression.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-constant-binary-expression.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-constant-binary-expression.md
                    
                
                )
