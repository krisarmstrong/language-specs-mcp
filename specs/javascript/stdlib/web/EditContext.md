# EditContext

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEditContext&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `EditContext` interface represents the text edit context of an element that was made editable by using the [EditContext API](/en-US/docs/Web/API/EditContext_API).

The [EditContext API](/en-US/docs/Web/API/EditContext_API) can be used to build rich text editors on the web that support advanced text input experiences, such as [Input Method Editor](/en-US/docs/Glossary/Input_method_editor) (IME) composition, emoji picker, or any other platform-specific editing-related UI surfaces.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[EditContext()](/en-US/docs/Web/API/EditContext/EditContext)Experimental

Returns a new `EditContext` instance.

## [Instance properties](#instance_properties)

[EditContext.text](/en-US/docs/Web/API/EditContext/text)Read onlyExperimental

The editable content of the element.

[EditContext.selectionStart](/en-US/docs/Web/API/EditContext/selectionStart)Read onlyExperimental

The offset, within the editable text content, of the start of the current selection.

[EditContext.selectionEnd](/en-US/docs/Web/API/EditContext/selectionEnd)Read onlyExperimental

The offset, within the editable text content, of the end of the current selection.

[EditContext.characterBoundsRangeStart](/en-US/docs/Web/API/EditContext/characterBoundsRangeStart)Read onlyExperimental

The offset, within the editable text content, where the last IME composition started.

## [Instance methods](#instance_methods)

`EditContext` is based on the [EventTarget](/en-US/docs/Web/API/EventTarget) interface, and includes its methods.

[EditContext.attachedElements()](/en-US/docs/Web/API/EditContext/attachedElements)Experimental

An [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) containing one [HTMLElement](/en-US/docs/Web/API/HTMLElement) object which is the element that's associated with the `EditContext` object.

[EditContext.characterBounds()](/en-US/docs/Web/API/EditContext/characterBounds)Experimental

The list of bounding rectangles for the characters in the `EditContext` object.

[EditContext.updateText()](/en-US/docs/Web/API/EditContext/updateText)Experimental

Updates the internal text content of the `EditContext` object.

[EditContext.updateSelection()](/en-US/docs/Web/API/EditContext/updateSelection)Experimental

Updates the internal state of the selection within the editable text context.

[EditContext.updateControlBounds()](/en-US/docs/Web/API/EditContext/updateControlBounds)Experimental

Informs the operating system about the position and size of the editable text region.

[EditContext.updateSelectionBounds()](/en-US/docs/Web/API/EditContext/updateSelectionBounds)Experimental

Informs the operating system about the position and size of the selection within the editable text region.

[EditContext.updateCharacterBounds()](/en-US/docs/Web/API/EditContext/updateCharacterBounds)Experimental

Informs the operating system about the position and size of the characters in the `EditContext` object.

## [Events](#events)

[textupdate](/en-US/docs/Web/API/EditContext/textupdate_event)Experimental

Fired when the user has made changes to the text or selection.

[textformatupdate](/en-US/docs/Web/API/EditContext/textformatupdate_event)Experimental

Fired when composition using an [Input Method Editor](/en-US/docs/Glossary/Input_method_editor) (IME) window is happening and the IME decides that certain parts of the text being composed should be formatted differently to indicate the composition state.

[characterboundsupdate](/en-US/docs/Web/API/EditContext/characterboundsupdate_event)Experimental

Fired when the operating system needs to know the size and position of certain characters within the editable text region of the `EditContext` object, in order to display an IME window.

[compositionstart](/en-US/docs/Web/API/EditContext/compositionstart_event)Experimental

Fired when composition using an IME window is starting.

[compositionend](/en-US/docs/Web/API/EditContext/compositionend_event)Experimental

Fired when composition using an IME window is ending.

## [Specifications](#specifications)

Specification
[EditContext API# dom-editcontext](https://w3c.github.io/edit-context/#dom-editcontext)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 21, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/EditContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/editcontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEditContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feditcontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEditContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feditcontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa6f2a5b313727d983c369dec91c4c7418b1b4f74%0A*+Document+last+modified%3A+2024-01-21T00%3A40%3A30.000Z%0A%0A%3C%2Fdetails%3E)
