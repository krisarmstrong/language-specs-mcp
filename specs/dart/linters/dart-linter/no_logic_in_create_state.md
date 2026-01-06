Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_logic_in_create_state](/tools/linter-rules/no_logic_in_create_state)

# no_logic_in_create_state

Learn about the no_logic_in_create_state linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_logic_in_create_state)

verified_userStableflutterFlutter

Don't put any logic in createState.

## Details

[#](#details)

DON'T put any logic in `createState()`.

 Implementations of `createState()` should return a new instance of a State object and do nothing more. Since state access is preferred via the `widget` field, passing data to `State` objects using custom constructor parameters should also be avoided and so further, the State constructor is required to be passed no arguments. 

BAD:

dart

```
MyState global;
​
class MyStateful extends StatefulWidget {
  @override
  MyState createState() {
    global = MyState();
    return global;
  }
}
```

content_copydart

```
class MyStateful extends StatefulWidget {
  @override
  MyState createState() => MyState()..field = 42;
}
```

content_copydart

```
class MyStateful extends StatefulWidget {
  @override
  MyState createState() => MyState(42);
}
```

content_copy

GOOD:

dart

```
class MyStateful extends StatefulWidget {
  @override
  MyState createState() {
    return MyState();
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `no_logic_in_create_state` rule, add `no_logic_in_create_state` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_logic_in_create_state
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_logic_in_create_state: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_logic_in_create_state: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_logic_in_create_state).
