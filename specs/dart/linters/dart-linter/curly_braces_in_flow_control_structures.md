Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [curly_braces_in_flow_control_structures](/tools/linter-rules/curly_braces_in_flow_control_structures)

# curly_braces_in_flow_control_structures

Learn about the curly_braces_in_flow_control_structures linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/curly_braces_in_flow_control_structures)

verified_userStablecirclesCorebuildFix available

DO use curly braces for all flow control structures.

## Details

[#](#details)

DO use curly braces for all flow control structures.

 Doing so avoids the [dangling else](https://en.wikipedia.org/wiki/Dangling_else) problem. 

BAD:

dart

```
if (overflowChars != other.overflowChars)
  return overflowChars < other.overflowChars;
```

content_copy

GOOD:

dart

```
if (isWeekDay) {
  print('Bike to work!');
} else {
  print('Go dancing or read a book!');
}
```

content_copy

 There is one exception to this: an `if` statement with no `else` clause where the entire `if` statement (including the condition and the body) fits in one line. In that case, you may leave off the braces if you prefer: 

GOOD:

dart

```
if (arg == null) return defaultValue;
```

content_copy

If the body wraps to the next line, though, use braces:

GOOD:

dart

```
if (overflowChars != other.overflowChars) {
  return overflowChars < other.overflowChars;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `curly_braces_in_flow_control_structures` rule, add `curly_braces_in_flow_control_structures` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - curly_braces_in_flow_control_structures
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `curly_braces_in_flow_control_structures: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    curly_braces_in_flow_control_structures: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/curly_braces_in_flow_control_structures).
