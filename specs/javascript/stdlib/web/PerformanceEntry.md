# PerformanceEntry

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceEntry&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PerformanceEntry` object encapsulates a single performance metric that is part of the browser's performance timeline.

The Performance API offers built-in metrics which are specialized subclasses of `PerformanceEntry`. This includes entries for resource loading, event timing, and more.

A performance entry can also be created by calling the [Performance.mark()](/en-US/docs/Web/API/Performance/mark) or [Performance.measure()](/en-US/docs/Web/API/Performance/measure) methods at an explicit point in an application. This allows you to add your own metrics to the performance timeline.

The `PerformanceEntry` instances will always be one of the following subclasses:

- [LargestContentfulPaint](/en-US/docs/Web/API/LargestContentfulPaint)
- [LayoutShift](/en-US/docs/Web/API/LayoutShift)
- [PerformanceEventTiming](/en-US/docs/Web/API/PerformanceEventTiming)
- [PerformanceLongAnimationFrameTiming](/en-US/docs/Web/API/PerformanceLongAnimationFrameTiming)
- [PerformanceLongTaskTiming](/en-US/docs/Web/API/PerformanceLongTaskTiming)
- [PerformanceMark](/en-US/docs/Web/API/PerformanceMark)
- [PerformanceMeasure](/en-US/docs/Web/API/PerformanceMeasure)
- [PerformanceNavigationTiming](/en-US/docs/Web/API/PerformanceNavigationTiming)
- [PerformancePaintTiming](/en-US/docs/Web/API/PerformancePaintTiming)
- [PerformanceResourceTiming](/en-US/docs/Web/API/PerformanceResourceTiming)
- [PerformanceScriptTiming](/en-US/docs/Web/API/PerformanceScriptTiming)
- [PerformanceServerTiming](/en-US/docs/Web/API/PerformanceServerTiming)
- [TaskAttributionTiming](/en-US/docs/Web/API/TaskAttributionTiming)
- [VisibilityStateEntry](/en-US/docs/Web/API/VisibilityStateEntry)

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read only

A string representing the name for a performance entry. The value depends on the subtype.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read only

A string representing the type of performance metric. For example, `"mark"` when [PerformanceMark](/en-US/docs/Web/API/PerformanceMark) is used.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the starting time for the performance metric.

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the duration of the performance entry.

## [Instance methods](#instance_methods)

[PerformanceEntry.toJSON()](/en-US/docs/Web/API/PerformanceEntry/toJSON)

Returns a JSON representation of the `PerformanceEntry` object.

## [Example](#example)

### [Working with performance entries](#working_with_performance_entries)

The following example creates `PerformanceEntry` objects that are of the types [PerformanceMark](/en-US/docs/Web/API/PerformanceMark) and [PerformanceMeasure](/en-US/docs/Web/API/PerformanceMeasure). The `PerformanceMark` and `PerformanceMeasure` subclasses inherit the `duration`, `entryType`, `name`, and `startTime` properties from `PerformanceEntry` and set them to their appropriate values.

js

```
// Place at a location in the code that starts login
performance.mark("login-started");

// Place at a location in the code that finishes login
performance.mark("login-finished");

// Measure login duration
performance.measure("login-duration", "login-started", "login-finished");

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
[Performance Timeline# dom-performanceentry](https://w3c.github.io/performance-timeline/#dom-performanceentry)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 20, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performanceentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformanceentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformanceentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0598721ab3f672c66a8357d9e6b27ec8644a2b21%0A*+Document+last+modified%3A+2024-11-20T09%3A12%3A46.000Z%0A%0A%3C%2Fdetails%3E)
