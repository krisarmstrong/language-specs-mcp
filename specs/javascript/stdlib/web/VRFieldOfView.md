# VRFieldOfView

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `VRFieldOfView` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents a field of view defined by 4 different degree values describing the view from a center point.

Note: This interface was part of the old [WebVR API](https://immersive-web.github.io/webvr/spec/1.1/). It has been superseded by the [WebXR Device API](https://immersive-web.github.io/webxr/).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[VRFieldOfView.upDegrees](/en-US/docs/Web/API/VRFieldOfView/upDegrees)DeprecatedRead onlyNon-standard

The number of degrees upwards that the field of view extends in.

[VRFieldOfView.rightDegrees](/en-US/docs/Web/API/VRFieldOfView/rightDegrees)DeprecatedRead onlyNon-standard

The number of degrees to the right that the field of view extends in.

[VRFieldOfView.downDegrees](/en-US/docs/Web/API/VRFieldOfView/downDegrees)DeprecatedRead onlyNon-standard

The number of degrees downwards that the field of view extends in.

[VRFieldOfView.leftDegrees](/en-US/docs/Web/API/VRFieldOfView/leftDegrees)DeprecatedRead onlyNon-standard

The number of degrees to the left that the field of view extends in.

## [Examples](#examples)

js

```
const info = document.querySelector("p");
const list = document.querySelector("ul");
let vrDisplay;

if (navigator.getVRDisplays) {
  reportFieldOfView();
} else {
  info.textContent = "WebVR API not supported by this browser.";
}

function reportFieldOfView() {
  navigator.getVRDisplays().then((displays) => {
    vrDisplay = displays[0];
    const lEye = vrDisplay.getEyeParameters("left");
    const rEye = vrDisplay.getEyeParameters("right");
    // lEye and rEye are VREyeParameters objects

    const lFOV = lEye.fieldOfView;
    const rFOV = rEye.fieldOfView;
    // lFOV and rFOV are VRFieldOfView objects

    const listitem1 = document.createElement("li");
    const listitem2 = document.createElement("li");

    listitem1.innerText = `
Offset: ${lEye.offset}
Render width: ${lEye.renderWidth}
Render height: ${lEye.renderHeight}
Up degrees: ${lFOV.upDegrees}
Right degrees: ${lFOV.rightDegrees}
Down degrees: ${lFOV.downDegrees}
Left degrees: ${lFOV.leftDegrees}`;
    listitem1.insertBefore(
      document.createElement("strong"),
      listitem1.firstChild,
    ).textContent = "Left eye parameters";

    listitem2.innerText = `
Offset: ${rEye.offset}
Render width: ${rEye.renderWidth}
Render height: ${rEye.renderHeight}
Up degrees: ${rFOV.upDegrees}
Right degrees: ${rFOV.rightDegrees}
Down degrees: ${rFOV.downDegrees}
Left degrees: ${rFOV.leftDegrees}`;
    listitem2.insertBefore(
      document.createElement("strong"),
      listitem2.firstChild,
    ).textContent = "Right eye parameters";

    list.appendChild(listitem1);
    list.appendChild(listitem2);
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

 This page was last modified on ⁨Sep 20, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VRFieldOfView/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/vrfieldofview/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRFieldOfView&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvrfieldofview%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVRFieldOfView%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvrfieldofview%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fce094c10e0b71ff594e013d459b9c29110a6442a%0A*+Document+last+modified%3A+2024-09-20T13%3A18%3A15.000Z%0A%0A%3C%2Fdetails%3E)
