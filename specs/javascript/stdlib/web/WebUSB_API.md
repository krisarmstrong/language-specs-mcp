# WebUSB API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebUSB_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebUSB API provides a way to expose non-standard Universal Serial Bus (USB) compatible devices services to the web, to make USB safer and easier to use.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

USB is the de-facto standard for wired peripherals. The USB devices that you connect to your computer are typically grouped into a number of device classes—such as keyboards, mice, video devices, and so on. These are supported using the operating system's class driver. Many of these are also web accessible via the [WebHID API](/en-US/docs/Web/API/WebHID_API).

In addition to these standardized devices, there are a large number of devices that don't fit into any class. These need custom drivers, and are inaccessible from the web due to the native code required to take advantage of them. Installing one of these devices often involves searching on a manufacturer's website for drivers and, should you wish to use the device on another computer, repeating the process again.

WebUSB provides a way for these non-standardized USB device services to be exposed to the web. This means that hardware manufacturers will be able to provide a way for their device to be accessed from the web, without having to provide their own API.

When connecting a new WebUSB-compatible device, the browser displays a notification providing a link to the manufacturer's website. On arriving at the site the browser prompts for permission to connect to the device, then the device is ready for use. No drivers need be downloaded and installed.

## [Interfaces](#interfaces)

[USB](/en-US/docs/Web/API/USB)

Provides attributes and methods for finding and connecting USB devices from a web page.

[USBConnectionEvent](/en-US/docs/Web/API/USBConnectionEvent)

The event type passed to `USB`[connect](/en-US/docs/Web/API/USB/connect_event) or [disconnect](/en-US/docs/Web/API/USB/disconnect_event) events when the user agent detects a new USB device has been connected to, or disconnected from the host.

[USBDevice](/en-US/docs/Web/API/USBDevice)

Provides access to metadata about a paired USB device and methods for controlling it.

[USBInTransferResult](/en-US/docs/Web/API/USBInTransferResult)

Represents the result from requesting a transfer of data from the USB device to the USB host.

[USBOutTransferResult](/en-US/docs/Web/API/USBOutTransferResult)

Represents the result from requesting a transfer of data from the USB host to the USB device.

[USBIsochronousInTransferPacket](/en-US/docs/Web/API/USBIsochronousInTransferPacket)

Represents the status of an individual packet from a request to transfer data from the USB device to the USB host over an isochronous endpoint.

[USBIsochronousInTransferResult](/en-US/docs/Web/API/USBIsochronousInTransferResult)

Represents the result from requesting a transfer of data from the USB device to the USB host.

[USBIsochronousOutTransferPacket](/en-US/docs/Web/API/USBIsochronousOutTransferPacket)

Represents the status of an individual packet from a request to transfer data from the USB host to the USB device over an isochronous endpoint.

[USBIsochronousOutTransferResult](/en-US/docs/Web/API/USBIsochronousOutTransferResult)

Represents the result from requesting a transfer of data from the USB host to the USB device.

[USBConfiguration](/en-US/docs/Web/API/USBConfiguration)

Provides information about a particular configuration of a USB device and the interfaces that it supports.

[USBInterface](/en-US/docs/Web/API/USBInterface)

Provides information about an interface provided by the USB device.

[USBAlternateInterface](/en-US/docs/Web/API/USBAlternateInterface)

Provides information about a particular configuration of an interface provided by the USB device.

[USBEndPoint](/en-US/docs/Web/API/USBEndpoint)

Provides information about an endpoint provided by the USB device.

## [Examples](#examples)

### [Accessing a connected device](#accessing_a_connected_device)

The following example demonstrates how to access a connected Arduino device using [USB.requestDevice()](/en-US/docs/Web/API/USB/requestDevice), which has a vendorId of `0x2341`.

js

```
navigator.usb
  .requestDevice({ filters: [{ vendorId: 0x2341 }] })
  .then((device) => {
    console.log(device.productName); // "Arduino Micro"
    console.log(device.manufacturerName); // "Arduino LLC"
  })
  .catch((error) => {
    console.error(error);
  });
```

### [Finding all connected devices](#finding_all_connected_devices)

You can find all connected devices with [USB.getDevices()](/en-US/docs/Web/API/USB/getDevices). In the following example, with the Arduino device connected, product and manufacturer name are printed to the console.

js

```
navigator.usb.getDevices().then((devices) => {
  devices.forEach((device) => {
    console.log(device.productName); // "Arduino Micro"
    console.log(device.manufacturerName); // "Arduino LLC"
  });
});
```

## [Specifications](#specifications)

Specification[WebUSB API](https://wicg.github.io/webusb/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Access USB Devices on the Web](https://developer.chrome.com/docs/capabilities/usb)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebUSB_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webusb_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebUSB_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebusb_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebUSB_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebusb_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdb01d0c8b4cbf8a4467b1db65e17f6724d0ce710%0A*+Document+last+modified%3A+2025-07-12T01%3A26%3A27.000Z%0A%0A%3C%2Fdetails%3E)
