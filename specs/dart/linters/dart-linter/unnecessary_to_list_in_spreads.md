Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_to_list_in_spreads](/tools/linter-rules/unnecessary_to_list_in_spreads)

# unnecessary_to_list_in_spreads

Learn about the unnecessary_to_list_in_spreads linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_to_list_in_spreads)

verified_userStablethumb_upRecommendedbuildFix available

Unnecessary `toList()` in spreads.

## Details

[#](#details)

Unnecessary `toList()` in spreads.

BAD:

dart

```
children: <Widget>[
  ...['foo', 'bar', 'baz'].map((String s) => Text(s)).toList(),
]
```

content_copy

GOOD:

dart

```
children: <Widget>[
  ...['foo', 'bar', 'baz'].map((String s) => Text(s)),
]
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_to_list_in_spreads` rule, add `unnecessary_to_list_in_spreads` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_to_list_in_spreads
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_to_list_in_spreads: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_to_list_in_spreads: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_to_list_in_spreads).
