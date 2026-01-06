# USBDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBDevice&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `USBDevice` interface of the [WebUSB API](/en-US/docs/Web/API/WebUSB_API) provides access to metadata about a paired USB device and methods for controlling it.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[USBDevice.configuration](/en-US/docs/Web/API/USBDevice/configuration)Read onlyExperimental

A [USBConfiguration](/en-US/docs/Web/API/USBConfiguration) object for the currently selected interface for a paired USB device.

[USBDevice.configurations](/en-US/docs/Web/API/USBDevice/configurations)Read onlyExperimental

An [array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of device-specific interfaces for controlling a paired USB device.

[USBDevice.deviceClass](/en-US/docs/Web/API/USBDevice/deviceClass)Read onlyExperimental

One of three properties that identify USB devices for the purpose of loading a USB driver that will work with that device. The other two properties are `USBDevice.deviceSubclass` and `USBDevice.deviceProtocol`.

[USBDevice.deviceProtocol](/en-US/docs/Web/API/USBDevice/deviceProtocol)Read onlyExperimental

One of three properties that identify USB devices for the purpose of loading a USB driver that will work with that device. The other two properties are `USBDevice.deviceClass` and `USBDevice.deviceSubclass`.

[USBDevice.deviceSubclass](/en-US/docs/Web/API/USBDevice/deviceSubclass)Read onlyExperimental

One of three properties that identify USB devices for the purpose of loading a USB driver that will work with that device. The other two properties are `USBDevice.deviceClass` and `USBDevice.deviceProtocol`.

[USBDevice.deviceVersionMajor](/en-US/docs/Web/API/USBDevice/deviceVersionMajor)Read onlyExperimental

The major version number of the device in a semantic versioning scheme.

[USBDevice.deviceVersionMinor](/en-US/docs/Web/API/USBDevice/deviceVersionMinor)Read onlyExperimental

The minor version number of the device in a semantic versioning scheme.

[USBDevice.deviceVersionSubminor](/en-US/docs/Web/API/USBDevice/deviceVersionSubminor)Read onlyExperimental

The patch version number of the device in a semantic versioning scheme.

[USBDevice.manufacturerName](/en-US/docs/Web/API/USBDevice/manufacturerName)Read onlyExperimental

The name of the organization that manufactured the USB device.

[USBDevice.opened](/en-US/docs/Web/API/USBDevice/opened)Read onlyExperimental

Indicates whether a session has been started with a paired USB device.

[USBDevice.productId](/en-US/docs/Web/API/USBDevice/productId)Read onlyExperimental

The manufacturer-defined code that identifies a USB device.

[USBDevice.productName](/en-US/docs/Web/API/USBDevice/productName)Read onlyExperimental

The manufacturer-defined name that identifies a USB device.

[USBDevice.serialNumber](/en-US/docs/Web/API/USBDevice/serialNumber)Read onlyExperimental

The manufacturer-defined serial number for the specific USB device.

[USBDevice.usbVersionMajor](/en-US/docs/Web/API/USBDevice/usbVersionMajor)Read onlyExperimental

One of three properties that declare the USB protocol version supported by the device. The other two properties are `USBDevice.usbVersionMinor` and `USBDevice.usbVersionSubminor`.

[USBDevice.usbVersionMinor](/en-US/docs/Web/API/USBDevice/usbVersionMinor)Read onlyExperimental

One of three properties that declare the USB protocol version supported by the device. The other two properties are `USBDevice.usbVersionMajor` and `USBDevice.usbVersionSubminor`.

[USBDevice.usbVersionSubminor](/en-US/docs/Web/API/USBDevice/usbVersionSubminor)Read onlyExperimental

One of three properties that declare the USB protocol version supported by the device. The other two properties are `USBDevice.usbVersionMajor` and `USBDevice.usbVersionMinor`.

[USBDevice.vendorId](/en-US/docs/Web/API/USBDevice/vendorId)Read onlyExperimental

The official usb.org-assigned vendor ID.

## [Instance methods](#instance_methods)

[USBDevice.claimInterface()](/en-US/docs/Web/API/USBDevice/claimInterface)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the requested interface is claimed for exclusive access.

[USBDevice.clearHalt()](/en-US/docs/Web/API/USBDevice/clearHalt)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when a halt condition is cleared.

[USBDevice.controlTransferIn()](/en-US/docs/Web/API/USBDevice/controlTransferIn)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [USBInTransferResult](/en-US/docs/Web/API/USBInTransferResult) when a command or status operation has been transmitted to the USB device.

[USBDevice.controlTransferOut()](/en-US/docs/Web/API/USBDevice/controlTransferOut)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [USBOutTransferResult](/en-US/docs/Web/API/USBOutTransferResult) when a command or status operation has been transmitted from the USB device.

[USBDevice.close()](/en-US/docs/Web/API/USBDevice/close)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when all open interfaces are released and the device session has ended.

[USBDevice.forget()](/en-US/docs/Web/API/USBDevice/forget)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves after all open interfaces are released, the device session has ended, and the permission is reset.

[USBDevice.isochronousTransferIn()](/en-US/docs/Web/API/USBDevice/isochronousTransferIn)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [USBIsochronousInTransferResult](/en-US/docs/Web/API/USBIsochronousInTransferResult) when time sensitive information has been transmitted to the USB device.

[USBDevice.isochronousTransferOut()](/en-US/docs/Web/API/USBDevice/isochronousTransferOut)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [USBIsochronousOutTransferResult](/en-US/docs/Web/API/USBIsochronousOutTransferResult) when time sensitive information has been transmitted from the USB device.

[USBDevice.open()](/en-US/docs/Web/API/USBDevice/open)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when a device session has started.

[USBDevice.releaseInterface()](/en-US/docs/Web/API/USBDevice/releaseInterface)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when a claimed interface is released from exclusive access.

[USBDevice.reset()](/en-US/docs/Web/API/USBDevice/reset)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the device is reset and all app operations canceled and their promises rejected.

[USBDevice.selectAlternateInterface()](/en-US/docs/Web/API/USBDevice/selectAlternateInterface)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the specified alternative endpoint is selected.

[USBDevice.selectConfiguration()](/en-US/docs/Web/API/USBDevice/selectConfiguration)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the specified configuration is selected.

[USBDevice.transferIn()](/en-US/docs/Web/API/USBDevice/transferIn)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [USBInTransferResult](/en-US/docs/Web/API/USBInTransferResult) when bulk or interrupt data is received from the USB device.

[USBDevice.transferOut()](/en-US/docs/Web/API/USBDevice/transferOut)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [USBOutTransferResult](/en-US/docs/Web/API/USBOutTransferResult) when bulk or interrupt data is sent to the USB device.

## [Specifications](#specifications)

Specification
[WebUSB API# device-usage](https://wicg.github.io/webusb/#device-usage)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/USBDevice/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/usbdevice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBDevice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fusbdevice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUSBDevice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fusbdevice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa10e3f00a346a0ec35380513f65915849d99f895%0A*+Document+last+modified%3A+2024-10-08T19%3A33%3A59.000Z%0A%0A%3C%2Fdetails%3E)
