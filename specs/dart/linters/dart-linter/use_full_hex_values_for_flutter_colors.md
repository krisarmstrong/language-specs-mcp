Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_full_hex_values_for_flutter_colors](/tools/linter-rules/use_full_hex_values_for_flutter_colors)

# use_full_hex_values_for_flutter_colors

Learn about the use_full_hex_values_for_flutter_colors linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_full_hex_values_for_flutter_colors)

verified_userStableflutterFlutterbuildFix available

Prefer an 8-digit hexadecimal integer (for example, 0xFFFFFFFF) to instantiate a Color.

## Details

[#](#details)

PREFER an 8-digit hexadecimal integer (for example, 0xFFFFFFFF) to instantiate a Color. Colors have four 8-bit channels, which adds up to 32 bits, so Colors are described using a 32-bit integer. 

BAD:

dart

```
Color(1);
Color(0x000001);
```

content_copy

GOOD:

dart

```
Color(0x00000001);
```

content_copy

## Enable

[#](#enable)

 To enable the `use_full_hex_values_for_flutter_colors` rule, add `use_full_hex_values_for_flutter_colors` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_full_hex_values_for_flutter_colors
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_full_hex_values_for_flutter_colors: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_full_hex_values_for_flutter_colors: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_full_hex_values_for_flutter_colors).
