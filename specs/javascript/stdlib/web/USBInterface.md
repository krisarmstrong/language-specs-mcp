# USBInterface

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBInterface&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `USBInterface` interface of the [WebUSB API](/en-US/docs/Web/API/WebUSB_API) provides information about an interface provided by the USB device. An interface represents a feature of the device which implements a particular protocol and may contain endpoints for bidirectional communication.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`USBInterface()`Experimental

Creates a new `USBInterface` object which will be populated with information about the interface on the provided `USBConfiguration` with the given interface number.

## [Instance properties](#instance_properties)

`USBInterface.interfaceNumber`Read onlyExperimental

Returns the interface number of this interface. This is equal to the `bInterfaceNumber` field of the interface descriptor defining this interface.

`USBInterface.alternate`Read onlyExperimental

Returns the currently selected alternative configuration of this interface. By default this is the `USBAlternateInterface` from `alternates` with `alternateSetting` equal to `0`. It can be changed by calling `USBDevice.selectAlternateInterface()` with any other value found in `alternates`.

`USBInterface.alternates`Read onlyExperimental

Returns an array containing instances of the `USBAlternateInterface` interface describing each of the alternative configurations possible for this interface.

`USBInterface.claimed`Read onlyExperimental

Returns whether or not this interface has been claimed by the current page by calling `USBDevice.claimInterface()`.

## [Specifications](#specifications)

Specification
[WebUSB API# usbinterface](https://wicg.github.io/webusb/#usbinterface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/USBInterface/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/usbinterface/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBInterface&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fusbinterface%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBInterface%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fusbinterface%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa10e3f00a346a0ec35380513f65915849d99f895%0A*+Document+last+modified%3A+2024-10-08T19%3A33%3A59.000Z%0A%0A%3C%2Fdetails%3E)
