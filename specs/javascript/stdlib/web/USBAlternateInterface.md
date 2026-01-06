# USBAlternateInterface

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBAlternateInterface&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `USBAlternateInterface` interface of the [WebUSB API](/en-US/docs/Web/API/WebUSB_API) provides information about a particular configuration of an interface provided by the USB device. An interface includes one or more alternate settings which can configure a set of endpoints based on the operating mode of the device.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`USBAlternateInterface()`Experimental

Creates a new `USBAlternateInterface` object which will be populated with information about the alternate interface of the provided `USBInterface` with the given alternate setting number.

## [Instance properties](#instance_properties)

`USBAlternateInterface.alternateSetting`Read onlyExperimental

Returns the alternate setting number of this interface. This is equal to the `bAlternateSetting` field of the interface descriptor defining this interface.

`USBAlternateInterface.interfaceClass`Read onlyExperimental

Returns the class of this interface. This is equal to the `bInterfaceClass` field of the interface descriptor defining this interface. [Standardized values](https://www.usb.org/defined-class-codes) for this field are defined by the USB Implementers Forum. A value of `0xFF` indicates a vendor-defined interface.

`USBAlternateInterface.interfaceSubclass`Read onlyExperimental

Returns the subclass of this interface. This is equal to the `bInterfaceSubClass` field of the interface descriptor defining this interface. The meaning of this value depends on the `interfaceClass` field.

`USBAlternateInterface.interfaceProtocol`Read onlyExperimental

Returns the protocol supported by this interface. This is equal to the `bInterfaceProtocol` field of the interface descriptor defining this interface. The meaning of this value depends on the `interfaceClass` and `interfaceSubclass` fields.

`USBAlternateInterface.interfaceName`Read onlyExperimental

Returns the name of the interface, if one is provided by the device. This is the value of the string descriptor with the index specified by the `iInterface` field of the interface descriptor defining this interface.

`USBAlternateInterface.endpoints`Read onlyExperimental

Returns an array containing instances of the `USBEndpoint` interface describing each of the endpoints that are part of this interface.

## [Specifications](#specifications)

Specification
[WebUSB API# usbalternateinterface](https://wicg.github.io/webusb/#usbalternateinterface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/USBAlternateInterface/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/usbalternateinterface/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBAlternateInterface&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fusbalternateinterface%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBAlternateInterface%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fusbalternateinterface%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa10e3f00a346a0ec35380513f65915849d99f895%0A*+Document+last+modified%3A+2024-10-08T19%3A33%3A59.000Z%0A%0A%3C%2Fdetails%3E)
