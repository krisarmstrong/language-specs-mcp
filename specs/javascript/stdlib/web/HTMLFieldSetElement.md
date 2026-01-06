# HTMLFieldSetElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFieldSetElement&level=high)

The `HTMLFieldSetElement` interface provides special properties and methods (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of [<fieldset>](/en-US/docs/Web/HTML/Reference/Elements/fieldset) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLFieldSetElement.disabled](/en-US/docs/Web/API/HTMLFieldSetElement/disabled)

A boolean value reflecting the [disabled](/en-US/docs/Web/HTML/Reference/Elements/fieldset#disabled) HTML attribute, indicating whether the user can interact with the control.

[HTMLFieldSetElement.elements](/en-US/docs/Web/API/HTMLFieldSetElement/elements)Read only

The elements belonging to this field set. The type of this property depends on the version of the spec that is implemented by the browser.

[HTMLFieldSetElement.form](/en-US/docs/Web/API/HTMLFieldSetElement/form)Read only

An [HTMLFormControlsCollection](/en-US/docs/Web/API/HTMLFormControlsCollection) or [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) referencing the containing form element, if this element is in a form. If the field set is not a descendant of a form element, then the attribute can be the ID of any form element in the same document it is related to, or the `null` value if none matches.

[HTMLFieldSetElement.name](/en-US/docs/Web/API/HTMLFieldSetElement/name)

A string reflecting the [name](/en-US/docs/Web/HTML/Reference/Elements/fieldset#name) HTML attribute, containing the name of the field set. This can be used when accessing the field set in JavaScript. It is not part of the data which is sent to the server.

[HTMLFieldSetElement.type](/en-US/docs/Web/API/HTMLFieldSetElement/type)Read only

The string `"fieldset"`.

[HTMLFieldSetElement.validationMessage](/en-US/docs/Web/API/HTMLFieldSetElement/validationMessage)Read only

A string representing a localized message that describes the validation constraints that the element does not satisfy (if any). This is the empty string if the element is not a candidate for constraint validation (`willValidate` is `false`), or it satisfies its constraints.

[HTMLFieldSetElement.validity](/en-US/docs/Web/API/HTMLFieldSetElement/validity)Read only

A [ValidityState](/en-US/docs/Web/API/ValidityState) representing the validity states that this element is in.

[HTMLFieldSetElement.willValidate](/en-US/docs/Web/API/HTMLFieldSetElement/willValidate)Read only

A boolean value `false`, because [<fieldset>](/en-US/docs/Web/HTML/Reference/Elements/fieldset) objects are never candidates for constraint validation.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLFieldSetElement.checkValidity()](/en-US/docs/Web/API/HTMLFieldSetElement/checkValidity)

Always returns `true` because [<fieldset>](/en-US/docs/Web/HTML/Reference/Elements/fieldset) objects are never candidates for constraint validation.

[HTMLFieldSetElement.reportValidity()](/en-US/docs/Web/API/HTMLFieldSetElement/reportValidity)

Always returns `true` because [<fieldset>](/en-US/docs/Web/HTML/Reference/Elements/fieldset) objects are never candidates for constraint validation.

[HTMLFieldSetElement.setCustomValidity()](/en-US/docs/Web/API/HTMLFieldSetElement/setCustomValidity)

Sets a custom validity message for the field set. If this message is not the empty string, then the field set is suffering from a custom validity error, and does not validate.

## [Specifications](#specifications)

Specification
[HTML# htmlfieldsetelement](https://html.spec.whatwg.org/multipage/form-elements.html#htmlfieldsetelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<fieldset>](/en-US/docs/Web/HTML/Reference/Elements/fieldset).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLFieldSetElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlfieldsetelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFieldSetElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlfieldsetelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFieldSetElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlfieldsetelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2406bfdc031740afbd500a1fc953a76a4b7f8484%0A*+Document+last+modified%3A+2025-09-04T00%3A22%3A02.000Z%0A%0A%3C%2Fdetails%3E)
