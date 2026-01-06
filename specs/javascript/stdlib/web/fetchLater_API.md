# fetchLater() API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FfetchLater_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `fetchLater()` API provides an interface to request a deferred fetch that can be sent after a specified period of time, or when the page is closed or navigated away from.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [HTTP headers](#http_headers)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Developers often need to send (or beacon) data back to the server, particularly at the end of a user's visit to a page — for example, for analytics services. There are several ways to do this: from adding 1 pixel [<img>](/en-US/docs/Web/HTML/Reference/Elements/img) elements to the page, to [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest), to the dedicated [Beacon API](/en-US/docs/Web/API/Beacon_API), and the [Fetch API](/en-US/docs/Web/API/Fetch_API) itself.

The issue is that all of these methods suffer from reliability problems for end-of-visit beaconing. While the Beacon API and the [keepalive](/en-US/docs/Web/API/Request/keepalive) property of the Fetch API will send data, even if the document is destroyed (to the best efforts that can be made in this scenario), this only solves part of the problem.

The other — more difficult — part to solve concerns deciding when to send the data, since there is not an ideal time in a page's lifecycle to make the JavaScript call to send out the beacon:

- The [unload](/en-US/docs/Web/API/Window/unload_event) and [beforeunload](/en-US/docs/Web/API/Window/beforeunload_event) events are unreliable, and outright ignored by several major browsers.
- The [pagehide](/en-US/docs/Web/API/Window/pagehide_event) and [visibilitychange](/en-US/docs/Web/API/Document/visibilitychange_event) events are more reliable, but still have issues on mobile platforms.

This means developers looking to reliably send out data via a beacon need to do so more frequently than is ideal. For example, they may send a beacon on each change, even if the final value for the page has not yet been reached. This has costs in network usage, server processing, and merging or discarding outdated beacons on the server.

Alternatively, developers can choose to accept some level of missing data — either by:

- Beaconing after a designated cut-off time and not collecting later data.
- Beaconing at the end of the page lifecycle but accepting that sometimes this will not be reliable.

The `fetchLater()` API extends the [Fetch API](/en-US/docs/Web/API/Fetch_API) to allow setting fetch requests up in advance. These deferred fetches can be updated before they have been sent, allowing the payload to reflect the latest data to be beaconed.

The browser then sends the beacon when the tab is closed or navigated away from, or after a set time if specified. This avoids sending multiple beacons but still ensures a reliable beacon within reasonable expectations (i.e., excluding when the browser process shuts down unexpectedly during a crash).

Deferred fetches can also be aborted using an [AbortController](/en-US/docs/Web/API/AbortController) if they are no longer required, avoiding further unnecessary costs.

### [Quotas](#quotas)

Deferred fetches are batched and sent once the tab is closed; at this point, there is no way for the user to abort them. To avoid situations where documents abuse this bandwidth to send unlimited amounts of data over the network, the overall quota for a top-level document is capped at 640KiB.

Callers of `fetchLater()` should be defensive and catch `QuotaExceededError` errors in almost all cases, especially if they embed third-party JavaScript.

Since this cap makes deferred fetch bandwidth a scarce resource, which needs to be shared between multiple reporting origins (for example, several RUM libraries) and subframes from multiple origins, the platform provides a reasonable default division of this quota. In addition, it provides [deferred-fetch](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/deferred-fetch) and [deferred-fetch-minimal](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/deferred-fetch-minimal)[Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) directives to allow dividing it differently when desired.

See [fetchLater() quotas](/en-US/docs/Web/API/fetchLater_API/fetchLater_quotas) for more details and examples.

## [Interfaces](#interfaces)

[Window.fetchLater()](/en-US/docs/Web/API/Window/fetchLater)

Used to queue a resource for sending at a later point.

[DeferredRequestInit](/en-US/docs/Web/API/DeferredRequestInit)

Represents the set of options that can be used to configure a deferred fetch request.

[FetchLaterResult](/en-US/docs/Web/API/FetchLaterResult)

Represents the result of requesting a deferred fetch.

## [HTTP headers](#http_headers)

[deferred-fetch](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/deferred-fetch)

Controls [top-level quota](/en-US/docs/Web/API/fetchLater_API/fetchLater_quotas) for the `fetchLater()` API.

[deferred-fetch-minimal](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/deferred-fetch-minimal)

Controls [shared cross-origin subframe quota](/en-US/docs/Web/API/fetchLater_API/fetchLater_quotas) for the `fetchLater()` API.

## [Specifications](#specifications)

Specification
[Fetch# deferred-fetch](https://fetch.spec.whatwg.org/#deferred-fetch)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [fetchLater() quotas](/en-US/docs/Web/API/fetchLater_API/fetchLater_quotas)
- [Fetch API](/en-US/docs/Web/API/Fetch_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/fetchLater_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/fetchlater_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FfetchLater_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffetchlater_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FfetchLater_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffetchlater_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5fad0829b5070d04993a57af8c276f5e35da3ed2%0A*+Document+last+modified%3A+2025-04-10T01%3A32%3A09.000Z%0A%0A%3C%2Fdetails%3E)
