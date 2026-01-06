# DevicePosture

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevicePosture&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `DevicePosture` interface of the [Device Posture API](/en-US/docs/Web/API/Device_Posture_API) represents the device's posture, that is, whether the viewport is in a flat or folded state.

## In this article

- [Instance properties](#instance_properties)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[type](/en-US/docs/Web/API/DevicePosture/type)Read onlyExperimental

Returns the device's current posture.

## [Events](#events)

[change](/en-US/docs/Web/API/DevicePosture/change_event)Experimental

Fires when the device's posture changes.

## [Examples](#examples)

js

```
const postureOutput = document.getElementById("currentPosture");

function reportPostureOutput() {
  // type property returns "continuous" or "folded"
  postureOutput.textContent = `Device posture: ${navigator.devicePosture.type}`;
}

navigator.devicePosture.addEventListener("change", reportPostureOutput);
```

## [Specifications](#specifications)

Specification
[Device Posture API# dom-deviceposture](https://w3c.github.io/device-posture/#dom-deviceposture)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- CSS [device-posture](/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture)`@media` feature
- [Device Posture API](/en-US/docs/Web/API/Device_Posture_API)
- [Origin trial for Foldable APIs](https://developer.chrome.com/blog/foldable-apis-ot) on developer.chrome.com (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DevicePosture/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/deviceposture/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevicePosture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdeviceposture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevicePosture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdeviceposture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa3d19af7e3eeb1c40748c80cd6b5143cfa201c54%0A*+Document+last+modified%3A+2025-02-07T18%3A26%3A29.000Z%0A%0A%3C%2Fdetails%3E)
