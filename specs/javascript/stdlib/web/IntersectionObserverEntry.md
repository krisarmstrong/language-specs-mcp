# IntersectionObserverEntry

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserverEntry&level=high)

The `IntersectionObserverEntry` interface of the [Intersection Observer API](/en-US/docs/Web/API/Intersection_Observer_API) describes the intersection between the target element and its root container at a specific moment of transition.

Instances of `IntersectionObserverEntry` are delivered to an [IntersectionObserver](/en-US/docs/Web/API/IntersectionObserver) callback in its `entries` parameter; otherwise, these objects can only be obtained by calling [IntersectionObserver.takeRecords()](/en-US/docs/Web/API/IntersectionObserver/takeRecords).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[IntersectionObserverEntry.boundingClientRect](/en-US/docs/Web/API/IntersectionObserverEntry/boundingClientRect)Read only

Returns the bounds rectangle of the target element as a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly). The bounds are computed as described in the documentation for [Element.getBoundingClientRect()](/en-US/docs/Web/API/Element/getBoundingClientRect).

[IntersectionObserverEntry.intersectionRatio](/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio)Read only

Returns the ratio of the `intersectionRect` to the `boundingClientRect`.

[IntersectionObserverEntry.intersectionRect](/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRect)Read only

Returns a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) representing the target's visible area.

[IntersectionObserverEntry.isIntersecting](/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting)Read only

A Boolean value which is `true` if the target element intersects with the intersection observer's root. If this is `true`, then, the `IntersectionObserverEntry` describes a transition into a state of intersection; if it's `false`, then you know the transition is from intersecting to not-intersecting.

[IntersectionObserverEntry.rootBounds](/en-US/docs/Web/API/IntersectionObserverEntry/rootBounds)Read only

Returns a [DOMRectReadOnly](/en-US/docs/Web/API/DOMRectReadOnly) for the intersection observer's root.

[IntersectionObserverEntry.target](/en-US/docs/Web/API/IntersectionObserverEntry/target)Read only

The [Element](/en-US/docs/Web/API/Element) whose intersection with the root changed.

[IntersectionObserverEntry.time](/en-US/docs/Web/API/IntersectionObserverEntry/time)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the time at which the intersection was recorded, relative to the `IntersectionObserver`'s [time origin](/en-US/docs/Web/API/Performance/timeOrigin).

## [Instance methods](#instance_methods)

This interface has no methods.

## [Specifications](#specifications)

Specification
[Intersection Observer# intersection-observer-entry](https://w3c.github.io/IntersectionObserver/#intersection-observer-entry)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/IntersectionObserverEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/intersectionobserverentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserverEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fintersectionobserverentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserverEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fintersectionobserverentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff9f48866f02963e752717310b76a70d5bdaf554c%0A*+Document+last+modified%3A+2024-07-02T08%3A05%3A13.000Z%0A%0A%3C%2Fdetails%3E)
