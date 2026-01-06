# WebGLShaderPrecisionFormat

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLShaderPrecisionFormat&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGLShaderPrecisionFormat interface is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and represents the information returned by calling the [WebGLRenderingContext.getShaderPrecisionFormat()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat) method.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[WebGLShaderPrecisionFormat.rangeMin](/en-US/docs/Web/API/WebGLShaderPrecisionFormat/rangeMin)Read only

The base 2 log of the absolute value of the minimum value that can be represented.

[WebGLShaderPrecisionFormat.rangeMax](/en-US/docs/Web/API/WebGLShaderPrecisionFormat/rangeMax)Read only

The base 2 log of the absolute value of the maximum value that can be represented.

[WebGLShaderPrecisionFormat.precision](/en-US/docs/Web/API/WebGLShaderPrecisionFormat/precision)Read only

The number of bits of precision that can be represented. For integer formats this value is always 0.

## [Examples](#examples)

A `WebGLShaderPrecisionFormat` object is returned by the [WebGLRenderingContext.getShaderPrecisionFormat()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat) method.

js

```
const canvas = document.getElementById("canvas");
const gl = canvas.getContext("webgl");
gl.getShaderPrecisionFormat(gl.VERTEX_SHADER, gl.MEDIUM_FLOAT);
// WebGLShaderPrecisionFormat { rangeMin: 127, rangeMax: 127, precision: 23 }
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.12](https://registry.khronos.org/webgl/specs/latest/1.0/#5.12)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.getShaderPrecisionFormat()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLShaderPrecisionFormat/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglshaderprecisionformat/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLShaderPrecisionFormat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglshaderprecisionformat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLShaderPrecisionFormat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglshaderprecisionformat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2b942f0d8f84641c233d701cb5d1f4e6c23120ff%0A*+Document+last+modified%3A+2024-09-28T05%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E)
