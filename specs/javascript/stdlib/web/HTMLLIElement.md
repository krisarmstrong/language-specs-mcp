# HTMLLIElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLLIElement&level=high)

The `HTMLLIElement` interface exposes specific properties and methods (beyond those defined by regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating list elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

`HTMLLIElement.type`Deprecated

A string representing the type of the bullets, `"disc"`, `"square"` or `"circle"`. As the standard way of defining the list type is via the CSS [list-style-type](/en-US/docs/Web/CSS/Reference/Properties/list-style-type) property, use the CSSOM methods to set it via a script.

[HTMLLIElement.value](/en-US/docs/Web/API/HTMLLIElement/value)

An integer indicating the ordinal position of the list element inside a given [<ol>](/en-US/docs/Web/HTML/Reference/Elements/ol). It reflects the `value` attribute of the HTML [<li>](/en-US/docs/Web/HTML/Reference/Elements/li) element, and can be smaller than `0`. If the [<li>](/en-US/docs/Web/HTML/Reference/Elements/li) element is not a child of an [<ol>](/en-US/docs/Web/HTML/Reference/Elements/ol) element, the property has no meaning.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmllielement](https://html.spec.whatwg.org/multipage/grouping-content.html#htmllielement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<li>](/en-US/docs/Web/HTML/Reference/Elements/li)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLLIElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmllielement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLLIElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmllielement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLLIElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmllielement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4032e31c51141511f5aa4068d5572e4736584afe%0A*+Document+last+modified%3A+2024-11-07T20%3A34%3A21.000Z%0A%0A%3C%2Fdetails%3E)
