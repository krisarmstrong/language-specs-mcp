# TextFormat

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextFormat&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `TextFormat` interface represents specific formatting that should be applied to a range of text in an editable text region that's attached to an [EditContext](/en-US/docs/Web/API/EditContext) instance. The text formatting is requested by the [Input Method Editor](/en-US/docs/Glossary/Input_method_editor) (IME) window that the user is composing text with.

When using one of the default editable regions of the web, such as a [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) element, IME composition is handled by the browser and operating system for you. For example, when using Japanese IME in a textarea, on Windows, the following text formats can be applied:

- 

When text is being composed with the keyboard, the typed characters have a thin wavy underline:

- 

When the user selects a suggestion from the list of candidates in the IME window, the text is replaced and is underlined with a thick solid line:

When creating your own custom editable region by using the [EditContext API](/en-US/docs/Web/API/EditContext_API), you need to handle IME composition yourself. You should listen for the [textformatupdate](/en-US/docs/Web/API/EditContext/textformatupdate_event) event, which gives you the list of text formats that the IME window wants to apply to the text being composed. You should then update the formatting of the text displayed in your editable region accordingly.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[TextFormat()](/en-US/docs/Web/API/TextFormat/TextFormat)Experimental

Returns a new `TextFormat` instance.

## [Instance properties](#instance_properties)

[TextFormat.rangeStart](/en-US/docs/Web/API/TextFormat/rangeStart)Read onlyExperimental

The start position of the text range that needs to be formatted with the given text format.

[TextFormat.rangeEnd](/en-US/docs/Web/API/TextFormat/rangeEnd)Read onlyExperimental

The end position of the text range that needs to be formatted with the given text format.

[TextFormat.underlineStyle](/en-US/docs/Web/API/TextFormat/underlineStyle)Read onlyExperimental

The style of the underline that needs to be applied to the text range that is being formatted.

[TextFormat.underlineThickness](/en-US/docs/Web/API/TextFormat/underlineThickness)Read onlyExperimental

The thickness of the underline that needs to be applied to the text range that is being formatted.

## [Examples](#examples)

### [Using the textformatupdate event](#using_the_textformatupdate_event)

In the following example, the `textformatupdate` event is used to log the various formats that the IME composition window wants to apply to text ranges in the editable element. Note that the event listener callback in this example is only called when using an IME window to compose text.

html

```
<div id="editor"></div>
```

```
#editor {
  height: 200px;
  background: #eeeeee;
}
```

js

```
const editorEl = document.getElementById("editor");
const editContext = new EditContext(editorEl);
editorEl.editContext = editContext;

editContext.addEventListener("textformatupdate", (e) => {
  // Get the TextFormat instances.
  const formats = e.getTextFormats();

  // Iterate over the TextFormat instances.
  for (const format of formats) {
    console.log(
      `Applying a ${format.underlineThickness} ${format.underlineStyle} underline between ${format.rangeStart} and ${format.rangeEnd}.`,
    );
  }
});
```

## [Specifications](#specifications)

Specification
[EditContext API# dom-textformat](https://w3c.github.io/edit-context/#dom-textformat)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TextFormat/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textformat/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextFormat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextformat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextFormat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextformat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbc9f7bec1ab48f29d241e38a9f1598f783f6b60a%0A*+Document+last+modified%3A+2025-08-12T01%3A00%3A18.000Z%0A%0A%3C%2Fdetails%3E)
