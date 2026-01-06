# DeferredRequestInit

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeferredRequestInit&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `DeferredRequestInit` dictionary of the [fetchLater() API](/en-US/docs/Web/API/fetchLater_API) represents the set of options that can be used to configure a deferred fetch request.

The `DeferredRequestInit` object is passed directly into the [window.fetchLater()](/en-US/docs/Web/API/Window/fetchLater) function call as the second argument.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This dictionary extends the [RequestInit](/en-US/docs/Web/API/RequestInit) dictionary with the addition of the following properties:

[activateAfter Optional](#activateafter)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating a timeout in milliseconds after which the fetch request should be sent. The fetch can be sent earlier on navigating away. The actual sending time is unknown, as the browser may wait for a longer or shorter time, for example, to optimize the batching of deferred fetches. If the `activateAfter` property is not provided, the deferred fetch waits until the end of the page visit (including entering the [bfcache](/en-US/docs/Glossary/bfcache)).

### [Exceptions](#exceptions)

`RangeError`[DOMException](/en-US/docs/Web/API/DOMException)

Raised when a negative `activateAfter` is provided.

## [Examples](#examples)

### [Defer a GET request until the page is destroyed or enters the bfcache](#defer_a_get_request_until_the_page_is_destroyed_or_enters_the_bfcache)

In this example, no `DeferredRequestInit` object is provided and no timeout is used:

js

```
fetchLater("/send_beacon");
```

### [Defer a POST request for around 1 minute](#defer_a_post_request_for_around_1_minute)

In this example we create a [Request](/en-US/docs/Web/API/Request), and provide an `activateAfter` value to delay sending the request for 60,000 milliseconds (or one minute):

js

```
fetchLater("/send_beacon", {
  method: "POST",
  body: getBeaconData(),
  activateAfter: 60000, // 1 minute
});
```

Note: The actual sending time is unknown, as the browser may wait for a longer or shorter period of time, for example to optimize batching of deferred fetches.

## [Specifications](#specifications)

Specification
[Fetch# deferred-fetch](https://fetch.spec.whatwg.org/#deferred-fetch)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Fetch](/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [ServiceWorker API](/en-US/docs/Web/API/Service_Worker_API)
- [HTTP access control (CORS)](/en-US/docs/Web/HTTP/Guides/CORS)
- [HTTP](/en-US/docs/Web/HTTP)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DeferredRequestInit/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/deferredrequestinit/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeferredRequestInit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdeferredrequestinit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDeferredRequestInit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdeferredrequestinit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
