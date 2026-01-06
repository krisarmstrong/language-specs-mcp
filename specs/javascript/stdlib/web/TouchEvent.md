# TouchEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouchEvent&level=not)

The `TouchEvent` interface represents an [UIEvent](/en-US/docs/Web/API/UIEvent) which is sent when the state of contacts with a touch-sensitive surface changes. This surface can be a touch screen or trackpad, for example. The event can describe one or more points of contact with the screen and includes support for detecting movement, addition and removal of contact points, and so forth.

Touches are represented by the [Touch](/en-US/docs/Web/API/Touch) object; each touch is described by a position, size and shape, amount of pressure, and target element. Lists of touches are represented by [TouchList](/en-US/docs/Web/API/TouchList) objects.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Touch event types](#touch_event_types)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TouchEvent()](/en-US/docs/Web/API/TouchEvent/TouchEvent)

Creates a `TouchEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

[TouchEvent.altKey](/en-US/docs/Web/API/TouchEvent/altKey)Read only

A Boolean value indicating whether or not the alt key was down when the touch event was fired.

[TouchEvent.changedTouches](/en-US/docs/Web/API/TouchEvent/changedTouches)Read only

A [TouchList](/en-US/docs/Web/API/TouchList) of all the [Touch](/en-US/docs/Web/API/Touch) objects representing individual points of contact whose states changed between the previous touch event and this one.

[TouchEvent.ctrlKey](/en-US/docs/Web/API/TouchEvent/ctrlKey)Read only

A Boolean value indicating whether or not the control key was down when the touch event was fired.

[TouchEvent.metaKey](/en-US/docs/Web/API/TouchEvent/metaKey)Read only

A Boolean value indicating whether or not the meta key was down when the touch event was fired.

[TouchEvent.shiftKey](/en-US/docs/Web/API/TouchEvent/shiftKey)Read only

A Boolean value indicating whether or not the shift key was down when the touch event was fired.

[TouchEvent.targetTouches](/en-US/docs/Web/API/TouchEvent/targetTouches)Read only

A [TouchList](/en-US/docs/Web/API/TouchList) of all the [Touch](/en-US/docs/Web/API/Touch) objects that are both currently in contact with the touch surface and were also started on the same element that is the target of the event.

[TouchEvent.touches](/en-US/docs/Web/API/TouchEvent/touches)Read only

A [TouchList](/en-US/docs/Web/API/TouchList) of all the [Touch](/en-US/docs/Web/API/Touch) objects representing all current points of contact with the surface, regardless of target or changed status.

`TouchEvent.rotation`Non-standardRead only

Change in rotation (in degrees) since the event's beginning. Positive values indicate clockwise rotation; negative values indicate counterclockwise rotation. Initial value: `0.0`.

`TouchEvent.scale`Non-standardRead only

Distance between two digits since the event's beginning. Expressed as a floating-point multiple of the initial distance between the digits at the beginning of the event. Values below 1.0 indicate an inward pinch (zoom out). Values above 1.0 indicate an outward unpinch (zoom in). Initial value: `1.0`.

## [Touch event types](#touch_event_types)

There are several types of event that can be fired to indicate that touch-related changes have occurred. You can determine which of these has happened by looking at the event's [TouchEvent.type](/en-US/docs/Web/API/Event/type) property.

[touchstart](/en-US/docs/Web/API/Element/touchstart_event)

Sent when the user places a touch point on the touch surface. The event's target will be the [element](/en-US/docs/Web/API/Element) in which the touch occurred.

[touchend](/en-US/docs/Web/API/Element/touchend_event)

Sent when the user removes a touch point from the surface; that is, when they lift a finger or stylus from the surface. This is also sent if the touch point moves off the edge of the surface; for example, if the user's finger slides off the edge of the screen.

The event's target is the same [element](/en-US/docs/Web/API/Element) that received the `touchstart` event corresponding to the touch point, even if the touch point has moved outside that element.

The touch point (or points) that were removed from the surface can be found in the [TouchList](/en-US/docs/Web/API/TouchList) specified by the `changedTouches` attribute.

[touchmove](/en-US/docs/Web/API/Element/touchmove_event)

Sent when the user moves a touch point along the surface. The event's target is the same [element](/en-US/docs/Web/API/Element) that received the `touchstart` event corresponding to the touch point, even if the touch point has moved outside that element.

This event is also sent if the values of the radius, rotation angle, or force attributes of a touch point change.

Note: The rate at which `touchmove` events is sent is browser-specific, and may also vary depending on the capability of the user's hardware. You must not rely on a specific granularity of these events.

[touchcancel](/en-US/docs/Web/API/Element/touchcancel_event)

Sent when a touch point has been disrupted in some way. There are several possible reasons why this might happen (and the exact reasons will vary from device to device, as well as browser to browser):

- An event of some kind occurred that canceled the touch; this might happen if a modal alert pops up during the interaction.
- The touch point has left the document window and moved into the browser's UI area, a plug-in, or other external content.
- The user has placed more touch points on the screen than can be supported, in which case the earliest [Touch](/en-US/docs/Web/API/Touch) in the [TouchList](/en-US/docs/Web/API/TouchList) gets canceled.

### [Using with addEventListener() and preventDefault()](#using_with_addeventlistener_and_preventdefault)

It's important to note that in many cases, both touch and mouse events get sent (in order to let non-touch-specific code still interact with the user). If you use touch events, you should call [preventDefault()](/en-US/docs/Web/API/Event/preventDefault) to keep the mouse event from being sent as well.

The exception to this is Chrome, starting with version 56 (desktop, Chrome for Android, and Android webview), where the default value for the `passive` option for [touchstart](/en-US/docs/Web/API/Element/touchstart_event) and [touchmove](/en-US/docs/Web/API/Element/touchmove_event) is `true` and calls to [preventDefault()](/en-US/docs/Web/API/Event/preventDefault) will have no effect. To override this behavior, you need to set the `passive` option to `false`, after which calling [preventDefault()](/en-US/docs/Web/API/Event/preventDefault) will work as specified. The change to treat listeners as `passive` by default prevents the listener from blocking page rendering while a user is scrolling. A demo is available on the [Chrome Developer](https://developer.chrome.com/blog/passive-event-listeners/) site.

## [Example](#example)

See the [example on the main Touch events article](/en-US/docs/Web/API/Touch_events#examples).

## [Specifications](#specifications)

Specification
[Touch Events# touchevent-interface](https://w3c.github.io/touch-events/#touchevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Touch events](/en-US/docs/Web/API/Touch_events)
- [GestureEvent](/en-US/docs/Web/API/GestureEvent)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TouchEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/touchevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouchEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftouchevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTouchEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftouchevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F36761819df2ebdd4e3dcc9ae6007029dec71fac0%0A*+Document+last+modified%3A+2025-10-21T22%3A19%3A42.000Z%0A%0A%3C%2Fdetails%3E)
