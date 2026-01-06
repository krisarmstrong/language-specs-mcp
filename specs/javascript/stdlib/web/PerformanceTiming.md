# PerformanceTiming

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Warning: This interface is deprecated in the [Navigation Timing Level 2 specification](https://w3c.github.io/navigation-timing/#obsolete). Please use the [PerformanceNavigationTiming](/en-US/docs/Web/API/PerformanceNavigationTiming) interface instead.

The `PerformanceTiming` interface is a legacy interface kept for backwards compatibility and contains properties that offer performance timing information for various events which occur during the loading and use of the current page. You get a `PerformanceTiming` object describing your page using the [window.performance.timing](/en-US/docs/Web/API/Performance/timing) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `PerformanceTiming` interface doesn't inherit any properties.

These properties each describe the time at which a particular point in the page loading process was reached. Some correspond to DOM events; others describe the time at which internal browser operations of interest took place.

Each time is provided as a number representing the moment, in milliseconds since the UNIX epoch.

These properties are listed in the order in which they occur during the navigation process.

[PerformanceTiming.navigationStart](/en-US/docs/Web/API/PerformanceTiming/navigationStart)Read onlyDeprecated

When the prompt for unload terminates on the previous document in the same browsing context. If there is no previous document, this value will be the same as `PerformanceTiming.fetchStart`.

[PerformanceTiming.unloadEventStart](/en-US/docs/Web/API/PerformanceTiming/unloadEventStart)Read onlyDeprecated

When the [unload](/en-US/docs/Web/API/Window/unload_event) event has been thrown, indicating the time at which the previous document in the window began to unload. If there is no previous document, or if the previous document or one of the needed redirects is not of the same origin, the value returned is `0`.

[PerformanceTiming.unloadEventEnd](/en-US/docs/Web/API/PerformanceTiming/unloadEventEnd)Read onlyDeprecated

When the [unload](/en-US/docs/Web/API/Window/unload_event) event handler finishes. If there is no previous document, or if the previous document, or one of the needed redirects, is not of the same origin, the value returned is `0`.

[PerformanceTiming.redirectStart](/en-US/docs/Web/API/PerformanceTiming/redirectStart)Read onlyDeprecated

When the first HTTP redirect starts. If there is no redirect, or if one of the redirects is not of the same origin, the value returned is `0`.

[PerformanceTiming.redirectEnd](/en-US/docs/Web/API/PerformanceTiming/redirectEnd)Read onlyDeprecated

When the last HTTP redirect is completed, that is when the last byte of the HTTP response has been received. If there is no redirect, or if one of the redirects is not of the same origin, the value returned is `0`.

[PerformanceTiming.fetchStart](/en-US/docs/Web/API/PerformanceTiming/fetchStart)Read onlyDeprecated

When the browser is ready to fetch the document using an HTTP request. This moment is before the check to any application cache.

[PerformanceTiming.domainLookupStart](/en-US/docs/Web/API/PerformanceTiming/domainLookupStart)Read onlyDeprecated

When the domain lookup starts. If a persistent connection is used, or the information is stored in a cache or a local resource, the value will be the same as `PerformanceTiming.fetchStart`.

[PerformanceTiming.domainLookupEnd](/en-US/docs/Web/API/PerformanceTiming/domainLookupEnd)Read onlyDeprecated

When the domain lookup is finished. If a persistent connection is used, or the information is stored in a cache or a local resource, the value will be the same as `PerformanceTiming.fetchStart`.

[PerformanceTiming.connectStart](/en-US/docs/Web/API/PerformanceTiming/connectStart)Read onlyDeprecated

When the request to open a connection is sent to the network. If the transport layer reports an error and the connection establishment is started again, the last connection establishment start time is given. If a persistent connection is used, the value will be the same as `PerformanceTiming.fetchStart`.

[PerformanceTiming.connectEnd](/en-US/docs/Web/API/PerformanceTiming/connectEnd)Read onlyDeprecated

When the connection is opened network. If the transport layer reports an error and the connection establishment is started again, the last connection establishment end time is given. If a persistent connection is used, the value will be the same as `PerformanceTiming.fetchStart`. A connection is considered as opened when all secure connection handshake, or SOCKS authentication, is terminated.

[PerformanceTiming.secureConnectionStart](/en-US/docs/Web/API/PerformanceTiming/secureConnectionStart)Read onlyDeprecated

When the secure connection handshake starts. If no such connection is requested, it returns `0`.

[PerformanceTiming.requestStart](/en-US/docs/Web/API/PerformanceTiming/requestStart)Read onlyDeprecated

When the browser sent the request to obtain the actual document, from the server or from a cache. If the transport layer fails after the start of the request and the connection is reopened, this property will be set to the time corresponding to the new request.

[PerformanceTiming.responseStart](/en-US/docs/Web/API/PerformanceTiming/responseStart)Read onlyDeprecated

When the browser received the first byte of the response, from the server from a cache, or from a local resource.

[PerformanceTiming.responseEnd](/en-US/docs/Web/API/PerformanceTiming/responseEnd)Read onlyDeprecated

When the browser received the last byte of the response, or when the connection is closed if this happened first, from the server, the cache, or from a local resource.

[PerformanceTiming.domLoading](/en-US/docs/Web/API/PerformanceTiming/domLoading)Read onlyDeprecated

When the parser started its work, that is when its [Document.readyState](/en-US/docs/Web/API/Document/readyState) changes to `'loading'` and the corresponding [readystatechange](/en-US/docs/Web/API/Document/readystatechange_event) event is thrown.

[PerformanceTiming.domInteractive](/en-US/docs/Web/API/PerformanceTiming/domInteractive)Read onlyDeprecated

When the parser finished its work on the main document, that is when its [Document.readyState](/en-US/docs/Web/API/Document/readyState) changes to `'interactive'` and the corresponding [readystatechange](/en-US/docs/Web/API/Document/readystatechange_event) event is thrown.

[PerformanceTiming.domContentLoadedEventStart](/en-US/docs/Web/API/PerformanceTiming/domContentLoadedEventStart)Read onlyDeprecated

Right before the parser sent the [DOMContentLoaded](/en-US/docs/Web/API/Document/DOMContentLoaded_event) event, that is right after all the scripts that need to be executed right after parsing have been executed.

[PerformanceTiming.domContentLoadedEventEnd](/en-US/docs/Web/API/PerformanceTiming/domContentLoadedEventEnd)Read onlyDeprecated

Right after all the scripts that need to be executed as soon as possible, in order or not, have been executed.

[PerformanceTiming.domComplete](/en-US/docs/Web/API/PerformanceTiming/domComplete)Read onlyDeprecated

When the parser finished its work on the main document, that is when its [Document.readyState](/en-US/docs/Web/API/Document/readyState) changes to `'complete'` and the corresponding [readystatechange](/en-US/docs/Web/API/Document/readystatechange_event) event is thrown.

[PerformanceTiming.loadEventStart](/en-US/docs/Web/API/PerformanceTiming/loadEventStart)Read onlyDeprecated

When the [load](/en-US/docs/Web/API/Window/load_event) event was sent for the current document. If this event has not yet been sent, it returns `0`.

[PerformanceTiming.loadEventEnd](/en-US/docs/Web/API/PerformanceTiming/loadEventEnd)Read onlyDeprecated

When the [load](/en-US/docs/Web/API/Window/load_event) event handler terminated, that is when the load event is completed. If this event has not yet been sent, or is not yet completed, it returns `0`.

## [Instance methods](#instance_methods)

The `PerformanceTiming`interface doesn't inherit any methods.

[PerformanceTiming.toJSON()](/en-US/docs/Web/API/PerformanceTiming/toJSON)Deprecated

Returns a [JSON object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) representing this `PerformanceTiming` object.

## [Specifications](#specifications)

Specification
[Navigation Timing Level 2# dom-performancetiming](https://w3c.github.io/navigation-timing/#dom-performancetiming)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Performance.timing](/en-US/docs/Web/API/Performance/timing) property that creates such an object.
- [PerformanceNavigationTiming](/en-US/docs/Web/API/PerformanceNavigationTiming) (part of Navigation Timing Level 2) that has superseded this API.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancetiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancetiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancetiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcb25e0acbd9f0af27c4a99965cb962230d49a35d%0A*+Document+last+modified%3A+2025-05-27T14%3A24%3A09.000Z%0A%0A%3C%2Fdetails%3E)
