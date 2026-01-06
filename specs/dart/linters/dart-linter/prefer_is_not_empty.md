Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_is_not_empty](/tools/linter-rules/prefer_is_not_empty)

# prefer_is_not_empty

Learn about the prefer_is_not_empty linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_is_not_empty)

verified_userStablecirclesCorebuildFix available

Use `isNotEmpty` for `Iterable`s and `Map`s.

## Details

[#](#details)

PREFER`x.isNotEmpty` to `!x.isEmpty` for `Iterable` and `Map` instances. 

 When testing whether an iterable or map is empty, prefer `isNotEmpty` over `!isEmpty` to improve code readability. 

BAD:

dart

```
if (!sources.isEmpty) {
  process(sources);
}
```

content_copy

GOOD:

dart

```
if (todo.isNotEmpty) {
  sendResults(request, todo.isEmpty);
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_is_not_empty` rule, add `prefer_is_not_empty` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_is_not_empty
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_is_not_empty: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_is_not_empty: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_is_not_empty).
