Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_single_quotes](/tools/linter-rules/prefer_single_quotes)

# prefer_single_quotes

Learn about the prefer_single_quotes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_single_quotes)

verified_userStablebuildFix available

Only use double quotes for strings containing single quotes.

## Details

[#](#details)

DO use single quotes where they wouldn't require additional escapes.

 That means strings with an apostrophe may use double quotes so that the apostrophe isn't escaped (note: we don't lint the other way around, ie, a single quoted string with an escaped apostrophe is not flagged). 

 It's also rare, but possible, to have strings within string interpolations. In this case, it's much more readable to use a double quote somewhere. So double quotes are allowed either within, or containing, an interpolated string literal. Arguably strings within string interpolations should be its own type of lint. 

BAD:

dart

```
useStrings(
    "should be single quote",
    r"should be single quote",
    r"""should be single quotes""")
```

content_copy

GOOD:

dart

```
useStrings(
    'should be single quote',
    r'should be single quote',
    r\'''should be single quotes\''',
    "here's ok",
    "nested \${a ? 'strings' : 'can'} be wrapped by a double quote",
    'and nested \${a ? "strings" : "can be double quoted themselves"}');
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `prefer_single_quotes` lint is incompatible with the following rules:

- [prefer_double_quotes](/tools/linter-rules/prefer_double_quotes)

## Enable

[#](#enable)

 To enable the `prefer_single_quotes` rule, add `prefer_single_quotes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_single_quotes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_single_quotes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_single_quotes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_single_quotes).
