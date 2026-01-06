Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_colored_box](/tools/linter-rules/use_colored_box)

# use_colored_box

Learn about the use_colored_box linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_colored_box)

verified_userStablebuildFix available

Use `ColoredBox`.

## Details

[#](#details)

DO use `ColoredBox` when `Container` has only a `Color`. 

 A `Container` is a heavier Widget than a `ColoredBox`, and as bonus, `ColoredBox` has a `const` constructor. 

BAD:

dart

```
Widget buildArea() {
  return Container(
    color: Colors.blue,
    child: const Text('hello'),
  );
}
```

content_copy

GOOD:

dart

```
Widget buildArea() {
  return const ColoredBox(
    color: Colors.blue,
    child: Text('hello'),
  );
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_colored_box` rule, add `use_colored_box` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_colored_box
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_colored_box: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_colored_box: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_colored_box).
