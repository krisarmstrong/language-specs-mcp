# WebGLRenderingContext

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLRenderingContext&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WebGLRenderingContext` interface provides an interface to the OpenGL ES 2.0 graphics rendering context for the drawing surface of an HTML [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element.

To get an access to a WebGL context for 2D and/or 3D graphics rendering, call [getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext) on a `<canvas>` element, supplying "webgl" as the argument:

js

```
const canvas = document.getElementById("myCanvas");
const gl = canvas.getContext("webgl");
```

Once you have the WebGL rendering context for a canvas, you can render within it. The [WebGL tutorial](/en-US/docs/Web/API/WebGL_API/Tutorial) has more information, examples, and resources on how to get started with WebGL.

If you require a WebGL 2.0 context, see [WebGL2RenderingContext](/en-US/docs/Web/API/WebGL2RenderingContext); this supplies access to an implementation of OpenGL ES 3.0 graphics.

## In this article

- [Constants](#constants)
- [The WebGL context](#the_webgl_context)
- [Viewing and clipping](#viewing_and_clipping)
- [State information](#state_information)
- [Buffers](#buffers)
- [Framebuffers](#framebuffers)
- [Renderbuffers](#renderbuffers)
- [Textures](#textures)
- [Programs and shaders](#programs_and_shaders)
- [Uniforms and attributes](#uniforms_and_attributes)
- [Drawing buffers](#drawing_buffers)
- [Color spaces](#color_spaces)
- [Working with extensions](#working_with_extensions)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constants](#constants)

See the [WebGL constants](/en-US/docs/Web/API/WebGL_API/Constants) page.

## [The WebGL context](#the_webgl_context)

The following properties and methods provide general information and functionality to deal with the WebGL context:

[WebGLRenderingContext.canvas](/en-US/docs/Web/API/WebGLRenderingContext/canvas)

A read-only back-reference to the [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement). Might be [null](/en-US/docs/Web/JavaScript/Reference/Operators/null) if it is not associated with a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element.

[WebGLRenderingContext.drawingBufferWidth](/en-US/docs/Web/API/WebGLRenderingContext/drawingBufferWidth)

The read-only width of the current drawing buffer. Should match the width of the canvas element associated with this context.

[WebGLRenderingContext.drawingBufferHeight](/en-US/docs/Web/API/WebGLRenderingContext/drawingBufferHeight)

The read-only height of the current drawing buffer. Should match the height of the canvas element associated with this context.

[WebGLRenderingContext.getContextAttributes()](/en-US/docs/Web/API/WebGLRenderingContext/getContextAttributes)

Returns a `WebGLContextAttributes` object that contains the actual context parameters. Might return [null](/en-US/docs/Web/JavaScript/Reference/Operators/null), if the context is lost.

[WebGLRenderingContext.isContextLost()](/en-US/docs/Web/API/WebGLRenderingContext/isContextLost)

Returns `true` if the context is lost, otherwise returns `false`.

[WebGLRenderingContext.makeXRCompatible()](/en-US/docs/Web/API/WebGLRenderingContext/makeXRCompatible)

Ensures the context is compatible with the user's XR hardware, re-creating the context if necessary with a new configuration to do so. This can be used to start an application using standard 2D presentation, then transition to using a VR or AR mode later.

## [Viewing and clipping](#viewing_and_clipping)

[WebGLRenderingContext.scissor()](/en-US/docs/Web/API/WebGLRenderingContext/scissor)

Defines the scissor box.

[WebGLRenderingContext.viewport()](/en-US/docs/Web/API/WebGLRenderingContext/viewport)

Sets the viewport.

## [State information](#state_information)

[WebGLRenderingContext.activeTexture()](/en-US/docs/Web/API/WebGLRenderingContext/activeTexture)

Selects the active texture unit.

[WebGLRenderingContext.blendColor()](/en-US/docs/Web/API/WebGLRenderingContext/blendColor)

Sets the source and destination blending factors.

[WebGLRenderingContext.blendEquation()](/en-US/docs/Web/API/WebGLRenderingContext/blendEquation)

Sets both the RGB blend equation and alpha blend equation to a single equation.

[WebGLRenderingContext.blendEquationSeparate()](/en-US/docs/Web/API/WebGLRenderingContext/blendEquationSeparate)

Sets the RGB blend equation and alpha blend equation separately.

[WebGLRenderingContext.blendFunc()](/en-US/docs/Web/API/WebGLRenderingContext/blendFunc)

Defines which function is used for blending pixel arithmetic.

[WebGLRenderingContext.blendFuncSeparate()](/en-US/docs/Web/API/WebGLRenderingContext/blendFuncSeparate)

Defines which function is used for blending pixel arithmetic for RGB and alpha components separately.

[WebGLRenderingContext.clearColor()](/en-US/docs/Web/API/WebGLRenderingContext/clearColor)

Specifies the color values used when clearing color buffers.

[WebGLRenderingContext.clearDepth()](/en-US/docs/Web/API/WebGLRenderingContext/clearDepth)

Specifies the depth value used when clearing the depth buffer.

[WebGLRenderingContext.clearStencil()](/en-US/docs/Web/API/WebGLRenderingContext/clearStencil)

Specifies the stencil value used when clearing the stencil buffer.

[WebGLRenderingContext.colorMask()](/en-US/docs/Web/API/WebGLRenderingContext/colorMask)

Sets which color components to enable or to disable when drawing or rendering to a [WebGLFramebuffer](/en-US/docs/Web/API/WebGLFramebuffer).

[WebGLRenderingContext.cullFace()](/en-US/docs/Web/API/WebGLRenderingContext/cullFace)

Specifies whether or not front- and/or back-facing polygons can be culled.

[WebGLRenderingContext.depthFunc()](/en-US/docs/Web/API/WebGLRenderingContext/depthFunc)

Specifies a function that compares incoming pixel depth to the current depth buffer value.

[WebGLRenderingContext.depthMask()](/en-US/docs/Web/API/WebGLRenderingContext/depthMask)

Sets whether writing into the depth buffer is enabled or disabled.

[WebGLRenderingContext.depthRange()](/en-US/docs/Web/API/WebGLRenderingContext/depthRange)

Specifies the depth range mapping from normalized device coordinates to window or viewport coordinates.

[WebGLRenderingContext.disable()](/en-US/docs/Web/API/WebGLRenderingContext/disable)

Disables specific WebGL capabilities for this context.

[WebGLRenderingContext.enable()](/en-US/docs/Web/API/WebGLRenderingContext/enable)

Enables specific WebGL capabilities for this context.

[WebGLRenderingContext.frontFace()](/en-US/docs/Web/API/WebGLRenderingContext/frontFace)

Specifies whether polygons are front- or back-facing by setting a winding orientation.

[WebGLRenderingContext.getParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getParameter)

Returns a value for the passed parameter name.

[WebGLRenderingContext.getError()](/en-US/docs/Web/API/WebGLRenderingContext/getError)

Returns error information.

[WebGLRenderingContext.hint()](/en-US/docs/Web/API/WebGLRenderingContext/hint)

Specifies hints for certain behaviors. The interpretation of these hints depend on the implementation.

[WebGLRenderingContext.isEnabled()](/en-US/docs/Web/API/WebGLRenderingContext/isEnabled)

Tests whether a specific WebGL capability is enabled or not for this context.

[WebGLRenderingContext.lineWidth()](/en-US/docs/Web/API/WebGLRenderingContext/lineWidth)

Sets the line width of rasterized lines.

[WebGLRenderingContext.pixelStorei()](/en-US/docs/Web/API/WebGLRenderingContext/pixelStorei)

Specifies the pixel storage modes

[WebGLRenderingContext.polygonOffset()](/en-US/docs/Web/API/WebGLRenderingContext/polygonOffset)

Specifies the scale factors and units to calculate depth values.

[WebGLRenderingContext.sampleCoverage()](/en-US/docs/Web/API/WebGLRenderingContext/sampleCoverage)

Specifies multi-sample coverage parameters for anti-aliasing effects.

[WebGLRenderingContext.stencilFunc()](/en-US/docs/Web/API/WebGLRenderingContext/stencilFunc)

Sets the both front and back function and reference value for stencil testing.

[WebGLRenderingContext.stencilFuncSeparate()](/en-US/docs/Web/API/WebGLRenderingContext/stencilFuncSeparate)

Sets the front and/or back function and reference value for stencil testing.

[WebGLRenderingContext.stencilMask()](/en-US/docs/Web/API/WebGLRenderingContext/stencilMask)

Controls enabling and disabling of both the front and back writing of individual bits in the stencil planes.

[WebGLRenderingContext.stencilMaskSeparate()](/en-US/docs/Web/API/WebGLRenderingContext/stencilMaskSeparate)

Controls enabling and disabling of front and/or back writing of individual bits in the stencil planes.

[WebGLRenderingContext.stencilOp()](/en-US/docs/Web/API/WebGLRenderingContext/stencilOp)

Sets both the front and back-facing stencil test actions.

[WebGLRenderingContext.stencilOpSeparate()](/en-US/docs/Web/API/WebGLRenderingContext/stencilOpSeparate)

Sets the front and/or back-facing stencil test actions.

## [Buffers](#buffers)

[WebGLRenderingContext.bindBuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindBuffer)

Binds a `WebGLBuffer` object to a given target.

[WebGLRenderingContext.bufferData()](/en-US/docs/Web/API/WebGLRenderingContext/bufferData)

Updates buffer data.

[WebGLRenderingContext.bufferSubData()](/en-US/docs/Web/API/WebGLRenderingContext/bufferSubData)

Updates buffer data starting at a passed offset.

[WebGLRenderingContext.createBuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createBuffer)

Creates a `WebGLBuffer` object.

[WebGLRenderingContext.deleteBuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteBuffer)

Deletes a `WebGLBuffer` object.

[WebGLRenderingContext.getBufferParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getBufferParameter)

Returns information about the buffer.

[WebGLRenderingContext.isBuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isBuffer)

Returns a Boolean indicating if the passed buffer is valid.

## [Framebuffers](#framebuffers)

[WebGLRenderingContext.bindFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindFramebuffer)

Binds a `WebGLFrameBuffer` object to a given target.

[WebGLRenderingContext.checkFramebufferStatus()](/en-US/docs/Web/API/WebGLRenderingContext/checkFramebufferStatus)

Returns the status of the framebuffer.

[WebGLRenderingContext.createFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createFramebuffer)

Creates a `WebGLFrameBuffer` object.

[WebGLRenderingContext.deleteFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteFramebuffer)

Deletes a `WebGLFrameBuffer` object.

[WebGLRenderingContext.framebufferRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferRenderbuffer)

Attaches a `WebGLRenderingBuffer` object to a `WebGLFrameBuffer` object.

[WebGLRenderingContext.framebufferTexture2D()](/en-US/docs/Web/API/WebGLRenderingContext/framebufferTexture2D)

Attaches a textures image to a `WebGLFrameBuffer` object.

[WebGLRenderingContext.getFramebufferAttachmentParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getFramebufferAttachmentParameter)

Returns information about the framebuffer.

[WebGLRenderingContext.isFramebuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isFramebuffer)

Returns a Boolean indicating if the passed `WebGLFrameBuffer` object is valid.

[WebGLRenderingContext.readPixels()](/en-US/docs/Web/API/WebGLRenderingContext/readPixels)

Reads a block of pixels from the `WebGLFrameBuffer`.

## [Renderbuffers](#renderbuffers)

[WebGLRenderingContext.bindRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/bindRenderbuffer)

Binds a `WebGLRenderBuffer` object to a given target.

[WebGLRenderingContext.createRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/createRenderbuffer)

Creates a `WebGLRenderBuffer` object.

[WebGLRenderingContext.deleteRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/deleteRenderbuffer)

Deletes a `WebGLRenderBuffer` object.

[WebGLRenderingContext.getRenderbufferParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getRenderbufferParameter)

Returns information about the renderbuffer.

[WebGLRenderingContext.isRenderbuffer()](/en-US/docs/Web/API/WebGLRenderingContext/isRenderbuffer)

Returns a Boolean indicating if the passed `WebGLRenderingBuffer` is valid.

[WebGLRenderingContext.renderbufferStorage()](/en-US/docs/Web/API/WebGLRenderingContext/renderbufferStorage)

Creates a renderbuffer data store.

## [Textures](#textures)

[WebGLRenderingContext.bindTexture()](/en-US/docs/Web/API/WebGLRenderingContext/bindTexture)

Binds a `WebGLTexture` object to a given target.

[WebGLRenderingContext.compressedTexImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/compressedTexImage2D)

Specifies a 2D texture image in a compressed format.

[WebGLRenderingContext.compressedTexSubImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/compressedTexSubImage2D)

Specifies a 2D texture sub-image in a compressed format.

[WebGLRenderingContext.copyTexImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/copyTexImage2D)

Copies a 2D texture image.

[WebGLRenderingContext.copyTexSubImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/copyTexSubImage2D)

Copies a 2D texture sub-image.

[WebGLRenderingContext.createTexture()](/en-US/docs/Web/API/WebGLRenderingContext/createTexture)

Creates a `WebGLTexture` object.

[WebGLRenderingContext.deleteTexture()](/en-US/docs/Web/API/WebGLRenderingContext/deleteTexture)

Deletes a `WebGLTexture` object.

[WebGLRenderingContext.generateMipmap()](/en-US/docs/Web/API/WebGLRenderingContext/generateMipmap)

Generates a set of mipmaps for a `WebGLTexture` object.

[WebGLRenderingContext.getTexParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getTexParameter)

Returns information about the texture.

[WebGLRenderingContext.isTexture()](/en-US/docs/Web/API/WebGLRenderingContext/isTexture)

Returns a Boolean indicating if the passed `WebGLTexture` is valid.

[WebGLRenderingContext.texImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/texImage2D)

Specifies a 2D texture image.

[WebGLRenderingContext.texSubImage2D()](/en-US/docs/Web/API/WebGLRenderingContext/texSubImage2D)

Updates a sub-rectangle of the current `WebGLTexture`.

[WebGLRenderingContext.texParameterf()](/en-US/docs/Web/API/WebGLRenderingContext/texParameter)

Sets texture parameters.

[WebGLRenderingContext.texParameteri()](/en-US/docs/Web/API/WebGLRenderingContext/texParameter)

Sets texture parameters.

## [Programs and shaders](#programs_and_shaders)

[WebGLRenderingContext.attachShader()](/en-US/docs/Web/API/WebGLRenderingContext/attachShader)

Attaches a `WebGLShader` to a `WebGLProgram`.

[WebGLRenderingContext.bindAttribLocation()](/en-US/docs/Web/API/WebGLRenderingContext/bindAttribLocation)

Binds a generic vertex index to a named attribute variable.

[WebGLRenderingContext.compileShader()](/en-US/docs/Web/API/WebGLRenderingContext/compileShader)

Compiles a `WebGLShader`.

[WebGLRenderingContext.createProgram()](/en-US/docs/Web/API/WebGLRenderingContext/createProgram)

Creates a `WebGLProgram`.

[WebGLRenderingContext.createShader()](/en-US/docs/Web/API/WebGLRenderingContext/createShader)

Creates a `WebGLShader`.

[WebGLRenderingContext.deleteProgram()](/en-US/docs/Web/API/WebGLRenderingContext/deleteProgram)

Deletes a `WebGLProgram`.

[WebGLRenderingContext.deleteShader()](/en-US/docs/Web/API/WebGLRenderingContext/deleteShader)

Deletes a `WebGLShader`.

[WebGLRenderingContext.detachShader()](/en-US/docs/Web/API/WebGLRenderingContext/detachShader)

Detaches a `WebGLShader`.

[WebGLRenderingContext.getAttachedShaders()](/en-US/docs/Web/API/WebGLRenderingContext/getAttachedShaders)

Returns a list of `WebGLShader` objects attached to a `WebGLProgram`.

[WebGLRenderingContext.getProgramParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getProgramParameter)

Returns information about the program.

[WebGLRenderingContext.getProgramInfoLog()](/en-US/docs/Web/API/WebGLRenderingContext/getProgramInfoLog)

Returns the information log for a `WebGLProgram` object.

[WebGLRenderingContext.getShaderParameter()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderParameter)

Returns information about the shader.

[WebGLRenderingContext.getShaderPrecisionFormat()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat)

Returns a `WebGLShaderPrecisionFormat` object describing the precision for the numeric format of the shader.

[WebGLRenderingContext.getShaderInfoLog()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderInfoLog)

Returns the information log for a `WebGLShader` object.

[WebGLRenderingContext.getShaderSource()](/en-US/docs/Web/API/WebGLRenderingContext/getShaderSource)

Returns the source code of a `WebGLShader` as a string.

[WebGLRenderingContext.isProgram()](/en-US/docs/Web/API/WebGLRenderingContext/isProgram)

Returns a Boolean indicating if the passed `WebGLProgram` is valid.

[WebGLRenderingContext.isShader()](/en-US/docs/Web/API/WebGLRenderingContext/isShader)

Returns a Boolean indicating if the passed `WebGLShader` is valid.

[WebGLRenderingContext.linkProgram()](/en-US/docs/Web/API/WebGLRenderingContext/linkProgram)

Links the passed `WebGLProgram` object.

[WebGLRenderingContext.shaderSource()](/en-US/docs/Web/API/WebGLRenderingContext/shaderSource)

Sets the source code in a `WebGLShader`.

[WebGLRenderingContext.useProgram()](/en-US/docs/Web/API/WebGLRenderingContext/useProgram)

Uses the specified `WebGLProgram` as part the current rendering state.

[WebGLRenderingContext.validateProgram()](/en-US/docs/Web/API/WebGLRenderingContext/validateProgram)

Validates a `WebGLProgram`.

## [Uniforms and attributes](#uniforms_and_attributes)

[WebGLRenderingContext.disableVertexAttribArray()](/en-US/docs/Web/API/WebGLRenderingContext/disableVertexAttribArray)

Disables a vertex attribute array at a given position.

[WebGLRenderingContext.enableVertexAttribArray()](/en-US/docs/Web/API/WebGLRenderingContext/enableVertexAttribArray)

Enables a vertex attribute array at a given position.

[WebGLRenderingContext.getActiveAttrib()](/en-US/docs/Web/API/WebGLRenderingContext/getActiveAttrib)

Returns information about an active attribute variable.

[WebGLRenderingContext.getActiveUniform()](/en-US/docs/Web/API/WebGLRenderingContext/getActiveUniform)

Returns information about an active uniform variable.

[WebGLRenderingContext.getAttribLocation()](/en-US/docs/Web/API/WebGLRenderingContext/getAttribLocation)

Returns the location of an attribute variable.

[WebGLRenderingContext.getUniform()](/en-US/docs/Web/API/WebGLRenderingContext/getUniform)

Returns the value of a uniform variable at a given location.

[WebGLRenderingContext.getUniformLocation()](/en-US/docs/Web/API/WebGLRenderingContext/getUniformLocation)

Returns the location of a uniform variable.

[WebGLRenderingContext.getVertexAttrib()](/en-US/docs/Web/API/WebGLRenderingContext/getVertexAttrib)

Returns information about a vertex attribute at a given position.

[WebGLRenderingContext.getVertexAttribOffset()](/en-US/docs/Web/API/WebGLRenderingContext/getVertexAttribOffset)

Returns the address of a given vertex attribute.

[WebGLRenderingContext.uniform[1234][fi][v]()](/en-US/docs/Web/API/WebGLRenderingContext/uniform)

Specifies a value for a uniform variable.

[WebGLRenderingContext.uniformMatrix[234]fv()](/en-US/docs/Web/API/WebGLRenderingContext/uniformMatrix)

Specifies a matrix value for a uniform variable.

[WebGLRenderingContext.vertexAttrib[1234]f[v]()](/en-US/docs/Web/API/WebGLRenderingContext/vertexAttrib)

Specifies a value for a generic vertex attribute.

[WebGLRenderingContext.vertexAttribPointer()](/en-US/docs/Web/API/WebGLRenderingContext/vertexAttribPointer)

Specifies the data formats and locations of vertex attributes in a vertex attributes array.

## [Drawing buffers](#drawing_buffers)

[WebGLRenderingContext.clear()](/en-US/docs/Web/API/WebGLRenderingContext/clear)

Clears specified buffers to preset values.

[WebGLRenderingContext.drawArrays()](/en-US/docs/Web/API/WebGLRenderingContext/drawArrays)

Renders primitives from array data.

[WebGLRenderingContext.drawElements()](/en-US/docs/Web/API/WebGLRenderingContext/drawElements)

Renders primitives from element array data.

[WebGLRenderingContext.finish()](/en-US/docs/Web/API/WebGLRenderingContext/finish)

Blocks execution until all previously called commands are finished.

[WebGLRenderingContext.flush()](/en-US/docs/Web/API/WebGLRenderingContext/flush)

Empties different buffer commands, causing all commands to be executed as quickly as possible.

## [Color spaces](#color_spaces)

[WebGLRenderingContext.drawingBufferColorSpace](/en-US/docs/Web/API/WebGLRenderingContext/drawingBufferColorSpace)

Specifies the color space of the WebGL drawing buffer.

[WebGLRenderingContext.unpackColorSpace](/en-US/docs/Web/API/WebGLRenderingContext/unpackColorSpace)

Specifies the color space to convert to when importing textures.

## [Working with extensions](#working_with_extensions)

These methods manage WebGL extensions:

[WebGLRenderingContext.getSupportedExtensions()](/en-US/docs/Web/API/WebGLRenderingContext/getSupportedExtensions)

Returns an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of strings containing all the supported WebGL extensions.

[WebGLRenderingContext.getExtension()](/en-US/docs/Web/API/WebGLRenderingContext/getExtension)

Returns an extension object.

## [Specifications](#specifications)

Specification
[WebGL Specification# 5.14](https://registry.khronos.org/webgl/specs/latest/1.0/#5.14)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 9, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGLRenderingContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webglrenderingcontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLRenderingContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebglrenderingcontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGLRenderingContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebglrenderingcontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F47962c4ebad5a138673422ec63a282ab9a63d454%0A*+Document+last+modified%3A+2024-10-09T04%3A58%3A03.000Z%0A%0A%3C%2Fdetails%3E)
