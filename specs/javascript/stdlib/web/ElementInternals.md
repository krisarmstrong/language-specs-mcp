# ElementInternals

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElementInternals&level=high)

The `ElementInternals` interface of the [Document Object Model](/en-US/docs/Web/API/Document_Object_Model) gives web developers a way to allow custom elements to fully participate in HTML forms. It provides utilities for working with these elements in the same way you would work with any standard HTML form element, and also exposes the [Accessibility Object Model](https://wicg.github.io/aom/explainer.html) to the element.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

This interface has no constructor. An `ElementInternals` object is returned when calling [HTMLElement.attachInternals()](/en-US/docs/Web/API/HTMLElement/attachInternals).

## [Instance properties](#instance_properties)

[ElementInternals.shadowRoot](/en-US/docs/Web/API/ElementInternals/shadowRoot)Read only

Returns the [ShadowRoot](/en-US/docs/Web/API/ShadowRoot) object associated with this element.

[ElementInternals.form](/en-US/docs/Web/API/ElementInternals/form)Read only

Returns the [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) associated with this element.

[ElementInternals.states](/en-US/docs/Web/API/ElementInternals/states)Read only

Returns the [CustomStateSet](/en-US/docs/Web/API/CustomStateSet) associated with this element.

[ElementInternals.willValidate](/en-US/docs/Web/API/ElementInternals/willValidate)Read only

A boolean value which returns true if the element is a submittable element that is a candidate for [constraint validation](/en-US/docs/Web/HTML/Guides/Constraint_validation).

[ElementInternals.validity](/en-US/docs/Web/API/ElementInternals/validity)Read only

Returns a [ValidityState](/en-US/docs/Web/API/ValidityState) object which represents the different validity states the element can be in, with respect to constraint validation.

[ElementInternals.validationMessage](/en-US/docs/Web/API/ElementInternals/validationMessage)Read only

A string containing the validation message of this element.

[ElementInternals.labels](/en-US/docs/Web/API/ElementInternals/labels)Read only

Returns a [NodeList](/en-US/docs/Web/API/NodeList) of all of the label elements associated with this element.

### [Instance properties included from ARIA](#instance_properties_included_from_aria)

The `ElementInternals` interface also includes the following properties.

Note: These are included in order that default accessibility semantics can be defined on a custom element. These may be overwritten by author-defined attributes, but ensure that default semantics are retained should the author delete those attributes, or fail to add them at all. For more information see the [Accessibility Object Model explainer](https://wicg.github.io/aom/explainer.html#default-semantics-for-custom-elements-via-the-elementinternals-object).

[ElementInternals.ariaAtomic](/en-US/docs/Web/API/ElementInternals/ariaAtomic)

A string reflecting the [aria-atomic](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-atomic) attribute, which indicates whether assistive technologies will present all, or only parts of, the changed region based on the change notifications defined by the [aria-relevant](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-relevant) attribute.

[ElementInternals.ariaAutoComplete](/en-US/docs/Web/API/ElementInternals/ariaAutoComplete)

A string reflecting the [aria-autocomplete](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-autocomplete) attribute, which indicates whether inputting text could trigger display of one or more predictions of the user's intended value for a combobox, searchbox, or textbox and specifies how predictions would be presented if they were made.

[ElementInternals.ariaBrailleLabel](/en-US/docs/Web/API/ElementInternals/ariaBrailleLabel)

A string reflecting the [aria-braillelabel](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-braillelabel) attribute, which defines the braille label of the element.

[ElementInternals.ariaBrailleRoleDescription](/en-US/docs/Web/API/ElementInternals/ariaBrailleRoleDescription)

A string reflecting the [aria-brailleroledescription](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-brailleroledescription) attribute, which defines the ARIA braille role description of the element.

[ElementInternals.ariaBusy](/en-US/docs/Web/API/ElementInternals/ariaBusy)

A string reflecting the [aria-busy](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-busy) attribute, which indicates whether an element is being modified, as assistive technologies may want to wait until the modifications are complete before exposing them to the user.

[ElementInternals.ariaChecked](/en-US/docs/Web/API/ElementInternals/ariaChecked)

A string reflecting the [aria-checked](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-checked) attribute, which indicates the current "checked" state of checkboxes, radio buttons, and other widgets that have a checked state.

[ElementInternals.ariaColCount](/en-US/docs/Web/API/ElementInternals/ariaColCount)

A string reflecting the [aria-colcount](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colcount) attribute, which defines the number of columns in a table, grid, or treegrid.

[ElementInternals.ariaColIndex](/en-US/docs/Web/API/ElementInternals/ariaColIndex)

A string reflecting the [aria-colindex](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colindex) attribute, which defines an element's column index or position with respect to the total number of columns within a table, grid, or treegrid.

[ElementInternals.ariaColIndexText](/en-US/docs/Web/API/ElementInternals/ariaColIndexText)

A string reflecting the [aria-colindextext](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colindextext) attribute, which defines a human readable text alternative of aria-colindex.

[ElementInternals.ariaColSpan](/en-US/docs/Web/API/ElementInternals/ariaColSpan)

A string reflecting the [aria-colspan](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-colspan) attribute, which defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid.

[ElementInternals.ariaCurrent](/en-US/docs/Web/API/ElementInternals/ariaCurrent)

A string reflecting the [aria-current](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-current) attribute, which indicates the element that represents the current item within a container or set of related elements.

[ElementInternals.ariaDescription](/en-US/docs/Web/API/ElementInternals/ariaDescription)

A string reflecting the [aria-description](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-description) attribute, which defines a string value that describes or annotates the current ElementInternals.

[ElementInternals.ariaDisabled](/en-US/docs/Web/API/ElementInternals/ariaDisabled)

A string reflecting the [aria-disabled](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-disabled) attribute, which indicates that the element is perceivable but disabled, so it is not editable or otherwise operable.

[ElementInternals.ariaExpanded](/en-US/docs/Web/API/ElementInternals/ariaExpanded)

A string reflecting the [aria-expanded](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-expanded) attribute, which indicates whether a grouping element owned or controlled by this element is expanded or collapsed.

[ElementInternals.ariaHasPopup](/en-US/docs/Web/API/ElementInternals/ariaHasPopup)

A string reflecting the [aria-haspopup](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-haspopup) attribute, which indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an ElementInternals.

[ElementInternals.ariaHidden](/en-US/docs/Web/API/ElementInternals/ariaHidden)

A string reflecting the [aria-hidden](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden) attribute, which indicates whether the element is exposed to an accessibility API.

[ElementInternals.ariaInvalid](/en-US/docs/Web/API/ElementInternals/ariaInvalid)

A string reflecting the [aria-invalid](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-invalid) attribute, which indicates the entered value does not conform to the format expected by the application.

[ElementInternals.ariaKeyShortcuts](/en-US/docs/Web/API/ElementInternals/ariaKeyShortcuts)

A string reflecting the [aria-keyshortcuts](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-keyshortcuts) attribute, which indicates keyboard shortcuts that an author has implemented to activate or give focus to an object.

[ElementInternals.ariaLabel](/en-US/docs/Web/API/ElementInternals/ariaLabel)

A string reflecting the [aria-label](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label) attribute, which defines a string value that labels the current object.

[ElementInternals.ariaLevel](/en-US/docs/Web/API/ElementInternals/ariaLevel)

A string reflecting the [aria-level](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level) attribute, which defines the hierarchical level of an element within a structure.

[ElementInternals.ariaLive](/en-US/docs/Web/API/ElementInternals/ariaLive)

A string reflecting the [aria-live](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-live) attribute, which indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region.

[ElementInternals.ariaModal](/en-US/docs/Web/API/ElementInternals/ariaModal)

A string reflecting the [aria-modal](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-modal) attribute, which indicates whether an element is modal when displayed.

[ElementInternals.ariaMultiline](/en-US/docs/Web/API/ElementInternals/ariaMultiLine)

A string reflecting the [aria-multiline](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-multiline) attribute, which indicates whether a text box accepts multiple lines of input or only a single line.

[ElementInternals.ariaMultiSelectable](/en-US/docs/Web/API/ElementInternals/ariaMultiSelectable)

A string reflecting the [aria-multiselectable](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-multiselectable) attribute, which indicates that the user may select more than one item from the current selectable descendants.

[ElementInternals.ariaOrientation](/en-US/docs/Web/API/ElementInternals/ariaOrientation)

A string reflecting the [aria-orientation](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-orientation) attribute, which indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous.

[ElementInternals.ariaPlaceholder](/en-US/docs/Web/API/ElementInternals/ariaPlaceholder)

A string reflecting the [aria-placeholder](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-placeholder) attribute, which defines a short hint intended to aid the user with data entry when the control has no value.

[ElementInternals.ariaPosInSet](/en-US/docs/Web/API/ElementInternals/ariaPosInSet)

A string reflecting the [aria-posinset](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-posinset) attribute, which defines an element's number or position in the current set of listitems or treeitems.

[ElementInternals.ariaPressed](/en-US/docs/Web/API/ElementInternals/ariaPressed)

A string reflecting the [aria-pressed](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-pressed) attribute, which indicates the current "pressed" state of toggle buttons.

[ElementInternals.ariaReadOnly](/en-US/docs/Web/API/ElementInternals/ariaReadOnly)

A string reflecting the [aria-readonly](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-readonly) attribute, which indicates that the element is not editable, but is otherwise operable.

[ElementInternals.ariaRelevant](/en-US/docs/Web/API/ElementInternals/ariaRelevant)Non-standard

A string reflecting the [aria-relevant](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-relevant) attribute, which indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified. This is used to describe what changes in an `aria-live` region are relevant and should be announced.

[ElementInternals.ariaRequired](/en-US/docs/Web/API/ElementInternals/ariaRequired)

A string reflecting the [aria-required](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-required) attribute, which indicates that user input is required on the element before a form may be submitted.

[ElementInternals.role](/en-US/docs/Web/API/ElementInternals/role)

A string which contains an ARIA role. A full list of ARIA roles can be found on the [ARIA techniques page](/en-US/docs/Web/Accessibility/ARIA/Guides/Techniques).

[ElementInternals.ariaRoleDescription](/en-US/docs/Web/API/ElementInternals/ariaRoleDescription)

A string reflecting the [aria-roledescription](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-roledescription) attribute, which defines a human-readable, author-localized description for the role of an Element.

[ElementInternals.ariaRowCount](/en-US/docs/Web/API/ElementInternals/ariaRowCount)

A string reflecting the [aria-rowcount](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowcount) attribute, which defines the total number of rows in a table, grid, or treegrid.

[ElementInternals.ariaRowIndex](/en-US/docs/Web/API/ElementInternals/ariaRowIndex)

A string reflecting the [aria-rowindex](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowindex) attribute, which defines an element's row index or position with respect to the total number of rows within a table, grid, or treegrid.

[ElementInternals.ariaRowIndexText](/en-US/docs/Web/API/ElementInternals/ariaRowIndexText)

A string reflecting the [aria-rowindextext](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowindextext) attribute, which defines a human readable text alternative of aria-rowindex.

[ElementInternals.ariaRowSpan](/en-US/docs/Web/API/ElementInternals/ariaRowSpan)

A string reflecting the [aria-rowspan](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-rowspan) attribute, which defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid.

[ElementInternals.ariaSelected](/en-US/docs/Web/API/ElementInternals/ariaSelected)

A string reflecting the [aria-selected](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-selected) attribute, which indicates the current "selected" state of elements that have a selected state.

[ElementInternals.ariaSetSize](/en-US/docs/Web/API/ElementInternals/ariaSetSize)

A string reflecting the [aria-setsize](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-setsize) attribute, which defines the number of items in the current set of listitems or treeitems.

[ElementInternals.ariaSort](/en-US/docs/Web/API/ElementInternals/ariaSort)

A string reflecting the [aria-sort](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-sort) attribute, which indicates if items in a table or grid are sorted in ascending or descending order.

[ElementInternals.ariaValueMax](/en-US/docs/Web/API/ElementInternals/ariaValueMax)

A string reflecting the [aria-valueMax](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuemax) attribute, which defines the maximum allowed value for a range widget.

[ElementInternals.ariaValueMin](/en-US/docs/Web/API/ElementInternals/ariaValueMin)

A string reflecting the [aria-valueMin](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuemin) attribute, which defines the minimum allowed value for a range widget.

[ElementInternals.ariaValueNow](/en-US/docs/Web/API/ElementInternals/ariaValueNow)

A string reflecting the [aria-valueNow](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuenow) attribute, which defines the current value for a range widget.

[ElementInternals.ariaValueText](/en-US/docs/Web/API/ElementInternals/ariaValueText)

A string reflecting the [aria-valuetext](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-valuetext) attribute, which defines the human-readable text alternative of aria-valuenow for a range widget.

#### Instance properties reflected from ARIA element references

The properties reflect the elements specified by `id` reference in the corresponding attributes, but with some caveats. See [Reflected element references](/en-US/docs/Web/API/Document_Object_Model/Reflected_attributes#reflected_element_references) in the Reflected attributes guide for more information.

[ElementInternals.ariaActiveDescendantElement](/en-US/docs/Web/API/ElementInternals/ariaActiveDescendantElement)

An element that represents the current active element when focus is on a [composite](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/composite_role) widget, [combobox](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role), [textbox](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role), [group](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role), or [application](/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role). Reflects the [aria-activedescendant](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-activedescendant) attribute.

[ElementInternals.ariaControlsElements](/en-US/docs/Web/API/ElementInternals/ariaControlsElements)

An array of elements whose contents or presence are controlled by the element it is applied to. Reflects the [aria-controls](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-controls) attribute.

[ElementInternals.ariaDescribedByElements](/en-US/docs/Web/API/ElementInternals/ariaDescribedByElements)

An array of elements that contain the accessible description for the element it is applied to. Reflects the [aria-describedby](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby) attribute.

[ElementInternals.ariaDetailsElements](/en-US/docs/Web/API/ElementInternals/ariaDetailsElements)

An array of elements that provide accessible details for the element it is applied to. Reflects the [aria-details](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-details) attribute.

[ElementInternals.ariaErrorMessageElements](/en-US/docs/Web/API/ElementInternals/ariaErrorMessageElements)

An array of elements that provide an error message for the element it is applied to. Reflects the [aria-errormessage](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-errormessage) attribute.

[ElementInternals.ariaFlowToElements](/en-US/docs/Web/API/ElementInternals/ariaFlowToElements)

An array of elements that identify the next element (or elements) in an alternate reading order of content, overriding the general default reading order at the user's discretion. Reflects the [aria-flowto](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-flowto) attribute.

[ElementInternals.ariaLabelledByElements](/en-US/docs/Web/API/ElementInternals/ariaLabelledByElements)

An array of elements that provide the accessible name for the element it is applied to. Reflects the [aria-labelledby](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby) attribute.

[ElementInternals.ariaOwnsElements](/en-US/docs/Web/API/ElementInternals/ariaOwnsElements)

An array of elements owned by the element this is applied to. This is used to define a visual, functional, or contextual relationship between a parent and its child elements when the DOM hierarchy cannot be used to represent the relationship. Reflects the [aria-owns](/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-owns) attribute.

## [Instance methods](#instance_methods)

[ElementInternals.setFormValue()](/en-US/docs/Web/API/ElementInternals/setFormValue)

Sets the element's submission value and state, communicating these to the user agent.

[ElementInternals.setValidity()](/en-US/docs/Web/API/ElementInternals/setValidity)

Sets the validity of the element.

[ElementInternals.checkValidity()](/en-US/docs/Web/API/ElementInternals/checkValidity)

Checks if an element meets any [constraint validation](/en-US/docs/Web/HTML/Guides/Constraint_validation) rules applied to it.

[ElementInternals.reportValidity()](/en-US/docs/Web/API/ElementInternals/reportValidity)

Checks if an element meets any [constraint validation](/en-US/docs/Web/HTML/Guides/Constraint_validation) rules applied to it, and also sends a validation message to the user agent.

## [Examples](#examples)

The following example demonstrates how to create a custom form-associated element with [HTMLElement.attachInternals](/en-US/docs/Web/API/HTMLElement/attachInternals).

js

```
class CustomCheckbox extends HTMLElement {
  static formAssociated = true;

  constructor() {
    super();
    this.internals_ = this.attachInternals();
  }

  // …
}

window.customElements.define("custom-checkbox", CustomCheckbox);

let element = document.createElement("custom-checkbox");
let form = document.createElement("form");

// Append element to form to associate it
form.appendChild(element);

console.log(element.internals_.form);
// expected output: <form><custom-checkbox></custom-checkbox></form>
```

## [Specifications](#specifications)

Specification
[HTML# the-elementinternals-interface](https://html.spec.whatwg.org/multipage/custom-elements.html#the-elementinternals-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [More capable form controls](https://web.dev/articles/more-capable-form-controls) via web.dev (2019)
- [Creating custom form controls with ElementInternals](https://css-tricks.com/creating-custom-form-controls-with-elementinternals/) via CSS-tricks (2021)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ElementInternals/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/elementinternals/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElementInternals&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Felementinternals%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElementInternals%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Felementinternals%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85d5b8d224843c37974318ff04fbcc1ab69ef95d%0A*+Document+last+modified%3A+2025-05-02T00%3A21%3A14.000Z%0A%0A%3C%2Fdetails%3E)
