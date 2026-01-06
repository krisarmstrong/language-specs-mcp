# VRFrameData

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VRFrameData` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents all the information needed to render a single frame of a VR scene; constructed by [VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData).

Note: This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[VRFrameData()](/en-US/docs/Web/API/VRFrameData/VRFrameData)DeprecatedNon-standard

Creates a `VRFrameData` object instance.

## [Instance properties](#instance_properties)

[VRFrameData.leftProjectionMatrix](/en-US/docs/Web/API/VRFrameData/leftProjectionMatrix)DeprecatedRead onlyNon-standard

A [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) representing a 4x4 matrix that describes the projection to be used for the left eye's rendering.

[VRFrameData.leftViewMatrix](/en-US/docs/Web/API/VRFrameData/leftViewMatrix)DeprecatedRead onlyNon-standard

A [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) representing a 4x4 matrix that describes the view transform to be used for the left eye's rendering.

[VRFrameData.pose](/en-US/docs/Web/API/VRFrameData/pose)DeprecatedRead onlyNon-standard

The [VRPose](/en-US/docs/Web/API/VRPose) of the [VRDisplay](/en-US/docs/Web/API/VRDisplay) at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp).

[VRFrameData.rightProjectionMatrix](/en-US/docs/Web/API/VRFrameData/rightProjectionMatrix)DeprecatedRead onlyNon-standard

A [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) representing a 4x4 matrix that describes the projection to be used for the right eye's rendering.

[VRFrameData.rightViewMatrix](/en-US/docs/Web/API/VRFrameData/rightViewMatrix)DeprecatedRead onlyNon-standard

A [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) representing a 4x4 matrix that describes the view transform to be used for the right eye's rendering.

[VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp)DeprecatedRead onlyNon-standard

A constantly increasing timestamp value representing the time a frame update occurred.

## [Examples](#examples)

See [VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData#examples) for example code.

## [Specifications](#specifications)

This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/) that has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/). It is no longer on track to becoming a standard.

Until all browsers have implemented the new [WebXR APIs](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals), it is recommended to rely on frameworks, like [A-Frame](https://aframe.io/), [Babylon.js](https://www.babylonjs.com/), or [Three.js](https://threejs.org/), or a [polyfill](https://github.com/immersive-web/webxr-polyfill), to develop WebXR applications that will work across all browsers. Read [Meta's Porting from WebVR to WebXR](https://developers.meta.com/horizon/documentation/web/port-vr-xr/) guide for more information.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 20, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VRFrameData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vrframedata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRFrameData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvrframedata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRFrameData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvrframedata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fce094c10e0b71ff594e013d459b9c29110a6442a%0A*+Document+last+modified%3A+2024-09-20T13%3A18%3A15.000Z%0A%0A%3C%2Fdetails%3E)
