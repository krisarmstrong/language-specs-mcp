# Web Periodic Background Synchronization API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Web Periodic Background Synchronization API provides a way to register tasks to be run in a [service worker](/en-US/docs/Web/API/Service_Worker_API) at periodic intervals with network connectivity. These tasks are referred to as periodic background sync requests.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

The Periodic Background Sync API allows web applications to alert their service worker to make any updates, at a periodic time interval. Uses may include fetching latest content whilst a device is connected to Wi-Fi, or allowing background updates to an application.

The minimum time interval is set when the API is invoked; however the user agent might also take into account other factors which affect when the service worker receives the event. For instance previous website engagement, or connection to a known network.

The [PeriodicSyncManager](/en-US/docs/Web/API/PeriodicSyncManager) interface is available through [ServiceWorkerRegistration.periodicSync](/en-US/docs/Web/API/ServiceWorkerRegistration/periodicSync). A unique tag identifier is set to 'name' the sync event, which can then be listened for within the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) script. Once the event is received you can then run any functionality available, such as updating caches or fetching new resources.

As this API relies on service workers, functionality provided by this API is only available in a secure context.

## [Interfaces](#interfaces)

[PeriodicSyncManager](/en-US/docs/Web/API/PeriodicSyncManager)Experimental

Registers tasks to be run in a service worker at periodic intervals with network connectivity. These tasks are referred to as periodic background sync requests.

[PeriodicSyncEvent](/en-US/docs/Web/API/PeriodicSyncEvent)Experimental

Represents a synchronization event, sent to the [global scope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/Service_Worker_API). It provides a way to run tasks in the service worker with network connectivity.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The following additions to the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) are specified in the Periodic Background Sync specification to provide an entry point for using Periodic Background Sync.

[ServiceWorkerRegistration.periodicSync](/en-US/docs/Web/API/ServiceWorkerRegistration/periodicSync)Read onlyExperimental

Returns a reference to the [PeriodicSyncManager](/en-US/docs/Web/API/PeriodicSyncManager) interface for registering tasks to run at specific intervals.

[periodicsync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/periodicsync_event) event Experimental

Occurs at periodic intervals, which were specified when registering a [PeriodicSyncManager](/en-US/docs/Web/API/PeriodicSyncManager).

## [Examples](#examples)

The following examples show how to use the interface.

### [Requesting a Periodic Background Sync](#requesting_a_periodic_background_sync)

The following asynchronous function registers a periodic background sync at a minimum interval of one day from a browsing context:

js

```
async function registerPeriodicNewsCheck() {
  const registration = await navigator.serviceWorker.ready;
  try {
    await registration.periodicSync.register("get-latest-news", {
      minInterval: 24 * 60 * 60 * 1000,
    });
  } catch {
    console.log("Periodic Sync could not be registered!");
  }
}
```

### [Verifying a Background Periodic Sync by Tag](#verifying_a_background_periodic_sync_by_tag)

This code checks to see if a Periodic Background Sync task with a given tag is registered.

js

```
navigator.serviceWorker.ready.then((registration) => {
  registration.periodicSync.getTags().then((tags) => {
    if (tags.includes("get-latest-news")) skipDownloadingLatestNewsOnPageLoad();
  });
});
```

### [Removing a Periodic Background Sync Task](#removing_a_periodic_background_sync_task)

The following code removes a Periodic Background Sync task to stop articles syncing in the background.

js

```
navigator.serviceWorker.ready.then((registration) => {
  registration.periodicSync.unregister("get-latest-news");
});
```

### [Listening for a Periodic Background Sync within a Service Worker](#listening_for_a_periodic_background_sync_within_a_service_worker)

The following example shows how to respond to a periodic sync event in the service worker.

js

```
self.addEventListener("periodicsync", (event) => {
  if (event.tag === "get-latest-news") {
    event.waitUntil(fetchAndCacheLatestNews());
  }
});
```

## [Specifications](#specifications)

Specification[Web Periodic Background Synchronization](https://wicg.github.io/periodic-background-sync/)

## [Browser compatibility](#browser_compatibility)

### [api.PeriodicSyncManager](#api.PeriodicSyncManager)

### [api.ServiceWorkerGlobalScope.periodicsync_event](#api.ServiceWorkerGlobalScope.periodicsync_event)

## [See also](#see_also)

- [An article on using Periodic Background Sync](https://developer.chrome.com/docs/capabilities/periodic-background-sync)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_periodic_background_synchronization_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Periodic_Background_Synchronization_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_periodic_background_synchronization_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Periodic_Background_Synchronization_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_periodic_background_synchronization_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
