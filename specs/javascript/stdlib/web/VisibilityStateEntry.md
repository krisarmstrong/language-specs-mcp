# VisibilityStateEntry

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVisibilityStateEntry&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `VisibilityStateEntry` interface provides timings of page visibility state changes, i.e., when a tab changes from the foreground to the background or vice versa.

This can be used to pinpoint visibility changes on the performance timeline, and cross-reference them against other performance entries such as "first-contentful-paint" (see [PerformancePaintTiming](/en-US/docs/Web/API/PerformancePaintTiming)).

There are two key visibility state change times that this API reports on:

- `visible`: The time when the page becomes visible (i.e., when its tab moves into the foreground).
- `hidden`: The time when the pages become hidden (i.e., when its tab moves into the background).

The performance timeline will always have a `"visibility-state"` entry with a `startTime` of `0` and a `name` representing the initial page visibility state.

Note: Like other Performance APIs, this API extends [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface has no properties but it extends the properties of [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) by qualifying and constraining them as follows:

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Experimental

Returns `"visibility-state"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Experimental

Returns either `"visible"` or `"hidden"`.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Experimental

Returns the [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) when the visibility state change occurred.

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Experimental

Returns 0.

## [Instance methods](#instance_methods)

This interface has no methods.

## [Examples](#examples)

### [Basic usage](#basic_usage)

The following function could be used to log a table of all `"visibility-state"` performance entries to the console:

js

```
function getVisibilityStateEntries() {
  const visibilityStateEntries =
    performance.getEntriesByType("visibility-state");
  console.table(visibilityStateEntries);
}
```

### [Correlating visibility state changes with paint timing](#correlating_visibility_state_changes_with_paint_timing)

The below function gets a reference to all `"visibility-state"` entries and the `"first-contentful-paint"` entry, then uses [Array.some()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some) to test whether any of the `"hidden"` visibility entries occurred before the first contentful paint:

js

```
function wasHiddenBeforeFirstContentfulPaint() {
  const fcpEntry = performance.getEntriesByName("first-contentful-paint")[0];
  const visibilityStateEntries =
    performance.getEntriesByType("visibility-state");
  return visibilityStateEntries.some(
    (e) => e.startTime < fcpEntry.startTime && e.name === "hidden",
  );
}
```

## [Specifications](#specifications)

Specification
[HTML# the-visibilitystateentry-interface](https://html.spec.whatwg.org/multipage/interaction.html#the-visibilitystateentry-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

[Page Visibility API](/en-US/docs/Web/API/Page_Visibility_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VisibilityStateEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/visibilitystateentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVisibilityStateEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvisibilitystateentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVisibilityStateEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvisibilitystateentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
