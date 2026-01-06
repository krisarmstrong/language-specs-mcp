Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_null_aware_assignments](/tools/linter-rules/unnecessary_null_aware_assignments)

# unnecessary_null_aware_assignments

Learn about the unnecessary_null_aware_assignments linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_null_aware_assignments)

verified_userStablethumb_upRecommendedbuildFix available

Avoid `null` in `null`-aware assignment.

## Details

[#](#details)

AVOID`null` in `null`-aware assignment.

 Using `null` on the right-hand side of a `null`-aware assignment effectively makes the assignment redundant. 

BAD:

dart

```
var x;
x ??= null;
```

content_copy

GOOD:

dart

```
var x;
x ??= 1;
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_null_aware_assignments` rule, add `unnecessary_null_aware_assignments` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_null_aware_assignments
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_null_aware_assignments: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_null_aware_assignments: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_null_aware_assignments).
