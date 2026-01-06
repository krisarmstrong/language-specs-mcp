# SnapEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSnapEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `SnapEvent` interface defines the event object for the [scrollsnapchanging](/en-US/docs/Web/API/Element/scrollsnapchanging_event) and [scrollsnapchange](/en-US/docs/Web/API/Element/scrollsnapchange_event) events. Respectively, these fire on a [scroll container](/en-US/docs/Glossary/Scroll_container) when the browser determines that a new scroll snap target is pending (will be selected when the current scroll gesture ends), and when a new snap target is selected.

These events can be used to run code in response to new elements being snapped to; `SnapEvent` exposes references to the element snapped to in the inline and/or block direction. The property values available on `SnapEvent` correspond directly to the value of the [scroll-snap-type](/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type) CSS property set on the scroll container:

- If the snap axis is specified as `block` (or a physical axis value that equates to `block` in the current writing mode), only [snapTargetBlock](/en-US/docs/Web/API/SnapEvent/snapTargetBlock) returns an element reference.
- If the snap axis is specified as `inline` (or a physical axis value that equates to `inline` in the current writing mode), only [snapTargetInline](/en-US/docs/Web/API/SnapEvent/snapTargetInline) returns an element reference.
- If the snap axis is specified as `both`, `snapTargetBlock` and `snapTargetInline` return an element reference.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[SnapEvent()](/en-US/docs/Web/API/SnapEvent/SnapEvent)Experimental

Creates a new `SnapEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[snapTargetBlock](/en-US/docs/Web/API/SnapEvent/snapTargetBlock)Read onlyExperimental

Returns a reference to the element snapped to in the block direction when the event fired, or `null` if scroll snapping only occurs in the inline direction so no element is snapped to in the block direction.

[snapTargetInline](/en-US/docs/Web/API/SnapEvent/snapTargetInline)Read onlyExperimental

Returns a reference to the element snapped to in the inline direction when the event fired, or `null` if scroll snapping only occurs in the block direction so no element is snapped to in the inline direction.

## [Examples](#examples)

### [scrollsnapchanging example](#scrollsnapchanging_example)

In the following `scrollsnapchanging` handler function snippet, we set the [snapTargetBlock](/en-US/docs/Web/API/SnapEvent/snapTargetBlock) element's `class` attribute to `pending` using the [Element.className](/en-US/docs/Web/API/Element/className) property, which could be used to style the element differently when it becomes a pending snap target.

Note that this handler is intended to be set on a block-direction scroll container (vertically-scrolling if the page is set to a horizontal [writing-mode](/en-US/docs/Web/CSS/Reference/Properties/writing-mode)), therefore only the `snapTargetBlock` element will change between multiple events firing. [SnapEvent.snapTargetInline](/en-US/docs/Web/API/SnapEvent/snapTargetInline) will return `null`, because no snapping occurs in the inline direction.

js

```
scrollingElem.addEventListener("scrollsnapchanging", (event) => {
  // Set current pending snap target class to "pending"
  event.snapTargetBlock.className = "pending";

  // Logs the new pending block-direction snap target element
  console.log(event.snapTargetBlock);

  // Logs null; no inline snapping occurs
  console.log(event.snapTargetInline);
});
```

### [scrollsnapchange example](#scrollsnapchange_example)

In the following `scrollsnapchange` handler function snippet, we set a `selected` class on the [SnapEvent.snapTargetBlock](/en-US/docs/Web/API/SnapEvent/snapTargetBlock) element, which could be used to style a newly-selected snap target to look like it has been selected (for example, with an animation).

js

```
scrollingElem.addEventListener("scrollsnapchange", (event) => {
  event.snapTargetBlock.className = "selected";
});
```

## [Specifications](#specifications)

Specification
[CSS Scroll Snap Module Level 2# snapevent-interface](https://drafts.csswg.org/css-scroll-snap-2/#snapevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [scrollsnapchanging](/en-US/docs/Web/API/Element/scrollsnapchanging_event) event
- [scrollsnapchange](/en-US/docs/Web/API/Element/scrollsnapchange_event) event
- [CSS scroll snap module](/en-US/docs/Web/CSS/Guides/Scroll_snap)
- [Using scroll snap events](/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events)
- [Scroll Snap Events](https://developer.chrome.com/blog/scroll-snap-events) on developer.chrome.com (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SnapEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/snapevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSnapEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsnapevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSnapEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsnapevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
