Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_relative_lib_imports](/tools/linter-rules/avoid_relative_lib_imports)

# avoid_relative_lib_imports

Learn about the avoid_relative_lib_imports linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_relative_lib_imports)

verified_userStablecirclesCorebuildFix available

Avoid relative imports for files in `lib/`.

## Details

[#](#details)

DO avoid relative imports for files in `lib/`.

 When mixing relative and absolute imports it's possible to create confusion where the same member gets imported in two different ways. An easy way to avoid that is to ensure you have no relative imports that include `lib/` in their paths. 

 You can also use 'always_use_package_imports' to disallow relative imports between files within `lib/`. 

BAD:

dart

```
import 'package:foo/bar.dart';
​
import '../lib/baz.dart';
​
...
```

content_copy

GOOD:

dart

```
import 'package:foo/bar.dart';
​
import 'baz.dart';
​
...
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_relative_lib_imports` rule, add `avoid_relative_lib_imports` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_relative_lib_imports
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_relative_lib_imports: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_relative_lib_imports: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_relative_lib_imports).
