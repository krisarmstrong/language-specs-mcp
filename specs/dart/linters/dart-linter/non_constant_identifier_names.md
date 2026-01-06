Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [non_constant_identifier_names](/tools/linter-rules/non_constant_identifier_names)

# non_constant_identifier_names

Learn about the non_constant_identifier_names linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/non_constant_identifier_names)

verified_userStablecirclesCorebuildFix available

Name non-constant identifiers using lowerCamelCase.

## Details

[#](#details)

DO name non-constant identifiers using lowerCamelCase.

 Class members, top-level definitions, variables, parameters, named parameters and named constructors should capitalize the first letter of each word except the first word, and use no separators. 

GOOD:

dart

```
var item;
​
HttpRequest httpRequest;
​
align(clearItems) {
  // ...
}
```

content_copy

## Enable

[#](#enable)

 To enable the `non_constant_identifier_names` rule, add `non_constant_identifier_names` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - non_constant_identifier_names
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `non_constant_identifier_names: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    non_constant_identifier_names: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/non_constant_identifier_names).
