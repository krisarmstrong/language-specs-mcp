# HTMLElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement&level=high)

The `HTMLElement` interface represents any [HTML](/en-US/docs/Web/HTML) element. Some elements directly implement this interface, while others implement it via an interface that inherits it.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [Element](/en-US/docs/Web/API/Element).

[HTMLElement.accessKey](/en-US/docs/Web/API/HTMLElement/accessKey)

A string representing the access key assigned to the element.

[HTMLElement.accessKeyLabel](/en-US/docs/Web/API/HTMLElement/accessKeyLabel)Read only

Returns a string containing the element's assigned access key.

[HTMLElement.anchorElement](/en-US/docs/Web/API/HTMLElement/anchorElement)Read onlyNon-standardExperimental

Returns a reference to the element's anchor element, or `null` if it doesn't have one.

[HTMLElement.attributeStyleMap](/en-US/docs/Web/API/HTMLElement/attributeStyleMap)Read only

A [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap) representing the declarations of the element's [style](/en-US/docs/Web/HTML/Reference/Global_attributes/style) attribute.

[HTMLElement.autocapitalize](/en-US/docs/Web/API/HTMLElement/autocapitalize)

A string that represents the element's capitalization behavior for user input. Valid values are: `none`, `off`, `on`, `characters`, `words`, `sentences`.

[HTMLElement.autofocus](/en-US/docs/Web/API/HTMLElement/autofocus)

