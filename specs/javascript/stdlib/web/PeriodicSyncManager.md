# PeriodicSyncManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPeriodicSyncManager&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PeriodicSyncManager` interface of the [Web Periodic Background Synchronization API](/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API) provides a way to register tasks to be run in a service worker at periodic intervals with network connectivity. These tasks are referred to as periodic background sync requests. Access `PeriodicSyncManager` through the [ServiceWorkerRegistration.periodicSync](/en-US/docs/Web/API/ServiceWorkerRegistration/periodicSync).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[PeriodicSyncManager.register()](/en-US/docs/Web/API/PeriodicSyncManager/register)Experimental

Registers a periodic sync request with the browser with the specified tag and options. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the registration completes.

[PeriodicSyncManager.getTags()](/en-US/docs/Web/API/PeriodicSyncManager/getTags)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a list of [strings](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) representing the tags that are currently registered for periodic syncing.

[PeriodicSyncManager.unregister()](/en-US/docs/Web/API/PeriodicSyncManager/unregister)Experimental

Unregisters the periodic sync request corresponding to the specified tag and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when unregistration completes.

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

## [Specifications](#specifications)

Specification
[Web Periodic Background Synchronization# periodicsyncmanager-interface](https://wicg.github.io/periodic-background-sync/#periodicsyncmanager-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Richer offline experiences with the Periodic Background Sync API](https://developer.chrome.com/docs/capabilities/periodic-background-sync)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PeriodicSyncManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/periodicsyncmanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPeriodicSyncManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperiodicsyncmanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPeriodicSyncManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperiodicsyncmanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
