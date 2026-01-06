Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [only_throw_errors](/tools/linter-rules/only_throw_errors)

# only_throw_errors

Learn about the only_throw_errors linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/only_throw_errors)

verified_userStable

Only throw instances of classes extending either Exception or Error.

## Details

[#](#details)

DO throw only instances of classes that extend `dart.core.Error` or `dart.core.Exception`. 

 Throwing instances that do not extend `Error` or `Exception` is a bad practice; doing this is usually a hack for something that should be implemented more thoroughly. 

BAD:

dart

```
void throwString() {
  throw 'hello world!'; // LINT
}
```

content_copy

GOOD:

dart

```
void throwArgumentError() {
  Error error = ArgumentError('oh!');
  throw error; // OK
}
```

content_copy

## Enable

[#](#enable)

 To enable the `only_throw_errors` rule, add `only_throw_errors` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - only_throw_errors
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `only_throw_errors: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    only_throw_errors: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/only_throw_errors).
