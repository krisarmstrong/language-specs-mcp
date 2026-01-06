# Performance

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformance&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `Performance` interface provides access to performance-related information for the current page.

Performance entries are specific to each execution context. You can access performance information for code running in a window via [Window.performance](/en-US/docs/Web/API/Window/performance), and for code running in a worker via [WorkerGlobalScope.performance](/en-US/docs/Web/API/WorkerGlobalScope/performance).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

The `Performance` interface doesn't inherit any properties.

[Performance.eventCounts](/en-US/docs/Web/API/Performance/eventCounts)Read only

An [EventCounts](/en-US/docs/Web/API/EventCounts) map containing the number of events which have been dispatched per event type.

[Performance.navigation](/en-US/docs/Web/API/Performance/navigation)Read onlyDeprecated

A legacy [PerformanceNavigation](/en-US/docs/Web/API/PerformanceNavigation) object that provides useful context about the operations included in the times listed in `timing`, including whether the page was a load or a refresh, how many redirections occurred, and so forth.

[Performance.timing](/en-US/docs/Web/API/Performance/timing)Read onlyDeprecated

A legacy [PerformanceTiming](/en-US/docs/Web/API/PerformanceTiming) object containing latency-related performance information.

[Performance.memory](/en-US/docs/Web/API/Performance/memory)Read onlyNon-standardDeprecated

A non-standard extension added in Chrome, this property provides an object with basic memory usage information. You should not use this non-standard API.

[Performance.timeOrigin](/en-US/docs/Web/API/Performance/timeOrigin)Read only

Returns the high resolution timestamp of the start time of the performance measurement.

## [Instance methods](#instance_methods)

The `Performance` interface doesn't inherit any methods.

[Performance.clearMarks()](/en-US/docs/Web/API/Performance/clearMarks)

Removes the given mark from the browser's performance entry buffer.

[Performance.clearMeasures()](/en-US/docs/Web/API/Performance/clearMeasures)

Removes the given measure from the browser's performance entry buffer.

[Performance.clearResourceTimings()](/en-US/docs/Web/API/Performance/clearResourceTimings)

Removes all [performance entries](/en-US/docs/Web/API/PerformanceEntry) with an [entryType](/en-US/docs/Web/API/PerformanceEntry/entryType) of `"resource"` from the browser's performance data buffer.

[Performance.getEntries()](/en-US/docs/Web/API/Performance/getEntries)

Returns a list of [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects based on the given filter.

[Performance.getEntriesByName()](/en-US/docs/Web/API/Performance/getEntriesByName)

Returns a list of [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects based on the given name and entry type.

[Performance.getEntriesByType()](/en-US/docs/Web/API/Performance/getEntriesByType)

Returns a list of [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects of the given entry type.

[Performance.mark()](/en-US/docs/Web/API/Performance/mark)

Creates a [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) in the browser's performance entry buffer with the given name.

[Performance.measure()](/en-US/docs/Web/API/Performance/measure)

Creates a named [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) in the browser's performance entry buffer between two specified marks (known as the start mark and end mark, respectively).

[Performance.measureUserAgentSpecificMemory()](/en-US/docs/Web/API/Performance/measureUserAgentSpecificMemory)Experimental

Estimates the memory usage of a web application including all its iframes and workers.

[Performance.now()](/en-US/docs/Web/API/Performance/now)

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the number of milliseconds elapsed since a reference instant.

[Performance.setResourceTimingBufferSize()](/en-US/docs/Web/API/Performance/setResourceTimingBufferSize)

Sets the browser's resource timing buffer size to the specified number of `"resource"`[type](/en-US/docs/Web/API/PerformanceEntry/entryType)[PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects.

[Performance.toJSON()](/en-US/docs/Web/API/Performance/toJSON)

Returns a JSON representation of the `Performance` object.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[resourcetimingbufferfull](/en-US/docs/Web/API/Performance/resourcetimingbufferfull_event)

Fired when the browser's [resource timing buffer](/en-US/docs/Web/API/Performance/setResourceTimingBufferSize) is full.

## [Specifications](#specifications)

Specification
[High Resolution Time# sec-performance](https://w3c.github.io/hr-time/#sec-performance)
[Performance Timeline# extensions-to-the-performance-interface](https://w3c.github.io/performance-timeline/#extensions-to-the-performance-interface)
[Resource Timing# sec-extensions-performance-interface](https://w3c.github.io/resource-timing/#sec-extensions-performance-interface)
[User Timing# extensions-performance-interface](https://w3c.github.io/user-timing/#extensions-performance-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Performance/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performance/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformance&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformance%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformance%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformance%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
