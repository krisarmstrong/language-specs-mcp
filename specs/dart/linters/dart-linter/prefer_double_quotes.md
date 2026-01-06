Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_double_quotes](/tools/linter-rules/prefer_double_quotes)

# prefer_double_quotes

Learn about the prefer_double_quotes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_double_quotes)

verified_userStablebuildFix available

Prefer double quotes where they won't require escape sequences.

## Details

[#](#details)

DO use double quotes where they wouldn't require additional escapes.

 That means strings with a double quote may use apostrophes so that the double quote isn't escaped (note: we don't lint the other way around, ie, a double quoted string with an escaped double quote is not flagged). 

 It's also rare, but possible, to have strings within string interpolations. In this case, it's much more readable to use a single quote somewhere. So single quotes are allowed either within, or containing, an interpolated string literal. Arguably strings within string interpolations should be its own type of lint. 

BAD:

dart

```
useStrings(
    'should be double quote',
    r'should be double quote',
    r\'''should be double quotes\''')
```

content_copy

GOOD:

dart

```
useStrings(
    "should be double quote",
    r"should be double quote",
    r"""should be double quotes""",
    'ok with " inside',
    'nested \${a ? "strings" : "can"} be wrapped by a double quote',
    "and nested \${a ? 'strings' : 'can be double quoted themselves'}");
```

content_copy

## Incompatible rules

[#](#incompatible-rules)

The `prefer_double_quotes` lint is incompatible with the following rules:

- [prefer_single_quotes](/tools/linter-rules/prefer_single_quotes)

## Enable

[#](#enable)

 To enable the `prefer_double_quotes` rule, add `prefer_double_quotes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_double_quotes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_double_quotes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_double_quotes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_double_quotes).
