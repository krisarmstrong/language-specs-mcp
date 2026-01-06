# WorkerNavigator

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerNavigator&level=high)

Note: This feature is only available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WorkerNavigator` interface represents a subset of the [Navigator](/en-US/docs/Web/API/Navigator) interface allowed to be accessed from a [Worker](/en-US/docs/Web/API/Worker). Such an object is initialized for each worker and is available via the [self.navigator](/en-US/docs/Web/API/WorkerGlobalScope/navigator) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `WorkerNavigator` interface doesn't inherit any property.

[WorkerNavigator.appCodeName](/en-US/docs/Web/API/WorkerNavigator/appCodeName)DeprecatedRead only

Always returns `'Mozilla'`, in any browser. This property is kept only for compatibility purposes.

[WorkerNavigator.appName](/en-US/docs/Web/API/WorkerNavigator/appName)DeprecatedRead only

Returns the official name of the browser. Do not rely on this property to return the correct value.

[WorkerNavigator.appVersion](/en-US/docs/Web/API/WorkerNavigator/appVersion)DeprecatedRead only

Returns the version of the browser as a string. Do not rely on this property to return the correct value.

[WorkerNavigator.connection](/en-US/docs/Web/API/WorkerNavigator/connection)Read only

Provides a [NetworkInformation](/en-US/docs/Web/API/NetworkInformation) object containing information about the network connection of a device.

[WorkerNavigator.deviceMemory](/en-US/docs/Web/API/WorkerNavigator/deviceMemory)Read onlySecure context

Returns the amount of device memory in gigabytes. This value is an approximation given by rounding to the nearest power of 2 and dividing that number by 1024.

[WorkerNavigator.globalPrivacyControl](/en-US/docs/Web/API/WorkerNavigator/globalPrivacyControl)Read onlyExperimental

Returns a boolean indicating a user's consent to their information being shared or sold.

[WorkerNavigator.gpu](/en-US/docs/Web/API/WorkerNavigator/gpu)Read onlySecure context

Returns the [GPU](/en-US/docs/Web/API/GPU) object for the current worker context. The entry point for the [WebGPU API](/en-US/docs/Web/API/WebGPU_API).

[WorkerNavigator.hardwareConcurrency](/en-US/docs/Web/API/WorkerNavigator/hardwareConcurrency)Read only

Returns the number of logical processor cores available.

[WorkerNavigator.hid](/en-US/docs/Web/API/WorkerNavigator/hid)Read onlyExperimentalSecure context

Returns an [HID](/en-US/docs/Web/API/HID) object providing methods for connecting to HID devices already granted permission by the user and listing attached HID devices, and event handlers for responding to HID devices connecting and disconnecting.

[WorkerNavigator.language](/en-US/docs/Web/API/WorkerNavigator/language)Read only

Returns a string representing the preferred language of the user, usually the language of the browser UI. The `null` value is returned when this is unknown.

[WorkerNavigator.languages](/en-US/docs/Web/API/WorkerNavigator/languages)Read only

Returns an array of strings representing the languages known to the user, by order of preference.

[WorkerNavigator.locks](/en-US/docs/Web/API/WorkerNavigator/locks)Read onlySecure context

Returns a [LockManager](/en-US/docs/Web/API/LockManager) object which provides methods for requesting a new [Lock](/en-US/docs/Web/API/Lock) object and querying for an existing [Lock](/en-US/docs/Web/API/Lock) object.

[WorkerNavigator.mediaCapabilities](/en-US/docs/Web/API/WorkerNavigator/mediaCapabilities)Read only

Returns a [MediaCapabilities](/en-US/docs/Web/API/MediaCapabilities) object that can expose information about the decoding and encoding capabilities for a given format and output capabilities.

[WorkerNavigator.onLine](/en-US/docs/Web/API/WorkerNavigator/onLine)Read only

Returns a boolean value indicating whether the browser is online.

[WorkerNavigator.permissions](/en-US/docs/Web/API/WorkerNavigator/permissions)Read only

Returns a [Permissions](/en-US/docs/Web/API/Permissions) object that can be used to query and update permission status of APIs covered by the [Permissions API](/en-US/docs/Web/API/Permissions_API).

[WorkerNavigator.platform](/en-US/docs/Web/API/WorkerNavigator/platform)DeprecatedRead only

Returns a string representing the platform of the browser. Do not rely on this property to return the correct value.

[WorkerNavigator.product](/en-US/docs/Web/API/WorkerNavigator/product)DeprecatedRead only

Always returns `'Gecko'`, on any browser. This property is kept only for compatibility purposes.

[WorkerNavigator.serial](/en-US/docs/Web/API/WorkerNavigator/serial)Read onlyExperimentalSecure context

Returns a [Serial](/en-US/docs/Web/API/Serial) object, which represents the entry point into the [Web Serial API](/en-US/docs/Web/API/Web_Serial_API), to enable the control of serial ports.

[WorkerNavigator.serviceWorker](/en-US/docs/Web/API/WorkerNavigator/serviceWorker)Read onlySecure context

Returns a [ServiceWorkerContainer](/en-US/docs/Web/API/ServiceWorkerContainer) object, which provides access to registration, removal, upgrade, and communication with the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) objects for the [associated document](https://html.spec.whatwg.org/multipage/browsers.html#concept-document-window).

[WorkerNavigator.storage](/en-US/docs/Web/API/WorkerNavigator/storage)Read onlySecure context

Returns a [StorageManager](/en-US/docs/Web/API/StorageManager) interface for managing persistence permissions and estimating available storage.

[WorkerNavigator.usb](/en-US/docs/Web/API/WorkerNavigator/usb)Read onlySecure context

Returns a [USB](/en-US/docs/Web/API/USB) object for the current document, providing access to [WebUSB API](/en-US/docs/Web/API/WebUSB_API) functionality.

[WorkerNavigator.userAgent](/en-US/docs/Web/API/WorkerNavigator/userAgent)Read only

Returns the user agent string for the current browser.

[WorkerNavigator.userAgentData](/en-US/docs/Web/API/WorkerNavigator/userAgentData)Read onlyExperimentalSecure context

Returns a [NavigatorUAData](/en-US/docs/Web/API/NavigatorUAData) object, which gives access to information about the browser and operating system of the user.

## [Instance methods](#instance_methods)

The `WorkerNavigator` interface doesn't inherit any method.

[WorkerNavigator.clearAppBadge()](/en-US/docs/Web/API/WorkerNavigator/clearAppBadge)Secure context

Clears a badge on the current app's icon and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).

[WorkerNavigator.setAppBadge()](/en-US/docs/Web/API/WorkerNavigator/setAppBadge)Secure context

Sets a badge on the icon associated with this app and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).

## [Specifications](#specifications)

Specification
[HTML# the-workernavigator-object](https://html.spec.whatwg.org/multipage/workers.html#the-workernavigator-object)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Other Worker-related interfaces: [Worker](/en-US/docs/Web/API/Worker), [WorkerLocation](/en-US/docs/Web/API/WorkerLocation), and [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WorkerNavigator/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/workernavigator/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerNavigator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fworkernavigator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerNavigator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fworkernavigator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
