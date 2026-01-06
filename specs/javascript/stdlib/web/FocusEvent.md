# FocusEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFocusEvent&level=high)

The `FocusEvent` interface represents focus-related events, including [focus](/en-US/docs/Web/API/Element/focus_event), [blur](/en-US/docs/Web/API/Element/blur_event), [focusin](/en-US/docs/Web/API/Element/focusin_event), and [focusout](/en-US/docs/Web/API/Element/focusout_event).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Order of events](#order_of_events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FocusEvent()](/en-US/docs/Web/API/FocusEvent/FocusEvent)

Creates a `FocusEvent` event with the given parameters.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent [UIEvent](/en-US/docs/Web/API/UIEvent), and indirectly from [Event](/en-US/docs/Web/API/Event).

[FocusEvent.relatedTarget](/en-US/docs/Web/API/FocusEvent/relatedTarget)

An [EventTarget](/en-US/docs/Web/API/EventTarget) representing a secondary target for this event. In some cases (such as when tabbing in or out a page), this property may be set to `null` for security reasons.

## [Instance methods](#instance_methods)

This interface has no specific methods. It inherits methods from its parent [UIEvent](/en-US/docs/Web/API/UIEvent), and indirectly from [Event](/en-US/docs/Web/API/Event).

## [Order of events](#order_of_events)

When focus is shifted from element A to element B, focus events are dispatched in the following order:

1. `blur`: sent after element A loses focus.
2. `focusout`: sent after the `blur` event.
3. `focus`: sent after element B receives focus.
4. `focusin`: sent after the `focus` event.

## [Specifications](#specifications)

Specification
[UI Events# interface-focusevent](https://w3c.github.io/uievents/#interface-focusevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Event](/en-US/docs/Web/API/Event) base interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 1, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/FocusEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/focusevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFocusEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ffocusevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFocusEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ffocusevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc45b0cf22b34da74660e7ca95140eff5ab2577d5%0A*+Document+last+modified%3A+2023-09-01T06%3A18%3A26.000Z%0A%0A%3C%2Fdetails%3E)
