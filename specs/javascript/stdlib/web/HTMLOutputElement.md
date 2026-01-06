# HTMLOutputElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨August 2016⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOutputElement&level=high)

The `HTMLOutputElement` interface provides properties and methods (beyond those inherited from [HTMLElement](/en-US/docs/Web/API/HTMLElement)) for manipulating the layout and presentation of [<output>](/en-US/docs/Web/HTML/Reference/Elements/output) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Modes](#modes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLOutputElement.defaultValue](/en-US/docs/Web/API/HTMLOutputElement/defaultValue)

A string representing the default value of the element, initially the empty string.

[HTMLOutputElement.form](/en-US/docs/Web/API/HTMLOutputElement/form)Read only

An [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) indicating the form associated with the control, reflecting the [form](/en-US/docs/Web/HTML/Reference/Elements/output#form) HTML attribute if it is defined.

[HTMLOutputElement.htmlFor](/en-US/docs/Web/API/HTMLOutputElement/htmlFor)Read only

A [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) reflecting the [for](/en-US/docs/Web/HTML/Reference/Elements/output#for) HTML attribute, containing a list of IDs of other elements in the same document that contribute to (or otherwise affect) the calculated `value`.

[HTMLOutputElement.labels](/en-US/docs/Web/API/HTMLOutputElement/labels)Read only

A [NodeList](/en-US/docs/Web/API/NodeList) of [<label>](/en-US/docs/Web/HTML/Reference/Elements/label) elements associated with the element.

[HTMLOutputElement.name](/en-US/docs/Web/API/HTMLOutputElement/name)

A string reflecting the [name](/en-US/docs/Web/HTML/Reference/Elements/output#name) HTML attribute, containing the name for the control that is submitted with form data.

[HTMLOutputElement.type](/en-US/docs/Web/API/HTMLOutputElement/type)Read only

The string `"output"`.

[HTMLOutputElement.validationMessage](/en-US/docs/Web/API/HTMLOutputElement/validationMessage)Read only

A string representing a localized message that describes the validation constraints that the control does not satisfy (if any). This is the empty string if the control is not a candidate for constraint validation (`willValidate` is `false`), or it satisfies its constraints.

[HTMLOutputElement.validity](/en-US/docs/Web/API/HTMLOutputElement/validity)Read only

A [ValidityState](/en-US/docs/Web/API/ValidityState) representing the validity states that this element is in.

[HTMLOutputElement.value](/en-US/docs/Web/API/HTMLOutputElement/value)

A string representing the value of the contents of the elements. Behaves like the [Node.textContent](/en-US/docs/Web/API/Node/textContent) property.

[HTMLOutputElement.willValidate](/en-US/docs/Web/API/HTMLOutputElement/willValidate)Read only

Returns a boolean value that indicates whether the element is a candidate for constraint validation. Always `false` for `HTMLOutputElement` objects.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLOutputElement.checkValidity()](/en-US/docs/Web/API/HTMLOutputElement/checkValidity)

Checks the validity of the element and returns a boolean value holding the check result.

[HTMLOutputElement.reportValidity()](/en-US/docs/Web/API/HTMLOutputElement/reportValidity)

This method reports the problems with the constraints on the element, if any, to the user. If there are problems, fires an [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) event at the element, and returns `false`; if there are no problems, it returns `true`.

When the problem is reported, the user agent may focus the element and change the scrolling position of the document or perform some other action that brings the element to the user's attention. User agents may report more than one constraint violation if this element suffers from multiple problems at once. If the element is not rendered, then the user agent may report the error for the running script instead of notifying the user.

[HTMLOutputElement.setCustomValidity()](/en-US/docs/Web/API/HTMLOutputElement/setCustomValidity)

Sets a custom validity message for the element. If this message is not the empty string, then the element is suffering from a custom validity error, and does not validate.

## [Modes](#modes)

This element behaves in one of two modes: default mode and value mode.

### [Default mode](#default_mode)

Initially, the element is in default mode, and so the contents of the element represent both the value of the element and its default value.

If the element is in default mode when the descendants of the element are changed in any way, the `defaultValue` property is set to the value of the [textContent](/en-US/docs/Web/API/Node/textContent) property.

Resetting the form puts the element into default mode, and sets the [textContent](/en-US/docs/Web/API/Node/textContent) property to the value of the `defaultValue` property.

### [Value mode](#value_mode)

The element goes into value mode when the contents of the `value` property are set. The `value` property otherwise behaves like the [textContent](/en-US/docs/Web/API/Node/textContent) property. When the element is in value mode, the default value is accessible only through the `defaultValue` property.

## [Specifications](#specifications)

Specification
[HTML# htmloutputelement](https://html.spec.whatwg.org/multipage/form-elements.html#htmloutputelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<output>](/en-US/docs/Web/HTML/Reference/Elements/output).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLOutputElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmloutputelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOutputElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmloutputelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLOutputElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmloutputelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
