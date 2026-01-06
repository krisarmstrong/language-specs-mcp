# Viewport Segments API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewport_segments_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Viewport Segments API allows developers to access the position and dimensions of logically separate viewport segments using CSS and JavaScript. Viewport segments are created when the viewport is split by one or more hardware features such as a fold or a hinge between separate displays. With the Viewport Segments API, developers can create responsive designs optimized for different viewport segment sizes and arrangements.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [CSS features](#css_features)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Devices with multiple displays that are intended to act as different segments of the same display surface (think foldable or hinged screen smartphones) present some unique design challenges to developers. You can optimize your layout for the display as a single entity, but how can you ensure that design elements fit snugly on the different segments and are not cut into two pieces? And how can you prevent content from being hidden by the physical fold/join?

It may be important to know whether a user's device screen has a fold or join, what size the different segments are, whether they are the same size, and the orientation of the segments (whether they are side-by-side or top-to-bottom). The Viewport Segments API enables accessing the user's segmented device information with CSS and JavaScript features that provide access to the position and dimensions of each viewport segment within a display, including [@media](/en-US/docs/Web/CSS/Reference/At-rules/@media) features to detect different horizontal and vertical region layouts.

For an explanation of how the API works, see [Using the Viewport Segments API](/en-US/docs/Web/API/Viewport_segments_API/Using).

## [Interfaces](#interfaces)

[Viewport](/en-US/docs/Web/API/Viewport)

Represents the device's viewport. Provides access to the [Viewport.segments](/en-US/docs/Web/API/Viewport/segments) property, which returns an array of [DOMRect](/en-US/docs/Web/API/DOMRect) objects representing the position and dimensions of each viewport segment within a segmented display.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Window.viewport](/en-US/docs/Web/API/Window/viewport)

Returns a `Viewport` object instance, which provides information about the current state of the device's viewport.

## [CSS features](#css_features)

[horizontal-viewport-segments](/en-US/docs/Web/CSS/Reference/At-rules/@media/horizontal-viewport-segments)`@media` feature

Detects whether the device has a specified number of viewport segments laid out horizontally.

[vertical-viewport-segments](/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments)`@media` feature

Detects whether the device has a specified number of viewport segments laid out vertically.

[Viewport segment environment variables](/en-US/docs/Web/CSS/Reference/Values/env#viewport-segment-width)

These [environment variables](/en-US/docs/Web/CSS/Guides/Environment_variables/Using) provide access to the edge coordinates and dimensions of each viewport segment.

## [Examples](#examples)

You can find a complete example demonstrating usage of the above features in the [Viewport segment API demo](https://mdn.github.io/dom-examples/viewport-segments-api/).

If possible, you should view the demo on a foldable device. Current browser developer tools enable emulating foldable devices, but don't include emulation of the different physical segments.

## [Specifications](#specifications)

Specification
[CSS Viewport Module Level 1# dom-viewport-segments](https://drafts.csswg.org/css-viewport/#dom-viewport-segments)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Viewport Segments API](/en-US/docs/Web/API/Viewport_segments_API/Using)
- [CSSOM view API](/en-US/docs/Web/API/CSSOM_view_API)
- [Device Posture API](/en-US/docs/Web/API/Device_Posture_API)
- [CSS environment variables](/en-US/docs/Web/CSS/Guides/Environment_variables) module
- [Origin trial for Foldable APIs](https://developer.chrome.com/blog/foldable-apis-ot) via developer.chrome.com (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Viewport_segments_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/viewport_segments_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewport_segments_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fviewport_segments_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewport_segments_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fviewport_segments_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9be502ee0f8b030908e59d30884190281acb8054%0A*+Document+last+modified%3A+2025-11-19T16%3A16%3A06.000Z%0A%0A%3C%2Fdetails%3E)
