Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [remove_deprecations_in_breaking_versions](/tools/linter-rules/remove_deprecations_in_breaking_versions)

# remove_deprecations_in_breaking_versions

Learn about the remove_deprecations_in_breaking_versions linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/remove_deprecations_in_breaking_versions)

verified_userStable

Deprecation in major version.

## Details

[#](#details)

DO Remove deprecated elements in breaking version numbers. Breaking version numbers are on the form `x.0.0` or `0.x.0`. 

For example given a package with a `pubspec.yaml` file containing:

yaml

```
name: p
version: 2.0.0
environment:
  sdk: ^3.9.0
```

content_copy

BAD:

dart

```
@deprecated
void f() {}
```

content_copy

GOOD:

dart

```
// (f is removed).
```

content_copy

GOOD:

yaml

```
name: p
version: 1.0.1
environment:
  sdk: ^3.9.0
```

content_copy

## Enable

[#](#enable)

 To enable the `remove_deprecations_in_breaking_versions` rule, add `remove_deprecations_in_breaking_versions` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - remove_deprecations_in_breaking_versions
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `remove_deprecations_in_breaking_versions: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    remove_deprecations_in_breaking_versions: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/remove_deprecations_in_breaking_versions).
