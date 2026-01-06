# PointerEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPointerEvent&level=high)

The `PointerEvent` interface represents the state of a DOM event produced by a pointer such as the geometry of the contact point, the device type that generated the event, the amount of pressure that was applied on the contact surface, etc.

A pointer is a hardware agnostic representation of input devices (such as a mouse, pen or contact point on a touch-enable surface). The pointer can target a specific coordinate (or set of coordinates) on the contact surface such as a screen.

A pointer's hit test is the process a browser uses to determine the target element for a pointer event. Typically, this is determined by considering the pointer's location and also the visual layout of elements in a document on screen media.

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Pointer event types](#pointer_event_types)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[PointerEvent()](/en-US/docs/Web/API/PointerEvent/PointerEvent)

Creates a synthetic—and untrusted—`PointerEvent`.

## [Instance properties](#instance_properties)

This interface inherits properties from [MouseEvent](/en-US/docs/Web/API/MouseEvent) and [Event](/en-US/docs/Web/API/Event).

[PointerEvent.altitudeAngle](/en-US/docs/Web/API/PointerEvent/altitudeAngle)Read only

Represents the angle between a transducer (a pointer or stylus) axis and the X-Y plane of a device screen.

[PointerEvent.azimuthAngle](/en-US/docs/Web/API/PointerEvent/azimuthAngle)Read only

Represents the angle between the Y-Z plane and the plane containing both the transducer (a pointer or stylus) axis and the Y axis.

[PointerEvent.persistentDeviceId](/en-US/docs/Web/API/PointerEvent/persistentDeviceId)Read only

A unique identifier for the pointing device generating the `PointerEvent`.

[PointerEvent.pointerId](/en-US/docs/Web/API/PointerEvent/pointerId)Read only

A unique identifier for the pointer causing the event.

[PointerEvent.width](/en-US/docs/Web/API/PointerEvent/width)Read only

The width (magnitude on the X axis), in CSS pixels, of the contact geometry of the pointer.

[PointerEvent.height](/en-US/docs/Web/API/PointerEvent/height)Read only

The height (magnitude on the Y axis), in CSS pixels, of the contact geometry of the pointer.

[PointerEvent.pressure](/en-US/docs/Web/API/PointerEvent/pressure)Read only

The normalized pressure of the pointer input in the range `0` to `1`, where `0` and `1` represent the minimum and maximum pressure the hardware is capable of detecting, respectively.

[PointerEvent.tangentialPressure](/en-US/docs/Web/API/PointerEvent/tangentialPressure)Read only

The normalized tangential pressure of the pointer input (also known as barrel pressure or [cylinder stress](https://en.wikipedia.org/wiki/Cylinder_stress)) in the range `-1` to `1`, where `0` is the neutral position of the control.

[PointerEvent.tiltX](/en-US/docs/Web/API/PointerEvent/tiltX)Read only

The plane angle (in degrees, in the range of `-90` to `90`) between the Y–Z plane and the plane containing both the pointer (e.g., pen stylus) axis and the Y axis.

[PointerEvent.tiltY](/en-US/docs/Web/API/PointerEvent/tiltY)Read only

The plane angle (in degrees, in the range of `-90` to `90`) between the X–Z plane and the plane containing both the pointer (e.g., pen stylus) axis and the X axis.

[PointerEvent.twist](/en-US/docs/Web/API/PointerEvent/twist)Read only

The clockwise rotation of the pointer (e.g., pen stylus) around its major axis in degrees, with a value in the range `0` to `359`.

[PointerEvent.pointerType](/en-US/docs/Web/API/PointerEvent/pointerType)Read only

Indicates the device type that caused the event (mouse, pen, touch, etc.).

[PointerEvent.isPrimary](/en-US/docs/Web/API/PointerEvent/isPrimary)Read only

Indicates if the pointer represents the primary pointer of this pointer type.

## [Instance methods](#instance_methods)

[PointerEvent.getCoalescedEvents()](/en-US/docs/Web/API/PointerEvent/getCoalescedEvents)Secure context

Returns a sequence of all `PointerEvent` instances that were coalesced into the dispatched [pointermove](/en-US/docs/Web/API/Element/pointermove_event) event.

[PointerEvent.getPredictedEvents()](/en-US/docs/Web/API/PointerEvent/getPredictedEvents)

Returns a sequence of `PointerEvent` instances that the browser predicts will follow the dispatched [pointermove](/en-US/docs/Web/API/Element/pointermove_event) event's coalesced events.

## [Pointer event types](#pointer_event_types)

The `PointerEvent` interface has several event types. To determine which event fired, look at the event's [type](/en-US/docs/Web/API/Event/type) property.

Note: It's important to note that in many cases, both pointer and mouse events get sent (in order to let non-pointer-specific code still interact with the user). If you use pointer events, you should call [preventDefault()](/en-US/docs/Web/API/Event/preventDefault) to keep the mouse event from being sent as well.

[pointerover](/en-US/docs/Web/API/Element/pointerover_event)

This event is fired when a pointing device is moved into an element's hit test boundaries.

[pointerenter](/en-US/docs/Web/API/Element/pointerenter_event)

This event is fired when a pointing device is moved into the hit test boundaries of an element or one of its descendants, including as a result of a `pointerdown` event from a device that does not support hover (see `pointerdown`). This event type is similar to `pointerover`, but differs in that it does not bubble.

[pointerdown](/en-US/docs/Web/API/Element/pointerdown_event)

The event is fired when a pointer becomes active. For mouse, it is fired when the device transitions from no buttons pressed to at least one button pressed. For touch, it is fired when physical contact is made with the digitizer. For pen, it is fired when the stylus makes physical contact with the digitizer.

Note: For touchscreen browsers that allow [direct manipulation](https://w3c.github.io/pointerevents/#dfn-direct-manipulation), a `pointerdown` event triggers [implicit pointer capture](https://w3c.github.io/pointerevents/#dfn-implicit-pointer-capture), which causes the target to capture all subsequent pointer events as if they were occurring over the capturing target. Accordingly, `pointerover`, `pointerenter`, `pointerleave`, and `pointerout`will not fire as long as this capture is set. The capture can be released manually by calling [element.releasePointerCapture](/en-US/docs/Web/API/Element/releasePointerCapture) on the target element, or it will be implicitly released after a `pointerup` or `pointercancel` event.

[pointermove](/en-US/docs/Web/API/Element/pointermove_event)

This event is fired when a pointer changes coordinates.

[pointerrawupdate](/en-US/docs/Web/API/Element/pointerrawupdate_event)Experimental

This event is fired when any of a pointer's properties change.

[pointerup](/en-US/docs/Web/API/Element/pointerup_event)

This event is fired when a pointer is no longer active.

[pointercancel](/en-US/docs/Web/API/Element/pointercancel_event)

A browser fires this event if it concludes the pointer will no longer be able to generate events (for example the related device is deactivated).

[pointerout](/en-US/docs/Web/API/Element/pointerout_event)

This event is fired for several reasons including: pointing device is moved out of the hit test boundaries of an element; firing the `pointerup` event for a device that does not support hover (see `pointerup`); after firing the `pointercancel` event (see `pointercancel`); when a pen stylus leaves the hover range detectable by the digitizer.

[pointerleave](/en-US/docs/Web/API/Element/pointerleave_event)

This event is fired when a pointing device is moved out of the hit test boundaries of an element. For pen devices, this event is fired when the stylus leaves the hover range detectable by the digitizer.

[gotpointercapture](/en-US/docs/Web/API/Element/gotpointercapture_event)

This event is fired when an element receives pointer capture.

[lostpointercapture](/en-US/docs/Web/API/Element/lostpointercapture_event)

This event is fired after pointer capture is released for a pointer.

## [Example](#example)

Examples of each property, event type, and global event handler are included in their respective reference pages.

## [Specifications](#specifications)

Specification
[Pointer Events# pointerevent-interface](https://w3c.github.io/pointerevents/#pointerevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Touch events](/en-US/docs/Web/API/Touch_events)
- [GestureEvent](/en-US/docs/Web/API/GestureEvent)
- [touch-action](/en-US/docs/Web/CSS/Reference/Properties/touch-action)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PointerEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pointerevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPointerEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpointerevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPointerEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpointerevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbec7ef59277e752985de0ee963c86f6e8e4b3400%0A*+Document+last+modified%3A+2025-06-25T18%3A43%3A22.000Z%0A%0A%3C%2Fdetails%3E)
