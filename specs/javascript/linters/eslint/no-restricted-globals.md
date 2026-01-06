# no-restricted-globals

Disallow specified global variables

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [globals](#globals)
  2. [checkGlobalObject](#checkglobalobject)
  3. [globalObjects](#globalobjects)

3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Disallowing usage of specific global variables can be useful if you want to allow a set of global variables, but still want to disallow some of those.

For instance, early Internet Explorer versions exposed the current DOM event as a global variable `event`, but using this variable has been considered as a bad practice for a long time. Restricting this will make sure this variable isn’t used in browser code.

## Rule Details

This rule allows you to specify global variable names that you don’t want to use in your application.

## Options

This rule has both string and object options to specify the global variables to restrict.

Using the string option, you can specify the name of a global variable that you want to restrict as a value in the rule options array:

```
{
    "rules": {
        "no-restricted-globals": ["error", "event", "fdescribe"]
    }
}
1
2
3
4
5
```

Copy code to clipboard

Alternatively, the rule also accepts objects, where the global name and an optional custom message are specified:

```
{
    "rules": {
        "no-restricted-globals": [
            "error",
            {
                "name": "event",
                "message": "Use local parameter instead."
            },
            {
                "name": "fdescribe",
                "message": "Do not commit fdescribe. Use describe instead."
            }
        ]
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
```

Copy code to clipboard

Examples of incorrect code for sample `"event", "fdescribe"` global variable names:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZXZlbnQsIGZkZXNjcmliZSovXG4vKmVzbGludCBuby1yZXN0cmljdGVkLWdsb2JhbHM6IFtcImVycm9yXCIsIFwiZXZlbnRcIiwgXCJmZGVzY3JpYmVcIl0qL1xuXG5mdW5jdGlvbiBvbkNsaWNrKCkge1xuICAgIGNvbnNvbGUubG9nKGV2ZW50KTtcbn1cblxuZmRlc2NyaWJlKFwiZm9vXCIsIGZ1bmN0aW9uKCkge1xufSk7In0=)

```
/*global event, fdescribe*/
/*eslint no-restricted-globals: ["error", "event", "fdescribe"]*/

function onClick() {
    console.log(event);
}

fdescribe("foo", function() {
});
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

Examples of correct code for a sample `"event"` global variable name:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZXZlbnQqL1xuLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1nbG9iYWxzOiBbXCJlcnJvclwiLCBcImV2ZW50XCJdKi9cblxuaW1wb3J0IGV2ZW50IGZyb20gXCJldmVudC1tb2R1bGVcIjsifQ==)

```
/*global event*/
/*eslint no-restricted-globals: ["error", "event"]*/

import event from "event-module";
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZXZlbnQqL1xuLyplc2xpbnQgbm8tcmVzdHJpY3RlZC1nbG9iYWxzOiBbXCJlcnJvclwiLCBcImV2ZW50XCJdKi9cblxuY29uc3QgZXZlbnQgPSAxOyJ9)

```
/*global event*/
/*eslint no-restricted-globals: ["error", "event"]*/

const event = 1;
1
2
3
4
```

Examples of incorrect code for a sample `"event"` global variable name, along with a custom error message:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZXZlbnQqL1xuLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtZ2xvYmFsczogW1wiZXJyb3JcIiwgeyBuYW1lOiBcImV2ZW50XCIsIG1lc3NhZ2U6IFwiVXNlIGxvY2FsIHBhcmFtZXRlciBpbnN0ZWFkLlwiIH1dICovXG5cbmZ1bmN0aW9uIG9uQ2xpY2soKSB7XG4gICAgY29uc29sZS5sb2coZXZlbnQpOyAgICAvLyBVbmV4cGVjdGVkIGdsb2JhbCB2YXJpYWJsZSAnZXZlbnQnLiBVc2UgbG9jYWwgcGFyYW1ldGVyIGluc3RlYWQuXG59In0=)

```
/*global event*/
/* eslint no-restricted-globals: ["error", { name: "event", message: "Use local parameter instead." }] */

function onClick() {
    console.log(event);    // Unexpected global variable 'event'. Use local parameter instead.
}
1
2
3
4
5
6
```

### globals

An object option whose value is an array containing the names of the globals you want to restrict.

Examples of incorrect code for `"event"` and `"fdescribe"` global variable names:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZXZlbnQsIGZkZXNjcmliZSovXG4vKmVzbGludCBuby1yZXN0cmljdGVkLWdsb2JhbHM6IFtcImVycm9yXCIsIHsgZ2xvYmFsczogW1wiZXZlbnRcIiwgXCJmZGVzY3JpYmVcIl0gfV0qL1xuXG5mdW5jdGlvbiBvbkNsaWNrKCkge1xuICAgIGNvbnNvbGUubG9nKGV2ZW50KTtcbn1cblxuZmRlc2NyaWJlKFwiZm9vXCIsIGZ1bmN0aW9uKCkge1xufSk7In0=)

