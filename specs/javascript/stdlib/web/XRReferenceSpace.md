# XRReferenceSpace

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRReferenceSpace&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The WebXR Device API's `XRReferenceSpace` interface describes the coordinate system for a specific tracked entity or object within the virtual world using a specified tracking behavior. The tracking behavior is defined by the selected [reference space type](#reference_space_types). It expands upon the base class, [XRSpace](/en-US/docs/Web/API/XRSpace), by adding support for several different tracking behaviors as well as to request a new reference space which describes the offset transform between the tracked object and another location in the world.

All reference spaces—with the sole exception being bounded reference spaces—are described using the `XRReferenceSpace` type. Bounded spaces are implemented as [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace) objects. These are special spaces which let you establish a perimeter within which it's "safe" for the viewer to move. For XR systems that allow the user to physically move around, such as those that track movement with a real-world camera, this boundary establishes the edges of the area the user is able to move around in, whether due to physical obstacles or due to limitations of the XR hardware. See the article [Using bounded reference spaces to protect the viewer](/en-US/docs/Web/API/WebXR_Device_API/Bounded_reference_spaces) for more on using boundaries to keep the user from colliding with obstacles both physical and virtual.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Reference space types](#reference_space_types)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

`XRReferenceSpace` inherits the properties of [EventTarget](/en-US/docs/Web/API/EventTarget) but defines no additional properties.

## [Instance methods](#instance_methods)

`XRReferenceSpace` also inherits methods from [EventTarget](/en-US/docs/Web/API/EventTarget) in addition to the following methods.

[getOffsetReferenceSpace()](/en-US/docs/Web/API/XRReferenceSpace/getOffsetReferenceSpace)

Creates and returns a new reference space object as the same type as the one on which you call the method (so, either `XRReferenceSpace` or [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace)). The new reference space can be used to transform a coordinate from the reference space of the object on which the method is called into a different coordinate space. This is useful for positioning objects while rendering, and to perform the needed transforms when changing the viewer's position and/or orientation in 3D space.

## [Events](#events)

[reset](/en-US/docs/Web/API/XRReferenceSpace/reset_event)

The `reset` event is sent to an `XRReferenceSpace` object when the browser detects a discontinuity between the tracked object's origin and the user's environment or location. This can happen, for example, after the user recalibrates their XR device, or if the device automatically adjusts its origin after losing and regaining tracking.

## [Reference space types](#reference_space_types)

The types of reference space are listed in the table below, with brief information about their use cases and which interface is used to implement them.

[bounded-floor](#bounded-floor)

An [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace) similar to the `local` type, except the user is not expected to move outside a predetermined boundary, given by the [boundsGeometry](/en-US/docs/Web/API/XRBoundedReferenceSpace/boundsGeometry) in the returned object.

[local](#local)

An `XRReferenceSpace` tracking space whose native origin is located near the viewer's position at the time the session was created. The exact position depends on the underlying platform and implementation. The user isn't expected to move much if at all beyond their starting position, and tracking is optimized for this use case. For devices with six degrees of freedom (6DoF) tracking, the `local` reference space tries to keep the origin stable relative to the environment.

[local-floor](#local-floor)

An `XRReferenceSpace` similar to the `local` type, except the starting position is placed in a safe location for the viewer to stand, where the value of the y axis is 0 at floor level. If that floor level isn't known, the [user agent](/en-US/docs/Glossary/User_agent) will estimate the floor level. If the estimated floor level is non-zero, the browser is expected to round it such a way as to avoid [fingerprinting](/en-US/docs/Glossary/Fingerprinting) (likely to the nearest centimeter).

[unbounded](#unbounded)

An `XRReferenceSpace` tracking space which allows the user total freedom of movement, possibly over extremely long distances from their origin point. The viewer isn't tracked at all; tracking is optimized for stability around the user's current position, so the native origin may drift as needed to accommodate that need.

[viewer](#viewer)

An `XRReferenceSpace` tracking space whose native origin tracks the viewer's position and orientation. This is used for environments in which the user can physically move around, and is supported by all instances of [XRSession](/en-US/docs/Web/API/XRSession), both immersive and inline, though it's most useful for inline sessions. It's particularly useful when determining the distance between the viewer and an input, or when working with offset spaces. Otherwise, typically, one of the other reference space types will be used more often.

## [Usage notes](#usage_notes)

### [Creating an XRReferenceSpace](#creating_an_xrreferencespace)

There are two situations in which you need to obtain an `XRReferenceSpace`. The first is when you set up your scene and need to obtain a reference space to represent the user's viewpoint on the world for the duration of the [XRSession](/en-US/docs/Web/API/XRSession). To do that, call the [XRSession](/en-US/docs/Web/API/XRSession) method [requestReferenceSpace()](/en-US/docs/Web/API/XRSession/requestReferenceSpace), specifying the reference space type you wish to obtain.

js

```
xrSession.requestReferenceSpace("local").then((refSpace) => {
  xrReferenceSpace = refSpace;
  // …
});
```

The other situation in which you may need to acquire a new reference space is if you need to move the origin to a new position; this is commonly done, for example, when your project allows the user to move through the environment using input devices such as the keyboard, mouse, touchpad, or game controls that are not connected through the XR device. Since the origin will typically be the user's location in the space, you need to change the origin to reflect their movement and any orientation changes they make.

To move or rotate the user's view of the world, you need to change the `XRReferenceSpace` used to represent that viewpoint. However, `XRReferenceSpace` is immutable, so you need to instead create a new reference space representing the changed viewpoint. This is easily done using the [getOffsetReferenceSpace()](/en-US/docs/Web/API/XRReferenceSpace/getOffsetReferenceSpace) method.

js

```
let offsetTransform = new XRRigidTransform(
  { x: 2, y: 0, z: 1 },
  { x: 0, y: 0, z: 0, w: 1 },
);
xrReferenceSpace = xrReferenceSpace.getOffsetReferenceSpace(offsetTransform);
```

This replaces the `XRReferenceSpace` with a new one whose origin and orientation are adjusted to place the new origin at (2, 0, 1) relative to the current origin and rotated given a unit [quaternion](/en-US/docs/Glossary/Quaternion) that orients the space to put the viewer facing straight up relative to the previous world orientation.

### [Geometry](#geometry)

The native origin of any `XRReferenceSpace` is always configured so that +X is considered to be to the right, +Y is upward, and +Z is "backward" or toward the user.

## [Specifications](#specifications)

Specification
[WebXR Device API# xrreferencespace-interface](https://immersive-web.github.io/webxr/#xrreferencespace-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fundamentals of WebXR](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals)
- [Geometry and reference spaces in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Geometry)
- [Viewpoints and viewers: Simulating cameras in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Cameras)
- [Matrix math for the web](/en-US/docs/Web/API/WebGL_API/Matrix_math_for_the_web)
- [Movement, orientation, and motion](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion)
- [Using bounded reference spaces to protect the user](/en-US/docs/Web/API/WebXR_Device_API/Bounded_reference_spaces)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XRReferenceSpace/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrreferencespace/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRReferenceSpace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrreferencespace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRReferenceSpace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrreferencespace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
