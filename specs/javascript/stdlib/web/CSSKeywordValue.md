# CSSKeywordValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeywordValue&level=not)

The `CSSKeywordValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) creates an object to represent CSS keywords and other identifiers.

The interface instance name is a [stringifier](/en-US/docs/Glossary/Stringifier) meaning that when used anywhere a string is expected it will return the value of `CSSKeyword.value`.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CSSKeywordValue()](/en-US/docs/Web/API/CSSKeywordValue/CSSKeywordValue)

Creates a new `CSSKeywordValue` object.

## [Instance properties](#instance_properties)

[CSSKeywordValue.value](/en-US/docs/Web/API/CSSKeywordValue/value)

Returns or sets the value of the `CSSKeywordValue`.

## [Instance methods](#instance_methods)

Inherits methods from [CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue).

## [Examples](#examples)

The following example resets the CSS [display](/en-US/docs/Web/CSS/Reference/Properties/display) property to its defaults, setting the inline [style](/en-US/docs/Web/HTML/Reference/Global_attributes/style) attribute to `style="display: initial"` if viewed in the [developer tools inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/select_an_element/index.html).

```
#myElement {
  display: flex;
}
```

```
<div id="myElement">
  Check the developer tools to see the log in the console and to inspect the
  style attribute on this div.
</div>
```

js

```
let myElement = document.getElementById("myElement").attributeStyleMap;
myElement.set("display", new CSSKeywordValue("initial"));

console.log(myElement.get("display").value); // 'initial'
```

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# keywordvalue-objects](https://drafts.css-houdini.org/css-typed-om/#keywordvalue-objects)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSImageValue](/en-US/docs/Web/API/CSSImageValue)
- [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)
- [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 10, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSKeywordValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csskeywordvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeywordValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsskeywordvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSKeywordValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsskeywordvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9b6cd1b7fa8612257b72b2a85a96dd7d45c0200%0A*+Document+last+modified%3A+2025-04-10T14%3A56%3A07.000Z%0A%0A%3C%2Fdetails%3E)
