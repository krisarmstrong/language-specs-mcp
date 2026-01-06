# no-loop-func

Disallow function declarations that contain unsafe references inside loop statements

## Table of Contents

1. [Rule Details](#rule-details)
2. [Known Limitations](#known-limitations)
3. [Version](#version)
4. [Resources](#resources)

Writing functions within loops tends to result in errors due to the way the function creates a closure around the loop. For example:

```
for (var i = 0; i < 10; i++) {
    funcs[i] = function() {
        return i;
    };
}
1
2
3
4
5
```

Copy code to clipboard

In this case, you would expect each function created within the loop to return a different number. In reality, each function returns 10, because that was the last value of `i` in the scope.

`let` or `const` mitigate this problem.

```
for (let i = 0; i < 10; i++) {
    funcs[i] = function() {
        return i;
    };
}
1
2
3
4
5
```

Copy code to clipboard

In this case, each function created within the loop returns a different number as expected.

## Rule Details

This error is raised to highlight a piece of code that may not work as you expect it to and could also indicate a misunderstanding of how the language works. Your code may run without any problems if you do not fix this error, but in some situations it could behave unexpectedly.

This rule disallows any function within a loop that contains unsafe references (e.g. to modified variables from the outer scope). This rule ignores IIFEs but not async or generator functions.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9vcC1mdW5jOiBcImVycm9yXCIqL1xuXG52YXIgaSA9IDA7XG53aGlsZShpIDwgNSkge1xuICAgIHZhciBhID0gZnVuY3Rpb24oKSB7IHJldHVybiBpOyB9O1xuICAgIGEoKTtcblxuICAgIGkrKztcbn1cblxudmFyIGkgPSAwO1xuZG8ge1xuICAgIGZ1bmN0aW9uIGEoKSB7IHJldHVybiBpOyB9O1xuICAgIGEoKTtcblxuICAgIGkrK1xufSB3aGlsZSAoaSA8IDUpO1xuXG5sZXQgZm9vID0gMDtcbmZvciAobGV0IGkgPSAwOyBpIDwgMTA7ICsraSkge1xuICAgIC8vQmFkLCBgZm9vYCBpcyBub3QgaW4gdGhlIGxvb3AtYmxvY2sncyBzY29wZSBhbmQgYGZvb2AgaXMgbW9kaWZpZWQgaW4vYWZ0ZXIgdGhlIGxvb3BcbiAgICBzZXRUaW1lb3V0KCgpID0+IGNvbnNvbGUubG9nKGZvbykpO1xuICAgIGZvbyArPSAxO1xufVxuXG5mb3IgKGxldCBpID0gMDsgaSA8IDEwOyArK2kpIHtcbiAgICAvL0JhZCwgYGZvb2AgaXMgbm90IGluIHRoZSBsb29wLWJsb2NrJ3Mgc2NvcGUgYW5kIGBmb29gIGlzIG1vZGlmaWVkIGluL2FmdGVyIHRoZSBsb29wXG4gICAgc2V0VGltZW91dCgoKSA9PiBjb25zb2xlLmxvZyhmb28pKTtcbn1cbmZvbyA9IDEwMDtcblxudmFyIGFyciA9IFtdO1xuXG5mb3IgKHZhciBpID0gMDsgaSA8IDU7IGkrKykge1xuICAgIGFyci5wdXNoKChmID0+IGYpKCgpID0+IGkpKTtcbn1cblxuZm9yICh2YXIgaSA9IDA7IGkgPCA1OyBpKyspIHtcbiAgICBhcnIucHVzaCgoKCkgPT4ge1xuICAgICAgICByZXR1cm4gKCkgPT4gaTtcbiAgICB9KSgpKTtcbn1cblxuZm9yICh2YXIgaSA9IDA7IGkgPCA1OyBpKyspIHtcbiAgICAoZnVuY3Rpb24gZnVuICgpIHtcbiAgICAgICAgaWYgKGFyci5pbmNsdWRlcyhmdW4pKSByZXR1cm4gaTtcbiAgICAgICAgZWxzZSBhcnIucHVzaChmdW4pO1xuICAgIH0pKCk7XG59In0=)

```
/*eslint no-loop-func: "error"*/

var i = 0;
while(i < 5) {
    var a = function() { return i; };
    a();

    i++;
}

var i = 0;
do {
    function a() { return i; };
    a();

    i++
} while (i < 5);

let foo = 0;
for (let i = 0; i < 10; ++i) {
    //Bad, `foo` is not in the loop-block's scope and `foo` is modified in/after the loop
    setTimeout(() => console.log(foo));
    foo += 1;
}

for (let i = 0; i < 10; ++i) {
    //Bad, `foo` is not in the loop-block's scope and `foo` is modified in/after the loop
    setTimeout(() => console.log(foo));
}
foo = 100;

var arr = [];

for (var i = 0; i < 5; i++) {
    arr.push((f => f)(() => i));
}

for (var i = 0; i < 5; i++) {
    arr.push((() => {
        return () => i;
    })());
}

for (var i = 0; i < 5; i++) {
    (function fun () {
        if (arr.includes(fun)) return i;
        else arr.push(fun);
    })();
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tbG9vcC1mdW5jOiBcImVycm9yXCIqL1xuXG52YXIgYSA9IGZ1bmN0aW9uKCkge307XG5cbmZvciAodmFyIGk9MTA7IGk7IGktLSkge1xuICAgIGEoKTtcbn1cblxuZm9yICh2YXIgaT0xMDsgaTsgaS0tKSB7XG4gICAgdmFyIGEgPSBmdW5jdGlvbigpIHt9OyAvLyBPSywgbm8gcmVmZXJlbmNlcyB0byB2YXJpYWJsZXMgaW4gdGhlIG91dGVyIHNjb3Blcy5cbiAgICBhKCk7XG59XG5cbmZvciAobGV0IGk9MTA7IGk7IGktLSkge1xuICAgIHZhciBhID0gZnVuY3Rpb24oKSB7IHJldHVybiBpOyB9OyAvLyBPSywgYWxsIHJlZmVyZW5jZXMgYXJlIHJlZmVycmluZyB0byBibG9jayBzY29wZWQgdmFyaWFibGVzIGluIHRoZSBsb29wLlxuICAgIGEoKTtcbn1cblxuZm9yIChjb25zdCBpIG9mIGZvbykge1xuICAgIHZhciBhID0gZnVuY3Rpb24oKSB7IHJldHVybiBpOyB9OyAvLyBPSywgYWxsIHJlZmVyZW5jZXMgYXJlIHJlZmVycmluZyB0byBibG9jayBzY29wZWQgdmFyaWFibGVzIGluIHRoZSBsb29wLlxuICAgIGEoKTtcbn1cblxuZm9yICh1c2luZyBpIG9mIGZvbykge1xuICAgIHZhciBhID0gZnVuY3Rpb24oKSB7IHJldHVybiBpOyB9OyAvLyBPSywgYWxsIHJlZmVyZW5jZXMgYXJlIHJlZmVycmluZyB0byBibG9jayBzY29wZWQgdmFyaWFibGVzIGluIHRoZSBsb29wLlxuICAgIGEoKTtcbn1cblxuZm9yICh2YXIgaT0xMDsgaTsgaS0tKSB7XG4gICAgY29uc3QgZm9vID0gZ2V0c29tZXRoaW5nKGkpO1xuICAgIHZhciBhID0gZnVuY3Rpb24oKSB7IHJldHVybiBmb287IH07IC8vIE9LLCBhbGwgcmVmZXJlbmNlcyBhcmUgcmVmZXJyaW5nIHRvIGJsb2NrIHNjb3BlZCB2YXJpYWJsZXMgaW4gdGhlIGxvb3AuXG4gICAgYSgpO1xufVxuXG5mb3IgKHZhciBpPTEwOyBpOyBpLS0pIHtcbiAgICB1c2luZyBmb28gPSBnZXRzb21ldGhpbmcoaSk7XG4gICAgdmFyIGEgPSBmdW5jdGlvbigpIHsgcmV0dXJuIGZvbzsgfTsgLy8gT0ssIGFsbCByZWZlcmVuY2VzIGFyZSByZWZlcnJpbmcgdG8gYmxvY2sgc2NvcGVkIHZhcmlhYmxlcyBpbiB0aGUgbG9vcC5cbiAgICBhKCk7XG59XG5cbmZvciAodmFyIGk9MTA7IGk7IGktLSkge1xuICAgIGF3YWl0IHVzaW5nIGZvbyA9IGdldHNvbWV0aGluZyhpKTtcbiAgICB2YXIgYSA9IGZ1bmN0aW9uKCkgeyByZXR1cm4gZm9vOyB9OyAvLyBPSywgYWxsIHJlZmVyZW5jZXMgYXJlIHJlZmVycmluZyB0byBibG9jayBzY29wZWQgdmFyaWFibGVzIGluIHRoZSBsb29wLlxuICAgIGEoKTtcbn1cblxudmFyIGZvbyA9IDEwMDtcbmZvciAobGV0IGk9MTA7IGk7IGktLSkge1xuICAgIHZhciBhID0gZnVuY3Rpb24oKSB7IHJldHVybiBmb287IH07IC8vIE9LLCBhbGwgcmVmZXJlbmNlcyBhcmUgcmVmZXJyaW5nIHRvIG5ldmVyIG1vZGlmaWVkIHZhcmlhYmxlcy5cbiAgICBhKCk7XG59XG4vLy4uLiBubyBtb2RpZmljYXRpb25zIG9mIGZvbyBhZnRlciB0aGlzIGxvb3AgLi4uXG5cbnZhciBhcnIgPSBbXTtcblxuZm9yICh2YXIgaT0xMDsgaTsgaS0tKSB7XG4gICAgKGZ1bmN0aW9uKCkgeyByZXR1cm4gaTsgfSkoKTtcbn1cblxuZm9yICh2YXIgaSA9IDA7IGkgPCA1OyBpKyspIHtcbiAgICBhcnIucHVzaCgoZiA9PiBmKSgoKCkgPT4gaSkoKSkpO1xufVxuXG5mb3IgKHZhciBpID0gMDsgaSA8IDU7IGkrKykge1xuICAgIGFyci5wdXNoKCgoKSA9PiB7XG4gICAgICAgIHJldHVybiAoKCkgPT4gaSkoKTtcbiAgICB9KSgpKTtcbn0ifQ==)

```
/*eslint no-loop-func: "error"*/

var a = function() {};

for (var i=10; i; i--) {
    a();
}

for (var i=10; i; i--) {
    var a = function() {}; // OK, no references to variables in the outer scopes.
    a();
}

for (let i=10; i; i--) {
    var a = function() { return i; }; // OK, all references are referring to block scoped variables in the loop.
    a();
}

for (const i of foo) {
    var a = function() { return i; }; // OK, all references are referring to block scoped variables in the loop.
    a();
}

for (using i of foo) {
    var a = function() { return i; }; // OK, all references are referring to block scoped variables in the loop.
    a();
}

for (var i=10; i; i--) {
    const foo = getsomething(i);
    var a = function() { return foo; }; // OK, all references are referring to block scoped variables in the loop.
    a();
}

for (var i=10; i; i--) {
    using foo = getsomething(i);
    var a = function() { return foo; }; // OK, all references are referring to block scoped variables in the loop.
    a();
}

for (var i=10; i; i--) {
    await using foo = getsomething(i);
    var a = function() { return foo; }; // OK, all references are referring to block scoped variables in the loop.
    a();
}

var foo = 100;
for (let i=10; i; i--) {
    var a = function() { return foo; }; // OK, all references are referring to never modified variables.
    a();
}
//... no modifications of foo after this loop ...

var arr = [];

for (var i=10; i; i--) {
    (function() { return i; })();
}

for (var i = 0; i < 5; i++) {
    arr.push((f => f)((() => i)()));
}

for (var i = 0; i < 5; i++) {
    arr.push((() => {
        return (() => i)();
    })());
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
```

This rule additionally supports TypeScript type syntax.

Examples of correct TypeScript code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby1sb29wLWZ1bmM6IFwiZXJyb3JcIiovXG5cbnR5cGUgTXlUeXBlID0gMTtcbmxldCBzb21lQXJyYXk6IE15VHlwZVtdID0gW107XG5mb3IgKGxldCBpID0gMDsgaSA8IDEwOyBpICs9IDEpIHtcblx0c29tZUFycmF5ID0gc29tZUFycmF5LmZpbHRlcigoaXRlbTogTXlUeXBlKSA9PiAhIWl0ZW0pO1xufSJ9)

```
/*eslint no-loop-func: "error"*/

type MyType = 1;
let someArray: MyType[] = [];
for (let i = 0; i < 10; i += 1) {
	someArray = someArray.filter((item: MyType) => !!item);
}
1
2
3
4
5
6
7
```

## Known Limitations

The rule cannot identify whether the function instance is just immediately invoked and then discarded, or possibly stored for later use.

```
const foo = [1, 2, 3, 4];
var i = 0;

while(foo.some(e => e > i)){
    i += 1;
}
1
2
3
4
5
6
```

Copy code to clipboard

Here the `some` method immediately executes the callback function for each element in the array and then discards the function instance. The function is not stored or reused beyond the scope of the loop iteration. So, this will work as intended.

`eslint-disable` comments can be used in such cases.

## Version

This rule was introduced in ESLint v0.0.9.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-loop-func.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-loop-func.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-loop-func.md
                    
                
                )
