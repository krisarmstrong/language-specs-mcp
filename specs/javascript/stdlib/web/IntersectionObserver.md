# IntersectionObserver

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserver&level=high)

The `IntersectionObserver` interface of the [Intersection Observer API](/en-US/docs/Web/API/Intersection_Observer_API) provides a way to asynchronously observe changes in the intersection of a target element with an ancestor element or with a top-level document's [viewport](/en-US/docs/Glossary/Viewport). The ancestor element or viewport is referred to as the root.

When an `IntersectionObserver` is created, it's configured to watch for given ratios of visibility within the root. The configuration cannot be changed once the `IntersectionObserver` is created, so a given observer object is only useful for watching for specific changes in degree of visibility; however, you can watch multiple target elements with the same observer.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[IntersectionObserver()](/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver)

Creates a new `IntersectionObserver` object which will execute a specified callback function when it detects that a target element's visibility has crossed one or more thresholds.

## [Instance properties](#instance_properties)

[IntersectionObserver.delay](/en-US/docs/Web/API/IntersectionObserver/delay)Read onlyExperimental

An integer indicating the minimum delay between notifications from this observer.

[IntersectionObserver.root](/en-US/docs/Web/API/IntersectionObserver/root)Read only

The [Element](/en-US/docs/Web/API/Element) or [Document](/en-US/docs/Web/API/Document) whose bounds are used as the bounding box when testing for intersection. If no `root` value was passed to the constructor or its value is `null`, the top-level document's viewport is used.

[IntersectionObserver.rootMargin](/en-US/docs/Web/API/IntersectionObserver/rootMargin)Read only

An offset rectangle applied to the root's [bounding box](/en-US/docs/Glossary/Bounding_box) when calculating intersections, effectively shrinking or growing the root for calculation purposes. The value returned by this property may not be the same as the one specified when calling the constructor as it may be changed to match internal requirements. Each offset can be expressed in pixels (`px`) or percentages (`%`). The default is "0px 0px 0px 0px".

[IntersectionObserver.scrollMargin](/en-US/docs/Web/API/IntersectionObserver/scrollMargin)Read only

An offset rectangle applied to each [scroll container](/en-US/docs/Glossary/Scroll_container) on the path from intersection root to target, effectively shrinking or growing the clip rectangles used to calculate intersections. The value returned by this property may not be the same as the one specified when calling the constructor.

[IntersectionObserver.thresholds](/en-US/docs/Web/API/IntersectionObserver/thresholds)Read only

A list of thresholds, sorted in increasing numeric order, where each threshold is a ratio of intersection area to bounding box area of an observed target. Notifications for a target are generated when any of the thresholds are crossed for that target. If no value was passed to the constructor, 0 is used.

[IntersectionObserver.trackVisibility](/en-US/docs/Web/API/IntersectionObserver/trackVisibility)Read onlyExperimental

A boolean indicating whether this `IntersectionObserver` is checking that the target does not have compromised visibility.

## [Instance methods](#instance_methods)

[IntersectionObserver.disconnect()](/en-US/docs/Web/API/IntersectionObserver/disconnect)

Stops the `IntersectionObserver` object from observing any target.

[IntersectionObserver.observe()](/en-US/docs/Web/API/IntersectionObserver/observe)

Tells the `IntersectionObserver` a target element to observe.

[IntersectionObserver.takeRecords()](/en-US/docs/Web/API/IntersectionObserver/takeRecords)

Returns an array of [IntersectionObserverEntry](/en-US/docs/Web/API/IntersectionObserverEntry) objects for all observed targets.

[IntersectionObserver.unobserve()](/en-US/docs/Web/API/IntersectionObserver/unobserve)

Tells the `IntersectionObserver` to stop observing a particular target element.

## [Examples](#examples)

js

```
const intersectionObserver = new IntersectionObserver((entries) => {
  // If intersectionRatio is 0, the target is out of view
  // and we do not need to do anything.
  if (entries[0].intersectionRatio <= 0) return;

  loadItems(10);
  console.log("Loaded new items");
});
// start observing
intersectionObserver.observe(document.querySelector(".scrollerFooter"));
```

## [Specifications](#specifications)

Specification
[Intersection Observer# intersection-observer-interface](https://w3c.github.io/IntersectionObserver/#intersection-observer-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MutationObserver](/en-US/docs/Web/API/MutationObserver)
- [PerformanceObserver](/en-US/docs/Web/API/PerformanceObserver)
- [ResizeObserver](/en-US/docs/Web/API/ResizeObserver)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 29, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IntersectionObserver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/intersectionobserver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fintersectionobserver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fintersectionobserver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1b61fe3aa68b972468514d5ab13ed93497b13a96%0A*+Document+last+modified%3A+2025-07-29T05%3A42%3A24.000Z%0A%0A%3C%2Fdetails%3E)
