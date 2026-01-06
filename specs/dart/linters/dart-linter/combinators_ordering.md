Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [combinators_ordering](/tools/linter-rules/combinators_ordering)

# combinators_ordering

Learn about the combinators_ordering linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/combinators_ordering)

verified_userStablebuildFix available

Sort combinator names alphabetically.

## Details

[#](#details)

DO sort combinator names alphabetically.

BAD:

dart

```
import 'a.dart' show B, A hide D, C;
export 'a.dart' show B, A hide D, C;
```

content_copy

GOOD:

dart

```
import 'a.dart' show A, B hide C, D;
export 'a.dart' show A, B hide C, D;
```

content_copy

## Enable

[#](#enable)

 To enable the `combinators_ordering` rule, add `combinators_ordering` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - combinators_ordering
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `combinators_ordering: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    combinators_ordering: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/combinators_ordering).
