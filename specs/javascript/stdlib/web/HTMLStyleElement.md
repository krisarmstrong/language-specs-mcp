# HTMLStyleElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLStyleElement&level=high)

The `HTMLStyleElement` interface represents a [<style>](/en-US/docs/Web/HTML/Reference/Elements/style) element. It inherits properties and methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

This interface doesn't allow to manipulate the CSS it contains (in most case). To manipulate CSS, see [Using dynamic styling information](/en-US/docs/Web/API/CSS_Object_Model/Using_dynamic_styling_information) for an overview of the objects used to manipulate specified CSS properties using the DOM.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLStyleElement.blocking](/en-US/docs/Web/API/HTMLStyleElement/blocking)

A string indicating that certain operations should be blocked on the fetching of critical subresources. It reflects the `blocking` attribute of the [<style>](/en-US/docs/Web/HTML/Reference/Elements/style) element.

[HTMLStyleElement.media](/en-US/docs/Web/API/HTMLStyleElement/media)

A string reflecting the HTML attribute representing the intended destination medium for style information.

[HTMLStyleElement.type](/en-US/docs/Web/API/HTMLStyleElement/type)Deprecated

A string reflecting the HTML attribute representing the type of style being applied by this statement.

[HTMLStyleElement.disabled](/en-US/docs/Web/API/HTMLStyleElement/disabled)

A boolean value indicating whether or not the associated stylesheet is disabled.

[HTMLStyleElement.sheet](/en-US/docs/Web/API/HTMLStyleElement/sheet)Read only

Returns the [CSSStyleSheet](/en-US/docs/Web/API/CSSStyleSheet) object associated with the given element, or `null` if there is none.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmlstyleelement](https://html.spec.whatwg.org/multipage/semantics.html#htmlstyleelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<style>](/en-US/docs/Web/HTML/Reference/Elements/style).
- [Using dynamic styling information](/en-US/docs/Web/API/CSS_Object_Model/Using_dynamic_styling_information) to see how to manipulate CSS.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLStyleElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlstyleelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLStyleElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlstyleelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLStyleElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlstyleelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7cd4706990ab95794415aee05ba0a9662e742a17%0A*+Document+last+modified%3A+2024-11-07T15%3A33%3A32.000Z%0A%0A%3C%2Fdetails%3E)
