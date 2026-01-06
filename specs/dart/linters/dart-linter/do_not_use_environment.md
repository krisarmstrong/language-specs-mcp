Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [do_not_use_environment](/tools/linter-rules/do_not_use_environment)

# do_not_use_environment

Learn about the do_not_use_environment linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/do_not_use_environment)

verified_userStable

Do not use environment declared variables.

## Details

[#](#details)

 Using values derived from the environment at compile-time, creates hidden global state and makes applications hard to understand and maintain. 

DON'T use `fromEnvironment` or `hasEnvironment` factory constructors. 

BAD:

dart

```
const loggingLevel =
  bool.hasEnvironment('logging') ? String.fromEnvironment('logging') : null;
```

content_copy

## Enable

[#](#enable)

 To enable the `do_not_use_environment` rule, add `do_not_use_environment` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - do_not_use_environment
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `do_not_use_environment: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    do_not_use_environment: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/do_not_use_environment).
