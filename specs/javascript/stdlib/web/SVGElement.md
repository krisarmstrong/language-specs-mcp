# SVGElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGElement&level=high)

All of the SVG DOM interfaces that correspond directly to elements in the SVG language derive from the `SVGElement` interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from the [Element](/en-US/docs/Web/API/Element) interface.

[SVGElement.attributeStyleMap](/en-US/docs/Web/API/SVGElement/attributeStyleMap)Read only

A [StylePropertyMap](/en-US/docs/Web/API/StylePropertyMap) representing the declarations of the element's [style](/en-US/docs/Web/SVG/Reference/Attribute/style) attribute.

[SVGElement.autofocus](/en-US/docs/Web/API/SVGElement/autofocus)

Whether the control should be focused when the page loads, or when a [<dialog>](/en-US/docs/Web/HTML/Reference/Elements/dialog) or [popover](/en-US/docs/Web/HTML/Reference/Global_attributes/popover) become shown.

`SVGElement.className`DeprecatedRead only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) that reflects the value of the [class](/en-US/docs/Web/SVG/Reference/Attribute/class) attribute on the given element, or the empty string if `class` is not present. This attribute is deprecated and may be removed in a future version of this specification. Authors are advised to use [Element.classList](/en-US/docs/Web/API/Element/classList) instead.

[SVGElement.dataset](/en-US/docs/Web/API/SVGElement/dataset)Read only

A [DOMStringMap](/en-US/docs/Web/API/DOMStringMap) object which provides a list of key/value pairs of named data attributes which correspond to [custom data attributes](/en-US/docs/Web/HTML/How_to/Use_data_attributes) attached to the element. These can also be defined in SVG using attributes of the form [data-*](/en-US/docs/Web/SVG/Reference/Attribute/data-*), where `*` is the key name for the pair. This works just like HTML's [HTMLElement.dataset](/en-US/docs/Web/API/HTMLElement/dataset) property and HTML's [data-*](/en-US/docs/Web/HTML/Reference/Global_attributes/data-*) global attribute.

[SVGElement.nonce](/en-US/docs/Web/API/SVGElement/nonce)

Returns the cryptographic number used once that is used by Content Security Policy to determine whether a given fetch will be allowed to proceed.

[SVGElement.ownerSVGElement](/en-US/docs/Web/API/SVGElement/ownerSVGElement)Read only

An [SVGSVGElement](/en-US/docs/Web/API/SVGSVGElement) referring to the nearest ancestor [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element. `null` if the given element is the outermost `<svg>` element.

[SVGElement.style](/en-US/docs/Web/API/SVGElement/style)

A [CSSStyleDeclaration](/en-US/docs/Web/API/CSSStyleDeclaration) representing the declarations of the element's [style](/en-US/docs/Web/SVG/Reference/Attribute/style) attribute.

[SVGElement.tabIndex](/en-US/docs/Web/API/SVGElement/tabIndex)

The position of the element in the tabbing order.

[SVGElement.viewportElement](/en-US/docs/Web/API/SVGElement/viewportElement)Read only

The `SVGElement` which established the current viewport. Often the nearest ancestor [<svg>](/en-US/docs/Web/SVG/Reference/Element/svg) element. `null` if the given element is the outermost `<svg>` element.

## [Instance methods](#instance_methods)

This interface also inherits methods from [Element](/en-US/docs/Web/API/Element).

[SVGElement.blur()](/en-US/docs/Web/API/SVGElement/blur)

Removes keyboard focus from the currently focused element.

[SVGElement.focus()](/en-US/docs/Web/API/SVGElement/focus)

Makes the element the current keyboard focus.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the equivalent `on...` handler property.

`abort`

Fired when page loading is stopped before an SVG element has been allowed to load completely.

[error](/en-US/docs/Web/API/SVGElement/error_event)

Fired when an SVG element does not load properly or when an error occurs during script execution.

[load](/en-US/docs/Web/API/SVGElement/load_event)

Fires on an `SVGElement` when it is loaded in the browser.

`resize`

Fired when an SVG document is being resized.

`scroll`

Fired when an SVG document view is being shifted along the X and/or Y axes.

`unload`

Fired when the DOM implementation removes an SVG document from a window or frame.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGElement](https://svgwg.org/svg2-draft/types.html#InterfaceSVGElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML [data-*](/en-US/docs/Web/HTML/Reference/Global_attributes/data-*) attribute
- SVG [data-*](/en-US/docs/Web/SVG/Reference/Attribute/data-*) attribute
- [Using custom data attributes in HTML](/en-US/docs/Web/HTML/How_to/Use_data_attributes)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd701f10306c8b0b9690532ff808df826818a04f%0A*+Document+last+modified%3A+2025-04-23T12%3A54%3A33.000Z%0A%0A%3C%2Fdetails%3E)
