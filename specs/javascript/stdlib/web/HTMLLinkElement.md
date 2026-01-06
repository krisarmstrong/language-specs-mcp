# HTMLLinkElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLLinkElement&level=high)

The `HTMLLinkElement` interface represents reference information for external resources and the relationship of those resources to a document and vice versa (corresponds to [<link>](/en-US/docs/Web/HTML/Reference/Elements/link) element; not to be confused with [<a>](/en-US/docs/Web/HTML/Reference/Elements/a), which is represented by [HTMLAnchorElement](/en-US/docs/Web/API/HTMLAnchorElement)). This object inherits all of the properties and methods of the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLLinkElement.as](/en-US/docs/Web/API/HTMLLinkElement/as)

A string representing the type of content being loaded by the HTML link when [rel="preload"](/en-US/docs/Web/HTML/Reference/Attributes/rel/preload) or [rel="modulepreload"](/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload).

[HTMLLinkElement.blocking](/en-US/docs/Web/API/HTMLLinkElement/blocking)

A string indicating that certain operations should be blocked on the fetching of an external resource. It reflects the `blocking` attribute of the [<link>](/en-US/docs/Web/HTML/Reference/Elements/link) element.

[HTMLLinkElement.crossOrigin](/en-US/docs/Web/API/HTMLLinkElement/crossOrigin)

A string that corresponds to the CORS setting for this link element. See [CORS settings attributes](/en-US/docs/Web/HTML/Reference/Attributes/crossorigin) for details.

[HTMLLinkElement.disabled](/en-US/docs/Web/API/HTMLLinkElement/disabled)

A boolean value which represents whether the link is disabled; currently only used with style sheet links.

[HTMLLinkElement.fetchPriority](/en-US/docs/Web/API/HTMLLinkElement/fetchPriority)

An optional string representing a hint given to the browser on how it should prioritize fetching of a preload relative to other resources of the same type. If this value is provided, it must be one of the possible permitted values: `high` to fetch at a higher priority, `low` to fetch at a lower priority, or `auto` to indicate no preference (which is the default).

[HTMLLinkElement.href](/en-US/docs/Web/API/HTMLLinkElement/href)

A string representing the URI for the target resource.

[HTMLLinkElement.hreflang](/en-US/docs/Web/API/HTMLLinkElement/hreflang)

A string representing the language code for the linked resource.

[HTMLLinkElement.imageSizes](/en-US/docs/Web/API/HTMLLinkElement/imageSizes)

A string reflecting the [imagesizes](/en-US/docs/Web/HTML/Reference/Elements/link#imagesizes) HTML attribute; a list of comma-separated image conditions and sizes.

[HTMLLinkElement.imageSrcset](/en-US/docs/Web/API/HTMLLinkElement/imageSrcset)

A string reflecting the [imagesrcset](/en-US/docs/Web/HTML/Reference/Elements/link#imagesrcset) HTML attribute; a comma-separated list of image candidate strings.

[HTMLLinkElement.integrity](/en-US/docs/Web/API/HTMLLinkElement/integrity)

A string that contains inline metadata that a browser can use to verify that a fetched resource has been delivered without unexpected manipulation. It reflects the `integrity` attribute of the [<link>](/en-US/docs/Web/HTML/Reference/Elements/link) element.

[HTMLLinkElement.media](/en-US/docs/Web/API/HTMLLinkElement/media)

A string representing a list of one or more media formats to which the resource applies. It reflects the `media` attribute of the [<link>](/en-US/docs/Web/HTML/Reference/Elements/link) element.

[HTMLLinkElement.referrerPolicy](/en-US/docs/Web/API/HTMLLinkElement/referrerPolicy)

A string that reflects the [referrerpolicy](/en-US/docs/Web/HTML/Reference/Elements/link#referrerpolicy) HTML attribute indicating which referrer to use.

[HTMLLinkElement.rel](/en-US/docs/Web/API/HTMLLinkElement/rel)

A string representing the forward relationship of the linked resource from the document to the resource.

[HTMLLinkElement.relList](/en-US/docs/Web/API/HTMLLinkElement/relList)Read only

A [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that reflects the [rel](/en-US/docs/Web/HTML/Reference/Elements/link#rel) HTML attribute, as a list of tokens.

[HTMLLinkElement.sizes](/en-US/docs/Web/API/HTMLLinkElement/sizes)Read only

A [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that reflects the [sizes](/en-US/docs/Web/HTML/Reference/Elements/link#sizes) HTML attribute, as a list of tokens.

[HTMLLinkElement.sheet](/en-US/docs/Web/API/HTMLLinkElement/sheet)Read only

Returns the [StyleSheet](/en-US/docs/Web/API/StyleSheet) object associated with the given element, or `null` if there is none.

[HTMLLinkElement.type](/en-US/docs/Web/API/HTMLLinkElement/type)

A string representing the MIME type of the linked resource.

### [Obsolete properties](#obsolete_properties)

`HTMLLinkElement.charset`Deprecated

A string representing the character encoding for the target resource.

`HTMLLinkElement.rev`Deprecated

A string representing the reverse relationship of the linked resource from the resource to the document.

Note: Currently the W3C HTML 5.2 spec states that `rev` is no longer obsolete, whereas the WHATWG living standard still has it labeled obsolete. Until this discrepancy is resolved, you should still assume it is obsolete.

`HTMLLinkElement.target`Deprecated

A string representing the name of the target frame to which the resource applies.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Specifications](#specifications)

Specification
[HTML# htmllinkelement](https://html.spec.whatwg.org/multipage/semantics.html#htmllinkelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<link>](/en-US/docs/Web/HTML/Reference/Elements/link).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLLinkElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmllinkelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLLinkElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmllinkelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLLinkElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmllinkelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
