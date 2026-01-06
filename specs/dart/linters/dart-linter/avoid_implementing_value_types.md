Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_implementing_value_types](/tools/linter-rules/avoid_implementing_value_types)

# avoid_implementing_value_types

Learn about the avoid_implementing_value_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_implementing_value_types)

verified_userStable

Don't implement classes that override `==`.

## Details

[#](#details)

DON'T implement classes that override `==`.

 The `==` operator is contractually required to be an equivalence relation; that is, symmetrically for all objects `o1` and `o2`, `o1 == o2` and `o2 == o1` must either both be true, or both be false. 

NOTE: Dart does not have true value types, so instead we consider a class that implements `==` as a proxy for identifying value types. 

 When using `implements`, you do not inherit the method body of `==`, making it nearly impossible to follow the contract of `==`. Classes that override `==` typically are usable directly in tests without creating mocks or fakes as well. For example, for a given class `Size`: 

dart

```
class Size {
  final int inBytes;
  const Size(this.inBytes);
​
  @override
  bool operator ==(Object other) => other is Size && other.inBytes == inBytes;
​
  @override
  int get hashCode => inBytes.hashCode;
}
```

content_copy

BAD:

dart

```
class CustomSize implements Size {
  final int inBytes;
  const CustomSize(this.inBytes);
​
  int get inKilobytes => inBytes ~/ 1000;
}
```

content_copy

BAD:

dart

```
import 'package:test/test.dart';
import 'size.dart';
​
class FakeSize implements Size {
  int inBytes = 0;
}
​
void main() {
  test('should not throw on a size >1Kb', () {
    expect(() => someFunction(FakeSize()..inBytes = 1001), returnsNormally);
  });
}
```

content_copy

GOOD:

dart

```
class ExtendedSize extends Size {
  ExtendedSize(int inBytes) : super(inBytes);
​
  int get inKilobytes => inBytes ~/ 1000;
}
```

content_copy

GOOD:

dart

```
import 'package:test/test.dart';
import 'size.dart';
​
void main() {
  test('should not throw on a size >1Kb', () {
    expect(() => someFunction(Size(1001)), returnsNormally);
  });
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_implementing_value_types` rule, add `avoid_implementing_value_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_implementing_value_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_implementing_value_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_implementing_value_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_implementing_value_types).
