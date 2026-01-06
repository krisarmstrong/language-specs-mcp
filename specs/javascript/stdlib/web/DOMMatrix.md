# DOMMatrix

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMMatrix&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `DOMMatrix` interface represents 4×4 matrices, suitable for 2D and 3D operations including rotation and translation. It is a mutable version of the [DOMMatrixReadOnly](/en-US/docs/Web/API/DOMMatrixReadOnly) interface. The interface is available inside [web workers](/en-US/docs/Web/API/Web_Workers_API).

`WebKitCSSMatrix` and `SVGMatrix` are aliases to `DOMMatrix`.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static methods](#static_methods)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMMatrix()](/en-US/docs/Web/API/DOMMatrix/DOMMatrix)

Creates and returns a new `DOMMatrix` object.

## [Instance properties](#instance_properties)

This interface inherits properties from [DOMMatrixReadOnly](/en-US/docs/Web/API/DOMMatrixReadOnly), though some of these properties are altered to be mutable.

[m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42, m43, m44](#m11)

Double-precision floating-point values representing each component of a 4×4 matrix, where `m11` through `m14` are the first column, `m21` through `m24` are the second column, and so forth.

[a, b, c, d, e, f](#a)

Double-precision floating-point values representing the components of a 4×4 matrix which are required in order to perform 2D rotations and translations. These are aliases for specific components of a 4×4 matrix, as shown below.

`2D``3D equivalent``a``m11``b``m12``c``m21``d``m22``e``m41``f``m42`

## [Instance methods](#instance_methods)

This interface includes the following methods, as well as the methods it inherits from [DOMMatrixReadOnly](/en-US/docs/Web/API/DOMMatrixReadOnly).

[DOMMatrix.invertSelf()](/en-US/docs/Web/API/DOMMatrix/invertSelf)

Modifies the matrix by inverting it. If the matrix can't be inverted, its components are all set to `NaN`, and [is2D](/en-US/docs/Web/API/DOMMatrixReadOnly/is2D) returns `false`.

[DOMMatrix.multiplySelf()](/en-US/docs/Web/API/DOMMatrix/multiplySelf)

Modifies the matrix by post-multiplying it with the specified `DOMMatrix`. This is equivalent to the dot product `A⋅B`, where matrix `A` is the source matrix and `B` is the matrix given as an input to the method. Returns itself.

[DOMMatrix.preMultiplySelf()](/en-US/docs/Web/API/DOMMatrix/preMultiplySelf)

Modifies the matrix by pre-multiplying it with the specified `DOMMatrix`. Returns itself.

[DOMMatrix.translateSelf()](/en-US/docs/Web/API/DOMMatrix/translateSelf)

Modifies the matrix by applying the specified vector. The default vector is `[0, 0, 0]`. Returns itself.

[DOMMatrix.scaleSelf()](/en-US/docs/Web/API/DOMMatrix/scaleSelf)

Modifies the matrix by applying the specified scaling factors, with the center located at the specified origin. Also returns itself. By default, the scaling factor is `1` for all three axes, and the origin is `(0, 0, 0)`. Returns itself.

[DOMMatrix.scale3dSelf()](/en-US/docs/Web/API/DOMMatrix/scale3dSelf)

Modifies the matrix by applying the specified scaling factor to all three axes, centered on the given origin. Returns itself.

[DOMMatrix.rotateSelf()](/en-US/docs/Web/API/DOMMatrix/rotateSelf)

Modifies the matrix by rotating itself around each axis by the specified number of degrees. Returns itself.

[DOMMatrix.rotateAxisAngleSelf()](/en-US/docs/Web/API/DOMMatrix/rotateAxisAngleSelf)

Modifies the matrix by rotating it by the specified angle around the given vector. Returns itself.

[DOMMatrix.rotateFromVectorSelf()](/en-US/docs/Web/API/DOMMatrix/rotateFromVectorSelf)

Modifies the matrix by rotating it by the angle between the specified vector and `(1, 0)`. Returns itself.

[DOMMatrix.setMatrixValue()](/en-US/docs/Web/API/DOMMatrix/setMatrixValue)

Replaces the contents of the matrix with the matrix described by the specified transform or transforms. Returns itself.

[DOMMatrix.skewXSelf()](/en-US/docs/Web/API/DOMMatrix/skewXSelf)

Modifies the matrix by applying the specified skew transformation along the X-axis. Returns itself.

[DOMMatrix.skewYSelf()](/en-US/docs/Web/API/DOMMatrix/skewYSelf)

Modifies the matrix by applying the specified skew transformation along the Y-axis. Returns itself.

## [Static methods](#static_methods)

[fromFloat32Array()](/en-US/docs/Web/API/DOMMatrix/fromFloat32Array_static)

Creates a new `DOMMatrix` object given a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) of 6 or 16 single-precision (32-bit) floating-point values.

[fromFloat64Array()](/en-US/docs/Web/API/DOMMatrix/fromFloat64Array_static)

Creates a new `DOMMatrix` object given a [Float64Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) of 6 or 16 double-precision (64-bit) floating-point values.

[fromMatrix()](/en-US/docs/Web/API/DOMMatrix/fromMatrix_static)

Creates a new `DOMMatrix` object given an existing matrix or an object which provides the values for its properties.

## [Usage notes](#usage_notes)

The matrix defined by the `DOMMatrix` interface is comprised of four rows of four columns each. While it's beyond the scope of this article to explain the mathematics involved, this 4×4 size is enough to describe any transformation you might apply to either 2D or 3D geometries.

Here are the positions of the 16 elements (m_11 through m_44) which comprise the 4×4 abstract matrix:

[m11m21m31m41m12m22m32m42m13m23m33m43m14m24m34m44]\left [ \begin{matrix} m_{11} & m_{21} & m_{31} & m_{41} \\ m_{12} & m_{22} & m_{32} & m_{42} \\ m_{13} & m_{23} & m_{33} & m_{43} \\ m_{14} & m_{24} & m_{34} & m_{44} \end{matrix} \right ]

The `DOMMatrix` interface is designed with the intent that it will be used for all matrices within markup.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMMatrix](https://drafts.fxtf.org/geometry/#DOMMatrix)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMMatrixReadOnly.is2D](/en-US/docs/Web/API/DOMMatrixReadOnly/is2D)
- [DOMMatrixReadOnly.isIdentity](/en-US/docs/Web/API/DOMMatrixReadOnly/isIdentity)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMMatrix/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dommatrix/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMMatrix&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdommatrix%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMMatrix%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdommatrix%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F359abb1dcdc87d46d7271fc28c53a998a5523bf1%0A*+Document+last+modified%3A+2025-10-27T15%3A55%3A30.000Z%0A%0A%3C%2Fdetails%3E)
