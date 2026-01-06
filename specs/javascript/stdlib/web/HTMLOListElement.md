# HTMLOListElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOListElement&level=high)

The `HTMLOListElement` interface provides special properties (beyond those defined on the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating ordered list elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLOListElement.reversed](/en-US/docs/Web/API/HTMLOListElement/reversed)

A boolean value reflecting the [reversed](/en-US/docs/Web/HTML/Reference/Elements/ol#reversed) and defining if the numbering is descending, that is its value is `true`, or ascending (`false`).

[HTMLOListElement.start](/en-US/docs/Web/API/HTMLOListElement/start)

A `long` value reflecting the [start](/en-US/docs/Web/HTML/Reference/Elements/ol#start) and defining the value of the first number of the first element of the list.

[HTMLOListElement.type](/en-US/docs/Web/API/HTMLOListElement/type)

A string value reflecting the [type](/en-US/docs/Web/HTML/Reference/Elements/ol#type) and defining the kind of marker to be used to display. It can have the following values:

- `'1'` meaning that decimal numbers are used: `1`, `2`, `3`, `4`, `5`, …
- `'a'` meaning that the lowercase latin alphabet is used: `a`, `b`, `c`, `d`, `e`, …
- `'A'` meaning that the uppercase latin alphabet is used: `A`, `B`, `C`, `D`, `E`, …
- `'i'` meaning that the lowercase latin numerals are used: `i`, `ii`, `iii`, `iv`, `v`, …
- `'I'` meaning that the uppercase latin numerals are used: `I`, `II`, `III`, `IV`, `V`, …

[HTMLOListElement.compact](/en-US/docs/Web/API/HTMLOListElement/compact)Deprecated

A boolean value indicating that spacing between list items should be reduced. This property reflects the [compact](/en-US/docs/Web/HTML/Reference/Elements/ol#compact) attribute only, it doesn't consider the [line-height](/en-US/docs/Web/CSS/Reference/Properties/line-height) CSS property used for that behavior in modern pages.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmlolistelement](https://html.spec.whatwg.org/multipage/grouping-content.html#htmlolistelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<ol>](/en-US/docs/Web/HTML/Reference/Elements/ol).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLOListElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlolistelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOListElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlolistelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOListElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlolistelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
