# DOMParser

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMParser&level=high)

The `DOMParser` interface provides the ability to parse [XML](/en-US/docs/Glossary/XML) or [HTML](/en-US/docs/Glossary/HTML) source code from a string into a DOM [Document](/en-US/docs/Web/API/Document).

You can perform the opposite operation—converting a DOM tree into XML or HTML source—using the [XMLSerializer](/en-US/docs/Web/API/XMLSerializer) interface.

In the case of an HTML document, you can also replace portions of the DOM with new DOM trees built from HTML by setting the value of the [Element.innerHTML](/en-US/docs/Web/API/Element/innerHTML) and [outerHTML](/en-US/docs/Web/API/Element/outerHTML) properties. These properties can also be read to fetch HTML fragments corresponding to the corresponding DOM subtree.

Note that [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) can parse XML and HTML directly from a URL-addressable resource, returning a `Document` in its [response](/en-US/docs/Web/API/XMLHttpRequest/response) property.

Note: Be aware that [block-level elements](/en-US/docs/Glossary/Block-level_content) like `<p>` will be automatically closed if another block-level element is nested inside and therefore parsed before the closing `</p>` tag.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DOMParser()](/en-US/docs/Web/API/DOMParser/DOMParser)

Creates a new `DOMParser` object.

## [Instance methods](#instance_methods)

[DOMParser.parseFromString()](/en-US/docs/Web/API/DOMParser/parseFromString)

Parses an input [TrustedHTML](/en-US/docs/Web/API/TrustedHTML) instance or string as HTML or XML and returns a [Document](/en-US/docs/Web/API/Document).

## [Examples](#examples)

The documentation for [DOMParser.parseFromString()](/en-US/docs/Web/API/DOMParser/parseFromString), this interface's only method, contains examples for parsing XML, SVG, and HTML strings.

## [Specifications](#specifications)

Specification
[HTML# dom-parsing-and-serialization](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#dom-parsing-and-serialization)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Parsing and serializing XML](/en-US/docs/Web/XML/Guides/Parsing_and_serializing_XML)
- [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest)
- [XMLSerializer](/en-US/docs/Web/API/XMLSerializer)
- [JSON.parse()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) - counterpart for [JSON](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) documents.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DOMParser/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/domparser/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMParser&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdomparser%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDOMParser%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdomparser%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2c538b494ed560fe68f239f40ce4417b720a5595%0A*+Document+last+modified%3A+2025-10-13T23%3A42%3A40.000Z%0A%0A%3C%2Fdetails%3E)
