# BluetoothRemoteGATTService

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTService&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `BluetoothRemoteGATTService` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) represents a service provided by a GATT server, including a device, a list of referenced services, and a list of the characteristics of this service.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[BluetoothRemoteGATTService.device](/en-US/docs/Web/API/BluetoothRemoteGATTService/device)Read onlyExperimental

Returns information about a Bluetooth device through an instance of [BluetoothDevice](/en-US/docs/Web/API/BluetoothDevice).

[BluetoothRemoteGATTService.isPrimary](/en-US/docs/Web/API/BluetoothRemoteGATTService/isPrimary)Read onlyExperimental

Returns a boolean value indicating whether this is a primary or secondary service.

[BluetoothRemoteGATTService.uuid](/en-US/docs/Web/API/BluetoothRemoteGATTService/uuid)Read onlyExperimental

Returns a string representing the UUID of this service.

## [Instance methods](#instance_methods)

[BluetoothRemoteGATTService.getCharacteristic()](/en-US/docs/Web/API/BluetoothRemoteGATTService/getCharacteristic)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) to an instance of [BluetoothRemoteGATTCharacteristic](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic) for a given universally unique identifier (UUID).

[BluetoothRemoteGATTService.getCharacteristics()](/en-US/docs/Web/API/BluetoothRemoteGATTService/getCharacteristics)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) to an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of [BluetoothRemoteGATTCharacteristic](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic) instances for an optional universally unique identifier (UUID).

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetoothgattservice-interface](https://webbluetoothcg.github.io/web-bluetooth/#bluetoothgattservice-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothRemoteGATTService/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothremotegattservice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTService&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothremotegattservice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTService%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothremotegattservice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbfc735c04506625c8c60054fe6f2f136bc43bbea%0A*+Document+last+modified%3A+2024-08-11T15%3A28%3A08.000Z%0A%0A%3C%2Fdetails%3E)
