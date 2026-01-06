# VRDisplay

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VRDisplay` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents any VR device supported by this API. It includes generic information such as device IDs and descriptions, as well as methods for starting to present a VR scene, retrieving eye parameters and display capabilities, and other important functionality.

Note: This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

An array of all connected VR Devices can be returned by invoking the [Navigator.getVRDisplays()](/en-US/docs/Web/API/Navigator/getVRDisplays) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[VRDisplay.capabilities](/en-US/docs/Web/API/VRDisplay/capabilities)Read onlyDeprecatedNon-standard

Returns a [VRDisplayCapabilities](/en-US/docs/Web/API/VRDisplayCapabilities) object that indicates the various capabilities of the `VRDisplay`.

[VRDisplay.depthFar](/en-US/docs/Web/API/VRDisplay/depthFar)DeprecatedNon-standard

Gets and sets the z-depth defining the far plane of the [eye view frustum](https://en.wikipedia.org/wiki/Viewing_frustum), i.e., the furthest viewable boundary of the scene.

[VRDisplay.depthNear](/en-US/docs/Web/API/VRDisplay/depthNear)DeprecatedNon-standard

Gets and sets the z-depth defining the near plane of the [eye view frustum](https://en.wikipedia.org/wiki/Viewing_frustum), i.e., the nearest viewable boundary of the scene.

[VRDisplay.displayId](/en-US/docs/Web/API/VRDisplay/displayId)Read onlyDeprecatedNon-standard

Returns an identifier for this particular VRDisplay, which is also used as an association point in the [Gamepad API](/en-US/docs/Web/API/Gamepad_API) (see [Gamepad.displayId](/en-US/docs/Web/API/Gamepad/displayId)).

[VRDisplay.displayName](/en-US/docs/Web/API/VRDisplay/displayName)Read onlyDeprecatedNon-standard

Returns a human-readable name to identify the `VRDisplay`.

[VRDisplay.isConnected](/en-US/docs/Web/API/VRDisplay/isConnected)Read onlyDeprecatedNon-standard

Returns a boolean value indicating whether the `VRDisplay` is connected to the computer.

[VRDisplay.isPresenting](/en-US/docs/Web/API/VRDisplay/isPresenting)Read onlyDeprecatedNon-standard

Returns a boolean value indicating whether the `VRDisplay` is currently having content presented through it.

[VRDisplay.stageParameters](/en-US/docs/Web/API/VRDisplay/stageParameters)Read onlyDeprecatedNon-standard

Returns a [VRStageParameters](/en-US/docs/Web/API/VRStageParameters) object containing room-scale parameters, if the `VRDisplay` is capable of supporting room-scale experiences.

## [Instance methods](#instance_methods)

[VRDisplay.getEyeParameters()](/en-US/docs/Web/API/VRDisplay/getEyeParameters)DeprecatedNon-standard

Returns the [VREyeParameters](/en-US/docs/Web/API/VREyeParameters) object containing the eye parameters for the specified eye.

[VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData)DeprecatedNon-standard

Accepts a [VRFrameData](/en-US/docs/Web/API/VRFrameData) object and populates it with the information required to render the current frame.

[VRDisplay.getImmediatePose()](/en-US/docs/Web/API/VRDisplay/getImmediatePose)DeprecatedNon-standard

Returns a [VRPose](/en-US/docs/Web/API/VRPose) object defining the current pose of the `VRDisplay`, with no prediction applied. This is no longer needed, and has been removed from the spec.

[VRDisplay.getLayers()](/en-US/docs/Web/API/VRDisplay/getLayers)DeprecatedNon-standard

Returns the layers currently being presented by the `VRDisplay`.

[VRDisplay.getPose()](/en-US/docs/Web/API/VRDisplay/getPose)DeprecatedNon-standard

Returns a [VRPose](/en-US/docs/Web/API/VRPose) object defining the future predicted pose of the `VRDisplay` as it will be when the current frame is actually presented. This method is deprecated — instead, you should use [VRDisplay.getFrameData()](/en-US/docs/Web/API/VRDisplay/getFrameData), which also provides a [VRPose](/en-US/docs/Web/API/VRPose) object.

[VRDisplay.resetPose()](/en-US/docs/Web/API/VRDisplay/resetPose)DeprecatedNon-standard

Resets the pose for this `VRDisplay`, treating its current [VRPose.position](/en-US/docs/Web/API/VRPose/position) and [VRPose.orientation](/en-US/docs/Web/API/VRPose/orientation) as the "origin/zero" values.

[VRDisplay.cancelAnimationFrame()](/en-US/docs/Web/API/VRDisplay/cancelAnimationFrame)DeprecatedNon-standard

A special implementation of [Window.cancelAnimationFrame](/en-US/docs/Web/API/Window/cancelAnimationFrame) that allows callbacks registered with [VRDisplay.requestAnimationFrame()](/en-US/docs/Web/API/VRDisplay/requestAnimationFrame) to be unregistered.

[VRDisplay.requestAnimationFrame()](/en-US/docs/Web/API/VRDisplay/requestAnimationFrame)DeprecatedNon-standard

A special implementation of [Window.requestAnimationFrame](/en-US/docs/Web/API/Window/requestAnimationFrame) containing a callback function that will be called every time a new frame of the `VRDisplay` presentation is rendered.

[VRDisplay.requestPresent()](/en-US/docs/Web/API/VRDisplay/requestPresent)DeprecatedNon-standard

Starts the `VRDisplay` presenting a scene.

[VRDisplay.exitPresent()](/en-US/docs/Web/API/VRDisplay/exitPresent)DeprecatedNon-standard

Stops the `VRDisplay` presenting a scene.

[VRDisplay.submitFrame()](/en-US/docs/Web/API/VRDisplay/submitFrame)DeprecatedNon-standard

Captures the current state of the [VRLayerInit](/en-US/docs/Web/API/VRLayerInit) currently being presented and displays it on the `VRDisplay`.

## [Examples](#examples)

js

```
if (navigator.getVRDisplays) {
  console.log("WebVR 1.1 supported");
  // Then get the displays attached to the computer
  navigator.getVRDisplays().then((displays) => {
    // If a display is available, use it to present the scene
    if (displays.length > 0) {
      vrDisplay = displays[0];
      // Now we have our VRDisplay object and can do what we want with it
    }
  });
}
```

Note: You can see this complete code at [raw-webgl-example](https://github.com/mdn/webvr-tests/blob/main/webvr/raw-webgl-example/webgl-demo.js).

## [Specifications](#specifications)

This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/#interface-vrdisplay) that has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/). It is no longer on track to becoming a standard.

Until all browsers have implemented the new [WebXR APIs](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals), it is recommended to rely on frameworks, like [A-Frame](https://aframe.io/), [Babylon.js](https://www.babylonjs.com/), or [Three.js](https://threejs.org/), or a [polyfill](https://github.com/immersive-web/webxr-polyfill), to develop WebXR applications that will work across all browsers. Read [Meta's Porting from WebVR to WebXR](https://developers.meta.com/horizon/documentation/web/port-vr-xr/) guide for more information.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VRDisplay/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vrdisplay/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRDisplay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvrdisplay%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRDisplay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvrdisplay%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
