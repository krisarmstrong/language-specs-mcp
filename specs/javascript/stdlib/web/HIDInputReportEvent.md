# HIDInputReportEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDInputReportEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Shared Web Workers](/en-US/docs/Web/API/SharedWorkerGlobalScope).

The `HIDInputReportEvent` interface of the [WebHID API](/en-US/docs/Web/API/WebHID_API) is passed to [inputreport](/en-US/docs/Web/API/HIDDevice/inputreport_event) event of `HIDDevice` when an input report is received from any associated HID device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from [Event](/en-US/docs/Web/API/Event).

[HIDInputReportEvent.data](/en-US/docs/Web/API/HIDInputReportEvent/data)Read onlyExperimental

A [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) containing the data from the input report, excluding the `reportId` if the HID interface uses report IDs.

[HIDInputReportEvent.device](/en-US/docs/Web/API/HIDInputReportEvent/device)Read onlyExperimental

The [HIDDevice](/en-US/docs/Web/API/HIDDevice) instance that represents the HID interface that sent the input report.

[HIDInputReportEvent.reportId](/en-US/docs/Web/API/HIDInputReportEvent/reportId)Read onlyExperimental

The one-byte identification prefix for this report, or 0 if the HID interface does not use report IDs.

## [Instance methods](#instance_methods)

This interface inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

The following example demonstrates listening for an `inputReport` that will allow the application to detect which button is pressed on a Joy-Con Right device. You can see more examples, and live demos in the article [Connecting to uncommon HID devices](https://developer.chrome.com/docs/capabilities/hid).

js

```
device.addEventListener("inputreport", (event) => {
  const { data, device, reportId } = event;

  // Handle only the Joy-Con Right device and a specific report ID.
  if (device.productId !== 0x2007 && reportId !== 0x3f) return;

  const value = data.getUint8(0);
  if (value === 0) return;

  const someButtons = { 1: "A", 2: "X", 4: "B", 8: "Y" };
  console.log(`User pressed button ${someButtons[value]}.`);
});
```

## [Specifications](#specifications)

Specification
[WebHID API# dom-hidinputreportevent](https://wicg.github.io/webhid/#dom-hidinputreportevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HIDInputReportEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/hidinputreportevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDInputReportEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhidinputreportevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDInputReportEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhidinputreportevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F534e2c61fee576355e8a9b7036d9fa36056edb03%0A*+Document+last+modified%3A+2024-10-17T16%3A09%3A06.000Z%0A%0A%3C%2Fdetails%3E)