A boolean value reflecting the [autofocus](/en-US/docs/Web/HTML/Reference/Elements/select#autofocus) HTML global attribute, which indicates whether the control should be focused when the page loads, or when dialog or popover become shown if specified in an element inside [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) elements or elements whose popover attribute is set.

[HTMLElement.autocorrect](/en-US/docs/Web/API/HTMLElement/autocorrect)

A boolean that represents whether or not text input by a user should be automatically corrected. This reflects the [autocorrect](/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect) HTML global attribute.

[HTMLElement.contentEditable](/en-US/docs/Web/API/HTMLElement/contentEditable)

A string, where a value of `true` means the element is editable and a value of `false` means it isn't.

[HTMLElement.dataset](/en-US/docs/Web/API/HTMLElement/dataset)Read only

Returns a [DOMStringMap](/en-US/docs/Web/API/DOMStringMap) with which script can read and write the element's [custom data attributes](/en-US/docs/Web/HTML/How_to/Use_data_attributes) (`data-*`).

[HTMLElement.dir](/en-US/docs/Web/API/HTMLElement/dir)

A string, reflecting the `dir` global attribute, representing the directionality of the element. Possible values are `"ltr"`, `"rtl"`, and `"auto"`.

[HTMLElement.draggable](/en-US/docs/Web/API/HTMLElement/draggable)

A boolean value indicating if the element can be dragged.

[HTMLElement.editContext](/en-US/docs/Web/API/HTMLElement/editContext)Experimental

Returns the [EditContext](/en-US/docs/Web/API/EditContext) associated with the element, or `null` if there isn't one.

[HTMLElement.enterKeyHint](/en-US/docs/Web/API/HTMLElement/enterKeyHint)

A string defining what action label (or icon) to present for the enter key on virtual keyboards.

[HTMLElement.hidden](/en-US/docs/Web/API/HTMLElement/hidden)

A string or boolean value reflecting the value of the element's [hidden](/en-US/docs/Web/HTML/Reference/Global_attributes/hidden) attribute.

[HTMLElement.inert](/en-US/docs/Web/API/HTMLElement/inert)

A boolean value indicating whether the user agent must act as though the given node is absent for the purposes of user interaction events, in-page text searches ("find in page"), and text selection.

[HTMLElement.innerText](/en-US/docs/Web/API/HTMLElement/innerText)

Represents the rendered text content of a node and its descendants. As a getter, it approximates the text the user would get if they highlighted the contents of the element with the cursor and then copied it to the clipboard. As a setter, it replaces the content inside the selected element, converting any line breaks into [<br>](/en-US/docs/Web/HTML/Reference/Elements/br) elements.

[HTMLElement.inputMode](/en-US/docs/Web/API/HTMLElement/inputMode)

A string value reflecting the value of the element's [inputmode](/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode) attribute.

[HTMLElement.isContentEditable](/en-US/docs/Web/API/HTMLElement/isContentEditable)Read only

Returns a boolean value indicating whether or not the content of the element can be edited.

[HTMLElement.lang](/en-US/docs/Web/API/HTMLElement/lang)

A string representing the language of an element's attributes, text, and element contents.

[HTMLElement.nonce](/en-US/docs/Web/API/HTMLElement/nonce)

Returns the cryptographic number used once that is used by Content Security Policy to determine whether a given fetch will be allowed to proceed.

[HTMLElement.offsetHeight](/en-US/docs/Web/API/HTMLElement/offsetHeight)Read only

Returns a `double` containing the height of an element, relative to the layout.

[HTMLElement.offsetLeft](/en-US/docs/Web/API/HTMLElement/offsetLeft)Read only

Returns a `double`, the distance from this element's left border to its `offsetParent`'s left border.

[HTMLElement.offsetParent](/en-US/docs/Web/API/HTMLElement/offsetParent)Read only

An [Element](/en-US/docs/Web/API/Element) that is the element from which all offset calculations are currently computed.

[HTMLElement.offsetTop](/en-US/docs/Web/API/HTMLElement/offsetTop)Read only

Returns a `double`, the distance from this element's top border to its `offsetParent`'s top border.

[HTMLElement.offsetWidth](/en-US/docs/Web/API/HTMLElement/offsetWidth)Read only

Returns a `double` containing the width of an element, relative to the layout.

[HTMLElement.outerText](/en-US/docs/Web/API/HTMLElement/outerText)

Represents the rendered text content of a node and its descendants. As a getter, it is the same as [HTMLElement.innerText](/en-US/docs/Web/API/HTMLElement/innerText) (it represents the rendered text content of an element and its descendants). As a setter, it replaces the selected node and its contents with the given value, converting any line breaks into [<br>](/en-US/docs/Web/HTML/Reference/Elements/br) elements.

[HTMLElement.popover](/en-US/docs/Web/API/HTMLElement/popover)

Gets and sets an element's popover state via JavaScript (`"auto"`, `"hint"`, or `"manual"`), and can be used for feature detection. Reflects the value of the [popover](/en-US/docs/Web/HTML/Reference/Global_attributes/popover) global HTML attribute.

[HTMLElement.spellcheck](/en-US/docs/Web/API/HTMLElement/spellcheck)

A boolean value that controls the [spell-checking](/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck) hint. It is available on all HTML elements, though it doesn't affect all of them.

[HTMLElement.style](/en-US/docs/Web/API/HTMLElement/style)

A [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration) representing the declarations of the element's [style](/en-US/docs/Web/HTML/Reference/Global_attributes/style) attribute.

[HTMLElement.tabIndex](/en-US/docs/Web/API/HTMLElement/tabIndex)

A `long` representing the position of the element in the tabbing order.

[HTMLElement.title](/en-US/docs/Web/API/HTMLElement/title)

A string containing the text that appears in a popup box when mouse is over the element.

[HTMLElement.translate](/en-US/docs/Web/API/HTMLElement/translate)

A boolean value representing the translation.

[HTMLElement.virtualKeyboardPolicy](/en-US/docs/Web/API/HTMLElement/virtualKeyboardPolicy)Experimental

A string indicating the on-screen virtual keyboard behavior on devices such as tablets, mobile phones, or other devices where a hardware keyboard may not be available, if the element's content is editable (for example, it is an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) or [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) element, or an element with the [contenteditable](/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable) attribute set).

[HTMLElement.writingSuggestions](/en-US/docs/Web/API/HTMLElement/writingSuggestions)

A string indicating if browser-provided writing suggestions should be enabled under the scope of the element or not.

## [Instance methods](#instance_methods)

Also inherits methods from its parent, [Element](/en-US/docs/Web/API/Element).

[HTMLElement.attachInternals()](/en-US/docs/Web/API/HTMLElement/attachInternals)

Returns an [ElementInternals](/en-US/docs/Web/API/ElementInternals) object, and enables a custom element to participate in HTML forms.

[HTMLElement.blur()](/en-US/docs/Web/API/HTMLElement/blur)

Removes keyboard focus from the currently focused element.

[HTMLElement.click()](/en-US/docs/Web/API/HTMLElement/click)

Sends a mouse click event to the element.

[HTMLElement.focus()](/en-US/docs/Web/API/HTMLElement/focus)

Makes the element the current keyboard focus.

[HTMLElement.hidePopover()](/en-US/docs/Web/API/HTMLElement/hidePopover)

Hides a popover element by removing it from the [top layer](/en-US/docs/Glossary/Top_layer) and styling it with `display: none`.

[HTMLElement.showPopover()](/en-US/docs/Web/API/HTMLElement/showPopover)

Shows a popover element by adding it to the [top layer](/en-US/docs/Glossary/Top_layer) and removing `display: none;` from its styles.

[HTMLElement.togglePopover()](/en-US/docs/Web/API/HTMLElement/togglePopover)

Toggles a popover element between the hidden and showing states.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

Also, inherits events from its parent, [Element](/en-US/docs/Web/API/Element).

[change](/en-US/docs/Web/API/HTMLElement/change_event)

Fired when the `value` of an [<input>](/en-US/docs/Web/HTML/Reference/Elements/input), [<select>](/en-US/docs/Web/HTML/Reference/Elements/select), or [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) element has been changed and committed by the user. Unlike the [input](/en-US/docs/Web/API/Element/input_event) event, the `change` event is not necessarily fired for each alteration to an element's `value`.

[command](/en-US/docs/Web/API/HTMLElement/command_event)

Fires on an element that is controlled via a [button](/en-US/docs/Web/API/HTMLButtonElement) with valid [commandForElement](/en-US/docs/Web/API/HTMLButtonElement/commandForElement) and [command](/en-US/docs/Web/API/HTMLButtonElement/command) values, whenever the button is interacted with (e.g., it is clicked).

[error](/en-US/docs/Web/API/HTMLElement/error_event)

Fired when a resource failed to load, or can't be used.

[load](/en-US/docs/Web/API/HTMLElement/load_event)

Fires for elements containing a resource when the resource has successfully loaded.

### [Drag & drop events](#drag_drop_events)

[drag](/en-US/docs/Web/API/HTMLElement/drag_event)

This event is fired when an element or text selection is being dragged.

[dragend](/en-US/docs/Web/API/HTMLElement/dragend_event)

This event is fired when a drag operation is being ended (by releasing a mouse button or hitting the escape key).

[dragenter](/en-US/docs/Web/API/HTMLElement/dragenter_event)

This event is fired when a dragged element or text selection enters a valid drop target.

[dragleave](/en-US/docs/Web/API/HTMLElement/dragleave_event)

This event is fired when a dragged element or text selection leaves a valid drop target.

[dragover](/en-US/docs/Web/API/HTMLElement/dragover_event)

This event is fired continuously when an element or text selection is being dragged and the mouse pointer is over a valid drop target (every 50 ms WHEN mouse is not moving ELSE much faster between 5 ms (slow movement) and 1ms (fast movement) approximately. This firing pattern is different than [mouseover](/en-US/docs/Web/API/Element/mouseover_event) ).

[dragstart](/en-US/docs/Web/API/HTMLElement/dragstart_event)

This event is fired when the user starts dragging an element or text selection.

[drop](/en-US/docs/Web/API/HTMLElement/drop_event)

This event is fired when an element or text selection is dropped on a valid drop target.

### [Interest invoker events](#interest_invoker_events)

[interest](/en-US/docs/Web/API/HTMLElement/interest_event)ExperimentalNon-standard

Fired on the target element of an [interest invoker](/en-US/docs/Web/API/Popover_API/Using_interest_invokers) when interest is shown, allowing code to be run in response.

[loseinterest](/en-US/docs/Web/API/HTMLElement/loseinterest_event)ExperimentalNon-standard

Fired on the target element of an interest invoker when interest is lost, allowing code to be run in response.

### [Toggle events](#toggle_events)

[beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event)

Fired when the element is a [popover](/en-US/docs/Web/API/Popover_API) or [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog), before it is hidden or shown.

[toggle](/en-US/docs/Web/API/HTMLElement/toggle_event)

Fired when the element is a [popover](/en-US/docs/Web/API/Popover_API), [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog), or [<details>](/en-US/docs/Web/HTML/Reference/Elements/details) element, just after it is hidden or shown.

## [Specifications](#specifications)

Specification
[HTML# htmlelement](https://html.spec.whatwg.org/multipage/dom.html#htmlelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Element](/en-US/docs/Web/API/Element)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
