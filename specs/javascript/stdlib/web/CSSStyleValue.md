# CSSStyleValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleValue&level=not)

The `CSSStyleValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) is the base class of all CSS values accessible through the Typed OM API. An instance of this class may be used anywhere a string is expected.

## In this article

- [Interfaces based on CSSStyleValue](#interfaces_based_on_cssstylevalue)
- [Static methods](#static_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces based on CSSStyleValue](#interfaces_based_on_cssstylevalue)

Below is a list of interfaces based on the `CSSStyleValue` interface.

- [CSSImageValue](/en-US/docs/Web/API/CSSImageValue)
- [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)
- [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)
- [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)

## [Static methods](#static_methods)

[CSSStyleValue.parse()](/en-US/docs/Web/API/CSSStyleValue/parse_static)

Sets a specific CSS property to the specified values and returns the first value as a `CSSStyleValue` object.

[CSSStyleValue.parseAll()](/en-US/docs/Web/API/CSSStyleValue/parseAll_static)

Sets all occurrences of a specific CSS property to the specified value and returns an array of `CSSStyleValue` objects, each containing one of the supplied values.

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# stylevalue-objects](https://drafts.css-houdini.org/css-typed-om/#stylevalue-objects)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CSSStyleValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssstylevalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssstylevalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSStyleValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssstylevalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
