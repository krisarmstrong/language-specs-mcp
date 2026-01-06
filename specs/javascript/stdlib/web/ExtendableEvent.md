# ExtendableEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableEvent&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `ExtendableEvent` interface extends the lifetime of the [install](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event) and [activate](/en-US/docs/Web/API/ServiceWorkerGlobalScope/activate_event) events dispatched on the global scope as part of the service worker lifecycle. This ensures that any functional events (like [FetchEvent](/en-US/docs/Web/API/FetchEvent)) are not dispatched until it upgrades database schemas and deletes the outdated cache entries.

If [waitUntil()](/en-US/docs/Web/API/ExtendableEvent/waitUntil) is called outside of the `ExtendableEvent` handler, the browser should throw an `InvalidStateError`; note also that multiple calls will stack up, and the resulting promises will be added to the list of [extend lifetime promises](https://w3c.github.io/ServiceWorker/#extendableevent-extend-lifetime-promises).

This interface inherits from the [Event](/en-US/docs/Web/API/Event) interface.

Note: This interface is only available when the global scope is a [ServiceWorkerGlobalScope](/en-US/docs/Web/API/ServiceWorkerGlobalScope). It is not available when it is a [Window](/en-US/docs/Web/API/Window), or the scope of another kind of worker.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ExtendableEvent()](/en-US/docs/Web/API/ExtendableEvent/ExtendableEvent)

Creates a new `ExtendableEvent` object.

## [Instance properties](#instance_properties)

Doesn't implement any specific properties, but inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

[ExtendableEvent.waitUntil()](/en-US/docs/Web/API/ExtendableEvent/waitUntil)

Extends the lifetime of the event. It is intended to be called in the [install](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event)[event handler](/en-US/docs/Web/API/Document_Object_Model/Events#registering_event_handlers) for the [installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing) worker and on the [activate](/en-US/docs/Web/API/ServiceWorkerGlobalScope/activate_event)[event handler](/en-US/docs/Web/API/Document_Object_Model/Events#registering_event_handlers) for the [active](/en-US/docs/Web/API/ServiceWorkerRegistration/active) worker.

## [Examples](#examples)

This code snippet is from the [service worker prefetch sample](https://github.com/GoogleChrome/samples/blob/gh-pages/service-worker/prefetch/service-worker.js) (see [prefetch example live](https://googlechrome.github.io/samples/service-worker/prefetch/).) The code calls [ExtendableEvent.waitUntil()](/en-US/docs/Web/API/ExtendableEvent/waitUntil) in [oninstall](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event), delaying treating the [ServiceWorkerRegistration.installing](/en-US/docs/Web/API/ServiceWorkerRegistration/installing) worker as installed until the passed promise resolves successfully. The promise resolves when all resources have been fetched and cached, or else when any exception occurs.

The code snippet also shows a best practice for versioning caches used by the service worker. Though there's only one cache in this example, the same approach can be used for multiple caches. It maps a shorthand identifier for a cache to a specific, versioned cache name.

Note: In Chrome, logging statements are visible via the "Inspect" interface for the relevant service worker accessed via chrome://serviceworker-internals.

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

Note: When fetching resources, it's very important to use `{mode: 'no-cors'}` if there is any chance that the resources are served off of a server that doesn't support [CORS](/en-US/docs/Glossary/CORS). In this example, [www.chromium.org](https://www.chromium.org/) doesn't support CORS.

## [Specifications](#specifications)

Specification
[Service Workers Nightly# extendableevent-interface](https://w3c.github.io/ServiceWorker/#extendableevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers basic code example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 29, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ExtendableEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/extendableevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fextendableevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FExtendableEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fextendableevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff4c0e822eb6a1ea438c7342f43a3e4809adbd56a%0A*+Document+last+modified%3A+2025-07-29T01%3A48%3A17.000Z%0A%0A%3C%2Fdetails%3E)
