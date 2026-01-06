Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [invalid_runtime_check_with_js_interop_types](/tools/linter-rules/invalid_runtime_check_with_js_interop_types)

# invalid_runtime_check_with_js_interop_types

Learn about the invalid_runtime_check_with_js_interop_types linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/invalid_runtime_check_with_js_interop_types)

verified_userStablethumb_upRecommended

 Avoid runtime type tests with JS interop types where the result may not be platform-consistent. 

## Details

[#](#details)

DON'T use `is` checks where the type is a JS interop type.

DON'T use `is` checks where the type is a generic Dart type that has JS interop type arguments. 

DON'T use `is` checks with a JS interop value.

`dart:js_interop` types have runtime types that are different based on whether you are compiling to JS or to Wasm. Therefore, runtime type checks may result in different behavior. Runtime checks also do not necessarily check that a JS interop value is a particular JavaScript type. 

BAD:

dart

```
extension type HTMLElement(JSObject o) {}
extension type HTMLDivElement(JSObject o) implements HTMLElement {}
​
void compute(JSAny a, bool b, List<JSObject> lo, List<String> ls, JSObject o,
    HTMLElement e) {
  a is String; // LINT, checking that a JS value is a Dart type
  b is JSBoolean; // LINT, checking that a Dart value is a JS type
  a is JSString; // LINT, checking that a JS value is a different JS interop
                 // type
  o is JSNumber; // LINT, checking that a JS value is a different JS interop
                 // type
  lo is List<String>; // LINT, JS interop type argument and Dart type argument
                      // are incompatible
  ls is List<JSString>; // LINT, Dart type argument and JS interop type argument
                        // are incompatible
  lo is List<JSArray>; // LINT, comparing JS interop type argument with
                       // different JS interop type argument
  lo is List<JSNumber>; // LINT, comparing JS interop type argument with
                        // different JS interop type argument
  o is HTMLElement; // LINT, true because both are JSObjects but doesn't check
                    // that it's a JS HTMLElement
  e is HTMLDivElement; // LINT, true because both are JSObjects but doesn't
                       // check that it's a JS HTMLDivElement
}
```

content_copy

 Prefer using JS interop helpers like `isA` from `dart:js_interop` to check the underlying type of JS interop values. 

GOOD:

dart

```
extension type HTMLElement(JSObject o) implements JSObject {}
extension type HTMLDivElement(JSObject o) implements HTMLElement {}
​
void compute(JSAny a, List<JSAny> l, JSObject o, HTMLElement e) {
  a.isA<JSString>; // OK, uses JS interop to check it is a JS string
  l[0].isA<JSString>; // OK, uses JS interop to check it is a JS string
  o.isA<HTMLElement>(); // OK, uses JS interop to check `o` is an HTMLElement
  e.isA<HTMLDivElement>(); // OK, uses JS interop to check `e` is an
                           // HTMLDivElement
}
```

content_copy

DON'T use `as` to cast a JS interop value to an unrelated Dart type or an unrelated Dart value to a JS interop type. 

DON'T use `as` to cast a JS interop value to a JS interop type represented by an incompatible `dart:js_interop` type. 

BAD:

dart

```
extension type Window(JSObject o) {}
​
void compute(String s, JSBoolean b, Window w, List<String> l,
    List<JSObject> lo) {
  s as JSString; // LINT, casting Dart type to JS interop type
  b as bool; // LINT, casting JS interop type to Dart type
  b as JSNumber; // LINT, JSBoolean and JSNumber are incompatible
  b as Window; // LINT, JSBoolean and JSObject are incompatible
  w as JSBoolean; // LINT, JSObject and JSBoolean are incompatible
  l as List<JSString>; // LINT, casting Dart value with Dart type argument to
                       // Dart type with JS interop type argument
  lo as List<String>; // LINT, casting Dart value with JS interop type argument
                      // to Dart type with Dart type argument
  lo as List<JSBoolean>; // LINT, casting Dart value with JS interop type
                         // argument to Dart type with incompatible JS interop
                         // type argument
}
```

content_copy

 Prefer using `dart:js_interop` conversion methods to convert a JS interop value to a Dart value and vice versa. 

GOOD:

dart

```
extension type Window(JSObject o) {}
extension type Document(JSObject o) {}
​
void compute(String s, JSBoolean b, Window w, JSArray<JSString> a,
    List<String> ls, JSObject o, List<JSAny> la) {
  s.toJS; // OK, converts the Dart type to a JS type
  b.toDart; // OK, converts the JS type to a Dart type
  a.toDart; // OK, converts the JS type to a Dart type
  w as Document; // OK, but no runtime check that `w` is a JS Document
  ls.map((e) => e.toJS).toList(); // OK, converts the Dart types to JS types
  o as JSArray<JSString>; // OK, JSObject and JSArray are compatible
  la as List<JSString>; // OK, JSAny and JSString are compatible
  (o as Object) as JSObject; // OK, Object is a supertype of JSAny
}
```

content_copy

## Enable

[#](#enable)

 To enable the `invalid_runtime_check_with_js_interop_types` rule, add `invalid_runtime_check_with_js_interop_types` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - invalid_runtime_check_with_js_interop_types
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `invalid_runtime_check_with_js_interop_types: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    invalid_runtime_check_with_js_interop_types: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/invalid_runtime_check_with_js_interop_types).
