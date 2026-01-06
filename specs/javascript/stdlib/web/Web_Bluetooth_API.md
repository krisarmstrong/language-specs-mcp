# Web Bluetooth API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Bluetooth_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Web Bluetooth API provides the ability to connect and interact with Bluetooth Low Energy peripherals.

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

## In this article

- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Security considerations](#security_considerations)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces](#interfaces)

[Bluetooth](/en-US/docs/Web/API/Bluetooth)

Provides methods to query Bluetooth availability and request access to devices.

[BluetoothCharacteristicProperties](/en-US/docs/Web/API/BluetoothCharacteristicProperties)

Provides properties of a particular `BluetoothRemoteGATTCharacteristic`.

[BluetoothDevice](/en-US/docs/Web/API/BluetoothDevice)

Represents a Bluetooth device inside a particular script execution environment.

[BluetoothRemoteGATTCharacteristic](/en-US/docs/Web/API/BluetoothRemoteGATTCharacteristic)

Represents a GATT Characteristic, which is a basic data element that provides further information about a peripheral's service.

[BluetoothRemoteGATTDescriptor](/en-US/docs/Web/API/BluetoothRemoteGATTDescriptor)

Represents a GATT Descriptor, which provides further information about a characteristic's value.

[BluetoothRemoteGATTServer](/en-US/docs/Web/API/BluetoothRemoteGATTServer)

Represents a GATT Server on a remote device.

[BluetoothRemoteGATTService](/en-US/docs/Web/API/BluetoothRemoteGATTService)

Represents a service provided by a GATT server, including a device, a list of referenced services, and a list of the characteristics of this service.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

The Bluetooth API extends the following APIs, adding the listed features.

### [Navigator](#navigator)

[Navigator.bluetooth](/en-US/docs/Web/API/Navigator/bluetooth)

Returns a [Bluetooth](/en-US/docs/Web/API/Bluetooth) object for the current document, providing access to Web Bluetooth API functionality.

## [Security considerations](#security_considerations)

The Web Bluetooth API can only be used in a secure context.

Access to the API is controlled by the [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) directive [bluetooth](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/bluetooth). The default allowlist for the `bluetooth` policy is `self`, which enables Bluetooth usage in same-origin nested frames but prevents access by third-party content by default. Cross-origin access is enabled by specifying the allowed origins in both the `Permissions-Policy: bluetooth` HTTP header and the desired `<iframe>`.

In order to use the feature the user must first grant explicit permission (they will not be prompted for access if it is not allowed for other reasons, such as being blocked by a Permissions Policy). The permission prompt is displayed when calling [Bluetooth.requestDevice()](/en-US/docs/Web/API/Bluetooth/requestDevice) to request access to a new Bluetooth device for which permission is not granted (the owning global object must also have [transient activation](/en-US/docs/Glossary/Transient_activation)). You can use [Bluetooth.getDevices()](/en-US/docs/Web/API/Bluetooth/getDevices) to retrieve any devices that have previously been granted permission for the site.

The [Permissions API](/en-US/docs/Web/API/Permissions_API)[navigator.permissions.query()](/en-US/docs/Web/API/Permissions/query) method can be used with the `bluetooth` permission to test whether a site has permission to use Bluetooth devices. The permission state will be `granted`, `denied` or `prompt` (requires user acknowledgement of a prompt):

js

```
const btPermission = await navigator.permissions.query({ name: "bluetooth" });
if (btPermission.state !== "denied") {
  // Do something
}
```

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetooth](https://webbluetoothcg.github.io/web-bluetooth/#bluetooth)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Bluetooth_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_bluetooth_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Bluetooth_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_bluetooth_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Bluetooth_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_bluetooth_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fffa6f5871f50856c60983a125cef7de267be7aeb%0A*+Document+last+modified%3A+2025-05-27T12%3A53%3A43.000Z%0A%0A%3C%2Fdetails%3E)
