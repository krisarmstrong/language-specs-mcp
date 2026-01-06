# UIEvent

The `UIEvent` interface represents simple user interface events. It is part of the [UI Events](/en-US/docs/Web/API/UI_Events) API, which includes various event types and interfaces related to user interactions.

`UIEvent` derives from [Event](/en-US/docs/Web/API/Event). Although the [UIEvent.initUIEvent()](/en-US/docs/Web/API/UIEvent/initUIEvent) method is kept for backward compatibility, you should create a `UIEvent` object using the [UIEvent()](/en-US/docs/Web/API/UIEvent/UIEvent) constructor.

Several interfaces are direct or indirect descendants of this one: [MouseEvent](/en-US/docs/Web/API/MouseEvent), [TouchEvent](/en-US/docs/Web/API/TouchEvent), [FocusEvent](/en-US/docs/Web/API/FocusEvent), [KeyboardEvent](/en-US/docs/Web/API/KeyboardEvent), [WheelEvent](/en-US/docs/Web/API/WheelEvent), [InputEvent](/en-US/docs/Web/API/InputEvent), and [CompositionEvent](/en-US/docs/Web/API/CompositionEvent).

## In this article

- [Constructors](#constructors)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructors](#constructors)

[UIEvent()](/en-US/docs/Web/API/UIEvent/UIEvent)

Creates a `UIEvent` object.

## [Instance properties](#instance_properties)

This interface also inherits properties of its parent, [Event](/en-US/docs/Web/API/Event).

[UIEvent.detail](/en-US/docs/Web/API/UIEvent/detail)Read only

Returns a `long` with details about the event, depending on the event type.

[UIEvent.sourceCapabilities](/en-US/docs/Web/API/UIEvent/sourceCapabilities)ExperimentalRead only

Returns an instance of the `InputDeviceCapabilities` interface, which provides information about the physical device responsible for generating a touch event.

[UIEvent.view](/en-US/docs/Web/API/UIEvent/view)Read only

Returns a [WindowProxy](/en-US/docs/Glossary/WindowProxy) that contains the view that generated the event.

[UIEvent.which](/en-US/docs/Web/API/UIEvent/which)DeprecatedRead only

Returns the numeric `keyCode` of the key pressed, or the character code (`charCode`) for an alphanumeric key pressed.

## [Instance methods](#instance_methods)

This interface also inherits methods of its parent, [Event](/en-US/docs/Web/API/Event).

[UIEvent.initUIEvent()](/en-US/docs/Web/API/UIEvent/initUIEvent)Deprecated

Initializes a `UIEvent` object. If the event has already been dispatched, this method does nothing.

## [Specifications](#specifications)

Specification
[UI Events# idl-uievent](https://w3c.github.io/uievents/#idl-uievent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [UI Events API](/en-US/docs/Web/API/UI_Events)
- [Introduction to events](/en-US/docs/Learn_web_development/Core/Scripting/Events)
- [Event](/en-US/docs/Web/API/Event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/UIEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/uievent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUIEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fuievent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FUIEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fuievent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F63d0c539650bee867018575bb45c14114f154997%0A*+Document+last+modified%3A+2025-02-09T16%3A34%3A06.000Z%0A%0A%3C%2Fdetails%3E)
