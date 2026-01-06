# BluetoothCharacteristicProperties

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothCharacteristicProperties&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `BluetoothCharacteristicProperties` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) provides the operations that are valid on the given [BluetoothRemoteGATTCharacteristic](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic).

This interface is returned by calling [BluetoothRemoteGATTCharacteristic.properties](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic/properties).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[authenticatedSignedWrites](/en-US/docs/Web/API/BluetoothCharacteristicProperties/authenticatedSignedWrites)Read onlyExperimental

Returns a `boolean` that is `true` if signed writing to the characteristic value is permitted.

[broadcast](/en-US/docs/Web/API/BluetoothCharacteristicProperties/broadcast)Read onlyExperimental

Returns a `boolean` that is `true` if the broadcast of the characteristic value is permitted using the Server Characteristic Configuration Descriptor.

[indicate](/en-US/docs/Web/API/BluetoothCharacteristicProperties/indicate)Read onlyExperimental

Returns a `boolean` that is `true` if indications of the characteristic value with acknowledgement is permitted.

[notify](/en-US/docs/Web/API/BluetoothCharacteristicProperties/notify)Read onlyExperimental

Returns a `boolean` that is `true` if notifications of the characteristic value without acknowledgement is permitted.

[read](/en-US/docs/Web/API/BluetoothCharacteristicProperties/read)Read onlyExperimental

Returns a `boolean` that is `true` if the reading of the characteristic value is permitted.

[reliableWrite](/en-US/docs/Web/API/BluetoothCharacteristicProperties/reliableWrite)Read onlyExperimental

Returns a `boolean` that is `true` if reliable writes to the characteristic is permitted.

[writableAuxiliaries](/en-US/docs/Web/API/BluetoothCharacteristicProperties/writableAuxiliaries)Read onlyExperimental

Returns a `boolean` that is `true` if reliable writes to the characteristic descriptor is permitted.

[write](/en-US/docs/Web/API/BluetoothCharacteristicProperties/write)Read onlyExperimental

Returns a `boolean` that is `true` if the writing to the characteristic with response is permitted.

[writeWithoutResponse](/en-US/docs/Web/API/BluetoothCharacteristicProperties/writeWithoutResponse)Read onlyExperimental

Returns a `boolean` that is `true` if the writing to the characteristic without response is permitted.

## [Examples](#examples)

The following example shows how tell if a GATT characteristic supports value change notifications.

js

```
let device = await navigator.bluetooth.requestDevice({
  filters: [{ services: ["heart_rate"] }],
});
let gatt = await device.gatt.connect();
let service = await gatt.getPrimaryService("heart_rate");
let characteristic = await service.getCharacteristic("heart_rate_measurement");
if (characteristic.properties.notify) {
  characteristic.addEventListener(
    "characteristicvaluechanged",
    async (event) => {
      console.log(`Received heart rate measurement: ${event.target.value}`);
    },
  );
  await characteristic.startNotifications();
}
```

## [Specifications](#specifications)

Specification
[Web Bluetooth# characteristicproperties-interface](https://webbluetoothcg.github.io/web-bluetooth/#characteristicproperties-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothCharacteristicProperties/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothcharacteristicproperties/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothCharacteristicProperties&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothcharacteristicproperties%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothCharacteristicProperties%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothcharacteristicproperties%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
