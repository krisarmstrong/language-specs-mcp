# CharacterBoundsUpdateEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCharacterBoundsUpdateEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `CharacterBoundsUpdateEvent` interface is a [DOM event](/en-US/docs/Web/API/Event) that represents a request from the operating system to know the bounds of certain characters within an editable region that's attached to an [EditContext](/en-US/docs/Web/API/EditContext) instance.

This interface inherits properties from [Event](/en-US/docs/Web/API/Event).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[CharacterBoundsUpdateEvent()](/en-US/docs/Web/API/CharacterBoundsUpdateEvent/CharacterBoundsUpdateEvent)Experimental

Creates a new `CharacterBoundsUpdateEvent` object.

## [Instance properties](#instance_properties)

[CharacterBoundsUpdateEvent.rangeStart](/en-US/docs/Web/API/CharacterBoundsUpdateEvent/rangeStart)Read onlyExperimental

The offset of the first character within the editable region text for which the operating system needs the bounds.

[CharacterBoundsUpdateEvent.rangeEnd](/en-US/docs/Web/API/CharacterBoundsUpdateEvent/rangeEnd)Read onlyExperimental

The offset of the last character within the editable region text for which the operating system needs the bounds.

## [Examples](#examples)

### [Updating the character bounds when needed](#updating_the_character_bounds_when_needed)

This example shows how to use the `characterboundsupdate` event and the `updateCharacterBounds` method to inform the operating system of the character bounds it requires. Note that the event listener callback is only called when using an IME window, or other platform-specific editing UI surfaces, to compose text.

html

```
<canvas id="editor-canvas"></canvas>
```

js

```
const FONT_SIZE = 40;
const FONT = `${FONT_SIZE}px Arial`;

const canvas = document.getElementById("editor-canvas");
const ctx = canvas.getContext("2d");
ctx.font = FONT;

const editContext = new EditContext();
canvas.editContext = editContext;

function computeCharacterBound(offset) {
  // Measure the width from the start of the text to the character.
  const widthBeforeChar = ctx.measureText(
    editContext.text.substring(0, offset),
  ).width;

  // Measure the character width.
  const charWidth = ctx.measureText(editContext.text[offset]).width;

  const charX = canvas.offsetLeft + widthBeforeChar;
  const charY = canvas.offsetTop;

  // Return a DOMRect representing the character bounds.
  return DOMRect.fromRect({
    x: charX,
    y: charY - FONT_SIZE,
    width: charWidth,
    height: FONT_SIZE,
  });
}

editContext.addEventListener("characterboundsupdate", (e) => {
  const charBounds = [];
  for (let offset = e.rangeStart; offset < e.rangeEnd; offset++) {
    charBounds.push(computeCharacterBound(offset));
  }

  // Update the character bounds in the EditContext instance.
  editContext.updateCharacterBounds(e.rangeStart, charBounds);

  console.log(
    "The required character bounds are",
    charBounds
      .map(
        (bound) =>
          `(x: ${bound.x}, y: ${bound.y}, width: ${bound.width}, height: ${bound.height})`,
      )
      .join(", "),
  );
});
```

## [Specifications](#specifications)

Specification
[EditContext API# dom-characterboundsupdateevent](https://w3c.github.io/edit-context/#dom-characterboundsupdateevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CharacterBoundsUpdateEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/characterboundsupdateevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCharacterBoundsUpdateEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcharacterboundsupdateevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCharacterBoundsUpdateEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcharacterboundsupdateevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4a0413ef319179b7d0d833c42a156629544c8248%0A*+Document+last+modified%3A+2025-05-23T12%3A39%3A21.000Z%0A%0A%3C%2Fdetails%3E)
