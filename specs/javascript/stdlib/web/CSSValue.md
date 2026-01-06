# CSSValue

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `CSSValue` interface represents the current computed value of a CSS property.

Note: This interface was part of an attempt to create a typed CSS Object Model. This attempt has been abandoned, and most browsers do not implement it.

To achieve your purpose, you can use:

- the untyped [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model), widely supported, or
- the modern [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API), less supported and considered experimental.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[CSSValue.cssText](/en-US/docs/Web/API/CSSValue/cssText)Deprecated

A string representing the current value.

[CSSValue.cssValueType](/en-US/docs/Web/API/CSSValue/cssValueType)Read onlyDeprecated

An `unsigned short` representing a code defining the type of the value. Possible values are:

ConstantDescription`CSS_CUSTOM`The value is a custom value.`CSS_INHERIT`The value is inherited and the `cssText` contains `"inherit"`.`CSS_PRIMITIVE_VALUE`The value is a primitive value and an instance of the [CSSPrimitiveValue](/en-US/docs/Web/API/CSSPrimitiveValue) interface can be obtained by using binding-specific casting methods on this instance of the `CSSValue` interface.`CSS_VALUE_LIST`The value is a `CSSValue` list and an instance of the [CSSValueList](/en-US/docs/Web/API/CSSValueList) interface can be obtained by using binding-specific casting methods on this instance of the `CSSValue` interface.

## [Specifications](#specifications)

This feature was originally defined in the [DOM Style Level 2](https://www.w3.org/TR/DOM-Level-2-Style/) specification, but has been dropped from any standardization effort since then.

It has been superseded by a modern, but incompatible, [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API) that is now on the standard track.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSPrimitiveValue](/en-US/docs/Web/API/CSSPrimitiveValue)
- [CSSValueList](/en-US/docs/Web/API/CSSValueList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
