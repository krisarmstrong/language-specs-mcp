# HTMLAnchorElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAnchorElement&level=high)

The `HTMLAnchorElement` interface represents hyperlink elements and provides special properties and methods (beyond those of the regular [HTMLElement](/en-US/docs/Web/API/HTMLElement) object interface that they inherit from) for manipulating the layout and presentation of such elements. This interface corresponds to [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) element; not to be confused with [<link>](/en-US/docs/Web/HTML/Reference/Elements/link), which is represented by [HTMLLinkElement](/en-US/docs/Web/API/HTMLLinkElement).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLAnchorElement.attributionSrc](/en-US/docs/Web/API/HTMLAnchorElement/attributionSrc)Secure contextDeprecated

Gets and sets the [attributionsrc](/en-US/docs/Web/HTML/Reference/Elements/a#attributionsrc) attribute on an [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) element programmatically, reflecting the value of that attribute. `attributionsrc` specifies that you want the browser to send an [Attribution-Reporting-Eligible](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible) header. On the server-side this is used to trigger sending an [Attribution-Reporting-Register-Source](/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source) header in the response, to register a navigation-based attribution source.

[HTMLAnchorElement.download](/en-US/docs/Web/API/HTMLAnchorElement/download)

A string indicating that the linked resource is intended to be downloaded rather than displayed in the browser. The value represents the proposed name of the file. If the name is not a valid filename of the underlying OS, the browser will adapt it.

[HTMLAnchorElement.hash](/en-US/docs/Web/API/HTMLAnchorElement/hash)

A string representing the fragment identifier, including the leading hash mark (`#`), if any, in the referenced URL.

[HTMLAnchorElement.host](/en-US/docs/Web/API/HTMLAnchorElement/host)

A string representing the hostname and port (if it's not the default port) in the referenced URL.

[HTMLAnchorElement.hostname](/en-US/docs/Web/API/HTMLAnchorElement/hostname)

A string representing the hostname in the referenced URL.

[HTMLAnchorElement.href](/en-US/docs/Web/API/HTMLAnchorElement/href)

A string that is the result of parsing the [href](/en-US/docs/Web/HTML/Reference/Elements/a#href) HTML attribute relative to the document, containing a valid URL of a linked resource.

[HTMLAnchorElement.hreflang](/en-US/docs/Web/API/HTMLAnchorElement/hreflang)

A string that reflects the [hreflang](/en-US/docs/Web/HTML/Reference/Elements/a#hreflang) HTML attribute, indicating the language of the linked resource.

[HTMLAnchorElement.interestForElement](/en-US/docs/Web/API/HTMLAnchorElement/interestForElement)ExperimentalNon-standard

Gets or sets the target element of an interest invoker, in cases where the associated [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) element is specified as an [interest invoker](/en-US/docs/Web/API/Popover_API/Using_interest_invokers#creating_an_interest_invoker).

[HTMLAnchorElement.origin](/en-US/docs/Web/API/HTMLAnchorElement/origin)Read only

Returns a string containing the origin of the URL, that is its scheme, its domain and its port.

[HTMLAnchorElement.password](/en-US/docs/Web/API/HTMLAnchorElement/password)

A string containing the password specified before the domain name.

[HTMLAnchorElement.pathname](/en-US/docs/Web/API/HTMLAnchorElement/pathname)

A string containing an initial `/` followed by the path of the URL, not including the query string or fragment.

[HTMLAnchorElement.ping](/en-US/docs/Web/API/HTMLAnchorElement/ping)

A space-separated list of URLs. When the link is followed, the browser will send [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST) requests with the body PING to the URLs.

[HTMLAnchorElement.port](/en-US/docs/Web/API/HTMLAnchorElement/port)

A string representing the port component, if any, of the referenced URL.

[HTMLAnchorElement.protocol](/en-US/docs/Web/API/HTMLAnchorElement/protocol)

A string representing the protocol component, including trailing colon (`:`), of the referenced URL.

[HTMLAnchorElement.referrerPolicy](/en-US/docs/Web/API/HTMLAnchorElement/referrerPolicy)

A string that reflects the [referrerpolicy](/en-US/docs/Web/HTML/Reference/Elements/a#referrerpolicy) HTML attribute indicating which referrer to use.

[HTMLAnchorElement.rel](/en-US/docs/Web/API/HTMLAnchorElement/rel)

A string that reflects the [rel](/en-US/docs/Web/HTML/Reference/Elements/a#rel) HTML attribute, specifying the relationship of the target object to the linked object.

[HTMLAnchorElement.relList](/en-US/docs/Web/API/HTMLAnchorElement/relList)Read only

Returns a [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that reflects the [rel](/en-US/docs/Web/HTML/Reference/Elements/a#rel) HTML attribute, as a list of tokens.

[HTMLAnchorElement.search](/en-US/docs/Web/API/HTMLAnchorElement/search)

A string representing the search element, including leading question mark (`?`), if any, of the referenced URL.

[HTMLAnchorElement.target](/en-US/docs/Web/API/HTMLAnchorElement/target)

A string that reflects the [target](/en-US/docs/Web/HTML/Reference/Elements/a#target) HTML attribute, indicating where to display the linked resource.

[HTMLAnchorElement.text](/en-US/docs/Web/API/HTMLAnchorElement/text)

A string being a synonym for the [Node.textContent](/en-US/docs/Web/API/Node/textContent) property.

[HTMLAnchorElement.type](/en-US/docs/Web/API/HTMLAnchorElement/type)

A string that reflects the [type](/en-US/docs/Web/HTML/Reference/Elements/a#type) HTML attribute, indicating the MIME type of the linked resource.

[HTMLAnchorElement.username](/en-US/docs/Web/API/HTMLAnchorElement/username)

A string containing the username specified before the domain name.

### [Obsolete properties](#obsolete_properties)

[HTMLAnchorElement.charset 
Deprecated](#htmlanchorelement.charset)

A string representing the character encoding of the linked resource.

[HTMLAnchorElement.coords 
Deprecated](#htmlanchorelement.coords)

A string representing a comma-separated list of coordinates.

[HTMLAnchorElement.name 
Deprecated](#htmlanchorelement.name)

A string representing the anchor name.

[HTMLAnchorElement.rev 
Deprecated](#htmlanchorelement.rev)

A string representing that the [rev](/en-US/docs/Web/HTML/Reference/Elements/a#rev) HTML attribute, specifying the relationship of the link object to the target object.

[HTMLAnchorElement.shape 
Deprecated](#htmlanchorelement.shape)

A string representing the shape of the active area.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLAnchorElement.toString()](/en-US/docs/Web/API/HTMLAnchorElement/toString)

Returns a string containing the whole URL. It is a synonym for [HTMLAnchorElement.href](/en-US/docs/Web/API/HTMLAnchorElement/href), though it can't be used to modify the value.

## [Specifications](#specifications)

Specification
[HTML# htmlanchorelement](https://html.spec.whatwg.org/multipage/text-level-semantics.html#htmlanchorelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<a>](/en-US/docs/Web/HTML/Reference/Elements/a)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLAnchorElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlanchorelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAnchorElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlanchorelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAnchorElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlanchorelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe936e7271df947f25184a5ba8a21445bbd4d056c%0A*+Document+last+modified%3A+2025-12-13T02%3A55%3A18.000Z%0A%0A%3C%2Fdetails%3E)
