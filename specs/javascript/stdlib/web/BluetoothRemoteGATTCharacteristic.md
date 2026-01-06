# BluetoothRemoteGATTCharacteristic

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTCharacteristic&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `BluetoothRemoteGattCharacteristic` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) represents a GATT Characteristic, which is a basic data element that provides further information about a peripheral's service.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[BluetoothRemoteGATTCharacteristic.service](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/service)Read onlyExperimental

Returns the [BluetoothRemoteGATTService](/en-US/docs/Web/API/BluetoothRemoteGATTService) this characteristic belongs to.

[BluetoothRemoteGATTCharacteristic.uuid](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/uuid)Read onlyExperimental

Returns a string containing the UUID of the characteristic, for example `'00002a37-0000-1000-8000-00805f9b34fb'` for the Heart Rate Measurement characteristic.

[BluetoothRemoteGATTCharacteristic.properties](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/properties)Read onlyExperimental

Returns the properties of this characteristic.

[BluetoothRemoteGATTCharacteristic.value](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/value)Read onlyExperimental

The currently cached characteristic value. This value gets updated when the value of the characteristic is read or updated via a notification or indication.

## [Instance methods](#instance_methods)

[BluetoothRemoteGATTCharacteristic.getDescriptor()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/getDescriptor)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to the first [BluetoothRemoteGATTDescriptor](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor) for a given descriptor UUID.

[BluetoothRemoteGATTCharacteristic.getDescriptors()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/getDescriptors)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of all [BluetoothRemoteGATTDescriptor](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor) objects for a given descriptor UUID.

[BluetoothRemoteGATTCharacteristic.readValue()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/readValue)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) holding a duplicate of the `value` property if it is available and supported. Otherwise it throws an error.

[BluetoothRemoteGATTCharacteristic.writeValue()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/writeValue)Deprecated

Sets the `value` property to the bytes contained in a given [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [writes the characteristic value with optional response](https://webbluetoothcg.github.io/web-bluetooth/#writecharacteristicvalue), and returns the resulting [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

[BluetoothRemoteGATTCharacteristic.writeValueWithResponse()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/writeValueWithResponse)Experimental

Sets the `value` property to the bytes contained in a given [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [writes the characteristic value with required response](https://webbluetoothcg.github.io/web-bluetooth/#writecharacteristicvalue), and returns the resulting [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

[BluetoothRemoteGATTCharacteristic.writeValueWithoutResponse()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/writeValueWithoutResponse)Experimental

Sets the `value` property to the bytes contained in a given [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [writes the characteristic value without response](https://webbluetoothcg.github.io/web-bluetooth/#writecharacteristicvalue), and returns the resulting [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

[BluetoothRemoteGATTCharacteristic.startNotifications()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/startNotifications)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when `navigator.bluetooth` is added to the active notification context.

[BluetoothRemoteGATTCharacteristic.stopNotifications()](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/stopNotifications)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when `navigator.bluetooth` is removed from the active notification context.

## [Events](#events)

`characteristicvaluechanged`Experimental

Fired on a `BluetoothRemoteGATTCharacteristic` when its value changes.

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetoothgattcharacteristic-interface](https://webbluetoothcg.github.io/web-bluetooth/#bluetoothgattcharacteristic-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothremotegattcharacteristic/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTCharacteristic&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothremotegattcharacteristic%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTCharacteristic%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothremotegattcharacteristic%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
