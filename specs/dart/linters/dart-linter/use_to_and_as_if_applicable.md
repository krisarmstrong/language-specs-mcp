Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_to_and_as_if_applicable](/tools/linter-rules/use_to_and_as_if_applicable)

# use_to_and_as_if_applicable

Learn about the use_to_and_as_if_applicable linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_to_and_as_if_applicable)

verified_userStable

Start the name of the method with to/_to or as/_as if applicable.

## Details

[#](#details)

 From [Effective Dart](https://dart.dev/effective-dart/design#prefer-naming-a-method-to___-if-it-copies-the-objects-state-to-a-new-object): 

PREFER naming a method `to___()` if it copies the object's state to a new object. 

PREFER naming a method `as___()` if it returns a different representation backed by the original object. 

BAD:

dart

```
class Bar {
  Foo myMethod() {
    return Foo.from(this);
  }
}
```

content_copy

GOOD:

dart

```
class Bar {
  Foo toFoo() {
    return Foo.from(this);
  }
}
```

content_copy

GOOD:

dart

```
class Bar {
  Foo asFoo() {
    return Foo.from(this);
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_to_and_as_if_applicable` rule, add `use_to_and_as_if_applicable` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_to_and_as_if_applicable
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_to_and_as_if_applicable: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_to_and_as_if_applicable: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_to_and_as_if_applicable).
