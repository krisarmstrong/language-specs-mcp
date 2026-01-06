# curly

Enforce consistent brace style for all control statements

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [all](#all)
  2. [multi](#multi)
  3. [multi-line](#multi-line)
  4. [multi-or-nest](#multi-or-nest)
  5. [consistent](#consistent)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

JavaScript allows the omission of curly braces when a block contains only one statement. However, it is considered by many to be best practice to never omit curly braces around blocks, even when they are optional, because it can lead to bugs and reduces code clarity. So the following:

```
if (foo) foo++;
1
```

Copy code to clipboard

Can be rewritten as:

```
if (foo) {
    foo++;
}
1
2
3
```

Copy code to clipboard

There are, however, some who prefer to only use braces when there is more than one statement to be executed.

## Rule Details

This rule is aimed at preventing bugs and increasing code clarity by ensuring that block statements are wrapped in curly braces. It will warn when it encounters blocks that omit curly braces.

## Options

### all

Examples of incorrect code for the default `"all"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFwiZXJyb3JcIiovXG5cbmlmIChmb28pIGZvbysrO1xuXG53aGlsZSAoYmFyKVxuICAgIGJheigpO1xuXG5pZiAoZm9vKSB7XG4gICAgYmF6KCk7XG59IGVsc2UgcXV4KCk7In0=)

```
/*eslint curly: "error"*/

if (foo) foo++;

while (bar)
    baz();

if (foo) {
    baz();
} else qux();
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

Examples of correct code for the default `"all"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFwiZXJyb3JcIiovXG5cbmlmIChmb28pIHtcbiAgICBmb28rKztcbn1cblxud2hpbGUgKGJhcikge1xuICAgIGJheigpO1xufVxuXG5pZiAoZm9vKSB7XG4gICAgYmF6KCk7XG59IGVsc2Uge1xuICAgIHF1eCgpO1xufSJ9)

```
/*eslint curly: "error"*/

if (foo) {
    foo++;
}

while (bar) {
    baz();
}

if (foo) {
    baz();
} else {
    qux();
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

### multi

By default, this rule warns whenever `if`, `else`, `for`, `while`, or `do` are used without block statements as their body. However, you can specify that block statements should be used only when there are multiple statements in the block and warn when there is only one statement in the block.

Examples of incorrect code for the `"multi"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGlcIl0qL1xuXG5pZiAoZm9vKSB7XG4gICAgZm9vKys7XG59XG5cbmlmIChmb28pIGJhcigpO1xuZWxzZSB7XG4gICAgZm9vKys7XG59XG5cbndoaWxlICh0cnVlKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuZm9yIChsZXQgaT0wOyBpIDwgaXRlbXMubGVuZ3RoOyBpKyspIHtcbiAgICBkb1NvbWV0aGluZygpO1xufSJ9)

```
/*eslint curly: ["error", "multi"]*/

if (foo) {
    foo++;
}

if (foo) bar();
else {
    foo++;
}

while (true) {
    doSomething();
}

for (let i=0; i < items.length; i++) {
    doSomething();
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

Examples of correct code for the `"multi"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGlcIl0qL1xuXG5pZiAoZm9vKSBmb28rKztcblxuZWxzZSBmb28oKTtcblxud2hpbGUgKHRydWUpIHtcbiAgICBkb1NvbWV0aGluZygpO1xuICAgIGRvU29tZXRoaW5nRWxzZSgpO1xufSJ9)

```
/*eslint curly: ["error", "multi"]*/

if (foo) foo++;

else foo();

while (true) {
    doSomething();
    doSomethingElse();
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

### multi-line

Alternatively, you can relax the rule to allow brace-less single-line `if`, `else if`, `else`, `for`, `while`, or `do`, while still enforcing the use of curly braces for other instances.

Examples of incorrect code for the `"multi-line"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGktbGluZVwiXSovXG5cbmlmIChmb28pXG4gIGRvU29tZXRoaW5nKCk7XG5lbHNlXG4gIGRvU29tZXRoaW5nRWxzZSgpO1xuXG5pZiAoZm9vKSBmb28oXG4gIGJhcixcbiAgYmF6KTsifQ==)

```
/*eslint curly: ["error", "multi-line"]*/

if (foo)
  doSomething();
else
  doSomethingElse();

if (foo) foo(
  bar,
  baz);
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

Examples of correct code for the `"multi-line"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGktbGluZVwiXSovXG5cbmlmIChmb28pIGZvbysrOyBlbHNlIGRvU29tZXRoaW5nKCk7XG5cbmlmIChmb28pIGZvbysrO1xuZWxzZSBpZiAoYmFyKSBiYXooKVxuZWxzZSBkb1NvbWV0aGluZygpO1xuXG5kbyBzb21ldGhpbmcoKTtcbndoaWxlIChmb28pO1xuXG53aGlsZSAoZm9vXG4gICYmIGJhcikgYmF6KCk7XG5cbmlmIChmb28pIHtcbiAgICBmb28rKztcbn1cblxuaWYgKGZvbykgeyBmb28rKzsgfVxuXG53aGlsZSAodHJ1ZSkge1xuICAgIGRvU29tZXRoaW5nKCk7XG4gICAgZG9Tb21ldGhpbmdFbHNlKCk7XG59In0=)

```
/*eslint curly: ["error", "multi-line"]*/

if (foo) foo++; else doSomething();

if (foo) foo++;
else if (bar) baz()
else doSomething();

do something();
while (foo);

while (foo
  && bar) baz();

if (foo) {
    foo++;
}

if (foo) { foo++; }

while (true) {
    doSomething();
    doSomethingElse();
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
```

### multi-or-nest

You can use another configuration that forces brace-less `if`, `else if`, `else`, `for`, `while`, or `do` if their body contains only one single-line statement. And forces braces in all other cases.

Examples of incorrect code for the `"multi-or-nest"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGktb3ItbmVzdFwiXSovXG5cbmlmICghZm9vKVxuICAgIGZvbyA9IHtcbiAgICAgICAgYmFyOiBiYXosXG4gICAgICAgIHF1eDogZm9vXG4gICAgfTtcblxud2hpbGUgKHRydWUpXG4gIGlmKGZvbylcbiAgICAgIGRvU29tZXRoaW5nKCk7XG4gIGVsc2VcbiAgICAgIGRvU29tZXRoaW5nRWxzZSgpO1xuXG5pZiAoZm9vKSB7XG4gICAgZm9vKys7XG59XG5cbndoaWxlICh0cnVlKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn1cblxuZm9yIChsZXQgaSA9IDA7IGZvbzsgaSsrKSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0ifQ==)

```
/*eslint curly: ["error", "multi-or-nest"]*/

if (!foo)
    foo = {
        bar: baz,
        qux: foo
    };

while (true)
  if(foo)
      doSomething();
  else
      doSomethingElse();

if (foo) {
    foo++;
}

while (true) {
    doSomething();
}

for (let i = 0; foo; i++) {
    doSomething();
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
```

Examples of correct code for the `"multi-or-nest"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGktb3ItbmVzdFwiXSovXG5cbmlmICghZm9vKSB7XG4gICAgZm9vID0ge1xuICAgICAgICBiYXI6IGJheixcbiAgICAgICAgcXV4OiBmb29cbiAgICB9O1xufVxuXG53aGlsZSAodHJ1ZSkge1xuICBpZihmb28pXG4gICAgICBkb1NvbWV0aGluZygpO1xuICBlbHNlXG4gICAgICBkb1NvbWV0aGluZ0Vsc2UoKTtcbn1cblxuaWYgKGZvbylcbiAgICBmb28rKztcblxud2hpbGUgKHRydWUpXG4gICAgZG9Tb21ldGhpbmcoKTtcblxuZm9yIChsZXQgaSA9IDA7IGZvbzsgaSsrKVxuICAgIGRvU29tZXRoaW5nKCk7In0=)

```
/*eslint curly: ["error", "multi-or-nest"]*/

if (!foo) {
    foo = {
        bar: baz,
        qux: foo
    };
}

while (true) {
  if(foo)
      doSomething();
  else
      doSomethingElse();
}

if (foo)
    foo++;

while (true)
    doSomething();

for (let i = 0; foo; i++)
    doSomething();
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
```

For single-line statements preceded by a comment, braces are allowed but not required.

Examples of additional correct code for the `"multi-or-nest"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGktb3ItbmVzdFwiXSovXG5cbmlmIChmb28pXG4gICAgLy8gc29tZSBjb21tZW50XG4gICAgYmFyKCk7XG5cbmlmIChmb28pIHtcbiAgICAvLyBzb21lIGNvbW1lbnRcbiAgICBiYXIoKTtcbn0ifQ==)

```
/*eslint curly: ["error", "multi-or-nest"]*/

if (foo)
    // some comment
    bar();

if (foo) {
    // some comment
    bar();
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

### consistent

When using any of the `multi*` options, you can add an option to enforce all bodies of a `if`, `else if` and `else` chain to be with or without braces.

Examples of incorrect code for the `"multi", "consistent"` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGlcIiwgXCJjb25zaXN0ZW50XCJdKi9cblxuaWYgKGZvbykge1xuICAgIGJhcigpO1xuICAgIGJheigpO1xufSBlbHNlXG4gICAgYnV6KCk7XG5cbmlmIChmb28pXG4gICAgYmFyKCk7XG5lbHNlIGlmIChmYWEpXG4gICAgYm9yKCk7XG5lbHNlIHtcbiAgICBvdGhlcigpO1xuICAgIHRoaW5ncygpO1xufVxuXG5pZiAodHJ1ZSlcbiAgICBmb28oKTtcbmVsc2Uge1xuICAgIGJheigpO1xufVxuXG5pZiAoZm9vKSB7XG4gICAgZm9vKys7XG59In0=)

```
/*eslint curly: ["error", "multi", "consistent"]*/

if (foo) {
    bar();
    baz();
} else
    buz();

if (foo)
    bar();
else if (faa)
    bor();
else {
    other();
    things();
}

if (true)
    foo();
else {
    baz();
}

if (foo) {
    foo++;
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

Examples of correct code for the `"multi", "consistent"` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgY3VybHk6IFtcImVycm9yXCIsIFwibXVsdGlcIiwgXCJjb25zaXN0ZW50XCJdKi9cblxuaWYgKGZvbykge1xuICAgIGJhcigpO1xuICAgIGJheigpO1xufSBlbHNlIHtcbiAgICBidXooKTtcbn1cblxuaWYgKGZvbykge1xuICAgIGJhcigpO1xufSBlbHNlIGlmIChmYWEpIHtcbiAgICBib3IoKTtcbn0gZWxzZSB7XG4gICAgb3RoZXIoKTtcbiAgICB0aGluZ3MoKTtcbn1cblxuaWYgKHRydWUpXG4gICAgZm9vKCk7XG5lbHNlXG4gICAgYmF6KCk7XG5cbmlmIChmb28pXG4gICAgZm9vKys7XG4ifQ==)

```
/*eslint curly: ["error", "multi", "consistent"]*/

if (foo) {
    bar();
    baz();
} else {
    buz();
}

if (foo) {
    bar();
} else if (faa) {
    bor();
} else {
    other();
    things();
}

if (true)
    foo();
else
    baz();

if (foo)
    foo++;

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

## When Not To Use It

If you have no strict conventions about when to use block statements and when not to, you can safely disable this rule.

## Version

This rule was introduced in ESLint v0.0.2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/curly.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/curly.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/curly.md
                    
                
                )
