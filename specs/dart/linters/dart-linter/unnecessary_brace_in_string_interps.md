Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_brace_in_string_interps](/tools/linter-rules/unnecessary_brace_in_string_interps)

# unnecessary_brace_in_string_interps

Learn about the unnecessary_brace_in_string_interps linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_brace_in_string_interps)

verified_userStablethumb_upRecommendedbuildFix available

Avoid using braces in interpolation when not needed.

## Details

[#](#details)

AVOID using braces in interpolation when not needed.

 If you're just interpolating a simple identifier, and it's not immediately followed by more alphanumeric text, the `{}` can and should be omitted. 

BAD:

dart

```
print("Hi, ${name}!");
```

content_copy

GOOD:

dart

```
print("Hi, $name!");
```

content_copy

## Enable

[#](#enable)

 To enable the `unnecessary_brace_in_string_interps` rule, add `unnecessary_brace_in_string_interps` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_brace_in_string_interps
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_brace_in_string_interps: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_brace_in_string_interps: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_brace_in_string_interps).
