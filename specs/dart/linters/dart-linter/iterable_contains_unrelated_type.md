Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [iterable_contains_unrelated_type](/tools/linter-rules/iterable_contains_unrelated_type)

# iterable_contains_unrelated_type

Learn about the iterable_contains_unrelated_type linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/iterable_contains_unrelated_type)

errorRemoved

Invocation of `Iterable<E>.contains` with references of unrelated types.

## Details

[#](#details)

NOTE: This rule is removed in Dart 3.3.0; it is no longer functional.

DON'T invoke `contains` on `Iterable` with an instance of different type than the parameter type. 

 Doing this will invoke `==` on its elements and most likely will return `false`. 

BAD:

dart

```
void someFunction() {
  var list = <int>[];
  if (list.contains('1')) print('someFunction'); // LINT
}
```

content_copy

BAD:

dart

```
void someFunction3() {
  List<int> list = <int>[];
  if (list.contains('1')) print('someFunction3'); // LINT
}
```

content_copy

BAD:

dart

```
void someFunction8() {
  List<DerivedClass2> list = <DerivedClass2>[];
  DerivedClass3 instance;
  if (list.contains(instance)) print('someFunction8'); // LINT
}
```

content_copy

BAD:

dart

```
abstract class SomeIterable<E> implements Iterable<E> {}
​
abstract class MyClass implements SomeIterable<int> {
  bool badMethod(String thing) => this.contains(thing); // LINT
}
```

content_copy

GOOD:

dart

```
void someFunction10() {
  var list = [];
  if (list.contains(1)) print('someFunction10'); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction1() {
  var list = <int>[];
  if (list.contains(1)) print('someFunction1'); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction4() {
  List<int> list = <int>[];
  if (list.contains(1)) print('someFunction4'); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction5() {
  List<ClassBase> list = <ClassBase>[];
  DerivedClass1 instance;
  if (list.contains(instance)) print('someFunction5'); // OK
}
​
abstract class ClassBase {}
​
class DerivedClass1 extends ClassBase {}
```

content_copy

GOOD:

dart

```
void someFunction6() {
  List<Mixin> list = <Mixin>[];
  DerivedClass2 instance;
  if (list.contains(instance)) print('someFunction6'); // OK
}
​
abstract class ClassBase {}
​
abstract class Mixin {}
​
class DerivedClass2 extends ClassBase with Mixin {}
```

content_copy

GOOD:

dart

```
void someFunction7() {
  List<Mixin> list = <Mixin>[];
  DerivedClass3 instance;
  if (list.contains(instance)) print('someFunction7'); // OK
}
​
abstract class ClassBase {}
​
abstract class Mixin {}
​
class DerivedClass3 extends ClassBase implements Mixin {}
```

content_copy

## Enable

[#](#enable)

 To enable the `iterable_contains_unrelated_type` rule, add `iterable_contains_unrelated_type` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - iterable_contains_unrelated_type
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `iterable_contains_unrelated_type: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    iterable_contains_unrelated_type: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/iterable_contains_unrelated_type).
