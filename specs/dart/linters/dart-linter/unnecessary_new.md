Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_new](/tools/linter-rules/unnecessary_new)

# unnecessary_new

Learn about the unnecessary_new linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_new)

verified_userStablethumb_upRecommendedbuildFix available

Unnecessary new keyword.

## Details

[#](#details)

AVOID new keyword to create instances.

BAD:

dart

```
class A { A(); }
m(){
  final a = new A();
}
```

content_copy

GOOD:

dart

```
class A { A(); }
m(){
  final a = A();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_new` rule, add `unnecessary_new` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_new
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_new: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_new: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_new).
