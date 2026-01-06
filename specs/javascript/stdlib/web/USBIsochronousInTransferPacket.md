# USBIsochronousInTransferPacket

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBIsochronousInTransferPacket&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `USBIsochronousInTransferPacket` interface of the [WebUSB API](/en-US/docs/Web/API/WebUSB_API) is part of the response from a call to the `isochronousTransferIn()` method of the `USBDevice` interface. It represents the status of an individual packet from a request to transfer data from the USB device to the USB host over an isochronous endpoint.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`USBIsochronousInTransferPacket()`Experimental

Creates a new `USBIsochronousInTransferPacket` object with the provided `status` and `data` fields.

## [Instance properties](#instance_properties)

`USBIsochronousInTransferPacket.data`Read onlyRead onlyExperimental

Returns a `DataView` object containing the data received from the USB device in this packet, if any.

`USBIsochronousInTransferPacket.status`Read onlyRead onlyExperimental

Returns the status of the transfer request, one of:

- `"ok"` - The transfer was successful.
- `"stall"` - The device indicated an error by generating a stall condition on the endpoint. A stall on an isochronous endpoint does not need to be cleared.
- `"babble"` - The device responded with more data than was expected.

## [Specifications](#specifications)

Specification
[WebUSB API# usbisochronousintransferpacket](https://wicg.github.io/webusb/#usbisochronousintransferpacket)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/USBIsochronousInTransferPacket/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/usbisochronousintransferpacket/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBIsochronousInTransferPacket&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fusbisochronousintransferpacket%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBIsochronousInTransferPacket%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fusbisochronousintransferpacket%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
