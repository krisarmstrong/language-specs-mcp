# WebGLTexture

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLTexture&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGLTexture interface is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and represents an opaque texture object providing storage and state for texturing operations.

## In this article

- [WebGL textures](#webgl_textures)
- [WebXR opaque textures](#webxr_opaque_textures)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [WebGL textures](#webgl_textures)

The `WebGLTexture` object does not define any methods or properties of its own and its content is not directly accessible. When working with `WebGLTexture` objects, the following methods of the [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext) are useful:

- [WebGLRenderingContext.bindTexture()](/en-US/docs/Web/API/WebGLRenderingContext/bindTexture)
- [WebGLRenderingContext.createTexture()](/en-US/docs/Web/API/WebGLRenderingContext/createTexture)
- [WebGLRenderingContext.deleteTexture()](/en-US/docs/Web/API/WebGLRenderingContext/deleteTexture)
- [WebGLRenderingContext.isTexture()](/en-US/docs/Web/API/WebGLRenderingContext/isTexture)

See also the [WebGL tutorial](/en-US/docs/Web/API/WebGL_API/Tutorial) on [Using textures in WebGL](/en-US/docs/Web/API/WebGL_API/Tutorial/Using_textures_in_WebGL).

## [WebXR opaque textures](#webxr_opaque_textures)

When using [WebXR](/en-US/docs/Web/API/WebXR_Device_API) layers, the [XRWebGLBinding](/en-US/docs/Web/API/XRWebGLBinding) object will return instances of an opaque`WebGLTexture` for the color and depth/stencil attachments.

WebXR methods that return opaque`WebGLTexture` objects:

- [XRWebGLBinding.getSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getSubImage)
- [XRWebGLBinding.getViewSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getViewSubImage)

The WebXR opaque texture is identical to the standard `WebGLTexture` with the following exceptions:

- A WebXR opaque texture is invalid outside a WebXR [requestAnimationFrame() callback](/en-US/docs/Web/API/XRSession/requestAnimationFrame) for its session.
- A WebXR opaque texture is invalid until it is returned by [XRWebGLBinding.getSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getSubImage) or [XRWebGLBinding.getViewSubImage()](/en-US/docs/Web/API/XRWebGLBinding/getViewSubImage).
- A WebXR opaque texture for the color attachment contains colors with premultiplied alpha.
- At the end of a [requestAnimationFrame() callback](/en-US/docs/Web/API/XRSession/requestAnimationFrame) a WebXR opaque texture is unbounded and detached from all [WebGLShader](/en-US/docs/Web/API/WebGLShader) objects.
- A WebXR opaque texture behaves as though it was allocated with [texStorage2D](/en-US/docs/Web/API/WebGL2RenderingContext/texStorage2D) or [texStorage3D](/en-US/docs/Web/API/WebGL2RenderingContext/texStorage3D), as appropriate, even when using a WebGL 1.0 context.
- If a WebXR opaque texture calls [WebGLRenderingContext.deleteTexture()](/en-US/docs/Web/API/WebGLRenderingContext/deleteTexture), an `INVALID_OPERATION` error is thrown.
- Changes to the dimension or format of a WebXR opaque texture are not allowed. GL functions may only alter the texel values and texture parameters.

## [Examples](#examples)

### [Creating a texture](#creating_a_texture)

js

```
const canvas = document.getElementById("canvas");
const gl = canvas.getContext("webgl");
const texture = gl.createTexture();
```

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.9](https://registry.khronos.org/webgl/specs/latest/1.0/#5.9)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGLRenderingContext.bindTexture()](/en-US/docs/Web/API/WebGLRenderingContext/bindTexture)
- [WebGLRenderingContext.createTexture()](/en-US/docs/Web/API/WebGLRenderingContext/createTexture)
- [WebGLRenderingContext.deleteTexture()](/en-US/docs/Web/API/WebGLRenderingContext/deleteTexture)
- [WebGLRenderingContext.isTexture()](/en-US/docs/Web/API/WebGLRenderingContext/isTexture)
- [WebGLRenderingContext.compressedTexImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/compressedTexImage2D)
- [WebGLRenderingContext.compressedTexSubImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/compressedTexSubImage2D)
- [WebGLRenderingContext.copyTexImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/copyTexImage2D)
- [WebGLRenderingContext.copyTexSubImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/copyTexSubImage2D)
- [WebGLRenderingContext.generateMipmap()](/en-US/docs/Web/API/WebGLRenderingContext/generateMipmap)
- [WebGLRenderingContext.getTexParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getTexParameter)
- [WebGLRenderingContext.texImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/texImage2D)
- [WebGLRenderingContext.texSubImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/texSubImage2D)
- [WebGLRenderingContext.texParameterf()](/en-US/docs/Web/API/WebGLRenderingContext/texParameter)
- [WebGLRenderingContext.texParameteri()](/en-US/docs/Web/API/WebGLRenderingContext/texParameter)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 28, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLTexture/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webgltexture/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLTexture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebgltexture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLTexture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebgltexture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2b942f0d8f84641c233d701cb5d1f4e6c23120ff%0A*+Document+last+modified%3A+2024-09-28T05%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E)
