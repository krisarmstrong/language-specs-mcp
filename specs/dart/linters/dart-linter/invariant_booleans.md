Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [invariant_booleans](/tools/linter-rules/invariant_booleans)

# invariant_booleans

Learn about the invariant_booleans linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/invariant_booleans)

errorRemoved

Conditions should not unconditionally evaluate to `true` or to `false`.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.0.0; it is no longer functional.

DON'T test for conditions that can be inferred at compile time or test the same condition twice. 

 Conditional statements using a condition which cannot be anything but `false` have the effect of making blocks of code non-functional. If the condition cannot evaluate to anything but `true`, the conditional statement is completely redundant, and makes the code less readable. It is quite likely that the code does not match the programmer's intent. Either the condition should be removed or it should be updated so that it does not always evaluate to `true` or `false` and does not perform redundant tests. This rule will hint to the test conflicting with the linted one. 

BAD:

dart

```
// foo can't be both equal and not equal to bar in the same expression
if(foo == bar && something && foo != bar) {...}
```

content_copy

BAD:

dart

```
void compute(int foo) {
  if (foo == 4) {
    doSomething();
    // we know foo is equal to 4 at this point, so the next condition is always false
    if (foo > 4) {...}
    ...
  }
  ...
}
```

content_copy

BAD:

dart

```
void compute(bool foo) {
  if (foo) {
    return;
  }
  doSomething();
  // foo is always false here
  if (foo){...}
  ...
}
```

content_copy

GOOD:

dart

```
void nestedOK() {
  if (foo == bar) {
    foo = baz;
    if (foo != bar) {...}
  }
}
```

content_copy

GOOD:

dart

```
void nestedOk2() {
  if (foo == bar) {
    return;
  }
​
  foo = baz;
  if (foo == bar) {...} // OK
}
```

content_copy

GOOD:

dart

```
void nestedOk5() {
  if (foo != null) {
    if (bar != null) {
      return;
    }
  }
​
  if (bar != null) {...} // OK
}
```

content_copy

## Enable

[#](#enable)

 To enable the `invariant_booleans` rule, add `invariant_booleans` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - invariant_booleans
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `invariant_booleans: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    invariant_booleans: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/invariant_booleans).
