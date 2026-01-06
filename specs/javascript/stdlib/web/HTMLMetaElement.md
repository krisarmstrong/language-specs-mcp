# HTMLMetaElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMetaElement&level=high)

The `HTMLMetaElement` interface contains descriptive metadata about a document provided in HTML as [<meta>](/en-US/docs/Web/HTML/Reference/Elements/meta) elements. This interface inherits all of the properties and methods described in the [HTMLElement](/en-US/docs/Web/API/HTMLElement) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[<meta#charset>](/en-US/docs/Web/HTML/Reference/Elements/meta#charset)

The character encoding for a HTML document.

[HTMLMetaElement.content](/en-US/docs/Web/API/HTMLMetaElement/content)

The 'value' part of the name-value pairs of the document metadata.

[HTMLMetaElement.httpEquiv](/en-US/docs/Web/API/HTMLMetaElement/httpEquiv)

The name of the pragma directive, the HTTP response header, for a document.

[HTMLMetaElement.media](/en-US/docs/Web/API/HTMLMetaElement/media)

The media context for a `theme-color` metadata property.

[HTMLMetaElement.name](/en-US/docs/Web/API/HTMLMetaElement/name)

The 'name' part of the name-value pairs defining the named metadata of a document.

[HTMLMetaElement.scheme](/en-US/docs/Web/API/HTMLMetaElement/scheme)Deprecated

Defines the scheme of the value in the [HTMLMetaElement.content](/en-US/docs/Web/API/HTMLMetaElement/content) attribute. This is deprecated and should not be used on new web pages.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Examples](#examples)

The following two examples show a general approach to using the `HTMLMetaElement` interface. For specific examples, see the pages for the individual properties as described in the [Instance properties](#instance_properties) section above.

### [Setting the page description metadata](#setting_the_page_description_metadata)

The following example creates a new `<meta>` element with a `name` attribute set to [description](/en-US/docs/Web/HTML/Reference/Elements/meta/name#meta_names_defined_in_the_html_specification). The `content` attribute sets a description of the document and is appended to the document `<head>`:

js

```
const meta = document.createElement("meta");
meta.name = "description";
meta.content =
  "The <meta> element can be used to provide document metadata in terms of name-value pairs, with the name attribute giving the metadata name, and the content attribute giving the value.";
document.head.appendChild(meta);
```

### [Setting the viewport metadata](#setting_the_viewport_metadata)

The following example shows how to create a new `<meta>` element with a `name` attribute set to [viewport](/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport). The `content` attribute sets the viewport size and is appended to the document `<head>`:

js

```
const meta = document.createElement("meta");
meta.name = "viewport";
meta.content = "width=device-width, initial-scale=1";
document.head.appendChild(meta);
```

For more information on setting the viewport, see [<meta name="viewport">](/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport).

## [Specifications](#specifications)

Specification
[HTML# htmlmetaelement](https://html.spec.whatwg.org/multipage/semantics.html#htmlmetaelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<meta>](/en-US/docs/Web/HTML/Reference/Elements/meta)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLMetaElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlmetaelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMetaElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlmetaelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMetaElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlmetaelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb5a6d8bc5fd751032f70b88e7ec1ec61339937de%0A*+Document+last+modified%3A+2025-10-17T01%3A33%3A06.000Z%0A%0A%3C%2Fdetails%3E)
