# HIDConnectionEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDConnectionEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Shared Web Workers](/en-US/docs/Web/API/SharedWorkerGlobalScope).

The `HIDConnectionEvent` interface of the [WebHID API](/en-US/docs/Web/API/WebHID_API) represents HID connection events, and is the event type passed to [connect](/en-US/docs/Web/API/HID/connect_event) and [disconnect](/en-US/docs/Web/API/HID/disconnect_event) event handlers when a device's connection state changes.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[HIDConnectionEvent()](/en-US/docs/Web/API/HIDConnectionEvent/HIDConnectionEvent)Experimental

Returns a new `HIDConnectionEvent` object. Typically this constructor is not used as events are created when a device's connection state changes.

## [Instance properties](#instance_properties)

This interface also inherits properties from [Event](/en-US/docs/Web/API/Event).

[HIDConnectionEvent.device](/en-US/docs/Web/API/HIDConnectionEvent/device)Read onlyExperimental

Returns the [HIDDevice](/en-US/docs/Web/API/HIDDevice) instance representing the device associated with the connection event.

## [Examples](#examples)

The following example registers event listeners for `connect` and `disconnect` events, then prints the [HIDDevice.productName](/en-US/docs/Web/API/HIDDevice/productName) to the console.

js

```
navigator.hid.addEventListener("connect", ({ device }) => {
  console.log(`HID connected: ${device.productName}`);
});

navigator.hid.addEventListener("disconnect", ({ device }) => {
  console.log(`HID disconnected: ${device.productName}`);
});
```

## [Specifications](#specifications)

Specification
[WebHID API# dom-hidconnectionevent](https://wicg.github.io/webhid/#dom-hidconnectionevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HIDConnectionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/hidconnectionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDConnectionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhidconnectionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDConnectionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhidconnectionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F534e2c61fee576355e8a9b7036d9fa36056edb03%0A*+Document+last+modified%3A+2024-10-17T16%3A09%3A06.000Z%0A%0A%3C%2Fdetails%3E)
