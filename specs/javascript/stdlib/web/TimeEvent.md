# TimeEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTimeEvent&level=not)

The `TimeEvent` interface, a part of [SVG SMIL](/en-US/docs/Web/SVG/Guides/SVG_animation_with_SMIL) animation, provides specific contextual information associated with Time events.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

`TimeEvent.detail`Read only

A `long` that specifies some detail information about the Event, depending on the type of the event. For this event type, indicates the repeat number for the animation.

`TimeEvent.view`Read only

A [WindowProxy](/en-US/docs/Glossary/WindowProxy) that identifies the Window from which the event was generated.

## [Instance methods](#instance_methods)

`TimeEvent.initTimeEvent()`

Used to initialize the value of a TimeEvent created through the DocumentEvent interface. This method may only be called before the TimeEvent has been dispatched via the dispatchEvent method, though it may be called multiple times during that phase if necessary.

## [Specifications](#specifications)

Specification
[SVG Animations Level 2# InterfaceTimeEvent](https://svgwg.org/specs/animations/#InterfaceTimeEvent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TimeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/timeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTimeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftimeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTimeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftimeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46b0ecd3b5280fbff659d138e3a7eaaf0fd12a24%0A*+Document+last+modified%3A+2025-03-25T14%3A00%3A13.000Z%0A%0A%3C%2Fdetails%3E)
