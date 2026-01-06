Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_underscores](/tools/linter-rules/unnecessary_underscores)

# unnecessary_underscores

Learn about the unnecessary_underscores linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_underscores)

verified_userStablethumb_upRecommendedbuildFix available

Unnecessary underscores can be removed.

## Details

[#](#details)

AVOID using multiple underscores when a single wildcard will do.

BAD:

dart

```
void function(int __) { }
```

content_copy

GOOD:

dart

```
void function(int _) { }
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_underscores` rule, add `unnecessary_underscores` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_underscores
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_underscores: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_underscores: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_underscores).
