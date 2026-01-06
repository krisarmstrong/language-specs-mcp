Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_leading_underscores_for_library_prefixes](/tools/linter-rules/no_leading_underscores_for_library_prefixes)

# no_leading_underscores_for_library_prefixes

Learn about the no_leading_underscores_for_library_prefixes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_leading_underscores_for_library_prefixes)

verified_userStablethumb_upRecommendedbuildFix available

Avoid leading underscores for library prefixes.

## Details

[#](#details)

DON'T use a leading underscore for library prefixes. There is no concept of "private" for library prefixes. When one of those has a name that starts with an underscore, it sends a confusing signal to the reader. To avoid that, don't use leading underscores in those names. 

BAD:

dart

```
import 'dart:core' as _core;
```

content_copy

GOOD:

dart

```
import 'dart:core' as core;
```

content_copy

## Enable

[#](#enable)

 To enable the `no_leading_underscores_for_library_prefixes` rule, add `no_leading_underscores_for_library_prefixes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_leading_underscores_for_library_prefixes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_leading_underscores_for_library_prefixes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_leading_underscores_for_library_prefixes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_leading_underscores_for_library_prefixes).
