# HTMLSelectElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSelectElement&level=high)

The `HTMLSelectElement` interface represents a [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) HTML Element. These elements also share all of the properties and methods of other HTML elements via the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits the properties of [HTMLElement](/en-US/docs/Web/API/HTMLElement), and of [Element](/en-US/docs/Web/API/Element) and [Node](/en-US/docs/Web/API/Node).

[HTMLSelectElement.autocomplete](/en-US/docs/Web/API/HTMLSelectElement/autocomplete)

A string value reflecting the [autocomplete](/en-US/docs/Web/HTML/Reference/Elements/select#autocomplete), which indicates whether the value of the control can be automatically completed by the browser.

[HTMLSelectElement.disabled](/en-US/docs/Web/API/HTMLSelectElement/disabled)

A boolean value reflecting the [disabled](/en-US/docs/Web/HTML/Reference/Elements/select#disabled) HTML attribute, which indicates whether the control is disabled. If it is disabled, it does not accept clicks.

[HTMLSelectElement.form](/en-US/docs/Web/API/HTMLSelectElement/form)Read only

An [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) referencing the form that this element is associated with. If the element is not associated with of a [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element, then it returns `null`.

[HTMLSelectElement.labels](/en-US/docs/Web/API/HTMLSelectElement/labels)Read only

A [NodeList](/en-US/docs/Web/API/NodeList) of [<label>](/en-US/docs/Web/HTML/Reference/Elements/label) elements associated with the element.

[HTMLSelectElement.length](/en-US/docs/Web/API/HTMLSelectElement/length)

An `unsigned long` The number of [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) elements in this `select` element.

[HTMLSelectElement.multiple](/en-US/docs/Web/API/HTMLSelectElement/multiple)

A boolean value reflecting the [multiple](/en-US/docs/Web/HTML/Reference/Elements/select#multiple) HTML attribute, which indicates whether multiple items can be selected.

[HTMLSelectElement.name](/en-US/docs/Web/API/HTMLSelectElement/name)

A string reflecting the [name](/en-US/docs/Web/HTML/Reference/Elements/select#name) HTML attribute, containing the name of this control used by servers and DOM search functions.

[HTMLSelectElement.options](/en-US/docs/Web/API/HTMLSelectElement/options)Read only

An [HTMLOptionsCollection](/en-US/docs/Web/API/HTMLOptionsCollection) representing the set of [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) ([HTMLOptionElement](/en-US/docs/Web/API/HTMLOptionElement)) elements contained by this element.

[HTMLSelectElement.required](/en-US/docs/Web/API/HTMLSelectElement/required)

A boolean value reflecting the [required](/en-US/docs/Web/HTML/Reference/Elements/select#required) HTML attribute, which indicates whether the user is required to select a value before submitting the form.

[HTMLSelectElement.selectedIndex](/en-US/docs/Web/API/HTMLSelectElement/selectedIndex)

A `long` reflecting the index of the first selected [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) element. The value `-1` indicates no element is selected.

[HTMLSelectElement.selectedOptions](/en-US/docs/Web/API/HTMLSelectElement/selectedOptions)Read only

An [HTMLCollection](/en-US/docs/Web/API/HTMLCollection) representing the set of [<option>](/en-US/docs/Web/HTML/Reference/Elements/option) elements that are selected.

[HTMLSelectElement.size](/en-US/docs/Web/API/HTMLSelectElement/size)

A `long` reflecting the [size](/en-US/docs/Web/HTML/Reference/Elements/select#size) HTML attribute, which contains the number of visible items in the control. The default is 1, unless `multiple` is `true`, in which case it is 4.

[HTMLSelectElement.type](/en-US/docs/Web/API/HTMLSelectElement/type)Read only

A string representing the form control's type. When `multiple` is `true`, it returns `"select-multiple"`; otherwise, it returns `"select-one"`.

[HTMLSelectElement.validationMessage](/en-US/docs/Web/API/HTMLSelectElement/validationMessage)Read only

A string representing a localized message that describes the validation constraints that the control does not satisfy (if any). This attribute is the empty string if the control is not a candidate for constraint validation (`willValidate` is false), or it satisfies its constraints.

[HTMLSelectElement.validity](/en-US/docs/Web/API/HTMLSelectElement/validity)Read only

A [ValidityState](/en-US/docs/Web/API/ValidityState) reflecting the validity state that this control is in.

[HTMLSelectElement.value](/en-US/docs/Web/API/HTMLSelectElement/value)

A string reflecting the value of the form control. Returns the `value` property of the first selected option element if there is one, otherwise the empty string.

[HTMLSelectElement.willValidate](/en-US/docs/Web/API/HTMLSelectElement/willValidate)Read only

A boolean value that indicates whether the button is a candidate for constraint validation. It is `false` if any conditions bar it from constraint validation.

## [Instance methods](#instance_methods)

This interface inherits the methods of [HTMLElement](/en-US/docs/Web/API/HTMLElement), and of [Element](/en-US/docs/Web/API/Element) and [Node](/en-US/docs/Web/API/Node).

[HTMLSelectElement.add()](/en-US/docs/Web/API/HTMLSelectElement/add)

Adds an element to the collection of `option` elements for this `select` element.

[HTMLSelectElement.checkValidity()](/en-US/docs/Web/API/HTMLSelectElement/checkValidity)

Checks whether the element has any constraints and whether it satisfies them. If the element fails its constraints, the browser fires a cancelable [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) event at the element (and returns `false`).

[HTMLSelectElement.item()](/en-US/docs/Web/API/HTMLSelectElement/item)

Gets an item from the options collection for this [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) element. You can also access an item by specifying the index in square brackets or parentheses, without calling this method explicitly.

[HTMLSelectElement.namedItem()](/en-US/docs/Web/API/HTMLSelectElement/namedItem)

Gets the item in the options collection with the specified name. The name string can match either the `id` or the `name` attribute of an option node. You can also access an item by specifying the name in square brackets or parentheses, without calling this method explicitly.

[HTMLSelectElement.remove()](/en-US/docs/Web/API/HTMLSelectElement/remove)

Removes the element at the specified index from the options collection for this `select` element.

[HTMLSelectElement.reportValidity()](/en-US/docs/Web/API/HTMLSelectElement/reportValidity)

This method reports the problems with the constraints on the element, if any, to the user. If there are problems, it fires a cancelable [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) event at the element, and returns `false`; if there are no problems, it returns `true`.

[HTMLSelectElement.setCustomValidity()](/en-US/docs/Web/API/HTMLSelectElement/setCustomValidity)

Sets the custom validity message for the selection element to the specified message. Use the empty string to indicate that the element does not have a custom validity error.

[showPicker()](/en-US/docs/Web/API/HTMLSelectElement/showPicker)

Shows the option picker.

## [Events](#events)

This interface inherits the events of [HTMLElement](/en-US/docs/Web/API/HTMLElement), and of [Element](/en-US/docs/Web/API/Element) and [Node](/en-US/docs/Web/API/Node).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[change](/en-US/docs/Web/API/HTMLElement/change_event) event

Fires when the user selects an option.

[input](/en-US/docs/Web/API/Element/input_event) event

Fires when the `value` of an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input), [<select>](/en-US/docs/Web/HTML/Reference/Elements/select), or [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) element has been changed.

## [Example](#example)

### [Get information about the selected option](#get_information_about_the_selected_option)

js

```
/* assuming we have the following HTML
<select id='s'>
    <option>First</option>
    <option selected>Second</option>
    <option>Third</option>
</select>
*/

const select = document.getElementById("s");

// return the index of the selected option
console.log(select.selectedIndex); // 1

// return the value of the selected option
console.log(select.options[select.selectedIndex].value); // Second
```

A better way to track changes to the user's selection is to watch for the [change](/en-US/docs/Web/API/HTMLElement/change_event) event to occur on the `<select>`. This will tell you when the value changes, and you can then update anything you need to. See [the example provided](/en-US/docs/Web/API/HTMLElement/change_event#select_element) in the documentation for the `change` event for details.

## [Specifications](#specifications)

Specification
[HTML# htmlselectelement](https://html.spec.whatwg.org/multipage/form-elements.html#htmlselectelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [<select>](/en-US/docs/Web/HTML/Reference/Elements/select) HTML element, which implements this interface.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLSelectElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlselectelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSelectElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlselectelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLSelectElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlselectelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb2c8dcdae36907a87d1d1b9393ca4a35ebc765d6%0A*+Document+last+modified%3A+2025-04-12T01%3A47%3A48.000Z%0A%0A%3C%2Fdetails%3E)
