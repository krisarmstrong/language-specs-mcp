# OES_draw_buffers_indexed

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨December 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOES_draw_buffers_indexed&level=high)

The `OES_draw_buffers_indexed` extension is part of the [WebGL API](/en-US/docs/Web/API/WebGL_API) and enables the use of different blend options when writing to multiple color buffers simultaneously.

WebGL extensions are available using the [WebGLRenderingContext.getExtension()](/en-US/docs/Web/API/WebGLRenderingContext/getExtension) method. For more information, see also [Using Extensions](/en-US/docs/Web/API/WebGL_API/Using_Extensions) in the [WebGL tutorial](/en-US/docs/Web/API/WebGL_API/Tutorial).

Note: This extension is only available to [WebGL2](/en-US/docs/Web/API/WebGL2RenderingContext) contexts.

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance methods](#instance_methods)

[OES_draw_buffers_indexed.blendEquationiOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/blendEquationiOES)

Sets both the RGB and alpha blend equations for a particular draw buffer.

[OES_draw_buffers_indexed.blendEquationSeparateiOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/blendEquationSeparateiOES)

Sets the RGB and alpha blend equations separately for a particular draw buffer.

[OES_draw_buffers_indexed.blendFunciOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/blendFunciOES)

Defines which function is used when blending pixels for a particular draw buffer.

[OES_draw_buffers_indexed.blendFuncSeparateiOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/blendFuncSeparateiOES)

Defines which function is used when blending pixels for RGB and alpha components separately for a particular draw buffer.

[OES_draw_buffers_indexed.colorMaskiOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/colorMaskiOES)

Sets which color components to enable or to disable when drawing or rendering for a particular draw buffer.

[OES_draw_buffers_indexed.disableiOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/disableiOES)

Disables blending for a particular draw buffer.

[OES_draw_buffers_indexed.enableiOES()](/en-US/docs/Web/API/OES_draw_buffers_indexed/enableiOES)

Enables blending for a particular draw buffer.

## [Examples](#examples)

### [Using the OES_draw_buffers_indexed extension](#using_the_oes_draw_buffers_indexed_extension)

Enable the extension with a call to [WebGLRenderingContext.getExtension()](/en-US/docs/Web/API/WebGLRenderingContext/getExtension).

js

```
const ext = gl.getExtension("OES_draw_buffers_indexed");
```

You can now enable blending, set blending equation, blending function, and color mask for a particular draw buffer.

js

```
// For gl.DRAW_BUFFER0
ext.enableiOES(gl.BLEND, 0);
ext.blendEquationiOES(0, gl.FUNC_ADD);
ext.blendFunciOES(0, gl.ONE, gl.ONE);
ext.colorMaskiOES(0, 1, 0, 0, 0);

// For gl.DRAW_BUFFER1
ext.enableiOES(gl.BLEND, 1);
ext.blendEquationSeparateiOES(1, gl.FUNC_ADD, gl.FUNC_SUBTRACT);
ext.blendFuncSeparateiOES(
  1,
  gl.SRC_ALPHA,
  gl.ONE_MINUS_SRC_ALPHA,
  gl.ZERO,
  gl.ZERO,
);
ext.colorMaskiOES(1, 0, 1, 0, 0);
```

To retrieve settings for a particular draw buffer, use [WebGL2RenderingContext.getIndexedParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getIndexedParameter).

js

```
// For gl.DRAW_BUFFER0
gl.getIndexedParameter(gl.BLEND_EQUATION_RGB, 0);
gl.getIndexedParameter(gl.BLEND_EQUATION_ALPHA, 0);
gl.getIndexedParameter(gl.BLEND_SRC_RGB, 0);
gl.getIndexedParameter(gl.BLEND_SRC_ALPHA, 0);
gl.getIndexedParameter(gl.BLEND_DST_RGB, 0);
gl.getIndexedParameter(gl.BLEND_DST_ALPHA, 0);
gl.getIndexedParameter(gl.COLOR_WRITEMASK, 0);

// For gl.DRAW_BUFFER1
gl.getIndexedParameter(gl.BLEND_EQUATION_RGB, 1);
gl.getIndexedParameter(gl.BLEND_EQUATION_ALPHA, 1);
gl.getIndexedParameter(gl.BLEND_SRC_RGB, 1);
gl.getIndexedParameter(gl.BLEND_SRC_ALPHA, 1);
gl.getIndexedParameter(gl.BLEND_DST_RGB, 1);
gl.getIndexedParameter(gl.BLEND_DST_ALPHA, 1);
gl.getIndexedParameter(gl.COLOR_WRITEMASK, 1);
```

You can use [WebGLRenderingContext.getParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getParameter) to see how many draw buffers are available.

js

```
const maxDrawBuffers = gl.getParameter(gl.MAX_DRAW_BUFFERS);
```

## [Specifications](#specifications)

Specification[WebGL OES_draw_buffers_indexed Extension Specification](https://registry.khronos.org/webgl/extensions/OES_draw_buffers_indexed/)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/OES_draw_buffers_indexed/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/oes_draw_buffers_indexed/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOES_draw_buffers_indexed&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Foes_draw_buffers_indexed%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOES_draw_buffers_indexed%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Foes_draw_buffers_indexed%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
