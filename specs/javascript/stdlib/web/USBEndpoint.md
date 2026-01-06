# USBEndpoint

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBEndpoint&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `USBEndpoint` interface of the [WebUSB API](/en-US/docs/Web/API/WebUSB_API) provides information about an endpoint provided by the USB device. An endpoint represents a unidirectional data stream into or out of a device.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`USBEndpoint()`Experimental

Creates a new `USBEndpoint` object which will be populated with information about the endpoint on the provided [USBAlternateInterface](/en-US/docs/Web/API/USBAlternateInterface) with the given endpoint number and transfer direction.

## [Instance properties](#instance_properties)

`USBEndpoint.endpointNumber`Experimental

Returns this endpoint's "endpoint number" which is a value from 1 to 15 extracted from the `bEndpointAddress` field of the endpoint descriptor defining this endpoint. This value is used to identify the endpoint when calling methods on `USBDevice`.

`USBEndpoint.direction`Experimental

Returns the direction in which this endpoint transfers data, one of:

- `"in"` - Data is transferred from device to host.
- `"out"` - Data is transferred from host to device.

`USBEndpoint.type`Experimental

Returns the type of this endpoint, one of:

- `"bulk"` - Provides reliable data transfer for large payloads. Data sent through a bulk endpoint is guaranteed to be delivered or generate an error but may be preempted by other data traffic.
- `"interrupt"` - Provides reliable data transfer for small payloads. Data sent through an interrupt endpoint is guaranteed to be delivered or generate an error and is also given dedicated bus time for transmission.
- `"isochronous"` - Provides unreliable data transfer for payloads that must be delivered periodically. They are given dedicated bus time but if a deadline is missed the data is dropped.

`USBEndpoint.packetSize`Experimental

Returns the size of the packets that data sent through this endpoint will be divided into.

## [Examples](#examples)

While sometimes the developer knows ahead of time the exact layout of a device's endpoints there are cases where this must be discovered at runtime. For example, a USB serial device must provide bulk input and output endpoints but their endpoint numbers will depend on what other interfaces the device provides.

This code identifies the correct endpoints by searching for the interface implementing the USB CDC interface class and then identifying the candidate endpoints based on their type and direction.

js

```
let inEndpoint = undefined;
let outEndpoint = undefined;

for (const { alternates } of device.configuration.interfaces) {
  // Only support devices with out multiple alternate interfaces.
  const alternate = alternates[0];

  // Identify the interface implementing the USB CDC class.
  const USB_CDC_CLASS = 10;
  if (alternate.interfaceClass !== USB_CDC_CLASS) {
    continue;
  }

  for (const endpoint of alternate.endpoints) {
    // Identify the bulk transfer endpoints.
    if (endpoint.type !== "bulk") {
      continue;
    }

    if (endpoint.direction === "in") {
      inEndpoint = endpoint.endpointNumber;
    } else if (endpoint.direction === "out") {
      outEndpoint = endpoint.endpointNumber;
    }
  }
}
```

## [Specifications](#specifications)

Specification
[WebUSB API# usbendpoint-interface](https://wicg.github.io/webusb/#usbendpoint-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/USBEndpoint/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/usbendpoint/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBEndpoint&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fusbendpoint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBEndpoint%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fusbendpoint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
