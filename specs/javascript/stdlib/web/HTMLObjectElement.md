# HTMLObjectElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLObjectElement&level=high)

The `HTMLObjectElement` interface provides special properties and methods (beyond those on the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) element, representing external resources.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

`HTMLObjectElement.align`Deprecated

A string representing an enumerated property indicating alignment of the element's contents with respect to the surrounding context. The possible values are `"left"`, `"right"`, `"justify"`, and `"center"`.

`HTMLObjectElement.archive`Deprecated

A string that reflects the [archive](/en-US/docs/Web/HTML/Reference/Elements/object#archive) HTML attribute, containing a list of archives for resources for this object.

`HTMLObjectElement.border`Deprecated

A string that reflects the [border](/en-US/docs/Web/HTML/Reference/Elements/object#border) HTML attribute, specifying the width of a border around the object.

`HTMLObjectElement.code`Deprecated

A string representing the name of an applet class file, containing either the applet's subclass, or the path to get to the class, including the class file itself.

`HTMLObjectElement.codeBase`Deprecated

A string that reflects the [codebase](/en-US/docs/Web/HTML/Reference/Elements/object#codebase) HTML attribute, specifying the base path to use to resolve relative URIs.

`HTMLObjectElement.codeType`Deprecated

A string that reflects the [codetype](/en-US/docs/Web/HTML/Reference/Elements/object#codetype) HTML attribute, specifying the content type of the data.

[HTMLObjectElement.contentDocument](/en-US/docs/Web/API/HTMLObjectElement/contentDocument)Read only

Returns a [Document](/en-US/docs/Web/API/Document) representing the active document of the object element's nested browsing context, if any; otherwise `null`.

[HTMLObjectElement.contentWindow](/en-US/docs/Web/API/HTMLObjectElement/contentWindow)Read only

Returns a [WindowProxy](/en-US/docs/Glossary/WindowProxy) representing the window proxy of the object element's nested browsing context, if any; otherwise `null`.

[HTMLObjectElement.data](/en-US/docs/Web/API/HTMLObjectElement/data)

Returns a string that reflects the [data](/en-US/docs/Web/HTML/Reference/Elements/object#data) HTML attribute, specifying the address of a resource's data.

`HTMLObjectElement.declare`Deprecated

A boolean value that reflects the [declare](/en-US/docs/Web/HTML/Reference/Elements/object#declare) HTML attribute, indicating that this is a declaration, not an instantiation, of the object.

[HTMLObjectElement.form](/en-US/docs/Web/API/HTMLObjectElement/form)Read only

Returns a [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) representing the object element's form owner, or null if there isn't one.

[HTMLObjectElement.height](/en-US/docs/Web/API/HTMLObjectElement/height)

Returns a string that reflects the [height](/en-US/docs/Web/HTML/Reference/Elements/object#height) HTML attribute, specifying the displayed height of the resource in CSS pixels.

`HTMLObjectElement.hspace`Deprecated

A `long` representing the horizontal space in pixels around the control.

[HTMLObjectElement.name](/en-US/docs/Web/API/HTMLObjectElement/name)

Returns a string that reflects the [name](/en-US/docs/Web/HTML/Reference/Elements/object#name) HTML attribute, specifying the name of the browsing context.

`HTMLObjectElement.standby`Deprecated

A string that reflects the [standby](/en-US/docs/Web/HTML/Reference/Elements/object#standby) HTML attribute, specifying a message to display while the object loads.

[HTMLObjectElement.type](/en-US/docs/Web/API/HTMLObjectElement/type)

A string that reflects the [type](/en-US/docs/Web/HTML/Reference/Elements/object#type) HTML attribute, specifying the MIME type of the resource.

[HTMLObjectElement.useMap](/en-US/docs/Web/API/HTMLObjectElement/useMap)Deprecated

A string that reflects the [usemap](/en-US/docs/Web/HTML/Reference/Elements/object#usemap) HTML attribute, specifying a [<map>](/en-US/docs/Web/HTML/Reference/Elements/map) element to use.

[HTMLObjectElement.validationMessage](/en-US/docs/Web/API/HTMLObjectElement/validationMessage)Read only

Returns a string representing a localized message that describes the validation constraints that the control does not satisfy (if any). This is the empty string if the control is not a candidate for constraint validation (`willValidate` is `false`), or it satisfies its constraints.

[HTMLObjectElement.validity](/en-US/docs/Web/API/HTMLObjectElement/validity)Read only

Returns a [ValidityState](/en-US/docs/Web/API/ValidityState) with the validity states that this element is in.

`HTMLObjectElement.vspace`Deprecated

A `long` representing the horizontal space in pixels around the control.

[HTMLObjectElement.width](/en-US/docs/Web/API/HTMLObjectElement/width)

A string that reflects the [width](/en-US/docs/Web/HTML/Reference/Elements/object#width) HTML attribute, specifying the displayed width of the resource in CSS pixels.

[HTMLObjectElement.willValidate](/en-US/docs/Web/API/HTMLObjectElement/willValidate)Read only

Returns a boolean value that indicates whether the element is a candidate for constraint validation. Always `false` for `HTMLObjectElement` objects.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLObjectElement.checkValidity()](/en-US/docs/Web/API/HTMLObjectElement/checkValidity)

Always returns `true` because [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) elements are never candidates for constraint validation.

[HTMLObjectElement.getSVGDocument()](/en-US/docs/Web/API/HTMLObjectElement/getSVGDocument)

Returns the embedded SVG as a [Document](/en-US/docs/Web/API/Document).

[HTMLObjectElement.reportValidity()](/en-US/docs/Web/API/HTMLObjectElement/reportValidity)

Always returns `true` because [<object>](/en-US/docs/Web/HTML/Reference/Elements/object) elements are never candidates for constraint validation.

[HTMLObjectElement.setCustomValidity()](/en-US/docs/Web/API/HTMLObjectElement/setCustomValidity)

Sets a custom validity message for the element. If this message is not the empty string, then the element is suffering from a custom validity error, and does not validate.

## [Specifications](#specifications)

Specification
[HTML# htmlobjectelement](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#htmlobjectelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<object>](/en-US/docs/Web/HTML/Reference/Elements/object)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLObjectElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlobjectelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLObjectElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlobjectelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLObjectElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlobjectelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
