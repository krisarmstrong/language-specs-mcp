# BluetoothRemoteGATTServer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTServer&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `BluetoothRemoteGATTServer` interface of the [Web Bluetooth API](/en-US/docs/Web/API/Web_Bluetooth_API) represents a GATT Server on a remote device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[BluetoothRemoteGATTServer.connected](/en-US/docs/Web/API/BluetoothRemoteGATTServer/connected)Read onlyExperimental

A boolean value that returns true while this script execution environment is connected to `this.device`. It can be false while the user agent is physically connected.

[BluetoothRemoteGATTServer.device](/en-US/docs/Web/API/BluetoothRemoteGATTServer/device)Read onlyExperimental

A reference to the [BluetoothDevice](/en-US/docs/Web/API/BluetoothDevice) running the server.

## [Instance methods](#instance_methods)

[BluetoothRemoteGATTServer.connect()](/en-US/docs/Web/API/BluetoothRemoteGATTServer/connect)Experimental

Causes the script execution environment to connect to `this.device`.

[BluetoothRemoteGATTServer.disconnect()](/en-US/docs/Web/API/BluetoothRemoteGATTServer/disconnect)Experimental

Causes the script execution environment to disconnect from `this.device`.

[BluetoothRemoteGATTServer.getPrimaryService()](/en-US/docs/Web/API/BluetoothRemoteGATTServer/getPrimaryService)Experimental

Returns a promise to the primary [BluetoothRemoteGATTService](/en-US/docs/Web/API/BluetoothRemoteGATTService) offered by the Bluetooth device for a specified `BluetoothServiceUUID`.

[BluetoothRemoteGATTServer.getPrimaryServices()](/en-US/docs/Web/API/BluetoothRemoteGATTServer/getPrimaryServices)Experimental

Returns a promise to a list of primary [BluetoothRemoteGATTService](/en-US/docs/Web/API/BluetoothRemoteGATTService) objects offered by the Bluetooth device for a specified `BluetoothServiceUUID`.

## [Specifications](#specifications)

Specification
[Web Bluetooth# bluetoothgattremoteserver-interface](https://webbluetoothcg.github.io/web-bluetooth/#bluetoothgattremoteserver-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BluetoothRemoteGATTServer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bluetoothremotegattserver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTServer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbluetoothremotegattserver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBluetoothRemoteGATTServer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbluetoothremotegattserver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbfc735c04506625c8c60054fe6f2f136bc43bbea%0A*+Document+last+modified%3A+2024-08-11T15%3A28%3A08.000Z%0A%0A%3C%2Fdetails%3E)
