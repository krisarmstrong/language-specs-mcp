Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_late](/tools/linter-rules/unnecessary_late)

# unnecessary_late

Learn about the unnecessary_late linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_late)

verified_userStablethumb_upRecommendedbuildFix available

Don't specify the `late` modifier when it is not needed.

## Details

[#](#details)

DO not specify the `late` modifier for top-level and static variables when the declaration contains an initializer. 

 Top-level and static variables with initializers are already evaluated lazily as if they are marked `late`. 

BAD:

dart

```
late String badTopLevel = '';
```

content_copy

GOOD:

dart

```
String goodTopLevel = '';
```

content_copy

BAD:

dart

```
class BadExample {
  static late String badStatic = '';
}
```

content_copy

GOOD:

dart

```
class GoodExample {
  late String goodStatic;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_late` rule, add `unnecessary_late` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_late
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_late: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_late: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_late).
