# HIDDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDDevice&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Shared Web Workers](/en-US/docs/Web/API/SharedWorkerGlobalScope).

The `HIDDevice` interface of the [WebHID API](/en-US/docs/Web/API/WebHID_API) represents a HID Device. It provides properties for accessing information about the device, methods for opening and closing the connection, and the sending and receiving of reports.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from [EventTarget](/en-US/docs/Web/API/EventTarget).

[HIDDevice.opened](/en-US/docs/Web/API/HIDDevice/opened)Read onlyExperimental

Returns a [boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean), true if the device has an open connection.

[HIDDevice.vendorId](/en-US/docs/Web/API/HIDDevice/vendorId)Read onlyExperimental

Returns the vendorId of the HID device.

[HIDDevice.productId](/en-US/docs/Web/API/HIDDevice/productId)Read onlyExperimental

Returns the productId of the HID device.

[HIDDevice.productName](/en-US/docs/Web/API/HIDDevice/productName)Read onlyExperimental

Returns a string containing the product name of the HID device.

[HIDDevice.collections](/en-US/docs/Web/API/HIDDevice/collections)Read onlyExperimental

Returns an array of report formats for the HID device.

### [Events](#events)

[inputreport](/en-US/docs/Web/API/HIDDevice/inputreport_event)Experimental

Fires when a report is sent from the device.

## [Instance methods](#instance_methods)

This interface also inherits methods from [EventTarget](/en-US/docs/Web/API/EventTarget).

[HIDDevice.open()](/en-US/docs/Web/API/HIDDevice/open)Experimental

Opens a connection to this HID device, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the connection has been successful.

[HIDDevice.close()](/en-US/docs/Web/API/HIDDevice/close)Experimental

Closes the connection to this HID device, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the connection has been closed.

[HIDDevice.forget()](/en-US/docs/Web/API/HIDDevice/forget)Experimental

Closes the connection to this HID device and resets access permission, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the permission was reset.

[HIDDevice.sendReport()](/en-US/docs/Web/API/HIDDevice/sendReport)Experimental

Sends an output report to this HID Device, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the report has been sent.

[HIDDevice.sendFeatureReport()](/en-US/docs/Web/API/HIDDevice/sendFeatureReport)Experimental

Sends a feature report to this HID device, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves once the report has been sent.

[HIDDevice.receiveFeatureReport()](/en-US/docs/Web/API/HIDDevice/receiveFeatureReport)Experimental

Receives a feature report from this HID device in the form of a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves with a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). This allows typed access to the contents of this message.

## [Examples](#examples)

The following example demonstrates listening for an `inputreport` event that will allow the application to detect which button is pressed on a Joy-Con Right device.

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

In the following example `sendFeatureReport` is used to make a device blink.

js

```
const reportId = 1;
for (let i = 0; i < 10; i++) {
  // Turn off
  await device.sendFeatureReport(reportId, Uint32Array.from([0, 0]));
  await new Promise((resolve) => setTimeout(resolve, 100));
  // Turn on
  await device.sendFeatureReport(reportId, Uint32Array.from([512, 0]));
  await new Promise((resolve) => setTimeout(resolve, 100));
}
```

You can see more examples, and live demos in the article [Connecting to uncommon HID devices](https://developer.chrome.com/docs/capabilities/hid).

## [Specifications](#specifications)

Specification
[WebHID API# dom-hiddevice](https://wicg.github.io/webhid/#dom-hiddevice)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 1, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HIDDevice/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/hiddevice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDDevice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhiddevice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHIDDevice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhiddevice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe4d6e3444fc0f46a2f12de882c5b12c44fb75e02%0A*+Document+last+modified%3A+2024-11-01T21%3A28%3A26.000Z%0A%0A%3C%2Fdetails%3E)
