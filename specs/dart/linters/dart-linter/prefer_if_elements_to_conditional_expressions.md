Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_if_elements_to_conditional_expressions](/tools/linter-rules/prefer_if_elements_to_conditional_expressions)

# prefer_if_elements_to_conditional_expressions

Learn about the prefer_if_elements_to_conditional_expressions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_if_elements_to_conditional_expressions)

verified_userStablebuildFix available

Prefer if elements to conditional expressions where possible.

## Details

[#](#details)

 When building collections, it is preferable to use `if` elements rather than conditionals. 

BAD:

dart

```
var list = ['a', 'b', condition ? 'c' : null].where((e) => e != null).toList();
```

content_copy

GOOD:

dart

```
var list = ['a', 'b', if (condition) 'c'];
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_if_elements_to_conditional_expressions` rule, add `prefer_if_elements_to_conditional_expressions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_if_elements_to_conditional_expressions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_if_elements_to_conditional_expressions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_if_elements_to_conditional_expressions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_if_elements_to_conditional_expressions).
