# CSSTransformValue

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransformValue&level=not)

The `CSSTransformValue` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model) represents `transform-list` values as used by the CSS [transform](/en-US/docs/Web/CSS/Reference/Properties/transform) property.

## In this article

- [Interfaces based on CSSTransformValue](#interfaces_based_on_csstransformvalue)
- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces based on CSSTransformValue](#interfaces_based_on_csstransformvalue)

Below is a list of interfaces based on the `CSSTransformValue` interface.

- [CSSTranslate](/en-US/docs/Web/API/CSSTranslate)
- [CSSRotate](/en-US/docs/Web/API/CSSRotate)
- [CSSScale](/en-US/docs/Web/API/CSSScale)
- [CSSSkew](/en-US/docs/Web/API/CSSSkew)
- [CSSSkewX](/en-US/docs/Web/API/CSSSkewX)
- [CSSSkewY](/en-US/docs/Web/API/CSSSkewY)
- [CSSPerspective](/en-US/docs/Web/API/CSSPerspective)
- [CSSMatrixComponent](/en-US/docs/Web/API/CSSMatrixComponent)

## [Constructor](#constructor)

[CSSTransformValue()](/en-US/docs/Web/API/CSSTransformValue/CSSTransformValue)

Creates a new `CSSTransformValue` object.

## [Instance properties](#instance_properties)

[CSSTransformValue.length](/en-US/docs/Web/API/CSSTransformValue/length)Read only

Returns how many transform components are contained within the `CSSTransformValue`.

[CSSTransformValue.is2D](/en-US/docs/Web/API/CSSTransformValue/is2D)Read only

Returns a boolean indicating whether the transform is 2D or 3D.

## [Instance methods](#instance_methods)

Inherits methods from its ancestor [CSSStyleValue](/en-US/docs/Web/API/CSSStyleValue).

[CSSTransformValue.toMatrix()](/en-US/docs/Web/API/CSSTransformValue/toMatrix)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) object.

[CSSTransformValue.entries()](/en-US/docs/Web/API/CSSTransformValue/entries)

Returns an array of a given object's own enumerable property `[key, value]` pairs in the same order as that provided by a [for...in](/en-US/docs/Web/JavaScript/Reference/Statements/for...in) loop (the difference being that a for-in loop enumerates properties in the prototype chain as well).

[CSSTransformValue.forEach()](/en-US/docs/Web/API/CSSTransformValue/forEach)

Executes a provided function once for each element of the `CSSTransformValue` object.

[CSSTransformValue.keys()](/en-US/docs/Web/API/CSSTransformValue/keys)

Returns a new array iterator object that contains the keys for each index in the `CSSTransformValue` object.

[CSSTransformValue.values()](/en-US/docs/Web/API/CSSTransformValue/values)

Returns a new array iterator object that contains the values for each index in the `CSSTransformValue` object.

## [Examples](#examples)

To Do.

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# transformvalue-objects](https://drafts.css-houdini.org/css-typed-om/#transformvalue-objects)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CSSTransformValue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csstransformvalue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransformValue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsstransformvalue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransformValue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsstransformvalue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcf331ccff0dd88648dc9fe22a14f9aaa595ec4bf%0A*+Document+last+modified%3A+2024-08-08T12%3A07%3A53.000Z%0A%0A%3C%2Fdetails%3E)
