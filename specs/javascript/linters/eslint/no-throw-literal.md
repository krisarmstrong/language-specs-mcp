# no-throw-literal

Disallow throwing literals as exceptions

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [Version](#version)
4. [Resources](#resources)

It is considered good practice to only `throw` the `Error` object itself or an object using the `Error` object as base objects for user-defined exceptions. The fundamental benefit of `Error` objects is that they automatically keep track of where they were built and originated.

This rule restricts what can be thrown as an exception. When it was first created, it only prevented literals from being thrown (hence the name), but it has now been expanded to only allow expressions which have a possibility of being an `Error` object.

## Rule Details

This rule is aimed at maintaining consistency when throwing exception by disallowing to throw literals and other expressions which cannot possibly be an `Error` object.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGhyb3ctbGl0ZXJhbDogXCJlcnJvclwiKi9cblxudGhyb3cgXCJlcnJvclwiO1xuXG50aHJvdyAwO1xuXG50aHJvdyB1bmRlZmluZWQ7XG5cbnRocm93IG51bGw7XG5cbmNvbnN0IGVyciA9IG5ldyBFcnJvcigpO1xudGhyb3cgXCJhbiBcIiArIGVycjtcbi8vIGVyciBpcyByZWNhc3QgdG8gYSBzdHJpbmcgbGl0ZXJhbFxuXG5jb25zdCBlcjIgPSBuZXcgRXJyb3IoKTtcbnRocm93IGAke2VycjJ9YFxuIn0=)

```
/*eslint no-throw-literal: "error"*/

throw "error";

throw 0;

throw undefined;

throw null;

const err = new Error();
throw "an " + err;
// err is recast to a string literal

const er2 = new Error();
throw `${err2}`

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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGhyb3ctbGl0ZXJhbDogXCJlcnJvclwiKi9cblxudGhyb3cgbmV3IEVycm9yKCk7XG5cbnRocm93IG5ldyBFcnJvcihcImVycm9yXCIpO1xuXG5jb25zdCBlID0gbmV3IEVycm9yKFwiZXJyb3JcIik7XG50aHJvdyBlO1xuXG50cnkge1xuICAgIHRocm93IG5ldyBFcnJvcihcImVycm9yXCIpO1xufSBjYXRjaCAoZSkge1xuICAgIHRocm93IGU7XG59In0=)

```
/*eslint no-throw-literal: "error"*/

throw new Error();

throw new Error("error");

const e = new Error("error");
throw e;

try {
    throw new Error("error");
} catch (e) {
    throw e;
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

## Known Limitations

Due to the limits of static analysis, this rule cannot guarantee that you will only throw `Error` objects.

Examples of correct code for this rule, but which do not throw an `Error` object:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdGhyb3ctbGl0ZXJhbDogXCJlcnJvclwiKi9cblxuY29uc3QgZXJyID0gXCJlcnJvclwiO1xudGhyb3cgZXJyO1xuXG5mdW5jdGlvbiBmb28oYmFyKSB7XG4gICAgY29uc29sZS5sb2coYmFyKTtcbn1cbnRocm93IGZvbyhcImVycm9yXCIpO1xuXG50aHJvdyBuZXcgU3RyaW5nKFwiZXJyb3JcIik7XG5cbmNvbnN0IGJheiA9IHtcbiAgICBiYXI6IFwiZXJyb3JcIlxufTtcbnRocm93IGJhei5iYXI7In0=)

```
/*eslint no-throw-literal: "error"*/

const err = "error";
throw err;

function foo(bar) {
    console.log(bar);
}
throw foo("error");

throw new String("error");

const baz = {
    bar: "error"
};
throw baz.bar;
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

## Version

This rule was introduced in ESLint v0.15.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-throw-literal.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-throw-literal.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-throw-literal.md
                    
                
                )
