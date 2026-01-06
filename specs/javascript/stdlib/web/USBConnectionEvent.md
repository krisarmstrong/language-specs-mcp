# USBConnectionEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBConnectionEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `USBConnectionEvent` interface of the [WebUSB API](/en-US/docs/Web/API/WebUSB_API) is the event type passed to `USB`[connect](/en-US/docs/Web/API/USB/connect_event) and [disconnect](/en-US/docs/Web/API/USB/disconnect_event) events when the user agent detects that a new USB device has been connected or disconnected.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[USBConnectionEvent()](/en-US/docs/Web/API/USBConnectionEvent/USBConnectionEvent)Experimental

Returns a `USBConnectionEvent` object.

## [Instance properties](#instance_properties)

[USBConnectionEvent.device](/en-US/docs/Web/API/USBConnectionEvent/device)Read onlyExperimental

Returns a [USBDevice](/en-US/docs/Web/API/USBDevice) object representing the current device.

## [Examples](#examples)

In the following example listening for connect and disconnect events is used to add and remove the devices from the user interface of an application.

js

```
navigator.usb.addEventListener("connect", (event) => {
  // Add event.device to the UI.
});

navigator.usb.addEventListener("disconnect", (event) => {
  // Remove event.device from the UI.
});
```

## [Specifications](#specifications)

Specification
[WebUSB API# usbconnectionevent](https://wicg.github.io/webusb/#usbconnectionevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/USBConnectionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/usbconnectionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBConnectionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fusbconnectionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBConnectionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fusbconnectionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa10e3f00a346a0ec35380513f65915849d99f895%0A*+Document+last+modified%3A+2024-10-08T19%3A33%3A59.000Z%0A%0A%3C%2Fdetails%3E)
