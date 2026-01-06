Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [always_put_control_body_on_new_line](/tools/linter-rules/always_put_control_body_on_new_line)

# always_put_control_body_on_new_line

Learn about the always_put_control_body_on_new_line linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_put_control_body_on_new_line)

verified_userStablebuildFix available

Separate the control structure expression from its statement.

## Details

[#](#details)

From the [style guide for the flutter repo](https://flutter.dev/style-guide/):

DO separate the control structure expression from its statement.

 Don't put the statement part of an `if`, `for`, `while`, `do` on the same line as the expression, even if it is short. Doing so makes it unclear that there is relevant code there. This is especially important for early returns. 

BAD:

dart

```
if (notReady) return;
​
if (notReady)
  return;
else print('ok')
​
while (condition) i += 1;
```

content_copy

GOOD:

dart

```
if (notReady)
  return;
​
if (notReady)
  return;
else
  print('ok')
​
while (condition)
  i += 1;
```

content_copy

 Note that this rule can conflict with the [Dart formatter](https://dart.dev/tools/dart-format), and should not be enabled when the Dart formatter is used. 

## Enable

[#](#enable)

 To enable the `always_put_control_body_on_new_line` rule, add `always_put_control_body_on_new_line` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - always_put_control_body_on_new_line
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `always_put_control_body_on_new_line: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    always_put_control_body_on_new_line: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/always_put_control_body_on_new_line).
