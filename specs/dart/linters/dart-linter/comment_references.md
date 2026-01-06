Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [comment_references](/tools/linter-rules/comment_references)

# comment_references

Learn about the comment_references linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/comment_references)

verified_userStablebuildFix available

Only reference in-scope identifiers in doc comments.

## Details

[#](#details)

DO reference only in-scope identifiers in doc comments.

 If you surround identifiers like variable, method, or type names in square brackets, then tools like your IDE and [dart doc](https://dart.dev/tools/dart-doc) can link to them. For this to work, ensure that all identifiers in docs wrapped in brackets are in scope. 

For example, assuming `outOfScopeId` is out of scope:

BAD:

dart

```
/// Returns whether [value] is larger than [outOfScopeId].
bool isOutOfRange(int value) { ... }
```

content_copy

GOOD:

dart

```
/// Returns the larger of [a] or [b].
int max_int(int a, int b) { ... }
```

content_copy

 Note that the square bracket comment format is designed to allow comments to refer to declarations using a fairly natural format but does not allow arbitrary expressions. In particular, code references within square brackets can consist of any of the following: 

-  A bare identifier which is in-scope for the comment (see the spec for what is "in-scope" in doc comments). Examples include `[print]` and `[Future]`. 
-  Two identifiers separated by a period (a "prefixed identifier"), such that the first identifier acts as a namespacing identifier, such as a class property name or method name prefixed by the containing class's name, or a top-level identifier prefixed by an import prefix. Examples include `[Future.new]` (an unnamed constructor), `[Future.value]` (a constructor), `[Future.wait]` (a static method), `[Future.then]` (an instance method), `[math.max]` (given that 'dart:async' is imported with a `max` prefix). 
-  A prefixed identifier followed by a pair of parentheses, used to disambiguate named constructors from instance members (whose names are allowed to collide). Examples include `[Future.value()]`. 
-  Three identifiers separated by two periods, such that the first identifier is an import prefix name, the second identifier is a top-level element like a class or an extension, and the third identifier is a member of that top-level element. Examples include `[async.Future.then]` (given that 'dart:async' is imported with an `async` prefix). 

Known limitations

 The `comment_references` lint rule aligns with the Dart analyzer's notion of comment references, which is occasionally distinct from Dartdoc's notion of comment references. The lint rule may report comment references which Dartdoc can resolve, even though the analyzer cannot. See [sdk#57783](https://github.com/dart-lang/sdk/issues/57783) for more information. 

## Enable

[#](#enable)

 To enable the `comment_references` rule, add `comment_references` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - comment_references
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `comment_references: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    comment_references: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/comment_references).
