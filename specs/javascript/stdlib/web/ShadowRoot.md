# ShadowRoot

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FShadowRoot&level=high)

The `ShadowRoot` interface of the [Shadow DOM API](/en-US/docs/Web/API/Web_components/Using_shadow_DOM) is the root node of a DOM subtree that is rendered separately from a document's main DOM tree.

You can retrieve a reference to an element's shadow root using its [Element.shadowRoot](/en-US/docs/Web/API/Element/shadowRoot) property, provided it was created using [Element.attachShadow()](/en-US/docs/Web/API/Element/attachShadow) with the `mode` option set to `open`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[ShadowRoot.activeElement](/en-US/docs/Web/API/ShadowRoot/activeElement)Read only

Returns the [Element](/en-US/docs/Web/API/Element) within the shadow tree that has focus.

[ShadowRoot.adoptedStyleSheets](/en-US/docs/Web/API/ShadowRoot/adoptedStyleSheets)

Add an array of constructed stylesheets to be used by the shadow DOM subtree. These may be shared with other DOM subtrees that share the same parent [Document](/en-US/docs/Web/API/Document) node, and the document itself.

[ShadowRoot.clonable](/en-US/docs/Web/API/ShadowRoot/clonable)Read only

A boolean that indicates whether the shadow root is clonable.

[ShadowRoot.delegatesFocus](/en-US/docs/Web/API/ShadowRoot/delegatesFocus)Read only

A boolean that indicates whether the shadow root delegates focus if a non-focusable node is selected.

[ShadowRoot.fullscreenElement](/en-US/docs/Web/API/ShadowRoot/fullscreenElement)Read only

The element that's currently in full screen mode for this shadow tree.

[ShadowRoot.host](/en-US/docs/Web/API/ShadowRoot/host)Read only

Returns a reference to the DOM element the `ShadowRoot` is attached to.

[ShadowRoot.innerHTML](/en-US/docs/Web/API/ShadowRoot/innerHTML)

Sets or returns a reference to the DOM tree inside the `ShadowRoot`.

[ShadowRoot.mode](/en-US/docs/Web/API/ShadowRoot/mode)Read only

The mode of the `ShadowRoot`, either `open` or `closed`. This defines whether or not the shadow root's internal features are accessible from JavaScript.

[ShadowRoot.pictureInPictureElement](/en-US/docs/Web/API/ShadowRoot/pictureInPictureElement)Read only

Returns the [Element](/en-US/docs/Web/API/Element) within the shadow tree that is currently being presented in picture-in-picture mode.

[ShadowRoot.pointerLockElement](/en-US/docs/Web/API/ShadowRoot/pointerLockElement)Read only

Returns the [Element](/en-US/docs/Web/API/Element) set as the target for mouse events while the pointer is locked. `null` if lock is pending, pointer is unlocked, or if the target is in another tree.

[ShadowRoot.serializable](/en-US/docs/Web/API/ShadowRoot/serializable)Read only

