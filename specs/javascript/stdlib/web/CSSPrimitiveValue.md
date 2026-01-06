# CSSPrimitiveValue

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `CSSPrimitiveValue` interface derives from the [CSSValue](/en-US/docs/Web/API/CSSValue) interface and represents the current computed value of a CSS property.

Note: This interface was part of an attempt to create a typed CSS Object Model. This attempt has been abandoned, and most browsers do not implement it.

To achieve your purpose, you can use:

- the untyped [CSS Object Model](/en-US/docs/Web/API/CSS_Object_Model), widely supported, or
- the modern [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API), less supported and considered experimental.

This interface represents a single CSS value. It may be used to determine the value of a specific style property currently set in a block or to set a specific style property explicitly within the block. An instance of this interface might be obtained from the [getPropertyCSSValue()](/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyCSSValue) method of the [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration) interface. A `CSSPrimitiveValue` object only occurs in a context of a CSS property.

Conversions are allowed between absolute values (from millimeters to centimeters, from degrees to radians, and so on) but not between relative values. (For example, a pixel value cannot be converted to a centimeter value.) Percentage values can't be converted since they are relative to the parent value (or another property value). There is one exception for color percentage values: since a color percentage value is relative to the range 0-255, a color percentage value can be converted to a number (see also the `RGBColor` interface).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [CSSValue](/en-US/docs/Web/API/CSSValue).

[CSSPrimitiveValue.primitiveType](/en-US/docs/Web/API/CSSPrimitiveValue/primitiveType)Read onlyDeprecated

An `unsigned short` representing the type of the value. Possible values are:

