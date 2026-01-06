Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_is_empty](/tools/linter-rules/prefer_is_empty)

# prefer_is_empty

Learn about the prefer_is_empty linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_is_empty)

verified_userStablecirclesCorebuildFix available

Use `isEmpty` for `Iterable`s and `Map`s.

## Details

[#](#details)

DON'T use `length` to see if a collection is empty.

 The `Iterable` contract does not require that a collection know its length or be able to provide it in constant time. Calling `length` just to see if the collection contains anything can be painfully slow. 

 Instead, there are faster and more readable getters: `isEmpty` and `isNotEmpty`. Use the one that doesn't require you to negate the result. 

BAD:

dart

```
if (lunchBox.length == 0) return 'so hungry...';
if (words.length != 0) return words.join(' ');
```

content_copy

GOOD:

dart

```
if (lunchBox.isEmpty) return 'so hungry...';
if (words.isNotEmpty) return words.join(' ');
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_is_empty` rule, add `prefer_is_empty` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_is_empty
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_is_empty: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_is_empty: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_is_empty).
