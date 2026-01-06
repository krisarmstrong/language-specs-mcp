Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_js_rounded_ints](/tools/linter-rules/avoid_js_rounded_ints)

# avoid_js_rounded_ints

Learn about the avoid_js_rounded_ints linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_js_rounded_ints)

verified_userStable

Avoid JavaScript rounded ints.

## Details

[#](#details)

AVOID integer literals that cannot be represented exactly when compiled to JavaScript. 

 When a program is compiled to JavaScript `int` and `double` become JavaScript Numbers. Too large integers (`value < Number.MIN_SAFE_INTEGER` or `value > Number.MAX_SAFE_INTEGER`) may be rounded to the closest Number value. 

 For instance `1000000000000000001` cannot be represented exactly as a JavaScript Number, so `1000000000000000000` will be used instead. 

BAD:

dart

```
int value = 9007199254740995;
```

content_copy

GOOD:

dart

```
BigInt value = BigInt.parse('9007199254740995');
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_js_rounded_ints` rule, add `avoid_js_rounded_ints` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_js_rounded_ints
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_js_rounded_ints: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_js_rounded_ints: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_js_rounded_ints).
