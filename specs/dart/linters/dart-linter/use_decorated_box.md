Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_decorated_box](/tools/linter-rules/use_decorated_box)

# use_decorated_box

Learn about the use_decorated_box linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_decorated_box)

verified_userStablebuildFix available

Use `DecoratedBox`.

## Details

[#](#details)

DO use `DecoratedBox` when `Container` has only a `Decoration`. 

 A `Container` is a heavier Widget than a `DecoratedBox`, and as bonus, `DecoratedBox` has a `const` constructor. 

BAD:

dart

```
Widget buildArea() {
  return Container(
    decoration: const BoxDecoration(
      color: Colors.blue,
      borderRadius: BorderRadius.all(
        Radius.circular(5),
      ),
    ),
    child: const Text('...'),
  );
}
```

content_copy

GOOD:

dart

```
Widget buildArea() {
  return const DecoratedBox(
    decoration: BoxDecoration(
      color: Colors.blue,
      borderRadius: BorderRadius.all(
        Radius.circular(5),
      ),
    ),
    child: Text('...'),
  );
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_decorated_box` rule, add `use_decorated_box` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_decorated_box
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_decorated_box: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_decorated_box: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_decorated_box).
