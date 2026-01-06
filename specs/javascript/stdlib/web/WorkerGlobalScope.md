# WorkerGlobalScope

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerGlobalScope&level=high)

Note: This feature is only available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WorkerGlobalScope` interface of the [Web Workers API](/en-US/docs/Web/API/Web_Workers_API) is an interface representing the scope of any worker. Workers have no browsing context; this scope contains the information usually conveyed by [Window](/en-US/docs/Web/API/Window) objects — in this case event handlers, the console or the associated [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator) object. Each `WorkerGlobalScope` has its own event loop.

This interface is usually specialized by each worker type: [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) for dedicated workers, [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope) for shared workers, and [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) for [ServiceWorker](/en-US/docs/Web/API/Service_Worker_API). The `self` property returns the specialized scope for each context.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits properties from the [EventTarget](/en-US/docs/Web/API/EventTarget) interface.

[WorkerGlobalScope.caches](/en-US/docs/Web/API/WorkerGlobalScope/caches)Read onlySecure context

Returns the [CacheStorage](/en-US/docs/Web/API/CacheStorage) object associated with the current context. This object enables functionality such as storing assets for offline use, and generating custom responses to requests.

[WorkerGlobalScope.crossOriginIsolated](/en-US/docs/Web/API/WorkerGlobalScope/crossOriginIsolated)Read only

Returns a boolean value that indicates whether the website is in a cross-origin isolation state.

[WorkerGlobalScope.crypto](/en-US/docs/Web/API/WorkerGlobalScope/crypto)Read only

Returns the [Crypto](/en-US/docs/Web/API/Crypto) object associated to the global object.

[WorkerGlobalScope.fonts](/en-US/docs/Web/API/WorkerGlobalScope/fonts)Read only

Returns the [FontFaceSet](/en-US/docs/Web/API/FontFaceSet) associated with the worker.

[WorkerGlobalScope.indexedDB](/en-US/docs/Web/API/WorkerGlobalScope/indexedDB)Read only

Provides a mechanism for workers to asynchronously access capabilities of indexed databases; returns an [IDBFactory](/en-US/docs/Web/API/IDBFactory) object.

[WorkerGlobalScope.isSecureContext](/en-US/docs/Web/API/WorkerGlobalScope/isSecureContext)Read only

Returns a boolean indicating whether the current context is secure (`true`) or not (`false`).

[WorkerGlobalScope.location](/en-US/docs/Web/API/WorkerGlobalScope/location)Read only

Returns the [WorkerLocation](/en-US/docs/Web/API/WorkerLocation) associated with the worker. It is a specific location object, mostly a subset of the [Location](/en-US/docs/Web/API/Location) for browsing scopes, but adapted to workers.

[WorkerGlobalScope.navigator](/en-US/docs/Web/API/WorkerGlobalScope/navigator)Read only

Returns the [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator) associated with the worker. It is a specific navigator object, mostly a subset of the [Navigator](/en-US/docs/Web/API/Navigator) for browsing scopes, but adapted to workers.

[WorkerGlobalScope.origin](/en-US/docs/Web/API/WorkerGlobalScope/origin)Read only

Returns the global object's origin, serialized as a string.

[WorkerGlobalScope.performance](/en-US/docs/Web/API/WorkerGlobalScope/performance)Read only

Returns the [Performance](/en-US/docs/Web/API/Performance) associated with the worker. Only a subset of the properties and methods of the `Performance` interface are available to workers.

[WorkerGlobalScope.scheduler](/en-US/docs/Web/API/WorkerGlobalScope/scheduler)Read only

Returns the [Scheduler](/en-US/docs/Web/API/Scheduler) object associated with the current context. This is the entry point for using the [Prioritized Task Scheduling API](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API).

[WorkerGlobalScope.trustedTypes](/en-US/docs/Web/API/WorkerGlobalScope/trustedTypes)Read only

Returns the [TrustedTypePolicyFactory](/en-US/docs/Web/API/TrustedTypePolicyFactory) object associated with the global object, providing the entry point for using the [Trusted Types API](/en-US/docs/Web/API/Trusted_Types_API).

[WorkerGlobalScope.self](/en-US/docs/Web/API/WorkerGlobalScope/self)Read only

Returns a reference to the `WorkerGlobalScope` itself. Most of the time it is a specific scope like [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope), [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope) or [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope).

## [Instance methods](#instance_methods)

This interface inherits methods from the [EventTarget](/en-US/docs/Web/API/EventTarget) interface.

[WorkerGlobalScope.atob()](/en-US/docs/Web/API/WorkerGlobalScope/atob)

Decodes a string of data which has been encoded using base-64 encoding.

[WorkerGlobalScope.btoa()](/en-US/docs/Web/API/WorkerGlobalScope/btoa)

Creates a base-64 encoded [ASCII](/en-US/docs/Glossary/ASCII) string from a string of binary data.

[WorkerGlobalScope.clearInterval()](/en-US/docs/Web/API/WorkerGlobalScope/clearInterval)

Cancels the repeated execution set using [WorkerGlobalScope.setInterval()](/en-US/docs/Web/API/WorkerGlobalScope/setInterval).

[WorkerGlobalScope.clearTimeout()](/en-US/docs/Web/API/WorkerGlobalScope/clearTimeout)

Cancels the delayed execution set using [WorkerGlobalScope.setTimeout()](/en-US/docs/Web/API/WorkerGlobalScope/setTimeout).

[WorkerGlobalScope.createImageBitmap()](/en-US/docs/Web/API/WorkerGlobalScope/createImageBitmap)

Accepts a variety of different image sources, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves to an [ImageBitmap](/en-US/docs/Web/API/ImageBitmap). Optionally the source is cropped to the rectangle of pixels originating at (sx, sy) with width sw, and height sh.

[WorkerGlobalScope.dump()](/en-US/docs/Web/API/WorkerGlobalScope/dump)DeprecatedNon-standard

Allows you to write a message to stdout — i.e., in your terminal. This is the same as Firefox's [window.dump](/en-US/docs/Web/API/Window/dump), but for workers.

[WorkerGlobalScope.fetch()](/en-US/docs/Web/API/WorkerGlobalScope/fetch)

Starts the process of fetching a resource from the network.

[WorkerGlobalScope.importScripts()](/en-US/docs/Web/API/WorkerGlobalScope/importScripts)

Imports one or more scripts into the worker's scope. You can specify as many as you'd like, separated by commas. For example: `importScripts('foo.js', 'bar.js');`.

[WorkerGlobalScope.queueMicrotask()](/en-US/docs/Web/API/WorkerGlobalScope/queueMicrotask)

Queues a microtask to be executed at a safe time prior to control returning to the browser's event loop.

[WorkerGlobalScope.setInterval()](/en-US/docs/Web/API/WorkerGlobalScope/setInterval)

Schedules a function to execute every time a given number of milliseconds elapses.

[WorkerGlobalScope.setTimeout()](/en-US/docs/Web/API/WorkerGlobalScope/setTimeout)

Schedules a function to execute in a given amount of time.

[WorkerGlobalScope.structuredClone()](/en-US/docs/Web/API/WorkerGlobalScope/structuredClone)

Creates a [deep clone](/en-US/docs/Glossary/Deep_copy) of a given value using the [structured clone algorithm](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm).

[WorkerGlobalScope.reportError()](/en-US/docs/Web/API/WorkerGlobalScope/reportError)

Reports an error in a script, emulating an unhandled exception.

## [Events](#events)

[error](/en-US/docs/Web/API/WorkerGlobalScope/error_event)

Fired when an error occurred.

[languagechange](/en-US/docs/Web/API/WorkerGlobalScope/languagechange_event)

Fired at the global/worker scope object when the user's preferred languages change.

[offline](/en-US/docs/Web/API/WorkerGlobalScope/offline_event)

Fired when the browser has lost access to the network and the value of `navigator.onLine` switched to `false`.

[online](/en-US/docs/Web/API/WorkerGlobalScope/online_event)

Fired when the browser has gained access to the network and the value of `navigator.onLine` switched to `true`.

[rejectionhandled](/en-US/docs/Web/API/WorkerGlobalScope/rejectionhandled_event)

Fired on handled [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) rejection events.

[securitypolicyviolation](/en-US/docs/Web/API/WorkerGlobalScope/securitypolicyviolation_event)

Fired when a [Content Security Policy](/en-US/docs/Web/HTTP/Guides/CSP) is violated.

[unhandledrejection](/en-US/docs/Web/API/WorkerGlobalScope/unhandledrejection_event)

Fired on unhandled [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) rejection events.

## [Example](#example)

You won't access `WorkerGlobalScope` directly in your code; however, its properties and methods are inherited by more specific global scopes such as [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) and [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope). For example, you could import another script into the worker and print out the contents of the worker scope's `navigator` object using the following two lines:

js

```
importScripts("foo.js");
console.log(navigator);
```

Note: Since the global scope of the worker script is effectively the global scope of the worker you are running ([DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope) or whatever) and all worker global scopes inherit methods, properties, etc. from `WorkerGlobalScope`, you can run lines such as those above without specifying a parent object.

## [Specifications](#specifications)

Specification
[HTML# the-workerglobalscope-common-interface](https://html.spec.whatwg.org/multipage/workers.html#the-workerglobalscope-common-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Other global object interface: [Window](/en-US/docs/Web/API/Window), [DedicatedWorkerGlobalScope](/en-US/docs/Web/API/DedicatedWorkerGlobalScope), [SharedWorkerGlobalScope](/en-US/docs/Web/API/SharedWorkerGlobalScope), [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope)
- Other Worker-related interfaces: [Worker](/en-US/docs/Web/API/Worker), [WorkerLocation](/en-US/docs/Web/API/WorkerLocation) and [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WorkerGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/workerglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fworkerglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fworkerglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
