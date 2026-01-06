# CSSTransformComponent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransformComponent&level=not)

The `CSSTransformComponent` interface of the [CSS Typed Object Model API](/en-US/docs/Web/API/CSS_Object_Model) is part of the [CSSTransformValue](/en-US/docs/Web/API/CSSTransformValue) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[CSSTransformComponent.is2D](/en-US/docs/Web/API/CSSTransformComponent/is2D)Read only

Returns a boolean indicting whether the transform is 2D or 3D.

## [Instance methods](#instance_methods)

[CSSTransformComponent.toMatrix()](/en-US/docs/Web/API/CSSTransformComponent/toMatrix)

Returns a new [DOMMatrix](/en-US/docs/Web/API/DOMMatrix) object.

[CSSTransformComponent.toString()](/en-US/docs/Web/API/CSSTransformComponent/toString)

A string in the form of a CSS [transform function](/en-US/docs/Web/CSS/Reference/Values/transform-function).

This will use the value of `is2D` to return either a 2D or 3D transform. For example if the component represents [CSSRotate](/en-US/docs/Web/API/CSSRotate) and `is2D` is false then the string returned will be in the form of the CSS transformation [rotate3d()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d) function. If true the string returned will be in the form of the 2-dimensional [rotate()](/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate) function.

## [Examples](#examples)

To do

## [Specifications](#specifications)

Specification
[CSS Typed OM Level 1# csstransformcomponent](https://drafts.css-houdini.org/css-typed-om/#csstransformcomponent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSTransformComponent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csstransformcomponent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransformComponent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsstransformcomponent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransformComponent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsstransformcomponent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c13af55e869cbc54830fd1a601fd05f60717375%0A*+Document+last+modified%3A+2025-12-17T16%3A01%3A14.000Z%0A%0A%3C%2Fdetails%3E)
