# SVGAngle

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAngle&level=high)

The `SVGAngle` interface is used to represent a value that can be an [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) or [<number>](/en-US/docs/Web/CSS/Reference/Values/number) value.

The `SVGAngle` returned from [SVGAnimatedAngle.animVal](/en-US/docs/Web/API/SVGAnimatedAngle/animVal) and [SVGAnimatedAngle.baseVal](/en-US/docs/Web/API/SVGAnimatedAngle/baseVal) is read only, but the `SVGAngle` returned from [SVGSVGElement.createSVGAngle()](/en-US/docs/Web/API/SVGSVGElement/createSVGAngle) is writable. When designated as read only, attempts to modify the object will result in an exception being thrown.

An `SVGAngle` object can be associated with a particular element. The associated element is used to determine which element's content attribute to update if the object reflects an attribute. Unless otherwise described, an `SVGAngle` object is not associated with any element.

Every `SVGAngle` object operates in one of two modes:

1. Reflect the base value of a reflected animatable attribute (being exposed through the [baseVal](/en-US/docs/Web/API/SVGAnimatedAngle/baseVal) member of an [SVGAnimatedAngle](/en-US/docs/Web/API/SVGAnimatedAngle)),
2. Be detached, which is the case for `SVGAngle` objects created with [SVGSVGElement.createSVGAngle()](/en-US/docs/Web/API/SVGSVGElement/createSVGAngle).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[SVGAngle.unitType](/en-US/docs/Web/API/SVGAngle/unitType)

The type of the value as specified by one of the `SVG_ANGLETYPE_*` constants defined on this interface.

[SVGAngle.value](/en-US/docs/Web/API/SVGAngle/value)

The value as a floating point value, in user units. Setting this attribute will cause `valueInSpecifiedUnits` and `valueAsString` to be updated automatically to reflect this setting.

[SVGAngle.valueInSpecifiedUnits](/en-US/docs/Web/API/SVGAngle/valueInSpecifiedUnits)

The value as a floating point value, in the units expressed by `unitType`. Setting this attribute will cause `value` and `valueAsString` to be updated automatically to reflect this setting.

[SVGAngle.valueAsString](/en-US/docs/Web/API/SVGAngle/valueAsString)

The value as a string value, in the units expressed by `unitType`. Setting this attribute will cause `value`, `valueInSpecifiedUnits`, and `unitType` to be updated automatically to reflect this setting.

## [Instance methods](#instance_methods)

[SVGAngle.convertToSpecifiedUnits()](/en-US/docs/Web/API/SVGAngle/convertToSpecifiedUnits)

Preserve the same underlying stored value, but reset the stored unit identifier to the given `unitType`. Object attributes `unitType`, `valueInSpecifiedUnits`, and `valueAsString` might be modified as a result of this method.

[SVGAngle.newValueSpecifiedUnits()](/en-US/docs/Web/API/SVGAngle/newValueSpecifiedUnits)

Reset the value as a number with an associated unitType, thereby replacing the values for all of the attributes on the object.

## [Static properties](#static_properties)

[SVG_ANGLETYPE_UNKNOWN (0)](#svg_angletype_unknown)

Some unknown type of value.

[SVG_ANGLETYPE_UNSPECIFIED (1)](#svg_angletype_unspecified)

A unitless [<number>](/en-US/docs/Web/CSS/Reference/Values/number) interpreted as a value in degrees.

[SVG_ANGLETYPE_DEG (2)](#svg_angletype_deg)

An [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) with a `deg` unit.

[SVG_ANGLETYPE_RAD (3)](#svg_angletype_rad)

An [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) with a `rad` unit.

[SVG_ANGLETYPE_GRAD (4)](#svg_angletype_grad)

An [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) with a `grad` unit.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGAngle](https://svgwg.org/svg2-draft/types.html#InterfaceSVGAngle)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGAngle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgangle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAngle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgangle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAngle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgangle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
