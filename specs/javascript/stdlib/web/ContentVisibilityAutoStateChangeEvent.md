# ContentVisibilityAutoStateChangeEvent

 Baseline  2024 Newly available

 Since ⁨September 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentVisibilityAutoStateChangeEvent&level=low)

The `ContentVisibilityAutoStateChangeEvent` interface is the event object for the [contentvisibilityautostatechange](/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event) event, which fires on any element with [content-visibility: auto](/en-US/docs/Web/CSS/Reference/Properties/content-visibility) set on it when it starts or stops being [relevant to the user](/en-US/docs/Web/CSS/Guides/Containment/Using#relevant_to_the_user) and [skipping its contents](/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents).

While the element is not relevant (between the start and end events), the user agent skips an element's rendering, including layout and painting. This can significantly improve page rendering speed. The [contentvisibilityautostatechange](/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event) event provides a way for an app's code to also start or stop rendering processes (e.g., drawing on a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas)) when they are not needed, thereby conserving processing power.

Note that even when hidden from view, element contents will remain semantically relevant (e.g., to assistive technology users), so this signal should not be used to skip significant semantic DOM updates.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ContentVisibilityAutoStateChangeEvent()](/en-US/docs/Web/API/ContentVisibilityAutoStateChangeEvent/ContentVisibilityAutoStateChangeEvent)

Creates a new `ContentVisibilityAutoStateChangeEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[skipped](/en-US/docs/Web/API/ContentVisibilityAutoStateChangeEvent/skipped)Read only

Returns `true` if the user agent is skipping the element's rendering, or `false` otherwise.

## [Examples](#examples)

js

```
const canvasElem = document.querySelector("canvas");

canvasElem.addEventListener("contentvisibilityautostatechange", stateChanged);
canvasElem.style.contentVisibility = "auto";

function stateChanged(event) {
  if (event.skipped) {
    stopCanvasUpdates(canvasElem);
  } else {
    startCanvasUpdates(canvasElem);
  }
}

// Call this when the canvas updates need to start.
function startCanvasUpdates(canvas) {
  // …
}

// Call this when the canvas updates need to stop.
function stopCanvasUpdates(canvas) {
  // …
}
```

## [Specifications](#specifications)

Specification
[CSS Containment Module Level 2# content-visibility-auto-state-change](https://drafts.csswg.org/css-contain/#content-visibility-auto-state-change)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [contentvisibilityautostatechange](/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event) event
- [CSS Containment](/en-US/docs/Web/CSS/Guides/Containment)
- The [content-visibility](/en-US/docs/Web/CSS/Reference/Properties/content-visibility) property
- The [contain](/en-US/docs/Web/CSS/Reference/Properties/contain) property

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ContentVisibilityAutoStateChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/contentvisibilityautostatechangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentVisibilityAutoStateChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcontentvisibilityautostatechangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FContentVisibilityAutoStateChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcontentvisibilityautostatechangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
