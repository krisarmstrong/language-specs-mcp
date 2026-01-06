Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [sized_box_shrink_expand](/tools/linter-rules/sized_box_shrink_expand)

# sized_box_shrink_expand

Learn about the sized_box_shrink_expand linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sized_box_shrink_expand)

verified_userStable

Use SizedBox shrink and expand named constructors.

## Details

[#](#details)

 Use `SizedBox.shrink(...)` and `SizedBox.expand(...)` constructors appropriately. 

 Either the `SizedBox.shrink(...)` or `SizedBox.expand(...)` constructor should be used instead of the more general `SizedBox(...)` constructor when one of the named constructors capture the intent of the code more succinctly. 

Examples

BAD:

dart

```
Widget buildLogo() {
  return SizedBox(
    height: 0,
    width: 0,
    child: const MyLogo(),
  );
}
```

content_copydart

```
Widget buildLogo() {
  return SizedBox(
    height: double.infinity,
    width: double.infinity,
    child: const MyLogo(),
  );
}
```

content_copy

GOOD:

dart

```
Widget buildLogo() {
  return SizedBox.shrink(
    child: const MyLogo(),
  );
}
```

content_copydart

```
Widget buildLogo() {
  return SizedBox.expand(
    child: const MyLogo(),
  );
}
```

content_copy

## Enable

[#](#enable)

 To enable the `sized_box_shrink_expand` rule, add `sized_box_shrink_expand` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - sized_box_shrink_expand
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `sized_box_shrink_expand: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    sized_box_shrink_expand: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sized_box_shrink_expand).
