# WebHID API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebHID_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Shared Web Workers](/en-US/docs/Web/API/SharedWorkerGlobalScope).

A Human Interface Device (HID) is a type of device that takes input from or provides output to humans. It also refers to the HID protocol, a standard for bi-directional communication between a host and a device that is designed to simplify the installation procedure. The HID protocol was originally developed for USB devices but has since been implemented over many other protocols, including Bluetooth.

## In this article

- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces](#interfaces)

[HID](/en-US/docs/Web/API/HID)

Provides methods for connecting to HID devices, listing attached HID devices and event handlers for connected HID devices.

[HIDDevice](/en-US/docs/Web/API/HIDDevice)

Represents an HID device. It's possible for a single physical device to be represented by multiple `HIDDevice` objects.

[HIDInputReportEvent](/en-US/docs/Web/API/HIDInputReportEvent)

Passed to the `HIDDevice`[inputreport](/en-US/docs/Web/API/HIDDevice/inputreport_event) event when an input report is received from any associated HID device.

[HIDConnectionEvent](/en-US/docs/Web/API/HIDConnectionEvent)

Passed to `HID`[connect](/en-US/docs/Web/API/HID/connect_event) and [disconnect](/en-US/docs/Web/API/HID/disconnect_event) events when a device is connected or disconnected.

## [Examples](#examples)

You can connect to a device with the [requestDevice()](/en-US/docs/Web/API/HID/requestDevice) method. In this case, we select from all the available devices.

js

```
const device = await navigator.hid.requestDevice({ filters: [] });
// A popup titled `... wants to connect to a HID Device` with `Cancel` and `Connect` buttons will show up with a device list to select from.
// Select one and click on `Connect` button. Then the device will be an array with the selected device in it.
```

We can retrieve all the devices the website has been granted access to previously and log the device names to the console.

js

```
let devices = await navigator.hid.getDevices();
devices.forEach((device) => {
  console.log(`HID: ${device.productName}`);
});
```

We can register event listeners for disconnection of any HID devices.

js

```
navigator.hid.addEventListener("disconnect", (event) => {
  console.log(`HID disconnected: ${event.device.productName}`);
  console.dir(event);
});
// For example, when my connected keyboard gets disconnected, the log in the console will show:
// HID disconnected: USB Keyboard
// {
//    bubbles: false
//    cancelBubble: false
//    cancelable: false
//    composed: false
//    currentTarget: HID {onconnect: null, ondisconnect: null}
//    defaultPrevented: false
//    device: HIDDevice {oninputreport: null, opened: false, vendorId: 6700, productId: 11555, productName: "USB Keyboard", …}
//    eventPhase: 0
//    isTrusted: true
//    path: []
//    returnValue: true
//    srcElement: HID {onconnect: null, ondisconnect: null}
//    target: HID {onconnect: null, ondisconnect: null}
//    timeStamp: 18176.600000023842
//    type: "disconnect"
// }

// The event above is an instance of the HIDConnectionEvent interface.
```

## [Specifications](#specifications)

Specification
[WebHID API# dom-hid](https://wicg.github.io/webhid/#dom-hid)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebHID_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webhid_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebHID_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebhid_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebHID_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebhid_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F534e2c61fee576355e8a9b7036d9fa36056edb03%0A*+Document+last+modified%3A+2024-10-17T16%3A09%3A06.000Z%0A%0A%3C%2Fdetails%3E)
