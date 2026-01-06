Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [library_prefixes](/tools/linter-rules/library_prefixes)

# library_prefixes

Learn about the library_prefixes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/library_prefixes)

verified_userStablethumb_upRecommended

Use `lowercase_with_underscores` when specifying a library prefix.

## Details

[#](#details)

DO use `lowercase_with_underscores` when specifying a library prefix.

BAD:

dart

```
import 'dart:math' as Math;
import 'dart:json' as JSON;
import 'package:js/js.dart' as JS;
import 'package:javascript_utils/javascript_utils.dart' as jsUtils;
```

content_copy

GOOD:

dart

```
import 'dart:math' as math;
import 'dart:json' as json;
import 'package:js/js.dart' as js;
import 'package:javascript_utils/javascript_utils.dart' as js_utils;
```

content_copy

## Enable

[#](#enable)

 To enable the `library_prefixes` rule, add `library_prefixes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - library_prefixes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `library_prefixes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    library_prefixes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/library_prefixes).
