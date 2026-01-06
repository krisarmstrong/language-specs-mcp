Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [depend_on_referenced_packages](/tools/linter-rules/depend_on_referenced_packages)

# depend_on_referenced_packages

Learn about the depend_on_referenced_packages linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/depend_on_referenced_packages)

verified_userStablecirclesCore

Depend on referenced packages.

## Details

[#](#details)

DO depend on referenced packages.

When importing a package, add a dependency on it to your pubspec.

 Depending explicitly on packages that you reference ensures they will always exist and allows you to put a dependency constraint on them to guard you against breaking changes. 

 Whether this should be a regular dependency or dev_dependency depends on if it is referenced from a public file (one under either `lib` or `bin`), or some other private file. 

BAD:

dart

```
import 'package:a/a.dart';
```

content_copyyaml

```
dependencies:
```

content_copy

GOOD:

dart

```
import 'package:a/a.dart';
```

content_copyyaml

```
dependencies:
  a: ^1.0.0
```

content_copy

## Enable

[#](#enable)

 To enable the `depend_on_referenced_packages` rule, add `depend_on_referenced_packages` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - depend_on_referenced_packages
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `depend_on_referenced_packages: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    depend_on_referenced_packages: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/depend_on_referenced_packages).
