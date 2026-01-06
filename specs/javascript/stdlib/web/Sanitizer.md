# Sanitizer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSanitizer&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Sanitizer` interface of the [HTML Sanitizer API](/en-US/docs/Web/API/HTML_Sanitizer_API) defines a configuration object that specifies what elements, attributes and comments are allowed or should be removed when inserting strings of HTML into an [Element](/en-US/docs/Web/API/Element) or [ShadowRoot](/en-US/docs/Web/API/ShadowRoot), or when parsing an HTML string into a [Document](/en-US/docs/Web/API/Document).

A `Sanitizer` instance is effectively a wrapper around a [SanitizerConfig](/en-US/docs/Web/API/SanitizerConfig), and can be passed as a configuration alternative in the same [sanitization methods](/en-US/docs/Web/API/HTML_Sanitizer_API#sanitization_methods):

- [setHTML()](/en-US/docs/Web/API/Element/setHTML) or [setHTMLUnsafe()](/en-US/docs/Web/API/Element/setHTMLUnsafe) on [Element](/en-US/docs/Web/API/Element).
- [setHTML()](/en-US/docs/Web/API/ShadowRoot/setHTML) or [setHTMLUnsafe()](/en-US/docs/Web/API/ShadowRoot/setHTMLUnsafe) on [ShadowRoot](/en-US/docs/Web/API/ShadowRoot).
- [Document.parseHTML()](/en-US/docs/Web/API/Document/parseHTML_static) or [Document.parseHTMLUnsafe()](/en-US/docs/Web/API/Document/parseHTMLUnsafe_static) static methods.

Note that `Sanitizer` is expected to be more efficient to reuse and modify when needed.

## In this article

- [Constructors](#constructors)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructors](#constructors)

[Sanitizer()](/en-US/docs/Web/API/Sanitizer/Sanitizer)Experimental

Creates and returns a `Sanitizer` object, optionally with custom sanitization behavior defined in a [SanitizerConfig](/en-US/docs/Web/API/SanitizerConfig).

## [Instance methods](#instance_methods)

[Sanitizer.allowElement()](/en-US/docs/Web/API/Sanitizer/allowElement)Experimental

Sets an element as allowed by the sanitizer, optionally with an array of attributes that are allowed or disallowed.

[Sanitizer.get()](/en-US/docs/Web/API/Sanitizer/get)Experimental

Returns the current `Sanitizer` configuration as a [SanitizerConfig](/en-US/docs/Web/API/SanitizerConfig) dictionary instance.

[Sanitizer.removeElement()](/en-US/docs/Web/API/Sanitizer/removeElement)Experimental

Sets an element to be removed by the sanitizer.

[Sanitizer.removeUnsafe()](/en-US/docs/Web/API/Sanitizer/removeUnsafe)Experimental

Updates the sanitizer configuration so that it will remove any XSS-unsafe HTML.

[Sanitizer.replaceElementWithChildren()](/en-US/docs/Web/API/Sanitizer/replaceElementWithChildren)Experimental

Sets an element to be replaced by its child HTML elements.

[Sanitizer.allowAttribute()](/en-US/docs/Web/API/Sanitizer/allowAttribute)Experimental

Sets an attribute as allowed on any element.

[Sanitizer.removeAttribute()](/en-US/docs/Web/API/Sanitizer/removeAttribute)Experimental

Sets an attribute to be removed from any element.

[Sanitizer.setComments()](/en-US/docs/Web/API/Sanitizer/setComments)Experimental

Sets whether comments will be allowed or removed by the sanitizer.

[Sanitizer.setDataAttributes()](/en-US/docs/Web/API/Sanitizer/setDataAttributes)Experimental

Sets whether data attributes on elements will be allowed or removed by the sanitizer.

## [Examples](#examples)

For more examples see the [HTML Sanitizer API](/en-US/docs/Web/API/HTML_Sanitizer_API) and the individual methods. Below we show a few examples of how you might create different sanitizer configurations.

### [Creating a default sanitizer](#creating_a_default_sanitizer)

The default sanitizer is constructed as shown below.

js

```
const sanitizer = new Sanitizer();
```

The XSS-safe [sanitization methods](/en-US/docs/Web/API/HTML_Sanitizer_API#sanitization_methods) create the same sanitizer automatically if no options are passed.

### [Creating an empty sanitizer](#creating_an_empty_sanitizer)

To create an empty sanitizer, pass an empty object to the constructor. The resulting sanitizer configuration is shown below.

js

```
const sanitizer = new Sanitizer({});
/*
{
  "attributes": [],
  "comments": true,
  "dataAttributes": true,
  "elements": [],
  "removeAttributes": [],
  "removeElements": [],
  "replaceWithChildrenElements": []
}
*/
```

### [Creating an "allow" sanitizer](#creating_an_allow_sanitizer)

This example shows how you might create an "allow sanitizer": a sanitizer that allows only a subset of attributes and elements.

The code first uses the [Sanitizer()](/en-US/docs/Web/API/Sanitizer/Sanitizer) constructor to create a `Sanitizer`, specifying a [SanitizerConfig](/en-US/docs/Web/API/SanitizerConfig) that allows the element `<div>`, `<p>` and `<script>`.

The example then uses `allowElement()` to further allow `<span>` elements, `allowAttribute()` to allow the `id` attribute on any element, and `replaceElementWithChildren()` method to set that any `<b>` elements should be replaced by their inner content (this is a kind of "allow" in that you are explicitly specifying some entities to keep). Lastly we specify that comments should be retained.

js

```
const sanitizer = new Sanitizer({ elements: ["div", "p", "script"] });
sanitizer.allowElement("span");
sanitizer.allowAttribute("id");
sanitizer.replaceElementWithChildren("b");
sanitizer.setComments(true);
```

### [Creating a "remove" sanitizer](#creating_a_remove_sanitizer)

This example shows how you might create a "remove sanitizer", specifying items to remove from the input.

The code first uses the [Sanitizer()](/en-US/docs/Web/API/Sanitizer/Sanitizer) constructor to create a `Sanitizer`, specifying a [SanitizerConfig](/en-US/docs/Web/API/SanitizerConfig) that removes the element `<span>` and `<script>`. We then use `removeElement()` to add `<h6>` to the array of elements to be removed, and `removeAttribute()` to remove `lang` from the attributes list. We also remove comments.

js

```
const sanitizer = new Sanitizer({ removeElements: ["span", "script"] });
sanitizer.removeElement("h6");
sanitizer.removeAttribute("lang");
sanitizer.setComments(false);
```

## [Specifications](#specifications)

Specification
[HTML Sanitizer API# sanitizer](https://wicg.github.io/sanitizer-api/#sanitizer)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Sanitizer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sanitizer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSanitizer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsanitizer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSanitizer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsanitizer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
