Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [annotate_overrides](/tools/linter-rules/annotate_overrides)

# annotate_overrides

Learn about the annotate_overrides linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/annotate_overrides)

verified_userStablethumb_upRecommendedbuildFix available

Annotate overridden members.

## Details

[#](#details)

DO annotate overridden methods and fields.

 This practice improves code readability and helps protect against unintentionally overriding superclass members. 

BAD:

dart

```
class Cat {
  int get lives => 9;
}
​
class Lucky extends Cat {
  final int lives = 14;
}
```

content_copy

GOOD:

dart

```
abstract class Dog {
  String get breed;
  void bark() {}
}
​
class Husky extends Dog {
  @override
  final String breed = 'Husky';
  @override
  void bark() {}
}
```

content_copy

## Enable

[#](#enable)

 To enable the `annotate_overrides` rule, add `annotate_overrides` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - annotate_overrides
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `annotate_overrides: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    annotate_overrides: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/annotate_overrides).
