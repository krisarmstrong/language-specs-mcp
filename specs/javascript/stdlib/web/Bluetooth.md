# Bluetooth

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetooth&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Bluetooth` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) provides methods to query Bluetooth availability and request access to devices.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Inherits properties from its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

[Bluetooth.getAvailability()](/en-US/docs/Web/API/Bluetooth/getAvailability)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a boolean value indicating whether the user agent can support Bluetooth. Some user agents let the user configure an option that specifies what value is returned by this method.

[Bluetooth.getDevices()](/en-US/docs/Web/API/Bluetooth/getDevices)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an array of [BluetoothDevice](/en-US/docs/Web/API/BluetoothDevice)s this origin is allowed to access. Permission is obtained via previous calls to [Bluetooth.requestDevice()](/en-US/docs/Web/API/Bluetooth/requestDevice).

[Bluetooth.requestDevice()](/en-US/docs/Web/API/Bluetooth/requestDevice)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to a [BluetoothDevice](/en-US/docs/Web/API/BluetoothDevice) object matching the specified options.

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetooth](https://webbluetoothcg.github.io/web-bluetooth/#bluetooth)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 15, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Bluetooth/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetooth/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetooth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetooth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetooth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetooth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe676701495a168168e0868311e4c4e7274fb6ed4%0A*+Document+last+modified%3A+2024-08-15T02%3A33%3A23.000Z%0A%0A%3C%2Fdetails%3E)
