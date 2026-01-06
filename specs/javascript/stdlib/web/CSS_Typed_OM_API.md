# CSS Typed Object Model API

The CSS Typed Object Model API simplifies CSS property manipulation by exposing CSS values as typed JavaScript objects rather than strings. This not only simplifies CSS manipulation, but also lessens the negative impact on performance as compared to [HTMLElement.style](/en-US/docs/Web/API/HTMLElement/style).

Generally, CSS values can be read and written in JavaScript as strings, which can be slow and cumbersome. CSS Typed Object Model API provides interfaces to interact with underlying values, by representing them with specialized JS objects that can be manipulated and understood more easily and more reliably than string parsing and concatenation. This is easier for authors (for example, numeric values are reflected with actual JS numbers, and have unit-aware mathematical operations defined for them). It is also generally faster, as values can be directly manipulated and then cheaply translated back into underlying values without having to both build and parse strings of CSS.

CSS Typed OM both allows for the performant manipulation of values assigned to CSS properties while enabling maintainable code that is both more understandable and easier to write.

## In this article

- [Interfaces](#interfaces)
- [CSSStyleValue Interfaces](#cssstylevalue_interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

### [CSSStyleValue](#cssstylevalue)

The [CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue) interface of the CSS Typed Object Model API is the base class of all CSS values accessible through the Typed OM API. An instance of this class may be used anywhere a string is expected.

[CSSStyleValue.parse()](/en-US/docs/Web/API/CSSStyleValue/parse_static)

Method that allows `CSSNumericValue` to be constructed from a CSS string. It sets a specific CSS property to the specified values and returns the first value as a `CSSStyleValue` object.

[CSSStyleValue.parseAll()](/en-US/docs/Web/API/CSSStyleValue/parseAll_static)

Method that sets all occurrences of a specific CSS property to the specified value and returns an array of `CSSStyleValue` objects, each containing one of the supplied values.

### [StylePropertyMap](#stylepropertymap)

The [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap) interface of the CSS Typed Object Model API provides a representation of a CSS declaration block that is an alternative to `CSSStyleDeclaration`.

[StylePropertyMap.set()](/en-US/docs/Web/API/StylePropertyMap/set)

Method that changes the CSS declaration with the given property to the value given.

[StylePropertyMap.append()](/en-US/docs/Web/API/StylePropertyMap/append)

Method that adds a new CSS declaration to the `StylePropertyMap` with the given property and value.

[StylePropertyMap.delete()](/en-US/docs/Web/API/StylePropertyMap/delete)

Method that removes the CSS declaration with the given property from the `StylePropertyMap`.

[StylePropertyMap.clear()](/en-US/docs/Web/API/StylePropertyMap/clear)

Method that removes all declarations in the `StylePropertyMap`.

### [CSSUnparsedValue](#cssunparsedvalue)

The [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue) interface of the CSS Typed Object Model API represents property values that reference custom properties. It consists of a list of string fragments and variable references.

[CSSUnparsedValue()](/en-US/docs/Web/API/CSSUnparsedValue/CSSUnparsedValue) constructor

Creates a new `CSSUnparsedValue` object which represents property values that reference custom properties.

[CSSUnparsedValue.entries()](/en-US/docs/Web/API/CSSUnparsedValue/entries)

Method returning an array of a given object's own enumerable property `[key, value]` pairs in the same order as that provided by a `for...in` loop (the difference being that a for-in loop enumerates properties in the prototype chain as well).

[CSSUnparsedValue.forEach()](/en-US/docs/Web/API/CSSUnparsedValue/forEach)

Method executing a provided function once for each element of the `CSSUnparsedValue`.

[CSSUnparsedValue.keys()](/en-US/docs/Web/API/CSSUnparsedValue/keys)

Method returning a new array iterator object that contains the keys for each index in the array.

### [CSSKeywordValue Serialization](#csskeywordvalue_serialization)

The [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue) interface of the CSS Typed Object Model API creates an object to represent CSS keywords and other identifiers.

[CSSKeywordValue()](/en-US/docs/Web/API/CSSKeywordValue/CSSKeywordValue) constructor

Constructor creates a new [CSSKeywordValue()](/en-US/docs/Web/API/CSSKeywordValue/CSSKeywordValue) object which represents CSS keywords and other identifiers.

[CSSKeywordValue.value()](/en-US/docs/Web/API/CSSKeywordValue/value)

Property of the `CSSKeywordValue` interface returning or setting the value of the `CSSKeywordValue`.

## [CSSStyleValue Interfaces](#cssstylevalue_interfaces)

[CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue) is the base class through which all CSS values are expressed. Subclasses include:

[CSSImageValue](/en-US/docs/Web/API/CSSImageValue)

An interface representing values for properties that take an image, for example [background-image](/en-US/docs/Web/CSS/Reference/Properties/background-image), [list-style-image](/en-US/docs/Web/CSS/Reference/Properties/list-style-image), or [border-image-source](/en-US/docs/Web/CSS/Reference/Properties/border-image-source).

[CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)

An interface which creates an object to represent CSS keywords and other identifiers. When used where a string is expected, it will return the value of `CSSKeyword.value`.

[CSSMathValue](/en-US/docs/Web/API/CSSMathValue)

A tree of subclasses representing numeric values that are more complicated than a single value and unit, including:

- [CSSMathInvert](/en-US/docs/Web/API/CSSMathInvert) - represents a CSS [calc()](/en-US/docs/Web/CSS/Reference/Values/calc) value used as `calc(1 / <value>)`.
- [CSSMathMax](/en-US/docs/Web/API/CSSMathMax) - represents the CSS [max()](/en-US/docs/Web/CSS/Reference/Values/max) function.
- [CSSMathMin](/en-US/docs/Web/API/CSSMathMin) - represents the CSS [min()](/en-US/docs/Web/CSS/Reference/Values/min) function.
- [CSSMathNegate](/en-US/docs/Web/API/CSSMathNegate) - negates the value passed into it.
- [CSSMathProduct](/en-US/docs/Web/API/CSSMathProduct) - represents the result obtained by calling [add()](/en-US/docs/Web/API/CSSNumericValue/add), [sub()](/en-US/docs/Web/API/CSSNumericValue/sub), or [toSum()](/en-US/docs/Web/API/CSSNumericValue/toSum) on [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).
- [CSSMathSum](/en-US/docs/Web/API/CSSMathSum) - represents the result obtained by calling [add()](/en-US/docs/Web/API/CSSNumericValue/add), [sub()](/en-US/docs/Web/API/CSSNumericValue/sub), or [toSum()](/en-US/docs/Web/API/CSSNumericValue/toSum) on [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue).

[CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)

An interface representing operations that all numeric values can perform, including:

- [CSSNumericValue.add](/en-US/docs/Web/API/CSSNumericValue/add) - Adds supplied numbers to the `CSSNumericValue`.
- [CSSNumericValue.sub](/en-US/docs/Web/API/CSSNumericValue/sub) - Subtracts supplied numbers to the `CSSNumericValue`.
- [CSSNumericValue.mul](/en-US/docs/Web/API/CSSNumericValue/mul) - Multiplies supplied numbers to the `CSSNumericValue`.
- [CSSNumericValue.div](/en-US/docs/Web/API/CSSNumericValue/div) - Divides the `CSSNumericValue` by the supplied value, throwing an error if `0`.
- [CSSNumericValue.min](/en-US/docs/Web/API/CSSNumericValue/min) - Returns the minimum value passed
- [CSSNumericValue.max](/en-US/docs/Web/API/CSSNumericValue/max) - Returns the maximum value passed
- [CSSNumericValue.equals](/en-US/docs/Web/API/CSSNumericValue/equals) - Returns true if all the values are the exact same type and value, in the same order. Otherwise, false
- [CSSNumericValue.to](/en-US/docs/Web/API/CSSNumericValue/to) - Converts `value` into another one with the specified unit.
- [CSSNumericValue.toSum](/en-US/docs/Web/API/CSSNumericValue/toSum)
- [CSSNumericValue.type](/en-US/docs/Web/API/CSSNumericValue/type)
- [CSSNumericValue.parse](/en-US/docs/Web/API/CSSNumericValue/parse_static) - Returns a number parsed from a CSS string

[CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)

Represents values for properties that take a position, for example object-position.

[CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)

An interface representing a list of [transform](/en-US/docs/Web/CSS/Reference/Properties/transform) list values. They "contain" one or more [CSSTransformComponent](/en-US/docs/Web/API/CSSTransformComponent)s, which represent individual `transform` function values.

[CSSUnitValue](/en-US/docs/Web/API/CSSUnitValue)

An interface representing numeric values that can be represented as a single unit, or a named number and percentage.

[CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)

Represents property values that reference [custom properties](/en-US/docs/Web/CSS/Reference/Properties/--*). It consists of a list of string fragments and variable references.

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# stylevalue-objects](https://drafts.css-houdini.org/css-typed-om/#stylevalue-objects)
[CSS Typed OM Level 1# the-stylepropertymap](https://drafts.css-houdini.org/css-typed-om/#the-stylepropertymap)
[CSS Typed OM Level 1# cssunparsedvalue](https://drafts.css-houdini.org/css-typed-om/#cssunparsedvalue)
[CSS Typed OM Level 1# keywordvalue-objects](https://drafts.css-houdini.org/css-typed-om/#keywordvalue-objects)

## [Browser compatibility](#browser_compatibility)

### [api.CSSStyleValue](#api.CSSStyleValue)

### [api.StylePropertyMap](#api.StylePropertyMap)

### [api.CSSUnparsedValue](#api.CSSUnparsedValue)

### [api.CSSKeywordValue](#api.CSSKeywordValue)

## [See also](#see_also)

- [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API)
- [Using the CSS Typed Object Model](/en-US/docs/Web/API/CSS_Typed_OM_API/Guide)
- [CSS Houdini](/en-US/docs/Web/API/Houdini_APIs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSS_Typed_OM_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/css_typed_om_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Typed_OM_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcss_typed_om_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSS_Typed_OM_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcss_typed_om_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
