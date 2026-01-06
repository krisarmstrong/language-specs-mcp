# HTMLInputElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLInputElement&level=high)

The `HTMLInputElement` interface provides special properties and methods for manipulating the options, layout, and presentation of [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Some properties only apply to input element types that support the corresponding attributes.

`align`Deprecated

A string that represents the alignment of the element. Use CSS instead.

[alpha](/en-US/docs/Web/API/HTMLInputElement/alpha)Experimental

A boolean that represents the element's [alpha](/en-US/docs/Web/HTML/Reference/Elements/input/color#alpha) attribute, indicating whether the color's alpha component can be manipulated by the end user and does not have to be fully opaque.

[colorSpace](/en-US/docs/Web/API/HTMLInputElement/colorSpace)Experimental

A string that represents the element's [colorspace](/en-US/docs/Web/HTML/Reference/Elements/input/color#colorspace) attribute, indicating the [color space](/en-US/docs/Glossary/Color_space) of the serialized CSS color (sRGB or display-p3).

[defaultValue](/en-US/docs/Web/API/HTMLInputElement/defaultValue)

A string that represents the default value as originally specified in the HTML that created this object.

[dirName](/en-US/docs/Web/API/HTMLInputElement/dirName)

A string that represents the directionality of the element.

`incremental`Non-standard

A boolean that represents the search event fire mode, if `true`, fires on every keypress, or on clicking the cancel button; otherwise fires when pressing Enter.

[labels](/en-US/docs/Web/API/HTMLInputElement/labels)Read only

Returns a list of [<label>](/en-US/docs/Web/HTML/Reference/Elements/label) elements that are labels for this element.

[list](/en-US/docs/Web/API/HTMLInputElement/list)Read only

Returns the element pointed to by the [list](/en-US/docs/Web/HTML/Reference/Elements/input#list) attribute. The property may be `null` if no HTML element is found in the same tree.

[multiple](/en-US/docs/Web/API/HTMLInputElement/multiple)

A boolean that represents the element's [multiple](/en-US/docs/Web/HTML/Reference/Elements/input#multiple) attribute, indicating whether more than one value is possible (e.g., multiple files).

[name](/en-US/docs/Web/API/HTMLInputElement/name)

A string that represents the element's [name](/en-US/docs/Web/HTML/Reference/Elements/input#name) attribute, containing a name that identifies the element when submitting the form.

[popoverTargetAction](/en-US/docs/Web/API/HTMLInputElement/popoverTargetAction)

Gets and sets the action to be performed (`"hide"`, `"show"`, or `"toggle"`) on a popover element being controlled by an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element of `type="button"`. It reflects the value of the [popovertargetaction](/en-US/docs/Web/HTML/Reference/Elements/input#popovertargetaction) HTML attribute.

[popoverTargetElement](/en-US/docs/Web/API/HTMLInputElement/popoverTargetElement)

Gets and sets the popover element to control via an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element of `type="button"`. The JavaScript equivalent of the [popovertarget](/en-US/docs/Web/HTML/Reference/Elements/input#popovertarget) HTML attribute.

[step](/en-US/docs/Web/API/HTMLInputElement/step)

A string that represents the element's [step](/en-US/docs/Web/HTML/Reference/Elements/input#step) attribute, which works with [min](/en-US/docs/Web/HTML/Reference/Elements/input#min) and [max](/en-US/docs/Web/HTML/Reference/Elements/input#max) to limit the increments at which a numeric or date-time value can be set. It can be the string `any` or a positive floating point number. If this is not set to `any`, the control accepts only values at multiples of the step value greater than the minimum.

[type](/en-US/docs/Web/API/HTMLInputElement/type)

A string that represents the element's [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) attribute, indicating the type of control to display. For possible values, see the documentation for the [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) attribute.

`useMap`Deprecated

A string that represents a client-side image map.

[value](/en-US/docs/Web/API/HTMLInputElement/value)

A string that represents the current value of the control. If the user enters a value different from the value expected, this may return an empty string.

[valueAsDate](/en-US/docs/Web/API/HTMLInputElement/valueAsDate)

A [Date](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) that represents the value of the element, interpreted as a date, or `null` if conversion is not possible.

[valueAsNumber](/en-US/docs/Web/API/HTMLInputElement/valueAsNumber)

A number that represents the value of the element, interpreted as one of the following, in order: A time value, a number, or `NaN` if conversion is impossible.

### [Instance properties related to the parent form](#instance_properties_related_to_the_parent_form)

[form](/en-US/docs/Web/API/HTMLInputElement/form)Read only

Returns a reference to the parent [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element.

[formAction](/en-US/docs/Web/API/HTMLInputElement/formAction)

A string that represents the element's [formaction](/en-US/docs/Web/HTML/Reference/Elements/input#formaction) attribute, containing the URL of a program that processes information submitted by the element. This overrides the [action](/en-US/docs/Web/HTML/Reference/Elements/form#action) attribute of the parent form.

[formEnctype](/en-US/docs/Web/API/HTMLInputElement/formEnctype)

A string that represents the element's [formenctype](/en-US/docs/Web/HTML/Reference/Elements/input#formenctype) attribute, containing the type of content that is used to submit the form to the server. This overrides the [enctype](/en-US/docs/Web/HTML/Reference/Elements/form#enctype) attribute of the parent form.

[formMethod](/en-US/docs/Web/API/HTMLInputElement/formMethod)

A string that represents the element's [formmethod](/en-US/docs/Web/HTML/Reference/Elements/input#formmethod) attribute, containing the HTTP method that the browser uses to submit the form. This overrides the [method](/en-US/docs/Web/HTML/Reference/Elements/form#method) attribute of the parent form.

[formNoValidate](/en-US/docs/Web/API/HTMLInputElement/formNoValidate)

A boolean that represents the element's [formnovalidate](/en-US/docs/Web/HTML/Reference/Elements/input#formnovalidate) attribute, indicating that the form is not to be validated when it is submitted. This overrides the [novalidate](/en-US/docs/Web/HTML/Reference/Elements/form#novalidate) attribute of the parent form.

[formTarget](/en-US/docs/Web/API/HTMLInputElement/formTarget)

A string that represents the element's [formtarget](/en-US/docs/Web/HTML/Reference/Elements/input#formtarget) attribute, containing a name or keyword indicating where to display the response that is received after submitting the form. This overrides the [target](/en-US/docs/Web/HTML/Reference/Elements/form#target) attribute of the parent form.

### [Instance properties that apply to any type of input element that is not hidden](#instance_properties_that_apply_to_any_type_of_input_element_that_is_not_hidden)

[disabled](/en-US/docs/Web/API/HTMLInputElement/disabled)

A boolean that represents the element's [disabled](/en-US/docs/Web/HTML/Reference/Elements/input#disabled) attribute, indicating that the control is not available for interaction. The input values will not be submitted with the form. See also [readonly](/en-US/docs/Web/HTML/Reference/Elements/input#readonly).

[required](/en-US/docs/Web/API/HTMLInputElement/required)

A boolean that represents the element's [required](/en-US/docs/Web/HTML/Reference/Elements/input#required) attribute, indicating that the user must fill in a value before submitting a form.

[validationMessage](/en-US/docs/Web/API/HTMLInputElement/validationMessage)Read only

Returns a localized message that describes the validation constraints that the control does not satisfy (if any). This is the empty string if the control is not a candidate for constraint validation ([willValidate](/en-US/docs/Web/API/HTMLInputElement/willValidate) is `false`), or it satisfies its constraints. This value can be set by the [setCustomValidity()](/en-US/docs/Web/API/HTMLInputElement/setCustomValidity) method.

[validity](/en-US/docs/Web/API/HTMLInputElement/validity)Read only

Returns the element's current validity state.

[willValidate](/en-US/docs/Web/API/HTMLInputElement/willValidate)Read only

Returns whether the element is a candidate for constraint validation. It is `false` if any conditions bar it from constraint validation, including: its `type` is one of `hidden`, `reset` or `button`, it has a [<datalist>](/en-US/docs/Web/HTML/Reference/Elements/datalist) ancestor or its `disabled` property is `true`.

### [Instance properties that apply only to elements of type checkbox or radio](#instance_properties_that_apply_only_to_elements_of_type_checkbox_or_radio)

[checked](/en-US/docs/Web/API/HTMLInputElement/checked)

A boolean that represents the current state of the element.

[defaultChecked](/en-US/docs/Web/API/HTMLInputElement/defaultChecked)

A boolean that represents the default state of a radio button or checkbox as originally specified in HTML that created this object.

[indeterminate](/en-US/docs/Web/API/HTMLInputElement/indeterminate)

A boolean that represents whether the checkbox or radio button is in indeterminate state. For checkboxes, the effect is that the appearance of the checkbox is obscured/greyed in some way as to indicate its state is indeterminate (not checked but not unchecked). Does not affect the value of the `checked` attribute, and clicking the checkbox will set the value to false.

### [Instance properties that apply only to elements of type image](#instance_properties_that_apply_only_to_elements_of_type_image)

[alt](/en-US/docs/Web/API/HTMLInputElement/alt)

A string that represents the element's [alt](/en-US/docs/Web/HTML/Reference/Elements/input#alt) attribute, containing alternative text to use.

[height](/en-US/docs/Web/API/HTMLInputElement/height)

A string that represents the element's [height](/en-US/docs/Web/HTML/Reference/Elements/input#height) attribute, which defines the height of the image displayed for the button.

[src](/en-US/docs/Web/API/HTMLInputElement/src)

A string that represents the element's [src](/en-US/docs/Web/HTML/Reference/Elements/input#src) attribute, which specifies a URI for the location of an image to display on the graphical submit button.

[width](/en-US/docs/Web/API/HTMLInputElement/width)

A string that represents the element's [width](/en-US/docs/Web/HTML/Reference/Elements/input#width) attribute, which defines the width of the image displayed for the button.

### [Instance properties that apply only to elements of type file](#instance_properties_that_apply_only_to_elements_of_type_file)

[accept](/en-US/docs/Web/API/HTMLInputElement/accept)

A string that represents the element's [accept](/en-US/docs/Web/HTML/Reference/Elements/input#accept) attribute, containing comma-separated list of file types that can be selected.

[capture](/en-US/docs/Web/API/HTMLInputElement/capture)

A string that represents the element's [capture](/en-US/docs/Web/HTML/Reference/Elements/input#capture) attribute, indicating the media capture input method in file upload controls.

[files](/en-US/docs/Web/API/HTMLInputElement/files)

A [FileList](/en-US/docs/Web/API/FileList) that represents the files selected for upload.

[webkitdirectory](/en-US/docs/Web/API/HTMLInputElement/webkitdirectory)

A boolean that represents the [webkitdirectory](/en-US/docs/Web/HTML/Reference/Elements/input#webkitdirectory) attribute. If `true`, the file-system-picker interface only accepts directories instead of files.

[webkitEntries](/en-US/docs/Web/API/HTMLInputElement/webkitEntries)Read only

Describes the currently selected files or directories.

### [Instance properties that apply only to visible elements containing text or numbers](#instance_properties_that_apply_only_to_visible_elements_containing_text_or_numbers)

[autocomplete](/en-US/docs/Web/API/HTMLInputElement/autocomplete)

A string that represents the element's [autocomplete](/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete) attribute, indicating whether the value of the control can be automatically completed by the browser.

[max](/en-US/docs/Web/API/HTMLInputElement/max)

A string that represents the element's [max](/en-US/docs/Web/HTML/Reference/Elements/input#max) attribute, containing the maximum (numeric or date-time) value for this item, which must not be less than its minimum ([min](/en-US/docs/Web/HTML/Reference/Elements/input#min) attribute) value.

[maxLength](/en-US/docs/Web/API/HTMLInputElement/maxLength)

A number that represents the element's [maxlength](/en-US/docs/Web/HTML/Reference/Elements/input#maxlength) attribute, containing the maximum number of characters (in Unicode code points) that the value can have.

[min](/en-US/docs/Web/API/HTMLInputElement/min)

A string that represents the element's [min](/en-US/docs/Web/HTML/Reference/Elements/input#min) attribute, containing the minimum (numeric or date-time) value for this item, which must not be greater than its maximum ([max](/en-US/docs/Web/HTML/Reference/Elements/input#max) attribute) value.

[minLength](/en-US/docs/Web/API/HTMLInputElement/minLength)

A number that represents the element's [minlength](/en-US/docs/Web/HTML/Reference/Elements/input#minlength) attribute, containing the minimum number of characters (in Unicode code points) that the value can have.

[pattern](/en-US/docs/Web/API/HTMLInputElement/pattern)

A string that represents the element's [pattern](/en-US/docs/Web/HTML/Reference/Elements/input#pattern) attribute, containing a regular expression that the control's value is checked against. Use the [title](/en-US/docs/Web/HTML/Reference/Elements/input#title) attribute to describe the pattern to help the user. This attribute only applies when the value of the [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) attribute is `text`, `search`, `tel`, `url` or `email`.

[placeholder](/en-US/docs/Web/API/HTMLInputElement/placeholder)

A string that represents the element's [placeholder](/en-US/docs/Web/HTML/Reference/Elements/input#placeholder) attribute, containing a hint to the user of what can be entered in the control. The placeholder text must not contain carriage returns or line-feeds. This attribute only applies when the value of the [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) attribute is `text`, `search`, `tel`, `url` or `email`.

[readOnly](/en-US/docs/Web/API/HTMLInputElement/readOnly)

A boolean that represents the element's [readonly](/en-US/docs/Web/HTML/Reference/Elements/input#readonly) attribute, indicating that the user cannot modify the value of the control. This is ignored if the [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) is `hidden`, `range`, `color`, `checkbox`, `radio`, `file`, or a button type.

[selectionDirection](/en-US/docs/Web/API/HTMLInputElement/selectionDirection)

A string that represents the direction in which selection occurred. Possible values are: `forward` (the selection was performed in the start-to-end direction of the current locale), `backward` (the opposite direction) or `none` (the direction is unknown).

[selectionEnd](/en-US/docs/Web/API/HTMLInputElement/selectionEnd)

A number that represents the end index of the selected text. When there's no selection, this returns the offset of the character immediately following the current text input cursor position.

[selectionStart](/en-US/docs/Web/API/HTMLInputElement/selectionStart)

A number that represents the beginning index of the selected text. When nothing is selected, this returns the position of the text input cursor (caret) inside of the [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element.

[size](/en-US/docs/Web/API/HTMLInputElement/size)

A number that represents the element's [size](/en-US/docs/Web/HTML/Reference/Elements/input#size) attribute, containing visual size of the control. This value is in pixels unless the value of [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) is `text` or `password`, in which case, it is an integer number of characters. Applies only when [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) is set to `text`, `search`, `tel`, `url`, `email`, or `password`.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[checkValidity()](/en-US/docs/Web/API/HTMLInputElement/checkValidity)

Returns a boolean value that is `false` if the element is a candidate for constraint validation, and it does not satisfy its constraints. In this case, it also fires an [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) event at the element. It returns `true` if the element is not a candidate for constraint validation, or if it satisfies its constraints.

[reportValidity()](/en-US/docs/Web/API/HTMLInputElement/reportValidity)

Runs the `checkValidity()` method, and if it returns false (for an invalid input or no pattern attribute provided), then it reports to the user that the input is invalid in the same manner as if you submitted a form.

[select()](/en-US/docs/Web/API/HTMLInputElement/select)

Selects all the text in the input element, and focuses it so the user can subsequently replace all of its content.

[setCustomValidity()](/en-US/docs/Web/API/HTMLInputElement/setCustomValidity)

Sets a custom validity message for the element. If this message is not the empty string, then the element is suffering from a custom validity error, and does not validate.

[setRangeText()](/en-US/docs/Web/API/HTMLInputElement/setRangeText)

Replaces a range of text in the input element with new text.

[setSelectionRange()](/en-US/docs/Web/API/HTMLInputElement/setSelectionRange)

Selects a range of text in the input element (but does not focus it).

[showPicker()](/en-US/docs/Web/API/HTMLInputElement/showPicker)

Shows a browser picker for date, time, color, and files.

[stepDown()](/en-US/docs/Web/API/HTMLInputElement/stepDown)

Decrements the [value](/en-US/docs/Web/HTML/Reference/Elements/input#value) by ([step](/en-US/docs/Web/HTML/Reference/Elements/input#step) * n), where n defaults to 1 if not specified.

[stepUp()](/en-US/docs/Web/API/HTMLInputElement/stepUp)

Increments the [value](/en-US/docs/Web/HTML/Reference/Elements/input#value) by ([step](/en-US/docs/Web/HTML/Reference/Elements/input#step) * n), where n defaults to 1 if not specified.

## [Events](#events)

Also inherits events from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[cancel](/en-US/docs/Web/API/HTMLInputElement/cancel_event) event

Fired when the user cancels the file picker dialog via the Esc key or the cancel button and when the user re-selects the same files that were previously selected.

[invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) event

Fired when an element does not satisfy its constraints during constraint validation.

[search](/en-US/docs/Web/API/HTMLInputElement/search_event) event Non-standard

Fired when a search is initiated on an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) of `type="search"`.

[select](/en-US/docs/Web/API/HTMLInputElement/select_event) event

Fired when some text has been selected.

[selectionchange](/en-US/docs/Web/API/HTMLInputElement/selectionchange_event) event

Fires when the text selection in an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element has been changed.

## [Specifications](#specifications)

Specification
[HTML# htmlinputelement](https://html.spec.whatwg.org/multipage/input.html#htmlinputelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<input>](/en-US/docs/Web/HTML/Reference/Elements/input)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLInputElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlinputelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLInputElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlinputelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLInputElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlinputelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6d4ac4a04fd5c01adc690b9c95de3d9261570212%0A*+Document+last+modified%3A+2025-08-19T20%3A09%3A59.000Z%0A%0A%3C%2Fdetails%3E)
