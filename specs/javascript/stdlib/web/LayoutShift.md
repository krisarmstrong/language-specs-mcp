# LayoutShift

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLayoutShift&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `LayoutShift` interface of the [Performance API](/en-US/docs/Web/API/Performance_API) provides insights into the layout stability of web pages based on movements of the elements on the page.

## In this article

- [Description](#description)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

A layout shift happens when any element that is visible in the viewport changes its position between two frames. These elements are described as being unstable, indicating a lack of visual stability.

The Layout Instability API provides a way to measure and report on these layout shifts. All tools for debugging layout shifts, including those in the browser's developer tools, use this API. The API can also be used to observe and debug layout shifts by logging the information to the console, to send the data to a server endpoint, or to web page analytics.

Performance tools can use this API to calculate a [CLS](/en-US/docs/Glossary/CLS) score.

## [Instance properties](#instance_properties)

This interface extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties by qualifying them as follows:

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)Read onlyExperimental

Always returns `0` (the concept of duration does not apply to layout shifts).

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)Read onlyExperimental

Always returns `"layout-shift"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)Read onlyExperimental

Always returns `"layout-shift"`.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)Read onlyExperimental

Returns a [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) representing the time when the layout shift started.

This interface also supports the following properties:

[LayoutShift.value](/en-US/docs/Web/API/LayoutShift/value)Experimental

Returns the layout shift score calculated as the impact fraction (fraction of the viewport that was shifted) multiplied by the distance fraction (distance moved as a fraction of viewport).

[LayoutShift.hadRecentInput](/en-US/docs/Web/API/LayoutShift/hadRecentInput)Experimental

Returns `true` if [lastInputTime](/en-US/docs/Web/API/LayoutShift/lastInputTime) is less than 500 milliseconds in the past.

[LayoutShift.lastInputTime](/en-US/docs/Web/API/LayoutShift/lastInputTime)Experimental

Returns the time of the most recent excluding input (user input that would exclude this entry as a contributor to the CLS score) or `0` if no excluding input has occurred.

[LayoutShift.sources](/en-US/docs/Web/API/LayoutShift/sources)Experimental

Returns an array of [LayoutShiftAttribution](/en-US/docs/Web/API/LayoutShiftAttribution) objects with information on the elements that were shifted.

## [Instance methods](#instance_methods)

[LayoutShift.toJSON()](/en-US/docs/Web/API/LayoutShift/toJSON)Experimental

Converts the properties to JSON.

## [Examples](#examples)

### [Logging layout shift values](#logging_layout_shift_values)

The following example shows how to capture layout shifts and log them to the console.

js

```
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    // Count layout shifts without recent user input only
    if (!entry.hadRecentInput) {
      console.log("LayoutShift value:", entry.value);
      if (entry.sources) {
        for (const { node, currentRect, previousRect } of entry.sources)
          console.log("LayoutShift source:", node, {
            currentRect,
            previousRect,
          });
      }
    }
  }
});

observer.observe({ type: "layout-shift", buffered: true });
```

## [Specifications](#specifications)

Specification
[Layout Instability API# sec-layout-shift](https://wicg.github.io/layout-instability/#sec-layout-shift)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [LayoutShiftAttribution](/en-US/docs/Web/API/LayoutShiftAttribution)
- [CLS](/en-US/docs/Glossary/CLS)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 15, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/LayoutShift/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/layoutshift/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLayoutShift&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flayoutshift%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLayoutShift%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flayoutshift%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffcd4f39485d740615c32ccaef63471bc27095fb0%0A*+Document+last+modified%3A+2024-05-15T02%3A31%3A46.000Z%0A%0A%3C%2Fdetails%3E)
