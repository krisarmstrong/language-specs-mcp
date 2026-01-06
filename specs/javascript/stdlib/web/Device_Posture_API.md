# Device Posture API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_Posture_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Device Posture API allows developers to create user interfaces that adapt to a foldable device's posture and respond to posture changes.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [CSS features](#css_features)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Foldable devices present unique design challenges to developers — they can be used like a regular flat screen or like a book. In addition, some of them feature a single folded screen, and some of them feature two screens with a hinged join in the middle. Care must be taken to ensure that content is not hidden by the physical join, or rendered difficult to read due to close proximity to the central fold.

The Device Posture API defines postures, which indicate the current physical folding state of a device. The current available postures are:

[continuous](#continuous)

Indicates a flat screen state. Foldable devices are `continuous` while they are flat; either fully opened or fully closed. Non-foldable devices are considered flat and therefore always `continuous` — this includes seamless curved displays and standard desktop, laptop, tablet, and mobile screens. 

[folded](#folded)

Indicates a folded screen state. Foldable devices are `folded` while used in a book or laptop posture. 

The Device Posture API includes features enabling you to run scripts and vary layouts depending on current device posture and posture changes.

## [CSS features](#css_features)

[device-posture](/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture)`@media` feature

Detects the device's current posture.

## [Interfaces](#interfaces)

[DevicePosture](/en-US/docs/Web/API/DevicePosture)

Represents the device's posture, providing access to the current posture `type` and a `change` event that fires on posture change.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.devicePosture](/en-US/docs/Web/API/Navigator/devicePosture)

The entry point for the Device Posture API — returns the browser's `DevicePosture` object.

## [Examples](#examples)

You can find a complete example showing all of the features in action in the [Device Posture API demo](https://mdn.github.io/dom-examples/device-posture-api/).

If possible, you should view this on a foldable device. Current browser developer tools enable emulating foldable devices, but don't include emulation of partially folded devices — only fully open or closed — so they will always return `continuous`.

## [Specifications](#specifications)

Specification
[Device Posture API# dom-deviceposture](https://w3c.github.io/device-posture/#dom-deviceposture)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Origin trial for Foldable APIs](https://developer.chrome.com/blog/foldable-apis-ot) on developer.chrome.com (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Device_Posture_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/device_posture_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_Posture_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdevice_posture_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_Posture_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdevice_posture_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F01e8b5077df6d79e52f2521dfbe734e0923d1fc4%0A*+Document+last+modified%3A+2025-02-08T02%3A59%3A29.000Z%0A%0A%3C%2Fdetails%3E)
