Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_catches_without_on_clauses](/tools/linter-rules/avoid_catches_without_on_clauses)

# avoid_catches_without_on_clauses

Learn about the avoid_catches_without_on_clauses linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_catches_without_on_clauses)

verified_userStable

Avoid catches without on clauses.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#avoid-catches-without-on-clauses): 

AVOID catches without on clauses.

 Using catch clauses without on clauses make your code prone to encountering unexpected errors that won't be thrown (and thus will go unnoticed). 

BAD:

dart

```
try {
 somethingRisky()
} catch(e) {
  doSomething(e);
}
```

content_copy

GOOD:

dart

```
try {
 somethingRisky()
} on Exception catch(e) {
  doSomething(e);
}
```

content_copy

A few exceptional cases are allowed:

- If the body of the catch rethrows the exception.
-  If the caught exception is "directly used" in an argument to `Future.error`, `Completer.completeError`, or `FlutterError.reportError`, or any function with a return type of `Never`. 
- If the caught exception is "directly used" in a new throw-expression.

 In these cases, "directly used" means that the exception is referenced within the relevant code (like within an argument). If the exception variable is referenced before the relevant code, for example to instantiate a wrapper exception, the variable is not "directly used." 

## Enable

[#](#enable)

 To enable the `avoid_catches_without_on_clauses` rule, add `avoid_catches_without_on_clauses` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_catches_without_on_clauses
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_catches_without_on_clauses: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_catches_without_on_clauses: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_catches_without_on_clauses).
