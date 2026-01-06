# no-dupe-class-members

Disallow duplicate class members

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Examples](#examples)
3. [When Not To Use It](#when-not-to-use-it)
4. [Handled by TypeScript](#handled_by_typescript)
5. [Version](#version)
6. [Resources](#resources)

If there are declarations of the same name in class members, the last declaration overwrites other declarations silently. It can cause unexpected behaviors.

```
class Foo {
  bar() { console.log("hello"); }
  bar() { console.log("goodbye"); }
}

const foo = new Foo();
foo.bar(); // goodbye
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

This rule is aimed to flag the use of duplicate names in class members.

## Examples

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1jbGFzcy1tZW1iZXJzOiBcImVycm9yXCIqL1xuXG5jbGFzcyBBIHtcbiAgYmFyKCkgeyB9XG4gIGJhcigpIHsgfVxufVxuXG5jbGFzcyBCIHtcbiAgYmFyKCkgeyB9XG4gIGdldCBiYXIoKSB7IH1cbn1cblxuY2xhc3MgQyB7XG4gIGJhcjtcbiAgYmFyO1xufVxuXG5jbGFzcyBEIHtcbiAgYmFyO1xuICBiYXIoKSB7IH1cbn1cblxuY2xhc3MgRSB7XG4gIHN0YXRpYyBiYXIoKSB7IH1cbiAgc3RhdGljIGJhcigpIHsgfVxufSJ9)

```
/*eslint no-dupe-class-members: "error"*/

class A {
  bar() { }
  bar() { }
}

class B {
  bar() { }
  get bar() { }
}

class C {
  bar;
  bar;
}

class D {
  bar;
  bar() { }
}

class E {
  static bar() { }
  static bar() { }
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZHVwZS1jbGFzcy1tZW1iZXJzOiBcImVycm9yXCIqL1xuXG5jbGFzcyBBIHtcbiAgYmFyKCkgeyB9XG4gIHF1eCgpIHsgfVxufVxuXG5jbGFzcyBCIHtcbiAgZ2V0IGJhcigpIHsgfVxuICBzZXQgYmFyKHZhbHVlKSB7IH1cbn1cblxuY2xhc3MgQyB7XG4gIGJhcjtcbiAgcXV4O1xufVxuXG5jbGFzcyBEIHtcbiAgYmFyO1xuICBxdXgoKSB7IH1cbn1cblxuY2xhc3MgRSB7XG4gIHN0YXRpYyBiYXIoKSB7IH1cbiAgYmFyKCkgeyB9XG59In0=)

```
/*eslint no-dupe-class-members: "error"*/

class A {
  bar() { }
  qux() { }
}

class B {
  get bar() { }
  set bar(value) { }
}

class C {
  bar;
  qux;
}

class D {
  bar;
  qux() { }
}

class E {
  static bar() { }
  bar() { }
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
```

This rule additionally supports TypeScript type syntax. It has support for TypeScript’s method overload definitions.

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKiBlc2xpbnQgbm8tZHVwZS1jbGFzcy1tZW1iZXJzOiBcImVycm9yXCIgKi9cblxuY2xhc3MgQSB7XG5cdGZvbyh2YWx1ZTogc3RyaW5nKTogdm9pZDtcblx0Zm9vKHZhbHVlOiBudW1iZXIpOiB2b2lkO1xuXHRmb28odmFsdWU6IHN0cmluZyB8IG51bWJlcikge30gLy8g4pyFIFRoaXMgaXMgdGhlIGFjdHVhbCBpbXBsZW1lbnRhdGlvbi5cbn0ifQ==)

```
/* eslint no-dupe-class-members: "error" */

class A {
	foo(value: string): void;
	foo(value: number): void;
	foo(value: string | number) {} // ✅ This is the actual implementation.
}
1
2
3
4
5
6
7
```

## When Not To Use It

This rule should not be used in ES3/5 environments.

In ES2015 (ES6) or later, if you don’t want to be notified about duplicate names in class members, you can safely disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

## Version

This rule was introduced in ESLint v1.2.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-dupe-class-members.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-dupe-class-members.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-dupe-class-members.md
                    
                
                )
