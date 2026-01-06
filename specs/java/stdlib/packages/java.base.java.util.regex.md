Module[java.base](../../../module-summary.html)

# Package java.util.regex

package java.util.regexClasses for matching character sequences against patterns specified by regular expressions. 

 An instance of the [Pattern](Pattern.html) class represents a regular expression that is specified in string form in a syntax similar to that used by Perl. 

 Instances of the [Matcher](Matcher.html) class are used to match character sequences against a given pattern. Input is provided to matchers via the [CharSequence](../../lang/CharSequence.html) interface in order to support matching against characters from a wide variety of input sources. 

 Unless otherwise noted, passing a `null` argument to a method in any class or interface in this package will cause a [NullPointerException](../../lang/NullPointerException.html) to be thrown. 

## Related Documentation

 An excellent tutorial and overview of regular expressions is [Mastering Regular
 Expressions, Jeffrey E. F. Friedl, O'Reilly and Associates,
 1997.](http://www.oreilly.com/catalog/regex/)

Since:1.4

- Related PackagesPackageDescription[java.util](../package-summary.html)Contains the collections framework, some internationalization support classes, a service loader, properties, random number generation, string parsing and scanning classes, base64 encoding and decoding, a bit array, and several miscellaneous utility classes.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[Matcher](Matcher.html)An engine that performs match operations on a [character sequence](../../lang/CharSequence.html) by interpreting a [Pattern](Pattern.html).[MatchResult](MatchResult.html)The result of a match operation.[Pattern](Pattern.html)A compiled representation of a regular expression.[PatternSyntaxException](PatternSyntaxException.html)Unchecked exception thrown to indicate a syntax error in a regular-expression pattern.
