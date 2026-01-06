# HTMLOptionElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOptionElement&level=high)

The `HTMLOptionElement` interface represents [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) elements and inherits all properties and methods of the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Option()](/en-US/docs/Web/API/HTMLOptionElement/Option)

Returns a newly created `HTMLOptionElement` object. It has four parameters: the text to display, `text`, the value associated, `value`, the value of `defaultSelected`, and the value of `selected`. The last three parameters are optional.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLOptionElement.defaultSelected](/en-US/docs/Web/API/HTMLOptionElement/defaultSelected)

Has a value of either `true` or `false` that shows the initial value of the [selected](/en-US/docs/Web/HTML/Reference/Elements/option#selected) HTML attribute, indicating whether the option is selected by default or not.

[HTMLOptionElement.disabled](/en-US/docs/Web/API/HTMLOptionElement/disabled)

Has a value of either `true` or `false` representing the value of the [disabled](/en-US/docs/Web/HTML/Reference/Elements/option#disabled) HTML attribute, which indicates that the option is unavailable to be selected.

[HTMLOptionElement.form](/en-US/docs/Web/API/HTMLOptionElement/form)Read only

A [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) representing the same value as the `form` of the corresponding [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) element, if the option is a descendant of a [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) element, or null if none is found.

[HTMLOptionElement.index](/en-US/docs/Web/API/HTMLOptionElement/index)Read only

A `long` representing the position of the option within the list of options it belongs to, in tree-order. If the option is not part of a list of options, like when it is part of the [<datalist>](/en-US/docs/Web/HTML/Reference/Elements/datalist) element, the value is `0`.

[HTMLOptionElement.label](/en-US/docs/Web/API/HTMLOptionElement/label)

A string that reflects the value of the [label](/en-US/docs/Web/HTML/Reference/Elements/option#label) HTML attribute, which provides a label for the option. If this attribute isn't specifically set, reading it returns the element's [text](/en-US/docs/Web/API/HTMLOptionElement/text) content.

[HTMLOptionElement.selected](/en-US/docs/Web/API/HTMLOptionElement/selected)

Has a value of either `true` or `false` that indicates whether the option is currently selected.

[HTMLOptionElement.text](/en-US/docs/Web/API/HTMLOptionElement/text)

A string that contains the text content of the element.

[HTMLOptionElement.value](/en-US/docs/Web/API/HTMLOptionElement/value)

A string that reflects the value of the [value](/en-US/docs/Web/HTML/Reference/Elements/option#value) HTML attribute, if it exists; otherwise reflects value of the [Node.textContent](/en-US/docs/Web/API/Node/textContent) property.

## [Instance methods](#instance_methods)

Doesn't implement any specific method, but inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmloptionelement](https://html.spec.whatwg.org/multipage/form-elements.html#htmloptionelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [<option>](/en-US/docs/Web/HTML/Reference/Elements/option)
- [<select>](/en-US/docs/Web/HTML/Reference/Elements/select)
- [<datalist>](/en-US/docs/Web/HTML/Reference/Elements/datalist)
- [<optgroup>](/en-US/docs/Web/HTML/Reference/Elements/optgroup)
- [HTMLOptionsCollection](/en-US/docs/Web/API/HTMLOptionsCollection)
- [HTMLSelectElement](/en-US/docs/Web/API/HTMLSelectElement)
- [HTMLOptGroupElement](/en-US/docs/Web/API/HTMLOptGroupElement)
- [HTMLElement](/en-US/docs/Web/API/HTMLElement)
- [HTMLCollection](/en-US/docs/Web/API/HTMLCollection)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLOptionElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmloptionelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOptionElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmloptionelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOptionElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmloptionelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
