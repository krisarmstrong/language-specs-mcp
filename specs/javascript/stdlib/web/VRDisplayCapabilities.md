# VRDisplayCapabilities

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VRDisplayCapabilities` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) describes the capabilities of a [VRDisplay](/en-US/docs/Web/API/VRDisplay) — its features can be used to perform VR device capability tests, for example can it return position information.

Note: This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

This interface is accessible through the [VRDisplay.capabilities](/en-US/docs/Web/API/VRDisplay/capabilities) property.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[VRDisplayCapabilities.canPresent](/en-US/docs/Web/API/VRDisplayCapabilities/canPresent)DeprecatedRead onlyNon-standard

Returns a boolean value stating whether the VR display is capable of presenting content (e.g., through an HMD).

[VRDisplayCapabilities.hasExternalDisplay](/en-US/docs/Web/API/VRDisplayCapabilities/hasExternalDisplay)DeprecatedRead onlyNon-standard

Returns a boolean value stating whether the VR display is separate from the device's primary display.

[VRDisplayCapabilities.hasOrientation](/en-US/docs/Web/API/VRDisplayCapabilities/hasOrientation)DeprecatedRead onlyNon-standard

Returns a boolean value stating whether the VR display can track and return orientation information.

[VRDisplayCapabilities.hasPosition](/en-US/docs/Web/API/VRDisplayCapabilities/hasPosition)DeprecatedRead onlyNon-standard

Returns a boolean value stating whether the VR display can track and return position information.

[VRDisplayCapabilities.maxLayers](/en-US/docs/Web/API/VRDisplayCapabilities/maxLayers)DeprecatedRead onlyNon-standard

Returns a number indicating the maximum number of [VRLayerInit](/en-US/docs/Web/API/VRLayerInit)s that the VR display can present at once (e.g., the maximum length of the array that [VRDisplay.requestPresent()](/en-US/docs/Web/API/VRDisplay/requestPresent) can accept.)

## [Examples](#examples)

js

```
function reportDisplays() {
  navigator.getVRDisplays().then((displays) => {
    displays.forEach((display, i) => {
      const cap = display.capabilities;
      // cap is a VRDisplayCapabilities object
      const listItem = document.createElement("li");
      listItem.innerText = `
VR Display ID: ${display.displayId}
VR Display Name: ${display.displayName}
Display can present content: ${cap.canPresent}
Display is separate from the computer's main display: ${cap.hasExternalDisplay}
Display can return position info: ${cap.hasPosition}
Display can return orientation info: ${cap.hasOrientation}
Display max layers: ${cap.maxLayers}`;
      listItem.insertBefore(
        document.createElement("strong"),
        listItem.firstChild,
      ).textContent = `Display ${i + 1}`;
      list.appendChild(listItem);
    });
  });
}
```

## [Specifications](#specifications)

This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/) that has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/). It is no longer on track to becoming a standard.

Until all browsers have implemented the new [WebXR APIs](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals), it is recommended to rely on frameworks, like [A-Frame](https://aframe.io/), [Babylon.js](https://www.babylonjs.com/), or [Three.js](https://threejs.org/), or a [polyfill](https://github.com/immersive-web/webxr-polyfill), to develop WebXR applications that will work across all browsers. Read [Meta's Porting from WebVR to WebXR](https://developers.meta.com/horizon/documentation/web/port-vr-xr/) guide for more information.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VRDisplayCapabilities/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vrdisplaycapabilities/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRDisplayCapabilities&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvrdisplaycapabilities%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRDisplayCapabilities%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvrdisplaycapabilities%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
