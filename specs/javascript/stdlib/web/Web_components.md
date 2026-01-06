# Web Components

Web Components is a suite of different technologies allowing you to create reusable custom elements — with their functionality encapsulated away from the rest of your code — and utilize them in your web apps.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Guides](#guides)
- [Reference](#reference)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

As developers, we all know that reusing code as much as possible is a good idea. This has traditionally not been so easy for custom markup structures — think of the complex HTML (and associated style and script) you've sometimes had to write to render custom UI controls, and how using them multiple times can turn your page into a mess if you are not careful.

Web Components aims to solve such problems — it consists of three main technologies, which can be used together to create versatile custom elements with encapsulated functionality that can be reused wherever you like without fear of code collisions.

[Custom elements](#custom_elements_2)

A set of JavaScript APIs that allow you to define custom elements and their behavior, which can then be used as desired in your user interface.

[Shadow DOM](#shadow_dom_2)

A set of JavaScript APIs for attaching an encapsulated "shadow" DOM tree to an element — which is rendered separately from the main document DOM — and controlling associated functionality. In this way, you can keep an element's features private, so they can be scripted and styled without the fear of collision with other parts of the document.

[HTML templates](#html_templates_2)

The [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) and [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) elements enable you to write markup templates that are not displayed in the rendered page. These can then be reused multiple times as the basis of a custom element's structure.

The basic approach for implementing a web component generally looks something like this:

1. Create a class in which you specify your web component functionality, using the [class](/en-US/docs/Web/JavaScript/Reference/Classes) syntax.
2. Register your new custom element using the [CustomElementRegistry.define()](/en-US/docs/Web/API/CustomElementRegistry/define) method, passing it the element name to be defined, the class or function in which its functionality is specified, and optionally, what element it inherits from.
3. If required, attach a shadow DOM to the custom element using [Element.attachShadow()](/en-US/docs/Web/API/Element/attachShadow) method. Add child elements, event listeners, etc., to the shadow DOM using regular DOM methods.
4. If required, define an HTML template using [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) and [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot). Again use regular DOM methods to clone the template and attach it to your shadow DOM.
5. Use your custom element wherever you like on your page, just like you would any regular HTML element.

## [Guides](#guides)

[Using custom elements](/en-US/docs/Web/API/Web_components/Using_custom_elements)

A guide showing how to use the features of custom elements to create simple web components, as well as looking into lifecycle callbacks and some other more advanced features.

[Using shadow DOM](/en-US/docs/Web/API/Web_components/Using_shadow_DOM)

A guide that looks at shadow DOM fundamentals, showing how to attach a shadow DOM to an element, add to the shadow DOM tree, style it, and more.

[Using templates and slots](/en-US/docs/Web/API/Web_components/Using_templates_and_slots)

A guide showing how to define a reusable HTML structure using [<template>](/en-US/docs/Web/HTML/Reference/Elements/template) and [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) elements, and then use that structure inside your web components.

## [Reference](#reference)

### [Custom elements](#custom_elements)

[CustomElementRegistry](/en-US/docs/Web/API/CustomElementRegistry)

Contains functionality related to custom elements, most notably the [CustomElementRegistry.define()](/en-US/docs/Web/API/CustomElementRegistry/define) method used to register new custom elements so they can then be used in your document.

[Window.customElements](/en-US/docs/Web/API/Window/customElements)

Returns a reference to the `CustomElementRegistry` object.

[Life cycle callbacks](/en-US/docs/Web/API/Web_components/Using_custom_elements#custom_element_lifecycle_callbacks)

Special callback functions defined inside the custom element's class definition, which affect its behavior:

[connectedCallback()](#connectedcallback)

Invoked when the custom element is first connected to the document's DOM.

[disconnectedCallback()](#disconnectedcallback)

Invoked when the custom element is disconnected from the document's DOM.

[adoptedCallback()](#adoptedcallback)

Invoked when the custom element is moved to a new document.

[attributeChangedCallback()](#attributechangedcallback)

Invoked when one of the custom element's attributes is added, removed, or changed.

[Extensions for creating customized built-in elements](#extensions_for_creating_customized_built-in_elements)

The following extensions are defined:

The [is](/en-US/docs/Web/HTML/Reference/Global_attributes/is) global HTML attribute

Allows you to specify that a standard HTML element should behave like a registered customized built-in element.

The "is" option of the [Document.createElement()](/en-US/docs/Web/API/Document/createElement) method

Allows you to create an instance of a standard HTML element that behaves like a given registered customized built-in element.

[CSS pseudo-classes](#css_pseudo-classes)

Pseudo-classes relating specifically to custom elements:

[:defined](/en-US/docs/Web/CSS/Reference/Selectors/:defined)

Matches any element that is defined, including built in elements and custom elements defined with `CustomElementRegistry.define()`.

[:host](/en-US/docs/Web/CSS/Reference/Selectors/:host)

Selects the shadow host of the [shadow DOM](/en-US/docs/Web/API/Web_components/Using_shadow_DOM) containing the CSS it is used inside.

[:host()](/en-US/docs/Web/CSS/Reference/Selectors/:host)

Selects the shadow host of the [shadow DOM](/en-US/docs/Web/API/Web_components/Using_shadow_DOM) containing the CSS it is used inside (so you can select a custom element from inside its shadow DOM) — but only if the selector given as the function's parameter matches the shadow host.

[:host-context()](/en-US/docs/Web/CSS/Reference/Selectors/:host-context)

Selects the shadow host of the [shadow DOM](/en-US/docs/Web/API/Web_components/Using_shadow_DOM) containing the CSS it is used inside (so you can select a custom element from inside its shadow DOM) — but only if the selector given as the function's parameter matches the shadow host's ancestor(s) in the place it sits inside the DOM hierarchy.

[:state()](/en-US/docs/Web/CSS/Reference/Selectors/:state)

Matches custom elements that are in a specified custom state. More precisely, it matches anonymous custom elements where the specified state is present in the element's [CustomStateSet](/en-US/docs/Web/API/CustomStateSet).

[CSS pseudo-elements](#css_pseudo-elements)

Pseudo-elements relating specifically to custom elements:

[::part](/en-US/docs/Web/CSS/Reference/Selectors/::part)

Represents any element within a [shadow tree](/en-US/docs/Web/API/Web_components/Using_shadow_DOM) that has a matching [part](/en-US/docs/Web/HTML/Reference/Global_attributes/part) attribute.

### [Shadow DOM](#shadow_dom)

[ShadowRoot](/en-US/docs/Web/API/ShadowRoot)

Represents the root node of a shadow DOM subtree.

[Element](/en-US/docs/Web/API/Element) extensions

Extensions to the `Element` interface related to shadow DOM:

- The [Element.attachShadow()](/en-US/docs/Web/API/Element/attachShadow) method attaches a shadow DOM tree to the specified element.
- The [Element.shadowRoot](/en-US/docs/Web/API/Element/shadowRoot) property returns the shadow root attached to the specified element, or `null` if there is no shadow root attached.

Relevant [Node](/en-US/docs/Web/API/Node) additions

Additions to the `Node` interface relevant to shadow DOM:

- The [Node.getRootNode()](/en-US/docs/Web/API/Node/getRootNode) method returns the context object's root, which optionally includes the shadow root if it is available.
- The [Node.isConnected](/en-US/docs/Web/API/Node/isConnected) property returns a boolean indicating whether or not the Node is connected (directly or indirectly) to the context object, e.g., the [Document](/en-US/docs/Web/API/Document) object in the case of the normal DOM, or the [ShadowRoot](/en-US/docs/Web/API/ShadowRoot) in the case of a shadow DOM.

[Event](/en-US/docs/Web/API/Event) extensions

Extensions to the `Event` interface related to shadow DOM:

[Event.composed](/en-US/docs/Web/API/Event/composed)

Returns `true` if the event will propagate across the shadow DOM boundary into the standard DOM, otherwise `false`.

[Event.composedPath](/en-US/docs/Web/API/Event/composedPath)

Returns the event's path (objects on which listeners will be invoked). This does not include nodes in shadow trees if the shadow root was created with [ShadowRoot.mode](/en-US/docs/Web/API/ShadowRoot/mode) closed.

### [HTML templates](#html_templates)

[<template>](/en-US/docs/Web/HTML/Reference/Elements/template)

Contains an HTML fragment that is not rendered when a containing document is initially loaded, but can be displayed at runtime using JavaScript, mainly used as the basis of custom element structures. The associated DOM interface is [HTMLTemplateElement](/en-US/docs/Web/API/HTMLTemplateElement).

[<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot)

A placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together. The associated DOM interface is [HTMLSlotElement](/en-US/docs/Web/API/HTMLSlotElement).

The [slot](/en-US/docs/Web/HTML/Reference/Global_attributes/slot) global HTML attribute

Assigns a slot in a shadow DOM shadow tree to an element.

[Element.assignedSlot](/en-US/docs/Web/API/Element/assignedSlot)

A read-only attribute which returns a reference to the [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) in which this element is inserted.

[Text.assignedSlot](/en-US/docs/Web/API/Text/assignedSlot)

A read-only attribute which returns a reference to the [<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) in which this text node is inserted.

[Element](/en-US/docs/Web/API/Element) extensions

Extensions to the `Element` interface related to slots:

[Element.slot](/en-US/docs/Web/API/Element/slot)

Returns the name of the shadow DOM slot attached to the element.

[CSS pseudo-elements](#css_pseudo-elements_2)

Pseudo-elements relating specifically to slots:

[::slotted](/en-US/docs/Web/CSS/Reference/Selectors/::slotted)

Matches any content that is inserted into a slot.

The [slotchange](/en-US/docs/Web/API/HTMLSlotElement/slotchange_event) event

Fired on an [HTMLSlotElement](/en-US/docs/Web/API/HTMLSlotElement) instance ([<slot>](/en-US/docs/Web/HTML/Reference/Elements/slot) element) when the node(s) contained in that slot change.

## [Examples](#examples)

We are building up a number of examples in our [web-components-examples](https://github.com/mdn/web-components-examples) GitHub repo. More will be added as time goes on.

## [Specifications](#specifications)

Specification
[HTML# the-template-element](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element)
[DOM# interface-shadowroot](https://dom.spec.whatwg.org/#interface-shadowroot)

## [Browser compatibility](#browser_compatibility)

### [html.elements.template](#html.elements.template)

### [api.ShadowRoot](#api.ShadowRoot)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_components/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_components/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_components&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_components%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_components%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_components%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f5609d323467cd08eeaddc57e4490a02be1889%0A*+Document+last+modified%3A+2025-09-08T23%3A24%3A30.000Z%0A%0A%3C%2Fdetails%3E)
