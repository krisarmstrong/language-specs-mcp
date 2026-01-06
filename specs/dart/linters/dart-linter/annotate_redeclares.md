Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [annotate_redeclares](/tools/linter-rules/annotate_redeclares)

# annotate_redeclares

Learn about the annotate_redeclares linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/annotate_redeclares)

scienceExperimentalbuildFix available

Annotate redeclared members.

## Details

[#](#details)

DO annotate redeclared members.

 This practice improves code readability and helps protect against unintentionally redeclaring members or being surprised when a member ceases to redeclare (due for example to a rename refactoring). 

BAD:

dart

```
class C {
  void f() { }
}
​
extension type E(C c) implements C {
  void f() {
    ...
  }
}
```

content_copy

GOOD:

dart

```
import 'package:meta/meta.dart';
​
class C {
  void f() { }
}
​
extension type E(C c) implements C {
  @redeclare
  void f() {
    ...
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `annotate_redeclares` rule, add `annotate_redeclares` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - annotate_redeclares
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `annotate_redeclares: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    annotate_redeclares: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/annotate_redeclares).
