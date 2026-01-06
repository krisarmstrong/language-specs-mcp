# TextUpdateEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextUpdateEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `TextUpdateEvent` interface is a [DOM event](/en-US/docs/Web/API/Event) that represents a text or selection update in an editable text region that's attached to an [EditContext](/en-US/docs/Web/API/EditContext) instance.

This interface inherits properties from [Event](/en-US/docs/Web/API/Event).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[TextUpdateEvent()](/en-US/docs/Web/API/TextUpdateEvent/TextUpdateEvent)Experimental

Creates a new `TextUpdateEvent` object.

## [Instance properties](#instance_properties)

[TextUpdateEvent.updateRangeStart](/en-US/docs/Web/API/TextUpdateEvent/updateRangeStart)Read onlyExperimental

Returns the index of the first character in the range of text that was updated.

[TextUpdateEvent.updateRangeEnd](/en-US/docs/Web/API/TextUpdateEvent/updateRangeEnd)Read onlyExperimental

Returns the index of the last character in the range of text that was updated.

[TextUpdateEvent.text](/en-US/docs/Web/API/TextUpdateEvent/text)Read onlyExperimental

Returns the text that was inserted in the updated range.

[TextUpdateEvent.selectionStart](/en-US/docs/Web/API/TextUpdateEvent/selectionStart)Read onlyExperimental

Returns the index of the first character in the new selection range, after the update.

[TextUpdateEvent.selectionEnd](/en-US/docs/Web/API/TextUpdateEvent/selectionEnd)Read onlyExperimental

Returns the index of the last character in the new selection range, after the update.

## [Examples](#examples)

### [Rendering the updated text in an editable canvas](#rendering_the_updated_text_in_an_editable_canvas)

In the following example, the EditContext API is used to render editable text in a `<canvas>` element, and the `textupdate` event is used to render the text when the user is typing.

html

```
<canvas id="editor-canvas"></canvas>
```

js

```
const canvas = document.getElementById("editor-canvas");
const ctx = canvas.getContext("2d");
const editContext = new EditContext();
canvas.editContext = editContext;

function render() {
  // Clear the canvas.
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Render the text.
  ctx.fillText(editContext.text, 10, 10);
}

editContext.addEventListener("textupdate", (e) => {
  // Re-render the editor view when the user is entering text.
  render();

  console.log(
    `The user entered ${e.text}. Rendering the entire text: ${editContext.text}`,
  );
});
```

## [Specifications](#specifications)

Specification
[EditContext API# dom-textupdateevent](https://w3c.github.io/edit-context/#dom-textupdateevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TextUpdateEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textupdateevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextUpdateEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextupdateevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextUpdateEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextupdateevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc29cee3dcb0d0e66093dd0c18aa82e0eab9d6d14%0A*+Document+last+modified%3A+2024-07-26T15%3A08%3A29.000Z%0A%0A%3C%2Fdetails%3E)
