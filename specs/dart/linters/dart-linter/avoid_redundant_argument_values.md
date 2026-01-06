Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_redundant_argument_values](/tools/linter-rules/avoid_redundant_argument_values)

# avoid_redundant_argument_values

Learn about the avoid_redundant_argument_values linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_redundant_argument_values)

verified_userStablebuildFix available

Avoid redundant argument values.

## Details

[#](#details)

DON'T pass an argument that matches the corresponding parameter's default value. 

 Note that a method override can change the default value of a parameter, so that an argument may be equal to one default value, and not the other. Take, for example, two classes, `A` and `B` where `B` is a subclass of `A`, and `B` overrides a method declared on `A`, and that method has a parameter with one default value in `A`'s declaration, and a different default value in `B`'s declaration. If the static type of the target of the invoked method is `B`, and `B`'s default value matches the argument, then the argument can be omitted (and if the argument value is different, then a lint is not reported). If, however, the static type of the target of the invoked method is `A`, then a lint may be reported, but we cannot know statically which method is invoked, so the reported lint may be a false positive. Such cases can be ignored inline with a comment like `// ignore: avoid_redundant_argument_values`. 

BAD:

dart

```
void f({bool valWithDefault = true, bool? val}) {
  ...
}
​
void main() {
  f(valWithDefault: true);
}
```

content_copy

GOOD:

dart

```
void f({bool valWithDefault = true, bool? val}) {
  ...
}
​
void main() {
  f(valWithDefault: false);
  f();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_redundant_argument_values` rule, add `avoid_redundant_argument_values` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_redundant_argument_values
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_redundant_argument_values: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_redundant_argument_values: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_redundant_argument_values).
