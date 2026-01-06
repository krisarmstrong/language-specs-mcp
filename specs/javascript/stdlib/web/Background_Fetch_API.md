# Background Fetch API

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Background Fetch API provides a method for managing downloads that may take a significant amount of time such as movies, audio files, and software.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and Usage](#concepts_and_usage)

When a web application requires the user to download large files, this often presents a problem in that the user needs to stay connected to the page for the download to complete. If they lose connectivity, close the tab or navigate away from the page the download stops.

The [Background Synchronization API](/en-US/docs/Web/API/Background_Synchronization_API) provides a way for service workers to defer processing until a user is connected; however it can't be used for long running tasks such as downloading a large file. Background Sync requires that the service worker stays alive until the fetch is completed, and to conserve battery life and to prevent unwanted tasks happening in the background the browser will at some point terminate the task.

The Background Fetch API solves this problem. It creates a way for a web developer to tell the browser to perform some fetches in the background, for example when the user clicks a button to download a video file. The browser then performs the fetches in a user-visible way, displaying progress to the user and giving them a method to cancel the download. Once the download is complete the browser then opens the service worker, at which point your application can do something with the response if required.

The Background Fetch API will enable the fetch to happen if the user starts the process while offline. Once they are connected it will begin. If the user goes off line, the process pauses until the user is on again.

## [Interfaces](#interfaces)

[BackgroundFetchManager](/en-US/docs/Web/API/BackgroundFetchManager)Experimental

A map where the keys are background fetch IDs and the values are [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration) objects.

[BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration)Experimental

Represents a Background Fetch.

[BackgroundFetchRecord](/en-US/docs/Web/API/BackgroundFetchRecord)Experimental

Represents an individual fetch request and response.

[BackgroundFetchEvent](/en-US/docs/Web/API/BackgroundFetchEvent)Experimental

The event type for the [backgroundfetchabort](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchabort_event) and [backgroundfetchclick](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchclick_event) event

[BackgroundFetchUpdateUIEvent](/en-US/docs/Web/API/BackgroundFetchUpdateUIEvent)Experimental

The event type for the [backgroundfetchsuccess](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchsuccess_event) and [backgroundfetchfail](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchfail_event) event

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[ServiceWorkerRegistration.backgroundFetch](/en-US/docs/Web/API/ServiceWorkerRegistration/backgroundFetch)Read onlyExperimental

Returns a reference to a [BackgroundFetchManager](/en-US/docs/Web/API/BackgroundFetchManager) object, which manages background fetch operations.

[backgroundfetchabort](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchabort_event) event Experimental

Fired when a background fetch operation has been canceled by the user or the app.

[backgroundfetchclick](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchclick_event) event Experimental

Fired when the user has clicked on the UI for a background fetch operation.

[backgroundfetchfail](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchfail_event) event Experimental

Fired when at least one of the requests in a background fetch operation has failed.

[backgroundfetchsuccess](/en-US/docs/Web/API/ServiceWorkerGlobalScope/backgroundfetchsuccess_event) event Experimental

Fired when all of the requests in a background fetch operation have succeeded.

## [Examples](#examples)

Before using Background Fetch, check for browser support.

js

```
if (!("BackgroundFetchManager" in self)) {
  // Provide fallback downloading.
}
```

Using Background Fetch requires a registered service worker. Then call `backgroundFetch.fetch()` to perform a fetch. This returns a promise that resolves with a [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration).

A background fetch may fetch a number of files. In our example the fetch requests an MP3 and a JPEG. This enables a package of files that the user sees as one item (for example a podcast and artwork) to be downloaded at once.

js

```
navigator.serviceWorker.ready.then(async (swReg) => {
  const bgFetch = await swReg.backgroundFetch.fetch(
    "my-fetch",
    ["/ep-5.mp3", "ep-5-artwork.jpg"],
    {
      title: "Episode 5: Interesting things.",
      icons: [
        {
          sizes: "300x300",
          src: "/ep-5-icon.png",
          type: "image/png",
        },
      ],
      downloadTotal: 60 * 1024 * 1024,
    },
  );
});
```

You can find further code examples and a demo in [Introducing Background Fetch](https://developer.chrome.com/blog/background-fetch/).

## [Specifications](#specifications)

Specification[Background Fetch](https://wicg.github.io/background-fetch/)

## [Browser compatibility](#browser_compatibility)

### [api.BackgroundFetchManager](#api.BackgroundFetchManager)

### [api.BackgroundFetchRegistration](#api.BackgroundFetchRegistration)

### [api.BackgroundFetchRecord](#api.BackgroundFetchRecord)

## [See also](#see_also)

- [Introducing Background Fetch](https://developer.chrome.com/blog/background-fetch/)
- [Background Fetch - HTTP 203](https://www.youtube.com/watch?v=cElAoxhQz6w)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Background_Fetch_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/background_fetch_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackground_Fetch_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackground_fetch_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackground_Fetch_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackground_fetch_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F90eafc463fe122c86a64836f4f3953a0bee85be9%0A*+Document+last+modified%3A+2025-07-07T16%3A29%3A09.000Z%0A%0A%3C%2Fdetails%3E)
