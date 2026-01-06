# CSSUnparsedValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSUnparsedValue&level=not)

The `CSSUnparsedValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model) represents property values that reference [custom properties](/en-US/docs/Web/CSS/Guides/Cascading_variables). It consists of a list of string fragments and variable references.

Custom properties are represented by `CSSUnparsedValue` and [var()](/en-US/docs/Web/CSS/Reference/Values/var) references are represented using [CSSVariableReferenceValue](/en-US/docs/Web/API/CSSVariableReferenceValue).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CSSUnparsedValue()](/en-US/docs/Web/API/CSSUnparsedValue/CSSUnparsedValue)

Creates a new `CSSUnparsedValue` object.

## [Instance properties](#instance_properties)

[CSSUnparsedValue.length](/en-US/docs/Web/API/CSSUnparsedValue/length)

Returns the number of items in the `CSSUnparsedValue` object.

## [Instance methods](#instance_methods)

[CSSUnparsedValue.entries()](/en-US/docs/Web/API/CSSUnparsedValue/entries)

Returns an array of a given object's own enumerable property `[key, value]` pairs in the same order as that provided by a [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in) loop (the difference being that a for-in loop enumerates properties in the prototype chain as well).

[CSSUnparsedValue.forEach()](/en-US/docs/Web/API/CSSUnparsedValue/forEach)

Executes a provided function once for each element of the `CSSUnparsedValue` object.

[CSSUnparsedValue.keys()](/en-US/docs/Web/API/CSSUnparsedValue/keys)

Returns a new array iterator object that contains the keys for each index in the `CSSUnparsedValue` object.

[CSSUnparsedValue.values()](/en-US/docs/Web/API/CSSUnparsedValue/values)

Returns a new array iterator object that contains the values for each index in the `CSSUnparsedValue` object.

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# cssunparsedvalue](https://drafts.css-houdini.org/css-typed-om/#cssunparsedvalue)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSImageValue](/en-US/docs/Web/API/CSSImageValue)
- [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)
- [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)
- [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [Using the CSS Typed OM](/en-US/docs/Web/API/CSS_Typed_OM_API/Guide)
- [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSUnparsedValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssunparsedvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSUnparsedValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssunparsedvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSUnparsedValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssunparsedvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
