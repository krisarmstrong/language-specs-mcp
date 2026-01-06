# grouped-accessor-pairs

Require grouped accessor pairs in object literals and classes

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [getBeforeSet](#getbeforeset)
  2. [setBeforeGet](#setbeforeget)
  3. [enforceForTSTypes](#enforcefortstypes)

3. [Known Limitations](#known-limitations)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

A getter and setter for the same property don’t necessarily have to be defined adjacent to each other.

For example, the following statements would create the same object:

```
const o = {
    get a() {
        return this.val;
    },
    set a(value) {
        this.val = value;
    },
    b: 1
};

const o1 = {
    get a() {
        return this.val;
    },
    b: 1,
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
13
14
15
16
17
18
19
```

Copy code to clipboard

While it is allowed to define the pair for a getter or a setter anywhere in an object or class definition, it’s considered a best practice to group accessor functions for the same property.

In other words, if a property has a getter and a setter, the setter should be defined right after the getter, or vice versa.

## Rule Details

This rule requires grouped definitions of accessor functions for the same property in object literals, class declarations and class expressions.

Optionally, this rule can also enforce consistent order (`getBeforeSet` or `setBeforeGet`).

This rule does not enforce the existence of the pair for a getter or a setter. See [accessor-pairs](accessor-pairs) if you also want to enforce getter/setter pairs.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3JvdXBlZC1hY2Nlc3Nvci1wYWlyczogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0ge1xuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfSxcbiAgICBiOiAxLFxuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuY29uc3QgYmFyID0ge1xuICAgIHNldCBiKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfSxcbiAgICBhOiAxLFxuICAgIGdldCBiKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufVxuXG5jbGFzcyBGb28ge1xuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxuICAgIGIoKXt9XG4gICAgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59XG5cbmNvbnN0IEJhciA9IGNsYXNzIHtcbiAgICBzdGF0aWMgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG4gICAgYigpe31cbiAgICBzdGF0aWMgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59In0=)

```
/*eslint grouped-accessor-pairs: "error"*/

const foo = {
    get a() {
        return this.val;
    },
    b: 1,
    set a(value) {
        this.val = value;
    }
};

const bar = {
    set b(value) {
        this.val = value;
    },
    a: 1,
    get b() {
        return this.val;
    }
}

class Foo {
    set a(value) {
        this.val = value;
    }
    b(){}
    get a() {
        return this.val;
    }
}

const Bar = class {
    static get a() {
        return this.val;
    }
    b(){}
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3JvdXBlZC1hY2Nlc3Nvci1wYWlyczogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0ge1xuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfSxcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH0sXG4gICAgYjogMVxufTtcblxuY29uc3QgYmFyID0ge1xuICAgIHNldCBiKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfSxcbiAgICBnZXQgYigpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH0sXG4gICAgYTogMVxufVxuXG5jbGFzcyBGb28ge1xuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxuICAgIGIoKXt9XG59XG5cbmNvbnN0IEJhciA9IGNsYXNzIHtcbiAgICBzdGF0aWMgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG4gICAgc3RhdGljIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxuICAgIGIoKXt9XG59In0=)

```
/*eslint grouped-accessor-pairs: "error"*/

const foo = {
    get a() {
        return this.val;
    },
    set a(value) {
        this.val = value;
    },
    b: 1
};

const bar = {
    set b(value) {
        this.val = value;
    },
    get b() {
        return this.val;
    },
    a: 1
}

class Foo {
    set a(value) {
        this.val = value;
    }
    get a() {
        return this.val;
    }
    b(){}
}

const Bar = class {
    static get a() {
        return this.val;
    }
    static set a(value) {
        this.val = value;
    }
    b(){}
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
```

## Options

This rule has a primary string and an optional secondary object option. The string option specifies the order:

- `"anyOrder"` (default) does not enforce order.
- `"getBeforeSet"` if a property has both getter and setter, requires the getter to be defined before the setter.
- `"setBeforeGet"` if a property has both getter and setter, requires the setter to be defined before the getter.

The optional object option allows opting-in to check additional object-likes:

- `enforceForTSTypes`: also check TypeScript types (interfaces and type literals)

### getBeforeSet

Examples of incorrect code for this rule with the `"getBeforeSet"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3JvdXBlZC1hY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwgXCJnZXRCZWZvcmVTZXRcIl0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9LFxuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufTtcblxuY2xhc3MgRm9vIHtcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbn1cblxuY29uc3QgQmFyID0gY2xhc3Mge1xuICAgIHN0YXRpYyBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbiAgICBzdGF0aWMgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59In0=)

```
/*eslint grouped-accessor-pairs: ["error", "getBeforeSet"]*/

const foo = {
    set a(value) {
        this.val = value;
    },
    get a() {
        return this.val;
    }
};

class Foo {
    set a(value) {
        this.val = value;
    }
    get a() {
        return this.val;
    }
}

const Bar = class {
    static set a(value) {
        this.val = value;
    }
    static get a() {
        return this.val;
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
```

Examples of correct code for this rule with the `"getBeforeSet"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3JvdXBlZC1hY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwgXCJnZXRCZWZvcmVTZXRcIl0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9LFxuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuY2xhc3MgRm9vIHtcbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn1cblxuY29uc3QgQmFyID0gY2xhc3Mge1xuICAgIHN0YXRpYyBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbiAgICBzdGF0aWMgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59In0=)

```
/*eslint grouped-accessor-pairs: ["error", "getBeforeSet"]*/

const foo = {
    get a() {
        return this.val;
    },
    set a(value) {
        this.val = value;
    }
};

class Foo {
    get a() {
        return this.val;
    }
    set a(value) {
        this.val = value;
    }
}

const Bar = class {
    static get a() {
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
23
24
25
26
27
28
```

### setBeforeGet

Examples of incorrect code for this rule with the `"setBeforeGet"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3JvdXBlZC1hY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwgXCJzZXRCZWZvcmVHZXRcIl0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9LFxuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuY2xhc3MgRm9vIHtcbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbn1cblxuY29uc3QgQmFyID0gY2xhc3Mge1xuICAgIHN0YXRpYyBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbiAgICBzdGF0aWMgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59In0=)

```
/*eslint grouped-accessor-pairs: ["error", "setBeforeGet"]*/

const foo = {
    get a() {
        return this.val;
    },
    set a(value) {
        this.val = value;
    }
};

class Foo {
    get a() {
        return this.val;
    }
    set a(value) {
        this.val = value;
    }
}

const Bar = class {
    static get a() {
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
23
24
25
26
27
28
```

Examples of correct code for this rule with the `"setBeforeGet"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgZ3JvdXBlZC1hY2Nlc3Nvci1wYWlyczogW1wiZXJyb3JcIiwgXCJzZXRCZWZvcmVHZXRcIl0qL1xuXG5jb25zdCBmb28gPSB7XG4gICAgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9LFxuICAgIGdldCBhKCkge1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufTtcblxuY2xhc3MgRm9vIHtcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbiAgICBnZXQgYSgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMudmFsO1xuICAgIH1cbn1cblxuY29uc3QgQmFyID0gY2xhc3Mge1xuICAgIHN0YXRpYyBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlO1xuICAgIH1cbiAgICBzdGF0aWMgZ2V0IGEoKSB7XG4gICAgICAgIHJldHVybiB0aGlzLnZhbDtcbiAgICB9XG59In0=)

```
/*eslint grouped-accessor-pairs: ["error", "setBeforeGet"]*/

const foo = {
    set a(value) {
        this.val = value;
    },
    get a() {
        return this.val;
    }
};

class Foo {
    set a(value) {
        this.val = value;
    }
    get a() {
        return this.val;
    }
}

const Bar = class {
    static set a(value) {
        this.val = value;
    }
    static get a() {
        return this.val;
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
```

### enforceForTSTypes

Examples of incorrect code for this rule with `["anyOrder", { enforceForTSTypes: true }]`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBncm91cGVkLWFjY2Vzc29yLXBhaXJzOiBbXCJlcnJvclwiLCBcImFueU9yZGVyXCIsIHsgZW5mb3JjZUZvclRTVHlwZXM6IHRydWUgfV0gKi9cblxuaW50ZXJmYWNlIEkge1xuICAgIGdldCBhKCk6IHN0cmluZyxcbiAgICBiZXR3ZWVuOiB0cnVlLFxuICAgIHNldCBhKHZhbHVlOiBzdHJpbmcpOiB2b2lkXG59XG5cbnR5cGUgVCA9IHtcbiAgICBnZXQgYSgpOiBzdHJpbmcsXG4gICAgYmV0d2VlbjogdHJ1ZSxcbiAgICBzZXQgYSh2YWx1ZTogc3RyaW5nKTogdm9pZFxufTsifQ==)

```
/*eslint grouped-accessor-pairs: ["error", "anyOrder", { enforceForTSTypes: true }] */

interface I {
    get a(): string,
    between: true,
    set a(value: string): void
}

type T = {
    get a(): string,
    between: true,
    set a(value: string): void
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

Examples of correct code for this rule with `["anyOrder", { enforceForTSTypes: true }]`:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBncm91cGVkLWFjY2Vzc29yLXBhaXJzOiBbXCJlcnJvclwiLCBcImFueU9yZGVyXCIsIHsgZW5mb3JjZUZvclRTVHlwZXM6IHRydWUgfV0gKi9cblxuaW50ZXJmYWNlIEkge1xuICAgIGdldCBhKCk6IHN0cmluZyxcbiAgICBzZXQgYSh2YWx1ZTogc3RyaW5nKTogdm9pZCxcbn1cblxudHlwZSBUID0ge1xuICAgIHNldCBhKHZhbHVlOiBzdHJpbmcpOiB2b2lkLFxuICAgIGdldCBhKCk6IHN0cmluZyxcbn07In0=)

```
/*eslint grouped-accessor-pairs: ["error", "anyOrder", { enforceForTSTypes: true }] */

interface I {
    get a(): string,
    set a(value: string): void,
}

type T = {
    set a(value: string): void,
    get a(): string,
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
```

## Known Limitations

Due to the limits of static analysis, this rule does not account for possible side effects and in certain cases might require or miss to require grouping or order for getters/setters that have a computed key, like in the following example:

```
/*eslint grouped-accessor-pairs: "error"*/

let a = 1;

// false warning (false positive)
const foo = {
    get [a++]() {
        return this.val;
    },
    b: 1,
    set [a++](value) {
        this.val = value;
    }
};

// missed warning (false negative)
const bar = {
    get [++a]() {
        return this.val;
    },
    b: 1,
    set [a](value) {
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

Copy code to clipboard

Also, this rule does not report any warnings for properties that have duplicate getters or setters.

See [no-dupe-keys](no-dupe-keys) if you also want to disallow duplicate keys in object literals.

See [no-dupe-class-members](no-dupe-class-members) if you also want to disallow duplicate names in class definitions.

## Related Rules

- [accessor-pairs](/docs/latest/rules/accessor-pairs)
- [no-dupe-keys](/docs/latest/rules/no-dupe-keys)
- [no-dupe-class-members](/docs/latest/rules/no-dupe-class-members)

## Version

This rule was introduced in ESLint v6.7.0.

## Further Reading

[setter - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 developer.mozilla.org[getter - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 developer.mozilla.org[Classes - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/grouped-accessor-pairs.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/grouped-accessor-pairs.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/grouped-accessor-pairs.md
                    
                
                )
