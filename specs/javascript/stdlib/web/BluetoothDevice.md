# BluetoothDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothDevice&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The BluetoothDevice interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) represents a Bluetooth device inside a particular script execution environment.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[BluetoothDevice.id](/en-US/docs/Web/API/BluetoothDevice/id)ExperimentalRead only

A string that uniquely identifies a device.

[BluetoothDevice.name](/en-US/docs/Web/API/BluetoothDevice/name)ExperimentalRead only

A string that provides a human-readable name for the device.

[BluetoothDevice.gatt](/en-US/docs/Web/API/BluetoothDevice/gatt)ExperimentalRead only

A reference to the device's [BluetoothRemoteGATTServer](/en-US/docs/Web/API/BluetoothRemoteGATTServer).

## [Instance methods](#instance_methods)

`BluetoothDevice.watchAdvertisements()`Experimental

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to `undefined` or is rejected with an error if advertisements can't be shown for any reason.

`BluetoothDevice.forget()`Experimental

Provides a way for the page to revoke access to a device the user has granted access to.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

`gattserverdisconnected`Experimental

Fired on a device when an active GATT connection is lost.

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetoothdevice-interface](https://webbluetoothcg.github.io/web-bluetooth/#bluetoothdevice-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothDevice/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothdevice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothDevice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothdevice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothDevice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothdevice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff33c6e8a7204272b90d8f005f3d8c743333d7dbf%0A*+Document+last+modified%3A+2024-03-26T04%3A46%3A35.000Z%0A%0A%3C%2Fdetails%3E)
