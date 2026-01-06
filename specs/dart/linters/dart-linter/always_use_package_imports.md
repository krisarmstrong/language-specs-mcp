Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [always_use_package_imports](/tools/linter-rules/always_use_package_imports)

# always_use_package_imports

Learn about the always_use_package_imports linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_use_package_imports)

verified_userStablebuildFix available

Avoid relative imports for files in `lib/`.

## Details

[#](#details)

DO avoid relative imports for files in `lib/`.

 When mixing relative and absolute imports it's possible to create confusion where the same member gets imported in two different ways. One way to avoid that is to ensure you consistently use absolute imports for files within the `lib/` directory. 

This is the opposite of 'prefer_relative_imports'.

 You can also use 'avoid_relative_lib_imports' to disallow relative imports of files within `lib/` directory outside of it (for example `test/`). 

BAD:

dart

```
import 'baz.dart';
​
import 'src/bag.dart'
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
import 'package:foo/baz.dart';
​
import 'package:foo/src/baz.dart';
...
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `always_use_package_imports` lint is incompatible with the following rules:

- [prefer_relative_imports](/tools/linter-rules/prefer_relative_imports)

## Enable

[#](#enable)

 To enable the `always_use_package_imports` rule, add `always_use_package_imports` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - always_use_package_imports
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `always_use_package_imports: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    always_use_package_imports: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_use_package_imports).
