# XRFrame

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRFrame&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

A [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)`XRFrame` object is passed into the [requestAnimationFrame()](/en-US/docs/Web/API/XRSession/requestAnimationFrame) callback function and provides access to the information needed in order to render a single frame of animation for an [XRSession](/en-US/docs/Web/API/XRSession) describing a VR or AR scene. Events which communicate the tracking state of objects also provide an `XRFrame` reference as part of their structure.

In addition to providing a reference to the [XRSession](/en-US/docs/Web/API/XRSession) for which this frame is to be rendered, the [getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) method is provided to obtain the [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) describing the viewer's position and orientation in space, and [getPose()](/en-US/docs/Web/API/XRFrame/getPose) can be used to create an [XRPose](/en-US/docs/Web/API/XRPose) describing the relative position of one [XRSpace](/en-US/docs/Web/API/XRSpace) relative to another.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[session](/en-US/docs/Web/API/XRFrame/session)Read onlyExperimental

The [XRSession](/en-US/docs/Web/API/XRSession) that for which this `XRFrame` describes the tracking details for all objects. The information about a specific object can be obtained by calling one of the methods on the object.

[trackedAnchors](/en-US/docs/Web/API/XRFrame/trackedAnchors)Read onlyExperimental

An [XRAnchorSet](/en-US/docs/Web/API/XRAnchorSet) containing all anchors still tracked in the frame.

## [Instance methods](#instance_methods)

[createAnchor()](/en-US/docs/Web/API/XRFrame/createAnchor)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to a free-floating [XRAnchor](/en-US/docs/Web/API/XRAnchor) object.

[fillJointRadii()](/en-US/docs/Web/API/XRFrame/fillJointRadii)Experimental

Populates a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) with radii for a list of hand joint spaces. Returns `true` if successful for all spaces.

[fillPoses()](/en-US/docs/Web/API/XRFrame/fillPoses)Experimental

Populates a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) with the matrices of the poses, relative to a given base space. Returns `true` if all spaces have a valid pose.

[getDepthInformation()](/en-US/docs/Web/API/XRFrame/getDepthInformation)Experimental

Returns an [XRCPUDepthInformation](/en-US/docs/Web/API/XRCPUDepthInformation) object containing CPU depth information for the frame.

[getHitTestResults()](/en-US/docs/Web/API/XRFrame/getHitTestResults)Experimental

Returns an array of [XRHitTestResult](/en-US/docs/Web/API/XRHitTestResult) objects containing hit test results for a given [XRHitTestSource](/en-US/docs/Web/API/XRHitTestSource).

[getHitTestResultsForTransientInput()](/en-US/docs/Web/API/XRFrame/getHitTestResultsForTransientInput)Experimental

Returns an array of [XRTransientInputHitTestResult](/en-US/docs/Web/API/XRTransientInputHitTestResult) objects containing hit test results for a given [XRTransientInputHitTestSource](/en-US/docs/Web/API/XRTransientInputHitTestSource).

[getJointPose()](/en-US/docs/Web/API/XRFrame/getJointPose)Experimental

Returns an [XRJointPose](/en-US/docs/Web/API/XRJointPose) object providing the pose of a hand joint (see [XRHand](/en-US/docs/Web/API/XRHand)) relative to a given base space.

[getLightEstimate()](/en-US/docs/Web/API/XRFrame/getLightEstimate)Experimental

Returns an [XRLightEstimate](/en-US/docs/Web/API/XRLightEstimate) object containing estimated lighting values for an [XRLightProbe](/en-US/docs/Web/API/XRLightProbe).

[getPose()](/en-US/docs/Web/API/XRFrame/getPose)Experimental

Returns an [XRPose](/en-US/docs/Web/API/XRPose) object representing the spatial relationship between the two specified [XRSpace](/en-US/docs/Web/API/XRSpace) objects.

[getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose)Experimental

Returns an [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) describing the viewer's position and orientation in a given [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace).

## [Specifications](#specifications)

Specification
[WebXR Device API# xrframe-interface](https://immersive-web.github.io/webxr/#xrframe-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)
- [Spatial tracking in WebXR](/en-US/docs/Web/API/WebXR_Device_API/Spatial_tracking)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRFrame/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrframe/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRFrame&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRFrame%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5b33acd44e7bb9c7be2efc75ba9a04b8bf8b2b2%0A*+Document+last+modified%3A+2023-02-18T09%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E)
