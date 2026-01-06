Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [hash_and_equals](/tools/linter-rules/hash_and_equals)

# hash_and_equals

Learn about the hash_and_equals linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/hash_and_equals)

verified_userStablecirclesCorebuildFix available

Always override `hashCode` if overriding `==`.

## Details

[#](#details)

DO override `hashCode` if overriding `==` and prefer overriding `==` if overriding `hashCode`. 

 Every object in Dart has a `hashCode`. Both the `==` operator and the `hashCode` property of objects must be consistent in order for a common hash map implementation to function properly. Thus, when overriding `==`, the `hashCode` should also be overridden to maintain consistency. Similarly, if `hashCode` is overridden, `==` should be also. 

BAD:

dart

```
class Bad {
  final int value;
  Bad(this.value);
​
  @override
  bool operator ==(Object other) => other is Bad && other.value == value;
}
```

content_copy

GOOD:

dart

```
class Better {
  final int value;
  Better(this.value);
​
  @override
  bool operator ==(Object other) =>
      other is Better &&
      other.runtimeType == runtimeType &&
      other.value == value;
​
  @override
  int get hashCode => value.hashCode;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `hash_and_equals` rule, add `hash_and_equals` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - hash_and_equals
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `hash_and_equals: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    hash_and_equals: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/hash_and_equals).
