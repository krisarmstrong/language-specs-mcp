# Device Memory API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The capabilities of a client device largely depend on the amount of available RAM. Traditionally, developers had to use heuristics and either benchmark a device or infer device capabilities based on other factors like the device manufacturer or User Agent strings.

## In this article

- [Determining device memory](#determining_device_memory)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Determining device memory](#determining_device_memory)

There are two ways to determine the approximate amount of RAM a device has: use the Device Memory JavaScript API or accept Client Hints.

### [JavaScript API](#javascript_api)

You may query the approximate amount of RAM a device has by retrieving [Navigator.deviceMemory](/en-US/docs/Web/API/Navigator/deviceMemory) or [WorkerNavigator.deviceMemory](/en-US/docs/Web/API/WorkerNavigator/deviceMemory).

js

```
const RAM = navigator.deviceMemory;
```

### [Client Hints](#client_hints)

You may also use the [Client Hints](/en-US/docs/Web/HTTP/Guides/Client_hints) HTTP Header with the `Device-Memory` directive to retrieve the same approximate RAM capacity.

## [Interfaces](#interfaces)

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.deviceMemory](/en-US/docs/Web/API/Navigator/deviceMemory)Read only

Returns the approximate amount of device memory in gigabytes.

[WorkerNavigator.deviceMemory](/en-US/docs/Web/API/WorkerNavigator/deviceMemory)Read only

Returns the approximate amount of device memory in gigabytes.

## [Specifications](#specifications)

Specification[Device Memory](https://www.w3.org/TR/device-memory/)

## [Browser compatibility](#browser_compatibility)

### [api.Navigator.deviceMemory](#api.Navigator.deviceMemory)

### [api.WorkerNavigator.deviceMemory](#api.WorkerNavigator.deviceMemory)

### [http.headers.Sec-CH-Device-Memory](#http.headers.Sec-CH-Device-Memory)

## [See also](#see_also)

- [Sec-CH-Device-Memory](/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Device-Memory) header

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Device_Memory_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/device_memory_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_Memory_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdevice_memory_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDevice_Memory_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdevice_memory_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F53d1a4810a69dc436badd5b73c1a66c8764c835b%0A*+Document+last+modified%3A+2025-12-15T22%3A26%3A18.000Z%0A%0A%3C%2Fdetails%3E)
