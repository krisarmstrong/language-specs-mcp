Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_for_elements_to_map_fromIterable](/tools/linter-rules/prefer_for_elements_to_map_fromIterable)

# prefer_for_elements_to_map_fromIterable

Learn about the prefer_for_elements_to_map_fromIterable linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_for_elements_to_map_fromIterable)

verified_userStablethumb_upRecommendedbuildFix available

Prefer `for` elements when building maps from iterables.

## Details

[#](#details)

When building maps from iterables, it is preferable to use `for` elements.

Using 'for' elements brings several benefits including:

- Performance
- Flexibility
- Readability
- Improved type inference
- Improved interaction with null safety

BAD:

dart

```
Map<String, WidgetBuilder>.fromIterable(
  kAllGalleryDemos,
  key: (demo) => '${demo.routeName}',
  value: (demo) => demo.buildRoute,
);
```

content_copy

GOOD:

dart

```
return {
  for (var demo in kAllGalleryDemos)
    '${demo.routeName}': demo.buildRoute,
};
```

content_copy

GOOD:

dart

```
// Map<int, Student> is not required, type is inferred automatically.
final pizzaRecipients = {
  ...studentLeaders,
  for (var student in classG)
    if (student.isPassing) student.id: student,
};
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_for_elements_to_map_fromIterable` rule, add `prefer_for_elements_to_map_fromIterable` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_for_elements_to_map_fromIterable
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_for_elements_to_map_fromIterable: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_for_elements_to_map_fromIterable: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_for_elements_to_map_fromIterable).
