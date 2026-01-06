# VREyeParameters

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VREyeParameters` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents all the information required to correctly render a scene for a given eye, including field of view information.

Note: This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

This interface is accessible through the [VRDisplay.getEyeParameters()](/en-US/docs/Web/API/VRDisplay/getEyeParameters) method.

Warning: The values in this interface should not be used to compute view or projection matrices. In order to ensure the widest possible hardware compatibility use the matrices provided by [VRFrameData](/en-US/docs/Web/API/VRFrameData).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[VREyeParameters.offset](/en-US/docs/Web/API/VREyeParameters/offset)DeprecatedRead onlyNon-standard

Represents the offset from the center point between the user's eyes to the center of the eye, measured in meters.

[VREyeParameters.fieldOfView](/en-US/docs/Web/API/VREyeParameters/fieldOfView)DeprecatedRead onlyNon-standard

Describes the current field of view for the eye, which can vary as the user adjusts their interpupillary distance (IPD).

[VREyeParameters.maximumFieldOfView](/en-US/docs/Web/API/VREyeParameters/maximumFieldOfView)DeprecatedRead onlyNon-standard

Describes the maximum supported field of view for the current eye.

[VREyeParameters.minimumFieldOfView](/en-US/docs/Web/API/VREyeParameters/minimumFieldOfView)DeprecatedRead onlyNon-standard

Describes the minimum supported field of view for the current eye.

[VREyeParameters.renderWidth](/en-US/docs/Web/API/VREyeParameters/renderWidth)DeprecatedRead onlyNon-standard

Describes the recommended render target width of each eye viewport, in pixels.

[VREyeParameters.renderHeight](/en-US/docs/Web/API/VREyeParameters/renderHeight)DeprecatedRead onlyNon-standard

Describes the recommended render target height of each eye viewport, in pixels.

## [Examples](#examples)

js

```
navigator.getVRDisplays().then((displays) => {
  // If a display is available, use it to present the scene
  vrDisplay = displays[0];
  console.log("Display found");
  // Starting the presentation when the button is clicked:
  //   It can only be called in response to a user gesture
  btn.addEventListener("click", () => {
    vrDisplay.requestPresent([{ source: canvas }]).then(() => {
      console.log("Presenting to WebVR display");

      // Set the canvas size to the size of the vrDisplay viewport

      const leftEye = vrDisplay.getEyeParameters("left");
      const rightEye = vrDisplay.getEyeParameters("right");

      canvas.width = Math.max(leftEye.renderWidth, rightEye.renderWidth) * 2;
      canvas.height = Math.max(leftEye.renderHeight, rightEye.renderHeight);

      drawVRScene();
    });
  });
});
```

## [Specifications](#specifications)

This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/) that has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/). It is no longer on track to becoming a standard.

Until all browsers have implemented the new [WebXR APIs](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals), it is recommended to rely on frameworks, like [A-Frame](https://aframe.io/), [Babylon.js](https://www.babylonjs.com/), or [Three.js](https://threejs.org/), or a [polyfill](https://github.com/immersive-web/webxr-polyfill), to develop WebXR applications that will work across all browsers. Read [Meta's Porting from WebVR to WebXR](https://developers.meta.com/horizon/documentation/web/port-vr-xr/) guide for more information.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 20, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VREyeParameters/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vreyeparameters/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVREyeParameters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvreyeparameters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVREyeParameters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvreyeparameters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fce094c10e0b71ff594e013d459b9c29110a6442a%0A*+Document+last+modified%3A+2024-09-20T13%3A18%3A15.000Z%0A%0A%3C%2Fdetails%3E)