ConstantDescription`CSS_ATTR`The value is an [attr()](/en-US/docs/Web/CSS/Reference/Values/attr) function. The value can be obtained by using the `getStringValue()` method.`CSS_CM`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in centimeters. The value can be obtained by using the `getFloatValue()` method.`CSS_COUNTER`The value is a [counter or counters](/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters) function. The value can be obtained by using the `getCounterValue()` method.`CSS_DEG`The value is an [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) in degrees. The value can be obtained by using the `getFloatValue()` method.`CSS_DIMENSION`The value is a [<number>](/en-US/docs/Web/CSS/Reference/Values/number) with an unknown dimension. The value can be obtained by using the `getFloatValue()` method.`CSS_EMS`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in em units. The value can be obtained by using the `getFloatValue()` method.`CSS_EXS`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in ex units. The value can be obtained by using the `getFloatValue()` method.`CSS_GRAD`The value is an [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) in grads. The value can be obtained by using the `getFloatValue()` method.`CSS_HZ`The value is a [<frequency>](/en-US/docs/Web/CSS/Reference/Values/frequency) in Hertz. The value can be obtained by using the getFloatValue method.`CSS_IDENT`The value is an identifier. The value can be obtained by using the `getStringValue()` method.`CSS_IN`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in inches. The value can be obtained by using the `getFloatValue()` method.`CSS_KHZ`The value is a [<frequency>](/en-US/docs/Web/CSS/Reference/Values/frequency) in Kilohertz. The value can be obtained by using the `getFloatValue()` method.`CSS_MM`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in millimeters. The value can be obtained by using the `getFloatValue()` method.`CSS_MS`The value is a [<time>](/en-US/docs/Web/CSS/Reference/Values/time) in milliseconds. The value can be obtained by using the `getFloatValue()` method.`CSS_NUMBER`The value is a simple [<number>](/en-US/docs/Web/CSS/Reference/Values/number). The value can be obtained by using the `getFloatValue()` method.`CSS_PC`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in picas. The value can be obtained by using the `getFloatValue()` method.`CSS_PERCENTAGE`The value is a [<percentage>](/en-US/docs/Web/CSS/Reference/Values/percentage). The value can be obtained by using the `getFloatValue()` method.`CSS_PT`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in points. The value can be obtained by using the `getFloatValue()` method.`CSS_PX`The value is a [<length>](/en-US/docs/Web/CSS/Reference/Values/length) in pixels. The value can be obtained by using the `getFloatValue()` method.`CSS_RAD`The value is an [<angle>](/en-US/docs/Web/CSS/Reference/Values/angle) in radians. The value can be obtained by using the `getFloatValue()` method.`CSS_RECT`The value is a [rect()](/en-US/docs/Web/CSS/Reference/Values/shape#syntax) function. The value can be obtained by using the `getRectValue()` method.`CSS_RGBCOLOR`The value is an [<color>](/en-US/docs/Web/CSS/Reference/Values/color_value). The value can be obtained by using the `getRGBColorValue()` method.`CSS_S`The value is a [<time>](/en-US/docs/Web/CSS/Reference/Values/time) in seconds. The value can be obtained by using the `getFloatValue()` method.`CSS_STRING`The value is a [<string>](/en-US/docs/Web/CSS/Reference/Values/string). The value can be obtained by using the `getStringValue()` method.`CSS_UNKNOWN`The value is not a recognized CSS2 value. The value can only be obtained by using the [cssText](/en-US/docs/Web/API/CSSValue/cssText) attribute.`CSS_URI`The value is a [<url>](/en-US/docs/Web/CSS/Reference/Values/url_value). The value can be obtained by using the `getStringValue()` method.

## [Instance methods](#instance_methods)

[CSSPrimitiveValue.getCounterValue()](/en-US/docs/Web/API/CSSPrimitiveValue/getCounterValue)Deprecated

This method is used to get the [counter](/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters) value. If this CSS value doesn't contain a counter value, a [DOMException](/en-US/docs/Web/API/DOMException) is raised. Modification to the corresponding style property can be achieved using the `Counter` interface.

[CSSPrimitiveValue.getFloatValue()](/en-US/docs/Web/API/CSSPrimitiveValue/getFloatValue)Deprecated

This method is used to get a float value in a specified unit. If this CSS value doesn't contain a float value or can't be converted into the specified unit, a [DOMException](/en-US/docs/Web/API/DOMException) is raised.

[CSSPrimitiveValue.getRGBColorValue()](/en-US/docs/Web/API/CSSPrimitiveValue/getRGBColorValue)Deprecated

This method is used to get the RGB color. If this CSS value doesn't contain a RGB color value, a [DOMException](/en-US/docs/Web/API/DOMException) is raised. Modification to the corresponding style property can be achieved using the `RGBColor` interface.

[CSSPrimitiveValue.getRectValue()](/en-US/docs/Web/API/CSSPrimitiveValue/getRectValue)Deprecated

This method is used to get the Rect value. If this CSS value doesn't contain a rect value, a [DOMException](/en-US/docs/Web/API/DOMException) is raised. Modification to the corresponding style property can be achieved using the `Rect` interface.

[CSSPrimitiveValue.getStringValue()](/en-US/docs/Web/API/CSSPrimitiveValue/getStringValue)Deprecated

This method is used to get the string value. If the CSS value doesn't contain a string value, a [DOMException](/en-US/docs/Web/API/DOMException) is raised.

[CSSPrimitiveValue.setFloatValue()](/en-US/docs/Web/API/CSSPrimitiveValue/setFloatValue)Deprecated

A method to set the float value with a specified unit. If the property attached with this value can not accept the specified unit or the float value, the value will be unchanged and a [DOMException](/en-US/docs/Web/API/DOMException) will be raised.

[CSSPrimitiveValue.setStringValue()](/en-US/docs/Web/API/CSSPrimitiveValue/setStringValue)Deprecated

A method to set the string value with the specified unit. If the property attached to this value can't accept the specified unit or the string value, the value will be unchanged and a [DOMException](/en-US/docs/Web/API/DOMException) will be raised.

## [Specifications](#specifications)

This feature was originally defined in the [DOM Style Level 2](https://www.w3.org/TR/DOM-Level-2-Style/) specification, but has been dropped from any standardization effort since then.

It has been superseded by a modern, but incompatible, [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Typed_OM_API) that is now on the standard track.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSValue](/en-US/docs/Web/API/CSSValue)
- [CSSValueList](/en-US/docs/Web/API/CSSValueList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSPrimitiveValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssprimitivevalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPrimitiveValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssprimitivevalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSPrimitiveValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssprimitivevalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
