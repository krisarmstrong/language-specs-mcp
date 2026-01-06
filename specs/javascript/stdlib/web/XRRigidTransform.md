# XRRigidTransform

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRRigidTransform&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `XRRigidTransform` is a [WebXR API](/en-US/docs/Web/API/WebXR_Device_API) interface that represents the 3D geometric transform described by a position and orientation.

`XRRigidTransform` is used to specify transforms throughout the WebXR APIs, including:

- The offset and orientation relative to the parent reference space to use when creating a new reference space with [getOffsetReferenceSpace()](/en-US/docs/Web/API/XRReferenceSpace/getOffsetReferenceSpace).
- The [transform](/en-US/docs/Web/API/XRView/transform) of an [XRView](/en-US/docs/Web/API/XRView).
- The [transform](/en-US/docs/Web/API/XRPose/transform) of an [XRPose](/en-US/docs/Web/API/XRPose).
- The [XRReferenceSpaceEvent](/en-US/docs/Web/API/XRReferenceSpaceEvent) event's [transform](/en-US/docs/Web/API/XRReferenceSpaceEvent/transform) property, as found in the [reset](/en-US/docs/Web/API/XRReferenceSpace/reset_event) event received by an [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace).

Using `XRRigidTransform` in these places rather than bare arrays that provide the matrix data has an advantage. It automatically computes the inverse of the transform and even caches it making subsequent requests significantly faster.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[XRRigidTransform()](/en-US/docs/Web/API/XRRigidTransform/XRRigidTransform)

Creates a new `XRRigidTransform` object which represents a transform that applies a specified position and/or orientation.

## [Instance properties](#instance_properties)

[XRRigidTransform.position](/en-US/docs/Web/API/XRRigidTransform/position)Read only

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) specifying a 3-dimensional point, expressed in meters, describing the translation component of the transform. The [w](/en-US/docs/Web/API/DOMPointReadOnly/w) property is always `1.0`.

[XRRigidTransform.orientation](/en-US/docs/Web/API/XRRigidTransform/orientation)Read only

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) which contains a unit quaternion describing the rotational component of the transform. As a unit quaternion, its length is always normalized to `1.0`.

[XRRigidTransform.matrix](/en-US/docs/Web/API/XRRigidTransform/matrix)Read only

Returns the transform matrix in the form of a 16-member [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array). See the section [Matrix format](/en-US/docs/Web/API/XRRigidTransform/matrix#matrix_format) for how the array is used to represent a matrix.

[XRRigidTransform.inverse](/en-US/docs/Web/API/XRRigidTransform/inverse)Read only

Returns a `XRRigidTransform` which is the inverse of this transform. That is, if applied to an object that had been previously transformed by the original transform, it will undo the transform and return the original object.

## [Usage notes](#usage_notes)

When an `XRRigidTransform` is interpreted, the orientation is always applied to the affected object before the position is applied.

## [Example](#example)

This code snippet creates an `XRRigidTransform` to specify the offset and orientation in relation to the current reference space to use when creating a new reference space. It then requests the first animation frame callback by calling the session's [requestAnimationFrame()](/en-US/docs/Web/API/XRSession/requestAnimationFrame) method.

js

```
xrSession.requestReferenceSpace(refSpaceType).then((refSpace) => {
  xrReferenceSpace = refSpace;
  xrReferenceSpace = xrReferenceSpace.getOffsetReferenceSpace(
    new XRRigidTransform(viewerStartPosition, cubeOrientation),
  );
  animationFrameRequestID = xrSession.requestAnimationFrame(drawFrame);
});
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrrigidtransform-interface](https://immersive-web.github.io/webxr/#xrrigidtransform-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/XRRigidTransform/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrrigidtransform/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRRigidTransform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrrigidtransform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRRigidTransform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrrigidtransform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F73b2b6ee411ac094b9fc57dafac6f9c232fc20d9%0A*+Document+last+modified%3A+2024-07-26T02%3A14%3A04.000Z%0A%0A%3C%2Fdetails%3E)
