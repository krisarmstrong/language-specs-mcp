Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_runtimeType_toString](/tools/linter-rules/no_runtimeType_toString)

# no_runtimeType_toString

Learn about the no_runtimeType_toString linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_runtimeType_toString)

verified_userStable

Avoid calling `toString()` on `runtimeType`.

## Details

[#](#details)

 Calling `toString` on a runtime type is a non-trivial operation that can negatively impact performance. It's better to avoid it. 

BAD:

dart

```
class A {
  String toString() => '$runtimeType()';
}
```

content_copy

GOOD:

dart

```
class A {
  String toString() => 'A()';
}
```

content_copy

 This lint has some exceptions where performance is not a problem or where real type information is more important than performance: 

- in an assertion
- in a throw expression
- in a catch clause
- in a mixin declaration
- in an abstract class declaration

## Enable

[#](#enable)

 To enable the `no_runtimeType_toString` rule, add `no_runtimeType_toString` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_runtimeType_toString
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_runtimeType_toString: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_runtimeType_toString: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_runtimeType_toString).
