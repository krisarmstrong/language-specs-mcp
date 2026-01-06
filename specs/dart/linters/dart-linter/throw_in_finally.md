Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [throw_in_finally](/tools/linter-rules/throw_in_finally)

# throw_in_finally

Learn about the throw_in_finally linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/throw_in_finally)

verified_userStable

Avoid `throw` in `finally` block.

## Details

[#](#details)

AVOID throwing exceptions in `finally` blocks.

 Throwing exceptions in `finally` blocks will inevitably cause unexpected behavior that is hard to debug. 

BAD:

dart

```
class BadThrow {
  double nonCompliantMethod() {
    try {
      print('hello world! ${1 / 0}');
    } catch (e) {
      print(e);
    } finally {
      throw 'Find the hidden error :P'; // LINT
    }
  }
}
```

content_copy

GOOD:

dart

```
class Ok {
  double compliantMethod() {
    var i = 5;
    try {
      i = 1 / 0;
    } catch (e) {
      print(e); // OK
    }
    return i;
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `throw_in_finally` rule, add `throw_in_finally` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - throw_in_finally
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `throw_in_finally: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    throw_in_finally: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/throw_in_finally).
