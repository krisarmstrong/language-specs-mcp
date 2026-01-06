# no-empty-function

Disallow empty functions

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allow: functions](#allow-functions)
  2. [allow: arrowFunctions](#allow-arrowfunctions)
  3. [allow: generatorFunctions](#allow-generatorfunctions)
  4. [allow: methods](#allow-methods)
  5. [allow: generatorMethods](#allow-generatormethods)
  6. [allow: getters](#allow-getters)
  7. [allow: setters](#allow-setters)
  8. [allow: constructors](#allow-constructors)
  9. [allow: asyncFunctions](#allow-asyncfunctions)
  10. [allow: asyncMethods](#allow-asyncmethods)
  11. [allow: privateConstructors](#allow-privateconstructors)
  12. [allow: protectedConstructors](#allow-protectedconstructors)
  13. [allow: decoratedFunctions](#allow-decoratedfunctions)
  14. [allow: overrideMethods](#allow-overridemethods)

3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

Empty functions can reduce readability because readers need to guess whether it’s intentional or not. So writing a clear comment for empty functions is a good practice.

```
function foo() {
    // do nothing.
}
1
2
3
```

Copy code to clipboard

Especially, the empty block of arrow functions might be confusing developers. It’s very similar to an empty object literal.

```
list.map(() => {});   // This is a block, would return undefined.
list.map(() => ({})); // This is an empty object.
1
2
```

Copy code to clipboard

## Rule Details

This rule is aimed at eliminating empty functions. A function will not be considered a problem if it contains a comment.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbygpIHt9XG5cbmNvbnN0IGJhciA9IGZ1bmN0aW9uKCkge307XG5cbmNvbnN0IGJhcjEgPSAoKSA9PiB7fTtcblxuZnVuY3Rpb24qIGJheigpIHt9XG5cbmNvbnN0IGJhcjIgPSBmdW5jdGlvbiooKSB7fTtcblxuY29uc3Qgb2JqID0ge1xuICAgIGZvbzogZnVuY3Rpb24oKSB7fSxcblxuICAgIGZvbzogZnVuY3Rpb24qKCkge30sXG5cbiAgICBmb28oKSB7fSxcblxuICAgICpmb28oKSB7fSxcblxuICAgIGdldCBmb28oKSB7fSxcblxuICAgIHNldCBmb28odmFsdWUpIHt9XG59O1xuXG5jbGFzcyBBIHtcbiAgICBjb25zdHJ1Y3RvcigpIHt9XG5cbiAgICBmb28oKSB7fVxuXG4gICAgKmZvbygpIHt9XG5cbiAgICBnZXQgZm9vKCkge31cblxuICAgIHNldCBmb28odmFsdWUpIHt9XG5cbiAgICBzdGF0aWMgZm9vKCkge31cblxuICAgIHN0YXRpYyAqZm9vKCkge31cblxuICAgIHN0YXRpYyBnZXQgZm9vKCkge31cblxuICAgIHN0YXRpYyBzZXQgZm9vKHZhbHVlKSB7fVxufSJ9)

```
/*eslint no-empty-function: "error"*/

function foo() {}

const bar = function() {};

const bar1 = () => {};

function* baz() {}

const bar2 = function*() {};

const obj = {
    foo: function() {},

    foo: function*() {},

    foo() {},

    *foo() {},

    get foo() {},

    set foo(value) {}
};

class A {
    constructor() {}

    foo() {}

    *foo() {}

    get foo() {}

    set foo(value) {}

    static foo() {}

    static *foo() {}

    static get foo() {}

    static set foo(value) {}
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICAvLyBkbyBub3RoaW5nLlxufVxuXG5jb25zdCBiYXogPSBmdW5jdGlvbigpIHtcbiAgICAvLyBhbnkgY2xlYXIgY29tbWVudHMuXG59O1xuXG5jb25zdCBiYXoxID0gKCkgPT4ge1xuICAgIGJhcigpO1xufTtcblxuZnVuY3Rpb24qIGZvb2JhcigpIHtcbiAgICAvLyBkbyBub3RoaW5nLlxufVxuXG5jb25zdCBiYXoyID0gZnVuY3Rpb24qKCkge1xuICAgIC8vIGRvIG5vdGhpbmcuXG59O1xuXG5jb25zdCBvYmogPSB7XG4gICAgZm9vOiBmdW5jdGlvbigpIHtcbiAgICAgICAgLy8gZG8gbm90aGluZy5cbiAgICB9LFxuXG4gICAgZm9vOiBmdW5jdGlvbiooKSB7XG4gICAgICAgIC8vIGRvIG5vdGhpbmcuXG4gICAgfSxcblxuICAgIGZvbygpIHtcbiAgICAgICAgLy8gZG8gbm90aGluZy5cbiAgICB9LFxuXG4gICAgKmZvbygpIHtcbiAgICAgICAgLy8gZG8gbm90aGluZy5cbiAgICB9LFxuXG4gICAgZ2V0IGZvbygpIHtcbiAgICAgICAgLy8gZG8gbm90aGluZy5cbiAgICB9LFxuXG4gICAgc2V0IGZvbyh2YWx1ZSkge1xuICAgICAgICAvLyBkbyBub3RoaW5nLlxuICAgIH1cbn07XG5cbmNsYXNzIEEge1xuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICAvLyBkbyBub3RoaW5nLlxuICAgIH1cblxuICAgIGZvbygpIHtcbiAgICAgICAgLy8gZG8gbm90aGluZy5cbiAgICB9XG5cbiAgICAqZm9vKCkge1xuICAgICAgICAvLyBkbyBub3RoaW5nLlxuICAgIH1cblxuICAgIGdldCBmb28oKSB7XG4gICAgICAgIC8vIGRvIG5vdGhpbmcuXG4gICAgfVxuXG4gICAgc2V0IGZvbyh2YWx1ZSkge1xuICAgICAgICAvLyBkbyBub3RoaW5nLlxuICAgIH1cblxuICAgIHN0YXRpYyBmb28oKSB7XG4gICAgICAgIC8vIGRvIG5vdGhpbmcuXG4gICAgfVxuXG4gICAgc3RhdGljICpmb28oKSB7XG4gICAgICAgIC8vIGRvIG5vdGhpbmcuXG4gICAgfVxuXG4gICAgc3RhdGljIGdldCBmb28oKSB7XG4gICAgICAgIC8vIGRvIG5vdGhpbmcuXG4gICAgfVxuXG4gICAgc3RhdGljIHNldCBmb28odmFsdWUpIHtcbiAgICAgICAgLy8gZG8gbm90aGluZy5cbiAgICB9XG59In0=)

```
/*eslint no-empty-function: "error"*/

function foo() {
    // do nothing.
}

const baz = function() {
    // any clear comments.
};

const baz1 = () => {
    bar();
};

function* foobar() {
    // do nothing.
}

const baz2 = function*() {
    // do nothing.
};

const obj = {
    foo: function() {
        // do nothing.
    },

    foo: function*() {
        // do nothing.
    },

    foo() {
        // do nothing.
    },

    *foo() {
        // do nothing.
    },

    get foo() {
        // do nothing.
    },

    set foo(value) {
        // do nothing.
    }
};

class A {
    constructor() {
        // do nothing.
    }

    foo() {
        // do nothing.
    }

    *foo() {
        // do nothing.
    }

    get foo() {
        // do nothing.
    }

    set foo(value) {
        // do nothing.
    }

    static foo() {
        // do nothing.
    }

    static *foo() {
        // do nothing.
    }

    static get foo() {
        // do nothing.
    }

    static set foo(value) {
        // do nothing.
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
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
```

## Options

This rule has an option to allow specific kinds of functions to be empty.

- `allow` (`string[]`) - A list of kind to allow empty functions. List items are some of the following strings. An empty array (`[]`) by default. 

  - `"functions"` - Normal functions.
  - `"arrowFunctions"` - Arrow functions.
  - `"generatorFunctions"` - Generator functions.
  - `"methods"` - Class methods and method shorthands of object literals.
  - `"generatorMethods"` - Class methods and method shorthands of object literals with generator.
  - `"getters"` - Getters.
  - `"setters"` - Setters.
  - `"constructors"` - Class constructors.
  - `"asyncFunctions"` - Async functions.
  - `"asyncMethods"` - Async class methods and method shorthands of object literals.
  - `"privateConstructors"` - Private class constructors. (TypeScript only)
  - `"protectedConstructors"` - Protected class constructors. (TypeScript only)
  - `"decoratedFunctions"` - Class methods with decorators. (TypeScript only)
  - `"overrideMethods"` - Methods that use the override keyword. (TypeScript only)

### allow: functions

Examples of correct code for the `{ "allow": ["functions"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJmdW5jdGlvbnNcIl0gfV0qL1xuXG5mdW5jdGlvbiBmb28oKSB7fVxuXG5jb25zdCBiYXIgPSBmdW5jdGlvbigpIHt9O1xuXG5jb25zdCBvYmogPSB7XG4gICAgZm9vOiBmdW5jdGlvbigpIHt9XG59OyJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["functions"] }]*/

function foo() {}

const bar = function() {};

const obj = {
    foo: function() {}
};
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

### allow: arrowFunctions

Examples of correct code for the `{ "allow": ["arrowFunctions"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJhcnJvd0Z1bmN0aW9uc1wiXSB9XSovXG5cbmNvbnN0IGZvbyA9ICgpID0+IHt9OyJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["arrowFunctions"] }]*/

const foo = () => {};
1
2
3
```

### allow: generatorFunctions

Examples of correct code for the `{ "allow": ["generatorFunctions"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJnZW5lcmF0b3JGdW5jdGlvbnNcIl0gfV0qL1xuXG5mdW5jdGlvbiogZm9vKCkge31cblxuY29uc3QgYmFyID0gZnVuY3Rpb24qKCkge307XG5cbmNvbnN0IG9iaiA9IHtcbiAgICBmb286IGZ1bmN0aW9uKigpIHt9XG59OyJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["generatorFunctions"] }]*/

function* foo() {}

const bar = function*() {};

const obj = {
    foo: function*() {}
};
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

### allow: methods

Examples of correct code for the `{ "allow": ["methods"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJtZXRob2RzXCJdIH1dKi9cblxuY29uc3Qgb2JqID0ge1xuICAgIGZvbygpIHt9XG59O1xuXG5jbGFzcyBBIHtcbiAgICBmb28oKSB7fVxuICAgIHN0YXRpYyBmb28oKSB7fVxufSJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["methods"] }]*/

const obj = {
    foo() {}
};

class A {
    foo() {}
    static foo() {}
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
```

### allow: generatorMethods

Examples of correct code for the `{ "allow": ["generatorMethods"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJnZW5lcmF0b3JNZXRob2RzXCJdIH1dKi9cblxuY29uc3Qgb2JqID0ge1xuICAgICpmb28oKSB7fVxufTtcblxuY2xhc3MgQSB7XG4gICAgKmZvbygpIHt9XG4gICAgc3RhdGljICpmb28oKSB7fVxufSJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["generatorMethods"] }]*/

const obj = {
    *foo() {}
};

class A {
    *foo() {}
    static *foo() {}
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
```

### allow: getters

Examples of correct code for the `{ "allow": ["getters"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJnZXR0ZXJzXCJdIH1dKi9cblxuY29uc3Qgb2JqID0ge1xuICAgIGdldCBmb28oKSB7fVxufTtcblxuY2xhc3MgQSB7XG4gICAgZ2V0IGZvbygpIHt9XG4gICAgc3RhdGljIGdldCBmb28oKSB7fVxufSJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["getters"] }]*/

const obj = {
    get foo() {}
};

class A {
    get foo() {}
    static get foo() {}
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
```

### allow: setters

Examples of correct code for the `{ "allow": ["setters"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJzZXR0ZXJzXCJdIH1dKi9cblxuY29uc3Qgb2JqID0ge1xuICAgIHNldCBmb28odmFsdWUpIHt9XG59O1xuXG5jbGFzcyBBIHtcbiAgICBzZXQgZm9vKHZhbHVlKSB7fVxuICAgIHN0YXRpYyBzZXQgZm9vKHZhbHVlKSB7fVxufSJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["setters"] }]*/

const obj = {
    set foo(value) {}
};

class A {
    set foo(value) {}
    static set foo(value) {}
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
```

### allow: constructors

Examples of correct code for the `{ "allow": ["constructors"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJjb25zdHJ1Y3RvcnNcIl0gfV0qL1xuXG5jbGFzcyBBIHtcbiAgICBjb25zdHJ1Y3RvcigpIHt9XG59In0=)

```
/*eslint no-empty-function: ["error", { "allow": ["constructors"] }]*/

class A {
    constructor() {}
}
1
2
3
4
5
```

### allow: asyncFunctions

Examples of correct code for the `{ "allow": ["asyncFunctions"] }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJhc3luY0Z1bmN0aW9uc1wiXSB9XSovXG5cbmFzeW5jIGZ1bmN0aW9uIGEoKXt9In0=)

```
/*eslint no-empty-function: ["error", { "allow": ["asyncFunctions"] }]*/

async function a(){}
1
2
3
```

### allow: asyncMethods

Examples of correct code for the `{ "allow": ["asyncMethods"] }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZW1wdHktZnVuY3Rpb246IFtcImVycm9yXCIsIHsgXCJhbGxvd1wiOiBbXCJhc3luY01ldGhvZHNcIl0gfV0qL1xuXG5jb25zdCBvYmogPSB7XG4gICAgYXN5bmMgZm9vKCkge31cbn07XG5cbmNsYXNzIEEge1xuICAgIGFzeW5jIGZvbygpIHt9XG4gICAgc3RhdGljIGFzeW5jIGZvbygpIHt9XG59In0=)

```
/*eslint no-empty-function: ["error", { "allow": ["asyncMethods"] }]*/

const obj = {
    async foo() {}
};

class A {
    async foo() {}
    static async foo() {}
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
```

### allow: privateConstructors

Examples of correct TypeScript code for the `{ "allow": ["privateConstructors"] }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1lbXB0eS1mdW5jdGlvbjogW1wiZXJyb3JcIiwgeyBcImFsbG93XCI6IFtcInByaXZhdGVDb25zdHJ1Y3RvcnNcIl0gfV0qL1xuXG5jbGFzcyBBIHtcbiAgICBwcml2YXRlIGNvbnN0cnVjdG9yKCkge31cbn0ifQ==)

```
/*eslint no-empty-function: ["error", { "allow": ["privateConstructors"] }]*/

class A {
    private constructor() {}
}
1
2
3
4
5
```

### allow: protectedConstructors

Examples of correct TypeScript code for the `{ "allow": ["protectedConstructors"] }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1lbXB0eS1mdW5jdGlvbjogW1wiZXJyb3JcIiwgeyBcImFsbG93XCI6IFtcInByb3RlY3RlZENvbnN0cnVjdG9yc1wiXSB9XSovXG5cbmNsYXNzIEEge1xuICAgIHByb3RlY3RlZCBjb25zdHJ1Y3RvcigpIHt9XG59In0=)

```
/*eslint no-empty-function: ["error", { "allow": ["protectedConstructors"] }]*/

class A {
    protected constructor() {}
}
1
2
3
4
5
```

### allow: decoratedFunctions

Examples of correct TypeScript code for the `{ "allow": ["decoratedFunctions"] }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1lbXB0eS1mdW5jdGlvbjogW1wiZXJyb3JcIiwgeyBcImFsbG93XCI6IFtcImRlY29yYXRlZEZ1bmN0aW9uc1wiXSB9XSovXG5cbmNsYXNzIEEge1xuICAgIEBkZWNvcmF0b3JcbiAgICBmb28oKSB7fVxufSJ9)

```
/*eslint no-empty-function: ["error", { "allow": ["decoratedFunctions"] }]*/

class A {
    @decorator
    foo() {}
}
1
2
3
4
5
6
```

### allow: overrideMethods

Examples of correct TypeScript code for the `{ "allow": ["overrideMethods"] }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1lbXB0eS1mdW5jdGlvbjogW1wiZXJyb3JcIiwgeyBcImFsbG93XCI6IFtcIm92ZXJyaWRlTWV0aG9kc1wiXSB9XSovXG5cbmFic3RyYWN0IGNsYXNzIEJhc2Uge1xuICAgIGFic3RyYWN0IG1ldGhvZCgpOiB2b2lkO1xufVxuXG5jbGFzcyBEZXJpdmVkIGV4dGVuZHMgQmFzZSB7XG4gICAgb3ZlcnJpZGUgbWV0aG9kKCkge31cbn0ifQ==)

```
/*eslint no-empty-function: ["error", { "allow": ["overrideMethods"] }]*/

abstract class Base {
    abstract method(): void;
}

class Derived extends Base {
    override method() {}
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

## When Not To Use It

If you don’t want to be notified about empty functions, then it’s safe to disable this rule.

## Related Rules

- [no-empty](/docs/latest/rules/no-empty)

## Version

This rule was introduced in ESLint v2.0.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-empty-function.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-empty-function.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-empty-function.md
                    
                
                )
