Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_statements](/tools/linter-rules/unnecessary_statements)

# unnecessary_statements

Learn about the unnecessary_statements linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_statements)

verified_userStable

Avoid using unnecessary statements.

## Details

[#](#details)

AVOID using unnecessary statements.

 Statements which have no clear effect are usually unnecessary, or should be broken up. 

For example,

BAD:

dart

```
myvar;
list.clear;
1 + 2;
methodOne() + methodTwo();
foo ? bar : baz;
```

content_copy

 Though the added methods have a clear effect, the addition itself does not unless there is some magical overload of the + operator. 

Usually code like this indicates an incomplete thought, and is a bug.

GOOD:

dart

```
some.method();
const SomeClass();
methodOne();
methodTwo();
foo ? bar() : baz();
return myvar;
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_statements` rule, add `unnecessary_statements` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_statements
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_statements: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_statements: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_statements).
