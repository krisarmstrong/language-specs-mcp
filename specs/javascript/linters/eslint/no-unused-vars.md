# no-unused-vars

Disallow unused variables

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)

  1. [exported](#exported)

2. [Options](#options)

  1. [vars](#vars)

    1. [vars: local](#vars-local)

  2. [varsIgnorePattern](#varsignorepattern)
  3. [args](#args)

    1. [args: after-used](#args-after-used)
    2. [args: all](#args-all)
    3. [args: none](#args-none)

  4. [argsIgnorePattern](#argsignorepattern)
  5. [caughtErrors](#caughterrors)

    1. [caughtErrors: all](#caughterrors-all)
    2. [caughtErrors: none](#caughterrors-none)

  6. [caughtErrorsIgnorePattern](#caughterrorsignorepattern)
  7. [destructuredArrayIgnorePattern](#destructuredarrayignorepattern)
  8. [ignoreRestSiblings](#ignorerestsiblings)
  9. [ignoreClassWithStaticInitBlock](#ignoreclasswithstaticinitblock)
  10. [ignoreUsingDeclarations](#ignoreusingdeclarations)
  11. [reportUsedIgnorePattern](#reportusedignorepattern)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Variables that are declared and not used anywhere in the code are most likely an error due to incomplete refactoring. Such variables take up space in the code and can lead to confusion by readers.

## Rule Details

This rule is aimed at eliminating unused variables, functions, and function parameters.

A variable `foo` is considered to be used if any of the following are true:

- It is called (`foo()`) or constructed (`new foo()`)
- It is read (`let bar = foo`)
- It is passed into a function as an argument (`doSomething(foo)`)
- It is read inside of a function that is passed to another function (`doSomething(function() { foo(); })`)

A variable is not considered to be used if it is only ever declared (`let foo = 5`) or assigned to (`foo = 7`).

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFwiZXJyb3JcIiovXG4vKmdsb2JhbCBzb21lX3VudXNlZF92YXIqL1xuXG4vLyBJdCBjaGVja3MgdmFyaWFibGVzIHlvdSBoYXZlIGRlZmluZWQgYXMgZ2xvYmFsXG5zb21lX3VudXNlZF92YXIgPSA0MjtcblxubGV0IHg7XG5cbi8vIFdyaXRlLW9ubHkgdmFyaWFibGVzIGFyZSBub3QgY29uc2lkZXJlZCBhcyB1c2VkLlxubGV0IHkgPSAxMDtcbnkgPSA1O1xuXG4vLyBBIHJlYWQgZm9yIGEgbW9kaWZpY2F0aW9uIG9mIGl0c2VsZiBpcyBub3QgY29uc2lkZXJlZCBhcyB1c2VkLlxubGV0IHogPSAwO1xueiA9IHogKyAxO1xuXG4vLyBCeSBkZWZhdWx0LCB1bnVzZWQgYXJndW1lbnRzIGNhdXNlIHdhcm5pbmdzLlxuKGZ1bmN0aW9uKGZvbykge1xuICAgIHJldHVybiA1O1xufSkoKTtcblxuLy8gVW51c2VkIHJlY3Vyc2l2ZSBmdW5jdGlvbnMgYWxzbyBjYXVzZSB3YXJuaW5ncy5cbmZ1bmN0aW9uIGZhY3Qobikge1xuICAgIGlmIChuIDwgMikgcmV0dXJuIDE7XG4gICAgcmV0dXJuIG4gKiBmYWN0KG4gLSAxKTtcbn1cblxuLy8gV2hlbiBhIGZ1bmN0aW9uIGRlZmluaXRpb24gZGVzdHJ1Y3R1cmVzIGFuIGFycmF5LCB1bnVzZWQgZW50cmllcyBmcm9tIHRoZSBhcnJheSBhbHNvIGNhdXNlIHdhcm5pbmdzLlxuZnVuY3Rpb24gZ2V0WShbeCwgeV0pIHtcbiAgICByZXR1cm4geTtcbn1cbmdldFkoW1wiYVwiLCBcImJcIl0pOyJ9)

```
/*eslint no-unused-vars: "error"*/
/*global some_unused_var*/

// It checks variables you have defined as global
some_unused_var = 42;

let x;

// Write-only variables are not considered as used.
let y = 10;
y = 5;

// A read for a modification of itself is not considered as used.
let z = 0;
z = z + 1;

// By default, unused arguments cause warnings.
(function(foo) {
    return 5;
})();

// Unused recursive functions also cause warnings.
function fact(n) {
    if (n < 2) return 1;
    return n * fact(n - 1);
}

// When a function definition destructures an array, unused entries from the array also cause warnings.
function getY([x, y]) {
    return y;
}
getY(["a", "b"]);
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHggPSAxMDtcbmFsZXJ0KHgpO1xuXG4vLyBmb28gaXMgY29uc2lkZXJlZCB1c2VkIGhlcmVcbm15RnVuYyhmdW5jdGlvbiBmb28oKSB7XG4gICAgLy8gLi4uXG59LmJpbmQodGhpcykpO1xuXG4oZnVuY3Rpb24oZm9vKSB7XG4gICAgcmV0dXJuIGZvbztcbn0pKCk7XG5cbnZhciBteUZ1bmM7XG5teUZ1bmMgPSBzZXRUaW1lb3V0KGZ1bmN0aW9uKCkge1xuICAgIC8vIG15RnVuYyBpcyBjb25zaWRlcmVkIHVzZWRcbiAgICBteUZ1bmMoKTtcbn0sIDUwKTtcblxuLy8gT25seSB0aGUgc2Vjb25kIGFyZ3VtZW50IGZyb20gdGhlIGRlc3RydWN0dXJlZCBhcnJheSBpcyB1c2VkLlxuZnVuY3Rpb24gZ2V0WShbLCB5XSkge1xuICAgIHJldHVybiB5O1xufVxuZ2V0WShbXCJhXCIsIFwiYlwiXSk7In0=)

```
/*eslint no-unused-vars: "error"*/

const x = 10;
alert(x);

// foo is considered used here
myFunc(function foo() {
    // ...
}.bind(this));

(function(foo) {
    return foo;
})();

var myFunc;
myFunc = setTimeout(function() {
    // myFunc is considered used
    myFunc();
}, 50);

// Only the second argument from the destructured array is used.
function getY([, y]) {
    return y;
}
getY(["a", "b"]);
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
```

### exported

In environments outside of CommonJS or ECMAScript modules, you may use `var` to create a global variable that may be used by other scripts. You can use the `/* exported variableName */` comment block to indicate that this variable is being exported and therefore should not be considered unused.

Note that `/* exported */` has no effect for any of the following:

- when `languageOptions.sourceType` is `module` (default) or `commonjs`
- when `languageOptions.parserOptions.ecmaFeatures.globalReturn` is `true`

The line comment `// exported variableName` will not work as `exported` is not line-specific.

```
/* exported global_var */

var global_var = 42;
1
2
3
```

Copy code to clipboard

Examples of correct code for `/* exported variableName */` operation with `no-unused-vars`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFwiZXJyb3JcIiovXG4vKiBleHBvcnRlZCBnbG9iYWxfdmFyICovXG5cbnZhciBnbG9iYWxfdmFyID0gNDI7In0=)

```
/*eslint no-unused-vars: "error"*/
/* exported global_var */

var global_var = 42;
1
2
3
4
```

## Options

This rule takes one argument which can be a string or an object. The string settings are the same as those of the `vars` property (explained below).

By default this rule is enabled with `all` option for caught errors and variables, and `after-used` for arguments.

```
{
    "rules": {
        "no-unused-vars": ["error", {
            "vars": "all",
            "args": "after-used",
            "caughtErrors": "all",
            "ignoreRestSiblings": false,
            "ignoreUsingDeclarations": false,
            "reportUsedIgnorePattern": false
        }]
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
```

Copy code to clipboard

### vars

The `vars` option has two settings:

- `all` checks all variables for usage, including those in the global scope. However, it excludes variables targeted by other options like `args` and `caughtErrors`. This is the default setting.
- `local` checks only that locally-declared variables are used but will allow global variables to be unused.

#### vars: local

Examples of correct code for the `{ "vars": "local" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJ2YXJzXCI6IFwibG9jYWxcIiB9XSovXG4vKmdsb2JhbCBzb21lX3VudXNlZF92YXIgKi9cblxuc29tZV91bnVzZWRfdmFyID0gNDI7In0=)

```
/*eslint no-unused-vars: ["error", { "vars": "local" }]*/
/*global some_unused_var */

some_unused_var = 42;
1
2
3
4
```

### varsIgnorePattern

The `varsIgnorePattern` option specifies exceptions not to check for usage: variables whose names match a regexp pattern. For example, variables whose names contain `ignored` or `Ignored`. However, it excludes variables targeted by other options like `argsIgnorePattern` and `caughtErrorsIgnorePattern`.

Examples of correct code for the `{ "varsIgnorePattern": "[iI]gnored" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJ2YXJzSWdub3JlUGF0dGVyblwiOiBcIltpSV1nbm9yZWRcIiB9XSovXG5cbmNvbnN0IGZpcnN0VmFySWdub3JlZCA9IDE7XG5jb25zdCBzZWNvbmRWYXIgPSAyO1xuY29uc29sZS5sb2coc2Vjb25kVmFyKTsifQ==)

```
/*eslint no-unused-vars: ["error", { "varsIgnorePattern": "[iI]gnored" }]*/

const firstVarIgnored = 1;
const secondVar = 2;
console.log(secondVar);
1
2
3
4
5
```

### args

The `args` option has three settings:

- `after-used` - unused positional arguments that occur before the last used argument will not be checked, but all named arguments and all positional arguments after the last used argument will be checked.
- `all` - all named arguments must be used.
- `none` - do not check arguments.

#### args: after-used

Examples of incorrect code for the default `{ "args": "after-used" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJhcmdzXCI6IFwiYWZ0ZXItdXNlZFwiIH1dKi9cblxuLy8gMiBlcnJvcnMsIGZvciB0aGUgcGFyYW1ldGVycyBhZnRlciB0aGUgbGFzdCB1c2VkIHBhcmFtZXRlciAoYmFyKVxuLy8gXCJiYXpcIiBpcyBkZWZpbmVkIGJ1dCBuZXZlciB1c2VkXG4vLyBcInF1eFwiIGlzIGRlZmluZWQgYnV0IG5ldmVyIHVzZWRcbihmdW5jdGlvbihmb28sIGJhciwgYmF6LCBxdXgpIHtcbiAgICByZXR1cm4gYmFyO1xufSkoKTsifQ==)

```
/*eslint no-unused-vars: ["error", { "args": "after-used" }]*/

// 2 errors, for the parameters after the last used parameter (bar)
// "baz" is defined but never used
// "qux" is defined but never used
(function(foo, bar, baz, qux) {
    return bar;
})();
1
2
3
4
5
6
7
8
```

Examples of correct code for the default `{ "args": "after-used" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHtcImFyZ3NcIjogXCJhZnRlci11c2VkXCJ9XSovXG5cbihmdW5jdGlvbihmb28sIGJhciwgYmF6LCBxdXgpIHtcbiAgICByZXR1cm4gcXV4O1xufSkoKTsifQ==)

```
/*eslint no-unused-vars: ["error", {"args": "after-used"}]*/

(function(foo, bar, baz, qux) {
    return qux;
})();
1
2
3
4
5
```

#### args: all

Examples of incorrect code for the `{ "args": "all" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJhcmdzXCI6IFwiYWxsXCIgfV0qL1xuXG4vLyAyIGVycm9yc1xuLy8gXCJmb29cIiBpcyBkZWZpbmVkIGJ1dCBuZXZlciB1c2VkXG4vLyBcImJhelwiIGlzIGRlZmluZWQgYnV0IG5ldmVyIHVzZWRcbihmdW5jdGlvbihmb28sIGJhciwgYmF6KSB7XG4gICAgcmV0dXJuIGJhcjtcbn0pKCk7In0=)

```
/*eslint no-unused-vars: ["error", { "args": "all" }]*/

// 2 errors
// "foo" is defined but never used
// "baz" is defined but never used
(function(foo, bar, baz) {
    return bar;
})();
1
2
3
4
5
6
7
8
```

#### args: none

Examples of correct code for the `{ "args": "none" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJhcmdzXCI6IFwibm9uZVwiIH1dKi9cblxuKGZ1bmN0aW9uKGZvbywgYmFyLCBiYXopIHtcbiAgICByZXR1cm4gYmFyO1xufSkoKTsifQ==)

```
/*eslint no-unused-vars: ["error", { "args": "none" }]*/

(function(foo, bar, baz) {
    return bar;
})();
1
2
3
4
5
```

### argsIgnorePattern

The `argsIgnorePattern` option specifies exceptions not to check for usage: arguments whose names match a regexp pattern. For example, variables whose names begin with an underscore.

Examples of correct code for the `{ "argsIgnorePattern": "^_" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJhcmdzSWdub3JlUGF0dGVyblwiOiBcIl5fXCIgfV0qL1xuXG5mdW5jdGlvbiBmb28oeCwgX3kpIHtcbiAgICByZXR1cm4geCArIDE7XG59XG5mb28oKTsifQ==)

```
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/

function foo(x, _y) {
    return x + 1;
}
foo();
1
2
3
4
5
6
```

### caughtErrors

The `caughtErrors` option is used for `catch` block arguments validation.

It has two settings:

- `all` - all named arguments must be used. This is the default setting.
- `none` - do not check error objects.

#### caughtErrors: all

Not specifying this option is equivalent of assigning it to `all`.

Examples of incorrect code for the `{ "caughtErrors": "all" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJjYXVnaHRFcnJvcnNcIjogXCJhbGxcIiB9XSovXG5cbi8vIDEgZXJyb3Jcbi8vIFwiZXJyXCIgaXMgZGVmaW5lZCBidXQgbmV2ZXIgdXNlZFxudHJ5IHtcbiAgICAvLy4uLlxufSBjYXRjaCAoZXJyKSB7XG4gICAgY29uc29sZS5lcnJvcihcImVycm9yc1wiKTtcbn0ifQ==)

```
/*eslint no-unused-vars: ["error", { "caughtErrors": "all" }]*/

// 1 error
// "err" is defined but never used
try {
    //...
} catch (err) {
    console.error("errors");
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

#### caughtErrors: none

Examples of correct code for the `{ "caughtErrors": "none" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJjYXVnaHRFcnJvcnNcIjogXCJub25lXCIgfV0qL1xuXG50cnkge1xuICAgIC8vLi4uXG59IGNhdGNoIChlcnIpIHtcbiAgICBjb25zb2xlLmVycm9yKFwiZXJyb3JzXCIpO1xufSJ9)

```
/*eslint no-unused-vars: ["error", { "caughtErrors": "none" }]*/

try {
    //...
} catch (err) {
    console.error("errors");
}
1
2
3
4
5
6
7
```

### caughtErrorsIgnorePattern

The `caughtErrorsIgnorePattern` option specifies exceptions not to check for usage: catch arguments whose names match a regexp pattern. For example, variables whose names begin with a string ‘ignore’.

Examples of correct code for the `{ "caughtErrorsIgnorePattern": "^ignore" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJjYXVnaHRFcnJvcnNcIjogXCJhbGxcIiwgXCJjYXVnaHRFcnJvcnNJZ25vcmVQYXR0ZXJuXCI6IFwiXmlnbm9yZVwiIH1dKi9cblxudHJ5IHtcbiAgICAvLy4uLlxufSBjYXRjaCAoaWdub3JlRXJyKSB7XG4gICAgY29uc29sZS5lcnJvcihcImVycm9yc1wiKTtcbn0ifQ==)

```
/*eslint no-unused-vars: ["error", { "caughtErrors": "all", "caughtErrorsIgnorePattern": "^ignore" }]*/

try {
    //...
} catch (ignoreErr) {
    console.error("errors");
}
1
2
3
4
5
6
7
```

### destructuredArrayIgnorePattern

The `destructuredArrayIgnorePattern` option specifies exceptions not to check for usage: elements of array destructuring patterns whose names match a regexp pattern. For example, variables whose names begin with an underscore.

Examples of correct code for the `{ "destructuredArrayIgnorePattern": "^_" }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJkZXN0cnVjdHVyZWRBcnJheUlnbm9yZVBhdHRlcm5cIjogXCJeX1wiIH1dKi9cblxuY29uc3QgW2EsIF9iLCBjXSA9IFtcImFcIiwgXCJiXCIsIFwiY1wiXTtcbmNvbnNvbGUubG9nKGErYyk7XG5cbmNvbnN0IHsgeDogW19hLCBmb29dIH0gPSBiYXI7XG5jb25zb2xlLmxvZyhmb28pO1xuXG5mdW5jdGlvbiBiYXooW19jLCB4XSkge1xuICAgIHg7XG59XG5iYXooKTtcblxuZnVuY3Rpb24gdGVzdCh7cDogW19xLCByXX0pIHtcbiAgICByO1xufVxudGVzdCgpO1xuXG5sZXQgX20sIG47XG5mb28uZm9yRWFjaChpdGVtID0+IHtcbiAgICBbX20sIG5dID0gaXRlbTtcbiAgICBjb25zb2xlLmxvZyhuKTtcbn0pO1xuXG5sZXQgX28sIHA7XG5fbyA9IDE7XG5bX28sIHBdID0gZm9vO1xucDsifQ==)

```
/*eslint no-unused-vars: ["error", { "destructuredArrayIgnorePattern": "^_" }]*/

const [a, _b, c] = ["a", "b", "c"];
console.log(a+c);

const { x: [_a, foo] } = bar;
console.log(foo);

function baz([_c, x]) {
    x;
}
baz();

function test({p: [_q, r]}) {
    r;
}
test();

let _m, n;
foo.forEach(item => {
    [_m, n] = item;
    console.log(n);
});

let _o, p;
_o = 1;
[_o, p] = foo;
p;
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
```

### ignoreRestSiblings

The `ignoreRestSiblings` option is a boolean (default: `false`). Using a [Rest Property](https://github.com/tc39/proposal-object-rest-spread) it is possible to “omit” properties from an object, but by default the sibling properties are marked as “unused”. With this option enabled the rest property’s siblings are ignored.

Examples of correct code for the `{ "ignoreRestSiblings": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVSZXN0U2libGluZ3NcIjogdHJ1ZSB9XSovXG5cbi8vICdmb28nIGFuZCAnYmFyJyB3ZXJlIGlnbm9yZWQgYmVjYXVzZSB0aGV5IGhhdmUgYSByZXN0IHByb3BlcnR5IHNpYmxpbmcuXG5jb25zdCB7IGZvbywgLi4ucmVzdCB9ID0gZGF0YTtcbmNvbnNvbGUubG9nKHJlc3QpO1xuXG4vLyBPUlxuXG5sZXQgYmFyO1xuKHsgYmFyLCAuLi5yZXN0IH0gPSBkYXRhKTsifQ==)

```
/*eslint no-unused-vars: ["error", { "ignoreRestSiblings": true }]*/

// 'foo' and 'bar' were ignored because they have a rest property sibling.
const { foo, ...rest } = data;
console.log(rest);

// OR

let bar;
({ bar, ...rest } = data);
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

### ignoreClassWithStaticInitBlock

The `ignoreClassWithStaticInitBlock` option is a boolean (default: `false`). Static initialization blocks allow you to initialize static variables and execute code during the evaluation of a class definition, meaning the static block code is executed without creating a new instance of the class. When set to `true`, this option ignores classes containing static initialization blocks.

Examples of incorrect code for the `{ "ignoreClassWithStaticInitBlock": true }` option

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVDbGFzc1dpdGhTdGF0aWNJbml0QmxvY2tcIjogdHJ1ZSB9XSovXG5cbmNsYXNzIEZvbyB7XG4gICAgc3RhdGljIG15UHJvcGVydHkgPSBcInNvbWUgc3RyaW5nXCI7XG4gICAgc3RhdGljIG15bWV0aG9kKCkge1xuICAgICAgICByZXR1cm4gXCJzb21lIHN0cmluZ1wiO1xuICAgIH1cbn1cblxuY2xhc3MgQmFyIHtcbiAgICBzdGF0aWMge1xuICAgICAgICBsZXQgYmF6OyAvLyB1bnVzZWQgdmFyaWFibGVcbiAgICB9XG59In0=)

```
/*eslint no-unused-vars: ["error", { "ignoreClassWithStaticInitBlock": true }]*/

class Foo {
    static myProperty = "some string";
    static mymethod() {
        return "some string";
    }
}

class Bar {
    static {
        let baz; // unused variable
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
```

Examples of correct code for the `{ "ignoreClassWithStaticInitBlock": true }` option

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVDbGFzc1dpdGhTdGF0aWNJbml0QmxvY2tcIjogdHJ1ZSB9XSovXG5cbmNsYXNzIEZvbyB7XG4gICAgc3RhdGljIHtcbiAgICAgICAgbGV0IGJhciA9IFwic29tZSBzdHJpbmdcIjtcblxuICAgICAgICBjb25zb2xlLmxvZyhiYXIpO1xuICAgIH1cbn0ifQ==)

```
/*eslint no-unused-vars: ["error", { "ignoreClassWithStaticInitBlock": true }]*/

class Foo {
    static {
        let bar = "some string";

        console.log(bar);
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
```

### ignoreUsingDeclarations

The `ignoreUsingDeclarations` option is a boolean (default: `false`). Explicit resource management allows automatic teardown of disposables by calling `Symbol.dispose` or `Symbol.asyncDispose` method implicitly at the end of the variable’s scope. When this option is set to `true`, this rule ignores variables declared with `using` or `await using`.

Examples of incorrect code for the `{ "ignoreUsingDeclarations": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVVc2luZ0RlY2xhcmF0aW9uc1wiOiB0cnVlIH1dKi9cbmNvbnN0IHJlc291cmNlID0gZ2V0UmVzb3VyY2UoKTsifQ==)

```
/*eslint no-unused-vars: ["error", { "ignoreUsingDeclarations": true }]*/
const resource = getResource();
1
2
```

Examples of correct code for the `{ "ignoreUsingDeclarations": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJpZ25vcmVVc2luZ0RlY2xhcmF0aW9uc1wiOiB0cnVlIH1dKi9cblxudXNpbmcgc3luY1Jlc291cmNlID0gZ2V0U3luY1Jlc291cmNlKCk7XG5hd2FpdCB1c2luZyBhc3luY1Jlc291cmNlID0gZ2V0QXN5bmNSZXNvdXJjZSgpOyJ9)

```
/*eslint no-unused-vars: ["error", { "ignoreUsingDeclarations": true }]*/

using syncResource = getSyncResource();
await using asyncResource = getAsyncResource();
1
2
3
4
```

### reportUsedIgnorePattern

The `reportUsedIgnorePattern` option is a boolean (default: `false`). Using this option will report variables that match any of the valid ignore pattern options (`varsIgnorePattern`, `argsIgnorePattern`, `caughtErrorsIgnorePattern`, or `destructuredArrayIgnorePattern`) if they have been used.

Examples of incorrect code for the `{ "reportUsedIgnorePattern": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRVc2VkSWdub3JlUGF0dGVyblwiOiB0cnVlLCBcInZhcnNJZ25vcmVQYXR0ZXJuXCI6IFwiW2lJXWdub3JlZFwiIH1dKi9cblxuY29uc3QgZmlyc3RWYXJJZ25vcmVkID0gMTtcbmNvbnN0IHNlY29uZFZhciA9IDI7XG5jb25zb2xlLmxvZyhmaXJzdFZhcklnbm9yZWQsIHNlY29uZFZhcik7In0=)

```
/*eslint no-unused-vars: ["error", { "reportUsedIgnorePattern": true, "varsIgnorePattern": "[iI]gnored" }]*/

const firstVarIgnored = 1;
const secondVar = 2;
console.log(firstVarIgnored, secondVar);
1
2
3
4
5
```

Examples of correct code for the `{ "reportUsedIgnorePattern": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLXZhcnM6IFtcImVycm9yXCIsIHsgXCJyZXBvcnRVc2VkSWdub3JlUGF0dGVyblwiOiB0cnVlLCBcInZhcnNJZ25vcmVQYXR0ZXJuXCI6IFwiW2lJXWdub3JlZFwiIH1dKi9cblxuY29uc3QgZmlyc3RWYXIgPSAxO1xuY29uc3Qgc2Vjb25kVmFyID0gMjtcbmNvbnNvbGUubG9nKGZpcnN0VmFyLCBzZWNvbmRWYXIpOyJ9)

```
/*eslint no-unused-vars: ["error", { "reportUsedIgnorePattern": true, "varsIgnorePattern": "[iI]gnored" }]*/

const firstVar = 1;
const secondVar = 2;
console.log(firstVar, secondVar);
1
2
3
4
5
```

## When Not To Use It

If you don’t want to be notified about unused variables or function arguments, you can safely turn this rule off.

## Related Rules

- [no-unassigned-vars](/docs/latest/rules/no-unassigned-vars)
- [no-useless-assignment](/docs/latest/rules/no-useless-assignment)

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unused-vars.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unused-vars.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unused-vars.md
                    
                
                )
