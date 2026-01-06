# WebGLRenderbuffer

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLRenderbuffer&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGLRenderbuffer interface is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and represents a buffer that can contain an image, or that can be a source or target of a rendering operation.

## In this article

- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

The `WebGLRenderbuffer` object does not define any methods or properties of its own and its content is not directly accessible. When working with `WebGLRenderbuffer` objects, the following methods are useful:

- [WebGLRenderingContext.bindRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindRenderbuffer)
- [WebGLRenderingContext.createRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createRenderbuffer)
- [WebGLRenderingContext.deleteRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteRenderbuffer)
- [WebGLRenderingContext.framebufferRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferRenderbuffer)
- [WebGLRenderingContext.getRenderbufferParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getRenderbufferParameter)
- [WebGLRenderingContext.isRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isRenderbuffer)
- [WebGLRenderingContext.renderbufferStorage()](/en-US/docs/Web/API/WebGLRenderingContext/renderbufferStorage)
- [WebGL2RenderingContext.renderbufferStorageMultisample()](/en-US/docs/Web/API/WebGL2RenderingContext/renderbufferStorageMultisample)

## [Examples](#examples)

### [Creating a render buffer](#creating_a_render_buffer)

js

```
const canvas = document.getElementById("canvas");
const gl = canvas.getContext("webgl");
const buffer = gl.createRenderbuffer();
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.7](https://registry.khronos.org/webgl/specs/latest/1.0/#5.7)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.bindRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindRenderbuffer)
- [WebGLRenderingContext.createRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createRenderbuffer)
- [WebGLRenderingContext.deleteRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteRenderbuffer)
- [WebGLRenderingContext.framebufferRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferRenderbuffer)
- [WebGLRenderingContext.getRenderbufferParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getRenderbufferParameter)
- [WebGLRenderingContext.isRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isRenderbuffer)
- [WebGLRenderingContext.renderbufferStorage()](/en-US/docs/Web/API/WebGLRenderingContext/renderbufferStorage)
- Other buffers: [WebGLBuffer](/en-US/docs/Web/API/WebGLBuffer), [WebGLFramebuffer](/en-US/docs/Web/API/WebGLFramebuffer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLRenderbuffer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglrenderbuffer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLRenderbuffer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglrenderbuffer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLRenderbuffer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglrenderbuffer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2b942f0d8f84641c233d701cb5d1f4e6c23120ff%0A*+Document+last+modified%3A+2024-09-28T05%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E)
