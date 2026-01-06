# Beacon API

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBeacon_API&level=high)

The `Beacon` API is used to send an asynchronous and non-blocking request to a web server. The request does not expect a response. Unlike requests made using [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) or the [Fetch API](/en-US/docs/Web/API/Fetch_API), the browser guarantees to initiate beacon requests before the page is unloaded and to run them to completion.

The main use case for the Beacon API is to send analytics such as client-side events or session data to the server. Historically, websites have used [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) for this, but browsers do not guarantee to send these asynchronous requests in some circumstances (for example, if the page is about to be unloaded). To combat this, websites have resorted to various techniques, such as making the request synchronous, that have a bad effect on responsiveness. Because beacon requests are both asynchronous and guaranteed to be sent, they combine good performance characteristics and reliability.

For more details about the motivation for and usage of this API, see the documentation for the [navigator.sendBeacon()](/en-US/docs/Web/API/Navigator/sendBeacon) method.

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Interfaces](#interfaces)

This API defines a single method: [navigator.sendBeacon()](/en-US/docs/Web/API/Navigator/sendBeacon).

The method takes two arguments, the URL and the data to send in the request. The data argument is optional and its type may be a string, an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray), a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView), a [ReadableStream](/en-US/docs/Web/API/ReadableStream), a [Blob](/en-US/docs/Web/API/Blob), a [FormData](/en-US/docs/Web/API/FormData) object, or a [URLSearchParams](/en-US/docs/Web/API/URLSearchParams) object. If the browser successfully queues the request for delivery, the method returns `true`; otherwise, it returns `false`.

## [Specifications](#specifications)

Specification
[Beacon# sendbeacon-method](https://w3c.github.io/beacon/#sendbeacon-method)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Beacon standard](https://w3c.github.io/beacon/)
- [Beacon CanIUse data](https://caniuse.com/#search=beacon)
- [Intercepting beacons through service workers](https://ehsanakhgari.org/blog/2015-04-08/intercepting-beacons-through-service-workers/); Ehsan Akhgari; 2015-Apr-08
- [https://webkit.org/blog/8821/link-click-analytics-and-privacy/](https://webkit.org/blog/8821/link-click-analytics-and-privacy/)
- [Beaconing in Practice](https://calendar.perfplanet.com/2020/beaconing-in-practice/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Beacon_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/beacon_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBeacon_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbeacon_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBeacon_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbeacon_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdcbb1d99185118360cc84b3a0e935e77fe0a03e3%0A*+Document+last+modified%3A+2024-09-24T13%3A57%3A44.000Z%0A%0A%3C%2Fdetails%3E)
