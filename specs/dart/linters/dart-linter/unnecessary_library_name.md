Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_library_name](/tools/linter-rules/unnecessary_library_name)

# unnecessary_library_name

Learn about the unnecessary_library_name linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_library_name)

verified_userStablethumb_upRecommendedbuildFix available

Don't have a library name in a `library` declaration.

## Details

[#](#details)

DON'T have a library name in a `library` declaration.

Library names are not necessary.

 A library does not need a library declaration, but one can be added to attach library documentation and library metadata to. A declaration of `library;` is sufficient for those uses. 

 The only use of a library name is for a `part` file to refer back to its owning library, but part files should prefer to use a string URI to refer back to the library file, not a library name. 

 If a library name is added to a library declaration, it introduces the risk of name conflicts. It's a compile-time error if two libraries in the same program have the same library name. To avoid that, library names tend to be long, including the package name and path, just to avoid accidental name clashes. That makes such library names hard to read, and not even useful as documentation. 

BAD:

dart

```
/// This library has a long name.
library magnificator.src.helper.bananas;
```

content_copydart

```
library utils; // Not as verbose, but risks conflicts.
```

content_copy

GOOD:

dart

```
/// This library is awesome.
library;
​
part "apart.dart"; // contains: `part of "good_library.dart";`
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_library_name` rule, add `unnecessary_library_name` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_library_name
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_library_name: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_library_name: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_library_name).
