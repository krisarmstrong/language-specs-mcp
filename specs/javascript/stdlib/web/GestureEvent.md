# GestureEvent

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `GestureEvent` is a proprietary interface specific to WebKit which gives information regarding multi-touch gestures. Events using this interface include [gesturestart](/en-US/docs/Web/API/Element/gesturestart_event), [gesturechange](/en-US/docs/Web/API/Element/gesturechange_event), and [gestureend](/en-US/docs/Web/API/Element/gestureend_event).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Gesture event types](#gesture_event_types)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties of its parents, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

`GestureEvent.rotation`Read onlyNon-standard

Change in rotation (in degrees) since the event's beginning. Positive values indicate clockwise rotation; negative values indicate counterclockwise rotation. Initial value: `0.0`.

`GestureEvent.scale`Read onlyNon-standard

Distance between two digits since the event's beginning. Expressed as a floating-point multiple of the initial distance between the digits at the beginning of the gesture. Values below 1.0 indicate an inward pinch (zoom out). Values above 1.0 indicate an outward unpinch (zoom in). Initial value: `1.0`.

## [Instance methods](#instance_methods)

This interface also inherits methods of its parents, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

`GestureEvent.initGestureEvent()`Non-standard

Initializes the value of a `GestureEvent`. If the event has already been dispatched, this method does nothing.

## [Gesture event types](#gesture_event_types)

- [gesturestart](/en-US/docs/Web/API/Element/gesturestart_event)
- [gesturechange](/en-US/docs/Web/API/Element/gesturechange_event)
- [gestureend](/en-US/docs/Web/API/Element/gestureend_event)

## [Specifications](#specifications)

Not part of any specification. Apple has [a description at the Safari Developer Library](https://developer.apple.com/documentation/webkitjs/gestureevent).

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GestureEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gestureevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGestureEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgestureevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGestureEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgestureevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
