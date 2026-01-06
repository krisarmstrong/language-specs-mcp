# PerformanceMeasure

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceMeasure&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

`PerformanceMeasure` is an abstract interface for [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) objects with an [entryType](/en-US/docs/Web/API/PerformanceEntry/entryType) of `"measure"`. Entries of this type are created by calling [performance.measure()](/en-US/docs/Web/API/Performance/measure) to add a named[DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) (the measure) between two marks to the browser's performance timeline.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[PerformanceMeasure.detail](/en-US/docs/Web/API/PerformanceMeasure/detail)

Contains arbitrary metadata about the measure.

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties by qualifying/constraining the properties as follows:

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)

Returns `"measure"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)

Returns the name given to the measure when it was created via a call to [performance.measure()](/en-US/docs/Web/API/Performance/measure).

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)

Returns a [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) given to the measure when [performance.measure()](/en-US/docs/Web/API/Performance/measure) was called.

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that is the duration of the measure (typically, the measure's end mark timestamp minus its start mark timestamp).

## [Instance methods](#instance_methods)

This interface has no methods.

## [Example](#example)

See the example in [Using the User Timing API](/en-US/docs/Web/API/Performance_API/User_timing).

Chrome DevTools uses `performance.measure()` and in particular a structured `detail` property as part of its extensibility API that surfaces these in custom tracks in performance traces. See the example in [Performance: measure() method](/en-US/docs/Web/API/Performance/measure) page and the [Chrome's extensibility API documentation](https://developer.chrome.com/docs/devtools/performance/extension#inject_your_data_with_the_user_timings_api) for more information and examples.

## [Specifications](#specifications)

Specification
[User Timing# performancemeasure](https://w3c.github.io/user-timing/#performancemeasure)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [User Timing (Overview)](/en-US/docs/Web/API/Performance_API/User_timing)
- [Using the User Timing API](/en-US/docs/Web/API/Performance_API/User_timing)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 5, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformanceMeasure/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancemeasure/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceMeasure&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancemeasure%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformanceMeasure%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancemeasure%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5143045a1106f2e415985dec50f11d3cf5d1d4f9%0A*+Document+last+modified%3A+2025-11-05T20%3A46%3A43.000Z%0A%0A%3C%2Fdetails%3E)
