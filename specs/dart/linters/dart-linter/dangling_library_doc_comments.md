Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [dangling_library_doc_comments](/tools/linter-rules/dangling_library_doc_comments)

# dangling_library_doc_comments

Learn about the dangling_library_doc_comments linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/dangling_library_doc_comments)

verified_userStablecirclesCorebuildFix available

Attach library doc comments to library directives.

## Details

[#](#details)

 Attach library doc comments (with `///`) to library directives, rather than leaving them dangling near the top of a library. 

BAD:

dart

```
/// This is a great library.
import 'package:math';
```

content_copydart

```
/// This is a great library.
​
class C {}
```

content_copy

GOOD:

dart

```
/// This is a great library.
library;
​
import 'package:math';
​
class C {}
```

content_copy

NOTE: An unnamed library, like `library;` above, is only supported in Dart 2.19 and later. Code which might run in earlier versions of Dart will need to provide a name in the `library` directive. 

## Enable

[#](#enable)

 To enable the `dangling_library_doc_comments` rule, add `dangling_library_doc_comments` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - dangling_library_doc_comments
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `dangling_library_doc_comments: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    dangling_library_doc_comments: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/dangling_library_doc_comments).
