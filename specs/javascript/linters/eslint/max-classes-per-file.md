# max-classes-per-file

Enforce a maximum number of classes per file

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [Version](#version)
4. [Resources](#resources)

Files containing multiple classes can often result in a less navigable and poorly structured codebase. Best practice is to keep each file limited to a single responsibility.

## Rule Details

This rule enforces that each file may contain only a particular number of classes and no more.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWNsYXNzZXMtcGVyLWZpbGU6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEZvbyB7fVxuY2xhc3MgQmFyIHt9In0=)

```
/*eslint max-classes-per-file: "error"*/

class Foo {}
class Bar {}
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbWF4LWNsYXNzZXMtcGVyLWZpbGU6IFwiZXJyb3JcIiovXG5cbmNsYXNzIEZvbyB7fSJ9)

```
/*eslint max-classes-per-file: "error"*/

class Foo {}
1
2
3
```

## Options

This rule may be configured with either an object or a number.

If the option is an object, it may contain one or both of:

- `ignoreExpressions`: a boolean option (defaulted to `false`) to ignore class expressions.
- `max`: a numeric option (defaulted to 1) to specify the maximum number of classes.

For example:

```
{
    "max-classes-per-file": ["error", 1]
}
1
2
3
```

Copy code to clipboard

```
{
    "max-classes-per-file": [
        "error",
        { "ignoreExpressions": true, "max": 2 }
    ]
}
1
2
3
4
5
6
```

Copy code to clipboard

Examples of correct code for this rule with the `max` option set to `2`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG1heC1jbGFzc2VzLXBlci1maWxlOiBbXCJlcnJvclwiLCAyXSAqL1xuXG5jbGFzcyBGb28ge31cbmNsYXNzIEJhciB7fSJ9)

```
/* eslint max-classes-per-file: ["error", 2] */

class Foo {}
class Bar {}
1
2
3
4
```

Examples of correct code for this rule with the `ignoreExpressions` option set to `true`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG1heC1jbGFzc2VzLXBlci1maWxlOiBbXCJlcnJvclwiLCB7IGlnbm9yZUV4cHJlc3Npb25zOiB0cnVlIH1dICovXG5cbmNsYXNzIFZpc2l0b3JGYWN0b3J5IHtcbiAgICBmb3JEZXNjcmlwdG9yKGRlc2NyaXB0b3IpIHtcbiAgICAgICAgcmV0dXJuIGNsYXNzIHtcbiAgICAgICAgICAgIHZpc2l0KG5vZGUpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gYFZpc2l0aW5nICR7ZGVzY3JpcHRvcn0uYDtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfTtcbiAgICB9XG59In0=)

```
/* eslint max-classes-per-file: ["error", { ignoreExpressions: true }] */

class VisitorFactory {
    forDescriptor(descriptor) {
        return class {
            visit(node) {
                return `Visiting ${descriptor}.`;
            }
        };
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
```

## Version

This rule was introduced in ESLint v5.0.0-alpha.3.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/max-classes-per-file.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/max-classes-per-file.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/max-classes-per-file.md
                    
                
                )
