# SVGAElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAElement&level=high)

The `SVGAElement` interface provides access to the properties of an [<a>](/en-US/docs/Web/SVG/Reference/Element/a) element, as well as methods to manipulate them.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

[SVGAElement.download](/en-US/docs/Web/API/SVGAElement/download)

A string indicating that the linked resource is intended to be downloaded rather than displayed in the browser.

[SVGAElement.hash](/en-US/docs/Web/API/SVGAElement/hash)

A string representing the fragment identifier, including the leading hash mark (`#`), if any, in the referenced URL.

[SVGAElement.host](/en-US/docs/Web/API/SVGAElement/host)

A string representing the hostname and port (if it's not the default port) in the referenced URL.

[SVGAElement.hostname](/en-US/docs/Web/API/SVGAElement/hostname)

A string representing the hostname in the referenced URL.

[SVGAElement.href](/en-US/docs/Web/API/SVGAElement/href)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) that reflects the [href](/en-US/docs/Web/SVG/Reference/Attribute/href) or [xlink:href](/en-US/docs/Web/SVG/Reference/Attribute/xlink:href)Deprecated attribute.

[SVGAElement.hreflang](/en-US/docs/Web/API/SVGAElement/hreflang)

A string indicating the language of the linked resource.

[SVGAElement.interestForElement](/en-US/docs/Web/API/SVGAElement/interestForElement)ExperimentalNon-standard

Gets or sets the target element of an [interest invoker](/en-US/docs/Web/API/Popover_API/Using_interest_invokers#creating_an_interest_invoker), in cases where the associated [<a>](/en-US/docs/Web/SVG/Reference/Element/a) element is specified as an interest invoker.

[SVGAElement.origin](/en-US/docs/Web/API/SVGAElement/origin)Read only

Returns a string containing the origin of the URL — that is, its scheme, its domain and its port.

[SVGAElement.pathname](/en-US/docs/Web/API/SVGAElement/pathname)

A string containing an initial `/` followed by the path of the URL, not including the query string or fragment.

[SVGAElement.password](/en-US/docs/Web/API/SVGAElement/password)

A string containing the password specified before the domain name.

[SVGAElement.ping](/en-US/docs/Web/API/SVGAElement/ping)

A string that reflects the `ping` attribute, containing a space-separated list of URLs to which, when the hyperlink is followed, [POST](/en-US/docs/Web/HTTP/Reference/Methods/POST) requests with the body `PING` will be sent by the browser (in the background). Typically used for tracking.

[SVGAElement.port](/en-US/docs/Web/API/SVGAElement/port)

A string representing the port component, if any, of the referenced URL.

[SVGAElement.protocol](/en-US/docs/Web/API/SVGAElement/protocol)

A string representing the protocol component, including trailing colon (`:`), of the referenced URL.

[SVGAElement.referrerPolicy](/en-US/docs/Web/API/SVGAElement/referrerpolicy)

A string specifying which [referrer](/en-US/docs/Web/HTTP/Reference/Headers/Referer) to send when fetching the [URL](/en-US/docs/Glossary/URL).

[SVGAElement.rel](/en-US/docs/Web/API/SVGAElement/rel)

A string reflecting the `rel` SVG attribute, specifying the relationship of the link's target.

[SVGAElement.relList](/en-US/docs/Web/API/SVGAElement/relList)

A [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) reflecting the `rel` SVG attribute, as a list of tokens.

[SVGAElement.search](/en-US/docs/Web/API/SVGAElement/search)

A string representing the URL's query string, if any, including the leading question mark (`?`).

[SVGAElement.target](/en-US/docs/Web/API/SVGAElement/target)Read only

It corresponds to the [target](/en-US/docs/Web/SVG/Reference/Attribute/target) attribute of the given element.

[SVGAElement.text](/en-US/docs/Web/API/SVGAElement/text)Deprecated

A string that is a synonym for the [Node.textContent](/en-US/docs/Web/API/Node/textContent) property.

[SVGAElement.type](/en-US/docs/Web/API/SVGAElement/type)

A string that reflects the `type` attribute, indicating the MIME type of the linked resource.

[SVGAElement.username](/en-US/docs/Web/API/SVGAElement/username)

A string containing the username specified before the domain name.

## [Instance methods](#instance_methods)

This interface has no methods but inherits methods from its parent, [SVGGraphicsElement](/en-US/docs/Web/API/SVGGraphicsElement).

## [Example](#example)

In the example below, the [target](/en-US/docs/Web/SVG/Reference/Attribute/target) attribute of the [<a>](/en-US/docs/Web/SVG/Reference/Element/a) element is set to `_blank` and when the link is clicked, it logs to notify whether the condition is met or not.

js

```
const linkRef = document.querySelector("a");
linkRef.target = "_self";

linkRef.onclick = () => {
  if (linkRef.target === "_blank") {
    console.log("BLANK!");
    linkRef.target = "_self";
  } else {
    console.log("SORRY! not _blank");
  }
};
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGAElement](https://svgwg.org/svg2-draft/linking.html#InterfaceSVGAElement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- SVG [<a>](/en-US/docs/Web/SVG/Reference/Element/a) element

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGAElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgaelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgaelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgaelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
