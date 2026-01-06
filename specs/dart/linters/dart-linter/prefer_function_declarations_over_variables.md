Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_function_declarations_over_variables](/tools/linter-rules/prefer_function_declarations_over_variables)

# prefer_function_declarations_over_variables

Learn about the prefer_function_declarations_over_variables linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_function_declarations_over_variables)

verified_userStablethumb_upRecommendedbuildFix available

Use a function declaration to bind a function to a name.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/usage#do-use-a-function-declaration-to-bind-a-function-to-a-name): 

DO use a function declaration to bind a function to a name.

 As Dart allows local function declarations, it is a good practice to use them in the place of function literals. 

BAD:

dart

```
void main() {
  var localFunction = () {
    ...
  };
}
```

content_copy

GOOD:

dart

```
void main() {
  localFunction() {
    ...
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_function_declarations_over_variables` rule, add `prefer_function_declarations_over_variables` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_function_declarations_over_variables
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_function_declarations_over_variables: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_function_declarations_over_variables: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_function_declarations_over_variables).
