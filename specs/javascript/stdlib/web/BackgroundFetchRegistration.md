# BackgroundFetchRegistration

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchRegistration&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `BackgroundFetchRegistration` interface of the [Background Fetch API](/en-US/docs/Web/API/Background_Fetch_API) represents an individual background fetch.

A `BackgroundFetchRegistration` instance is returned by the [BackgroundFetchManager.fetch()](/en-US/docs/Web/API/BackgroundFetchManager/fetch) or [BackgroundFetchManager.get()](/en-US/docs/Web/API/BackgroundFetchManager/get) methods, and therefore there has no constructor.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[BackgroundFetchRegistration.id](/en-US/docs/Web/API/BackgroundFetchRegistration/id)Read onlyExperimental

A string containing the background fetch's ID.

[BackgroundFetchRegistration.uploadTotal](/en-US/docs/Web/API/BackgroundFetchRegistration/uploadTotal)Read onlyExperimental

A [number](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) containing the total number of bytes to be uploaded.

[BackgroundFetchRegistration.uploaded](/en-US/docs/Web/API/BackgroundFetchRegistration/uploaded)Read onlyExperimental

A [number](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) containing the size in bytes successfully sent, initially `0`.

[BackgroundFetchRegistration.downloadTotal](/en-US/docs/Web/API/BackgroundFetchRegistration/downloadTotal)Read onlyExperimental

A [number](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) containing the total size in bytes of this download. This is the value set when the background fetch was registered, or `0`.

[BackgroundFetchRegistration.downloaded](/en-US/docs/Web/API/BackgroundFetchRegistration/downloaded)Read onlyExperimental

A [number](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) containing the size in bytes that has been downloaded, initially `0`.

[BackgroundFetchRegistration.result](/en-US/docs/Web/API/BackgroundFetchRegistration/result)Read onlyExperimental

Returns an empty string initially, on completion either the string `"success"` or `"failure"`.

[BackgroundFetchRegistration.failureReason](/en-US/docs/Web/API/BackgroundFetchRegistration/failureReason)Read onlyExperimental

A string with a value that indicates a reason for a background fetch failure. Can be one of the following values: `""`, `"aborted"`, `"bad-status"`, `"fetch-error"`, `"quota-exceeded"`, `"download-total-exceeded"`.

[BackgroundFetchRegistration.recordsAvailable](/en-US/docs/Web/API/BackgroundFetchRegistration/recordsAvailable)Read onlyExperimental

A [boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) indicating whether the `recordsAvailable` flag is set.

## [Instance methods](#instance_methods)

Also inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[BackgroundFetchRegistration.abort()](/en-US/docs/Web/API/BackgroundFetchRegistration/abort)Experimental

Aborts the background fetch. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with `true` if the fetch was successfully aborted.

[BackgroundFetchRegistration.match()](/en-US/docs/Web/API/BackgroundFetchRegistration/match)Experimental

Returns a single [BackgroundFetchRecord](/en-US/docs/Web/API/BackgroundFetchRecord) object which is the first match for the arguments.

[BackgroundFetchRegistration.matchAll()](/en-US/docs/Web/API/BackgroundFetchRegistration/matchAll)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an array of [BackgroundFetchRecord](/en-US/docs/Web/API/BackgroundFetchRecord) objects containing requests and responses.

## [Events](#events)

Also inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[progress](/en-US/docs/Web/API/BackgroundFetchRegistration/progress_event)Experimental

Fired when there is a change to any of the following properties: [uploaded](/en-US/docs/Web/API/BackgroundFetchRegistration/uploaded), [downloaded](/en-US/docs/Web/API/BackgroundFetchRegistration/downloaded), [result](/en-US/docs/Web/API/BackgroundFetchRegistration/result) or [failureReason](/en-US/docs/Web/API/BackgroundFetchRegistration/failureReason).

## [Examples](#examples)

The following code creates a `BackGroundFetchRegistration` as `bgFetch`, with an `id` of `"my-fetch"`.

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

Logging the [id](/en-US/docs/Web/API/BackgroundFetchRegistration/id) to the console returns `"my-fetch"`.

js

```
console.log(bgFetch.id); // "my-fetch"
```

The [match()](/en-US/docs/Web/API/BackgroundFetchRegistration/match) method can be used to find a particular [BackgroundFetchRecord](/en-US/docs/Web/API/BackgroundFetchRecord) from those that are part of the registration.

js

```
bgFetch.match("/ep-5.mp3").then(async (record) => {
  if (!record) {
    console.log("No record found");
    return;
  }

  console.log(`Here's the request`, record.request);
  const response = await record.responseReady;
  console.log(`And here's the response`, response);
});
```

## [Specifications](#specifications)

Specification
[Background Fetch# background-fetch-registration](https://wicg.github.io/background-fetch/#background-fetch-registration)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/BackgroundFetchRegistration/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/backgroundfetchregistration/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchRegistration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbackgroundfetchregistration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBackgroundFetchRegistration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbackgroundfetchregistration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
