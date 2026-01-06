# SVGSVGElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGSVGElement&level=high)

The `SVGSVGElement` interface provides access to the properties of [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) elements, as well as methods to manipulate them. This interface contains also various miscellaneous commonly-used utility methods, such as matrix operations and the ability to control the time of redraw on visual rendering devices.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Event handlers](#event_handlers)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGSVGElement.x](/en-US/docs/Web/API/SVGSVGElement/x)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [x](/en-US/docs/Web/SVG/Reference/Attribute/x) attribute of the given [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element.

[SVGSVGElement.y](/en-US/docs/Web/API/SVGSVGElement/y)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [y](/en-US/docs/Web/SVG/Reference/Attribute/y) attribute of the given [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element.

[SVGSVGElement.width](/en-US/docs/Web/API/SVGSVGElement/width)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [width](/en-US/docs/Web/SVG/Reference/Attribute/width) attribute of the given [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element.

[SVGSVGElement.height](/en-US/docs/Web/API/SVGSVGElement/height)Read only

An [SVGAnimatedLength](/en-US/docs/Web/API/SVGAnimatedLength) corresponding to the [height](/en-US/docs/Web/SVG/Reference/Attribute/height) attribute of the given [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element.

[SVGSVGElement.viewBox](/en-US/docs/Web/API/SVGSVGElement/viewBox)Read only

An [SVGAnimatedRect](/en-US/docs/Web/API/SVGAnimatedRect) corresponding to the [viewBox](/en-US/docs/Web/SVG/Reference/Attribute/viewBox) attribute of the given [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element.

[SVGSVGElement.preserveAspectRatio](/en-US/docs/Web/API/SVGSVGElement/preserveAspectRatio)Read only

An [SVGAnimatedPreserveAspectRatio](/en-US/docs/Web/API/SVGAnimatedPreserveAspectRatio) corresponding to the [preserveAspectRatio](/en-US/docs/Web/SVG/Reference/Attribute/preserveAspectRatio) attribute of the given [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element.

`SVGSVGElement.pixelUnitToMillimeterX`Deprecated

A float representing the size of the pixel unit (as defined by CSS2) along the x-axis of the viewport, which represents a unit somewhere in the range of 70dpi to 120dpi, and, on systems that support this, might actually match the characteristics of the target medium. On systems where it is impossible to know the size of a pixel, a suitable default pixel size is provided.

`SVGSVGElement.pixelUnitToMillimeterY`Deprecated

A float representing the size of a pixel unit along the y-axis of the viewport.

`SVGSVGElement.screenPixelToMillimeterX`Deprecated

User interface (UI) events in DOM Level 2 indicate the screen positions at which the given UI event occurred. When the browser actually knows the physical size of a "screen unit", this float attribute will express that information; otherwise, user agents will provide a suitable default value (such as `.28mm`).

`SVGSVGElement.screenPixelToMillimeterY`Deprecated

Corresponding size of a screen pixel along the y-axis of the viewport.

`SVGSVGElement.useCurrentView`DeprecatedNon-standard

The initial view (i.e., before magnification and panning) of the current innermost SVG document fragment can be either the "standard" view, i.e., based on attributes on the [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element such as [viewBox](/en-US/docs/Web/SVG/Reference/Attribute/viewBox) or on a "custom" view (i.e., a hyperlink into a particular [<view>](/en-US/docs/Web/SVG/Reference/Element/view) or other element). If the initial view is the "standard" view, then this attribute is `false`. If the initial view is a "custom" view, then this attribute is `true`.

`SVGSVGElement.currentView`DeprecatedNon-standard

An `SVGViewSpec` defining the initial view (i.e., before magnification and panning) of the current innermost SVG document fragment. The meaning depends on the situation: If the initial view was a "standard" view, then:

- the values for `viewBox`, `preserveAspectRatio`, and `zoomAndPan` within `currentView` will match the values for the corresponding DOM attributes that are on `SVGSVGElement` directly
- the value for `transform` within `currentView` will be `null`

If the initial view was a link into a [<view>](/en-US/docs/Web/SVG/Reference/Element/view) element, then:

- the values for `viewBox`, `preserveAspectRatio`, and `zoomAndPan` within `currentView` will correspond to the corresponding attributes for the given [<view>](/en-US/docs/Web/SVG/Reference/Element/view) element
- the value for `transform` within `currentView` will be `null`

If the initial view was a link into another element (i.e., other than a [<view>](/en-US/docs/Web/SVG/Reference/Element/view)), then:

- the values for `viewBox`, `preserveAspectRatio`, and `zoomAndPan` within `currentView` will match the values for the corresponding DOM attributes that are on `SVGSVGElement` directly for the closest ancestor [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element
- the values for `transform` within `currentView` will be `null`

If the initial view was a link into the SVG document fragment using an SVG view specification fragment identifier (i.e., `#svgView(…)`), then:

- the values for `viewBox`, `preserveAspectRatio`, `zoomAndPan`, and `transform` within `currentView` will correspond to the values from the SVG view specification fragment identifier

[SVGSVGElement.currentScale](/en-US/docs/Web/API/SVGSVGElement/currentScale)

On an outermost [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element, this float attribute indicates the current scale factor relative to the initial view to take into account user magnification and panning operations. DOM attributes `currentScale` and `currentTranslate` are equivalent to the 2×3 matrix `[a b c d e f] = [currentScale 0 0 currentScale currentTranslate.x currentTranslate.y]`. If "magnification" is enabled (i.e., `zoomAndPan="magnify"`), then the effect is as if an extra transformation were placed at the outermost level on the SVG document fragment (i.e., outside the outermost [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element).

[SVGSVGElement.currentTranslate](/en-US/docs/Web/API/SVGSVGElement/currentTranslate)Read only

A [DOMPointReadOnly](/en-US/docs/Web/API/DOMPointReadOnly) representing the translation factor that takes into account user "magnification" corresponding to an outermost [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element. The behavior is undefined for `<svg>` elements that are not at the outermost level.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

`SVGSVGElement.suspendRedraw()`Deprecated

Takes a time-out value which indicates that redraw shall not occur until:

the corresponding `unsuspendRedraw()` call has been made, an `unsuspendRedrawAll()` call has been made, or its timer has timed out.

In environments that do not support interactivity (e.g., print media), then redraw shall not be suspended. Calls to `suspendRedraw()` and `unsuspendRedraw()` should, but need not be, made in balanced pairs.

To suspend redraw actions as a collection of SVG DOM changes occur, precede the changes to the SVG DOM with a method call similar to:

js

```
const suspendHandleID = suspendRedraw(maxWaitMilliseconds);
```

and follow the changes with a method call similar to:

js

```
unsuspendRedraw(suspendHandleID);
```

Note that multiple `suspendRedraw()` calls can be used at once, and that each such method call is treated independently of the other `suspendRedraw()` method calls.

`SVGSVGElement.unsuspendRedraw()`Deprecated

Cancels a specified `suspendRedraw()` by providing a unique suspend handle ID that was returned by a previous `suspendRedraw()` call.

`SVGSVGElement.unsuspendRedrawAll()`Deprecated

Cancels all currently active `suspendRedraw()` method calls. This method is most useful at the very end of a set of SVG DOM calls to ensure that all pending `suspendRedraw()` method calls have been cancelled.

`SVGSVGElement.forceRedraw()`Deprecated

In rendering environments supporting interactivity, forces the user agent to immediately redraw all regions of the viewport that require updating.

[SVGSVGElement.pauseAnimations()](/en-US/docs/Web/API/SVGSVGElement/pauseAnimations)

Suspends (i.e., pauses) all currently running animations that are defined within the SVG document fragment corresponding to this [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element, causing the animation clock corresponding to this document fragment to stand still until it is unpaused.

[SVGSVGElement.unpauseAnimations()](/en-US/docs/Web/API/SVGSVGElement/unpauseAnimations)

Resumes (i.e., unpauses) currently running animations that are defined within the SVG document fragment, causing the animation clock to continue from the time at which it was suspended.

[SVGSVGElement.animationsPaused()](/en-US/docs/Web/API/SVGSVGElement/animationsPaused)

Returns `true` if this SVG document fragment is in a paused state.

[SVGSVGElement.getCurrentTime()](/en-US/docs/Web/API/SVGSVGElement/getCurrentTime)

Returns the current time in seconds relative to the start time for the current SVG document fragment. If `getCurrentTime()` is called before the document timeline has begun (for example, by script running in a [<script>](/en-US/docs/Web/SVG/Reference/Element/script) element before the document's `SVGLoad` event is dispatched), then `0` is returned.

[SVGSVGElement.setCurrentTime()](/en-US/docs/Web/API/SVGSVGElement/setCurrentTime)

Adjusts the clock for this SVG document fragment, establishing a new current time. If `setCurrentTime()` is called before the document timeline has begun (for example, by script running in a [<script>](/en-US/docs/Web/SVG/Reference/Element/script) element before the document's `SVGLoad` event is dispatched), then the value of seconds in the last invocation of the method gives the time that the document will seek to once the document timeline has begun.

`SVGSVGElement.getIntersectionList()`

Returns a [NodeList](/en-US/docs/Web/API/NodeList) of graphics elements whose rendered content intersects the supplied rectangle. Each candidate graphics element is to be considered a match only if the same graphics element can be a target of pointer events as defined in [pointer-events](/en-US/docs/Web/SVG/Reference/Attribute/pointer-events) processing.

`SVGSVGElement.getEnclosureList()`

Returns a [NodeList](/en-US/docs/Web/API/NodeList) of graphics elements whose rendered content is entirely contained within the supplied rectangle. Each candidate graphics element is to be considered a match only if the same graphics element can be a target of pointer events as defined in [pointer-events](/en-US/docs/Web/SVG/Reference/Attribute/pointer-events) processing.

[SVGSVGElement.checkIntersection()](/en-US/docs/Web/API/SVGSVGElement/checkIntersection)

Returns `true` if the rendered content of the given element intersects the supplied rectangle. Each candidate graphics element is to be considered a match only if the same graphics element can be a target of pointer events as defined in [pointer-events](/en-US/docs/Web/SVG/Reference/Attribute/pointer-events) processing.

[SVGSVGElement.checkEnclosure()](/en-US/docs/Web/API/SVGSVGElement/checkEnclosure)

Returns `true` if the rendered content of the given element is entirely contained within the supplied rectangle. Each candidate graphics element is to be considered a match only if the same graphics element can be a target of pointer events as defined in [pointer-events](/en-US/docs/Web/SVG/Reference/Attribute/pointer-events) processing.

[SVGSVGElement.deselectAll()](/en-US/docs/Web/API/SVGSVGElement/deselectAll)

Unselects any selected objects, including any selections of text strings and type-in bars.

[SVGSVGElement.createSVGNumber()](/en-US/docs/Web/API/SVGSVGElement/createSVGNumber)

Creates an [SVGNumber](/en-US/docs/Web/API/SVGNumber) object outside of any document trees. The object is initialized to `0`.

[SVGSVGElement.createSVGLength()](/en-US/docs/Web/API/SVGSVGElement/createSVGLength)

Creates an [SVGLength](/en-US/docs/Web/API/SVGLength) object outside of any document trees. The object is initialized to `0` user units.

[SVGSVGElement.createSVGAngle()](/en-US/docs/Web/API/SVGSVGElement/createSVGAngle)

Creates an [SVGAngle](/en-US/docs/Web/API/SVGAngle) object outside of any document trees. The object is initialized to a value of `0` degrees (unitless).

[SVGSVGElement.createSVGPoint()](/en-US/docs/Web/API/SVGSVGElement/createSVGPoint)

Creates a [DOMPoint](/en-US/docs/Web/API/DOMPoint) object outside of any document trees. The object is initialized to the point `(0,0)` in the user coordinate system.

[SVGSVGElement.createSVGMatrix()](/en-US/docs/Web/API/SVGSVGElement/createSVGMatrix)

Creates a [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) object outside of any document trees. The object is initialized to the identity matrix.

[SVGSVGElement.createSVGRect()](/en-US/docs/Web/API/SVGSVGElement/createSVGRect)

Creates an [SVGRect](/en-US/docs/Web/API/SVGRect) object outside of any document trees. The object is initialized such that all values are set to `0` user units.

[SVGSVGElement.createSVGTransform()](/en-US/docs/Web/API/SVGSVGElement/createSVGTransform)

Creates an [SVGTransform](/en-US/docs/Web/API/SVGTransform) object outside of any document trees. The object is initialized to an identity matrix transform (`SVG_TRANSFORM_MATRIX`).

[SVGSVGElement.createSVGTransformFromMatrix()](/en-US/docs/Web/API/SVGSVGElement/createSVGTransformFromMatrix)

Creates an [SVGTransform](/en-US/docs/Web/API/SVGTransform) object outside of any document trees. The object is initialized to the given matrix transform (i.e., `SVG_TRANSFORM_MATRIX`). The values from the parameter matrix are copied, the matrix parameter is not adopted as `SVGTransform::matrix`.

[SVGSVGElement.getElementById()](/en-US/docs/Web/API/SVGSVGElement/getElementById)

Searches this SVG document fragment (i.e., the search is restricted to a subset of the document tree) for an Element whose `id` is given by `elementId`. If an Element is found, that Element is returned. If no such element exists, returns `null`. Behavior is not defined if more than one element has this id.

## [Event handlers](#event_handlers)

The following [Window](/en-US/docs/Web/API/Window)`onXYZ` event handler properties are also available as aliases targeting the `window` object. However, it is advised to listen to them on the `window` object directly rather than on `SVGSVGElement`.

Note: Using `addEventListener()` on `SVGSVGElement` will not work for the `onXYZ` event handlers listed below. Listen to the events on the [window](/en-US/docs/Web/API/Window) object instead.

[SVGSVGElement.onafterprint](/en-US/docs/Web/API/Window/afterprint_event)

Fired after the associated document has started printing or the print preview has been closed.

[SVGSVGElement.onbeforeprint](/en-US/docs/Web/API/Window/beforeprint_event)

Fired when the associated document is about to be printed or previewed for printing.

[SVGSVGElement.onbeforeunload](/en-US/docs/Web/API/Window/beforeunload_event)

Fired when the window, the document and its resources are about to be unloaded.

[SVGSVGElement.ongamepadconnected](/en-US/docs/Web/API/Window/gamepadconnected_event)

Fired when the browser detects that a gamepad has been connected or the first time a button/axis of the gamepad is used.

[SVGSVGElement.ongamepaddisconnected](/en-US/docs/Web/API/Window/gamepaddisconnected_event)

Fired when the browser detects that a gamepad has been disconnected.

[SVGSVGElement.onhashchange](/en-US/docs/Web/API/Window/hashchange_event)

Fired when the fragment identifier of the URL has changed (the part of the URL beginning with and following the `#` symbol).

[SVGSVGElement.onlanguagechange](/en-US/docs/Web/API/Window/languagechange_event)

Fired when the user's preferred language changes.

[SVGSVGElement.onmessage](/en-US/docs/Web/API/Window/message_event)

Fired when the window receives a message, for example from a call to [Window.postMessage()](/en-US/docs/Web/API/Window/postMessage) from another browsing context.

[SVGSVGElement.onmessageerror](/en-US/docs/Web/API/Window/messageerror_event)

Fired when the window receives a message that can't be deserialized.

[SVGSVGElement.onoffline](/en-US/docs/Web/API/Window/offline_event)

Fired when the browser has lost access to the network and the value of [Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine) switches to `false`.

[SVGSVGElement.ononline](/en-US/docs/Web/API/Window/online_event)

Fired when the browser has gained access to the network and the value of [Navigator.onLine](/en-US/docs/Web/API/Navigator/onLine) switches to `true`.

[SVGSVGElement.onpagehide](/en-US/docs/Web/API/Window/pagehide_event)

Fired when the browser hides the current page in the process of presenting a different page from the session's history.

[SVGSVGElement.onpageshow](/en-US/docs/Web/API/Window/pageshow_event)

Fired when the browser displays the window's document due to navigation.

[SVGSVGElement.onpopstate](/en-US/docs/Web/API/Window/popstate_event)

Fired when the active history entry changes while the user navigates the session history.

[SVGSVGElement.onrejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)

Fired whenever a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected and the rejection has been handled.

[SVGSVGElement.onstorage](/en-US/docs/Web/API/Window/storage_event)

Fired when a storage area (`localStorage`) has been modified in the context of another document.

[SVGSVGElement.onunhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event)

Fired whenever a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected but the rejection was not handled.

[SVGSVGElement.onunload](/en-US/docs/Web/API/Window/unload_event)

Fired when the document is being unloaded.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGSVGElement](https://svgwg.org/svg2-draft/struct.html#InterfaceSVGSVGElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<circle>](/en-US/docs/Web/SVG/Reference/Element/circle)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGSVGElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgsvgelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGSVGElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgsvgelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGSVGElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgsvgelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2d19a88d0cc560f031a07585bf57f005fec02670%0A*+Document+last+modified%3A+2025-07-07T07%3A44%3A55.000Z%0A%0A%3C%2Fdetails%3E)
