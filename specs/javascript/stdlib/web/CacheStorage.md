# CacheStorage

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCacheStorage&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `CacheStorage` interface represents the storage for [Cache](/en-US/docs/Web/API/Cache) objects.

The interface:

- Provides a master directory of all the named caches that can be accessed by a [ServiceWorker](/en-US/docs/Web/API/ServiceWorker) or other type of worker or [window](/en-US/docs/Web/API/Window) scope (you're not limited to only using it with service workers).
- Maintains a mapping of string names to corresponding [Cache](/en-US/docs/Web/API/Cache) objects.

Use [CacheStorage.open()](/en-US/docs/Web/API/CacheStorage/open) to obtain a [Cache](/en-US/docs/Web/API/Cache) instance.

Use [CacheStorage.match()](/en-US/docs/Web/API/CacheStorage/match) to check if a given [Request](/en-US/docs/Web/API/Request) is a key in any of the [Cache](/en-US/docs/Web/API/Cache) objects that the `CacheStorage` object tracks.

You can access `CacheStorage` through the [Window.caches](/en-US/docs/Web/API/Window/caches) property in windows or through the [WorkerGlobalScope.caches](/en-US/docs/Web/API/WorkerGlobalScope/caches) property in workers.

Note:`CacheStorage` always rejects with a `SecurityError` on untrusted origins (i.e., those that aren't using HTTPS, although this definition will likely become more complex in the future.) When testing on Firefox, you can get around this by checking the Enable Service Workers over HTTP (when toolbox is open) option in the Firefox DevTools options/gear menu. Furthermore, because `CacheStorage` requires file-system access, it may be unavailable in private mode in Firefox.

Note:[CacheStorage.match()](/en-US/docs/Web/API/CacheStorage/match) is a convenience method. Equivalent functionality to match a cache entry can be implemented by returning an array of cache names from [CacheStorage.keys()](/en-US/docs/Web/API/CacheStorage/keys), opening each cache with [CacheStorage.open()](/en-US/docs/Web/API/CacheStorage/open), and matching the one you want with [Cache.match()](/en-US/docs/Web/API/Cache/match).

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[CacheStorage.match()](/en-US/docs/Web/API/CacheStorage/match)

Checks if a given [Request](/en-US/docs/Web/API/Request) is a key in any of the [Cache](/en-US/docs/Web/API/Cache) objects that the `CacheStorage` object tracks, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to that match.

[CacheStorage.has()](/en-US/docs/Web/API/CacheStorage/has)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to `true` if a [Cache](/en-US/docs/Web/API/Cache) object matching the `cacheName` exists.

[CacheStorage.open()](/en-US/docs/Web/API/CacheStorage/open)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to the [Cache](/en-US/docs/Web/API/Cache) object matching the `cacheName` (a new cache is created if it doesn't already exist.)

[CacheStorage.delete()](/en-US/docs/Web/API/CacheStorage/delete)

Finds the [Cache](/en-US/docs/Web/API/Cache) object matching the `cacheName`, and if found, deletes the [Cache](/en-US/docs/Web/API/Cache) object and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to `true`. If no [Cache](/en-US/docs/Web/API/Cache) object is found, it resolves to `false`.

[CacheStorage.keys()](/en-US/docs/Web/API/CacheStorage/keys)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that will resolve with an array containing strings corresponding to all of the named [Cache](/en-US/docs/Web/API/Cache) objects tracked by the `CacheStorage`. Use this method to iterate over a list of all the [Cache](/en-US/docs/Web/API/Cache) objects.

## [Examples](#examples)

This code snippet is from the MDN [simple service worker example](https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker) (see [simple service worker running live](https://bncb2v.csb.app/).) This service worker script waits for an [install](/en-US/docs/Web/API/ServiceWorkerGlobalScope/install_event) event to fire, then runs [waitUntil](/en-US/docs/Web/API/ExtendableEvent/waitUntil) to handle the install process for the app. This consists of calling [CacheStorage.open](/en-US/docs/Web/API/CacheStorage/open) to create a new cache, then using [Cache.addAll](/en-US/docs/Web/API/Cache/addAll) to add a series of assets to it.

In the second code block, we wait for a [FetchEvent](/en-US/docs/Web/API/FetchEvent) to fire. We construct a custom response like so:

1. Check whether a match for the request is found in the CacheStorage. If so, serve that.
2. If not, fetch the request from the network, then also open the cache created in the first block and add a clone of the request to it using [Cache.put](/en-US/docs/Web/API/Cache/put) (`cache.put(event.request, response.clone())`.)
3. If this fails (e.g., because the network is down), return a fallback response.

Finally, return whatever the custom response ended up being equal to, using [FetchEvent.respondWith](/en-US/docs/Web/API/FetchEvent/respondWith).

js

```
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open("v1")
      .then((cache) =>
        cache.addAll([
          "/",
          "/index.html",
          "/style.css",
          "/app.js",
          "/image-list.js",
          "/star-wars-logo.jpg",
          "/gallery/bountyHunters.jpg",
          "/gallery/myLittleVader.jpg",
          "/gallery/snowTroopers.jpg",
        ]),
      ),
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      // caches.match() always resolves
      // but in case of success response will have value
      if (response !== undefined) {
        return response;
      }
      return fetch(event.request)
        .then((response) => {
          // response may be used only once
          // we need to save clone to put one copy in cache
          // and serve second one
          let responseClone = response.clone();

          caches
            .open("v1")
            .then((cache) => cache.put(event.request, responseClone));
          return response;
        })
        .catch(() => caches.match("/gallery/myLittleVader.jpg"));
    }),
  );
});
```

This snippet shows how the API can be used outside of a service worker context, and uses the `await` operator for much more readable code.

js

```
// Try to get data from the cache, but fall back to fetching it live.
async function getData() {
  const cacheVersion = 1;
  const cacheName = `myapp-${cacheVersion}`;
  const url = "https://jsonplaceholder.typicode.com/todos/1";
  let cachedData = await getCachedData(cacheName, url);

  if (cachedData) {
    console.log("Retrieved cached data");
    return cachedData;
  }

  console.log("Fetching fresh data");

  const cacheStorage = await caches.open(cacheName);
  await cacheStorage.add(url);
  cachedData = await getCachedData(cacheName, url);
  await deleteOldCaches(cacheName);

  return cachedData;
}

// Get data from the cache.
async function getCachedData(cacheName, url) {
  const cacheStorage = await caches.open(cacheName);
  const cachedResponse = await cacheStorage.match(url);

  if (!cachedResponse || !cachedResponse.ok) {
    return false;
  }

  return await cachedResponse.json();
}

// Delete any old caches to respect user's disk space.
async function deleteOldCaches(currentCache) {
  const keys = await caches.keys();

  for (const key of keys) {
    const isOurCache = key.startsWith("myapp-");
    if (currentCache === key || !isOurCache) {
      continue;
    }
    caches.delete(key);
  }
}

try {
  const data = await getData();
  console.log({ data });
} catch (error) {
  console.error({ error });
}
```

## [Specifications](#specifications)

Specification
[Service Workers Nightly# cachestorage-interface](https://w3c.github.io/ServiceWorker/#cachestorage-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Cache](/en-US/docs/Web/API/Cache)
- [Window.caches](/en-US/docs/Web/API/Window/caches) and [WorkerGlobalScope.caches](/en-US/docs/Web/API/WorkerGlobalScope/caches)
- [Private Browsing / Incognito modes](/en-US/docs/Web/API/Web_Storage_API#private_browsing_incognito_modes)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CacheStorage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cachestorage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCacheStorage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcachestorage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCacheStorage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcachestorage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
