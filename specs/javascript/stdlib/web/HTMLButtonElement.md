# HTMLButtonElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLButtonElement&level=high)

The `HTMLButtonElement` interface provides properties and methods (beyond the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLButtonElement.command](/en-US/docs/Web/API/HTMLButtonElement/command)

A string value indicating the action to be performed on an element being controlled by this button.

[HTMLButtonElement.commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement)

A reference to an existing [Element](/en-US/docs/Web/API/Element) that the button controls.

[HTMLButtonElement.disabled](/en-US/docs/Web/API/HTMLButtonElement/disabled)

A boolean value indicating whether or not the control is disabled, meaning that it does not accept any clicks.

[HTMLButtonElement.form](/en-US/docs/Web/API/HTMLButtonElement/form)Read only

An [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) reflecting the form that this button is associated with. If the button is a descendant of a form element, then this attribute is a reference to that form's associated `HTMLFormElement`. If the button is not a descendant of a form element, then the attribute can be a reference to any `HTMLFormElement` element in the same document it is related to, or the `null` value if none matches.

[HTMLButtonElement.formAction](/en-US/docs/Web/API/HTMLButtonElement/formAction)

A string reflecting the URI of a resource that processes information submitted by the button. If specified, this attribute overrides the [action](/en-US/docs/Web/HTML/Reference/Elements/form#action) attribute of the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element that owns this element.

[HTMLButtonElement.formEnctype](/en-US/docs/Web/API/HTMLButtonElement/formEnctype)

A string reflecting the type of content that is used to submit the form to the server. If specified, this attribute overrides the [enctype](/en-US/docs/Web/HTML/Reference/Elements/form#enctype) attribute of the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element that owns this element.

[HTMLButtonElement.formMethod](/en-US/docs/Web/API/HTMLButtonElement/formMethod)

A string reflecting the HTTP method that the browser uses to submit the form. If specified, this attribute overrides the [method](/en-US/docs/Web/HTML/Reference/Elements/form#method) attribute of the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element that owns this element.

[HTMLButtonElement.formNoValidate](/en-US/docs/Web/API/HTMLButtonElement/formNoValidate)

A boolean value indicating that the form is not to be validated when it is submitted. If specified, this attribute overrides the [novalidate](/en-US/docs/Web/HTML/Reference/Elements/form#novalidate) attribute of the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element that owns this element.

[HTMLButtonElement.formTarget](/en-US/docs/Web/API/HTMLButtonElement/formTarget)

A string reflecting a name or keyword indicating where to display the response received after submitting the form. If specified, this attribute overrides the [target](/en-US/docs/Web/HTML/Reference/Elements/form#target) attribute of the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element that owns this element.

[HTMLButtonElement.interestForElement](/en-US/docs/Web/API/HTMLButtonElement/interestForElement)ExperimentalNon-standard

Gets or sets the target element of an interest invoker, in cases where the associated [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) element is specified as an [interest invoker](/en-US/docs/Web/API/Popover_API/Using_interest_invokers#creating_an_interest_invoker).

[HTMLButtonElement.labels](/en-US/docs/Web/API/HTMLButtonElement/labels)Read only

A [NodeList](/en-US/docs/Web/API/NodeList) that represents a list of [<label>](/en-US/docs/Web/HTML/Reference/Elements/label) elements that are labels for this button.

[HTMLButtonElement.name](/en-US/docs/Web/API/HTMLButtonElement/name)

A string representing the object's name when submitted with a form. If specified, it must not be the empty string.

[HTMLButtonElement.popoverTargetAction](/en-US/docs/Web/API/HTMLButtonElement/popoverTargetAction)

Gets and sets the action to be performed (`"hide"`, `"show"`, or `"toggle"`) on a popover element being controlled by a control button. It reflects the value of the [popovertargetaction](/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction) HTML attribute.

[HTMLButtonElement.popoverTargetElement](/en-US/docs/Web/API/HTMLButtonElement/popoverTargetElement)

Gets and sets the popover element to control via a button. The JavaScript equivalent of the [popovertarget](/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget) HTML attribute.

[HTMLButtonElement.type](/en-US/docs/Web/API/HTMLButtonElement/type)

A string indicating the behavior of the button. This is an enumerated attribute with the following possible values:

- `submit`: The button submits the form. This is the default value if the attribute is not specified, or if it is dynamically changed to an empty or invalid value.
- `reset`: The button resets the form.
- `button`: The button does nothing.
- `menu`: The button displays a menu. Experimental

[HTMLButtonElement.willValidate](/en-US/docs/Web/API/HTMLButtonElement/willValidate)Read only

A boolean value indicating whether the button is a candidate for constraint validation. It is `false` if any conditions bar it from constraint validation, including: its `type` property is `reset` or `button`; it has a [<datalist>](/en-US/docs/Web/HTML/Reference/Elements/datalist) ancestor; or the `disabled` property is set to `true`.

[HTMLButtonElement.validationMessage](/en-US/docs/Web/API/HTMLButtonElement/validationMessage)Read only

A string representing the localized message that describes the validation constraints that the control does not satisfy (if any). This attribute is the empty string if the control is not a candidate for constraint validation (`willValidate` is `false`), or it satisfies its constraints.

[HTMLButtonElement.validity](/en-US/docs/Web/API/HTMLButtonElement/validity)Read only

A [ValidityState](/en-US/docs/Web/API/ValidityState) representing the validity states that this button is in.

[HTMLButtonElement.value](/en-US/docs/Web/API/HTMLButtonElement/value)

A string representing the current form control value of the button.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLButtonElement.checkValidity()](/en-US/docs/Web/API/HTMLButtonElement/checkValidity)

Returns `true` if the element's value has no validity problems; otherwise, returns `false`.

[HTMLButtonElement.reportValidity()](/en-US/docs/Web/API/HTMLButtonElement/reportValidity)

Performs the same action as `checkValidity()`, but also reports the result to the user if the `invalid` event was not canceled.

[HTMLButtonElement.setCustomValidity()](/en-US/docs/Web/API/HTMLButtonElement/setCustomValidity)

Sets the custom validity message for the element. Use the empty string to indicate that the element does not have a custom validity error.

## [Specifications](#specifications)

Specification
[HTML# htmlbuttonelement](https://html.spec.whatwg.org/multipage/form-elements.html#htmlbuttonelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<button>](/en-US/docs/Web/HTML/Reference/Elements/button)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLButtonElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlbuttonelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLButtonElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlbuttonelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLButtonElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlbuttonelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
