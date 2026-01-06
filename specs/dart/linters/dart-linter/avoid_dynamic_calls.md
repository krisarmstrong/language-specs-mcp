Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [avoid_dynamic_calls](/tools/linter-rules/avoid_dynamic_calls)

# avoid_dynamic_calls

Learn about the avoid_dynamic_calls linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_dynamic_calls)

verified_userStable

Avoid method calls or property accesses on a `dynamic` target.

## Details

[#](#details)

DO avoid method calls or accessing properties on an object that is either explicitly or implicitly statically typed `dynamic`. Dynamic calls are treated slightly different in every runtime environment and compiler, but most production modes (and even some development modes) have both compile size and runtime performance penalties associated with dynamic calls. 

 Additionally, targets typed `dynamic` disables most static analysis, meaning it is easier to lead to a runtime `NoSuchMethodError` or `TypeError` than properly statically typed Dart code. 

There is an exception to methods and properties that exist on `Object?`:

- `a.hashCode`
- `a.runtimeType`
- `a.noSuchMethod(someInvocation)`
- `a.toString()`

 ... these members are dynamically dispatched in the web-based runtimes, but not in the VM-based ones. Additionally, they are so common that it would be very punishing to disallow `any.toString()` or `any == true`, for example. 

 Note that despite `Function` being a type, the semantics are close to identical to `dynamic`, and calls to an object that is typed `Function` will also trigger this lint. 

Dynamic calls are allowed on cast expressions (`as dynamic` or `as Function`).

BAD:

dart

```
void explicitDynamicType(dynamic object) {
  print(object.foo());
}
​
void implicitDynamicType(object) {
  print(object.foo());
}
​
abstract class SomeWrapper {
  T doSomething<T>();
}
​
void inferredDynamicType(SomeWrapper wrapper) {
  var object = wrapper.doSomething();
  print(object.foo());
}
​
void callDynamic(dynamic function) {
  function();
}
​
void functionType(Function function) {
  function();
}
```

content_copy

GOOD:

dart

```
void explicitType(Fooable object) {
  object.foo();
}
​
void castedType(dynamic object) {
  (object as Fooable).foo();
}
​
abstract class SomeWrapper {
  T doSomething<T>();
}
​
void inferredType(SomeWrapper wrapper) {
  var object = wrapper.doSomething<Fooable>();
  object.foo();
}
​
void functionTypeWithParameters(Function() function) {
  function();
}
```

content_copy

## Enable

[#](#enable)

 To enable the `avoid_dynamic_calls` rule, add `avoid_dynamic_calls` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - avoid_dynamic_calls
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `avoid_dynamic_calls: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    avoid_dynamic_calls: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/avoid_dynamic_calls).
