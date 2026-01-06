# CSSNumericValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSNumericValue&level=not)

The `CSSNumericValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) represents operations that all numeric values can perform.

## In this article

- [Interfaces based on CSSNumericValue](#interfaces_based_on_cssnumericvalue)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces based on CSSNumericValue](#interfaces_based_on_cssnumericvalue)

Below is a list of interfaces based on the CSSNumericValue interface.

- `CSSMathClamp`
- [CSSMathInvert](/en-US/docs/Web/API/CSSMathInvert)
- [CSSMathMax](/en-US/docs/Web/API/CSSMathMax)
- [CSSMathMin](/en-US/docs/Web/API/CSSMathMin)
- [CSSMathNegate](/en-US/docs/Web/API/CSSMathNegate)
- [CSSMathProduct](/en-US/docs/Web/API/CSSMathProduct)
- [CSSMathSum](/en-US/docs/Web/API/CSSMathSum)
- [CSSMathValue](/en-US/docs/Web/API/CSSMathValue)
- [CSSNumericArray](/en-US/docs/Web/API/CSSNumericArray)
- [CSSUnitValue](/en-US/docs/Web/API/CSSUnitValue)

## [Instance properties](#instance_properties)

None.

## [Static methods](#static_methods)

[CSSNumericValue.parse](/en-US/docs/Web/API/CSSNumericValue/parse_static)

Allows a `CSSNumericValue` to be constructed directly from a string containing CSS.

## [Instance methods](#instance_methods)

[CSSNumericValue.add](/en-US/docs/Web/API/CSSNumericValue/add)

Adds a supplied number to the `CSSNumericValue`.

[CSSNumericValue.sub](/en-US/docs/Web/API/CSSNumericValue/sub)

Subtracts a supplied number from the `CSSNumericValue`.

[CSSNumericValue.mul](/en-US/docs/Web/API/CSSNumericValue/mul)

Multiplies the `CSSNumericValue` by the supplied value.

[CSSNumericValue.div](/en-US/docs/Web/API/CSSNumericValue/div)

Divides the `CSSNumericValue` by the supplied value.

[CSSNumericValue.min](/en-US/docs/Web/API/CSSNumericValue/min)

Returns the minimum value passed

[CSSNumericValue.max](/en-US/docs/Web/API/CSSNumericValue/max)

Returns the maximum value passed

[CSSNumericValue.equals](/en-US/docs/Web/API/CSSNumericValue/equals)

True if all the values are the exact same type and value, in the same order. Otherwise, false.

[CSSNumericValue.to](/en-US/docs/Web/API/CSSNumericValue/to)

Converts `value` into another one with the specified unit.

[CSSNumericValue.toSum](/en-US/docs/Web/API/CSSNumericValue/toSum)

Converts an existing `CSSNumericValue` into a [CSSMathSum](/en-US/docs/Web/API/CSSMathSum) object with values of a specified unit.

[CSSNumericValue.type](/en-US/docs/Web/API/CSSNumericValue/type)

Returns the type of `CSSNumericValue`, one of `angle`, `flex`, `frequency`, `length`, `resolution`, `percent`, `percentHint`, or `time`.

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# numeric-value](https://drafts.css-houdini.org/css-typed-om/#numeric-value)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSImageValue](/en-US/docs/Web/API/CSSImageValue)
- [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)
- [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CSSNumericValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssnumericvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSNumericValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssnumericvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSNumericValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssnumericvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1b094710cd2816a6669ce616b6f56d0a5b25e6ad%0A*+Document+last+modified%3A+2023-07-18T16%3A15%3A49.000Z%0A%0A%3C%2Fdetails%3E)
