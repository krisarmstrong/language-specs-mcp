# Popover API

The Popover API provides developers with a standard, consistent, flexible mechanism for displaying popover content on top of other page content. Popover content can be controlled either using HTML attributes, or via JavaScript.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [HTML attributes](#html_attributes)
- [CSS features](#css_features)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

A very common pattern on the web is to show content over the top of other content, drawing the user's attention to specific important information or actions that need to be taken. This content can take several different names — overlays, popups, popovers, dialogs, etc. We will refer to them as popovers through the documentation. Generally speaking, these can be:

- modal, meaning that while a popover is being shown, the rest of the page is rendered non-interactive until the popover is actioned in some way (for example an important choice is made).
- non-modal, meaning that the rest of the page can be interacted with while the popover is being shown.

Popovers created using the Popover API are always non-modal. If you want to create a modal popover, a [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) element is the right way to go. There is significant overlap between the two — you might for example want to create a popover that persists, but control it using HTML. You can turn a `<dialog>` element into a popover (`<dialog popover>` is perfectly valid) if you want to combine popover control with dialog semantics.

Typical use cases for the popover API include user-interactive elements like action menus, custom "toast" notifications, form element suggestions, content pickers, or teaching UI.

You can create popovers in multiple ways:

- 

Via a set of new HTML attributes. A simple popover with a toggle button can be created using the following code:

html

```
<button popovertarget="mypopover">Toggle the popover</button>
<div id="mypopover" popover>Popover content</div>
```

- 

Via a JavaScript API. For example, [HTMLElement.togglePopover()](/en-US/docs/Web/API/HTMLElement/togglePopover) can be used to toggle a popover between shown and hidden.

The Popover API also provides events to react to a popover being toggled and CSS features to aid in styling popovers. See [Using the popover API](/en-US/docs/Web/API/Popover_API/Using) for a detailed guide to the API.

A related feature — interest invokers — can be used to show popovers on hover/focus, without requiring JavaScript. Check out [Using interest invokers](/en-US/docs/Web/API/Popover_API/Using_interest_invokers) to learn more.

## [HTML attributes](#html_attributes)

[interestfor](/en-US/docs/Web/HTML/Reference/Elements/button#interestfor)Experimental

Defines an HTML [<a>](/en-US/docs/Web/HTML/Reference/Elements/a), [<button>](/en-US/docs/Web/HTML/Reference/Elements/button), or [<area>](/en-US/docs/Web/HTML/Reference/Elements/area) element, or an SVG [<a>](/en-US/docs/Web/SVG/Reference/Element/a) element, as an interest invoker. Its value is the `id` of the target element, which will be affected in some way (normally shown or hidden) when interest is shown or lost on the invoker element.

[popover](/en-US/docs/Web/HTML/Reference/Global_attributes/popover)

A global attribute that turns an element into a popover element; takes a popover state (`"auto"`, `"hint"`, or `"manual"`) as its value.

[popovertarget](/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)

Turns a [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) or [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) element into a popover control button; takes the ID of the popover element to control as its value.

[popovertargetaction](/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction)

Specifies the action to be performed (`"hide"`, `"show"`, or `"toggle"`) on the popover element being controlled by a control [<button>](/en-US/docs/Web/HTML/Reference/Elements/button) or [<input>](/en-US/docs/Web/HTML/Reference/Elements/input).

## [CSS features](#css_features)

[::backdrop](/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)

The `::backdrop` pseudo-element is a full-screen element placed directly behind popover elements, allowing effects to be added to the page content behind the popover(s) if desired (for example blurring it out).

[interest-delay](/en-US/docs/Web/CSS/Reference/Properties/interest-delay), [interest-delay-start](/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start), and [interest-delay-end](/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)Experimental

The `interest-delay` shorthand property and its related `interest-delay-start` and `interest-delay-end` longhands can be used to add a delay between the user showing or losing interest and the browser acting on that change.

[:interest-source](/en-US/docs/Web/CSS/Reference/Selectors/:interest-source) and [:interest-target](/en-US/docs/Web/CSS/Reference/Selectors/:interest-target)

These selectors can be used to apply styles to the interest invoker and its associated target element, respectively, only when interest is indicated.

[:popover-open](/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)

The `:popover-open` pseudo-class matches a popover element only when it is in the showing state — it can be used to style popover elements when they are showing.

## [Interfaces](#interfaces)

[InterestEvent](/en-US/docs/Web/API/InterestEvent)Experimental

The event object for the [interest](/en-US/docs/Web/API/HTMLElement/interest_event) and [loseinterest](/en-US/docs/Web/API/HTMLElement/loseinterest_event) events. This includes a `source` property that contains a reference to the associated interest invoker element.

[ToggleEvent](/en-US/docs/Web/API/ToggleEvent)

Represents an event that fires when a popover element is toggled between being shown and hidden. It is the event object for the [beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event) and [toggle](/en-US/docs/Web/API/HTMLElement/toggle_event) events, which fire on popovers when their state changes.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

### [Instance properties](#instance_properties)

[interestForElement](/en-US/docs/Web/API/HTMLButtonElement/interestForElement)Experimental

Gets or sets a reference to the element being targeted by an interest invoker. If an HTML or SVG interest invoker references a target element in its `interestfor` attribute, that element will be referenced in the equivalent DOM object's `interestForElement` property. Available on the [HTMLButtonElement](/en-US/docs/Web/API/HTMLButtonElement), [HTMLAnchorElement](/en-US/docs/Web/API/HTMLAnchorElement), [HTMLAreaElement](/en-US/docs/Web/API/HTMLAreaElement), and [SVGAElement](/en-US/docs/Web/API/SVGAElement) interfaces.

[HTMLElement.popover](/en-US/docs/Web/API/HTMLElement/popover)

Gets and sets an element's popover state via JavaScript (`"auto"`, `"hint"`, or `"manual"`), and can be used for feature detection. Reflects the value of the [popover](/en-US/docs/Web/HTML/Reference/Global_attributes/popover) global HTML attribute.

[HTMLButtonElement.popoverTargetElement](/en-US/docs/Web/API/HTMLButtonElement/popoverTargetElement) and [HTMLInputElement.popoverTargetElement](/en-US/docs/Web/API/HTMLInputElement/popoverTargetElement)

Gets and sets the popover element being controlled by the control button. The JavaScript equivalent of the [popovertarget](/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget) HTML attribute.

[HTMLButtonElement.popoverTargetAction](/en-US/docs/Web/API/HTMLButtonElement/popoverTargetAction) and [HTMLInputElement.popoverTargetAction](/en-US/docs/Web/API/HTMLInputElement/popoverTargetAction)

Gets and sets the action to be performed (`"hide"`, `"show"`, or `"toggle"`) on the popover element being controlled by the control button. Reflects the value of the [popovertargetaction](/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction) HTML attribute.

### [Instance methods](#instance_methods)

[HTMLElement.hidePopover()](/en-US/docs/Web/API/HTMLElement/hidePopover)

Hides a popover element by removing it from the top layer and styling it with `display: none`.

[HTMLElement.showPopover()](/en-US/docs/Web/API/HTMLElement/showPopover)

Shows a popover element by adding it to the top layer.

[HTMLElement.togglePopover()](/en-US/docs/Web/API/HTMLElement/togglePopover)

Toggles a popover element between the showing and hidden states.

### [Events](#events)

[beforetoggle](/en-US/docs/Web/API/HTMLElement/beforetoggle_event) event

Fired just before a popover element's state changes between showing and hidden, or vice versa. Can be used to prevent a popover from opening, or to update other elements that need to be triggered by popover state.

[toggle](/en-US/docs/Web/API/HTMLElement/toggle_event) event

Fired just after a popover element's state changes between showing and hidden, or vice versa.

[interest](/en-US/docs/Web/API/HTMLElement/interest_event)Experimental

Fired on an interest invoker's target element when interest is shown, allowing code to be run in response.

[loseinterest](/en-US/docs/Web/API/HTMLElement/loseinterest_event)Experimental

Fired on an interest invoker's target element when interest is lost, allowing code to be run in response.

## [Examples](#examples)

- See our collection of [Popover API examples](https://mdn.github.io/dom-examples/popover-api/).
- See our collection of [interest invoker examples](https://mdn.github.io/dom-examples/interest-invokers/).

## [Specifications](#specifications)

Specification
[HTML# dom-popover](https://html.spec.whatwg.org/multipage/popover.html#dom-popover)
[HTML# event-beforetoggle](https://html.spec.whatwg.org/multipage/indices.html#event-beforetoggle)
[HTML# event-toggle](https://html.spec.whatwg.org/multipage/indices.html#event-toggle)

## [Browser compatibility](#browser_compatibility)

### [api.HTMLElement.popover](#api.HTMLElement.popover)

### [api.HTMLElement.beforetoggle_event.popover_elements](#api.HTMLElement.beforetoggle_event.popover_elements)

### [api.HTMLElement.toggle_event.popover_elements](#api.HTMLElement.toggle_event.popover_elements)

## [See also](#see_also)

- [popover](/en-US/docs/Web/HTML/Reference/Global_attributes/popover) HTML global attribute
- [popovertarget](/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget) HTML attribute
- [popovertargetaction](/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction) HTML attribute
- [::backdrop](/en-US/docs/Web/CSS/Reference/Selectors/::backdrop) CSS pseudo-element
- [:popover-open](/en-US/docs/Web/CSS/Reference/Selectors/:popover-open) CSS pseudo-class

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Popover_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/popover_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPopover_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpopover_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPopover_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpopover_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
