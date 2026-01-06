Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [sized_box_for_whitespace](/tools/linter-rules/sized_box_for_whitespace)

# sized_box_for_whitespace

Learn about the sized_box_for_whitespace linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sized_box_for_whitespace)

verified_userStableflutterFlutterbuildFix available

`SizedBox` for whitespace.

## Details

[#](#details)

Use `SizedBox` to add whitespace to a layout.

 A `Container` is a heavier Widget than a `SizedBox`, and as bonus, `SizedBox` has a `const` constructor. 

BAD:

dart

```
Widget buildRow() {
  return Row(
    children: <Widget>[
      const MyLogo(),
      Container(width: 4),
      const Expanded(
        child: Text('...'),
      ),
    ],
  );
}
```

content_copy

GOOD:

dart

```
Widget buildRow() {
  return Row(
    children: const <Widget>[
      MyLogo(),
      SizedBox(width: 4),
      Expanded(
        child: Text('...'),
      ),
    ],
  );
}
```

content_copy

## Enable

[#](#enable)

 To enable the `sized_box_for_whitespace` rule, add `sized_box_for_whitespace` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - sized_box_for_whitespace
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `sized_box_for_whitespace: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    sized_box_for_whitespace: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sized_box_for_whitespace).
