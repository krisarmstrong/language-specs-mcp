# HTMLIFrameElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLIFrameElement&level=high)

The `HTMLIFrameElement` interface provides special properties and methods (beyond those of the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface it also has available to it by inheritance) for manipulating the layout and presentation of inline frame elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

`HTMLIFrameElement.align`Deprecated

A string that specifies the alignment of the frame with respect to the surrounding context.

[HTMLIFrameElement.allow](/en-US/docs/Web/API/HTMLIFrameElement/allow)

A string that indicates the [Permissions Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) specified for this `<iframe>`.

[HTMLIFrameElement.allowFullscreen](/en-US/docs/Web/API/HTMLIFrameElement/allowFullscreen)

A boolean value indicating whether the inline frame is willing to be placed into full screen mode. See [Using fullscreen mode](/en-US/docs/Web/API/Fullscreen_API) for details.

[HTMLIFrameElement.allowPaymentRequest](/en-US/docs/Web/API/HTMLIFrameElement/allowPaymentRequest)DeprecatedNon-standard

A boolean value indicating whether the [Payment Request API](/en-US/docs/Web/API/Payment_Request_API) may be invoked inside a cross-origin iframe.

[HTMLIFrameElement.browsingTopics](/en-US/docs/Web/API/HTMLIFrameElement/browsingTopics)Non-standardDeprecated

A boolean property specifying that the selected topics for the current user should be sent with the request for the associated [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)'s source. This reflects the `browsingtopics` content attribute value.

[HTMLIFrameElement.contentDocument](/en-US/docs/Web/API/HTMLIFrameElement/contentDocument)Read only

Returns a [Document](/en-US/docs/Web/API/Document), the active document in the inline frame's nested browsing context.

[HTMLIFrameElement.contentWindow](/en-US/docs/Web/API/HTMLIFrameElement/contentWindow)Read only

Returns a [WindowProxy](/en-US/docs/Glossary/WindowProxy), the window proxy for the nested browsing context.

[HTMLIFrameElement.credentialless](/en-US/docs/Web/API/HTMLIFrameElement/credentialless)Experimental

A boolean value indicating whether the `<iframe>` is credentialless, meaning that its content is loaded in a new, ephemeral context. This context does not have access to the parent context's shared storage and credentials. In return, the [Cross-Origin-Embedder-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy) (COEP) embedding rules can be lifted, so documents with COEP set can embed third-party documents that do not. See [IFrame credentialless](/en-US/docs/Web/HTTP/Guides/IFrame_credentialless) for a deeper explanation.

[HTMLIFrameElement.csp](/en-US/docs/Web/API/HTMLIFrameElement/csp)Experimental

Specifies the Content Security Policy that an embedded document must agree to enforce upon itself.

[HTMLIFrameElement.featurePolicy](/en-US/docs/Web/API/HTMLIFrameElement/featurePolicy)Read onlyExperimental

Returns the [FeaturePolicy](/en-US/docs/Web/API/FeaturePolicy) interface which provides a simple API for introspecting the [Permissions Policies](/en-US/docs/Web/HTTP/Guides/Permissions_Policy) applied to a specific document.

`HTMLIFrameElement.frameBorder`Deprecated

A string that indicates whether to create borders between frames.

[HTMLIFrameElement.height](/en-US/docs/Web/API/HTMLIFrameElement/height)

A string that reflects the [height](/en-US/docs/Web/HTML/Reference/Elements/iframe#height) HTML attribute, indicating the height of the frame.

[HTMLIFrameElement.loading](/en-US/docs/Web/API/HTMLIFrameElement/loading)

A string providing a hint to the browser that the iframe should be loaded immediately (`eager`) or on an as-needed basis (`lazy`). This reflects the [loading](/en-US/docs/Web/HTML/Reference/Elements/iframe#loading) HTML attribute.

`HTMLIFrameElement.longDesc`Deprecated

A string that contains the URI of a long description of the frame.

`HTMLIFrameElement.marginHeight`Deprecated

A string being the height of the frame margin.

`HTMLIFrameElement.marginWidth`Deprecated

A string being the width of the frame margin.

[HTMLIFrameElement.name](/en-US/docs/Web/API/HTMLIFrameElement/name)

A string that reflects the [name](/en-US/docs/Web/HTML/Reference/Elements/iframe#name) HTML attribute, containing a name by which to refer to the frame.

[HTMLIFrameElement.privateToken](/en-US/docs/Web/API/HTMLIFrameElement/privateToken)Experimental

A string representation of an options object representing a [private state token](/en-US/docs/Web/API/Private_State_Token_API/Using) operation; this object has the same structure as the `RequestInit` dictionary's [privateToken](/en-US/docs/Web/API/RequestInit#privatetoken) property. Mirrors the content of the associated `<iframe>` element's [privateToken](/en-US/docs/Web/HTML/Reference/Elements/iframe#privatetoken) attribute.

[HTMLIFrameElement.referrerPolicy](/en-US/docs/Web/API/HTMLIFrameElement/referrerPolicy)

A string that reflects the [referrerPolicy](/en-US/docs/Web/HTML/Reference/Elements/iframe#referrerpolicy) HTML attribute indicating which referrer to use when fetching the linked resource.

[HTMLIFrameElement.sandbox](/en-US/docs/Web/API/HTMLIFrameElement/sandbox)Read only

Returns a [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that reflects the [sandbox](/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox) HTML attribute, indicating extra restrictions on the behavior of the nested content.

`HTMLIFrameElement.scrolling`Deprecated

A string that indicates whether the browser should provide scrollbars for the frame.

[HTMLIFrameElement.src](/en-US/docs/Web/API/HTMLIFrameElement/src)

A string that reflects the [src](/en-US/docs/Web/HTML/Reference/Elements/iframe#src) HTML attribute, containing the address of the content to be embedded. Note that programmatically removing an `<iframe>`'s src attribute (e.g., via [Element.removeAttribute()](/en-US/docs/Web/API/Element/removeAttribute)) causes `about:blank` to be loaded in the frame in Firefox (from version 65), Chromium-based browsers, and Safari/iOS.

[HTMLIFrameElement.srcdoc](/en-US/docs/Web/API/HTMLIFrameElement/srcdoc)

A [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) or string that represents the HTML document loaded into the frame.

[HTMLIFrameElement.width](/en-US/docs/Web/API/HTMLIFrameElement/width)

A string that reflects the [width](/en-US/docs/Web/HTML/Reference/Elements/iframe#width) HTML attribute, indicating the width of the frame.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLIFrameElement.getSVGDocument()](/en-US/docs/Web/API/HTMLIFrameElement/getSVGDocument)

Returns the embedded SVG as a [Document](/en-US/docs/Web/API/Document).

## [Specifications](#specifications)

Specification
[HTML# htmliframeelement](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#htmliframeelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 16, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLIFrameElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmliframeelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLIFrameElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmliframeelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLIFrameElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmliframeelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff6e66d18205c93fcaeb2ea9ad51541b5b4d7d2b1%0A*+Document+last+modified%3A+2025-12-16T10%3A03%3A04.000Z%0A%0A%3C%2Fdetails%3E)
