# no-invalid-this

Disallow use of `this` in contexts where the value of `this` is `undefined`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [capIsConstructor](#capisconstructor)

3. [When Not To Use It](#when-not-to-use-it)
4. [Handled by TypeScript](#handled_by_typescript)
5. [Version](#version)
6. [Resources](#resources)

Under the strict mode, `this` keywords outside of classes or class-like objects might be `undefined` and raise a `TypeError`.

## Rule Details

This rule aims to flag usage of `this` keywords in contexts where the value of `this` is `undefined`.

Top-level `this` in scripts is always considered valid because it refers to the global object regardless of the strict mode.

Top-level `this` in ECMAScript modules is always considered invalid because its value is `undefined`.

For `this` inside functions, this rule basically checks whether or not the function containing `this` keyword is a constructor or a method. Note that arrow functions have lexical `this`, and that therefore this rule checks their enclosing contexts.

This rule judges from following conditions whether or not the function is a constructor:

- The name of the function starts with uppercase.
- The function is assigned to a variable which starts with an uppercase letter.
- The function is a constructor of ES2015 Classes.

This rule judges from following conditions whether or not the function is a method:

- The function is on an object literal.
- The function is assigned to a property.
- The function is a method/getter/setter of ES2015 Classes.

And this rule allows `this` keywords in functions below:

- The `call/apply/bind` method of the function is called directly.
- The function is a callback of array methods (such as `.forEach()`) if `thisArg` is given.
- The function has `@this` tag in its JSDoc comment.

And this rule always allows `this` keywords in the following contexts:

- At the top level of scripts.
- In class field initializers.
- In class static blocks.

Otherwise are considered problems.

This rule applies only in strict mode. With `"parserOptions": { "sourceType": "module" }` in the ESLint configuration, your code is in strict mode even without a `"use strict"` directive.

Examples of incorrect code for this rule in strict mode:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC10aGlzOiBcImVycm9yXCIqL1xuXG5cInVzZSBzdHJpY3RcIjtcblxuKGZ1bmN0aW9uKCkge1xuICAgIHRoaXMuYSA9IDA7XG4gICAgYmF6KCgpID0+IHRoaXMpO1xufSkoKTtcblxuZnVuY3Rpb24gZm9vKCkge1xuICAgIHRoaXMuYSA9IDA7XG4gICAgYmF6KCgpID0+IHRoaXMpO1xufVxuXG5jb25zdCBiYXIgPSBmdW5jdGlvbigpIHtcbiAgICB0aGlzLmEgPSAwO1xuICAgIGJheigoKSA9PiB0aGlzKTtcbn07XG5cbmZvbyhmdW5jdGlvbigpIHtcbiAgICB0aGlzLmEgPSAwO1xuICAgIGJheigoKSA9PiB0aGlzKTtcbn0pO1xuXG5jb25zdCBvYmogPSB7XG4gICAgYWFhOiBmdW5jdGlvbigpIHtcbiAgICAgICAgcmV0dXJuIGZ1bmN0aW9uIGZvbygpIHtcbiAgICAgICAgICAgIC8vIFRoZXJlIGlzIGluIGEgbWV0aG9kIGBhYWFgLCBidXQgYGZvb2AgaXMgbm90IGEgbWV0aG9kLlxuICAgICAgICAgICAgdGhpcy5hID0gMDtcbiAgICAgICAgICAgIGJheigoKSA9PiB0aGlzKTtcbiAgICAgICAgfTtcbiAgICB9XG59O1xuXG5mb28uZm9yRWFjaChmdW5jdGlvbigpIHtcbiAgICB0aGlzLmEgPSAwO1xuICAgIGJheigoKSA9PiB0aGlzKTtcbn0pOyJ9)

```
/*eslint no-invalid-this: "error"*/

"use strict";

(function() {
    this.a = 0;
    baz(() => this);
})();

function foo() {
    this.a = 0;
    baz(() => this);
}

const bar = function() {
    this.a = 0;
    baz(() => this);
};

foo(function() {
    this.a = 0;
    baz(() => this);
});

const obj = {
    aaa: function() {
        return function foo() {
            // There is in a method `aaa`, but `foo` is not a method.
            this.a = 0;
            baz(() => this);
        };
    }
};

foo.forEach(function() {
    this.a = 0;
    baz(() => this);
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
```

Examples of correct code for this rule in strict mode:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC10aGlzOiBcImVycm9yXCIqL1xuXG5cInVzZSBzdHJpY3RcIjtcblxudGhpcy5hID0gMDtcbmJheigoKSA9PiB0aGlzKTtcblxuZnVuY3Rpb24gRm9vKCkge1xuICAgIC8vIE9LLCB0aGlzIGlzIGluIGEgbGVnYWN5IHN0eWxlIGNvbnN0cnVjdG9yLlxuICAgIHRoaXMuYSA9IDA7XG4gICAgYmF6KCgpID0+IHRoaXMpO1xufVxuXG5jbGFzcyBCYXIge1xuICAgIGNvbnN0cnVjdG9yKCkge1xuICAgICAgICAvLyBPSywgdGhpcyBpcyBpbiBhIGNvbnN0cnVjdG9yLlxuICAgICAgICB0aGlzLmEgPSAwO1xuICAgICAgICBiYXooKCkgPT4gdGhpcyk7XG4gICAgfVxufVxuXG5jb25zdCBvYmogPSB7XG4gICAgZm9vOiBmdW5jdGlvbiBmb28oKSB7XG4gICAgICAgIC8vIE9LLCB0aGlzIGlzIGluIGEgbWV0aG9kICh0aGlzIGZ1bmN0aW9uIGlzIG9uIG9iamVjdCBsaXRlcmFsKS5cbiAgICAgICAgdGhpcy5hID0gMDtcbiAgICB9XG59O1xuXG5jb25zdCBvYmoxID0ge1xuICAgIGZvbygpIHtcbiAgICAgICAgLy8gT0ssIHRoaXMgaXMgaW4gYSBtZXRob2QgKHRoaXMgZnVuY3Rpb24gaXMgb24gb2JqZWN0IGxpdGVyYWwpLlxuICAgICAgICB0aGlzLmEgPSAwO1xuICAgIH1cbn07XG5cbmNvbnN0IG9iajIgPSB7XG4gICAgZ2V0IGZvbygpIHtcbiAgICAgICAgLy8gT0ssIHRoaXMgaXMgaW4gYSBtZXRob2QgKHRoaXMgZnVuY3Rpb24gaXMgb24gb2JqZWN0IGxpdGVyYWwpLlxuICAgICAgICByZXR1cm4gdGhpcy5hO1xuICAgIH1cbn07XG5cbmNvbnN0IG9iajMgPSBPYmplY3QuY3JlYXRlKG51bGwsIHtcbiAgICBmb286IHt2YWx1ZTogZnVuY3Rpb24gZm9vKCkge1xuICAgICAgICAvLyBPSywgdGhpcyBpcyBpbiBhIG1ldGhvZCAodGhpcyBmdW5jdGlvbiBpcyBvbiBvYmplY3QgbGl0ZXJhbCkuXG4gICAgICAgIHRoaXMuYSA9IDA7XG4gICAgfX1cbn0pO1xuXG5PYmplY3QuZGVmaW5lUHJvcGVydHkob2JqLCBcImZvb1wiLCB7XG4gICAgdmFsdWU6IGZ1bmN0aW9uIGZvbygpIHtcbiAgICAgICAgLy8gT0ssIHRoaXMgaXMgaW4gYSBtZXRob2QgKHRoaXMgZnVuY3Rpb24gaXMgb24gb2JqZWN0IGxpdGVyYWwpLlxuICAgICAgICB0aGlzLmEgPSAwO1xuICAgIH1cbn0pO1xuXG5PYmplY3QuZGVmaW5lUHJvcGVydGllcyhvYmosIHtcbiAgICBmb286IHt2YWx1ZTogZnVuY3Rpb24gZm9vKCkge1xuICAgICAgICAvLyBPSywgdGhpcyBpcyBpbiBhIG1ldGhvZCAodGhpcyBmdW5jdGlvbiBpcyBvbiBvYmplY3QgbGl0ZXJhbCkuXG4gICAgICAgIHRoaXMuYSA9IDA7XG4gICAgfX1cbn0pO1xuXG5mdW5jdGlvbiBGb28oKSB7XG4gICAgdGhpcy5mb28gPSBmdW5jdGlvbiBmb28oKSB7XG4gICAgICAgIC8vIE9LLCB0aGlzIGlzIGluIGEgbWV0aG9kICh0aGlzIGZ1bmN0aW9uIGFzc2lnbnMgdG8gYSBwcm9wZXJ0eSkuXG4gICAgICAgIHRoaXMuYSA9IDA7XG4gICAgICAgIGJheigoKSA9PiB0aGlzKTtcbiAgICB9O1xufVxuXG5vYmouZm9vID0gZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIE9LLCB0aGlzIGlzIGluIGEgbWV0aG9kICh0aGlzIGZ1bmN0aW9uIGFzc2lnbnMgdG8gYSBwcm9wZXJ0eSkuXG4gICAgdGhpcy5hID0gMDtcbn07XG5cbkZvby5wcm90b3R5cGUuZm9vID0gZnVuY3Rpb24gZm9vKCkge1xuICAgIC8vIE9LLCB0aGlzIGlzIGluIGEgbWV0aG9kICh0aGlzIGZ1bmN0aW9uIGFzc2lnbnMgdG8gYSBwcm9wZXJ0eSkuXG4gICAgdGhpcy5hID0gMDtcbn07XG5cbmNsYXNzIEJheiB7XG5cbiAgICAvLyBPSywgdGhpcyBpcyBpbiBhIGNsYXNzIGZpZWxkIGluaXRpYWxpemVyLlxuICAgIGEgPSB0aGlzLmI7XG5cbiAgICAvLyBPSywgc3RhdGljIGluaXRpYWxpemVycyBhbHNvIGhhdmUgdmFsaWQgdGhpcy5cbiAgICBzdGF0aWMgYSA9IHRoaXMuYjtcblxuICAgIGZvbygpIHtcbiAgICAgICAgLy8gT0ssIHRoaXMgaXMgaW4gYSBtZXRob2QuXG4gICAgICAgIHRoaXMuYSA9IDA7XG4gICAgICAgIGJheigoKSA9PiB0aGlzKTtcbiAgICB9XG5cbiAgICBzdGF0aWMgZm9vKCkge1xuICAgICAgICAvLyBPSywgdGhpcyBpcyBpbiBhIG1ldGhvZCAoc3RhdGljIG1ldGhvZHMgYWxzbyBoYXZlIHZhbGlkIHRoaXMpLlxuICAgICAgICB0aGlzLmEgPSAwO1xuICAgICAgICBiYXooKCkgPT4gdGhpcyk7XG4gICAgfVxuXG4gICAgc3RhdGljIHtcbiAgICAgICAgLy8gT0ssIHN0YXRpYyBibG9ja3MgYWxzbyBoYXZlIHZhbGlkIHRoaXMuXG4gICAgICAgIHRoaXMuYSA9IDA7XG4gICAgICAgIGJheigoKSA9PiB0aGlzKTtcbiAgICB9XG59XG5cbmNvbnN0IGJhciA9IChmdW5jdGlvbiBmb28oKSB7XG4gICAgLy8gT0ssIHRoZSBgYmluZGAgbWV0aG9kIG9mIHRoaXMgZnVuY3Rpb24gaXMgY2FsbGVkIGRpcmVjdGx5LlxuICAgIHRoaXMuYSA9IDA7XG59KS5iaW5kKG9iaik7XG5cbmZvby5mb3JFYWNoKGZ1bmN0aW9uKCkge1xuICAgIC8vIE9LLCBgdGhpc0FyZ2Agb2YgYC5mb3JFYWNoKClgIGlzIGdpdmVuLlxuICAgIHRoaXMuYSA9IDA7XG4gICAgYmF6KCgpID0+IHRoaXMpO1xufSwgdGhpc0FyZyk7XG5cbi8qKiBAdGhpcyBGb28gKi9cbmZ1bmN0aW9uIGZvbygpIHtcbiAgICAvLyBPSywgdGhpcyBmdW5jdGlvbiBoYXMgYSBgQHRoaXNgIHRhZyBpbiBpdHMgSlNEb2MgY29tbWVudC5cbiAgICB0aGlzLmEgPSAwO1xufSJ9)

```
/*eslint no-invalid-this: "error"*/

"use strict";

this.a = 0;
baz(() => this);

function Foo() {
    // OK, this is in a legacy style constructor.
    this.a = 0;
    baz(() => this);
}

class Bar {
    constructor() {
        // OK, this is in a constructor.
        this.a = 0;
        baz(() => this);
    }
}

const obj = {
    foo: function foo() {
        // OK, this is in a method (this function is on object literal).
        this.a = 0;
    }
};

const obj1 = {
    foo() {
        // OK, this is in a method (this function is on object literal).
        this.a = 0;
    }
};

const obj2 = {
    get foo() {
        // OK, this is in a method (this function is on object literal).
        return this.a;
    }
};

const obj3 = Object.create(null, {
    foo: {value: function foo() {
        // OK, this is in a method (this function is on object literal).
        this.a = 0;
    }}
});

Object.defineProperty(obj, "foo", {
    value: function foo() {
        // OK, this is in a method (this function is on object literal).
        this.a = 0;
    }
});

Object.defineProperties(obj, {
    foo: {value: function foo() {
        // OK, this is in a method (this function is on object literal).
        this.a = 0;
    }}
});

function Foo() {
    this.foo = function foo() {
        // OK, this is in a method (this function assigns to a property).
        this.a = 0;
        baz(() => this);
    };
}

obj.foo = function foo() {
    // OK, this is in a method (this function assigns to a property).
    this.a = 0;
};

Foo.prototype.foo = function foo() {
    // OK, this is in a method (this function assigns to a property).
    this.a = 0;
};

class Baz {

    // OK, this is in a class field initializer.
    a = this.b;

    // OK, static initializers also have valid this.
    static a = this.b;

    foo() {
        // OK, this is in a method.
        this.a = 0;
        baz(() => this);
    }

    static foo() {
        // OK, this is in a method (static methods also have valid this).
        this.a = 0;
        baz(() => this);
    }

    static {
        // OK, static blocks also have valid this.
        this.a = 0;
        baz(() => this);
    }
}

const bar = (function foo() {
    // OK, the `bind` method of this function is called directly.
    this.a = 0;
}).bind(obj);

foo.forEach(function() {
    // OK, `thisArg` of `.forEach()` is given.
    this.a = 0;
    baz(() => this);
}, thisArg);

/** @this Foo */
function foo() {
    // OK, this function has a `@this` tag in its JSDoc comment.
    this.a = 0;
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
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
```

## Options

This rule has an object option, with one option:

- `"capIsConstructor": false` (default `true`) disables the assumption that a function which name starts with an uppercase is a constructor.

### capIsConstructor

By default, this rule always allows the use of `this` in functions which name starts with an uppercase and anonymous functions that are assigned to a variable which name starts with an uppercase, assuming that those functions are used as constructor functions.

Set `"capIsConstructor"` to `false` if you want those functions to be treated as ‘regular’ functions.

Examples of incorrect code for this rule with `"capIsConstructor"` option set to `false`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC10aGlzOiBbXCJlcnJvclwiLCB7IFwiY2FwSXNDb25zdHJ1Y3RvclwiOiBmYWxzZSB9XSovXG5cblwidXNlIHN0cmljdFwiO1xuXG5mdW5jdGlvbiBGb28oKSB7XG4gICAgdGhpcy5hID0gMDtcbn1cblxuY29uc3QgYmFyID0gZnVuY3Rpb24gRm9vKCkge1xuICAgIHRoaXMuYSA9IDA7XG59XG5cbmNvbnN0IEJhciA9IGZ1bmN0aW9uKCkge1xuICAgIHRoaXMuYSA9IDA7XG59O1xuXG5CYXogPSBmdW5jdGlvbigpIHtcbiAgICB0aGlzLmEgPSAwO1xufTsifQ==)

```
/*eslint no-invalid-this: ["error", { "capIsConstructor": false }]*/

"use strict";

function Foo() {
    this.a = 0;
}

const bar = function Foo() {
    this.a = 0;
}

const Bar = function() {
    this.a = 0;
};

Baz = function() {
    this.a = 0;
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

Examples of correct code for this rule with `"capIsConstructor"` option set to `false`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8taW52YWxpZC10aGlzOiBbXCJlcnJvclwiLCB7IFwiY2FwSXNDb25zdHJ1Y3RvclwiOiBmYWxzZSB9XSovXG5cblwidXNlIHN0cmljdFwiO1xuXG5vYmouRm9vID0gZnVuY3Rpb24gRm9vKCkge1xuICAgIC8vIE9LLCB0aGlzIGlzIGluIGEgbWV0aG9kLlxuICAgIHRoaXMuYSA9IDA7XG59OyJ9)

```
/*eslint no-invalid-this: ["error", { "capIsConstructor": false }]*/

"use strict";

obj.Foo = function Foo() {
    // OK, this is in a method.
    this.a = 0;
};
1
2
3
4
5
6
7
8
```

This rule additionally supports TypeScript type syntax.

Examples of incorrect TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1pbnZhbGlkLXRoaXM6IFwiZXJyb3JcIiovXG5cbmZ1bmN0aW9uIGZvbyhiYXI6IHN0cmluZykge1xuICAgIHRoaXMucHJvcDtcbiAgICBjb25zb2xlLmxvZyhiYXIpXG59XG5cbi8qKiBAdGhpcyBPYmogKi9cbmZvbyhmdW5jdGlvbigpIHtcbiAgICBjb25zb2xlLmxvZyh0aGlzKTtcbiAgICB6KHggPT4gY29uc29sZS5sb2coeCwgdGhpcykpO1xufSk7XG5cbmZ1bmN0aW9uIGZvbygpIHtcbiAgY2xhc3MgQyB7XG4gICAgYWNjZXNzb3IgW3RoaXMuYV0gPSBmb287XG4gIH1cbn0ifQ==)

```
/*eslint no-invalid-this: "error"*/

function foo(bar: string) {
    this.prop;
    console.log(bar)
}

/** @this Obj */
foo(function() {
    console.log(this);
    z(x => console.log(x, this));
});

function foo() {
  class C {
    accessor [this.a] = foo;
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
```

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1pbnZhbGlkLXRoaXM6IFwiZXJyb3JcIiovXG5cbmludGVyZmFjZSBTb21lVHlwZSB7XG4gICAgcHJvcDogc3RyaW5nO1xufVxuXG5mdW5jdGlvbiBmb28odGhpczogU29tZVR5cGUpIHtcbiAgICB0aGlzLnByb3A7XG59XG5cbmNsYXNzIEEge1xuICAgIGEgPSA1O1xuICAgIGIgPSB0aGlzLmE7XG4gICAgYWNjZXNzb3IgYyA9IHRoaXMuYTtcbn0ifQ==)

```
/*eslint no-invalid-this: "error"*/

interface SomeType {
    prop: string;
}

function foo(this: SomeType) {
    this.prop;
}

class A {
    a = 5;
    b = this.a;
    accessor c = this.a;
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

## When Not To Use It

If you don’t want to be notified about usage of `this` keyword outside of classes or class-like objects, you can safely disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

Note that, technically, TypeScript will only catch this if you have the `strict` or `noImplicitThis` flags enabled. These are enabled in most TypeScript projects, since they are considered to be best practice.

## Version

This rule was introduced in ESLint v1.0.0-rc-2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-invalid-this.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-invalid-this.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-invalid-this.md
                    
                
                )
