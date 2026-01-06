Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [library_private_types_in_public_api](/tools/linter-rules/library_private_types_in_public_api)

# library_private_types_in_public_api

Learn about the library_private_types_in_public_api linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/library_private_types_in_public_api)

verified_userStablethumb_upRecommended

Avoid using private types in public APIs.

## Details

[#](#details)

AVOID using library private types in public APIs.

 For the purposes of this lint, a public API is considered to be any top-level or member declaration unless the declaration is library private or contained in a declaration that's library private. The following uses of types are checked: 

- the return type of a function or method,
- the type of any parameter of a function or method,
-  the bound of a type parameter to any function, method, class, mixin, extension's extended type, or type alias, 
- the type of any top level variable or field,
-  any type used in the declaration of a type alias (for example `typedef F = _Private Function();`), or 
- any type used in the `on` clause of an extension or a mixin

BAD:

dart

```
f(_Private p) { ... }
class _Private {}
```

content_copy

GOOD:

dart

```
f(String s) { ... }
```

content_copy

## Enable

[#](#enable)

 To enable the `library_private_types_in_public_api` rule, add `library_private_types_in_public_api` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - library_private_types_in_public_api
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `library_private_types_in_public_api: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    library_private_types_in_public_api: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/library_private_types_in_public_api).
