Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [leading_newlines_in_multiline_strings](/tools/linter-rules/leading_newlines_in_multiline_strings)

# leading_newlines_in_multiline_strings

Learn about the leading_newlines_in_multiline_strings linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/leading_newlines_in_multiline_strings)

verified_userStablebuildFix available

Start multiline strings with a newline.

## Details

[#](#details)

 Multiline strings are easier to read when they start with a newline (a newline starting a multiline string is ignored). 

BAD:

dart

```
var s1 = '''{
  "a": 1,
  "b": 2
}''';
```

content_copy

GOOD:

dart

```
var s1 = '''
{
  "a": 1,
  "b": 2
}''';
​
var s2 = '''This one-liner multiline string is ok. It usually allows to escape both ' and " in the string.''';
```

content_copy

## Enable

[#](#enable)

 To enable the `leading_newlines_in_multiline_strings` rule, add `leading_newlines_in_multiline_strings` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - leading_newlines_in_multiline_strings
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `leading_newlines_in_multiline_strings: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    leading_newlines_in_multiline_strings: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/leading_newlines_in_multiline_strings).
