# SVGLength

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGLength&level=high)

The `SVGLength` interface correspond to the [<length>](/en-US/docs/Web/SVG/Guides/Content_type#length) basic data type.

An `SVGLength` object can be designated as read only, which means that attempts to modify the object will result in an exception being thrown.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[unitType](/en-US/docs/Web/API/SVGLength/unitType)

The type of the value as specified by one of the `SVG_LENGTHTYPE_*` constants defined on this interface.

[value](/en-US/docs/Web/API/SVGLength/value)

The value as a floating point value, in user units.

[valueAsString](/en-US/docs/Web/API/SVGLength/valueAsString)

The value as a string value, in the units expressed by `unitType`.

[valueInSpecifiedUnits](/en-US/docs/Web/API/SVGLength/valueInSpecifiedUnits)

The value as a floating point value, in the units expressed by `unitType`.

## [Instance methods](#instance_methods)

[convertToSpecifiedUnits()](/en-US/docs/Web/API/SVGLength/convertToSpecifiedUnits)

Preserve the same underlying stored value, but reset the stored unit identifier to the given `unitType`.

[newValueSpecifiedUnits()](/en-US/docs/Web/API/SVGLength/newValueSpecifiedUnits)

Reset the value as a number with an associated `unitType`, thereby replacing the values for all of the attributes on the object.

## [Static properties](#static_properties)

[SVG_LENGTHTYPE_UNKNOWN (0)](#svg_lengthtype_unknown)

The unit type is not one of predefined unit types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_LENGTHTYPE_NUMBER (1)](#svg_lengthtype_number)

No unit type was provided (i.e., a unitless value was specified), which indicates a value in user units.

[SVG_LENGTHTYPE_PERCENTAGE (2)](#svg_lengthtype_percentage)

A percentage value was specified.

[SVG_LENGTHTYPE_EMS (3)](#svg_lengthtype_ems)

A value was specified using the `em` units.

[SVG_LENGTHTYPE_EXS (4)](#svg_lengthtype_exs)

A value was specified using the `ex` units.

[SVG_LENGTHTYPE_PX (5)](#svg_lengthtype_px)

A value was specified using the `px` units.

[SVG_LENGTHTYPE_CM (6)](#svg_lengthtype_cm)

A value was specified using the `cm` units.

[SVG_LENGTHTYPE_MM (7)](#svg_lengthtype_mm)

A value was specified using the `mm` units.

[SVG_LENGTHTYPE_IN (8)](#svg_lengthtype_in)

A value was specified using the `in` units.

[SVG_LENGTHTYPE_PT (9)](#svg_lengthtype_pt)

A value was specified using the `pt` units.

[SVG_LENGTHTYPE_PC (10)](#svg_lengthtype_pc)

A value was specified using the `pc` units.

## [Example](#example)

xml

```
<svg height="200" onload="start();" version="1.1" width="200" xmlns="http://www.w3.org/2000/svg">
  <script><![CDATA[
function start() {
  const rect = document.getElementById("myRect");
  const val = rect.x.baseVal;

  // read x in pixel and cm units
  console.log(
    `value: ${val.value}, valueInSpecifiedUnits: ${val.valueInSpecifiedUnits} (${val.unitType}), valueAsString: ${val.valueAsString}`,
  );

  // set x = 20pt and read it out in pixel and pt units
  val.newValueSpecifiedUnits(SVGLength.SVG_LENGTHTYPE_PT, 20);
  console.log(
    `value: ${val.value}, valueInSpecifiedUnits: ${val.valueInSpecifiedUnits} (${val.unitType}), valueAsString: ${val.valueAsString}`,
  );

  // convert x = 20pt to inches and read out in pixel and inch units
  val.convertToSpecifiedUnits(SVGLength.SVG_LENGTHTYPE_IN);
  console.log(
    `value: ${val.value}, valueInSpecifiedUnits: ${val.valueInSpecifiedUnits} (${val.unitType}), valueAsString: ${val.valueAsString}`,
  );
}
]]></script>
  <rect id="myRect"
        x="1cm" y="1cm"
        fill="green" stroke="black" stroke-width="1"
        width="1cm" height="1cm"
  />
</svg>
```

Results on a desktop monitor (pixel units will be dpi-dependent):

```
value: 37.7952766418457, valueInSpecifiedUnits: 6: 1, valueAsString: 1cm
value: 26.66666603088379, valueInSpecifiedUnits 9: 20, valueAsString: 20pt
value: 26.66666603088379, valueInSpecifiedUnits 8: 0.277777761220932, valueAsString: 0.277778in
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGLength](https://svgwg.org/svg2-draft/types.html#InterfaceSVGLength)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGLength/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svglength/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGLength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvglength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGLength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvglength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6d2000984203c51f1aad49107ebcebe14d3c1238%0A*+Document+last+modified%3A+2025-05-30T14%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E)
