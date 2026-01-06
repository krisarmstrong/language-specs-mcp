# WebGLFramebuffer

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLFramebuffer&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGLFramebuffer interface is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and represents a collection of buffers that serve as a rendering destination.

## In this article

- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Description](#description)

The `WebGLFramebuffer` object does not define any methods or properties of its own and its content is not directly accessible. When working with `WebGLFramebuffer` objects, the following methods of the [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext) are useful:

- [WebGLRenderingContext.bindFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindFramebuffer)
- [WebGLRenderingContext.createFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createFramebuffer)
- [WebGLRenderingContext.deleteFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteFramebuffer)
- [WebGLRenderingContext.isFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isFramebuffer)
- [WebGLRenderingContext.framebufferRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferRenderbuffer)
- [WebGLRenderingContext.framebufferTexture2D()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferTexture2D)

## [Examples](#examples)

### [Creating a frame buffer](#creating_a_frame_buffer)

js

```
const canvas = document.getElementById("canvas");
const gl = canvas.getContext("webgl");
const buffer = gl.createFramebuffer();
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.5](https://registry.khronos.org/webgl/specs/latest/1.0/#5.5)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.bindFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindFramebuffer)
- [WebGLRenderingContext.createFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createFramebuffer)
- [WebGLRenderingContext.deleteFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteFramebuffer)
- [WebGLRenderingContext.isFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isFramebuffer)
- [WebGLRenderingContext.framebufferRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferRenderbuffer)
- [WebGLRenderingContext.framebufferTexture2D()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferTexture2D)
- Other buffers: [WebGLBuffer](/en-US/docs/Web/API/WebGLBuffer), [WebGLRenderbuffer](/en-US/docs/Web/API/WebGLRenderbuffer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLFramebuffer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglframebuffer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLFramebuffer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglframebuffer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLFramebuffer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglframebuffer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2b942f0d8f84641c233d701cb5d1f4e6c23120ff%0A*+Document+last+modified%3A+2024-09-28T05%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E)
