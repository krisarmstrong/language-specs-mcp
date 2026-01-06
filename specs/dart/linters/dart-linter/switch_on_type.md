Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [switch_on_type](/tools/linter-rules/switch_on_type)

# switch_on_type

Learn about the switch_on_type linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/switch_on_type)

verified_userStable

Avoid switch statements on a 'Type'.

## Details

[#](#details)

AVOID using switch on `Type`.

 Switching on `Type` is not type-safe and can lead to bugs if the class hierarchy changes. Prefer to use pattern matching on the variable instead. 

BAD:

dart

```
void f(Object o) {
  switch (o.runtimeType) {
    case int:
      print('int');
    case String:
      print('String');
  }
}
```

content_copy

GOOD:

dart

```
void f(Object o) {
  switch(o) {
    case int():
      print('int');
    case String _:
      print('String');
    default:
      print('other');
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `switch_on_type` rule, add `switch_on_type` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - switch_on_type
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `switch_on_type: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    switch_on_type: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/switch_on_type).
