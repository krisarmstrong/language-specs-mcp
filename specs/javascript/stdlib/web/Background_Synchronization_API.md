# Background Synchronization API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Background Synchronization API enables a web app to defer tasks so that they can be run in a [service worker](/en-US/docs/Web/API/Service_Worker_API) once the user has a stable network connection.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The Background Synchronization API allows web applications to defer server synchronization work to their service worker to handle at a later time, if the device is offline. Uses may include sending requests in the background if they couldn't be sent while the application was being used.

For example, an email client application could let its users compose and send messages at any time, even when the device has no network connection. The application frontend just registers a sync request and the service worker gets alerted when the network is present again and handles the sync.

The [SyncManager](/en-US/docs/Web/API/SyncManager) interface is available through [ServiceWorkerRegistration.sync](/en-US/docs/Web/API/ServiceWorkerRegistration/sync). A unique tag identifier is set to 'name' the sync event, which can then be listened for within the [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) script. Once the event is received you can then run any functionality available, such as sending requests to the server.

As this API relies on service workers, functionality provided by this API is only available in a secure context.

## [Interfaces](#interfaces)

[SyncManager](/en-US/docs/Web/API/SyncManager)Experimental

Registers tasks to be run in a service worker at a later time with network connectivity. These tasks are referred to as background sync requests.

[SyncEvent](/en-US/docs/Web/API/SyncEvent)Experimental

Represents a synchronization event, sent to the [global scope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker). It provides a way to run tasks in the service worker once the device has network connectivity.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The following additions to the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) provide an entry point for setting up background synchronization.

[ServiceWorkerRegistration.sync](/en-US/docs/Web/API/ServiceWorkerRegistration/sync)Read only

Returns a reference to the [SyncManager](/en-US/docs/Web/API/SyncManager) interface for registering tasks to run once the device has network connectivity.

[sync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/sync_event) event

An event handler fired whenever a [sync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/sync_event) event occurs. This happens as soon as the network becomes available.

## [Examples](#examples)

The following examples show how to use the interface.

### [Requesting a background sync](#requesting_a_background_sync)

The following asynchronous function registers a background sync from a browsing context:

js

```
async function syncMessagesLater() {
  const registration = await navigator.serviceWorker.ready;
  try {
    await registration.sync.register("sync-messages");
  } catch {
    console.log("Background Sync could not be registered!");
  }
}
```

### [Verifying a background sync by Tag](#verifying_a_background_sync_by_tag)

This code checks to see if a background sync task with a given tag is registered.

js

```
navigator.serviceWorker.ready.then((registration) => {
  registration.sync.getTags().then((tags) => {
    if (tags.includes("sync-messages")) {
      console.log("Messages sync already requested");
    }
  });
});
```

### [Listening for a background sync within a Service Worker](#listening_for_a_background_sync_within_a_service_worker)

The following example shows how to respond to a background sync event in the service worker.

js

```
self.addEventListener("sync", (event) => {
  if (event.tag === "sync-messages") {
    event.waitUntil(sendOutboxMessages());
  }
});
```

## [Specifications](#specifications)

Specification[Web Background Synchronization](https://wicg.github.io/background-sync/spec/)

## [Browser compatibility](#browser_compatibility)

### [api.SyncManager](#api.SyncManager)

### [api.ServiceWorkerGlobalScope.sync_event](#api.ServiceWorkerGlobalScope.sync_event)

## [See also](#see_also)

- [Introducing Background Sync](https://developer.chrome.com/blog/background-sync/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Background_Synchronization_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/background_synchronization_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackground_Synchronization_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackground_synchronization_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackground_Synchronization_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackground_synchronization_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdd84b3b089d199be3771d6afe01e068b19889e71%0A*+Document+last+modified%3A+2024-04-22T06%3A26%3A49.000Z%0A%0A%3C%2Fdetails%3E)
