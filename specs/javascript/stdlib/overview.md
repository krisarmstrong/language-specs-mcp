# JavaScript reference

The JavaScript reference serves as a repository of facts about the JavaScript language. The entire language is described here in detail. As you write JavaScript code, you'll refer to these pages often (thus the title "JavaScript reference").

The JavaScript language is intended to be used within some larger environment, be it a browser, server-side scripts, or similar. For the most part, this reference attempts to be environment-agnostic and does not target a web browser environment.

If you are new to JavaScript, start with the [guide](/en-US/docs/Web/JavaScript/Guide). Once you have a firm grasp of the fundamentals, you can use the reference to get more details on individual objects and language constructs.

## In this article

- [Built-ins](#built-ins)
- [Statements](#statements)
- [Expressions and operators](#expressions_and_operators)
- [Functions](#functions)
- [Classes](#classes)
- [Regular expressions](#regular_expressions)
- [Additional reference pages](#additional_reference_pages)

## [Built-ins](#built-ins)

[JavaScript standard built-in objects](/en-US/docs/Web/JavaScript/Reference/Global_Objects), along with their methods and properties.

### [Value properties](#value_properties)

- [globalThis](/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
- [Infinity](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
- [NaN](/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
- [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)

### [Function properties](#function_properties)

- [eval()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
- [isFinite()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/isFinite)
- [isNaN()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
- [parseFloat()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)
- [parseInt()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
- [decodeURI()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
- [decodeURIComponent()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
- [encodeURI()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
- [encodeURIComponent()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
- [escape()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/escape)Deprecated
- [unescape()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/unescape)Deprecated

### [Fundamental objects](#fundamental_objects)

- [Object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- [Function](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
- [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
- [Symbol](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

### [Error objects](#error_objects)

- [Error](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [AggregateError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError)
- [EvalError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/EvalError)
- [RangeError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
- [ReferenceError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
- [SuppressedError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/SuppressedError)
- [SyntaxError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
- [TypeError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
- [URIError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
- [InternalError](/en-US/docs/Web/JavaScript/Reference/Global_Objects/InternalError)Non-standard

### [Numbers and dates](#numbers_and_dates)

- [Number](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
- [BigInt](/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
- [Math](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
- [Date](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
- [Temporal](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)

### [Text processing](#text_processing)

- [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [RegExp](/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)

### [Indexed collections](#indexed_collections)

- [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Int8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)
- [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
- [Uint8ClampedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)
- [Int16Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array)
- [Uint16Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array)
- [Int32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)
- [Uint32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array)
- [BigInt64Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)
- [BigUint64Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)
- [Float16Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float16Array)
- [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array)
- [Float64Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array)

### [Keyed collections](#keyed_collections)

- [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [Set](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [WeakMap](/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
- [WeakSet](/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)

### [Structured data](#structured_data)

- [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
- [SharedArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
- [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
- [Atomics](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)
- [JSON](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

### [Managing memory](#managing_memory)

- [WeakRef](/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)
- [FinalizationRegistry](/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)

### [Control abstraction objects](#control_abstraction_objects)

- [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
- [AsyncIterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)
- [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [GeneratorFunction](/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction)
- [AsyncGeneratorFunction](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction)
- [Generator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
- [AsyncGenerator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)
- [AsyncFunction](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction)
- [DisposableStack](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack)
- [AsyncDisposableStack](/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncDisposableStack)

### [Reflection](#reflection)

- [Reflect](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
- [Proxy](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

### [Internationalization](#internationalization)

- [Intl](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
- [Intl.Collator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
- [Intl.DateTimeFormat](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
- [Intl.DisplayNames](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)
- [Intl.DurationFormat](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat)
- [Intl.ListFormat](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat)
- [Intl.Locale](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
- [Intl.NumberFormat](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)
- [Intl.PluralRules](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)
- [Intl.RelativeTimeFormat](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)
- [Intl.Segmenter](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter)

## [Statements](#statements)

[JavaScript statements and declarations](/en-US/docs/Web/JavaScript/Reference/Statements)

### [Control flow](#control_flow)

- [return](/en-US/docs/Web/JavaScript/Reference/Statements/return)
- [break](/en-US/docs/Web/JavaScript/Reference/Statements/break)
- [continue](/en-US/docs/Web/JavaScript/Reference/Statements/continue)
- [throw](/en-US/docs/Web/JavaScript/Reference/Statements/throw)
- [if...else](/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
- [switch](/en-US/docs/Web/JavaScript/Reference/Statements/switch)
- [try...catch](/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)

### [Declaring variables](#declaring_variables)

- [var](/en-US/docs/Web/JavaScript/Reference/Statements/var)
- [let](/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [const](/en-US/docs/Web/JavaScript/Reference/Statements/const)
- [using](/en-US/docs/Web/JavaScript/Reference/Statements/using)
- [await using](/en-US/docs/Web/JavaScript/Reference/Statements/await_using)

### [Functions and classes](#functions_and_classes)

- [function](/en-US/docs/Web/JavaScript/Reference/Statements/function)
- [function*](/en-US/docs/Web/JavaScript/Reference/Statements/function*)
- [async function](/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [async function*](/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
- [class](/en-US/docs/Web/JavaScript/Reference/Statements/class)

### [Iterations](#iterations)

- [do...while](/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
- [for](/en-US/docs/Web/JavaScript/Reference/Statements/for)
- [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
- [for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
- [for await...of](/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
- [while](/en-US/docs/Web/JavaScript/Reference/Statements/while)

### [Others](#others)

- [Empty](/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
- [Block](/en-US/docs/Web/JavaScript/Reference/Statements/block)
- [Expression statement](/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
- [debugger](/en-US/docs/Web/JavaScript/Reference/Statements/debugger)
- [export](/en-US/docs/Web/JavaScript/Reference/Statements/export)
- [import](/en-US/docs/Web/JavaScript/Reference/Statements/import)
- [label](/en-US/docs/Web/JavaScript/Reference/Statements/label)
- [with](/en-US/docs/Web/JavaScript/Reference/Statements/with)Deprecated

## [Expressions and operators](#expressions_and_operators)

[JavaScript expressions and operators](/en-US/docs/Web/JavaScript/Reference/Operators).

### [Primary expressions](#primary_expressions)

- [this](/en-US/docs/Web/JavaScript/Reference/Operators/this)
- [Literals](/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#literals)
- [[]](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [{}](/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
- [function](/en-US/docs/Web/JavaScript/Reference/Operators/function)
- [class](/en-US/docs/Web/JavaScript/Reference/Operators/class)
- [function*](/en-US/docs/Web/JavaScript/Reference/Operators/function*)
- [async function](/en-US/docs/Web/JavaScript/Reference/Operators/async_function)
- [async function*](/en-US/docs/Web/JavaScript/Reference/Operators/async_function*)
- [/ab+c/i](/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
- [`string`](/en-US/docs/Web/JavaScript/Reference/Template_literals)
- [( )](/en-US/docs/Web/JavaScript/Reference/Operators/Grouping)

### [Left-hand-side expressions](#left-hand-side_expressions)

- [Property accessors](/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
- [?.](/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
- [new](/en-US/docs/Web/JavaScript/Reference/Operators/new)
- [new.target](/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
- [import.meta](/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)
- [super](/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [import()](/en-US/docs/Web/JavaScript/Reference/Operators/import)

### [Increment and decrement](#increment_and_decrement)

- [A++](/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
- [A--](/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
- [++A](/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
- [--A](/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)

### [Unary operators](#unary_operators)

- [delete](/en-US/docs/Web/JavaScript/Reference/Operators/delete)
- [void](/en-US/docs/Web/JavaScript/Reference/Operators/void)
- [typeof](/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- [+](/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
- [-](/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
- [~](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT)
- [!](/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)
- [await](/en-US/docs/Web/JavaScript/Reference/Operators/await)

### [Arithmetic operators](#arithmetic_operators)

- [**](/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
- [*](/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
- [/](/en-US/docs/Web/JavaScript/Reference/Operators/Division)
- [%](/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
- [+](/en-US/docs/Web/JavaScript/Reference/Operators/Addition) (Plus)
- [-](/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)

### [Relational operators](#relational_operators)

- [<](/en-US/docs/Web/JavaScript/Reference/Operators/Less_than) (Less than)
- [>](/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than) (Greater than)
- [<=](/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal)
- [>=](/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal)
- [instanceof](/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
- [in](/en-US/docs/Web/JavaScript/Reference/Operators/in)

### [Equality operators](#equality_operators)

- [==](/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
- [!=](/en-US/docs/Web/JavaScript/Reference/Operators/Inequality)
- [===](/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
- [!==](/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)

### [Bitwise shift operators](#bitwise_shift_operators)

- [<<](/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift)
- [>>](/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)
- [>>>](/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)

### [Binary bitwise operators](#binary_bitwise_operators)

- [&](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND)
- [|](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR)
- [^](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR)

### [Binary logical operators](#binary_logical_operators)

- [&&](/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)
- [||](/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR)
- [??](/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)

### [Conditional (ternary) operator](#conditional_ternary_operator)

- [(condition ? ifTrue : ifFalse)](/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)

### [Assignment operators](#assignment_operators)

- [=](/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
- [*=](/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication_assignment)
- [/=](/en-US/docs/Web/JavaScript/Reference/Operators/Division_assignment)
- [%=](/en-US/docs/Web/JavaScript/Reference/Operators/Remainder_assignment)
- [+=](/en-US/docs/Web/JavaScript/Reference/Operators/Addition_assignment)
- [-=](/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction_assignment)
- [<<=](/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift_assignment)
- [>>=](/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift_assignment)
- [>>>=](/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift_assignment)
- [&=](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND_assignment)
- [^=](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR_assignment)
- [|=](/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR_assignment)
- [**=](/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation_assignment)
- [&&=](/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND_assignment)
- [||=](/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR_assignment)
- [??=](/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment)
- [[a, b] = arr, { a, b } = obj](/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)

### [Yield operators](#yield_operators)

- [yield](/en-US/docs/Web/JavaScript/Reference/Operators/yield)
- [yield*](/en-US/docs/Web/JavaScript/Reference/Operators/yield*)

### [Spread syntax](#spread_syntax)

- [...obj](/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

### [Comma operator](#comma_operator)

- [,](/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)

## [Functions](#functions)

[JavaScript functions.](/en-US/docs/Web/JavaScript/Reference/Functions)

- [Arrow Functions](/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameters](/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [arguments](/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
- [Method definitions](/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
- [getter](/en-US/docs/Web/JavaScript/Reference/Functions/get)
- [setter](/en-US/docs/Web/JavaScript/Reference/Functions/set)

## [Classes](#classes)

[JavaScript classes.](/en-US/docs/Web/JavaScript/Reference/Classes)

- [constructor](/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
- [extends](/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Private elements](/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
- [Public class fields](/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
- [static](/en-US/docs/Web/JavaScript/Reference/Classes/static)
- [Static initialization blocks](/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)

## [Regular expressions](#regular_expressions)

[JavaScript regular expressions.](/en-US/docs/Web/JavaScript/Reference/Regular_expressions)

- [Backreference: \1, \2](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
- [Capturing group: (...)](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group)
- [Character class: [...], [^...]](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
- [Character class escape: \d, \D, \w, \W, \s, \S](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
- [Character escape: \n, \u{...}](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
- [Disjunction: |](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
- [Input boundary assertion: ^, $](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
- [Literal character: a, b](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
- [Lookahead assertion: (?=...), (?!...)](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
- [Lookbehind assertion: (?<=...), (?<!...)](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)
- [Modifier: (?ims-ims:...)](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier)
- [Named backreference: \k<name>](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_backreference)
- [Named capturing group: (?<name>...)](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
- [Non-capturing group: (?:...)](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
- [Quantifier: *, +, ?, {n}, {n,}, {n,m}](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
- [Unicode character class escape: \p{...}, \P{...}](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
- [Wildcard: .](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Wildcard)
- [Word boundary assertion: \b, \B](/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)

## [Additional reference pages](#additional_reference_pages)

- [JavaScript technologies overview](/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview)
- [Execution model](/en-US/docs/Web/JavaScript/Reference/Execution_model)
- [Lexical grammar](/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
- [Data types and data structures](/en-US/docs/Web/JavaScript/Guide/Data_structures)
- [Iteration protocols](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
- [Trailing commas](/en-US/docs/Web/JavaScript/Reference/Trailing_commas)
- [Errors](/en-US/docs/Web/JavaScript/Reference/Errors)
- [Strict mode](/en-US/docs/Web/JavaScript/Reference/Strict_mode)
- [Deprecated features](/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 29, 2025⁩ by [MDN contributors](/en-US/docs/Web/JavaScript/Reference/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb6a36de3428f4b42c7707c8f190a349db13bf531%0A*+Document+last+modified%3A+2025-07-29T03%3A29%3A14.000Z%0A%0A%3C%2Fdetails%3E)
