Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [missing_code_block_language_in_doc_comment](/tools/linter-rules/missing_code_block_language_in_doc_comment)

# missing_code_block_language_in_doc_comment

Learn about the missing_code_block_language_in_doc_comment linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/missing_code_block_language_in_doc_comment)

verified_userStable

A code block is missing a specified language.

## Details

[#](#details)

DO specify the language used in the code block of a doc comment.

 To enable proper syntax highlighting of Markdown code blocks, [dart doc](https://dart.dev/tools/dart-doc) strongly recommends code blocks to specify the language used after the initial code fence. 

 See [highlight.js](https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md) for the list of languages supported by `dart doc`. To disable syntax highlighting or if no language is suitable, you can specify `none` as the language. 

BAD:

dart

```
/// ```
/// void main() {}
/// ```
class A {}
```

content_copy

GOOD:

dart

```
/// ```dart
/// void main() {}
/// ```
class A {}
```

content_copy

## Enable

[#](#enable)

 To enable the `missing_code_block_language_in_doc_comment` rule, add `missing_code_block_language_in_doc_comment` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - missing_code_block_language_in_doc_comment
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `missing_code_block_language_in_doc_comment: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    missing_code_block_language_in_doc_comment: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/missing_code_block_language_in_doc_comment).
