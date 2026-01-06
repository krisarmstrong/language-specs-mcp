# CSSValueList

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `CSSValueList` interface derives from the [CSSValue](/en-US/docs/Web/API/CSSValue) interface and provides the abstraction of an ordered collection of CSS values.

Note: This interface was part of an attempt to create a typed CSS Object Model. This attempt has been abandoned, and most browsers do not implement it.

To achieve your purpose, you can use:

- the untyped [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model), widely supported, or
- the modern [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API), less supported and considered experimental.

Some properties allow an empty list in their syntax. In that case, these properties take the `none` identifier. So, an empty list means that the property has the value `none`.

The items in the `CSSValueList` are accessible via an integral index, starting from 0.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [CSSValue](/en-US/docs/Web/API/CSSValue).

[CSSValueList.length](/en-US/docs/Web/API/CSSValueList/length)Read onlyDeprecated

An `unsigned long` representing the number of `CSSValues` in the list.

## [Instance methods](#instance_methods)

[CSSValueList.item()](/en-US/docs/Web/API/CSSValueList/item)Deprecated

This method is used to retrieve a [CSSValue](/en-US/docs/Web/API/CSSValue) by ordinal index. The order in this collection represents the order of the values in the CSS style property. If index is greater than or equal to the number of values in the list, this returns `null`.

## [Specifications](#specifications)

This feature was originally defined in the [DOM Style Level 2](https://www.w3.org/TR/DOM-Level-2-Style/) specification, but has been dropped from any standardization effort since then.

It has been superseded by a modern, but incompatible, [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API) that is now on the standard track.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSPrimitiveValue](/en-US/docs/Web/API/CSSPrimitiveValue)
- [CSSValue](/en-US/docs/Web/API/CSSValue)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CSSValueList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssvaluelist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSValueList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssvaluelist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSValueList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssvaluelist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc7edf2734fccb185c5e93ee114ea3d5edc0177b5%0A*+Document+last+modified%3A+2024-07-26T02%3A57%3A09.000Z%0A%0A%3C%2Fdetails%3E)
