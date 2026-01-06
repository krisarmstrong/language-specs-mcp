Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_field_initializers_in_const_classes](/tools/linter-rules/avoid_field_initializers_in_const_classes)

# avoid_field_initializers_in_const_classes

Learn about the avoid_field_initializers_in_const_classes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_field_initializers_in_const_classes)

verified_userStable

Avoid field initializers in const classes.

## Details

[#](#details)

AVOID field initializers in const classes.

 Instead of `final x = const expr;`, you should write `get x => const expr;` and not allocate a useless field. As of April 2018 this is true for the VM, but not for code that will be compiled to JS. 

BAD:

dart

```
class A {
  final a = const [];
  const A();
}
```

content_copy

GOOD:

dart

```
class A {
  get a => const [];
  const A();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_field_initializers_in_const_classes` rule, add `avoid_field_initializers_in_const_classes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_field_initializers_in_const_classes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_field_initializers_in_const_classes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_field_initializers_in_const_classes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_field_initializers_in_const_classes).
