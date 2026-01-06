Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [null_check_on_nullable_type_parameter](/tools/linter-rules/null_check_on_nullable_type_parameter)

# null_check_on_nullable_type_parameter

Learn about the null_check_on_nullable_type_parameter linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/null_check_on_nullable_type_parameter)

verified_userStablecirclesCorebuildFix available

Don't use `null` check on a potentially nullable type parameter.

## Details

[#](#details)

DON'T use `null` check on a potentially nullable type parameter.

 Given a generic type parameter `T` which has a nullable bound (e.g., the default bound of `Object?`), it is very easy to introduce erroneous `null` checks when working with a variable of type `T?`. Specifically, it is not uncommon to have `T? x;` and want to assert that `x` has been set to a valid value of type `T`. A common mistake is to do so using `x!`. This is almost always incorrect, since if `T` is a nullable type, `x` may validly hold `null` as a value of type `T`. 

BAD:

dart

```
T run<T>(T callback()) {
  T? result;
  (() { result = callback(); })();
  return result!;
}
```

content_copy

GOOD:

dart

```
T run<T>(T callback()) {
  T? result;
  (() { result = callback(); })();
  return result as T;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `null_check_on_nullable_type_parameter` rule, add `null_check_on_nullable_type_parameter` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - null_check_on_nullable_type_parameter
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `null_check_on_nullable_type_parameter: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    null_check_on_nullable_type_parameter: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/null_check_on_nullable_type_parameter).
