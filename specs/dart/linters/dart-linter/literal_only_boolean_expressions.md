Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [literal_only_boolean_expressions](/tools/linter-rules/literal_only_boolean_expressions)

# literal_only_boolean_expressions

Learn about the literal_only_boolean_expressions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/literal_only_boolean_expressions)

verified_userStable

Boolean expression composed only with literals.

## Details

[#](#details)

DON'T test for conditions composed only by literals, since the value can be inferred at compile time. 

 Conditional statements using a condition which cannot be anything but FALSE have the effect of making blocks of code non-functional. If the condition cannot evaluate to anything but `true`, the conditional statement is completely redundant, and makes the code less readable. It is quite likely that the code does not match the programmer's intent. Either the condition should be removed or it should be updated so that it does not always evaluate to `true` or `false`. 

BAD:

dart

```
void bad() {
  if (true) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (true && 1 != 0) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (1 != 0 && true) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (1 < 0 && true) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (true && false) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (1 != 0) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (true && 1 != 0 || 3 < 4) {} // LINT
}
```

content_copy

BAD:

dart

```
void bad() {
  if (1 != 0 || 3 < 4 && true) {} // LINT
}
```

content_copy

NOTE: that an exception is made for the common `while (true) { }` idiom, which is often reasonably preferred to the equivalent `for (;;)`. 

GOOD:

dart

```
void good() {
  while (true) {
    // Do stuff.
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `literal_only_boolean_expressions` rule, add `literal_only_boolean_expressions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - literal_only_boolean_expressions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `literal_only_boolean_expressions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    literal_only_boolean_expressions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/literal_only_boolean_expressions).
