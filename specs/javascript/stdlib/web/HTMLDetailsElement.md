# HTMLDetailsElement

The `HTMLDetailsElement` interface provides special properties (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating [<details>](/en-US/docs/Web/HTML/Reference/Elements/details) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLDetailsElement.name](/en-US/docs/Web/API/HTMLDetailsElement/name)

A string reflecting the [name](/en-US/docs/Web/HTML/Reference/Elements/details#name) HTML attribute, which allows you to create a group of mutually-exclusive [<details>](/en-US/docs/Web/HTML/Reference/Elements/details) elements. Opening one of the named `<details>` elements of this group causes other elements of the group to close.

[HTMLDetailsElement.open](/en-US/docs/Web/API/HTMLDetailsElement/open)

A boolean value reflecting the [open](/en-US/docs/Web/HTML/Reference/Elements/details#open) HTML attribute, indicating whether or not the element's contents (not counting the [<summary>](/en-US/docs/Web/HTML/Reference/Elements/summary)) is to be shown to the user.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Events](#events)

Inherits events from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Examples](#examples)

### [Log chapters as they are opened and closed](#log_chapters_as_they_are_opened_and_closed)

This example uses the `HTMLElement`[toggle](/en-US/docs/Web/API/HTMLElement/toggle_event) event to add and remove chapters from a log aside as they are opened and closed.

#### HTML

html

```
<section id="summaries">
  <p>Chapter summaries:</p>
  <details id="ch1">
    <summary>Chapter I</summary>
    Philosophy reproves Boethius for the foolishness of his complaints against
    Fortune. Her very nature is caprice.
  </details>
  <details id="ch2">
    <summary>Chapter II</summary>
    Philosophy in Fortune's name replies to Boethius' reproaches, and proves
    that the gifts of Fortune are hers to give and to take away.
  </details>
  <details id="ch3">
    <summary>Chapter III</summary>
    Boethius falls back upon his present sense of misery. Philosophy reminds him
    of the brilliancy of his former fortunes.
  </details>
</section>
<aside id="log">
  <p>Open chapters:</p>
  <div data-id="ch1" hidden>I</div>
  <div data-id="ch2" hidden>II</div>
  <div data-id="ch3" hidden>III</div>
</aside>
```

#### CSS

css

```
body {
  display: flex;
}

#log {
  flex-shrink: 0;
  padding-left: 3em;
}

#summaries {
  flex-grow: 1;
}
```

#### JavaScript

js

```
function logItem(e) {
  console.log(e);
  const item = document.querySelector(`[data-id=${e.target.id}]`);
  item.toggleAttribute("hidden");
}

const chapters = document.querySelectorAll("details");
chapters.forEach((chapter) => {
  chapter.addEventListener("toggle", logItem);
});
```

#### Result

## [Specifications](#specifications)

Specification
[HTML# htmldetailselement](https://html.spec.whatwg.org/multipage/interactive-elements.html#htmldetailselement)
[HTML# event-toggle](https://html.spec.whatwg.org/multipage/indices.html#event-toggle)

## [Browser compatibility](#browser_compatibility)

### [api.HTMLDetailsElement](#api.HTMLDetailsElement)

### [api.HTMLElement.toggle_event.details_elements](#api.HTMLElement.toggle_event.details_elements)

## [See also](#see_also)

- The HTML element implementing this interface: [<details>](/en-US/docs/Web/HTML/Reference/Elements/details)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLDetailsElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmldetailselement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLDetailsElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmldetailselement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLDetailsElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmldetailselement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
