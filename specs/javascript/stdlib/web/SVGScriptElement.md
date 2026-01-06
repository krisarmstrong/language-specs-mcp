# SVGScriptElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGScriptElement&level=high)

The `SVGScriptElement` interface corresponds to the SVG [<script>](/en-US/docs/Web/SVG/Reference/Element/script) element.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[SVGScriptElement.href](/en-US/docs/Web/API/SVGScriptElement/href)Read only

An [SVGAnimatedString](/en-US/docs/Web/API/SVGAnimatedString) corresponding to the [href](/en-US/docs/Web/SVG/Reference/Attribute/href) or [xlink:href](/en-US/docs/Web/SVG/Reference/Attribute/xlink:href)Deprecated attribute of the given [<script>](/en-US/docs/Web/SVG/Reference/Element/script) element.

[SVGScriptElement.type](/en-US/docs/Web/API/SVGScriptElement/type)Read only

A string corresponding to the [type](/en-US/docs/Web/SVG/Reference/Attribute/type) attribute of the given [<script>](/en-US/docs/Web/SVG/Reference/Element/script) element. A [DOMException](/en-US/docs/Web/API/DOMException) is raised with the code `NO_MODIFICATION_ALLOWED_ERR` on an attempt to change the value of a read only attribute.

`SVGScriptElement.crossOrigin`Read only

A string corresponding to the [crossorigin](/en-US/docs/Web/SVG/Reference/Attribute/crossorigin) attribute of the given [<script>](/en-US/docs/Web/SVG/Reference/Element/script) element.

## [Instance methods](#instance_methods)

This interface doesn't implement any specific methods, but inherits methods from its parent interface, [SVGElement](/en-US/docs/Web/API/SVGElement).

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGScriptElement](https://svgwg.org/svg2-draft/interact.html#InterfaceSVGScriptElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 28, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/SVGScriptElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svgscriptelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGScriptElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvgscriptelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGScriptElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvgscriptelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7c9a25bc747b8a4a3dfd91a37ac1b2193414c3a%0A*+Document+last+modified%3A+2023-07-28T07%3A56%3A52.000Z%0A%0A%3C%2Fdetails%3E)
