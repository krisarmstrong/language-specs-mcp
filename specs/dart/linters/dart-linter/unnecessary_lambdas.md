Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_lambdas](/tools/linter-rules/unnecessary_lambdas)

# unnecessary_lambdas

Learn about the unnecessary_lambdas linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_lambdas)

verified_userStablebuildFix available

Don't create a lambda when a tear-off will do.

## Details

[#](#details)

DON'T create a lambda when a tear-off will do.

BAD:

dart

```
names.forEach((name) {
  print(name);
});
```

content_copy

GOOD:

dart

```
names.forEach(print);
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_lambdas` rule, add `unnecessary_lambdas` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_lambdas
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_lambdas: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_lambdas: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_lambdas).
