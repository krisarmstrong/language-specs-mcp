# SVGTransform

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTransform&level=high)

The `SVGTransform` interface reflects one of the component transformations within an [SVGTransformList](/en-US/docs/Web/API/SVGTransformList); thus, an `SVGTransform` object corresponds to a single component (e.g., `scale(…)` or `matrix(…)`) within a [transform](/en-US/docs/Web/SVG/Reference/Attribute/transform) attribute.

An `SVGTransform` object can be designated as read only, which means that attempts to modify the object will result in an exception being thrown.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static properties](#static_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[type](/en-US/docs/Web/API/SVGTransform/type)

The type of the value as specified by one of the `SVG_TRANSFORM_*` constants defined on this interface.

[angle](/en-US/docs/Web/API/SVGTransform/angle)

The angle as a floating point value. A convenience attribute for `SVG_TRANSFORM_ROTATE`, `SVG_TRANSFORM_SKEWX` and `SVG_TRANSFORM_SKEWY`. For `SVG_TRANSFORM_MATRIX`, `SVG_TRANSFORM_TRANSLATE` and `SVG_TRANSFORM_SCALE`, `angle` will be zero.

[matrix](/en-US/docs/Web/API/SVGTransform/matrix)

The matrix as a [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) that represents this transformation. The matrix object is live, meaning that any changes made to the `SVGTransform` object are immediately reflected in the matrix object and vice versa. In case the matrix object is changed directly (i.e., without using the methods on the `SVGTransform` interface itself) then the type of the `SVGTransform` changes to `SVG_TRANSFORM_MATRIX`.

## [Instance methods](#instance_methods)

[setMatrix()](/en-US/docs/Web/API/SVGTransform/setMatrix)

Sets the transform type to `SVG_TRANSFORM_MATRIX`, with parameter matrix defining the new transformation. Note that the values from the parameter `matrix` are copied.

[setTranslate()](/en-US/docs/Web/API/SVGTransform/setTranslate)

Sets the transform type to `SVG_TRANSFORM_TRANSLATE`, with parameters `tx` and `ty` defining the translation amounts.

[setScale()](/en-US/docs/Web/API/SVGTransform/setScale)

Sets the transform type to `SVG_TRANSFORM_SCALE`, with parameters `sx` and `sy` defining the scale amounts.

[setRotate()](/en-US/docs/Web/API/SVGTransform/setRotate)

Sets the transform type to `SVG_TRANSFORM_ROTATE`, with parameter `angle` defining the rotation angle and parameters `cx` and `cy` defining the optional center of rotation.

[setSkewX()](/en-US/docs/Web/API/SVGTransform/setSkewX)

Sets the transform type to `SVG_TRANSFORM_SKEWX`, with parameter `angle` defining the amount of skew.

[setSkewY()](/en-US/docs/Web/API/SVGTransform/setSkewY)

Sets the transform type to `SVG_TRANSFORM_SKEWY`, with parameter `angle` defining the amount of skew.

## [Static properties](#static_properties)

[SVG_TRANSFORM_UNKNOWN (0)](#svg_transform_unknown)

The unit type is not one of predefined unit types. It is invalid to attempt to define a new value of this type or to attempt to switch an existing value to this type.

[SVG_TRANSFORM_MATRIX (1)](#svg_transform_matrix)

A `matrix(…)` transformation.

[SVG_TRANSFORM_TRANSLATE (2)](#svg_transform_translate)

A `translate(…)` transformation.

[SVG_TRANSFORM_SCALE (3)](#svg_transform_scale)

A `scale(…)` transformation.

[SVG_TRANSFORM_ROTATE (4)](#svg_transform_rotate)

A `rotate(…)` transformation.

[SVG_TRANSFORM_SKEWX (5)](#svg_transform_skewx)

A `skewx(…)` transformation.

[SVG_TRANSFORM_SKEWY (6)](#svg_transform_skewy)

A `skewy(…)` transformation.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGTransform](https://svgwg.org/svg2-draft/coords.html#InterfaceSVGTransform)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGTransform/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgtransform/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTransform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgtransform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGTransform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgtransform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
