Dart 3.10 is taking off with dot shorthands, stable build hooks, nuanced deprecation annotations, and more! [Learn more](https://blog.dart.dev/announcing-dart-3-10-ea8b952b6088)

1. [Tools](/tools)chevron_right
2. [Linter rules](/tools/linter-rules)chevron_right
3. [unsafe_variance](/tools/linter-rules/unsafe_variance)

# unsafe_variance

Learn about the unsafe_variance linter rule.

more_vert

- copyCopy link
- [bug_reportReport issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unsafe_variance)

scienceExperimental

Unsafe type: Has a type variable in a non-covariant position.

## Details

[#](#details)

 An instance variable whose type contains a type parameter of the enclosing class, mixin, or enum in a non-covariant position is likely to cause run-time failures due to failing type checks. For example, in `class C<X> {...}`, an instance variable of the form `void Function(X) myVariable;` may cause this kind of run-time failure. 

 The same is true for a getter or method whose return type has a non-covariant occurrence of a type parameter of the enclosing declaration. 

This lint flags this kind of member declaration.

BAD:

dart

```
class C<X> {
  final bool Function(X) fun; // LINT
  C(this.fun);
}
​
void main() {
  C<num> c = C<int>((i) => i.isEven);
  c.fun(10); // Throws.
}
```

content_copy

 The problem is that `X` occurs as a parameter type in the type of `fun`. 

 One way to reduce the potential for run-time type errors is to ensure that the non-covariant member `fun` is only used on `this`. We cannot strictly enforce this, but we can make it private and add a forwarding method `fun` such that we can check locally in the same library that this constraint is satisfied: 

BETTER:

dart

```
class C<X> {
  // ignore: unsafe_variance
  final bool Function(X) _fun;
  bool fun(X x) => _fun(x);
  C(this._fun);
}
​
void main() {
  C<num> c = C<int>((i) => i.isEven);
  c.fun(10); // Succeeds.
}
```

content_copy

 A fully safe approach requires a feature that Dart does not yet have, namely statically checked variance. With that, we could specify that the type parameter `X` is invariant (`inout X`). 

 It is possible to emulate invariance without support for statically checked variance. This puts some restrictions on the creation of subtypes, but faithfully provides the typing that `inout` would give: 

GOOD:

dart

```
typedef Inv<X> = X Function(X);
typedef C<X> = _C<X, Inv<X>>;
​
class _C<X, Invariance extends Inv<X>> {
  // ignore: unsafe_variance
  final bool Function(X) fun; // Safe!
  _C(this.fun);
}
​
void main() {
  C<int> c = C<int>((i) => i.isEven);
  c.fun(10); // Succeeds.
}
```

content_copy

 With this approach, `C<int>` is not a subtype of `C<num>`, so `c` must have a different declared type. 

 Another possibility is to declare the variable to have a safe but more general type. It is then safe to use the variable itself, but every invocation will have to be checked at run time: 

HONEST:

dart

```
class C<X> {
  final bool Function(Never) fun;
  C(this.fun);
}
​
void main() {
  C<num> c = C<int>((int i) => i.isEven);
  var cfun = c.fun; // Local variable, enables promotion.
  if (cfun is bool Function(int)) cfun(10); // Succeeds.
  if (cfun is bool Function(bool)) cfun(true); // Not called.
}
```

content_copy

## Enable

[#](#enable)

 To enable the `unsafe_variance` rule, add `unsafe_variance` under linter > rules in your [analysis_options.yaml](/tools/analysis) file: 

analysis_options.yamlyaml

```
linter:
  rules:
    - unsafe_variance
```

content_copy

 If you're instead using the YAML map syntax to configure linter rules, add `unsafe_variance: true` under linter > rules: 

analysis_options.yamlyaml

```
linter:
  rules:
    unsafe_variance: true
```

content_copyWas this page's content helpful?thumb_upthumb_down

Unless stated otherwise, the documentation on this site reflects Dart 3.10.3. [Report an issue](https://github.com/dart-lang/site-www/issues/new?template=1_page_issue.yml&page-url=https://dart.dev/tools/linter-rules/unsafe_variance).
