Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [flutter_style_todos](/tools/linter-rules/flutter_style_todos)

# flutter_style_todos

Learn about the flutter_style_todos linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/flutter_style_todos)

verified_userStablebuildFix available

Use Flutter TODO format: // TODO(username): message, https://URL-to-issue.

## Details

[#](#details)

DO use Flutter TODO format.

 From the [Flutter
                    docs](https://github.com/flutter/flutter/blob/main/docs/contributing/Style-guide-for-Flutter-repo.md#comments): 

 TODOs should include the string TODO in all caps, followed by the GitHub username of the person with the best context about the problem referenced by the TODO in parenthesis. A TODO is not a commitment that the person referenced will fix the problem, it is intended to be the person with enough context to explain the problem. Thus, when you create a TODO, it is almost always your username that is given. 

GOOD:

dart

```
// TODO(username): message.
// TODO(username): message, https://URL-to-issue.
```

content_copy

## Enable

[#](#enable)

 To enable the `flutter_style_todos` rule, add `flutter_style_todos` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - flutter_style_todos
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `flutter_style_todos: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    flutter_style_todos: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/flutter_style_todos).
