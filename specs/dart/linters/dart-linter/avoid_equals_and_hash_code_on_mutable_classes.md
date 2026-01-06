Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_equals_and_hash_code_on_mutable_classes](/tools/linter-rules/avoid_equals_and_hash_code_on_mutable_classes)

# avoid_equals_and_hash_code_on_mutable_classes

Learn about the avoid_equals_and_hash_code_on_mutable_classes linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_equals_and_hash_code_on_mutable_classes)

verified_userStable

Avoid overloading operator == and hashCode on classes not marked `@immutable`.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#avoid-defining-custom-equality-for-mutable-classes): 

AVOID overloading operator == and hashCode on classes not marked `@immutable`. 

 If a class is not immutable, overloading `operator ==` and `hashCode` can lead to unpredictable and undesirable behavior when used in collections. 

BAD:

dart

```
class B {
  String key;
  const B(this.key);
  @override
  operator ==(other) => other is B && other.key == key;
  @override
  int get hashCode => key.hashCode;
}
```

content_copy

GOOD:

dart

```
@immutable
class A {
  final String key;
  const A(this.key);
  @override
  operator ==(other) => other is A && other.key == key;
  @override
  int get hashCode => key.hashCode;
}
```

content_copy

 NOTE: The lint checks the use of the `@immutable` annotation, and will trigger even if the class is otherwise not mutable. Thus: 

BAD:

dart

```
class C {
  final String key;
  const C(this.key);
  @override
  operator ==(other) => other is C && other.key == key;
  @override
  int get hashCode => key.hashCode;
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_equals_and_hash_code_on_mutable_classes` rule, add `avoid_equals_and_hash_code_on_mutable_classes` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_equals_and_hash_code_on_mutable_classes
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_equals_and_hash_code_on_mutable_classes: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_equals_and_hash_code_on_mutable_classes: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_equals_and_hash_code_on_mutable_classes).
