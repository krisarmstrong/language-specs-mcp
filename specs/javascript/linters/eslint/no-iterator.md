# no-iterator

Disallow the use of the `__iterator__` property

## Table of Contents

1. [Rule Details](#rule-details)
2. [Version](#version)
3. [Further Reading](#further-reading)
4. [Resources](#resources)

The `__iterator__` property was a SpiderMonkey extension to JavaScript that could be used to create custom iterators that are compatible with JavaScript’s `for in` and `for each` constructs. However, this property is now obsolete, so it should not be used. Here’s an example of how this used to work:

```
Foo.prototype.__iterator__ = function() {
    return new FooIterator(this);
}
1
2
3
```

Copy code to clipboard

You should use ECMAScript 6 iterators and generators instead.

## Rule Details

This rule is aimed at preventing errors that may arise from using the `__iterator__` property, which is not implemented in several browsers. As such, it will warn whenever it encounters the `__iterator__` property.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXRlcmF0b3I6IFwiZXJyb3JcIiovXG5cbkZvby5wcm90b3R5cGUuX19pdGVyYXRvcl9fID0gZnVuY3Rpb24oKSB7XG4gICAgcmV0dXJuIG5ldyBGb29JdGVyYXRvcih0aGlzKTtcbn07XG5cbmZvby5fX2l0ZXJhdG9yX18gPSBmdW5jdGlvbiAoKSB7fTtcblxuZm9vW1wiX19pdGVyYXRvcl9fXCJdID0gZnVuY3Rpb24gKCkge307XG4ifQ==)

```
/*eslint no-iterator: "error"*/

Foo.prototype.__iterator__ = function() {
    return new FooIterator(this);
};

foo.__iterator__ = function () {};

foo["__iterator__"] = function () {};

1
2
3
4
5
6
7
8
9
10
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taXRlcmF0b3I6IFwiZXJyb3JcIiovXG5cbmNvbnN0IF9faXRlcmF0b3JfXyA9IGZvbzsgLy8gTm90IHVzaW5nIHRoZSBgX19pdGVyYXRvcl9fYCBwcm9wZXJ0eS4ifQ==)

```
/*eslint no-iterator: "error"*/

const __iterator__ = foo; // Not using the `__iterator__` property.
1
2
3
```

## Version

This rule was introduced in ESLint v0.0.9.

## Further Reading

[Iterators and generators - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators)
 developer.mozilla.org[null](https://kangax.github.io/es5-compat-table/es6/#Iterators)
 kangax.github.io[Deprecated and obsolete features - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#Object_methods)
 developer.mozilla.org

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-iterator.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-iterator.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-iterator.md
                    
                
                )
