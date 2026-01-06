Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_function_literals_in_foreach_calls](/tools/linter-rules/avoid_function_literals_in_foreach_calls)

# avoid_function_literals_in_foreach_calls

Learn about the avoid_function_literals_in_foreach_calls linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_function_literals_in_foreach_calls)

verified_userStablethumb_upRecommendedbuildFix available

Avoid using `forEach` with a function literal.

## Details

[#](#details)

AVOID using `forEach` with a function literal.

 The `for` loop enables a developer to be clear and explicit as to their intent. A return in the body of the `for` loop returns from the body of the function, where as a return in the body of the `forEach` closure only returns a value for that iteration of the `forEach`. The body of a `for` loop can contain `await`s, while the closure body of a `forEach` cannot. 

BAD:

dart

```
people.forEach((person) {
  ...
});
```

content_copy

GOOD:

dart

```
for (var person in people) {
  ...
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_function_literals_in_foreach_calls` rule, add `avoid_function_literals_in_foreach_calls` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_function_literals_in_foreach_calls
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_function_literals_in_foreach_calls: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_function_literals_in_foreach_calls: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_function_literals_in_foreach_calls).
