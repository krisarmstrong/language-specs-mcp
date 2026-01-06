# PerformanceLongTaskTiming

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceLongTaskTiming&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `PerformanceLongTaskTiming` interface provides information about tasks that occupy the UI thread for 50 milliseconds or more.

## In this article

- [Description](#description)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

Long tasks that block the main thread for 50ms or more cause, among other issues:

- Delayed [Time to interactive](/en-US/docs/Glossary/Time_to_interactive) (TTI).
- High/variable input latency.
- High/variable event handling latency.
- Janky animations and scrolling.

A long task is any uninterrupted period where the main UI thread is busy for 50ms or longer. Common examples include:

- Long-running event handlers.
- Expensive reflows and other re-renders.
- Work the browser does between different turns of the event loop that exceeds 50 ms.

Long tasks refer to "culprit browsing context container", or "the container" for short, which is the top-level page, [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe), [<embed>](/en-US/docs/Web/HTML/Reference/Elements/embed) or [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) that the task occurred within.

For tasks that don't occur within the top-level page and for figuring out which container is responsible for the long task, the [TaskAttributionTiming](/en-US/docs/Web/API/TaskAttributionTiming) interface provides the `containerId`, `containerName` and `containerSrc` properties, which may provide more information about the source of the task.

`PerformanceLongTaskTiming` inherits from [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties for long task timing performance entry types by qualifying them as follows:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the elapsed time between the start and end of the task, with a 1ms granularity.

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Always returns `"longtask"`

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Returns one of the following strings referring to the browsing context or frame that can be attributed to the long task:

- `"cross-origin-ancestor"`
- `"cross-origin-descendant"`
- `"cross-origin-unreachable"`
- `"multiple-contexts"`
- `"same-origin-ancestor"`
- `"same-origin-descendant"`
- `"same-origin"`
- `"self"`
- `"unknown"`

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time when the task started.

This interface also supports the following properties:

[PerformanceLongTaskTiming.attribution](/en-US/docs/Web/API/PerformanceLongTaskTiming/attribution)Read onlyExperimental

Returns a sequence of [TaskAttributionTiming](/en-US/docs/Web/API/TaskAttributionTiming) instances.

## [Instance methods](#instance_methods)

[PerformanceLongTaskTiming.toJSON()](/en-US/docs/Web/API/PerformanceLongTaskTiming/toJSON)Experimental

Returns a JSON representation of the `PerformanceLongTaskTiming` object.

## [Examples](#examples)

### [Getting long tasks](#getting_long_tasks)

To get long task timing information, create a [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver) instance and then call its [observe()](/en-US/docs/Web/API/PerformanceObserver/observe) method, passing in `"longtask"` as the value of the [type](/en-US/docs/Web/API/PerformanceEntry/entryType) option. You also need to set `buffered` to `true` to get access to long tasks the user agent buffered while constructing the document. The `PerformanceObserver` object's callback will then be called with a list of `PerformanceLongTaskTiming` objects which you can analyze.

js

```
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(entry);
  });
});

observer.observe({ type: "longtask", buffered: true });
```

## [Specifications](#specifications)

Specification
[Long Tasks API# sec-PerformanceLongTaskTiming](https://w3c.github.io/longtasks/#sec-PerformanceLongTaskTiming)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [TaskAttributionTiming](/en-US/docs/Web/API/TaskAttributionTiming)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceLongTaskTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancelongtasktiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceLongTaskTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancelongtasktiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceLongTaskTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancelongtasktiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04301fa08caba25ce0fc17ea80e35383aa3361c0%0A*+Document+last+modified%3A+2024-10-08T19%3A44%3A13.000Z%0A%0A%3C%2Fdetails%3E)