A boolean that indicates whether the shadow root is serializable. A serializable shadow root inside an element will be serialized by [Element.getHTML()](/en-US/docs/Web/API/Element/getHTML) or [ShadowRoot.getHTML()](/en-US/docs/Web/API/ShadowRoot/getHTML) when its [options.serializableShadowRoots](/en-US/docs/Web/API/Element/getHTML#serializableshadowroots) parameter is set `true`. This is set when the shadow root is created.

[ShadowRoot.slotAssignment](/en-US/docs/Web/API/ShadowRoot/slotAssignment)Read only

Returns a string containing the type of slot assignment, either `manual` or `named`.

[ShadowRoot.styleSheets](/en-US/docs/Web/API/ShadowRoot/styleSheets)Read only

Returns a [StyleSheetList](/en-US/docs/Web/API/StyleSheetList) of [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) objects for stylesheets explicitly linked into, or embedded in a shadow tree.

## [Instance methods](#instance_methods)

[ShadowRoot.getAnimations()](/en-US/docs/Web/API/ShadowRoot/getAnimations)

Returns an array of all [Animation](/en-US/docs/Web/API/Animation) objects currently in effect, whose target elements are descendants of the shadow tree.

`ShadowRoot.getSelection()`Non-standard

Returns a [Selection](/en-US/docs/Web/API/Selection) object representing the range of text selected by the user, or the current position of the caret.

[ShadowRoot.elementFromPoint()](/en-US/docs/Web/API/ShadowRoot/elementFromPoint)Non-standard

Returns the topmost element at the specified coordinates.

[ShadowRoot.elementsFromPoint()](/en-US/docs/Web/API/ShadowRoot/elementsFromPoint)Non-standard

Returns an array of all elements at the specified coordinates.

[ShadowRoot.setHTML()](/en-US/docs/Web/API/ShadowRoot/setHTML)Experimental

Provides an XSS-safe method to parse and sanitize a string of HTML into a [DocumentFragment](/en-US/docs/Web/API/DocumentFragment), which then replaces the existing tree in the shadow DOM.

[ShadowRoot.setHTMLUnsafe()](/en-US/docs/Web/API/ShadowRoot/setHTMLUnsafe)

Parses a string of HTML into a document fragment, without sanitization, which then replaces the shadowroot's original subtree. The HTML string may include declarative shadow roots, which would be parsed as template elements the HTML was set using [ShadowRoot.innerHTML](/en-US/docs/Web/API/ShadowRoot/innerHTML).

## [Events](#events)

The following events are available to `ShadowRoot` via event bubbling from [HTMLSlotElement](/en-US/docs/Web/API/HTMLSlotElement):

`HTMLSlotElement`[slotchange](/en-US/docs/Web/API/HTMLSlotElement/slotchange_event) event

An event fired when the node(s) contained in that slot change.

## [Examples](#examples)

The following snippets are taken from our [life-cycle-callbacks](https://github.com/mdn/web-components-examples/tree/main/life-cycle-callbacks) example ([see it live also](https://mdn.github.io/web-components-examples/life-cycle-callbacks/)), which creates an element that displays a square of a size and color specified in the element's attributes.

Inside the `<custom-square>` element's class definition we include some life cycle callbacks that make a call to an external function, `updateStyle()`, which actually applies the size and color to the element. You'll see that we are passing it `this` (the custom element itself) as a parameter.

js

```
class Square extends HTMLElement {
  // …
  connectedCallback() {
    console.log("Custom square element added to page.");
    updateStyle(this);
  }

  attributeChangedCallback(name, oldValue, newValue) {
    console.log("Custom square element attributes changed.");
    updateStyle(this);
  }
  // …
}
```

In the `updateStyle()` function itself, we get a reference to the shadow DOM using [Element.shadowRoot](/en-US/docs/Web/API/Element/shadowRoot). From here we use standard DOM traversal techniques to find the [<style>](/en-US/docs/Web/HTML/Reference/Elements/style) element inside the shadow DOM and then update the CSS found inside it:

js

```
function updateStyle(elem) {
  const shadow = elem.shadowRoot;
  const childNodes = shadow.childNodes;
  for (const node of childNodes) {
    if (node.nodeName === "STYLE") {
      node.textContent = `
div {
  width: ${elem.getAttribute("l")}px;
  height: ${elem.getAttribute("l")}px;
  background-color: ${elem.getAttribute("c")};
}
      `;
    }
  }
}
```

## [Specifications](#specifications)

Specification
[DOM# interface-shadowroot](https://dom.spec.whatwg.org/#interface-shadowroot)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the shadow DOM](/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
- [Web components](/en-US/docs/Web/API/Web_components)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ShadowRoot/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/shadowroot/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FShadowRoot&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fshadowroot%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FShadowRoot%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fshadowroot%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F061611f4e4244587ee63436a987e51c3215596d3%0A*+Document+last+modified%3A+2025-10-27T10%3A29%3A07.000Z%0A%0A%3C%2Fdetails%3E)
