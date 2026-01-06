# NavigationPreloadManager

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationPreloadManager&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `NavigationPreloadManager` interface of the [Service Worker API](/en-US/docs/Web/API/Service_Worker_API) provides methods for managing the preloading of resources in parallel with service worker bootup.

If supported, an object of this type is returned by [ServiceWorkerRegistration.navigationPreload](/en-US/docs/Web/API/ServiceWorkerRegistration/navigationPreload). The result of a preload fetch request is waited on using the promise returned by [FetchEvent.preloadResponse](/en-US/docs/Web/API/FetchEvent/preloadResponse).

## In this article

- [Instance methods](#instance_methods)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[NavigationPreloadManager.enable()](/en-US/docs/Web/API/NavigationPreloadManager/enable)

Enables navigation preloading, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).

[NavigationPreloadManager.disable()](/en-US/docs/Web/API/NavigationPreloadManager/disable)

Disables navigation preloading, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined).

[NavigationPreloadManager.setHeaderValue()](/en-US/docs/Web/API/NavigationPreloadManager/setHeaderValue)

Sets the value of the [Service-Worker-Navigation-Preload](/en-US/docs/Web/HTTP/Reference/Headers/Service-Worker-Navigation-Preload) HTTP header sent in preloading requests and returns an empty [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

[NavigationPreloadManager.getState()](/en-US/docs/Web/API/NavigationPreloadManager/getState)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an object with properties that indicate whether preloading is enabled, and what value will be sent in the [Service-Worker-Navigation-Preload](/en-US/docs/Web/HTTP/Reference/Headers/Service-Worker-Navigation-Preload) HTTP header in preloading requests.

## [Description](#description)

Service workers handle [fetch()](/en-US/docs/Web/API/Window/fetch) events on behalf of a site, for pages within a given scope. When a user navigates to a page that uses a service worker, the browser boots up the worker (if it isn't already running), then sends it a fetch event and waits for the result. On receiving an event, the worker returns the resource from a cache if it is present, or otherwise fetches the resource from the remote server (storing a copy for returning in future requests).

A service worker cannot process events from the browser until it has booted. This is unavoidable, but usually doesn't have much impact. Service workers are often already started (they remain active for some time after processing other requests). Even if a service worker does have to boot, much of the time it may be returning values from a cache, which is very fast. However, in those cases where a worker has to boot before it can start fetching a remote resource, then the delay can be significant.

The `NavigationPreloadManager` provides a mechanism to allow fetching of the resources to run in parallel with service worker boot, so that by the time the worker is able to handle the fetch request from the browser, the resource may already have been fully or partially downloaded. This makes the case where the worker has to start up "no worse" than when the worker is already started, and in some cases better.

The preload manager sends the [Service-Worker-Navigation-Preload](/en-US/docs/Web/HTTP/Reference/Headers/Service-Worker-Navigation-Preload) HTTP header with preload requests, allowing responses to be customized for preload requests. This might be used, for example, to reduce the data sent to just part of the original page, or to customize the response based on the user's log-in state.

## [Examples](#examples)

The examples here are from [Speed up Service Worker with Navigation Preloads](https://web.dev/blog/navigation-preload) (developer.chrome.com).

### [Feature detection and enabling navigation preloading](#feature_detection_and_enabling_navigation_preloading)

Below we enable navigation preloading in the service worker's `activate` event handler, after first using [ServiceWorkerRegistration.navigationPreload](/en-US/docs/Web/API/ServiceWorkerRegistration/navigationPreload) to determine if the feature is supported (this returns either the `NavigationPreloadManager` for the service worker or `undefined` if the feature is not supported).

js

```
addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      if (self.registration.navigationPreload) {
        // Enable navigation preloads!
        await self.registration.navigationPreload.enable();
      }
    })(),
  );
});
```

### [Using a preloaded response](#using_a_preloaded_response)

The following code shows a service worker fetch event handler that uses a preloaded response ([FetchEvent.preloadResponse](/en-US/docs/Web/API/FetchEvent/preloadResponse)).

The `fetch` event handler calls [FetchEvent.respondWith()](/en-US/docs/Web/API/FetchEvent/respondWith) to pass a promise back to the controlled page. This promise will resolve with the requested resource, which may be from the cache, a preloaded fetch request, or a new network request.

If there is a matching URL request in the [Cache](/en-US/docs/Web/API/Cache) object, then the code returns a resolved promise for fetching the response from the cache. If no match is found in the cache, the code returns the resolved preloaded response ([FetchEvent.preloadResponse](/en-US/docs/Web/API/FetchEvent/preloadResponse)). If there is no matching cache entry or preloaded response, the code starts a new fetch operation from the network and returns the (unresolved) promise for that fetch operation.

js

```
addEventListener("fetch", (event) => {
  event.respondWith(
    (async () => {
      // Respond from the cache if we can
      const cachedResponse = await caches.match(event.request);
      if (cachedResponse) return cachedResponse;

      // Else, use the preloaded response, if it's there
      const response = await event.preloadResponse;
      if (response) return response;

      // Else try the network.
      return fetch(event.request);
    })(),
  );
});
```

### [Custom responses](#custom_responses)

The browser sends the HTTP header [Service-Worker-Navigation-Preload](/en-US/docs/Web/HTTP/Reference/Headers/Service-Worker-Navigation-Preload) with preload requests, with a default directive value of `true`. This allows servers to differentiate between normal and preload fetch requests, and to send different responses in each case if required.

Note: If the response from preload and normal fetch operations can be different, then the server must set `Vary: Service-Worker-Navigation-Preload` to ensure that the different responses are cached.

The header value can be changed to any other string value using [NavigationPreloadManager.setHeaderValue()](/en-US/docs/Web/API/NavigationPreloadManager/setHeaderValue) in order to provide additional context for the prefetch operation. For example, you might set the value to the ID of your most recently cached resource, so that the server won't return any resources unless they are actually needed. Similarly, you could configure the returned information based on authentication status instead of using cookies.

The code below shows how to set the value of the header directive to some variable `newValue`.

js

```
navigator.serviceWorker.ready
  .then((registration) =>
    registration.navigationPreload.setHeaderValue(newValue),
  )
  .then(() => {
    console.log("Done!");
  });
```

[Speed up Service Worker with Navigation Preloads > Custom responses for preloads](https://web.dev/blog/navigation-preload) provides a more complete example of a site where the response for an article web page is constructed from a cached header and footer, so that only the article content is returned for a prefetch.

### [Getting the state](#getting_the_state)

You can use [NavigationPreloadManager.getState()](/en-US/docs/Web/API/NavigationPreloadManager/getState) to check whether navigation preloading is enabled and to determine what directive value is sent with the [Service-Worker-Navigation-Preload](/en-US/docs/Web/HTTP/Reference/Headers/Service-Worker-Navigation-Preload) HTTP header for preload requests.

The code below shows how to get the promise that resolves to a `state` object and log the result.

js

```
navigator.serviceWorker.ready
  .then((registration) => registration.navigationPreload.getState())
  .then((state) => {
    console.log(state.enabled); // boolean
    console.log(state.headerValue); // string
  });
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# navigation-preload-manager](https://w3c.github.io/ServiceWorker/#navigation-preload-manager)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Speed up Service Worker with Navigation Preloads](https://web.dev/blog/navigation-preload) (developer.chrome.com)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 4, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/NavigationPreloadManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigationpreloadmanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationPreloadManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigationpreloadmanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationPreloadManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigationpreloadmanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2088b8912ef205a737551441d54b73507bd3ac6%0A*+Document+last+modified%3A+2024-08-04T23%3A19%3A14.000Z%0A%0A%3C%2Fdetails%3E)
