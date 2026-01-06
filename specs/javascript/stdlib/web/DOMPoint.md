# DOMPoint

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMPoint&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

A `DOMPoint` object represents a 2D or 3D point in a coordinate system; it includes values for the coordinates in up to three dimensions, as well as an optional perspective value. `DOMPoint` is based on [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) but allows its properties' values to be changed.

In general, a positive `x` component represents a position to the right of the origin, a positive `y` component is downward from the origin, and a positive `z` component extends outward from the screen (in other words, toward the user).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Static methods](#static_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMPoint()](/en-US/docs/Web/API/DOMPoint/DOMPoint)

Creates and returns a new `DOMPoint` object given the values of zero or more of its coordinate components and optionally the `w` perspective value. You can also use an existing `DOMPoint` or `DOMPointReadOnly` or an object to create a new point by calling the [DOMPoint.fromPoint()](/en-US/docs/Web/API/DOMPoint/fromPoint_static) static method.

## [Instance properties](#instance_properties)

`DOMPoint` may also inherit properties from its parent, [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly).

[DOMPoint.x](/en-US/docs/Web/API/DOMPoint/x)

The `x` coordinate of the `DOMPoint`.

[DOMPoint.y](/en-US/docs/Web/API/DOMPoint/y)

The `y` coordinate of the `DOMPoint`.

[DOMPoint.z](/en-US/docs/Web/API/DOMPoint/z)

The `z` coordinate of the `DOMPoint`.

[DOMPoint.w](/en-US/docs/Web/API/DOMPoint/w)

The perspective value of the `DOMPoint`.

## [Instance methods](#instance_methods)

`DOMPoint` inherits instance methods from its parent, [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly).

## [Static methods](#static_methods)

`DOMPoint` may also inherit static methods from its parent, [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly).

[DOMPoint.fromPoint()](/en-US/docs/Web/API/DOMPoint/fromPoint_static)

Creates a new mutable `DOMPoint` object given an existing point (or an object containing matching properties), which provides the values for its properties.

## [Examples](#examples)

In the [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API), `DOMPointReadOnly` values represent positions and orientations. In the following snippet, the pose of the XR device (such as a VR headset or phone with AR capabilities) can be retrieved by calling using [XRFrame.getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) during an [XRSession](/en-US/docs/Web/API/XRSession) animation frame, then accessing the resulting [XRPose](/en-US/docs/Web/API/XRPose)'s [transform](/en-US/docs/Web/API/XRPose/transform) property, which contains two `DOMPointReadOnly` attributes: [position](/en-US/docs/Web/API/XRRigidTransform/position) as a vector and [orientation](/en-US/docs/Web/API/XRRigidTransform/orientation) as a quaternion.

js

```
function onXRFrame(time, xrFrame) {
  let viewerPose = xrFrame.getViewerPose(xrReferenceSpace);

  if (viewerPose) {
    let position = viewerPose.transform.position;
    let orientation = viewerPose.transform.orientation;

    console.log(
      `XR Viewer Position: {x: ${roundToTwo(position.x)}, y: ${roundToTwo(
        position.y,
      )}, z: ${roundToTwo(position.z)}`,
    );

    console.log(
      `XR Viewer Orientation: {x: ${roundToTwo(orientation.x)}, y: ${roundToTwo(
        orientation.y,
      )}, z: ${roundToTwo(orientation.z)}, w: ${roundToTwo(orientation.w)}`,
    );
  }
}
```

## [Specifications](#specifications)

Specification
[Geometry Interfaces Module Level 1# DOMPoint](https://drafts.fxtf.org/geometry/#DOMPoint)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [DOMRect](/en-US/docs/Web/API/DOMRect)
- [DOMMatrix](/en-US/docs/Web/API/DOMMatrix)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DOMPoint/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dompoint/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMPoint&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdompoint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMPoint%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdompoint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3652cfa9c036cf3ceebb1384bdc7edfd549251f3%0A*+Document+last+modified%3A+2024-10-08T19%3A28%3A25.000Z%0A%0A%3C%2Fdetails%3E)
