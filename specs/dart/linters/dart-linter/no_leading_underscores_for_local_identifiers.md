Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_leading_underscores_for_local_identifiers](/tools/linter-rules/no_leading_underscores_for_local_identifiers)

# no_leading_underscores_for_local_identifiers

Learn about the no_leading_underscores_for_local_identifiers linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_leading_underscores_for_local_identifiers)

verified_userStablethumb_upRecommendedbuildFix available

Avoid leading underscores for local identifiers.

## Details

[#](#details)

DON'T use a leading underscore for identifiers that aren't private. Dart uses a leading underscore in an identifier to mark members and top-level declarations as private. This trains users to associate a leading underscore with one of those kinds of declarations. They see `_` and think "private". There is no concept of "private" for local variables or parameters. When one of those has a name that starts with an underscore, it sends a confusing signal to the reader. To avoid that, don't use leading underscores in those names. 

EXCEPTION:: An unused parameter can be named `_`, `__`, `___`, etc. This is common practice in callbacks where you are passed a value but you don't need to use it. Giving it a name that consists solely of underscores is the idiomatic way to indicate that the value isn't used. 

BAD:

dart

```
void print(String _name) {
  var _size = _name.length;
  ...
}
```

content_copy

GOOD:

dart

```
void print(String name) {
  var size = name.length;
  ...
}
```

content_copy

OK:

dart

```
[1,2,3].map((_) => print('Hello'));
```

content_copy

## Enable

[#](#enable)

 To enable the `no_leading_underscores_for_local_identifiers` rule, add `no_leading_underscores_for_local_identifiers` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_leading_underscores_for_local_identifiers
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_leading_underscores_for_local_identifiers: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_leading_underscores_for_local_identifiers: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_leading_underscores_for_local_identifiers).
