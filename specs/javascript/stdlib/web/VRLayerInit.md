# VRLayerInit

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VRLayerInit` dictionary of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents a content layer (an [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement) or [OffscreenCanvas](/en-US/docs/Web/API/OffscreenCanvas)) that you want to present in a VR display.

Note: This dictionary was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

You can retrieve `VRLayerInit` objects using [VRDisplay.getLayers()](/en-US/docs/Web/API/VRDisplay/getLayers), and present them using the [VRDisplay.requestPresent()](/en-US/docs/Web/API/VRDisplay/requestPresent) method.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[VRLayerInit.leftBounds](/en-US/docs/Web/API/VRLayerInit/leftBounds)Deprecated

Defines the left texture bounds of the canvas whose contents will be presented by the [VRDisplay](/en-US/docs/Web/API/VRDisplay).

[VRLayerInit.rightBounds](/en-US/docs/Web/API/VRLayerInit/rightBounds)Deprecated

Defines the right texture bounds of the canvas whose contents will be presented by the [VRDisplay](/en-US/docs/Web/API/VRDisplay).

[VRLayerInit.source](/en-US/docs/Web/API/VRLayerInit/source)Deprecated

Defines the canvas whose contents will be presented by the [VRDisplay](/en-US/docs/Web/API/VRDisplay) when [VRDisplay.submitFrame()](/en-US/docs/Web/API/VRDisplay/submitFrame) is called.

## [Examples](#examples)

js

```
// currently returns an empty array
let layers = vrDisplay.getLayers();

if (navigator.getVRDisplays) {
  console.log("WebVR 1.1 supported");
  // Then get the displays attached to the computer
  navigator.getVRDisplays().then((displays) => {
    // If a display is available, use it to present the scene
    if (displays.length > 0) {
      vrDisplay = displays[0];
      console.log("Display found");
      // Starting the presentation when the button is clicked: It can only be called in response to a user gesture
      btn.addEventListener("click", () => {
        vrDisplay.requestPresent([{ source: canvas }]).then(() => {
          console.log("Presenting to WebVR display");

          // Here it returns an array of VRLayerInit objects
          layers = vrDisplay.getLayers();

          // …
        });
      });
    }
  });
}
```

`VRLayerInit` objects look something like this:

js

```
const init = {
  leftBounds: [
    /* … */
  ],
  rightBounds: [
    /* … */
  ],
  source: canvasReference,
};
```

Note: The `canvasReference` refers to the [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element itself, not the WebGL context associated with the canvas. The other two members are arrays

## [Specifications](#specifications)

This dictionary was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/) that has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/). It is no longer on track to becoming a standard.

Until all browsers have implemented the new [WebXR APIs](/en-US/docs/Web/API/WebXR_Device_API/Fundamentals), it is recommended to rely on frameworks, like [A-Frame](https://aframe.io/), [Babylon.js](https://www.babylonjs.com/), or [Three.js](https://threejs.org/), or a [polyfill](https://github.com/immersive-web/webxr-polyfill), to develop WebXR applications that will work across all browsers. Read [Meta's Porting from WebVR to WebXR](https://developers.meta.com/horizon/documentation/web/port-vr-xr/) guide for more information.

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VRLayerInit/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vrlayerinit/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRLayerInit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvrlayerinit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRLayerInit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvrlayerinit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd22284cbba8b64afd6ad8c965d4ac2c927c59550%0A*+Document+last+modified%3A+2025-07-12T03%3A04%3A39.000Z%0A%0A%3C%2Fdetails%3E)
