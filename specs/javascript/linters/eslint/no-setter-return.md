# no-setter-return

Disallow returning values from setters

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Handled by TypeScript](#handled_by_typescript)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

Setters cannot return values.

While returning a value from a setter does not produce an error, the returned value is being ignored. Therefore, returning a value from a setter is either unnecessary or a possible error, since the returned value cannot be used.

## Rule Details

This rule disallows returning values from setters and reports `return` statements in setter functions.

Only `return` without a value is allowed, as it’s a control flow statement.

This rule checks setters in:

- Object literals.
- Class declarations and class expressions.
- Property descriptors in `Object.create`, `Object.defineProperty`, `Object.defineProperties`, and `Reflect.defineProperty` methods of the global objects.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2V0dGVyLXJldHVybjogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0ge1xuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgICAgIHJldHVybiB2YWx1ZTtcbiAgICB9XG59O1xuXG5jbGFzcyBGb28ge1xuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWUgKiAyO1xuICAgICAgICByZXR1cm4gdGhpcy52YWw7XG4gICAgfVxufVxuXG5jb25zdCBCYXIgPSBjbGFzcyB7XG4gICAgc3RhdGljIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIGlmICh2YWx1ZSA8IDApIHtcbiAgICAgICAgICAgIHRoaXMudmFsID0gMDtcbiAgICAgICAgICAgIHJldHVybiAwO1xuICAgICAgICB9XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuT2JqZWN0LmRlZmluZVByb3BlcnR5KGZvbywgXCJiYXJcIiwge1xuICAgIHNldCh2YWx1ZSkge1xuICAgICAgICBpZiAodmFsdWUgPCAwKSB7XG4gICAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59KTsifQ==)

```
/*eslint no-setter-return: "error"*/

const foo = {
    set a(value) {
        this.val = value;
        return value;
    }
};

class Foo {
    set a(value) {
        this.val = value * 2;
        return this.val;
    }
}

const Bar = class {
    static set a(value) {
        if (value < 0) {
            this.val = 0;
            return 0;
        }
        this.val = value;
    }
};

Object.defineProperty(foo, "bar", {
    set(value) {
        if (value < 0) {
            return false;
        }
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tc2V0dGVyLXJldHVybjogXCJlcnJvclwiKi9cblxuY29uc3QgZm9vID0ge1xuICAgIHNldCBhKHZhbHVlKSB7XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuY2xhc3MgRm9vIHtcbiAgICBzZXQgYSh2YWx1ZSkge1xuICAgICAgICB0aGlzLnZhbCA9IHZhbHVlICogMjtcbiAgICB9XG59XG5cbmNvbnN0IEJhciA9IGNsYXNzIHtcbiAgICBzdGF0aWMgc2V0IGEodmFsdWUpIHtcbiAgICAgICAgaWYgKHZhbHVlIDwgMCkge1xuICAgICAgICAgICAgdGhpcy52YWwgPSAwO1xuICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIHRoaXMudmFsID0gdmFsdWU7XG4gICAgfVxufTtcblxuT2JqZWN0LmRlZmluZVByb3BlcnR5KGZvbywgXCJiYXJcIiwge1xuICAgIHNldCh2YWx1ZSkge1xuICAgICAgICBpZiAodmFsdWUgPCAwKSB7XG4gICAgICAgICAgICB0aHJvdyBuZXcgRXJyb3IoXCJOZWdhdGl2ZSB2YWx1ZS5cIik7XG4gICAgICAgIH1cbiAgICAgICAgdGhpcy52YWwgPSB2YWx1ZTtcbiAgICB9XG59KTsifQ==)

```
/*eslint no-setter-return: "error"*/

const foo = {
    set a(value) {
        this.val = value;
    }
};

class Foo {
    set a(value) {
        this.val = value * 2;
    }
}

const Bar = class {
    static set a(value) {
        if (value < 0) {
            this.val = 0;
            return;
        }
        this.val = value;
    }
};

Object.defineProperty(foo, "bar", {
    set(value) {
        if (value < 0) {
            throw new Error("Negative value.");
        }
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

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Related Rules

- [getter-return](/docs/latest/rules/getter-return)

## Version

This rule was introduced in ESLint v6.7.0.

## Further Reading

[setter - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-setter-return.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-setter-return.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-setter-return.md
                    
                
                )
