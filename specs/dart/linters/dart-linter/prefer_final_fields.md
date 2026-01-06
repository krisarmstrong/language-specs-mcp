Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_final_fields](/tools/linter-rules/prefer_final_fields)

# prefer_final_fields

Learn about the prefer_final_fields linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_final_fields)

verified_userStablethumb_upRecommendedbuildFix available

Private field could be `final`.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#prefer-making-fields-and-top-level-variables-final): 

DO prefer declaring private fields as `final` if they are not reassigned later in the library. 

 Declaring fields as `final` when possible is a good practice because it helps avoid accidental reassignments and allows the compiler to do optimizations. 

BAD:

dart

```
class BadImmutable {
  var _label = 'hola mundo! BadImmutable'; // LINT
  var label = 'hola mundo! BadImmutable'; // OK
}
```

content_copy

BAD:

dart

```
class MultipleMutable {
  var _label = 'hola mundo! GoodMutable', _offender = 'mumble mumble!'; // LINT
  var _someOther; // LINT
​
  MultipleMutable() : _someOther = 5;
​
  MultipleMutable(this._someOther);
​
  void changeLabel() {
    _label= 'hello world! GoodMutable';
  }
}
```

content_copy

GOOD:

dart

```
class GoodImmutable {
  final label = 'hola mundo! BadImmutable', bla = 5; // OK
  final _label = 'hola mundo! BadImmutable', _bla = 5; // OK
}
```

content_copy

GOOD:

dart

```
class GoodMutable {
  var _label = 'hola mundo! GoodMutable';
​
  void changeLabel() {
    _label = 'hello world! GoodMutable';
  }
}
```

content_copy

BAD:

dart

```
class AssignedInAllConstructors {
  var _label; // LINT
  AssignedInAllConstructors(this._label);
  AssignedInAllConstructors.withDefault() : _label = 'Hello';
}
```

content_copy

GOOD:

dart

```
class NotAssignedInAllConstructors {
  var _label; // OK
  NotAssignedInAllConstructors();
  NotAssignedInAllConstructors.withDefault() : _label = 'Hello';
}
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_final_fields` rule, add `prefer_final_fields` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_final_fields
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_final_fields: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_final_fields: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_final_fields).
