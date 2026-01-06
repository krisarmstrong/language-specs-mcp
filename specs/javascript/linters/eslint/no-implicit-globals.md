# no-implicit-globals

Disallow declarations in the global scope

## Table of Contents

1. [Rule Details](#rule-details)

  1. [var and function declarations](#var-and-function-declarations)
  2. [Global variable leaks](#global-variable-leaks)
  3. [Read-only global variables](#read-only-global-variables)
  4. [const, let and class declarations](#const-let-and-class-declarations)
  5. [exported](#exported)

2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

It is the best practice to avoid ‘polluting’ the global scope with variables that are intended to be local to the script.

Global variables created from a script can produce name collisions with global variables created from another script, which will usually lead to runtime errors or unexpected behavior.

This rule disallows the following:

- Declarations that create one or more variables in the global scope.
- Global variable leaks.
- Redeclarations of read-only global variables and assignments to read-only global variables.

There is an explicit way to create a global variable when needed, by assigning to a property of the global object.

This rule is mostly useful for browser scripts. Top-level declarations in ES modules and CommonJS modules create module-scoped variables. ES modules also have implicit `strict` mode, which prevents global variable leaks.

By default, this rule does not check `const`, `let` and `class` declarations.

This rule has an object option with one option:

- Set `"lexicalBindings"` to `true` if you want this rule to check `const`, `let` and `class` declarations as well.

## Rule Details

### `var` and `function` declarations

When working with browser scripts, developers often forget that variable and function declarations at the top-level scope become global variables on the `window` object. As opposed to modules which have their own scope. Globals should be explicitly assigned to `window` or `self` if that is the intent. Otherwise variables intended to be local to the script should be wrapped in an IIFE.

This rule disallows `var` and `function` declarations at the top-level script scope. This does not apply to ES and CommonJS modules since they have a module scope.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogXCJlcnJvclwiKi9cblxudmFyIGZvbyA9IDE7XG5cbmZ1bmN0aW9uIGJhcigpIHt9In0=)

```
/*eslint no-implicit-globals: "error"*/

var foo = 1;

function bar() {}
1
2
3
4
5
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogXCJlcnJvclwiKi9cblxuLy8gZXhwbGljaXRseSBzZXQgb24gd2luZG93XG53aW5kb3cuZm9vID0gMTtcbndpbmRvdy5iYXIgPSBmdW5jdGlvbigpIHt9O1xuXG4vLyBpbnRlbmRlZCB0byBiZSBzY29wZSB0byB0aGlzIGZpbGVcbihmdW5jdGlvbigpIHtcbiAgdmFyIGZvbyA9IDE7XG5cbiAgZnVuY3Rpb24gYmFyKCkge31cbn0pKCk7In0=)

```
/*eslint no-implicit-globals: "error"*/

// explicitly set on window
window.foo = 1;
window.bar = function() {};

// intended to be scope to this file
(function() {
  var foo = 1;

  function bar() {}
})();
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
```

Examples of correct code for this rule with `"parserOptions": { "sourceType": "module" }` in the ESLint configuration:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoibW9kdWxlIn19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogXCJlcnJvclwiKi9cblxuLy8gZm9vIGFuZCBiYXIgYXJlIGxvY2FsIHRvIG1vZHVsZVxudmFyIGZvbyA9IDE7XG5mdW5jdGlvbiBiYXIoKSB7fSJ9)

```
/*eslint no-implicit-globals: "error"*/

// foo and bar are local to module
var foo = 1;
function bar() {}
1
2
3
4
5
```

### Global variable leaks

When the code is not in `strict` mode, an assignment to an undeclared variable creates a new global variable. This will happen even if the code is in a function.

This does not apply to ES modules since the module code is implicitly in `strict` mode.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogXCJlcnJvclwiKi9cblxuZm9vID0gMTtcblxuQmFyLnByb3RvdHlwZS5iYXogPSBmdW5jdGlvbiAoKSB7XG4gICAgYSA9IDE7IC8vIEludGVuZGVkIHRvIGJlIHRoaXMuYSA9IDE7XG59OyJ9)

```
/*eslint no-implicit-globals: "error"*/

foo = 1;

Bar.prototype.baz = function () {
    a = 1; // Intended to be this.a = 1;
};
1
2
3
4
5
6
7
```

### Read-only global variables

This rule also disallows redeclarations of read-only global variables and assignments to read-only global variables.

A read-only global variable can be a built-in ES global (e.g. `Array`), or a global variable defined as `readonly` in the configuration file or in a `/*global */` comment.

See also: [Specifying Globals](../use/configure#specifying-globals)

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogXCJlcnJvclwiKi9cblxuLypnbG9iYWwgZm9vOnJlYWRvbmx5Ki9cblxuZm9vID0gMTtcblxuQXJyYXkgPSBbXTtcbnZhciBPYmplY3Q7In0=)

```
/*eslint no-implicit-globals: "error"*/

/*global foo:readonly*/

foo = 1;

Array = [];
var Object;
1
2
3
4
5
6
7
8
```

### `const`, `let` and `class` declarations

Lexical declarations `const` and `let`, as well as `class` declarations, create variables that are block-scoped.

However, when declared in the top-level of a browser script these variables are not ‘script-scoped’. They are actually created in the global scope and could produce name collisions with `var`, `const` and `let` variables and `function` and `class` declarations from other scripts. This does not apply to ES and CommonJS modules.

If the variable is intended to be local to the script, wrap the code with a block or with an immediately-invoked function expression (IIFE).

Examples of correct code for this rule with `"lexicalBindings"` option set to `false` (default):

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogW1wiZXJyb3JcIiwge1wibGV4aWNhbEJpbmRpbmdzXCI6IGZhbHNlfV0qL1xuXG5jb25zdCBmb28gPSAxO1xuXG5sZXQgYmF6O1xuXG5jbGFzcyBCYXIge30ifQ==)

```
/*eslint no-implicit-globals: ["error", {"lexicalBindings": false}]*/

const foo = 1;

let baz;

class Bar {}
1
2
3
4
5
6
7
```

Examples of incorrect code for this rule with `"lexicalBindings"` option set to `true`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogW1wiZXJyb3JcIiwge1wibGV4aWNhbEJpbmRpbmdzXCI6IHRydWV9XSovXG5cbmNvbnN0IGZvbyA9IDE7XG5cbmxldCBiYXo7XG5cbmNsYXNzIEJhciB7fSJ9)

```
/*eslint no-implicit-globals: ["error", {"lexicalBindings": true}]*/

const foo = 1;

let baz;

class Bar {}
1
2
3
4
5
6
7
```

Examples of correct code for this rule with `"lexicalBindings"` option set to `true`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogW1wiZXJyb3JcIiwge1wibGV4aWNhbEJpbmRpbmdzXCI6IHRydWV9XSovXG5cbntcbiAgICBjb25zdCBmb28gPSAxO1xuICAgIGxldCBiYXo7XG4gICAgY2xhc3MgQmFyIHt9XG59XG5cbihmdW5jdGlvbigpIHtcbiAgICBjb25zdCBmb28gPSAxO1xuICAgIGxldCBiYXo7XG4gICAgY2xhc3MgQmFyIHt9XG59KCkpOyJ9)

```
/*eslint no-implicit-globals: ["error", {"lexicalBindings": true}]*/

{
    const foo = 1;
    let baz;
    class Bar {}
}

(function() {
    const foo = 1;
    let baz;
    class Bar {}
}());
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

If you intend to create a global `const` or `let` variable or a global `class` declaration, to be used from other scripts, be aware that there are certain differences when compared to the traditional methods, which are `var` declarations and assigning to a property of the global `window` object:

- Lexically declared variables cannot be conditionally created. A script cannot check for the existence of a variable and then create a new one. `var` variables are also always created, but redeclarations do not cause runtime exceptions.
- Lexically declared variables do not create properties on the global object, which is what a consuming script might expect.
- Lexically declared variables are shadowing properties of the global object, which might produce errors if a consuming script is using both the variable and the property.
- Lexically declared variables can produce a permanent Temporal Dead Zone (TDZ) if the initialization throws an exception. Even the `typeof` check is not safe from TDZ reference exceptions.

Examples of incorrect code for this rule with `"lexicalBindings"` option set to `true`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogW1wiZXJyb3JcIiwge1wibGV4aWNhbEJpbmRpbmdzXCI6IHRydWV9XSovXG5cbmNvbnN0IE15R2xvYmFsRnVuY3Rpb24gPSAoZnVuY3Rpb24oKSB7XG4gICAgY29uc3QgYSA9IDE7XG4gICAgbGV0IGIgPSAyO1xuICAgIHJldHVybiBmdW5jdGlvbigpIHtcbiAgICAgICAgcmV0dXJuIGEgKyBiO1xuICAgIH1cbn0oKSk7In0=)

```
/*eslint no-implicit-globals: ["error", {"lexicalBindings": true}]*/

const MyGlobalFunction = (function() {
    const a = 1;
    let b = 2;
    return function() {
        return a + b;
    }
}());
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

Examples of correct code for this rule with `"lexicalBindings"` option set to `true`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wbGljaXQtZ2xvYmFsczogW1wiZXJyb3JcIiwge1wibGV4aWNhbEJpbmRpbmdzXCI6IHRydWV9XSovXG5cbndpbmRvdy5NeUdsb2JhbEZ1bmN0aW9uID0gKGZ1bmN0aW9uKCkge1xuICAgIGNvbnN0IGEgPSAxO1xuICAgIGxldCBiID0gMjtcbiAgICByZXR1cm4gZnVuY3Rpb24oKSB7XG4gICAgICAgIHJldHVybiBhICsgYjtcbiAgICB9XG59KCkpOyJ9)

```
/*eslint no-implicit-globals: ["error", {"lexicalBindings": true}]*/

window.MyGlobalFunction = (function() {
    const a = 1;
    let b = 2;
    return function() {
        return a + b;
    }
}());
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

### exported

You can use `/* exported variableName */` block comments in the same way as in [no-unused-vars](./no-unused-vars). See the [no-unused-vars exported section](./no-unused-vars#exported) for details.

Examples of correct code for `/* exported variableName */` operation:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyogZXNsaW50IG5vLWltcGxpY2l0LWdsb2JhbHM6IGVycm9yICovXG4vKiBleHBvcnRlZCBnbG9iYWxfdmFyICovXG5cbnZhciBnbG9iYWxfdmFyID0gNDI7In0=)

```
/* eslint no-implicit-globals: error */
/* exported global_var */

var global_var = 42;
1
2
3
4
```

## When Not To Use It

In the case of a browser script, if you want to be able to explicitly declare variables and functions in the global scope, and your code is in strict mode or you don’t want this rule to warn you about undeclared variables, and you also don’t want this rule to warn you about read-only globals, you can disable this rule.

In the case of a CommonJS module, if your code is in strict mode or you don’t want this rule to warn you about undeclared variables, and you also don’t want this rule to warn you about the read-only globals, you can disable this rule.

In the case of an ES module, if you don’t want this rule to warn you about the read-only globals you can disable this rule.

## Related Rules

- [no-undef](/docs/latest/rules/no-undef)
- [no-global-assign](/docs/latest/rules/no-global-assign)
- [no-unused-vars](/docs/latest/rules/no-unused-vars)

## Version

This rule was introduced in ESLint v2.0.0-alpha-1.

## Further Reading

[Ben Alman » Immediately-Invoked Function Expression (IIFE)](https://benalman.com/news/2010/11/immediately-invoked-function-expression/)
 benalman.com[ReferenceError: assignment to undeclared variable “x” - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Undeclared_var)
 developer.mozilla.org[let - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#Temporal_dead_zone)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-implicit-globals.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-implicit-globals.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-implicit-globals.md
                    
                
                )
