# TextFormatUpdateEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextFormatUpdateEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `TextFormatUpdateEvent` interface is a [DOM event](/en-US/docs/Web/API/Event) that represents a list of text formats that an [Input Method Editor](/en-US/docs/Glossary/Input_method_editor) (IME) window wants to apply to the text being composed in an editable region that's attached to an [EditContext](/en-US/docs/Web/API/EditContext) instance.

This interface inherits properties from [Event](/en-US/docs/Web/API/Event).

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[TextFormatUpdateEvent()](/en-US/docs/Web/API/TextFormatUpdateEvent/TextFormatUpdateEvent)Experimental

Creates a new `TextFormatUpdateEvent` object.

## [Instance methods](#instance_methods)

[TextFormatUpdateEvent.getTextFormats](/en-US/docs/Web/API/TextFormatUpdateEvent/getTextFormats)Experimental

Returns an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of [TextFormat](/en-US/docs/Web/API/TextFormat) objects that represent the formats that the IME window wants to apply to the text.

## [Examples](#examples)

### [Styling IME-composed text](#styling_ime-composed_text)

In the following example, the `textformatupdate` event is used to update the formatting of the text in the editable region.

html

```
<canvas id="editor-canvas"></canvas>
```

js

```
const TEXT_X = 10;
const TEXT_Y = 10;

const canvas = document.getElementById("editor-canvas");
const ctx = canvas.getContext("2d");

const editContext = new EditContext();
canvas.editContext = editContext;

editContext.addEventListener("textformatupdate", (e) => {
  // Clear the canvas.
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Render the text.
  ctx.fillText(editContext.text, TEXT_X, TEXT_Y);
  console.log(`Rendering text: ${editContext.text}`);

  // Get the text formats that the IME window wants to apply.
  const formats = e.getTextFormats();

  // Iterate over the text formats
  for (const format of formats) {
    const { rangeStart, rangeEnd, underlineStyle, underlineThickness } = format;

    console.log(
      `Applying underline ${underlineThickness} ${underlineStyle} between ${rangeStart} and ${rangeEnd}.`,
    );

    const underlineXStart = ctx.measureText(
      editContext.text.substring(0, rangeStart),
    ).width;
    const underlineXEnd = ctx.measureText(
      editContext.text.substring(0, rangeEnd),
    ).width;
    const underlineY = TEXT_Y + 3;

    // For brevity, this example only draws a simple underline.
    // Use underlineStyle and underlineThickness to draw the correct underline.

    ctx.beginPath();
    ctx.moveTo(TEXT_X + underlineXStart, underlineY);
    ctx.lineTo(TEXT_X + underlineXEnd, underlineY);
    ctx.stroke();
  }
});
```

## [Specifications](#specifications)

Specification
[EditContext API# dom-textformatupdateevent](https://w3c.github.io/edit-context/#dom-textformatupdateevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TextFormatUpdateEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textformatupdateevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextFormatUpdateEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextformatupdateevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextFormatUpdateEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextformatupdateevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc29cee3dcb0d0e66093dd0c18aa82e0eab9d6d14%0A*+Document+last+modified%3A+2024-07-26T15%3A08%3A29.000Z%0A%0A%3C%2Fdetails%3E)
