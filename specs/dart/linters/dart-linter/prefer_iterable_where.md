Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_iterable_whereType](/tools/linter-rules/prefer_iterable_whereType)

# prefer_iterable_whereType

Learn about the prefer_iterable_whereType linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_iterable_whereType)

verified_userStablecirclesCorebuildFix available

Prefer to use `whereType` on iterable.

## Details

[#](#details)

PREFER`iterable.whereType<T>()` over `iterable.where((e) => e is T)`. 

BAD:

dart

```
iterable.where((e) => e is MyClass);
```

content_copy

GOOD:

dart

```
iterable.whereType<MyClass>();
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_iterable_whereType` rule, add `prefer_iterable_whereType` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_iterable_whereType
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_iterable_whereType: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_iterable_whereType: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_iterable_whereType).
