Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_wildcard_variable_uses](/tools/linter-rules/no_wildcard_variable_uses)

# no_wildcard_variable_uses

Learn about the no_wildcard_variable_uses linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_wildcard_variable_uses)

verified_userStablecirclesCore

Don't use wildcard parameters or variables.

## Details

[#](#details)

DON'T use wildcard parameters or variables.

 Wildcard parameters and local variables (e.g. underscore-only names like `_`, `__`, `___`, etc.) will become non-binding in a future version of the Dart language. Any existing code that uses wildcard parameters or variables will break. In anticipation of this change, and to make adoption easier, this lint disallows wildcard and variable parameter uses. 

BAD:

dart

```
var _ = 1;
print(_); // LINT
```

content_copydart

```
void f(int __) {
  print(__); // LINT multiple underscores too
}
```

content_copy

GOOD:

dart

```
for (var _ in [1, 2, 3]) count++;
```

content_copydart

```
var [a, _, b, _] = [1, 2, 3, 4];
```

content_copy

## Enable

[#](#enable)

 To enable the `no_wildcard_variable_uses` rule, add `no_wildcard_variable_uses` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_wildcard_variable_uses
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_wildcard_variable_uses: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_wildcard_variable_uses: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_wildcard_variable_uses).
