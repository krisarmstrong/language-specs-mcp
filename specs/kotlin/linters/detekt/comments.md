Comments Rule Set | detekt[Skip to main content](#__docusaurus_skipToContent_fallback)[detekt](/)[Docs](/docs/intro)[Blog](/blog)[APIs](https://detekt.dev/kdoc/)[Marketplace](/marketplace)[2.0.0-alpha.1](/docs/rules/comments)

- [Next](/docs/next/rules/comments)
- [2.0.0-alpha.1](/docs/rules/comments)
- [2.0.0-alpha.0](/docs/2.0.0-alpha.0/rules/comments)
- [1.23.8](/docs/1.23.8/rules/comments)
- [1.23.7](/docs/1.23.7/rules/comments)
- [1.23.6](/docs/1.23.6/rules/comments)
- [1.23.5](/docs/1.23.5/rules/comments)
- [1.23.4](/docs/1.23.4/rules/comments)
- [1.23.3](/docs/1.23.3/rules/comments)
- [1.23.1](/docs/1.23.1/rules/comments)
- [1.23.0](/docs/1.23.0/rules/comments)
- [1.22.0](/docs/1.22.0/rules/comments)
- [1.21.0](/docs/1.21.0/rules/comments)
- [All changelogs](/changelog)

[GitHub](https://github.com/detekt/detekt)Search

- [Welcome](/docs/intro)
- [Introduction](/docs/introduction/configurations)
- [Getting Started](/docs/gettingstarted/cli)
- [Rules Documentation](/docs/rules/comments)

  - [Comments Rule Set](/docs/rules/comments)
  - [Complexity Rule Set](/docs/rules/complexity)
  - [Coroutines Rule Set](/docs/rules/coroutines)
  - [Empty-blocks Rule Set](/docs/rules/empty-blocks)
  - [Exceptions Rule Set](/docs/rules/exceptions)
  - [Formatting Rule Set](/docs/rules/formatting)
  - [Ktlint Rule Set](/docs/rules/ktlint)
  - [Libraries Rule Set](/docs/rules/libraries)
  - [Naming Rule Set](/docs/rules/naming)
  - [Performance Rule Set](/docs/rules/performance)
  - [Potential-bugs Rule Set](/docs/rules/potential-bugs)
  - [Ruleauthors Rule Set](/docs/rules/ruleauthors)
  - [Style Rule Set](/docs/rules/style)

- [Changelogs](/changelog-2.0.0)

- /
- Rules Documentation
- Comments Rule Set

Version: 2.0.0-alpha.1On this page

# Comments Rule Set

This rule set provides rules that address issues in comments and documentation of the code.

### AbsentOrWrongFileLicense[​](#absentorwrongfilelicense)

This rule will report every Kotlin source file which doesn't have the required license header. The rule validates each Kotlin source and operates in two modes: if `licenseTemplateIsRegex = false` (or missing) the rule checks whether the input file header starts with the read text from the passed file in the `licenseTemplateFile` configuration option. If `licenseTemplateIsRegex = true` the rule matches the header with a regular expression produced from the passed template license file (defined via `licenseTemplateFile` configuration option).

Active by default: No

#### Configuration options:[​](#configuration-options)

- 

`licenseTemplateFile` (default: `'license.template'`)

path to file with license header template resolved relatively to config file

- 

`licenseTemplateIsRegex` (default: `false`)

whether or not the license header template is a regex template

### CommentOverPrivateFunction[​](#commentoverprivatefunction)

This rule reports comments and documentation that has been added to private functions. These comments get reported because they probably explain the functionality of the private function. However, private functions should be small enough and have an understandable name so that they are self-explanatory and do not need this comment in the first place.

Instead of simply removing this comment to solve this issue prefer to split up the function into smaller functions with better names if necessary. Giving the function a better, more descriptive name can also help in solving this issue.

Active by default: No

### CommentOverPrivateProperty[​](#commentoverprivateproperty)

This rule reports comments and documentation above private properties. This can indicate that the property has a confusing name or is not in a small enough context to be understood. Private properties should be named in a self-explanatory way and readers of the code should be able to understand why the property exists and what purpose it solves without the comment.

Instead of simply removing the comment to solve this issue, prefer renaming the property to a more self-explanatory name. If this property is inside a bigger class, it makes sense to refactor and split up the class. This can increase readability and make the documentation obsolete.

Active by default: No

### DeprecatedBlockTag[​](#deprecatedblocktag)

This rule reports use of the `@deprecated` block tag in KDoc comments. Deprecation must be specified using a `@Deprecated` annotation as adding a `@deprecated` block tag in KDoc comments [has no effect and is not supported](https://kotlinlang.org/docs/kotlin-doc.html#suppress). The `@Deprecated` annotation constructor has dedicated fields for a message and a type (warning, error, etc.). You can also use the `@ReplaceWith` annotation to specify how to solve the deprecation automatically via the IDE.

Active by default: No

#### Noncompliant Code:[​](#noncompliant-code)

```
/**
* This function prints a message followed by a new line.
*
* @deprecated Useless, the Kotlin standard library can already do this. Replace with println.
*/
fun printThenNewline(what: String) {
    // ...
}
```

#### Compliant Code:[​](#compliant-code)

```
/**
* This function prints a message followed by a new line.
*/
@Deprecated("Useless, the Kotlin standard library can already do this.")
@ReplaceWith("println(what)")
fun printThenNewline(what: String) {
    // ...
}
```

### EndOfSentenceFormat[​](#endofsentenceformat)

This rule validates the end of the first sentence of a KDoc comment. It should end with proper punctuation or with a correct URL.

Active by default: No

#### Configuration options:[​](#configuration-options-1)

- 

`endOfSentenceFormat` (default: `'([.?!][ \t\n\r\f<])|([.?!:]$)'`)

regular expression which should match the end of the first sentence in the KDoc

### KDocReferencesNonPublicProperty[​](#kdocreferencesnonpublicproperty)

This rule will report any KDoc comments that refer to non-public properties of a class. Clients do not need to know the implementation details.

Active by default: No

#### Noncompliant Code:[​](#noncompliant-code-1)

```
/**
* Comment
* [prop1] - non-public property
* [prop2] - public property
*/
class Test {
    private val prop1 = 0
    val prop2 = 0
}
```

#### Compliant Code:[​](#compliant-code-1)

```
/**
* Comment
* [prop2] - public property
*/
class Test {
    private val prop1 = 0
    val prop2 = 0
}
```

### OutdatedDocumentation[​](#outdateddocumentation)

This rule will report any class, function or constructor with KDoc that does not match the declaration signature. If KDoc is not present or does not contain any @param or @property tags, rule violation will not be reported. By default, both type and value parameters need to be matched and declarations orders must be preserved. You can turn off these features using configuration options.

Active by default: No

#### Configuration options:[​](#configuration-options-2)

- 

`matchTypeParameters` (default: `true`)

if type parameters should be matched

- 

`matchDeclarationsOrder` (default: `true`)

if the order of declarations should be preserved

- 

`allowParamOnConstructorProperties` (default: `false`)

if we allow constructor parameters to be marked as @param instead of @property

#### Noncompliant Code:[​](#noncompliant-code-2)

```
/**
* @param someParam
* @property someProp
*/
class MyClass(otherParam: String, val otherProp: String)

/**
* @param T
* @param someParam
*/
fun <T, S> myFun(someParam: String)
```

#### Compliant Code:[​](#compliant-code-2)

```
/**
* @param someParam
* @property someProp
*/
class MyClass(someParam: String, val someProp: String)

/**
* @param T
* @param S
* @param someParam
*/
fun <T, S> myFun(someParam: String)
```

### UndocumentedPublicClass[​](#undocumentedpublicclass)

This rule reports public classes, objects and interfaces which do not have the required documentation. Enable this rule if the codebase should have documentation on every public class, interface and object.

By default, this rule also searches for nested and inner classes and objects. This default behavior can be changed with the configuration options of this rule.

Active by default: No

#### Configuration options:[​](#configuration-options-3)

- 

`searchInNestedClass` (default: `true`)

if nested classes should be searched

- 

`searchInInnerClass` (default: `true`)

if inner classes should be searched

- 

`searchInInnerObject` (default: `true`)

if inner objects should be searched

- 

`searchInInnerInterface` (default: `true`)

if inner interfaces should be searched

- 

`searchInProtectedClass` (default: `false`)

if protected classes should be searched

- 

`ignoreDefaultCompanionObject` (default: `false`)

whether default companion objects should be exempted

### UndocumentedPublicFunction[​](#undocumentedpublicfunction)

This rule will report any public function which does not have the required documentation. If the codebase should have documentation on all public functions enable this rule to enforce this. Overridden functions are excluded by this rule.

Active by default: No

#### Configuration options:[​](#configuration-options-4)

- 

`searchProtectedFunction` (default: `false`)

if protected functions should be searched

### UndocumentedPublicProperty[​](#undocumentedpublicproperty)

This rule will report any public property which does not have the required documentation. This also includes public properties defined in a primary constructor. If the codebase should have documentation on all public properties enable this rule to enforce this. Overridden properties are excluded by this rule.

Active by default: No

#### Configuration options:[​](#configuration-options-5)

- 

`searchProtectedProperty` (default: `false`)

if protected functions should be searched

- 

`ignoreEnumEntries` (default: `false`)

ignores a enum entries when set to true

[Edit this page](https://github.com/detekt/detekt/edit/main/website/versioned_docs/version-2.0.0-alpha.1/rules/comments.md)[PreviousRun detekt using the Compiler Plugin](/docs/gettingstarted/compilerplugin)[NextComplexity Rule Set](/docs/rules/complexity)

- [AbsentOrWrongFileLicense](#absentorwrongfilelicense)
- [CommentOverPrivateFunction](#commentoverprivatefunction)
- [CommentOverPrivateProperty](#commentoverprivateproperty)
- [DeprecatedBlockTag](#deprecatedblocktag)
- [EndOfSentenceFormat](#endofsentenceformat)
- [KDocReferencesNonPublicProperty](#kdocreferencesnonpublicproperty)
- [OutdatedDocumentation](#outdateddocumentation)
- [UndocumentedPublicClass](#undocumentedpublicclass)
- [UndocumentedPublicFunction](#undocumentedpublicfunction)
- [UndocumentedPublicProperty](#undocumentedpublicproperty)

Docs

- [Getting Started with Gradle](/docs/gettingstarted/gradle)
- [Getting Started with the CLI](/docs/gettingstarted/cli)
- [Rules Documentation](/docs/rules/comments)

Community

- [Slack](https://kotlinlang.slack.com/archives/C88E12QH4)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/detekt)

More

- [Blog](/blog)
- [GitHub](https://github.com/detekt/detekt)
- [KDoc](https://detekt.dev/kdoc)

Copyright © 2026 detekt team - Built with Docusaurus.
