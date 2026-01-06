# InputEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputEvent&level=high)

The `InputEvent` interface represents an event notifying the user of editable content changes.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[InputEvent()](/en-US/docs/Web/API/InputEvent/InputEvent)

Creates an `InputEvent` object.

## [Instance properties](#instance_properties)

This interface inherits properties from its parents, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

[InputEvent.data](/en-US/docs/Web/API/InputEvent/data)Read only

Returns a string with the inserted characters. This may be an empty string if the change doesn't insert text (for example, when deleting characters).

[InputEvent.dataTransfer](/en-US/docs/Web/API/InputEvent/dataTransfer)Read only

Returns a [DataTransfer](/en-US/docs/Web/API/DataTransfer) object containing information about richtext or plaintext data being added to or removed from editable content.

[InputEvent.inputType](/en-US/docs/Web/API/InputEvent/inputType)Read only

Returns the type of change for editable content such as, for example, inserting, deleting, or formatting text.

[InputEvent.isComposing](/en-US/docs/Web/API/InputEvent/isComposing)Read only

Returns a [Boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) value indicating if the event is fired after [compositionstart](/en-US/docs/Web/API/Element/compositionstart_event) and before [compositionend](/en-US/docs/Web/API/Element/compositionend_event).

## [Instance methods](#instance_methods)

This interface inherits methods from its parents, [UIEvent](/en-US/docs/Web/API/UIEvent) and [Event](/en-US/docs/Web/API/Event).

[InputEvent.getTargetRanges()](/en-US/docs/Web/API/InputEvent/getTargetRanges)

Returns an array of [StaticRange](/en-US/docs/Web/API/StaticRange) objects that will be affected by a change to the DOM if the input event is not canceled.

## [Specifications](#specifications)

Specification
[Input Events Level 2# interface-InputEvent](https://w3c.github.io/input-events/#interface-InputEvent)
[UI Events# interface-inputevent](https://w3c.github.io/uievents/#interface-inputevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [beforeinput event](/en-US/docs/Web/API/Element/beforeinput_event)
- [input event](/en-US/docs/Web/API/Element/input_event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 20, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/InputEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/inputevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finputevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finputevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ca15ba7933a738cf632a9bbf5cfd4e90d1a97b1%0A*+Document+last+modified%3A+2024-03-20T10%3A52%3A35.000Z%0A%0A%3C%2Fdetails%3E)
