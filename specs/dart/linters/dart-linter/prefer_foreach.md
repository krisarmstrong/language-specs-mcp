Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [prefer_foreach](/tools/linter-rules/prefer_foreach)

# prefer_foreach

Learn about the prefer_foreach linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_foreach)

verified_userStablebuildFix available

Use `forEach` to only apply a function to all the elements.

## Details

[#](#details)

DO use `forEach` if you are only going to apply a function or a method to all the elements of an iterable. 

 Using `forEach` when you are only going to apply a function or method to all elements of an iterable is a good practice because it makes your code more terse. 

BAD:

dart

```
for (final key in map.keys.toList()) {
  map.remove(key);
}
```

content_copy

GOOD:

dart

```
map.keys.toList().forEach(map.remove);
```

content_copy

NOTE: Replacing a for each statement with a forEach call may change the behavior in the case where there are side-effects on the iterable itself. 

dart

```
for (final v in myList) {
  foo().f(v); // This code invokes foo() many times.
}
​
myList.forEach(foo().f); // But this one invokes foo() just once.
```

content_copy

## Enable

[#](#enable)

 To enable the `prefer_foreach` rule, add `prefer_foreach` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - prefer_foreach
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `prefer_foreach: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    prefer_foreach: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/prefer_foreach).
