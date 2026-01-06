# accessor-pairs

Enforce getter and setter pairs in objects and classes

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [setWithoutGet](#setwithoutget)
  2. [getWithoutSet](#getwithoutset)
  3. [enforceForClassMembers](#enforceforclassmembers)
  4. [enforceForTSTypes](#enforcefortstypes)

3. [Known Limitations](#known-limitations)
4. [When Not To Use It](#when-not-to-use-it)
5. [Related Rules](#related-rules)
6. [Version](#version)
7. [Further Reading](#further-reading)
8. [Resources](#resources)

It’s a common mistake in JavaScript to create an object with just a setter for a property but never have a corresponding getter defined for it. Without a getter, you cannot read the property, so it ends up not being used.

Here are some examples:

```
// Bad
const o = {
    set a(value) {
        this.val = value;
    }
};

// Good
const p = {
    set a(value) {
        this.val = value;
    },
    get a() {
        return this.val;
    }
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
```

Copy code to clipboard

This rule warns if setters are defined without getters. Using an option `getWithoutSet`, it will warn if you have a getter without a setter also.

## Rule Details

This rule enforces a style where it requires to have a getter for every property which has a setter defined.

By activating the option `getWithoutSet` it enforces the presence of a setter for every property which has a getter defined.

This rule always checks object literals and property descriptors. By default, it also checks class declarations and class expressions.

## Options

- `setWithoutGet` set to `true` will warn for setters without getters (Default `true`).
- `getWithoutSet` set to `true` will warn for getters without setters (Default `false`).
- `enforceForClassMembers` set to `true` additionally applies this rule to class getters/setters (Default `true`). Set `enforceForClassMembers` to `false` if you want this rule to ignore class declarations and class expressions.
- `enforceForTSTypes`: set to `true` additionally applies this rule to TypeScript type definitions (Default `false`).

### setWithoutGet

Examples of incorrect code for the default `{ "setWithoutGet": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHEgPSB7XG4gICAgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59O1xuXG5cbmNvbnN0IHIgPSB7ZDogMX07XG5PYmplY3QuZGVmaW5lUHJvcGVydHkociwgJ2MnLCB7XG4gICAgc2V0OiBmdW5jdGlvbih2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn0pOyJ9)

```
/*eslint accessor-pairs: "error"*/

const q = {
    set a(value) {
        this.val = value;
    }
};

const r = {d: 1};
Object.defineProperty(r, 'c', {
    set: function(value) {
        this.val = value;
    }
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
```

Examples of correct code for the default `{ "setWithoutGet": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFwiZXJyb3JcIiovXG5cbmNvbnN0IHMgPSB7XG4gICAgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9LFxuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufTtcblxuY29uc3QgdCA9IHtkOiAxfTtcbk9iamVjdC5kZWZpbmVQcm9wZXJ0eSh0LCAnYycsIHtcbiAgICBzZXQ6IGZ1bmN0aW9uKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfSxcbiAgICBnZXQ6IGZ1bmN0aW9uKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufSk7XG4ifQ==)

```
/*eslint accessor-pairs: "error"*/

const s = {
    set a(value) {
        this.val = value;
    },
    get a() {
        return this.val;
    }
};

const t = {d: 1};
Object.defineProperty(t, 'c', {
    set: function(value) {
        this.val = value;
    },
    get: function() {
        return this.val;
    }
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
```

### getWithoutSet

Examples of incorrect code for the `{ "getWithoutSet": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFtcImVycm9yXCIsIHsgXCJnZXRXaXRob3V0U2V0XCI6IHRydWUgfV0qL1xuXG5jb25zdCB1ID0ge1xuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuY29uc3QgdiA9IHtcbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbn07XG5cbmNvbnN0IHcgPSB7ZDogMX07XG5PYmplY3QuZGVmaW5lUHJvcGVydHkodywgJ2MnLCB7XG4gICAgc2V0OiBmdW5jdGlvbih2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn0pO1xuXG5jb25zdCB4ID0ge2Q6IDF9O1xuT2JqZWN0LmRlZmluZVByb3BlcnR5KHgsICdjJywge1xuICAgIGdldDogZnVuY3Rpb24oKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59KTsifQ==)

```
/*eslint accessor-pairs: ["error", { "getWithoutSet": true }]*/

const u = {
    set a(value) {
        this.val = value;
    }
};

const v = {
    get a() {
        return this.val;
    }
};

const w = {d: 1};
Object.defineProperty(w, 'c', {
    set: function(value) {
        this.val = value;
    }
});

const x = {d: 1};
Object.defineProperty(x, 'c', {
    get: function() {
        return this.val;
    }
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
```

Examples of correct code for the `{ "getWithoutSet": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFtcImVycm9yXCIsIHsgXCJnZXRXaXRob3V0U2V0XCI6IHRydWUgfV0qL1xuY29uc3QgeSA9IHtcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH0sXG4gICAgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59O1xuXG5jb25zdCB6ID0ge2Q6IDF9O1xuT2JqZWN0LmRlZmluZVByb3BlcnR5KHosICdjJywge1xuICAgIHNldDogZnVuY3Rpb24odmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9LFxuICAgIGdldDogZnVuY3Rpb24oKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59KTtcbiJ9)

```
/*eslint accessor-pairs: ["error", { "getWithoutSet": true }]*/
const y = {
    set a(value) {
        this.val = value;
    },
    get a() {
        return this.val;
    }
};

const z = {d: 1};
Object.defineProperty(z, 'c', {
    set: function(value) {
        this.val = value;
    },
    get: function() {
        return this.val;
    }
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
```

### enforceForClassMembers

When `enforceForClassMembers` is set to `true` (default):

- `"getWithoutSet": true` will also warn for getters without setters in classes.
- `"setWithoutGet": true` will also warn for setters without getters in classes.

Examples of incorrect code for `{ "getWithoutSet": true, "enforceForClassMembers": true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFtcImVycm9yXCIsIHsgXCJnZXRXaXRob3V0U2V0XCI6IHRydWUsIFwiZW5mb3JjZUZvckNsYXNzTWVtYmVyc1wiOiB0cnVlIH1dKi9cblxuY2xhc3MgRm9vIHtcbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbn1cblxuY2xhc3MgQmFyIHtcbiAgICBzdGF0aWMgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59XG5cbmNvbnN0IEJheiA9IGNsYXNzIHtcbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbiAgICBzdGF0aWMgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59In0=)

```
/*eslint accessor-pairs: ["error", { "getWithoutSet": true, "enforceForClassMembers": true }]*/

class Foo {
    get a() {
        return this.val;
    }
}

class Bar {
    static get a() {
        return this.val;
    }
}

const Baz = class {
    get a() {
        return this.val;
    }
    static set a(value) {
        this.val = value;
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
```

Examples of incorrect code for `{ "setWithoutGet": true, "enforceForClassMembers": true }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFtcImVycm9yXCIsIHsgXCJzZXRXaXRob3V0R2V0XCI6IHRydWUsIFwiZW5mb3JjZUZvckNsYXNzTWVtYmVyc1wiOiB0cnVlIH1dKi9cblxuY2xhc3MgRm9vIHtcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn1cblxuY29uc3QgQmFyID0gY2xhc3Mge1xuICAgIHN0YXRpYyBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn0ifQ==)

```
/*eslint accessor-pairs: ["error", { "setWithoutGet": true, "enforceForClassMembers": true }]*/

class Foo {
    set a(value) {
        this.val = value;
    }
}

const Bar = class {
    static set a(value) {
        this.val = value;
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
```

When `enforceForClassMembers` is set to `false`, this rule ignores classes.

Examples of correct code for `{ "getWithoutSet": true, "setWithoutGet": true, "enforceForClassMembers": false }`:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgYWNjZXNzb3ItcGFpcnM6IFtcImVycm9yXCIsIHtcbiAgICBcImdldFdpdGhvdXRTZXRcIjogdHJ1ZSwgXCJzZXRXaXRob3V0R2V0XCI6IHRydWUsIFwiZW5mb3JjZUZvckNsYXNzTWVtYmVyc1wiOiBmYWxzZVxufV0qL1xuXG5jbGFzcyBGb28ge1xuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufVxuXG5jbGFzcyBCYXIge1xuICAgIHN0YXRpYyBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn1cblxuY29uc3QgQmF6ID0gY2xhc3Mge1xuICAgIHN0YXRpYyBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbn1cblxuY29uc3QgUXV1eCA9IGNsYXNzIHtcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn0ifQ==)

```
/*eslint accessor-pairs: ["error", {
    "getWithoutSet": true, "setWithoutGet": true, "enforceForClassMembers": false
}]*/

class Foo {
    get a() {
        return this.val;
    }
}

class Bar {
    static set a(value) {
        this.val = value;
    }
}

const Baz = class {
    static get a() {
        return this.val;
    }
}

const Quux = class {
    set a(value) {
        this.val = value;
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
```

### enforceForTSTypes

When `enforceForTSTypes` is set to `true`:

- `"getWithoutSet": true` will also warn for getters without setters in TypeScript types.
- `"setWithoutGet": true` will also warn for setters without getters in TypeScript types.

Examples of incorrect code for `{ "getWithoutSet": true, "enforceForTSTypes": true }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBhY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwgeyBcImdldFdpdGhvdXRTZXRcIjogdHJ1ZSwgXCJlbmZvcmNlRm9yVFNUeXBlc1wiOiB0cnVlIH1dKi9cblxuaW50ZXJmYWNlIEkge1xuICAgIGdldCBhKCk6IHN0cmluZ1xufVxuXG50eXBlIFQgPSB7XG4gICAgZ2V0IGEoKTogbnVtYmVyXG59In0=)

```
/*eslint accessor-pairs: ["error", { "getWithoutSet": true, "enforceForTSTypes": true }]*/

interface I {
    get a(): string
}

type T = {
    get a(): number
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

Examples of incorrect code for `{ "setWithoutGet": true, "enforceForTSTypes": true }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBhY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwgeyBcInNldFdpdGhvdXRHZXRcIjogdHJ1ZSwgXCJlbmZvcmNlRm9yVFNUeXBlc1wiOiB0cnVlIH1dKi9cblxuaW50ZXJmYWNlIEkge1xuICAgIHNldCBhKHZhbHVlOiB1bmtub3duKTogdm9pZFxufVxuXG50eXBlIFQgPSB7XG4gICAgc2V0IGEodmFsdWU6IHVua25vd24pOiB2b2lkXG59In0=)

```
/*eslint accessor-pairs: ["error", { "setWithoutGet": true, "enforceForTSTypes": true }]*/

interface I {
    set a(value: unknown): void
}

type T = {
    set a(value: unknown): void
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

When `enforceForTSTypes` is set to `false`, this rule ignores TypeScript types.

Examples of correct code for `{ "getWithoutSet": true, "setWithoutGet": true, "enforceForTSTypes": false }`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBhY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwge1xuICAgIFwiZ2V0V2l0aG91dFNldFwiOiB0cnVlLCBcInNldFdpdGhvdXRHZXRcIjogdHJ1ZSwgXCJlbmZvcmNlRm9yVFNUeXBlc1wiOiBmYWxzZVxufV0qL1xuXG5pbnRlcmZhY2UgSSB7XG4gICAgZ2V0IGEoKTogc3RyaW5nXG59XG5cbnR5cGUgVCA9IHtcbiAgICBzZXQgYSh2YWx1ZTogdW5rbm93bik6IHZvaWRcbn0ifQ==)

```
/*eslint accessor-pairs: ["error", {
    "getWithoutSet": true, "setWithoutGet": true, "enforceForTSTypes": false
}]*/

interface I {
    get a(): string
}

type T = {
    set a(value: unknown): void
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

## Known Limitations

Due to the limits of static analysis, this rule does not account for possible side effects and in certain cases might not report a missing pair for a getter/setter that has a computed key, like in the following example:

```
/*eslint accessor-pairs: "error"*/

const z = 1;

// no warnings
const a = {
    get [z++]() {
        return this.val;
    },
    set [z++](value) {
        this.val = value;
    }
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
```

Copy code to clipboard

Also, this rule does not disallow duplicate keys in object literals and class definitions, and in certain cases with duplicate keys might not report a missing pair for a getter/setter, like in the following example:

```
/*eslint accessor-pairs: "error"*/

// no warnings
const b = {
    get a() {
        return this.val;
    },
    a: 1,
    set a(value) {
        this.val = value;
    }
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
```

Copy code to clipboard

The code above creates an object with just a setter for the property `"a"`.

See [no-dupe-keys](no-dupe-keys) if you also want to disallow duplicate keys in object literals.

See [no-dupe-class-members](no-dupe-class-members) if you also want to disallow duplicate names in class definitions.

## When Not To Use It

You can turn this rule off if you are not concerned with the simultaneous presence of setters and getters on objects.

## Related Rules

- [no-dupe-keys](/docs/latest/rules/no-dupe-keys)
- [no-dupe-class-members](/docs/latest/rules/no-dupe-class-members)

## Version

This rule was introduced in ESLint v0.22.0.

## Further Reading

[setter - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 developer.mozilla.org[getter - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 developer.mozilla.org[Working with objects - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/accessor-pairs.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/accessor-pairs.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/accessor-pairs.md
                    
                
                )
