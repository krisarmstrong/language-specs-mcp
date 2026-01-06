Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [empty_statements](/tools/linter-rules/empty_statements)

# empty_statements

Learn about the empty_statements linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/empty_statements)

verified_userStablethumb_upRecommendedbuildFix available

Avoid empty statements.

## Details

[#](#details)

AVOID empty statements.

Empty statements almost always indicate a bug.

For example,

BAD:

dart

```
if (complicated.expression.foo());
  bar();
```

content_copy

Formatted with `dart format` the bug becomes obvious:

dart

```
if (complicated.expression.foo()) ;
bar();
```

content_copy

Better to avoid the empty statement altogether.

GOOD:

dart

```
if (complicated.expression.foo())
  bar();
```

content_copy

## Enable

[#](#enable)

 To enable the `empty_statements` rule, add `empty_statements` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - empty_statements
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `empty_statements: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    empty_statements: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/empty_statements).
