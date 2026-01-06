# VRPose

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VRPose` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents the state of a VR sensor at a given timestamp (which includes orientation, position, velocity, and acceleration information).

Note: This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

This interface is accessible through the [VRDisplay.getPose()](/en-US/docs/Web/API/VRDisplay/getPose) and [VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData) methods. [VRDisplay.getPose()](/en-US/docs/Web/API/VRDisplay/getPose) is deprecated.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[VRPose.position](/en-US/docs/Web/API/VRPose/position)DeprecatedRead onlyNon-standard

Returns the position of the [VRDisplay](/en-US/docs/Web/API/VRDisplay) at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp) as a 3D vector

[VRPose.linearVelocity](/en-US/docs/Web/API/VRPose/linearVelocity)DeprecatedRead onlyNon-standard

Returns the linear velocity of the [VRDisplay](/en-US/docs/Web/API/VRDisplay) at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp), in meters per second.

[VRPose.linearAcceleration](/en-US/docs/Web/API/VRPose/linearAcceleration)DeprecatedRead onlyNon-standard

Returns the linear acceleration of the [VRDisplay](/en-US/docs/Web/API/VRDisplay) at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp), in meters per second per second.

[VRPose.orientation](/en-US/docs/Web/API/VRPose/orientation)DeprecatedRead onlyNon-standard

Returns the orientation of the sensor at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp), as a quaternion value.

[VRPose.angularVelocity](/en-US/docs/Web/API/VRPose/angularVelocity)DeprecatedRead onlyNon-standard

Returns the angular velocity of the [VRDisplay](/en-US/docs/Web/API/VRDisplay) at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp), in radians per second.

[VRPose.angularAcceleration](/en-US/docs/Web/API/VRPose/angularAcceleration)DeprecatedRead onlyNon-standard

Returns the angular acceleration of the [VRDisplay](/en-US/docs/Web/API/VRDisplay) at the current [VRFrameData.timestamp](/en-US/docs/Web/API/VRFrameData/timestamp), in meters per second per second.

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

 This page was last modified on ⁨Aug 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VRPose/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vrpose/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRPose&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvrpose%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRPose%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvrpose%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F94ffd165232b5205418f8aa57127ee0854421db2%0A*+Document+last+modified%3A+2025-08-14T10%3A08%3A03.000Z%0A%0A%3C%2Fdetails%3E)
