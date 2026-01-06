Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unrelated_type_equality_checks](/tools/linter-rules/unrelated_type_equality_checks)

# unrelated_type_equality_checks

Learn about the unrelated_type_equality_checks linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unrelated_type_equality_checks)

verified_userStablecirclesCore

Equality operator `==` invocation with references of unrelated types.

## Details

[#](#details)

DON'T Compare references of unrelated types for equality.

 Comparing references of a type where neither is a subtype of the other most likely will return `false` and might not reflect programmer's intent. 

`Int64` and `Int32` from `package:fixnum` allow comparing to `int` provided the `int` is on the right hand side. The lint allows this as a special case. 

BAD:

dart

```
void someFunction() {
  var x = '1';
  if (x == 1) print('someFunction'); // LINT
}
```

content_copy

BAD:

dart

```
void someFunction1() {
  String x = '1';
  if (x == 1) print('someFunction1'); // LINT
}
```

content_copy

BAD:

dart

```
void someFunction13(DerivedClass2 instance) {
  var other = DerivedClass3();
​
  if (other == instance) print('someFunction13'); // LINT
}
​
class ClassBase {}
​
class DerivedClass1 extends ClassBase {}
​
abstract class Mixin {}
​
class DerivedClass2 extends ClassBase with Mixin {}
​
class DerivedClass3 extends ClassBase implements Mixin {}
```

content_copy

GOOD:

dart

```
void someFunction2() {
  var x = '1';
  var y = '2';
  if (x == y) print(someFunction2); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction3() {
  for (var i = 0; i < 10; i++) {
    if (i == 0) print(someFunction3); // OK
  }
}
```

content_copy

GOOD:

dart

```
void someFunction4() {
  var x = '1';
  if (x == null) print(someFunction4); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction7() {
  List someList;
​
  if (someList.length == 0) print('someFunction7'); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction8(ClassBase instance) {
  DerivedClass1 other;
​
  if (other == instance) print('someFunction8'); // OK
}
```

content_copy

GOOD:

dart

```
void someFunction10(unknown) {
  var what = unknown - 1;
  for (var index = 0; index < unknown; index++) {
    if (what == index) print('someFunction10'); // OK
  }
}
```

content_copy

GOOD:

dart

```
void someFunction11(Mixin instance) {
  var other = DerivedClass2();
​
  if (other == instance) print('someFunction11'); // OK
  if (other != instance) print('!someFunction11'); // OK
}
​
class ClassBase {}
​
abstract class Mixin {}
​
class DerivedClass2 extends ClassBase with Mixin {}
```

content_copy

## Enable

[#](#enable)

 To enable the `unrelated_type_equality_checks` rule, add `unrelated_type_equality_checks` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unrelated_type_equality_checks
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unrelated_type_equality_checks: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unrelated_type_equality_checks: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unrelated_type_equality_checks).
