# SVGGradientElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGradientElement&level=high)

The `SVGGradient` interface is a base interface used by [SVGLinearGradientElement](/en-US/docs/Web/API/SVGLinearGradientElement) and [SVGRadialGradientElement](/en-US/docs/Web/API/SVGRadialGradientElement).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGGradientElement.href](/en-US/docs/Web/API/SVGGradientElement/href)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [href](/en-US/docs/Web/SVG/Reference/Attribute/href) or [xlink:href](/en-US/docs/Web/SVG/Reference/Attribute/xlink:href) attribute of the given element.

[SVGGradientElement.gradientUnits](/en-US/docs/Web/API/SVGGradientElement/gradientUnits)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [gradientUnits](/en-US/docs/Web/SVG/Reference/Attribute/gradientUnits) attribute on the given element. This property takes one of the constants defined in [SVGUnitTypes](/en-US/docs/Web/API/SVGUnitTypes).

[SVGGradientElement.gradientTransform](/en-US/docs/Web/API/SVGGradientElement/gradientTransform)Read only

An [SVGAnimatedTransformList](/en-US/docs/Web/API/SVGAnimatedTransformList) corresponding to the [gradientTransform](/en-US/docs/Web/SVG/Reference/Attribute/gradientTransform) attribute on the given element.

[SVGGradientElement.spreadMethod](/en-US/docs/Web/API/SVGGradientElement/spreadMethod)Read only

An [SVGAnimatedEnumeration](/en-US/docs/Web/API/SVGAnimatedEnumeration) corresponding to the [spreadMethod](/en-US/docs/Web/SVG/Reference/Attribute/spreadMethod) attribute on the given element. One of the spread method types defined on this interface.

## [Instance methods](#instance_methods)

This interface does not provide any specific methods, but implements those of its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

## [Static properties](#static_properties)

[SVG_SPREADMETHOD_UNKNOWN (0)](#svg_spreadmethod_unknown)

The type is not one of predefined types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_SPREADMETHOD_PAD (1)](#svg_spreadmethod_pad)

Corresponds to value `pad`.

[SVG_SPREADMETHOD_REFLECT (2)](#svg_spreadmethod_reflect)

Corresponds to value `reflect`.

[SVG_SPREADMETHOD_REPEAT (3)](#svg_spreadmethod_repeat)

Corresponds to value `repeat`.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGGradientElement](https://svgwg.org/svg2-draft/pservers.html#InterfaceSVGGradientElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGGradientElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svggradientelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGradientElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvggradientelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGGradientElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvggradientelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
