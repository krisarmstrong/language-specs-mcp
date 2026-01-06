# PeriodicSyncEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPeriodicSyncEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `PeriodicSyncEvent` interface of the [Web Periodic Background Synchronization API](/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API) provides a way to run tasks in the service worker with network connectivity.

An instance of this event is passed to the [periodicsync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/periodicsync_event) handler. This happens periodically, at an interval greater than or equal to that set in the [PeriodicSyncManager.register()](/en-US/docs/Web/API/PeriodicSyncManager/register) method. Other implementation-specific factors such as the user's engagement with the site decide the actual interval.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PeriodicSyncEvent()](/en-US/docs/Web/API/PeriodicSyncEvent/PeriodicSyncEvent)Experimental

Creates a new `PeriodicSyncEvent` object. This constructor is not typically used. The browser creates these objects itself and provides them to [onperiodicsync](/en-US/docs/Web/API/ServiceWorkerGlobalScope/periodicsync_event) callback.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[PeriodicSyncEvent.tag](/en-US/docs/Web/API/PeriodicSyncEvent/tag)Read onlyExperimental

Returns the developer-defined identifier for this `PeriodicSyncEvent`. Multiple tags can be used by the web app to run different periodic tasks at different frequencies.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Examples](#examples)

The following example shows how to respond to a periodic sync event in the service worker.

js

```
self.addEventListener("periodicsync", (event) => {
  if (event.tag === "get-latest-news") {
    event.waitUntil(fetchAndCacheLatestNews());
  }
});
```

`fetchAndCacheLatestNews` is a developer defined function.

## [Specifications](#specifications)

Specification
[Web Periodic Background Synchronization# periodicsync-event](https://wicg.github.io/periodic-background-sync/#periodicsync-event)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Richer offline experiences with the Periodic Background Sync API](https://developer.chrome.com/docs/capabilities/periodic-background-sync)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PeriodicSyncEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/periodicsyncevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPeriodicSyncEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperiodicsyncevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPeriodicSyncEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperiodicsyncevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