```
/*global event, fdescribe*/
/*eslint no-restricted-globals: ["error", { globals: ["event", "fdescribe"] }]*/

function onClick() {
    console.log(event);
}

fdescribe("foo", function() {
});
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

Custom messages for a particular global can also be specified in `globals` array using objects with `name` and `message`:

Examples of incorrect code for an `"event"` global variable name, along with a custom error message:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZXZlbnQqL1xuLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtZ2xvYmFsczogW1wiZXJyb3JcIiwgeyBnbG9iYWxzOiBbeyBuYW1lOiBcImV2ZW50XCIsIG1lc3NhZ2U6IFwiVXNlIGxvY2FsIHBhcmFtZXRlciBpbnN0ZWFkLlwiIH1dIH1dICovXG5cbmZ1bmN0aW9uIG9uQ2xpY2soKSB7XG4gICAgY29uc29sZS5sb2coZXZlbnQpO1xufSJ9)

```
/*global event*/
/* eslint no-restricted-globals: ["error", { globals: [{ name: "event", message: "Use local parameter instead." }] }] */

function onClick() {
    console.log(event);
}
1
2
3
4
5
6
```

### checkGlobalObject

A boolean option that enables detection of restricted globals accessed via global objects. Default is `false`.

Examples of incorrect code for `checkGlobalObject: true` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZ2xvYmFsVGhpcywgc2VsZiwgd2luZG93Ki9cbi8qZXNsaW50IG5vLXJlc3RyaWN0ZWQtZ2xvYmFsczogW1wiZXJyb3JcIiwgeyBnbG9iYWxzOiBbXCJQcm9taXNlXCJdLCBjaGVja0dsb2JhbE9iamVjdDogdHJ1ZSB9XSovXG5cbmdsb2JhbFRoaXMuUHJvbWlzZVxuc2VsZi5Qcm9taXNlXG53aW5kb3cuUHJvbWlzZSJ9)

```
/*global globalThis, self, window*/
/*eslint no-restricted-globals: ["error", { globals: ["Promise"], checkGlobalObject: true }]*/

globalThis.Promise
self.Promise
window.Promise
1
2
3
4
5
6
```

### globalObjects

An array option that specifies additional global object names to check when `checkGlobalObject` is enabled. By default, the rule checks these global objects: `globalThis`, `self`, and `window`.

Examples of incorrect code for `globalObjects` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLypnbG9iYWwgZ2xvYmFsVGhpcywgc2VsZiwgd2luZG93LCBteUdsb2JhbCovXG4vKmVzbGludCBuby1yZXN0cmljdGVkLWdsb2JhbHM6IFtcImVycm9yXCIsIHtcbiAgICBnbG9iYWxzOiBbXCJQcm9taXNlXCJdLFxuICAgIGNoZWNrR2xvYmFsT2JqZWN0OiB0cnVlLFxuICAgIGdsb2JhbE9iamVjdHM6IFtcIm15R2xvYmFsXCJdXG59XSovXG5cbmdsb2JhbFRoaXMuUHJvbWlzZVxuc2VsZi5Qcm9taXNlXG53aW5kb3cuUHJvbWlzZVxubXlHbG9iYWwuUHJvbWlzZTsifQ==)

```
/*global globalThis, self, window, myGlobal*/
/*eslint no-restricted-globals: ["error", {
    globals: ["Promise"],
    checkGlobalObject: true,
    globalObjects: ["myGlobal"]
}]*/

globalThis.Promise
self.Promise
window.Promise
myGlobal.Promise;
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

Restricted globals used in TypeScript type annotations—such as type references, interface inheritance, or class implementations—are ignored by this rule.

Examples of correct TypeScript code for “Promise”, “Event”, and “Window” global variable names:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1yZXN0cmljdGVkLWdsb2JhbHM6IFtcImVycm9yXCIsIFwiUHJvbWlzZVwiLCBcIkV2ZW50XCIsIFwiV2luZG93XCJdKi9cblxuY29uc3QgZmV0Y2hEYXRhOiBQcm9taXNlPHN0cmluZz4gPSBmZXRjaFN0cmluZygpO1xuXG5pbnRlcmZhY2UgQ3VzdG9tRXZlbnQgZXh0ZW5kcyBFdmVudCB7fVxuXG5jbGFzcyBDdXN0b21XaW5kb3cgaW1wbGVtZW50cyBXaW5kb3cge31cblxuZnVuY3Rpb24gaGFuZGxlQ2xpY2soZXZlbnQ6IEV2ZW50KSB7XG4gIGNvbnNvbGUubG9nKGV2ZW50KTtcbn0ifQ==)

```
/*eslint no-restricted-globals: ["error", "Promise", "Event", "Window"]*/

const fetchData: Promise<string> = fetchString();

interface CustomEvent extends Event {}

class CustomWindow implements Window {}

function handleClick(event: Event) {
  console.log(event);
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

## Related Rules

- [no-restricted-properties](/docs/latest/rules/no-restricted-properties)
- [no-restricted-syntax](/docs/latest/rules/no-restricted-syntax)

## Version

This rule was introduced in ESLint v2.3.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-restricted-globals.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-restricted-globals.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-restricted-globals.md
                    
                
                )
