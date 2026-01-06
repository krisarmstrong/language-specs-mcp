# XRPose

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRPose&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

`XRPose` is a [WebXR API](/en-US/docs/Web/API/WebXR_Device_API) interface representing a position and orientation in the 3D space, relative to the [XRSpace](/en-US/docs/Web/API/XRSpace) within which it resides. The `XRSpace`—which is either an [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace) or an [XRBoundedReferenceSpace](/en-US/docs/Web/API/XRBoundedReferenceSpace)—defines the coordinate system used for the pose and, in the case of an [XRViewerPose](/en-US/docs/Web/API/XRViewerPose), its underlying views.

To obtain the `XRPose` for the `XRSpace` used as the local coordinate system of an object, call [XRFrame.getPose()](/en-US/docs/Web/API/XRFrame/getPose), specifying that local `XRSpace` and the space to which you wish to convert:

js

```
thePose = xrFrame.getPose(localSpace, baseSpace);
```

The pose for a viewer (or camera) is represented by the [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) subclass of `XRPose`. This is obtained using [XRFrame.getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) instead of `getPose()`, specifying a reference space which has been adjusted to position and orient the node to provide the desired viewing position and angle:

js

```
viewerPose = xrFrame.getViewerPose(adjReferenceSpace);
```

Here, `adjReferenceSpace` is a reference space which has been updated using the base frame of reference for the frame and any adjustments needed to position the viewer based on movement or rotation which is being supplied from a source other than the XR device, such as keyboard or mouse inputs.

See the article [Movement, orientation, and motion](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion) for further details and an example with thorough explanations of what's going on.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[XRPose.angularVelocity](/en-US/docs/Web/API/XRPose/angularVelocity)Read only

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) describing the angular velocity in radians per second relative to the base [XRSpace](/en-US/docs/Web/API/XRSpace).

[XRPose.emulatedPosition](/en-US/docs/Web/API/XRPose/emulatedPosition)Read only

A Boolean value which is `false` if the position and orientation given by [transform](/en-US/docs/Web/API/XRPose/transform) is obtained directly from a full six degree of freedom (6DoF) XR device (that is, a device which tracks not only the pitch, yaw, and roll of the head but also the forward, backward, and side-to-side motion of the viewer). If any component of the `transform` is computed or created artificially (such as by using mouse or keyboard controls to move through space), this value is instead `true`, indicating that the `transform` is in part emulated in software.

[XRPose.linearVelocity](/en-US/docs/Web/API/XRPose/linearVelocity)Read only

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) describing the linear velocity in meters per second relative to the base [XRSpace](/en-US/docs/Web/API/XRSpace).

[XRPose.transform](/en-US/docs/Web/API/XRPose/transform)Read only

A [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform) which provides the position and orientation of the pose relative to the base [XRSpace](/en-US/docs/Web/API/XRSpace).

## [Specifications](#specifications)

Specification
[WebXR Device API# xrpose-interface](https://immersive-web.github.io/webxr/#xrpose-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)
- [XRFrame.getPose()](/en-US/docs/Web/API/XRFrame/getPose)
- [XRViewerPose](/en-US/docs/Web/API/XRViewerPose)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRPose/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrpose/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRPose&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrpose%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRPose%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrpose%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
