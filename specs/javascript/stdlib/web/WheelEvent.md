# WheelEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWheelEvent&level=high)

The `WheelEvent` interface represents events that occur due to the user moving a mouse wheel or similar input device.

Note: This is the standard wheel event interface to use. Old versions of browsers implemented the non-standard and non-cross-browser-compatible `MouseWheelEvent` and [MouseScrollEvent](/en-US/docs/Web/API/MouseScrollEvent) interfaces. Use this interface and avoid the non-standard ones.

Don't confuse the `wheel` event with the [scroll](/en-US/docs/Web/API/Element/scroll_event) event:

- A `wheel` event doesn't necessarily dispatch a `scroll` event. For example, the element may be unscrollable at all. Zooming actions using the wheel or trackpad also fire `wheel` events.
- A `scroll` event isn't necessarily triggered by a `wheel` event. Elements can also be scrolled by using the keyboard, dragging a scrollbar, or using JavaScript.
- Even when the `wheel` event does trigger scrolling, the `delta*` values in the `wheel` event don't necessarily reflect the content's scrolling direction.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WheelEvent()](/en-US/docs/Web/API/WheelEvent/WheelEvent)

Creates a `WheelEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its ancestors, [MouseEvent](/en-US/docs/Web/API/MouseEvent), [UIEvent](/en-US/docs/Web/API/UIEvent), and [Event](/en-US/docs/Web/API/Event).

[WheelEvent.deltaX](/en-US/docs/Web/API/WheelEvent/deltaX)Read only

Returns a `double` representing the horizontal scroll amount.

[WheelEvent.deltaY](/en-US/docs/Web/API/WheelEvent/deltaY)Read only

Returns a `double` representing the vertical scroll amount.

[WheelEvent.deltaZ](/en-US/docs/Web/API/WheelEvent/deltaZ)Read only

Returns a `double` representing the scroll amount for the z-axis.

[WheelEvent.deltaMode](/en-US/docs/Web/API/WheelEvent/deltaMode)Read only

Returns an `unsigned long` representing the unit of the `delta*` values' scroll amount.

`WheelEvent.wheelDelta`Read onlyDeprecatedNon-standard

Returns an integer (32-bit) representing the distance in pixels.

`WheelEvent.wheelDeltaX`Read onlyDeprecatedNon-standard

Returns an integer representing the horizontal scroll amount.

`WheelEvent.wheelDeltaY`Read onlyDeprecatedNon-standard

Returns an integer representing the vertical scroll amount.

Note:[Element: mousewheel event](/en-US/docs/Web/API/Element/mousewheel_event) has additional documentation about the deprecated properties `wheelDelta`, `wheelDeltaX`, `wheelDeltaY`.

## [Instance methods](#instance_methods)

This interface doesn't define any specific methods, but inherits methods from its ancestors, [MouseEvent](/en-US/docs/Web/API/MouseEvent), [UIEvent](/en-US/docs/Web/API/UIEvent), and [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[UI Events# interface-wheelevent](https://w3c.github.io/uievents/#interface-wheelevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [wheel](/en-US/docs/Web/API/Element/wheel_event) event
- Interfaces replaced by this one: 

  - Gecko's legacy mouse wheel event object: [MouseScrollEvent](/en-US/docs/Web/API/MouseScrollEvent)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WheelEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/wheelevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWheelEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwheelevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWheelEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwheelevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
