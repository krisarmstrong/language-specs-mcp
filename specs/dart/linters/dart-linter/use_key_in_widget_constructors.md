Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [use_key_in_widget_constructors](/tools/linter-rules/use_key_in_widget_constructors)

# use_key_in_widget_constructors

Learn about the use_key_in_widget_constructors linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_key_in_widget_constructors)

verified_userStableflutterFlutterbuildFix available

Use key in widget constructors.

## Details

[#](#details)

DO use key in widget constructors.

 It's a good practice to expose the ability to provide a key when creating public widgets. 

BAD:

dart

```
class MyPublicWidget extends StatelessWidget {
}
```

content_copy

GOOD:

dart

```
class MyPublicWidget extends StatelessWidget {
  MyPublicWidget({super.key});
}
```

content_copy

## Enable

[#](#enable)

 To enable the `use_key_in_widget_constructors` rule, add `use_key_in_widget_constructors` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - use_key_in_widget_constructors
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `use_key_in_widget_constructors: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    use_key_in_widget_constructors: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/use_key_in_widget_constructors).
