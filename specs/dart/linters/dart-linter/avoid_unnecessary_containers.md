Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_unnecessary_containers](/tools/linter-rules/avoid_unnecessary_containers)

# avoid_unnecessary_containers

Learn about the avoid_unnecessary_containers linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_unnecessary_containers)

verified_userStableflutterFlutterbuildFix available

Avoid unnecessary containers.

## Details

[#](#details)

AVOID wrapping widgets in unnecessary containers.

 Wrapping a widget in `Container` with no other parameters set has no effect and makes code needlessly more complex. 

BAD:

dart

```
Widget buildRow() {
  return Container(
      child: Row(
        children: <Widget>[
          const MyLogo(),
          const Expanded(
            child: Text('...'),
          ),
        ],
      )
  );
}
```

content_copy

GOOD:

dart

```
Widget buildRow() {
  return Row(
    children: <Widget>[
      const MyLogo(),
      const Expanded(
        child: Text('...'),
      ),
    ],
  );
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_unnecessary_containers` rule, add `avoid_unnecessary_containers` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_unnecessary_containers
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_unnecessary_containers: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_unnecessary_containers: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_unnecessary_containers).
