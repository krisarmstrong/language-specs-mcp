# no-with

Disallow `with` statements

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

The `with` statement is potentially problematic because it adds members of an object to the current scope, making it impossible to tell what a variable inside the block actually refers to.

## Rule Details

This rule disallows `with` statements.

If ESLint parses code in strict mode, the parser (instead of this rule) reports the error.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8td2l0aDogXCJlcnJvclwiKi9cblxud2l0aCAocG9pbnQpIHtcbiAgICByID0gTWF0aC5zcXJ0KHggKiB4ICsgeSAqIHkpOyAvLyBpcyByIGEgbWVtYmVyIG9mIHBvaW50P1xufSJ9)

```
/*eslint no-with: "error"*/

with (point) {
    r = Math.sqrt(x * x + y * y); // is r a member of point?
}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8td2l0aDogXCJlcnJvclwiKi9cblxuY29uc3QgciA9ICh7eCwgeX0pID0+IE1hdGguc3FydCh4ICogeCArIHkgKiB5KTsifQ==)

```
/*eslint no-with: "error"*/

const r = ({x, y}) => Math.sqrt(x * x + y * y);
1
2
3
```

## When Not To Use It

If you intentionally use `with` statements then you can disable this rule.

## Version

This rule was introduced in ESLint v0.0.2.

## Further Reading

[with Statement Considered Harmful](https://web.archive.org/web/20200717110117/https://yuiblog.com/blog/2006/04/11/with-statement-considered-harmful/)
 web.archive.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-with.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-with.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-with.md
                    
                
                )
