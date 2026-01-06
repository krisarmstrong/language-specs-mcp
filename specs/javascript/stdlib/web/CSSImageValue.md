# CSSImageValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSImageValue&level=not)

The `CSSImageValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model#css_typed_object_model) represents values for properties that take an image, for example [background-image](/en-US/docs/Web/CSS/Reference/Properties/background-image), [list-style-image](/en-US/docs/Web/CSS/Reference/Properties/list-style-image), or [border-image-source](/en-US/docs/Web/CSS/Reference/Properties/border-image-source).

The CSSImageValue object represents an [<image>](/en-US/docs/Web/CSS/Reference/Values/image) that involves a URL, such as [url()](/en-US/docs/Web/CSS/Reference/Values/url_function) or [<image()>](/en-US/docs/Web/CSS/Reference/Values/image), but not [linear-gradient()](/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient) or [element()](/en-US/docs/Web/CSS/Reference/Values/element).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

Inherits methods from [CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue).

## [Examples](#examples)

We create an element

html

```
<button>Magic Wand</button>
```

We add some CSS, including a background image requesting a binary file:

css

```
button {
  display: inline-block;
  min-height: 100px;
  min-width: 100px;
  background: no-repeat 5% center url("magic-wand.png") aqua;
}
```

We get the element's style map. We then get() the background-image from the style map and stringify it:

js

```
// get the element
const button = document.querySelector("button");

// Retrieve all computed styles with computedStyleMap()
const allComputedStyles = button.computedStyleMap();

// Return the CSSImageValue Example
console.log(allComputedStyles.get("background-image"));
console.log(allComputedStyles.get("background-image").toString());
```

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# imagevalue-objects](https://drafts.css-houdini.org/css-typed-om/#imagevalue-objects)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [CSSKeywordValue](/en-US/docs/Web/API/CSSKeywordValue)
- [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue)
- [CSSPositionValue](/en-US/docs/Web/API/CSSPositionValue)
- [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue)
- [CSSUnparsedValue](/en-US/docs/Web/API/CSSUnparsedValue)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSImageValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssimagevalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSImageValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssimagevalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSImageValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssimagevalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
