# HTMLAreaElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAreaElement&level=high)

The `HTMLAreaElement` interface provides special properties and methods (beyond those of the regular object [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of [<area>](/en-US/docs/Web/HTML/Reference/Elements/area) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLAreaElement.alt](/en-US/docs/Web/API/HTMLAreaElement/alt)

A string that reflects the [alt](/en-US/docs/Web/HTML/Reference/Elements/area#alt) HTML attribute, containing alternative text for the element.

[HTMLAreaElement.coords](/en-US/docs/Web/API/HTMLAreaElement/coords)

A string that reflects the [coords](/en-US/docs/Web/HTML/Reference/Elements/area#coords) HTML attribute, containing coordinates to define the hot-spot region.

[HTMLAreaElement.download](/en-US/docs/Web/API/HTMLAreaElement/download)

A string indicating that the linked resource is intended to be downloaded rather than displayed in the browser. The value represent the proposed name of the file. If the name is not a valid filename of the underlying OS, browser will adjust it accordingly.

[HTMLAreaElement.hash](/en-US/docs/Web/API/HTMLAreaElement/hash)

A string containing the fragment identifier (including the leading hash mark (#)), if any, in the referenced URL.

[HTMLAreaElement.host](/en-US/docs/Web/API/HTMLAreaElement/host)

A string containing the hostname and port (if it's not the default port) in the referenced URL.

[HTMLAreaElement.hostname](/en-US/docs/Web/API/HTMLAreaElement/hostname)

A string containing the hostname in the referenced URL.

[HTMLAreaElement.href](/en-US/docs/Web/API/HTMLAreaElement/href)

A string containing that reflects the [href](/en-US/docs/Web/HTML/Reference/Elements/area#href) HTML attribute, containing a valid URL of a linked resource.

[HTMLAreaElement.interestForElement](/en-US/docs/Web/API/HTMLAreaElement/interestForElement)ExperimentalNon-standard

Gets or sets the target element of an interest invoker, in cases where the associated [<area>](/en-US/docs/Web/HTML/Reference/Elements/area) element is specified as an [interest invoker](/en-US/docs/Web/API/Popover_API/Using_interest_invokers#creating_an_interest_invoker).

`HTMLAreaElement.noHref`Deprecated

A boolean flag indicating if the area is inactive (`true`) or active (`false`).

[HTMLAreaElement.origin](/en-US/docs/Web/API/HTMLAreaElement/origin)Read only

Returns a string containing the origin of the URL, that is its scheme, its domain and its port.

[HTMLAreaElement.password](/en-US/docs/Web/API/HTMLAreaElement/password)

A string containing the password specified before the domain name.

[HTMLAreaElement.pathname](/en-US/docs/Web/API/HTMLAreaElement/pathname)

A string containing the path name component, if any, of the referenced URL.

[HTMLAreaElement.ping](/en-US/docs/Web/API/HTMLAreaElement/ping)

A space-separated list of URLs. When the link is followed, the browser will send [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST) requests with the body PING to the URLs.

[HTMLAreaElement.port](/en-US/docs/Web/API/HTMLAreaElement/port)

A string containing the port component, if any, of the referenced URL.

[HTMLAreaElement.protocol](/en-US/docs/Web/API/HTMLAreaElement/protocol)

A string containing the protocol component (including trailing colon `':'`), of the referenced URL.

[HTMLAreaElement.referrerPolicy](/en-US/docs/Web/API/HTMLAreaElement/referrerPolicy)

A string that reflects the [referrerpolicy](/en-US/docs/Web/HTML/Reference/Elements/area#referrerpolicy) HTML attribute indicating which referrer to use when fetching the linked resource.

[HTMLAreaElement.rel](/en-US/docs/Web/API/HTMLAreaElement/rel)

A string that reflects the [rel](/en-US/docs/Web/HTML/Reference/Elements/area#rel) HTML attribute, indicating relationships of the current document to the linked resource.

[HTMLAreaElement.relList](/en-US/docs/Web/API/HTMLAreaElement/relList)Read only

Returns a [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that reflects the [rel](/en-US/docs/Web/HTML/Reference/Elements/area#rel) HTML attribute, indicating relationships of the current document to the linked resource, as a list of tokens.

[HTMLAreaElement.search](/en-US/docs/Web/API/HTMLAreaElement/search)

A string containing the search element (including leading question mark `'?'`), if any, of the referenced URL.

[HTMLAreaElement.shape](/en-US/docs/Web/API/HTMLAreaElement/shape)

A string that reflects the [shape](/en-US/docs/Web/HTML/Reference/Elements/area#shape) HTML attribute, indicating the shape of the hot-spot, limited to known values.

[HTMLAreaElement.target](/en-US/docs/Web/API/HTMLAreaElement/target)

A string that reflects the [target](/en-US/docs/Web/HTML/Reference/Elements/area#target) HTML attribute, indicating the browsing context in which to open the linked resource.

[HTMLAreaElement.username](/en-US/docs/Web/API/HTMLAreaElement/username)

A string containing the username specified before the domain name.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLAreaElement.toString()](/en-US/docs/Web/API/HTMLAreaElement/toString)

Returns a string containing the whole URL. It is a synonym for [HTMLAreaElement.href](/en-US/docs/Web/API/HTMLAreaElement/href).

## [Specifications](#specifications)

Specification
[HTML# htmlareaelement](https://html.spec.whatwg.org/multipage/image-maps.html#htmlareaelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<area>](/en-US/docs/Web/HTML/Reference/Elements/area)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLAreaElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlareaelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAreaElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlareaelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAreaElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlareaelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
