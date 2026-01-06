# FetchEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetchEvent&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

This is the event type for `fetch` events dispatched on the [service worker global scope](/en-US/docs/Web/API/ServiceWorkerGlobalScope). It contains information about the fetch, including the request and how the receiver will treat the response. It provides the [event.respondWith()](/en-US/docs/Web/API/FetchEvent/respondWith) method, which allows us to provide a response to this fetch.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FetchEvent()](/en-US/docs/Web/API/FetchEvent/FetchEvent)

Creates a new `FetchEvent` object. This constructor is not typically used. The browser creates these objects and provides them to `fetch` event callbacks.

## [Instance properties](#instance_properties)

Inherits properties from its ancestor, [Event](/en-US/docs/Web/API/Event).

[FetchEvent.clientId](/en-US/docs/Web/API/FetchEvent/clientId)Read only

The [id](/en-US/docs/Web/API/Client/id) of the same-origin [client](/en-US/docs/Web/API/Client) that initiated the fetch.

[FetchEvent.handled](/en-US/docs/Web/API/FetchEvent/handled)Read only

A promise that is pending while the event has not been handled, and fulfilled once it has.

[FetchEvent.isReload](/en-US/docs/Web/API/FetchEvent/isReload)Read onlyDeprecatedNon-standard

Returns `true` if the event was dispatched by the user attempting to reload the page, and `false` otherwise.

[FetchEvent.preloadResponse](/en-US/docs/Web/API/FetchEvent/preloadResponse)Read only

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) for a [Response](/en-US/docs/Web/API/Response), or `undefined` if this fetch is not a navigation, or [navigation preload](/en-US/docs/Web/API/NavigationPreloadManager) is not enabled.

[FetchEvent.replacesClientId](/en-US/docs/Web/API/FetchEvent/replacesClientId)Read only

The [id](/en-US/docs/Web/API/Client/id) of the [client](/en-US/docs/Web/API/Client) that is being replaced during a page navigation.

[FetchEvent.resultingClientId](/en-US/docs/Web/API/FetchEvent/resultingClientId)Read only

The [id](/en-US/docs/Web/API/Client/id) of the [client](/en-US/docs/Web/API/Client) that replaces the previous client during a page navigation.

[FetchEvent.request](/en-US/docs/Web/API/FetchEvent/request)Read only

The [Request](/en-US/docs/Web/API/Request) the browser intends to make.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [ExtendableEvent](/en-US/docs/Web/API/ExtendableEvent).

[FetchEvent.respondWith()](/en-US/docs/Web/API/FetchEvent/respondWith)

Prevent the browser's default fetch handling, and provide (a promise for) a response yourself.

[ExtendableEvent.waitUntil()](/en-US/docs/Web/API/ExtendableEvent/waitUntil)

Extends the lifetime of the event. Used to notify the browser of tasks that extend beyond the returning of a response, such as streaming and caching.

## [Examples](#examples)

This fetch event uses the browser default for non-GET requests. For GET requests it tries to return a match in the cache, and falls back to the network. If it finds a match in the cache, it asynchronously updates the cache for next time.

js

```
self.addEventListener("fetch", (event) => {
  // Let the browser do its default thing
  // for non-GET requests.
  if (event.request.method !== "GET") return;

  // Prevent the default, and handle the request ourselves.
  event.respondWith(
    (async () => {
      // Try to get the response from a cache.
      const cache = await caches.open("dynamic-v1");
      const cachedResponse = await cache.match(event.request);

      if (cachedResponse) {
        // If we found a match in the cache, return it, but also
        // update the entry in the cache in the background.
        event.waitUntil(cache.add(event.request));
        return cachedResponse;
      }

      // If we didn't find a match in the cache, use the network.
      return fetch(event.request);
    })(),
  );
});
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# fetchevent-interface](https://w3c.github.io/ServiceWorker/#fetchevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [fetch event](/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event)
- [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Fetch API](/en-US/docs/Web/API/Fetch_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 31, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FetchEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fetchevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetchEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffetchevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetchEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffetchevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc640274a19227cd5790912ea76841732baa6731f%0A*+Document+last+modified%3A+2024-08-31T23%3A26%3A08.000Z%0A%0A%3C%2Fdetails%3E)
