# Force Touch events

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

Force Touch Events are a proprietary, Apple-specific feature which makes possible (where supported by the input hardware) new interactions based on how hard the user clicks or presses down on the touchscreen or trackpad.

## In this article

- [Events](#events)
- [Event properties](#event_properties)
- [Constants](#constants)
- [Specifications](#specifications)

## [Events](#events)

[webkitmouseforcewillbegin](/en-US/docs/Web/API/Element/webkitmouseforcewillbegin_event)Non-standard

This event is fired before the [mousedown](/en-US/docs/Web/API/Element/mousedown_event) event. Its main use is that it can be [default-prevented](/en-US/docs/Web/API/Event/preventDefault).

[webkitmouseforcedown](/en-US/docs/Web/API/Element/webkitmouseforcedown_event)Non-standard

This event is fired after the [mousedown](/en-US/docs/Web/API/Element/mousedown_event) event as soon as sufficient pressure has been applied for it to qualify as a "force click".

[webkitmouseforceup](/en-US/docs/Web/API/Element/webkitmouseforceup_event)Non-standard

This event is fired after the [webkitmouseforcedown](/en-US/docs/Web/API/Element/webkitmouseforcedown_event) event as soon as the pressure has been reduced sufficiently to end the "force click".

[webkitmouseforcechanged](/en-US/docs/Web/API/Element/webkitmouseforcechanged_event)Non-standard

This event is fired each time the amount of pressure changes. This event first fires after the [mousedown](/en-US/docs/Web/API/Element/mousedown_event) event and stops firing before the [mouseup](/en-US/docs/Web/API/Element/mouseup_event) event.

## [Event properties](#event_properties)

The following property is known to be available on the [webkitmouseforcewillbegin](/en-US/docs/Web/API/Element/webkitmouseforcewillbegin_event), [mousedown](/en-US/docs/Web/API/Element/mousedown_event), [webkitmouseforcechanged](/en-US/docs/Web/API/Element/webkitmouseforcechanged_event), [webkitmouseforcedown](/en-US/docs/Web/API/Element/webkitmouseforcedown_event), [webkitmouseforceup](/en-US/docs/Web/API/Element/webkitmouseforceup_event), [mousemove](/en-US/docs/Web/API/Element/mousemove_event), and [mouseup](/en-US/docs/Web/API/Element/mouseup_event) event objects:

[MouseEvent.webkitForce](/en-US/docs/Web/API/MouseEvent/webkitForce)Non-standardRead only

The amount of pressure currently being applied to the trackpad/touchscreen.

## [Constants](#constants)

These constants are useful for determining the relative intensity of the pressure indicated by [MouseEvent.webkitForce](/en-US/docs/Web/API/MouseEvent/webkitForce):

[MouseEvent.WEBKIT_FORCE_AT_MOUSE_DOWN](/en-US/docs/Web/API/MouseEvent/WEBKIT_FORCE_AT_MOUSE_DOWN_static)Non-standardRead only

Minimum force necessary for a normal click.

[MouseEvent.WEBKIT_FORCE_AT_FORCE_MOUSE_DOWN](/en-US/docs/Web/API/MouseEvent/WEBKIT_FORCE_AT_FORCE_MOUSE_DOWN_static)Non-standardRead only

Minimum force necessary for a force click.

## [Specifications](#specifications)

Not part of any specification. Apple has [a description at the Mac Developer Library](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/RespondingtoForceTouchEventsfromJavaScript.html).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Force_Touch_events/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/force_touch_events/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FForce_Touch_events&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fforce_touch_events%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FForce_Touch_events%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fforce_touch_events%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7972ac25580ffbfb160e6d40013bbab3013d7cbe%0A*+Document+last+modified%3A+2024-08-12T07%3A02%3A43.000Z%0A%0A%3C%2Fdetails%3E)
