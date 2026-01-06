# BluetoothUUID

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothUUID&level=not)

The `BluetoothUUID` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) provides a way to look up Universally Unique Identifier (UUID) values by name in the [registry](https://www.bluetooth.com/specifications/assigned-numbers/) maintained by the Bluetooth SIG.

## In this article

- [Description](#description)
- [Static methods](#static_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Description](#description)

A UUID string is a 128-bit UUID, for example `00001818-0000-1000-8000-00805f9b34fb`. The Bluetooth registry contains lists of descriptors, services, and characteristics identified by these UUIDs in addition to a 16- or 32- bit alias, and a name.

The `BluetoothUUID` interface provides methods to retrieve these 128-bit UUIDs.

## [Static methods](#static_methods)

[BluetoothUUID.canonicalUUID()](/en-US/docs/Web/API/BluetoothUUID/canonicalUUID_static)Experimental

Returns the 128-bit UUID when passed the 16- or 32-bit UUID alias.

[BluetoothUUID.getCharacteristic()](/en-US/docs/Web/API/BluetoothUUID/getCharacteristic_static)Experimental

Returns the 128-bit UUID representing a registered characteristic when passed a name or the 16- or 32-bit UUID alias.

[BluetoothUUID.getDescriptor()](/en-US/docs/Web/API/BluetoothUUID/getDescriptor_static)Experimental

Returns a UUID representing a registered descriptor when passed a name or the 16- or 32-bit UUID alias.

[BluetoothUUID.getService()](/en-US/docs/Web/API/BluetoothUUID/getService_static)Experimental

Returns a UUID representing a registered service when passed a name or the 16- or 32-bit UUID alias.

## [Examples](#examples)

In the following example the UUID representing the service named `device_information` is returned and printed to the console.

js

```
let result = BluetoothUUID.getService("device_information");
console.log(result); // "0000180a-0000-1000-8000-00805f9b34fb"
```

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetoothuuid](https://webbluetoothcg.github.io/web-bluetooth/#bluetoothuuid)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothUUID/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothuuid/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothUUID&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothuuid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothUUID%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothuuid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4675b9077ae32f989c7ecac94f454db2653c4fc%0A*+Document+last+modified%3A+2024-07-25T22%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E)
