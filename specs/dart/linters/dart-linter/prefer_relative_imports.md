Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_relative_imports](/tools/linter-rules/prefer_relative_imports)

# prefer_relative_imports

Learn about the prefer_relative_imports linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_relative_imports)

verified_userStablebuildFix available

Prefer relative imports for files in `lib/`.

## Details

[#](#details)

PREFER relative imports for files in `lib/`.

 When mixing relative and absolute imports it's possible to create confusion where the same member gets imported in two different ways. One way to avoid that is to ensure you consistently use relative imports for files within the `lib/` directory. 

BAD:

dart

```
import 'package:my_package/bar.dart';
```

content_copy

GOOD:

dart

```
import 'bar.dart';
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `prefer_relative_imports` lint is incompatible with the following rules:

- [always_use_package_imports](/tools/linter-rules/always_use_package_imports)

## Enable

[#](#enable)

 To enable the `prefer_relative_imports` rule, add `prefer_relative_imports` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_relative_imports
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_relative_imports: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_relative_imports: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_relative_imports).
