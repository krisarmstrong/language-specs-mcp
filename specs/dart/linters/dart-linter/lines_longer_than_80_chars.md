Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [lines_longer_than_80_chars](/tools/linter-rules/lines_longer_than_80_chars)

# lines_longer_than_80_chars

Learn about the lines_longer_than_80_chars linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/lines_longer_than_80_chars)

verified_userStable

Avoid lines longer than 80 characters.

## Details

[#](#details)

AVOID lines longer than 80 characters

 Readability studies show that long lines of text are harder to read because your eye has to travel farther when moving to the beginning of the next line. This is why newspapers and magazines use multiple columns of text. 

 If you really find yourself wanting lines longer than 80 characters, our experience is that your code is likely too verbose and could be a little more compact. The main offender is usually `VeryLongCamelCaseClassNames`. Ask yourself, “Does each word in that type name tell me something critical or prevent a name collision?” If not, consider omitting it. 

 Note that `dart format` does 99% of this for you, but the last 1% is you. It does not split long string literals to fit in 80 columns, so you have to do that manually. 

 We make an exception for URIs and file paths. When those occur in comments or strings (usually in imports and exports), they may remain on a single line even if they go over the line limit. This makes it easier to search source files for a given path. 

## Enable

[#](#enable)

 To enable the `lines_longer_than_80_chars` rule, add `lines_longer_than_80_chars` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - lines_longer_than_80_chars
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `lines_longer_than_80_chars: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    lines_longer_than_80_chars: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/lines_longer_than_80_chars).
