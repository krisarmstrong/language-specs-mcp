# SVGAnimatedLengthList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimatedLengthList&level=high)

The `SVGAnimatedLengthList` interface is used for attributes of type [SVGLengthList](/en-US/docs/Web/API/SVGLengthList) which can be animated.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[SVGAnimatedLengthList.baseVal](/en-US/docs/Web/API/SVGAnimatedLengthList/baseVal)Read only

An [SVGLengthList](/en-US/docs/Web/API/SVGLengthList) that represents the base value of the given attribute before applying any animations.

[SVGAnimatedLengthList.animVal](/en-US/docs/Web/API/SVGAnimatedLengthList/animVal)Read only

A read only [SVGLengthList](/en-US/docs/Web/API/SVGLengthList) that represents the current animated value of the given attribute. If the given attribute is not currently being animated, then the [SVGLengthList](/en-US/docs/Web/API/SVGLengthList) will have the same contents as `baseVal`. The object referenced by `animVal` will always be distinct from the one referenced by `baseVal`, even when the attribute is not animated.

## [Instance methods](#instance_methods)

The `SVGAnimatedLengthList` interface does not provide any specific methods.

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGAnimatedLengthList](https://svgwg.org/svg2-draft/types.html#InterfaceSVGAnimatedLengthList)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SVGAnimatedLengthList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svganimatedlengthlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimatedLengthList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvganimatedlengthlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimatedLengthList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvganimatedlengthlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e39a37874913a1e3fd82999467505fd525e9177%0A*+Document+last+modified%3A+2025-05-02T19%3A48%3A16.000Z%0A%0A%3C%2Fdetails%3E)
