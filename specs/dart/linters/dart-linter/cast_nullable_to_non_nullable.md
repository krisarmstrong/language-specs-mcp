Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [cast_nullable_to_non_nullable](/tools/linter-rules/cast_nullable_to_non_nullable)

# cast_nullable_to_non_nullable

Learn about the cast_nullable_to_non_nullable linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/cast_nullable_to_non_nullable)

verified_userStablebuildFix available

Don't cast a nullable value to a non nullable type.

## Details

[#](#details)

DON'T cast a nullable value to a non nullable type. This hides a null check and most of the time it is not what is expected. 

BAD:

dart

```
class A {}
class B extends A {}
​
A? a;
var v = a as B;
var v = a as A;
```

content_copy

GOOD:

dart

```
class A {}
class B extends A {}
​
A? a;
var v = a! as B;
var v = a!;
```

content_copy

## Enable

[#](#enable)

 To enable the `cast_nullable_to_non_nullable` rule, add `cast_nullable_to_non_nullable` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - cast_nullable_to_non_nullable
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `cast_nullable_to_non_nullable: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    cast_nullable_to_non_nullable: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/cast_nullable_to_non_nullable).
