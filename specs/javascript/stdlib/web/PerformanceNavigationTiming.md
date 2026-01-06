# PerformanceNavigationTiming

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨October 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceNavigationTiming&level=high)

The `PerformanceNavigationTiming` interface provides methods and properties to store and retrieve metrics regarding the browser's document navigation events. For example, this interface can be used to determine how much time it takes to load or unload a document.

Only the current document is included in the performance timeline, so there is only one `PerformanceNavigationTiming` object in the performance timeline. It inherits all of the properties and methods of [PerformanceResourceTiming](/en-US/docs/Web/API/PerformanceResourceTiming) and [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

The following diagram shows all of the timestamp properties defined in `PerformanceNavigationTiming`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties by qualifying and constraining them as follows:

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read only

Returns `"navigation"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read only

Returns the [document's URL](/en-US/docs/Web/API/Document/URL). Note that [text fragments](/en-US/docs/Web/URI/Reference/Fragment/Text_fragments), and any other fragment directives, are stripped from the URL.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read only

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) with a value of `0`.

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read only

Returns a [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that is the difference between the [PerformanceNavigationTiming.loadEventEnd](/en-US/docs/Web/API/PerformanceNavigationTiming/loadEventEnd) and [PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime) properties.

This interface also extends the following [PerformanceResourceTiming](/en-US/docs/Web/API/PerformanceResourceTiming) properties by qualifying and constraining them as follows:

[PerformanceResourceTiming.initiatorType](/en-US/docs/Web/API/PerformanceResourceTiming/initiatorType)Read only

Returns `"navigation"`.

The interface also supports the following properties:

[PerformanceNavigationTiming.activationStart](/en-US/docs/Web/API/PerformanceNavigationTiming/activationStart)Read onlyExperimental

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time between when a document starts prerendering and when it is activated.

[PerformanceNavigationTiming.criticalCHRestart](/en-US/docs/Web/API/PerformanceNavigationTiming/criticalCHRestart)Read onlyExperimental

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time at which the connection restart occurred due to [Critical-CH](/en-US/docs/Web/HTTP/Reference/Headers/Critical-CH) HTTP response header mismatch.

[PerformanceNavigationTiming.domComplete](/en-US/docs/Web/API/PerformanceNavigationTiming/domComplete)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately before the user agent sets the document's [readyState](/en-US/docs/Web/API/Document/readyState) to `"complete"`.

[PerformanceNavigationTiming.domContentLoadedEventEnd](/en-US/docs/Web/API/PerformanceNavigationTiming/domContentLoadedEventEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately after the current document's [DOMContentLoaded](/en-US/docs/Web/API/Document/DOMContentLoaded_event) event handler completes.

[PerformanceNavigationTiming.domContentLoadedEventStart](/en-US/docs/Web/API/PerformanceNavigationTiming/domContentLoadedEventStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately before the current document's [DOMContentLoaded](/en-US/docs/Web/API/Document/DOMContentLoaded_event) event handler starts.

[PerformanceNavigationTiming.domInteractive](/en-US/docs/Web/API/PerformanceNavigationTiming/domInteractive)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately before the user agent sets the document's [readyState](/en-US/docs/Web/API/Document/readyState) to `"interactive"`.

[PerformanceNavigationTiming.loadEventEnd](/en-US/docs/Web/API/PerformanceNavigationTiming/loadEventEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately after the current document's [load](/en-US/docs/Web/API/Window/load_event) event handler completes.

[PerformanceNavigationTiming.loadEventStart](/en-US/docs/Web/API/PerformanceNavigationTiming/loadEventStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately before the current document's [load](/en-US/docs/Web/API/Window/load_event) event handler starts.

[PerformanceNavigationTiming.notRestoredReasons](/en-US/docs/Web/API/PerformanceNavigationTiming/notRestoredReasons)Read onlyExperimental

A [NotRestoredReasons](/en-US/docs/Web/API/NotRestoredReasons) object providing report data on reasons why the current document was blocked from using the back/forward cache ([bfcache](/en-US/docs/Glossary/bfcache)) on navigation.

[PerformanceNavigationTiming.redirectCount](/en-US/docs/Web/API/PerformanceNavigationTiming/redirectCount)Read only

A number representing the number of redirects since the last non-redirect navigation in the current browsing context.

[PerformanceNavigationTiming.type](/en-US/docs/Web/API/PerformanceNavigationTiming/type)Read only

A string representing the navigation type. Either `"navigate"`, `"reload"`, or `"back_forward"`.

[PerformanceNavigationTiming.unloadEventEnd](/en-US/docs/Web/API/PerformanceNavigationTiming/unloadEventEnd)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately after the current document's [unload](/en-US/docs/Web/API/Window/unload_event) event handler completes.

[PerformanceNavigationTiming.unloadEventStart](/en-US/docs/Web/API/PerformanceNavigationTiming/unloadEventStart)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time immediately before the current document's [unload](/en-US/docs/Web/API/Window/unload_event) event handler starts.

## [Instance methods](#instance_methods)

[PerformanceNavigationTiming.toJSON()](/en-US/docs/Web/API/PerformanceNavigationTiming/toJSON)

Returns a JSON representation of the `PerformanceNavigationTiming` object.

## [Specifications](#specifications)

Specification
[Navigation Timing Level 2# sec-PerformanceNavigationTiming](https://w3c.github.io/navigation-timing/#sec-PerformanceNavigationTiming)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Performance.navigation](/en-US/docs/Web/API/Performance/navigation)
- [PerformanceNavigation](/en-US/docs/Web/API/PerformanceNavigation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceNavigationTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancenavigationtiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceNavigationTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancenavigationtiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceNavigationTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancenavigationtiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11e09e7c584658fbfbecd2f00ae66e546cd54cc0%0A*+Document+last+modified%3A+2025-09-27T00%3A08%3A37.000Z%0A%0A%3C%2Fdetails%3E)
