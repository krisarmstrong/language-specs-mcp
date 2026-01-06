# DOMMatrixReadOnly

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMMatrixReadOnly&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `DOMMatrixReadOnly` interface represents a read-only 4×4 matrix, suitable for 2D and 3D operations. The [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) interface — which is based upon `DOMMatrixReadOnly`—adds [mutability](https://en.wikipedia.org/wiki/Immutable_object), allowing you to alter the matrix after creating it.

This interface should be available inside [web workers](/en-US/docs/Web/API/Web_Workers_API), though some implementations doesn't allow it yet.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static methods](#static_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMMatrixReadOnly()](/en-US/docs/Web/API/DOMMatrixReadOnly/DOMMatrixReadOnly)

Creates a new `DOMMatrixReadOnly` object.

## [Instance properties](#instance_properties)

This interface doesn't inherit any properties.

[DOMMatrixReadOnly.is2D](/en-US/docs/Web/API/DOMMatrixReadOnly/is2D)Read only

A Boolean flag whose value is `true` if the matrix was initialized as a 2D matrix. If `false`, the matrix is 3D.

[DOMMatrixReadOnly.isIdentity](/en-US/docs/Web/API/DOMMatrixReadOnly/isIdentity)Read only

A Boolean whose value is `true` if the matrix is an [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix).

[m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42, m43, m44](#m11)

Double-precision floating-point values representing each component of a 4×4 matrix, where `m11` through `m14` are the first column, `m21` through `m24` are the second column, and so forth.

[a, b, c, d, e, f](#a)

Double-precision floating-point values representing the components of a 4×4 matrix which are required in order to perform 2D rotations and translations. These are aliases for specific components of a 4×4 matrix, as shown below.

2D3D equivalent`a``m11``b``m12``c``m21``d``m22``e``m41``f``m42`

## [Instance methods](#instance_methods)

This interface doesn't inherit any methods. None of the following methods alter the original matrix.

[DOMMatrixReadOnly.flipX()](/en-US/docs/Web/API/DOMMatrixReadOnly/flipX)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by flipping the source matrix around its X-axis. This is equivalent to multiplying the matrix by `DOMMatrix(-1, 0, 0, 1, 0, 0)`. The original matrix is not modified.

[DOMMatrixReadOnly.flipY()](/en-US/docs/Web/API/DOMMatrixReadOnly/flipY)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by flipping the source matrix around its Y-axis. This is equivalent to multiplying the matrix by `DOMMatrix(1, 0, 0, -1, 0, 0)`. The original matrix is not modified.

[DOMMatrixReadOnly.inverse()](/en-US/docs/Web/API/DOMMatrixReadOnly/inverse)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by inverting the source matrix. The original matrix is not altered.

[DOMMatrixReadOnly.multiply()](/en-US/docs/Web/API/DOMMatrixReadOnly/multiply)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by computing the dot product of the source matrix and the specified matrix. The original matrix is not

[DOMMatrixReadOnly.rotateAxisAngle()](/en-US/docs/Web/API/DOMMatrixReadOnly/rotateAxisAngle)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by rotating the source matrix by the given angle around the specified vector. The original matrix is not modified.

[DOMMatrixReadOnly.rotate()](/en-US/docs/Web/API/DOMMatrixReadOnly/rotate)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by rotating the source matrix around each of its axes by the specified number of degrees. The original matrix is not altered.

[DOMMatrixReadOnly.rotateFromVector()](/en-US/docs/Web/API/DOMMatrixReadOnly/rotateFromVector)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by rotating the source matrix by the angle between the specified vector and `(1, 0)`. The original matrix is not modified.

[DOMMatrixReadOnly.scale()](/en-US/docs/Web/API/DOMMatrixReadOnly/scale)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by scaling the source matrix by the amount specified for each axis, centered on the given origin. By default, the X and Z axes are scaled by `1` and the Y axis has no default scaling value. The default origin is `(0, 0, 0)`. The original matrix is not modified.

[DOMMatrixReadOnly.scale3d()](/en-US/docs/Web/API/DOMMatrixReadOnly/scale3d)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by scaling the source 3D matrix by the given factor along all its axes, centered on the specified origin point. The default origin is `(0, 0, 0)`. The original matrix is not modified.

`DOMMatrixReadOnly.scaleNonUniform()`Deprecated

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by applying the specified scaling on the X, Y, and Z axes, centered at the given origin. By default, the Y and Z axes' scaling factors are both `1`, but the scaling factor for X must be specified. The default origin is `(0, 0, 0)`. The original matrix is not changed.

[DOMMatrixReadOnly.skewX()](/en-US/docs/Web/API/DOMMatrixReadOnly/skewX)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by applying the specified skew transformation to the source matrix along its X-axis. The original matrix is not modified.

[DOMMatrixReadOnly.skewY()](/en-US/docs/Web/API/DOMMatrixReadOnly/skewY)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) created by applying the specified skew transformation to the source matrix along its Y-axis. The original matrix is not modified.

[DOMMatrixReadOnly.toFloat32Array()](/en-US/docs/Web/API/DOMMatrixReadOnly/toFloat32Array)

Returns a new [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) of single-precision floating-point numbers, containing all 16 elements which comprise the matrix.

[DOMMatrixReadOnly.toFloat64Array()](/en-US/docs/Web/API/DOMMatrixReadOnly/toFloat64Array)

Returns a new [Float64Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) of double-precision floating-point numbers, containing all 16 elements which comprise the matrix.

[DOMMatrixReadOnly.toJSON()](/en-US/docs/Web/API/DOMMatrixReadOnly/toJSON)

Returns a JSON representation of the `DOMMatrixReadOnly` object.

[DOMMatrixReadOnly.toString()](/en-US/docs/Web/API/DOMMatrixReadOnly/toString)

Creates and returns a string representation of the matrix in CSS matrix syntax, using the appropriate CSS matrix notation.

[DOMMatrixReadOnly.transformPoint()](/en-US/docs/Web/API/DOMMatrixReadOnly/transformPoint)

Transforms the specified point using the matrix, returning a new [DOMPoint](/en-US/docs/Web/API/DOMPoint) object containing the transformed point. Neither the matrix nor the original point are altered.

[DOMMatrixReadOnly.translate()](/en-US/docs/Web/API/DOMMatrixReadOnly/translate)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) containing a matrix calculated by translating the source matrix using the specified vector. By default, the vector is `(0, 0, 0)`. The original matrix is not changed.

## [Static methods](#static_methods)

[fromFloat32Array()](/en-US/docs/Web/API/DOMMatrixReadOnly/fromFloat32Array_static)

Creates a new `DOMMatrixReadOnly` object given a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) of 6 or 16 single-precision (32-bit) floating-point values.

[fromFloat64Array()](/en-US/docs/Web/API/DOMMatrixReadOnly/fromFloat64Array_static)

Creates a new `DOMMatrixReadOnly` object given a [Float64Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) of 6 or 16 double-precision (64-bit) floating-point values.

[fromMatrix()](/en-US/docs/Web/API/DOMMatrixReadOnly/fromMatrix_static)

Creates a new `DOMMatrixReadOnly` object given an existing matrix or an object which provides the values for its properties.

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMMatrix](https://drafts.fxtf.org/geometry/#DOMMatrix)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The mutable matrix type, [DOMMatrix](/en-US/docs/Web/API/DOMMatrix), which is based on this one.
- The CSS [matrix()](/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix) and [matrix3d()](/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d) functional notation that can be generated from this interface to be used in a CSS [transform](/en-US/docs/Web/CSS/Reference/Properties/transform).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMMatrixReadOnly/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dommatrixreadonly/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMMatrixReadOnly&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdommatrixreadonly%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMMatrixReadOnly%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdommatrixreadonly%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe8ccddf06c8a9d700661ce2239ecaa4bf88a9529%0A*+Document+last+modified%3A+2025-10-27T15%3A46%3A00.000Z%0A%0A%3C%2Fdetails%3E)
