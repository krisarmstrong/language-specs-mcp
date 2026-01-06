# SVGTextPathElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTextPathElement&level=high)

The `SVGTextPathElement` interface corresponds to the [<textPath>](/en-US/docs/Web/SVG/Reference/Element/textPath) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent interface, [SVGTextContentElement](/en-US/docs/Web/API/SVGTextContentElement).

[SVGTextPathElement.href](/en-US/docs/Web/API/SVGTextPathElement/href)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [href](/en-US/docs/Web/SVG/Reference/Attribute/href) or [xlink:href](/en-US/docs/Web/SVG/Reference/Attribute/xlink:href) attribute of the given element.

[SVGTextPathElement.startOffset](/en-US/docs/Web/API/SVGTextPathElement/startOffset)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the X component of the [startOffset](/en-US/docs/Web/SVG/Reference/Attribute/startOffset) attribute of the given element.

[SVGTextPathElement.method](/en-US/docs/Web/API/SVGTextPathElement/method)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [method](/en-US/docs/Web/SVG/Reference/Attribute/method) attribute of the given element. It takes one of the `TEXTPATH_METHODTYPE_*` constants defined on this interface.

[SVGTextPathElement.spacing](/en-US/docs/Web/API/SVGTextPathElement/spacing)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [spacing](/en-US/docs/Web/SVG/Reference/Attribute/spacing) attribute of the given element. It takes one of the `TEXTPATH_SPACINGTYPE_*` constants defined on this interface.

## [Instance methods](#instance_methods)

This interface does not provide any specific methods, but implements those of its parent, [SVGTextContentElement](/en-US/docs/Web/API/SVGTextContentElement).

## [Static properties](#static_properties)

[TEXTPATH_METHODTYPE_UNKNOWN (0)](#textpath_methodtype_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[TEXTPATH_METHODTYPE_ALIGN (1)](#textpath_methodtype_align)

Corresponds to the value `align`.

[TEXTPATH_METHODTYPE_STRETCH (2)](#textpath_methodtype_stretch)

Corresponds to the value `stretch`.

[TEXTPATH_SPACINGTYPE_UNKNOWN (0)](#textpath_spacingtype_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[TEXTPATH_SPACINGTYPE_AUTO (1)](#textpath_spacingtype_auto)

Corresponds to the value `auto`.

[TEXTPATH_SPACINGTYPE_EXACT (2)](#textpath_spacingtype_exact)

Corresponds to the value `exact`.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGTextPathElement](https://svgwg.org/svg2-draft/text.html#InterfaceSVGTextPathElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<textPath>](/en-US/docs/Web/SVG/Reference/Element/textPath)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGTextPathElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgtextpathelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTextPathElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgtextpathelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTextPathElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgtextpathelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
