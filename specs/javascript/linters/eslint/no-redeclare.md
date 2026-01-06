# no-redeclare

Disallow variable redeclaration

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [builtinGlobals](#builtinglobals)

3. [Handled by TypeScript](#handled_by_typescript)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

In JavaScript, it’s possible to redeclare the same variable name using `var`. This can lead to confusion as to where the variable is actually declared and initialized.

## Rule Details

This rule is aimed at eliminating variables that have multiple declarations in the same scope.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVkZWNsYXJlOiBcImVycm9yXCIqL1xuXG52YXIgYSA9IDM7XG52YXIgYSA9IDEwO1xuXG5jbGFzcyBDIHtcbiAgICBmb28oKSB7XG4gICAgICAgIHZhciBiID0gMztcbiAgICAgICAgdmFyIGIgPSAxMDtcbiAgICB9XG5cbiAgICBzdGF0aWMge1xuICAgICAgICB2YXIgYyA9IDM7XG4gICAgICAgIHZhciBjID0gMTA7XG4gICAgfVxufSJ9)

```
/*eslint no-redeclare: "error"*/

var a = 3;
var a = 10;

class C {
    foo() {
        var b = 3;
        var b = 10;
    }

    static {
        var c = 3;
        var c = 10;
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVkZWNsYXJlOiBcImVycm9yXCIqL1xuXG52YXIgYSA9IDM7XG5hID0gMTA7XG5cbmNsYXNzIEMge1xuICAgIGZvbygpIHtcbiAgICAgICAgdmFyIGIgPSAzO1xuICAgICAgICBiID0gMTA7XG4gICAgfVxuXG4gICAgc3RhdGljIHtcbiAgICAgICAgdmFyIGMgPSAzO1xuICAgICAgICBjID0gMTA7XG4gICAgfVxufVxuIn0=)

```
/*eslint no-redeclare: "error"*/

var a = 3;
a = 10;

class C {
    foo() {
        var b = 3;
        b = 10;
    }

    static {
        var c = 3;
        c = 10;
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
```

## Options

This rule takes one optional argument, an object with a boolean property `"builtinGlobals"`. It defaults to `true`. If set to `true`, this rule also checks redeclaration of built-in globals, such as `Object`, `Array`, `Number`…

### builtinGlobals

The `"builtinGlobals"` option will check for redeclaration of built-in globals in global scope.

Examples of incorrect code for the `{ "builtinGlobals": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tcmVkZWNsYXJlOiBbXCJlcnJvclwiLCB7IFwiYnVpbHRpbkdsb2JhbHNcIjogdHJ1ZSB9XSovXG5cbnZhciBPYmplY3QgPSAwOyJ9)

```
/*eslint no-redeclare: ["error", { "builtinGlobals": true }]*/

var Object = 0;
1
2
3
```

Note that when using `sourceType: "commonjs"` (or `ecmaFeatures.globalReturn`, if using the default parser), the top scope of a program is not actually the global scope, but rather a “module” scope. When this is the case, declaring a variable named after a builtin global is not a redeclaration, but rather a shadowing of the global variable. In that case, the [no-shadow](no-shadow) rule with the `"builtinGlobals"` option should be used.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

Note that while TypeScript will catch `let` redeclares and `const` redeclares, it will not catch `var` redeclares. Thus, if you use the legacy `var` keyword in your TypeScript codebase, this rule will still provide some value.

## Related Rules

- [no-shadow](/docs/latest/rules/no-shadow)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-redeclare.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-redeclare.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-redeclare.md
                    
                
                )
