Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_inlined_adds](/tools/linter-rules/prefer_inlined_adds)

# prefer_inlined_adds

Learn about the prefer_inlined_adds linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_inlined_adds)

verified_userStablethumb_upRecommendedbuildFix available

Inline list item declarations where possible.

## Details

[#](#details)

 Declare elements in list literals inline, rather than using `add` and `addAll` methods where possible. 

BAD:

dart

```
var l = ['a']..add('b')..add('c');
var l2 = ['a']..addAll(['b', 'c']);
```

content_copy

GOOD:

dart

```
var l = ['a', 'b', 'c'];
var l2 = ['a', 'b', 'c'];
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_inlined_adds` rule, add `prefer_inlined_adds` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_inlined_adds
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_inlined_adds: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_inlined_adds: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_inlined_adds).
