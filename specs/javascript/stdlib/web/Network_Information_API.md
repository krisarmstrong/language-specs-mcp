# Network Information API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNetwork_Information_API&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Network Information API provides information about the system's connection in terms of general connection type (e.g., 'wifi, 'cellular', etc.). This can be used to select high definition content or low definition content based on the user's connection.

The interface consists of a single [NetworkInformation](/en-US/docs/Web/API/NetworkInformation) object, an instance of which is returned by the [Navigator.connection](/en-US/docs/Web/API/Navigator/connection) property or the [WorkerNavigator.connection](/en-US/docs/Web/API/WorkerNavigator/connection) property.

## In this article

- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

[NetworkInformation](/en-US/docs/Web/API/NetworkInformation)

Provides information about the connection a device is using to communicate with the network and provides a means for scripts to be notified if the connection type changes. The `NetworkInformation` interface cannot be instantiated. It is instead accessed through the [Navigator](/en-US/docs/Web/API/Navigator) interface or the [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator) interface.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.connection](/en-US/docs/Web/API/Navigator/connection)Read only

Returns a [NetworkInformation](/en-US/docs/Web/API/NetworkInformation) object containing information about the network connection of a device.

[WorkerNavigator.connection](/en-US/docs/Web/API/WorkerNavigator/connection)Read only

Provides a [NetworkInformation](/en-US/docs/Web/API/NetworkInformation) object containing information about the network connection of a device.

## [Examples](#examples)

### [Detect connection changes](#detect_connection_changes)

This example watches for changes to the user's connection.

js

```
let type = navigator.connection.effectiveType;

function updateConnectionStatus() {
  console.log(
    `Connection type changed from ${type} to ${navigator.connection.effectiveType}`,
  );
  type = navigator.connection.effectiveType;
}

navigator.connection.addEventListener("change", updateConnectionStatus);
```

### [Preload large resources](#preload_large_resources)

The connection object is useful for deciding whether to preload resources that take large amounts of bandwidth or memory. This example would be called soon after page load to check for a connection type where preloading a video may not be desirable. If a cellular connection is found, then the `preloadVideo` flag is set to `false`. For simplicity and clarity, this example only tests for one connection type. A real-world use case would likely use a switch statement or some other method to check all of the possible values of [NetworkInformation.type](/en-US/docs/Web/API/NetworkInformation/type). Regardless of the `type` value you can get an estimate of connection speed through the [NetworkInformation.effectiveType](/en-US/docs/Web/API/NetworkInformation/effectiveType) property.

js

```
let preloadVideo = true;
const connection = navigator.connection;
if (connection) {
  if (connection.effectiveType === "slow-2g") {
    preloadVideo = false;
  }
}
```

## [Specifications](#specifications)

Specification[Network Information API](https://wicg.github.io/netinfo/)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Online and offline events](/en-US/docs/Web/API/Navigator/onLine)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Network_Information_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/network_information_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNetwork_Information_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnetwork_information_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNetwork_Information_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnetwork_information_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1fae6a1db8be34bc73fb9d1e0fb058c253045853%0A*+Document+last+modified%3A+2025-04-13T06%3A32%3A19.000Z%0A%0A%3C%2Fdetails%3E)
