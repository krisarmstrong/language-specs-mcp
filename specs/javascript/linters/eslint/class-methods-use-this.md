# class-methods-use-this

Enforce that class methods utilize `this`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [exceptMethods](#exceptmethods)
  2. [enforceForClassFields](#enforceforclassfields)
  3. [ignoreOverrideMethods](#ignoreoverridemethods)
  4. [ignoreClassesWithImplements](#ignoreclasseswithimplements)

3. [Version](#version)
4. [Further Reading](#further-reading)
5. [Resources](#resources)

If a class method does not use `this`, it can sometimes be made into a static function. If you do convert the method into a static function, instances of the class that call that particular method have to be converted to a static call as well (`MyClass.callStaticMethod()`).

It’s possible to have a class method which doesn’t use `this`, such as:

```
class A {
    constructor() {
        this.a = "hi";
    }

    print() {
        console.log(this.a);
    }

    sayHi() {
        console.log("hi");
    }
}

let a = new A();
a.sayHi(); // => "hi"
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

Copy code to clipboard

In the example above, the `sayHi` method doesn’t use `this`, so we can make it a static method:

```
class A {
    constructor() {
        this.a = "hi";
    }

    print() {
        console.log(this.a);
    }

    static sayHi() {
        console.log("hi");
    }
}

A.sayHi(); // => "hi"
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

Also note in the above examples that if you switch a method to a static method, instances of the class that call the static method (`let a = new A(); a.sayHi();`) have to be updated to being a static call (`A.sayHi();`) instead of having the instance of the class call the method.

## Rule Details

This rule is aimed to flag class methods that do not use `this`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7XG4gICAgZm9vKCkge1xuICAgICAgICBjb25zb2xlLmxvZyhcIkhlbGxvIFdvcmxkXCIpOyAgICAgLyplcnJvciBFeHBlY3RlZCAndGhpcycgdG8gYmUgdXNlZCBieSBjbGFzcyBtZXRob2QgJ2ZvbycuKi9cbiAgICB9XG59In0=)

```
/*eslint class-methods-use-this: "error"*/

class A {
    foo() {
        console.log("Hello World");     /*error Expected 'this' to be used by class method 'foo'.*/
    }
}
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7XG4gICAgZm9vKCkge1xuICAgICAgICB0aGlzLmJhciA9IFwiSGVsbG8gV29ybGRcIjsgLy8gT0ssIHRoaXMgaXMgdXNlZFxuICAgIH1cbn1cblxuY2xhc3MgQiB7XG4gICAgY29uc3RydWN0b3IoKSB7XG4gICAgICAgIC8vIE9LLiBjb25zdHJ1Y3RvciBpcyBleGVtcHRcbiAgICB9XG59XG5cbmNsYXNzIEMge1xuICAgIHN0YXRpYyBmb28oKSB7XG4gICAgICAgIC8vIE9LLiBzdGF0aWMgbWV0aG9kcyBhcmVuJ3QgZXhwZWN0ZWQgdG8gdXNlIHRoaXMuXG4gICAgfVxuXG4gICAgc3RhdGljIHtcbiAgICAgICAgLy8gT0suIHN0YXRpYyBibG9ja3MgYXJlIGV4ZW1wdC5cbiAgICB9XG59In0=)

```
/*eslint class-methods-use-this: "error"*/

class A {
    foo() {
        this.bar = "Hello World"; // OK, this is used
    }
}

class B {
    constructor() {
        // OK. constructor is exempt
    }
}

class C {
    static foo() {
        // OK. static methods aren't expected to use this.
    }

    static {
        // OK. static blocks are exempt.
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
```

## Options

This rule has four options:

- `"exceptMethods"` allows specified method names to be ignored with this rule.
- `"enforceForClassFields"` enforces that arrow functions and function expressions used as instance field initializers utilize `this`. This also applies to auto-accessor fields (fields declared with the `accessor` keyword) which are part of the [stage 3 decorators proposal](https://github.com/tc39/proposal-decorators). (default: `true`)
- `"ignoreOverrideMethods"` ignores members that are marked with the `override` modifier. (TypeScript only, default: `false`)
- `"ignoreClassesWithImplements"` ignores class members that are defined within a class that `implements` an interface. (TypeScript only)

### exceptMethods

```
"class-methods-use-this": [<enabled>, { "exceptMethods": [<...exceptions>] }]
1
```

Copy code to clipboard

The `"exceptMethods"` option allows you to pass an array of method names for which you would like to ignore warnings. For example, you might have a spec from an external library that requires you to overwrite a method as a regular function (and not as a static method) and does not use `this` inside the function body. In this case, you can add that method to ignore in the warnings.

Examples of incorrect code for this rule when used without `"exceptMethods"`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogXCJlcnJvclwiKi9cblxuY2xhc3MgQSB7XG4gICAgZm9vKCkge1xuICAgIH1cbn0ifQ==)

```
/*eslint class-methods-use-this: "error"*/

class A {
    foo() {
    }
}
1
2
3
4
5
6
```

Examples of correct code for this rule when used with exceptMethods:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogW1wiZXJyb3JcIiwgeyBcImV4Y2VwdE1ldGhvZHNcIjogW1wiZm9vXCIsIFwiI2JhclwiXSB9XSAqL1xuXG5jbGFzcyBBIHtcbiAgICBmb28oKSB7XG4gICAgfVxuICAgICNiYXIoKSB7XG4gICAgfVxufSJ9)

```
/*eslint class-methods-use-this: ["error", { "exceptMethods": ["foo", "#bar"] }] */

class A {
    foo() {
    }
    #bar() {
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
```

### enforceForClassFields

```
"class-methods-use-this": [<enabled>, { "enforceForClassFields": true | false }]
1
```

Copy code to clipboard

The `enforceForClassFields` option enforces that arrow functions and function expressions used as instance field initializers utilize `this`. This also applies to auto-accessor fields (fields declared with the `accessor` keyword) which are part of the [stage 3 decorators proposal](https://github.com/tc39/proposal-decorators). (default: `true`)

Examples of incorrect code for this rule with the `{ "enforceForClassFields": true }` option (default):

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogW1wiZXJyb3JcIiwgeyBcImVuZm9yY2VGb3JDbGFzc0ZpZWxkc1wiOiB0cnVlIH1dICovXG5cbmNsYXNzIEEge1xuICAgIGZvbyA9ICgpID0+IHt9XG59In0=)

```
/*eslint class-methods-use-this: ["error", { "enforceForClassFields": true }] */

class A {
    foo = () => {}
}
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "enforceForClassFields": true }` option (default):

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogW1wiZXJyb3JcIiwgeyBcImVuZm9yY2VGb3JDbGFzc0ZpZWxkc1wiOiB0cnVlIH1dICovXG5cbmNsYXNzIEEge1xuICAgIGZvbyA9ICgpID0+IHt0aGlzO31cbn0ifQ==)

```
/*eslint class-methods-use-this: ["error", { "enforceForClassFields": true }] */

class A {
    foo = () => {this;}
}
1
2
3
4
5
```

Examples of correct code for this rule with the `{ "enforceForClassFields": false }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY2xhc3MtbWV0aG9kcy11c2UtdGhpczogW1wiZXJyb3JcIiwgeyBcImVuZm9yY2VGb3JDbGFzc0ZpZWxkc1wiOiBmYWxzZSB9XSAqL1xuXG5jbGFzcyBBIHtcbiAgICBmb28gPSAoKSA9PiB7fVxufSJ9)

```
/*eslint class-methods-use-this: ["error", { "enforceForClassFields": false }] */

class A {
    foo = () => {}
}
1
2
3
4
5
```

Examples of incorrect TypeScript code for this rule with the `{ "enforceForClassFields": true }` option (default):

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiZW5mb3JjZUZvckNsYXNzRmllbGRzXCI6IHRydWUgfV0gKi9cblxuY2xhc3MgQSB7XG4gICAgZm9vID0gKCkgPT4ge31cbiAgICBhY2Nlc3NvciBiYXIgPSAoKSA9PiB7fVxufSJ9)

```
/*eslint class-methods-use-this: ["error", { "enforceForClassFields": true }] */

class A {
    foo = () => {}
    accessor bar = () => {}
}
1
2
3
4
5
6
```

Examples of correct TypeScript code for this rule with the `{ "enforceForClassFields": true }` option (default):

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiZW5mb3JjZUZvckNsYXNzRmllbGRzXCI6IHRydWUgfV0gKi9cblxuY2xhc3MgQSB7XG4gICAgZm9vID0gKCkgPT4ge3RoaXM7fVxuICAgIGFjY2Vzc29yIGJhciA9ICgpID0+IHt0aGlzO31cbn0ifQ==)

```
/*eslint class-methods-use-this: ["error", { "enforceForClassFields": true }] */

class A {
    foo = () => {this;}
    accessor bar = () => {this;}
}
1
2
3
4
5
6
```

Examples of correct TypeScript code for this rule with the `{ "enforceForClassFields": false }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiZW5mb3JjZUZvckNsYXNzRmllbGRzXCI6IGZhbHNlIH1dICovXG5cbmNsYXNzIEEge1xuICAgIGZvbyA9ICgpID0+IHt9XG4gICAgYWNjZXNzb3IgYmFyID0gKCkgPT4ge31cbn0ifQ==)

```
/*eslint class-methods-use-this: ["error", { "enforceForClassFields": false }] */

class A {
    foo = () => {}
    accessor bar = () => {}
}
1
2
3
4
5
6
```

### ignoreOverrideMethods

```
"class-methods-use-this": [<enabled>, { "ignoreOverrideMethods": true | false }]
1
```

Copy code to clipboard

The `ignoreOverrideMethods` option ignores members that are marked with the `override` modifier. (default: `false`)

Examples of incorrect TypeScript code for this rule with the `{ "ignoreOverrideMethods": false }` option (default):

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlT3ZlcnJpZGVNZXRob2RzXCI6IGZhbHNlIH1dICovXG5cbmFic3RyYWN0IGNsYXNzIEJhc2Uge1xuICAgIGFic3RyYWN0IG1ldGhvZCgpOiB2b2lkO1xuICAgIGFic3RyYWN0IHByb3BlcnR5OiAoKSA9PiB2b2lkO1xufVxuXG5jbGFzcyBEZXJpdmVkIGV4dGVuZHMgQmFzZSB7XG4gICAgb3ZlcnJpZGUgbWV0aG9kKCkge31cbiAgICBvdmVycmlkZSBwcm9wZXJ0eSA9ICgpID0+IHt9O1xufSJ9)

```
/*eslint class-methods-use-this: ["error", { "ignoreOverrideMethods": false }] */

abstract class Base {
    abstract method(): void;
    abstract property: () => void;
}

class Derived extends Base {
    override method() {}
    override property = () => {};
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

Examples of correct TypeScript code for this rule with the `{ "ignoreOverrideMethods": false }` option (default):

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlT3ZlcnJpZGVNZXRob2RzXCI6IGZhbHNlIH1dICovXG5cbmFic3RyYWN0IGNsYXNzIEJhc2Uge1xuICAgIGFic3RyYWN0IG1ldGhvZCgpOiB2b2lkO1xuICAgIGFic3RyYWN0IHByb3BlcnR5OiAoKSA9PiB2b2lkO1xufVxuXG5jbGFzcyBEZXJpdmVkIGV4dGVuZHMgQmFzZSB7XG4gICAgb3ZlcnJpZGUgbWV0aG9kKCkge1xuICAgICAgICB0aGlzLmZvbyA9IFwiSGVsbG8gV29ybGRcIjtcbiAgICB9O1xuICAgIG92ZXJyaWRlIHByb3BlcnR5ID0gKCkgPT4ge1xuICAgICAgICB0aGlzO1xuICAgIH07XG59In0=)

```
/*eslint class-methods-use-this: ["error", { "ignoreOverrideMethods": false }] */

abstract class Base {
    abstract method(): void;
    abstract property: () => void;
}

class Derived extends Base {
    override method() {
        this.foo = "Hello World";
    };
    override property = () => {
        this;
    };
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

Examples of correct TypeScript code for this rule with the `{ "ignoreOverrideMethods": true }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlT3ZlcnJpZGVNZXRob2RzXCI6IHRydWUgfV0gKi9cblxuYWJzdHJhY3QgY2xhc3MgQmFzZSB7XG4gICAgYWJzdHJhY3QgbWV0aG9kKCk6IHZvaWQ7XG4gICAgYWJzdHJhY3QgcHJvcGVydHk6ICgpID0+IHZvaWQ7XG59XG5cbmNsYXNzIERlcml2ZWQgZXh0ZW5kcyBCYXNlIHtcbiAgICBvdmVycmlkZSBtZXRob2QoKSB7fVxuICAgIG92ZXJyaWRlIHByb3BlcnR5ID0gKCkgPT4ge307XG59In0=)

```
/*eslint class-methods-use-this: ["error", { "ignoreOverrideMethods": true }] */

abstract class Base {
    abstract method(): void;
    abstract property: () => void;
}

class Derived extends Base {
    override method() {}
    override property = () => {};
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

### ignoreClassesWithImplements

```
"class-methods-use-this": [<enabled>, { "ignoreClassesWithImplements": "all" | "public-fields" }]
1
```

Copy code to clipboard

The `ignoreClassesWithImplements` ignores class members that are defined within a class that `implements` an interface. The option accepts two possible values:

- `"all"` - Ignores all classes that implement interfaces
- `"public-fields"` - Only ignores public fields in classes that implement interfaces

Examples of incorrect TypeScript code for this rule with the `{ "ignoreClassesWithImplements": "all" }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2xhc3Nlc1dpdGhJbXBsZW1lbnRzXCI6IFwiYWxsXCIgfV0gKi9cblxuY2xhc3MgU3RhbmRhbG9uZSB7XG4gICAgbWV0aG9kKCkge31cbiAgICBwcm9wZXJ0eSA9ICgpID0+IHt9O1xufSJ9)

```
/*eslint class-methods-use-this: ["error", { "ignoreClassesWithImplements": "all" }] */

class Standalone {
    method() {}
    property = () => {};
}
1
2
3
4
5
6
```

Examples of correct TypeScript code for this rule with the `{ "ignoreClassesWithImplements": "all" }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2xhc3Nlc1dpdGhJbXBsZW1lbnRzXCI6IFwiYWxsXCIgfV0gKi9cblxuaW50ZXJmYWNlIEJhc2Uge1xuICAgIG1ldGhvZCgpOiB2b2lkO1xufVxuXG5jbGFzcyBEZXJpdmVkIGltcGxlbWVudHMgQmFzZSB7XG4gICAgbWV0aG9kKCkge31cbiAgICBwcm9wZXJ0eSA9ICgpID0+IHt9O1xufSJ9)

```
/*eslint class-methods-use-this: ["error", { "ignoreClassesWithImplements": "all" }] */

interface Base {
    method(): void;
}

class Derived implements Base {
    method() {}
    property = () => {};
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

Examples of incorrect TypeScript code for this rule with the `{ "ignoreClassesWithImplements": "public-fields" }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2xhc3Nlc1dpdGhJbXBsZW1lbnRzXCI6IFwicHVibGljLWZpZWxkc1wiIH1dICovXG5cbmludGVyZmFjZSBCYXNlIHtcbiAgICBtZXRob2QoKTogdm9pZDtcbn1cblxuY2xhc3MgRGVyaXZlZCBpbXBsZW1lbnRzIEJhc2Uge1xuICAgIG1ldGhvZCgpIHt9XG4gICAgcHJvcGVydHkgPSAoKSA9PiB7fTtcblxuICAgIHByaXZhdGUgcHJpdmF0ZU1ldGhvZCgpIHt9XG4gICAgcHJpdmF0ZSBwcml2YXRlUHJvcGVydHkgPSAoKSA9PiB7fTtcblxuICAgIHByb3RlY3RlZCBwcm90ZWN0ZWRNZXRob2QoKSB7fVxuICAgIHByb3RlY3RlZCBwcm90ZWN0ZWRQcm9wZXJ0eSA9ICgpID0+IHt9O1xufSJ9)

```
/*eslint class-methods-use-this: ["error", { "ignoreClassesWithImplements": "public-fields" }] */

interface Base {
    method(): void;
}

class Derived implements Base {
    method() {}
    property = () => {};

    private privateMethod() {}
    private privateProperty = () => {};

    protected protectedMethod() {}
    protected protectedProperty = () => {};
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

Examples of correct TypeScript code for this rule with the `{ "ignoreClassesWithImplements": "public-fields" }` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBjbGFzcy1tZXRob2RzLXVzZS10aGlzOiBbXCJlcnJvclwiLCB7IFwiaWdub3JlQ2xhc3Nlc1dpdGhJbXBsZW1lbnRzXCI6IFwicHVibGljLWZpZWxkc1wiIH1dICovXG5cbmludGVyZmFjZSBCYXNlIHtcbiAgICBtZXRob2QoKTogdm9pZDtcbn1cblxuY2xhc3MgRGVyaXZlZCBpbXBsZW1lbnRzIEJhc2Uge1xuICAgIG1ldGhvZCgpIHt9XG4gICAgcHJvcGVydHkgPSAoKSA9PiB7fTtcbn0ifQ==)

```
/*eslint class-methods-use-this: ["error", { "ignoreClassesWithImplements": "public-fields" }] */

interface Base {
    method(): void;
}

class Derived implements Base {
    method() {}
    property = () => {};
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

## Version

This rule was introduced in ESLint v3.4.0.

## Further Reading

[Classes - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 developer.mozilla.org[static - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/class-methods-use-this.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/class-methods-use-this.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/class-methods-use-this.md
                    
                
                )
