Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [sort_child_properties_last](/tools/linter-rules/sort_child_properties_last)

# sort_child_properties_last

Learn about the sort_child_properties_last linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sort_child_properties_last)

verified_userStableflutterFlutterbuildFix available

Sort child properties last in widget instance creations.

## Details

[#](#details)

 Sort child properties last in widget instance creations. This improves readability and plays nicest with UI as Code visualization in IDEs with UI as Code Guides in editors (such as IntelliJ) where Properties in the correct order appear clearly associated with the constructor call and separated from the children. 

BAD:

dart

```
return Scaffold(
  appBar: AppBar(
    title: Text(widget.title),
  ),
  body: Center(
    child: Column(
      children: <Widget>[
        Text(
          'You have pushed the button this many times:',
         ),
        Text(
          '$_counter',
          style: Theme.of(context).textTheme.display1,
         ),
      ],
      mainAxisAlignment: MainAxisAlignment.center,
    ),
    widthFactor: 0.5,
  ),
  floatingActionButton: FloatingActionButton(
    child: Icon(Icons.add),
    onPressed: _incrementCounter,
    tooltip: 'Increment',
  ),
);
```

content_copy

GOOD:

dart

```
return Scaffold(
  appBar: AppBar(
    title: Text(widget.title),
  ),
  body: Center(
    widthFactor: 0.5,
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(
          'You have pushed the button this many times:',
         ),
        Text(
          '$_counter',
          style: Theme.of(context).textTheme.display1,
         ),
      ],
    ),
  ),
  floatingActionButton: FloatingActionButton(
    onPressed: _incrementCounter,
    tooltip: 'Increment',
    child: Icon(Icons.add),
  ),
);
```

content_copy

 Exception: It's allowed to have parameter with a function expression after the `child` property. 

## Enable

[#](#enable)

 To enable the `sort_child_properties_last` rule, add `sort_child_properties_last` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - sort_child_properties_last
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `sort_child_properties_last: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    sort_child_properties_last: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/sort_child_properties_last).
