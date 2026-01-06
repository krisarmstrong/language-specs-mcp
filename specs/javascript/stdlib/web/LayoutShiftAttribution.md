# LayoutShiftAttribution

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLayoutShiftAttribution&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `LayoutShiftAttribution` interface provides debugging information about elements which have shifted.

Instances of `LayoutShiftAttribution` are returned in an array by calling [LayoutShift.sources](/en-US/docs/Web/API/LayoutShift/sources).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[LayoutShiftAttribution.node](/en-US/docs/Web/API/LayoutShiftAttribution/node)Read onlyExperimental

Returns the element that has shifted (null if it has been removed).

[LayoutShiftAttribution.previousRect](/en-US/docs/Web/API/LayoutShiftAttribution/previousRect)Read onlyExperimental

Returns a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) object representing the position of the element before the shift.

[LayoutShiftAttribution.currentRect](/en-US/docs/Web/API/LayoutShiftAttribution/currentRect)Read onlyExperimental

Returns a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) object representing the position of the element after the shift.

## [Instance methods](#instance_methods)

[LayoutShiftAttribution.toJSON()](/en-US/docs/Web/API/LayoutShiftAttribution/toJSON)Experimental

Returns a JSON representation of the `LayoutShiftAttribution` object.

## [Examples](#examples)

The following example observes layout shifts and identifies the most impactful element. The `sources` array is sorted by impact area, in descending order — so the first element (`sources[0]`) represents the element that contributed most to the layout shift. For more detail on that, see [Debug Web Vitals in the field](https://web.dev/articles/debug-performance-in-the-field).

js

```
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.sources || entry.sources.length === 0) continue;

    const mostImpactfulSource = entry.sources[0];
    console.log("Layout shift score:", entry.value);
    console.log("Most impactful element:", largestShiftSource.node);
    console.log("Previous position:", largestShiftSource.previousRect);
    console.log("Current position:", largestShiftSource.currentRect);
  }
});

observer.observe({ type: "layout-shift", buffered: true });
```

## [Specifications](#specifications)

Specification
[Layout Instability API# sec-layout-shift-attribution](https://wicg.github.io/layout-instability/#sec-layout-shift-attribution)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Debug layout shifts](https://web.dev/articles/debug-layout-shifts)
- [Debug Web Vitals in the field](https://web.dev/articles/debug-performance-in-the-field)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/LayoutShiftAttribution/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/layoutshiftattribution/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLayoutShiftAttribution&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Flayoutshiftattribution%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FLayoutShiftAttribution%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Flayoutshiftattribution%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5a74ef0b42f3585521b06dae93b72547649d83c%0A*+Document+last+modified%3A+2025-12-02T11%3A25%3A54.000Z%0A%0A%3C%2Fdetails%3E)
