Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [slash_for_doc_comments](/tools/linter-rules/slash_for_doc_comments)

# slash_for_doc_comments

Learn about the slash_for_doc_comments linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/slash_for_doc_comments)

verified_userStablethumb_upRecommendedbuildFix available

Prefer using `///` for doc comments.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/documentation#do-use--doc-comments-to-document-members-and-types): 

DO use `///` for documentation comments.

 Although Dart supports two syntaxes of doc comments (`///` and `/**`), we prefer using `///` for doc comments. 

GOOD:

dart

```
/// Parses a set of option strings. For each option:
///
/// * If it is `null`, then it is ignored.
/// * If it is a string, then [validate] is called on it.
/// * If it is any other type, it is *not* validated.
void parse(List options) {
  // ...
}
```

content_copy

Within a doc comment, you can use markdown for formatting.

## Enable

[#](#enable)

 To enable the `slash_for_doc_comments` rule, add `slash_for_doc_comments` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - slash_for_doc_comments
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `slash_for_doc_comments: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    slash_for_doc_comments: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/slash_for_doc_comments).
