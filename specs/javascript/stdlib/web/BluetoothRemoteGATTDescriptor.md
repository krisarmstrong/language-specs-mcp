# BluetoothRemoteGATTDescriptor

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTDescriptor&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `BluetoothRemoteGATTDescriptor` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) provides a GATT Descriptor, which provides further information about a characteristic's value.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[BluetoothRemoteGATTDescriptor.characteristic](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor/characteristic)Read onlyExperimental

Returns the [BluetoothRemoteGATTCharacteristic](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic) this descriptor belongs to.

[BluetoothRemoteGATTDescriptor.uuid](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor/uuid)Read onlyExperimental

Returns the UUID of the characteristic descriptor, for example `"00002902-0000-1000-8000-00805f9b34fb"` for the Client Characteristic Configuration descriptor.

[BluetoothRemoteGATTDescriptor.value](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor/value)Read onlyExperimental

Returns the currently cached descriptor value. This value gets updated when the value of the descriptor is read.

## [Instance methods](#instance_methods)

[BluetoothRemoteGATTDescriptor.readValue()](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor/readValue)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) holding a duplicate of the `value` property if it is available and supported. Otherwise it throws an error.

[BluetoothRemoteGATTDescriptor.writeValue()](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor/writeValue)Experimental

Sets the value property to the bytes contained in an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetoothgattdescriptor-interface](https://webbluetoothcg.github.io/web-bluetooth/#bluetoothgattdescriptor-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothremotegattdescriptor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTDescriptor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothremotegattdescriptor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTDescriptor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothremotegattdescriptor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdcbb1d99185118360cc84b3a0e935e77fe0a03e3%0A*+Document+last+modified%3A+2024-09-24T13%3A57%3A44.000Z%0A%0A%3C%2Fdetails%3E)
