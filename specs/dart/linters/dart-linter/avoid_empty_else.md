Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_empty_else](/tools/linter-rules/avoid_empty_else)

# avoid_empty_else

Learn about the avoid_empty_else linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_empty_else)

verified_userStablecirclesCorebuildFix available

Avoid empty statements in else clauses.

## Details

[#](#details)

AVOID empty statements in the `else` clause of `if` statements. 

BAD:

dart

```
if (x > y)
  print('1');
else ;
  print('2');
```

content_copy

 If you want a statement that follows the empty clause to conditionally run, remove the dangling semicolon to include it in the `else` clause. Optionally, also enclose the else's statement in a block. 

GOOD:

dart

```
if (x > y)
  print('1');
else
  print('2');
```

content_copy

GOOD:

dart

```
if (x > y) {
  print('1');
} else {
  print('2');
}
```

content_copy

 If you want a statement that follows the empty clause to unconditionally run, remove the `else` clause. 

GOOD:

dart

```
if (x > y) print('1');
​
print('2');
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_empty_else` rule, add `avoid_empty_else` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_empty_else
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_empty_else: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_empty_else: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_empty_else).
