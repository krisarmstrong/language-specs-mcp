# strict

Require or disallow strict mode directives

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [safe](#safe)
  2. [global](#global)
  3. [function](#function)
  4. [never](#never)
  5. [earlier default (removed)](#earlier-default-removed)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

A strict mode directive is a `"use strict"` literal at the beginning of a script or function body. It enables strict mode semantics.

When a directive occurs in global scope, strict mode applies to the entire script:

```
"use strict";

// strict mode

function foo() {
    // strict mode
}
1
2
3
4
5
6
7
```

Copy code to clipboard

When a directive occurs at the beginning of a function body, strict mode applies only to that function, including all contained functions:

```
function foo() {
    "use strict";
    // strict mode
}

function foo2() {
    // not strict mode
};

(function() {
    "use strict";
    function bar() {
        // strict mode
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
10
11
12
13
14
15
```

Copy code to clipboard

In the CommonJS module system, a hidden function wraps each module and limits the scope of a “global” strict mode directive.

In ECMAScript modules, which always have strict mode semantics, the directives are unnecessary.

## Rule Details

This rule requires or disallows strict mode directives.

This rule disallows strict mode directives, no matter which option is specified, if ESLint configuration specifies either of the following as [parser options](../use/configure/language-options#specifying-javascript-options):

- `"sourceType": "module"` that is, files are ECMAScript modules.
- `"impliedStrict": true` property in the `ecmaFeatures` object.

This rule disallows strict mode directives, no matter which option is specified, in functions with non-simple parameter lists (for example, parameter lists with default parameter values) because that is a syntax error in ECMAScript 2016 and later. See the examples of the [function](#function) option.

This rule does not apply to class static blocks, no matter which option is specified, because class static blocks do not have directives. Therefore, a `"use strict"` statement in a class static block is not a directive, and will be reported by the [no-unused-expressions](no-unused-expressions) rule.

The `--fix` option on the command line does not insert new `"use strict"` statements, but only removes unneeded statements.

## Options

This rule has a string option:

- `"safe"` (default) corresponds either of the following options: 

  - `"global"` if ESLint considers a file to be a CommonJS module
  - `"function"` otherwise

- `"global"` requires one strict mode directive in the global scope (and disallows any other strict mode directives)
- `"function"` requires one strict mode directive in each top-level function declaration or expression (and disallows any other strict mode directives)
- `"never"` disallows strict mode directives

### safe

The `"safe"` option corresponds to the `"global"` option if ESLint considers a file to be a Node.js or CommonJS module because the configuration specifies either of the following:

- `"sourceType": "commonjs"` in [language options](../use/configure/language-options#specifying-javascript-options)
- `"globalReturn": true` property in the `ecmaFeatures` object of [parser options](../use/configure/language-options#specifying-parser-options)

Otherwise the `"safe"` option corresponds to the `"function"` option.

### global

Examples of incorrect code for this rule with the `"global"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImdsb2JhbFwiXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbn0ifQ==)

```
/*eslint strict: ["error", "global"]*/

function foo() {
}
1
2
3
4
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImdsb2JhbFwiXSovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICBcInVzZSBzdHJpY3RcIjtcbn0ifQ==)

```
/*eslint strict: ["error", "global"]*/

function foo() {
    "use strict";
}
1
2
3
4
5
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImdsb2JhbFwiXSovXG5cblwidXNlIHN0cmljdFwiO1xuXG5mdW5jdGlvbiBmb28oKSB7XG4gICAgXCJ1c2Ugc3RyaWN0XCI7XG59In0=)

```
/*eslint strict: ["error", "global"]*/

"use strict";

function foo() {
    "use strict";
}
1
2
3
4
5
6
7
```

Examples of correct code for this rule with the `"global"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImdsb2JhbFwiXSovXG5cblwidXNlIHN0cmljdFwiO1xuXG5mdW5jdGlvbiBmb28oKSB7XG59In0=)

```
/*eslint strict: ["error", "global"]*/

"use strict";

function foo() {
}
1
2
3
4
5
6
```

### function

This option ensures that all function bodies are strict mode code, while global code is not. Particularly if a build step concatenates multiple scripts, a strict mode directive in global code of one script could unintentionally enable strict mode in another script that was not intended to be strict code.

Examples of incorrect code for this rule with the `"function"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImZ1bmN0aW9uXCJdKi9cblxuXCJ1c2Ugc3RyaWN0XCI7XG5cbmZ1bmN0aW9uIGZvbygpIHtcbn0ifQ==)

```
/*eslint strict: ["error", "function"]*/

"use strict";

function foo() {
}
1
2
3
4
5
6
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImZ1bmN0aW9uXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xufVxuXG4oZnVuY3Rpb24oKSB7XG4gICAgZnVuY3Rpb24gYmFyKCkge1xuICAgICAgICBcInVzZSBzdHJpY3RcIjtcbiAgICB9XG59KCkpOyJ9)

```
/*eslint strict: ["error", "function"]*/

function foo() {
}

(function() {
    function bar() {
        "use strict";
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
10
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJlY21hVmVyc2lvbiI6MjAxNSwic291cmNlVHlwZSI6InNjcmlwdCJ9fSwidGV4dCI6Ii8qZXNsaW50IHN0cmljdDogW1wiZXJyb3JcIiwgXCJmdW5jdGlvblwiXSovXG5cbi8vIElsbGVnYWwgXCJ1c2Ugc3RyaWN0XCIgZGlyZWN0aXZlIGluIGZ1bmN0aW9uIHdpdGggbm9uLXNpbXBsZSBwYXJhbWV0ZXIgbGlzdC5cbi8vIFRoaXMgaXMgYSBzeW50YXggZXJyb3Igc2luY2UgRVMyMDE2LlxuZnVuY3Rpb24gZm9vKGEgPSAxKSB7XG4gICAgXCJ1c2Ugc3RyaWN0XCI7XG59XG5cbi8vIFdlIGNhbm5vdCB3cml0ZSBcInVzZSBzdHJpY3RcIiBkaXJlY3RpdmUgaW4gdGhpcyBmdW5jdGlvbi5cbi8vIFNvIHdlIGhhdmUgdG8gd3JhcCB0aGlzIGZ1bmN0aW9uIHdpdGggYSBmdW5jdGlvbiB3aXRoIFwidXNlIHN0cmljdFwiIGRpcmVjdGl2ZS5cbmZ1bmN0aW9uIGZvbyhhID0gMSkge1xufSJ9)

```
/*eslint strict: ["error", "function"]*/

// Illegal "use strict" directive in function with non-simple parameter list.
// This is a syntax error since ES2016.
function foo(a = 1) {
    "use strict";
}

// We cannot write "use strict" directive in this function.
// So we have to wrap this function with a function with "use strict" directive.
function foo(a = 1) {
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
```

Examples of correct code for this rule with the `"function"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcImZ1bmN0aW9uXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIFwidXNlIHN0cmljdFwiO1xufVxuXG4oZnVuY3Rpb24oKSB7XG4gICAgXCJ1c2Ugc3RyaWN0XCI7XG5cbiAgICBmdW5jdGlvbiBiYXIoKSB7XG4gICAgfVxuXG4gICAgZnVuY3Rpb24gYmF6KGEgPSAxKSB7XG4gICAgfVxufSgpKTtcblxuY29uc3QgZm9vMiA9IChmdW5jdGlvbigpIHtcbiAgICBcInVzZSBzdHJpY3RcIjtcblxuICAgIHJldHVybiBmdW5jdGlvbiBmb28oYSA9IDEpIHtcbiAgICB9O1xufSgpKTsifQ==)

```
/*eslint strict: ["error", "function"]*/

function foo() {
    "use strict";
}

(function() {
    "use strict";

    function bar() {
    }

    function baz(a = 1) {
    }
}());

const foo2 = (function() {
    "use strict";

    return function foo(a = 1) {
    };
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
14
15
16
17
18
19
20
21
22
```

### never

Examples of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdKi9cblxuXCJ1c2Ugc3RyaWN0XCI7XG5cbmZ1bmN0aW9uIGZvbygpIHtcbn0ifQ==)

```
/*eslint strict: ["error", "never"]*/

"use strict";

function foo() {
}
1
2
3
4
5
6
```

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIFwidXNlIHN0cmljdFwiO1xufSJ9)

```
/*eslint strict: ["error", "never"]*/

function foo() {
    "use strict";
}
1
2
3
4
5
```

Examples of correct code for this rule with the `"never"` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgc3RyaWN0OiBbXCJlcnJvclwiLCBcIm5ldmVyXCJdKi9cblxuZnVuY3Rpb24gZm9vKCkge1xufSJ9)

```
/*eslint strict: ["error", "never"]*/

function foo() {
}
1
2
3
4
```

### earlier default (removed)

(removed) The default option (that is, no string option specified) for this rule was removed in ESLint v1.0. The `"function"` option is most similar to the removed option.

This option ensures that all functions are executed in strict mode. A strict mode directive must be present in global code or in every top-level function declaration or expression. It does not concern itself with unnecessary strict mode directives in nested functions that are already strict, nor with multiple strict mode directives at the same level.

Examples of incorrect code for this rule with the earlier default option which has been removed:

```
// "strict": "error"

function foo() {
}
1
2
3
4
```

Copy code to clipboard

```
// "strict": "error"

(function() {
    function bar() {
        "use strict";
    }
}());
1
2
3
4
5
6
7
```

Copy code to clipboard

Examples of correct code for this rule with the earlier default option which has been removed:

```
// "strict": "error"

"use strict";

function foo() {
}
1
2
3
4
5
6
```

Copy code to clipboard

```
// "strict": "error"

function foo() {
    "use strict";
}
1
2
3
4
5
```

Copy code to clipboard

```
// "strict": "error"

(function() {
    "use strict";
    function bar() {
        "use strict";
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
```

Copy code to clipboard

## When Not To Use It

In a codebase that has both strict and non-strict code, either turn this rule off, or [selectively disable it](../use/configure/rules#disabling-rules) where necessary. For example, functions referencing `arguments.callee` are invalid in strict mode. A [full list of strict mode differences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode/Transitioning_to_strict_mode#Differences_from_non-strict_to_strict) is available on MDN.

## Version

This rule was introduced in ESLint v0.1.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/strict.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/strict.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/strict.md
                    
                
                )
