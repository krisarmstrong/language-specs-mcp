# PerformanceObserver

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceObserver&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PerformanceObserver` interface is used to observe performance measurement events and be notified of new [performance entries](/en-US/docs/Web/API/PerformanceEntry) as they are recorded in the browser's performance timeline.

## In this article

- [Constructor](#constructor)
- [Static properties](#static_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PerformanceObserver()](/en-US/docs/Web/API/PerformanceObserver/PerformanceObserver)

Creates and returns a new `PerformanceObserver` object.

## [Static properties](#static_properties)

[PerformanceObserver.supportedEntryTypes](/en-US/docs/Web/API/PerformanceObserver/supportedEntryTypes_static)Read only

Returns an array of the [entryType](/en-US/docs/Web/API/PerformanceEntry/entryType) values supported by the user agent.

## [Instance methods](#instance_methods)

[PerformanceObserver.observe()](/en-US/docs/Web/API/PerformanceObserver/observe)

Specifies the set of entry types to observe. The performance observer's callback function will be invoked when performance entry is recorded for one of the specified `entryTypes`.

[PerformanceObserver.disconnect()](/en-US/docs/Web/API/PerformanceObserver/disconnect)

Stops the performance observer callback from receiving performance entries.

[PerformanceObserver.takeRecords()](/en-US/docs/Web/API/PerformanceObserver/takeRecords)

Returns the current list of performance entries stored in the performance observer, emptying it out.

## [Examples](#examples)

### [Creating a PerformanceObserver](#creating_a_performanceobserver)

The following example creates a `PerformanceObserver` watching for "mark" ([PerformanceMark](/en-US/docs/Web/API/PerformanceMark)) and "measure" ([PerformanceMeasure](/en-US/docs/Web/API/PerformanceMeasure)) events. The `perfObserver` callback provides a `list` ([PerformanceObserverEntryList](/en-US/docs/Web/API/PerformanceObserverEntryList)) which allows you to get observed performance entries.

js

```
function perfObserver(list, observer) {
  list.getEntries().forEach((entry) => {
    if (entry.entryType === "mark") {
      console.log(`${entry.name}'s startTime: ${entry.startTime}`);
    }
    if (entry.entryType === "measure") {
      console.log(`${entry.name}'s duration: ${entry.duration}`);
    }
  });
}
const observer = new PerformanceObserver(perfObserver);
observer.observe({ entryTypes: ["measure", "mark"] });
```

## [Specifications](#specifications)

Specification
[Performance Timeline# dom-performanceobserver](https://w3c.github.io/performance-timeline/#dom-performanceobserver)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MutationObserver](/en-US/docs/Web/API/MutationObserver)
- [ResizeObserver](/en-US/docs/Web/API/ResizeObserver)
- [IntersectionObserver](/en-US/docs/Web/API/IntersectionObserver)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceObserver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceobserver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceObserver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceobserver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceObserver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceobserver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ab0f2fde2a9c1c7e547884abedf3848f8d7dda5%0A*+Document+last+modified%3A+2024-10-12T14%3A21%3A59.000Z%0A%0A%3C%2Fdetails%3E)
