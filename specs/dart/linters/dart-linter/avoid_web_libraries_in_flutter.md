Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_web_libraries_in_flutter](/tools/linter-rules/avoid_web_libraries_in_flutter)

# avoid_web_libraries_in_flutter

Learn about the avoid_web_libraries_in_flutter linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_web_libraries_in_flutter)

verified_userStableflutterFlutter

Avoid using web-only libraries outside Flutter web plugin packages.

## Details

[#](#details)

AVOID using web libraries, `dart:html`, `dart:js` and `dart:js_util` in Flutter packages that are not web plugins. These libraries are not supported outside of a web context; functionality that depends on them will fail at runtime in Flutter mobile, and their use is generally discouraged in Flutter web. 

Web library access is allowed in:

- plugin packages that declare `web` as a supported context

 otherwise, imports of `dart:html`, `dart:js` and `dart:js_util` are disallowed. 

## Enable

[#](#enable)

 To enable the `avoid_web_libraries_in_flutter` rule, add `avoid_web_libraries_in_flutter` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_web_libraries_in_flutter
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_web_libraries_in_flutter: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_web_libraries_in_flutter: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_web_libraries_in_flutter).
