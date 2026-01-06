# PerformancePaintTiming

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformancePaintTiming&level=high)

The `PerformancePaintTiming` interface provides timing information about "paint" (also called "render") operations during web page construction. "Paint" refers to conversion of the render tree to on-screen pixels.

There are two key paint moments this API provides:

- [First Paint](/en-US/docs/Glossary/First_paint) (FP): Time when anything is rendered. Note that the marking of the first paint is optional, not all user agents report it.
- [First Contentful Paint](/en-US/docs/Glossary/First_contentful_paint) (FCP): Time when the first bit of DOM text or image content is rendered.

A third key paint moment is provided by the [LargestContentfulPaint](/en-US/docs/Web/API/LargestContentfulPaint) API:

- [Largest Contentful Paint](/en-US/docs/Glossary/Largest_contentful_paint) (LCP): Render time of the largest image or text block visible within the viewport, recorded from when the page first begins to load.

The data this API provides helps you minimize the time that users have to wait before they can see the site's content start to appear. Decreasing the time until these key paint moments make sites feel more responsive, performant, and engaging for your users.

Like other Performance APIs, this API extends [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface has no properties but it extends the following [PerformanceEntry](/en-US/docs/Web/API/PerformanceEntry) properties by qualifying and constraining the properties as follows:

[PerformanceEntry.entryType](/en-US/docs/Web/API/PerformanceEntry/entryType)

Returns `"paint"`.

[PerformanceEntry.name](/en-US/docs/Web/API/PerformanceEntry/name)

Returns either `"first-paint"` or `"first-contentful-paint"`.

[PerformanceEntry.startTime](/en-US/docs/Web/API/PerformanceEntry/startTime)

Returns the [timestamp](/en-US/docs/Web/API/DOMHighResTimeStamp) when the paint occurred.

[PerformanceEntry.duration](/en-US/docs/Web/API/PerformanceEntry/duration)

Returns 0.

## [Instance methods](#instance_methods)

[PerformancePaintTiming.toJSON()](/en-US/docs/Web/API/PerformancePaintTiming/toJSON)

Returns a JSON representation of the `PerformancePaintTiming` object.

## [Examples](#examples)

### [Getting paint timings](#getting_paint_timings)

Example using a [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver), which notifies of new `paint` performance entries as they are recorded in the browser's performance timeline. Use the `buffered` option to access entries from before the observer creation.

js

```
const observer = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(
      `The time to ${entry.name} was ${entry.startTime} milliseconds.`,
    );
    // Logs "The time to first-paint was 386.7999999523163 milliseconds."
    // Logs "The time to first-contentful-paint was 400.6999999284744 milliseconds."
  });
});

observer.observe({ type: "paint", buffered: true });
```

Example using [Performance.getEntriesByType()](/en-US/docs/Web/API/Performance/getEntriesByType), which only shows `paint` performance entries present in the browser's performance timeline at the time you call this method:

js

```
const entries = performance.getEntriesByType("paint");
entries.forEach((entry) => {
  console.log(`The time to ${entry.name} was ${entry.startTime} milliseconds.`);
  // Logs "The time to first-paint was 386.7999999523163 milliseconds."
  // Logs "The time to first-contentful-paint was 400.6999999284744 milliseconds."
});
```

## [Specifications](#specifications)

Specification
[Paint Timing# sec-PerformancePaintTiming](https://w3c.github.io/paint-timing/#sec-PerformancePaintTiming)

## [Browser compatibility](#browser_compatibility)

### [See also](#see_also)

- [LargestContentfulPaint](/en-US/docs/Web/API/LargestContentfulPaint)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PerformancePaintTiming/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/performancepainttiming/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformancePaintTiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fperformancepainttiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPerformancePaintTiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fperformancepainttiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fff2d2a411c10d5b8b6732a66e69d0b78842b44fe%0A*+Document+last+modified%3A+2025-12-19T11%3A37%3A43.000Z%0A%0A%3C%2Fdetails%3E)
