Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [no_self_assignments](/tools/linter-rules/no_self_assignments)

# no_self_assignments

Learn about the no_self_assignments linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_self_assignments)

verified_userStable

Don't assign a variable to itself.

## Details

[#](#details)

DON'T assign a variable to itself. Usually this is a mistake.

BAD:

dart

```
class C {
  int x;
​
  C(int x) {
    x = x;
  }
}
```

content_copy

GOOD:

dart

```
class C {
  int x;
​
  C(int x) : x = x;
}
```

content_copy

GOOD:

dart

```
class C {
  int x;
​
  C(int x) {
    this.x = x;
  }
}
```

content_copy

BAD:

dart

```
class C {
  int _x = 5;
​
  int get x => _x;
​
  set x(int x) {
    _x = x;
    _customUpdateLogic();
  }
​
  void _customUpdateLogic() {
    print('updated');
  }
​
  void example() {
    x = x;
  }
}
```

content_copy

GOOD:

dart

```
class C {
  int _x = 5;
​
  int get x => _x;
​
  set x(int x) {
    _x = x;
    _customUpdateLogic();
  }
​
  void _customUpdateLogic() {
    print('updated');
  }
​
  void example() {
    _customUpdateLogic();
  }
}
```

content_copy

BAD:

dart

```
class C {
  int x = 5;
​
  void update(C other) {
    this.x = this.x;
  }
}
```

content_copy

GOOD:

dart

```
class C {
  int x = 5;
​
  void update(C other) {
    this.x = other.x;
  }
}
```

content_copy

## Enable

[#](#enable)

 To enable the `no_self_assignments` rule, add `no_self_assignments` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - no_self_assignments
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `no_self_assignments: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    no_self_assignments: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/no_self_assignments).
