Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unnecessary_parenthesis](/tools/linter-rules/unnecessary_parenthesis)

# unnecessary_parenthesis

Learn about the unnecessary_parenthesis linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_parenthesis)

verified_userStablebuildFix available

Unnecessary parentheses can be removed.

## Details

[#](#details)

AVOID using parentheses when not needed.

BAD:

dart

```
a = (b);
```

content_copy

GOOD:

dart

```
a = b;
```

content_copy

 Parentheses are considered unnecessary if they do not change the meaning of the code and they do not improve the readability of the code. The goal is not to force all developers to maintain the expression precedence table in their heads, which is why the second condition is included. Examples of this condition include: 

-  cascade expressions - it is sometimes not clear what the target of a cascade expression is, especially with assignments, or nested cascades. For example, the expression `a.b = (c..d)`. 
-  expressions with whitespace between tokens - it can look very strange to see an expression like `!await foo` which is valid and equivalent to `!(await foo)`. 
-  logical expressions - parentheses can improve the readability of the implicit grouping defined by precedence. For example, the expression `(a && b) || c && d`. 

## Enable

[#](#enable)

 To enable the `unnecessary_parenthesis` rule, add `unnecessary_parenthesis` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unnecessary_parenthesis
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unnecessary_parenthesis: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unnecessary_parenthesis: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unnecessary_parenthesis).
