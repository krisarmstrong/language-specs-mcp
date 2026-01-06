# InstallEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInstallEvent&level=high)

The parameter passed into an [install](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event) event handler function, the `InstallEvent` interface represents an install action that is dispatched on the [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope) of a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker). As a child of [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent), it ensures that functional events such as [FetchEvent](/en-US/docs/Web/API/FetchEvent) are not dispatched during installation.

This interface inherits from the [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent) interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[InstallEvent()](/en-US/docs/Web/API/InstallEvent/InstallEvent)Experimental

Creates a new `InstallEvent` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[addRoutes()](/en-US/docs/Web/API/InstallEvent/addRoutes)Experimental

Specifies one or more static routes, which define rules for fetching specified resources that will be used even before service worker startup.

## [Examples](#examples)

This code snippet is from the [service worker prefetch sample](https://github.com/GoogleChrome/samples/blob/gh-pages/service-worker/prefetch/service-worker.js) (see [prefetch running live](https://googlechrome.github.io/samples/service-worker/prefetch/).) The code calls [ExtendableEvent.waitUntil()](/en-US/docs/Web/API/ExtendableEvent/waitUntil) in [ServiceWorkerGlobalScope.oninstall](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event) and delays treating the [ServiceWorkerRegistration.installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing) worker as installed until the passed promise resolves successfully. The promise resolves when all resources have been fetched and cached, or when any exception occurs.

The code snippet also shows a best practice for versioning caches used by the service worker. Although this example has only one cache, you can use this approach for multiple caches. The code maps a shorthand identifier for a cache to a specific, versioned cache name.

Note: Logging statements are visible in Google Chrome via the "Inspect" interface for the relevant service worker accessed via chrome://serviceworker-internals.

js

```
const CACHE_VERSION = 1;
const CURRENT_CACHES = {
  prefetch: `prefetch-cache-v${CACHE_VERSION}`,
};

self.addEventListener("install", (event) => {
  const urlsToPrefetch = [
    "./static/pre_fetched.txt",
    "./static/pre_fetched.html",
    "https://www.chromium.org/_/rsrc/1302286216006/config/customLogo.gif",
  ];

  console.log(
    "Handling install event. Resources to pre-fetch:",
    urlsToPrefetch,
  );

  event.waitUntil(
    caches
      .open(CURRENT_CACHES["prefetch"])
      .then((cache) =>
        cache.addAll(
          urlsToPrefetch.map(
            (urlToPrefetch) => new Request(urlToPrefetch, { mode: "no-cors" }),
          ),
        ),
      )
      .then(() => {
        console.log("All resources have been fetched and cached.");
      })
      .catch((error) => {
        console.error("Pre-fetching failed:", error);
      }),
  );
});
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# installevent](https://w3c.github.io/ServiceWorker/#installevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [install event](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event)
- [NotificationEvent](/en-US/docs/Web/API/NotificationEvent)
- [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Fetch API](/en-US/docs/Web/API/Fetch_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/InstallEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/installevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInstallEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finstallevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInstallEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finstallevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4a0413ef319179b7d0d833c42a156629544c8248%0A*+Document+last+modified%3A+2025-05-23T12%3A39%3A21.000Z%0A%0A%3C%2Fdetails%3E)
