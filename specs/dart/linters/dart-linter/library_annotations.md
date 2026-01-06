Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [library_annotations](/tools/linter-rules/library_annotations)

# library_annotations

Learn about the library_annotations linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/library_annotations)

verified_userStablecirclesCorebuildFix available

Attach library annotations to library directives.

## Details

[#](#details)

 Attach library annotations to library directives, rather than some other library-level element. 

BAD:

dart

```
@TestOn('browser')
​
import 'package:test/test.dart';
​
void main() {}
```

content_copy

GOOD:

dart

```
@TestOn('browser')
library;
​
import 'package:test/test.dart';
​
void main() {}
```

content_copy

NOTE: An unnamed library, like `library;` above, is only supported in Dart 2.19 and later. Code which might run in earlier versions of Dart will need to provide a name in the `library` directive. 

## Enable

[#](#enable)

 To enable the `library_annotations` rule, add `library_annotations` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - library_annotations
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `library_annotations: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    library_annotations: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/library_annotations).
