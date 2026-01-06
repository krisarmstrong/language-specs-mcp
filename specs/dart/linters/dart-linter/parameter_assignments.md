Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [parameter_assignments](/tools/linter-rules/parameter_assignments)

# parameter_assignments

Learn about the parameter_assignments linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/parameter_assignments)

verified_userStable

Don't reassign references to parameters of functions or methods.

## Details

[#](#details)

DON'T assign new values to parameters of methods or functions.

 Assigning new values to parameters is generally a bad practice unless an operator such as `??=` is used. Otherwise, arbitrarily reassigning parameters is usually a mistake. 

BAD:

dart

```
void badFunction(int parameter) { // LINT
  parameter = 4;
}
```

content_copy

BAD:

dart

```
void badFunction(int required, {int optional: 42}) { // LINT
  optional ??= 8;
}
```

content_copy

BAD:

dart

```
void badFunctionPositional(int required, [int optional = 42]) { // LINT
  optional ??= 8;
}
```

content_copy

BAD:

dart

```
class A {
  void badMethod(int parameter) { // LINT
    parameter = 4;
  }
}
```

content_copy

GOOD:

dart

```
void ok(String parameter) {
  print(parameter);
}
```

content_copy

GOOD:

dart

```
void actuallyGood(int required, {int optional}) { // OK
  optional ??= ...;
}
```

content_copy

GOOD:

dart

```
void actuallyGoodPositional(int required, [int optional]) { // OK
  optional ??= ...;
}
```

content_copy

GOOD:

dart

```
class A {
  void ok(String parameter) {
    print(parameter);
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `parameter_assignments` rule, add `parameter_assignments` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - parameter_assignments
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `parameter_assignments: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    parameter_assignments: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/parameter_assignments).
