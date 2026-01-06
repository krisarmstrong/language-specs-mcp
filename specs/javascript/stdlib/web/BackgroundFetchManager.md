# BackgroundFetchManager

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchManager&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `BackgroundFetchManager` interface of the [Background Fetch API](/en-US/docs/Web/API/Background_Fetch_API) is a map where the keys are background fetch IDs and the values are [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration) objects.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

[fetch()](/en-US/docs/Web/API/BackgroundFetchManager/fetch)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration) object for a supplied array of URLs and [Request](/en-US/docs/Web/API/Request) objects.

[get()](/en-US/docs/Web/API/BackgroundFetchManager/get)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the [BackgroundFetchRegistration](/en-US/docs/Web/API/BackgroundFetchRegistration) associated with the provided `id` or [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) if the `id` is not found.

[getIds()](/en-US/docs/Web/API/BackgroundFetchManager/getIds)Experimental

Returns the IDs of all registered background fetches.

## [Examples](#examples)

The example below shows how to get an instance of `BackgroundFetchManager` from a [ServiceWorkerRegistration](/en-US/docs/Web/API/ServiceWorkerRegistration) object and calls `fetch()` to download an audio file in the background.

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

## [Specifications](#specifications)

Specification
[Background Fetch# background-fetch-manager](https://wicg.github.io/background-fetch/#background-fetch-manager)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BackgroundFetchManager/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/backgroundfetchmanager/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchManager&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackgroundfetchmanager%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchManager%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackgroundfetchmanager%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc77a11ee1509542c16b0348afc4fcb3ffe588e1c%0A*+Document+last+modified%3A+2024-05-07T14%3A59%3A11.000Z%0A%0A%3C%2Fdetails%3E)
