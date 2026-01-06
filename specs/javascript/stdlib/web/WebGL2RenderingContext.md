# WebGL2RenderingContext

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL2RenderingContext&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The WebGL2RenderingContext interface provides the OpenGL ES 3.0 rendering context for the drawing surface of an HTML [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element.

To get an object of this interface, call [getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext) on a `<canvas>` element, supplying "webgl2" as the argument:

js

```
const canvas = document.getElementById("myCanvas");
const gl = canvas.getContext("webgl2");
```

Note: WebGL 2 is an extension to WebGL 1. The `WebGL2RenderingContext` interface implements all members of the [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext) interface. Some methods of the WebGL 1 context can accept additional values when used in a WebGL 2 context. You will find this info noted on the WebGL 1 reference pages.

The [WebGL tutorial](/en-US/docs/Web/API/WebGL_API/Tutorial) has more information, examples, and resources on how to get started with WebGL.

## In this article

- [Constants](#constants)
- [State information](#state_information)
- [Buffers](#buffers)
- [Framebuffers](#framebuffers)
- [Renderbuffers](#renderbuffers)
- [Textures](#textures)
- [Programs and shaders](#programs_and_shaders)
- [Uniforms and attributes](#uniforms_and_attributes)
- [Color spaces](#color_spaces)
- [Drawing buffers](#drawing_buffers)
- [Query objects](#query_objects)
- [Sampler objects](#sampler_objects)
- [Sync objects](#sync_objects)
- [Transform feedback](#transform_feedback)
- [Uniform buffer objects](#uniform_buffer_objects)
- [Vertex array objects](#vertex_array_objects)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constants](#constants)

See the [WebGL constants](/en-US/docs/Web/API/WebGL_API/Constants) page.

## [State information](#state_information)

[WebGL2RenderingContext.getIndexedParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getIndexedParameter)

Returns the indexed value for the given `target`.

## [Buffers](#buffers)

[WebGL2RenderingContext.bufferData()](/en-US/docs/Web/API/WebGL2RenderingContext/bufferData)

Initializes and creates the buffer object's data store.

[WebGL2RenderingContext.bufferSubData()](/en-US/docs/Web/API/WebGL2RenderingContext/bufferSubData)

Updates a subset of a buffer object's data store.

[WebGL2RenderingContext.copyBufferSubData()](/en-US/docs/Web/API/WebGL2RenderingContext/copyBufferSubData)

Copies part of the data of a buffer to another buffer.

[WebGL2RenderingContext.getBufferSubData()](/en-US/docs/Web/API/WebGL2RenderingContext/getBufferSubData)

Reads data from a buffer and writes them to an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) or [SharedArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer).

## [Framebuffers](#framebuffers)

[WebGL2RenderingContext.blitFramebuffer()](/en-US/docs/Web/API/WebGL2RenderingContext/blitFramebuffer)

Transfers a block of pixels from the read framebuffer to the draw framebuffer.

[WebGL2RenderingContext.framebufferTextureLayer()](/en-US/docs/Web/API/WebGL2RenderingContext/framebufferTextureLayer)

Attaches a single layer of a texture to a framebuffer.

[WebGL2RenderingContext.invalidateFramebuffer()](/en-US/docs/Web/API/WebGL2RenderingContext/invalidateFramebuffer)

Invalidates the contents of attachments in a framebuffer.

[WebGL2RenderingContext.invalidateSubFramebuffer()](/en-US/docs/Web/API/WebGL2RenderingContext/invalidateSubFramebuffer)

Invalidates portions of the contents of attachments in a framebuffer

[WebGL2RenderingContext.readBuffer()](/en-US/docs/Web/API/WebGL2RenderingContext/readBuffer)

Selects a color buffer as the source for pixels.

## [Renderbuffers](#renderbuffers)

[WebGL2RenderingContext.getInternalformatParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getInternalformatParameter)

Returns information about implementation-dependent support for internal formats.

[WebGL2RenderingContext.renderbufferStorageMultisample()](/en-US/docs/Web/API/WebGL2RenderingContext/renderbufferStorageMultisample)

Creates and initializes a renderbuffer object's data store and allows specifying the number of samples to be used.

## [Textures](#textures)

[WebGL2RenderingContext.texStorage2D()](/en-US/docs/Web/API/WebGL2RenderingContext/texStorage2D)

Specifies all levels of two-dimensional texture storage.

[WebGL2RenderingContext.texStorage3D()](/en-US/docs/Web/API/WebGL2RenderingContext/texStorage3D)

Specifies all levels of a three-dimensional texture or two-dimensional array texture.

[WebGL2RenderingContext.texImage3D()](/en-US/docs/Web/API/WebGL2RenderingContext/texImage3D)

Specifies a three-dimensional texture image.

[WebGL2RenderingContext.texSubImage3D()](/en-US/docs/Web/API/WebGL2RenderingContext/texSubImage3D)

Specifies a sub-rectangle of the current 3D texture.

[WebGL2RenderingContext.copyTexSubImage3D()](/en-US/docs/Web/API/WebGL2RenderingContext/copyTexSubImage3D)

Copies pixels from the current [WebGLFramebuffer](/en-US/docs/Web/API/WebGLFramebuffer) into an existing 3D texture sub-image.

[WebGL2RenderingContext.compressedTexImage3D](/en-US/docs/Web/API/WebGL2RenderingContext/compressedTexImage3D)

Specifies a three-dimensional texture image in a compressed format.

[WebGL2RenderingContext.compressedTexSubImage3D()](/en-US/docs/Web/API/WebGL2RenderingContext/compressedTexSubImage3D)

Specifies a three-dimensional sub-rectangle for a texture image in a compressed format.

## [Programs and shaders](#programs_and_shaders)

[WebGL2RenderingContext.getFragDataLocation()](/en-US/docs/Web/API/WebGL2RenderingContext/getFragDataLocation)

Returns the binding of color numbers to user-defined varying out variables.

## [Uniforms and attributes](#uniforms_and_attributes)

[WebGL2RenderingContext.uniform[1234][uif][v]()](/en-US/docs/Web/API/WebGL2RenderingContext/uniform)

Methods specifying values of uniform variables.

[WebGL2RenderingContext.uniformMatrix[234]x[234]fv()](/en-US/docs/Web/API/WebGL2RenderingContext/uniformMatrix)

Methods specifying matrix values for uniform variables.

[WebGL2RenderingContext.vertexAttribI4[u]i[v]()](/en-US/docs/Web/API/WebGL2RenderingContext/vertexAttribI)

Methods specifying integer values for generic vertex attributes.

[WebGL2RenderingContext.vertexAttribIPointer()](/en-US/docs/Web/API/WebGL2RenderingContext/vertexAttribIPointer)

Specifies integer data formats and locations of vertex attributes in a vertex attributes array.

## [Color spaces](#color_spaces)

[WebGL2RenderingContext.drawingBufferColorSpace](/en-US/docs/Web/API/WebGL2RenderingContext/drawingBufferColorSpace)

Specifies the color space of the WebGL drawing buffer.

[WebGL2RenderingContext.unpackColorSpace](/en-US/docs/Web/API/WebGL2RenderingContext/unpackColorSpace)

Specifies the color space to convert to when importing textures.

## [Drawing buffers](#drawing_buffers)

[WebGL2RenderingContext.vertexAttribDivisor()](/en-US/docs/Web/API/WebGL2RenderingContext/vertexAttribDivisor)

Modifies the rate at which generic vertex attributes advance when rendering multiple instances of primitives with [gl.drawArraysInstanced()](/en-US/docs/Web/API/WebGL2RenderingContext/drawArraysInstanced) and [gl.drawElementsInstanced()](/en-US/docs/Web/API/WebGL2RenderingContext/drawElementsInstanced).

[WebGL2RenderingContext.drawArraysInstanced()](/en-US/docs/Web/API/WebGL2RenderingContext/drawArraysInstanced)

Renders primitives from array data. In addition, it can execute multiple instances of the range of elements.

[WebGL2RenderingContext.drawElementsInstanced()](/en-US/docs/Web/API/WebGL2RenderingContext/drawElementsInstanced)

Renders primitives from array data. In addition, it can execute multiple instances of a set of elements.

[WebGL2RenderingContext.drawRangeElements()](/en-US/docs/Web/API/WebGL2RenderingContext/drawRangeElements)

Renders primitives from array data in a given range.

[WebGL2RenderingContext.drawBuffers()](/en-US/docs/Web/API/WebGL2RenderingContext/drawBuffers)

Specifies a list of color buffers to be drawn into.

[WebGL2RenderingContext.clearBuffer[fiuv]()](/en-US/docs/Web/API/WebGL2RenderingContext/clearBuffer)

Clears buffers from the currently bound framebuffer.

## [Query objects](#query_objects)

Methods for working with [WebGLQuery](/en-US/docs/Web/API/WebGLQuery) objects.

[WebGL2RenderingContext.createQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/createQuery)

Creates a new [WebGLQuery](/en-US/docs/Web/API/WebGLQuery) object.

[WebGL2RenderingContext.deleteQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteQuery)

Deletes a given [WebGLQuery](/en-US/docs/Web/API/WebGLQuery) object.

[WebGL2RenderingContext.isQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/isQuery)

Returns `true` if a given object is a valid [WebGLQuery](/en-US/docs/Web/API/WebGLQuery) object.

[WebGL2RenderingContext.beginQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/beginQuery)

Begins an asynchronous query.

[WebGL2RenderingContext.endQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/endQuery)

Marks the end of an asynchronous query.

[WebGL2RenderingContext.getQuery()](/en-US/docs/Web/API/WebGL2RenderingContext/getQuery)

Returns a [WebGLQuery](/en-US/docs/Web/API/WebGLQuery) object for a given target.

[WebGL2RenderingContext.getQueryParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getQueryParameter)

Returns information about a query.

## [Sampler objects](#sampler_objects)

[WebGL2RenderingContext.createSampler()](/en-US/docs/Web/API/WebGL2RenderingContext/createSampler)

Creates a new [WebGLSampler](/en-US/docs/Web/API/WebGLSampler) object.

[WebGL2RenderingContext.deleteSampler()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteSampler)

Deletes a given [WebGLSampler](/en-US/docs/Web/API/WebGLSampler) object.

[WebGL2RenderingContext.bindSampler()](/en-US/docs/Web/API/WebGL2RenderingContext/bindSampler)

Binds a given [WebGLSampler](/en-US/docs/Web/API/WebGLSampler) to a texture unit.

[WebGL2RenderingContext.isSampler()](/en-US/docs/Web/API/WebGL2RenderingContext/isSampler)

Returns `true` if a given object is a valid [WebGLSampler](/en-US/docs/Web/API/WebGLSampler) object.

[WebGL2RenderingContext.samplerParameter[if]()](/en-US/docs/Web/API/WebGL2RenderingContext/samplerParameter)

Sets sampler parameters.

[WebGL2RenderingContext.getSamplerParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getSamplerParameter)

Returns sampler parameter information.

## [Sync objects](#sync_objects)

[WebGL2RenderingContext.fenceSync()](/en-US/docs/Web/API/WebGL2RenderingContext/fenceSync)

Creates a new [WebGLSync](/en-US/docs/Web/API/WebGLSync) object and inserts it into the GL command stream.

[WebGL2RenderingContext.isSync()](/en-US/docs/Web/API/WebGL2RenderingContext/isSync)

Returns `true` if the passed object is a valid [WebGLSync](/en-US/docs/Web/API/WebGLSync) object.

[WebGL2RenderingContext.deleteSync()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteSync)

Deletes a given [WebGLSync](/en-US/docs/Web/API/WebGLSync) object.

[WebGL2RenderingContext.clientWaitSync()](/en-US/docs/Web/API/WebGL2RenderingContext/clientWaitSync)

Blocks and waits for a [WebGLSync](/en-US/docs/Web/API/WebGLSync) object to become signaled or a given timeout to be passed.

[WebGL2RenderingContext.waitSync()](/en-US/docs/Web/API/WebGL2RenderingContext/waitSync)

Returns immediately, but waits on the GL server until the given [WebGLSync](/en-US/docs/Web/API/WebGLSync) object is signaled.

[WebGL2RenderingContext.getSyncParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getSyncParameter)

Returns parameter information of a [WebGLSync](/en-US/docs/Web/API/WebGLSync) object.

## [Transform feedback](#transform_feedback)

[WebGL2RenderingContext.createTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/createTransformFeedback)

Creates and initializes [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback) objects.

[WebGL2RenderingContext.deleteTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteTransformFeedback)

Deletes a given [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback) object.

[WebGL2RenderingContext.isTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/isTransformFeedback)

Returns `true` if the passed object is a valid [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback) object.

[WebGL2RenderingContext.bindTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/bindTransformFeedback)

Binds a passed [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback) object to the current GL state.

[WebGL2RenderingContext.beginTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/beginTransformFeedback)

Starts a transform feedback operation.

[WebGL2RenderingContext.endTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/endTransformFeedback)

Ends a transform feedback operation.

[WebGL2RenderingContext.transformFeedbackVaryings()](/en-US/docs/Web/API/WebGL2RenderingContext/transformFeedbackVaryings)

Specifies values to record in [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback) buffers.

[WebGL2RenderingContext.getTransformFeedbackVarying()](/en-US/docs/Web/API/WebGL2RenderingContext/getTransformFeedbackVarying)

Returns information about varying variables from [WebGLTransformFeedback](/en-US/docs/Web/API/WebGLTransformFeedback) buffers.

[WebGL2RenderingContext.pauseTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/pauseTransformFeedback)

Pauses a transform feedback operation.

[WebGL2RenderingContext.resumeTransformFeedback()](/en-US/docs/Web/API/WebGL2RenderingContext/resumeTransformFeedback)

Resumes a transform feedback operation.

## [Uniform buffer objects](#uniform_buffer_objects)

[WebGL2RenderingContext.bindBufferBase()](/en-US/docs/Web/API/WebGL2RenderingContext/bindBufferBase)

Binds a given [WebGLBuffer](/en-US/docs/Web/API/WebGLBuffer) to a given binding point (`target`) at a given `index`.

[WebGL2RenderingContext.bindBufferRange()](/en-US/docs/Web/API/WebGL2RenderingContext/bindBufferRange)

Binds a range of a given [WebGLBuffer](/en-US/docs/Web/API/WebGLBuffer) to a given binding point (`target`) at a given `index`.

[WebGL2RenderingContext.getUniformIndices()](/en-US/docs/Web/API/WebGL2RenderingContext/getUniformIndices)

Retrieves the indices of a number of uniforms within a [WebGLProgram](/en-US/docs/Web/API/WebGLProgram).

[WebGL2RenderingContext.getActiveUniforms()](/en-US/docs/Web/API/WebGL2RenderingContext/getActiveUniforms)

Retrieves information about active uniforms within a [WebGLProgram](/en-US/docs/Web/API/WebGLProgram).

[WebGL2RenderingContext.getUniformBlockIndex()](/en-US/docs/Web/API/WebGL2RenderingContext/getUniformBlockIndex)

Retrieves the index of a uniform block within a [WebGLProgram](/en-US/docs/Web/API/WebGLProgram).

[WebGL2RenderingContext.getActiveUniformBlockParameter()](/en-US/docs/Web/API/WebGL2RenderingContext/getActiveUniformBlockParameter)

Retrieves information about an active uniform block within a [WebGLProgram](/en-US/docs/Web/API/WebGLProgram).

[WebGL2RenderingContext.getActiveUniformBlockName()](/en-US/docs/Web/API/WebGL2RenderingContext/getActiveUniformBlockName)

Retrieves the name of the active uniform block at a given index within a [WebGLProgram](/en-US/docs/Web/API/WebGLProgram).

[WebGL2RenderingContext.uniformBlockBinding()](/en-US/docs/Web/API/WebGL2RenderingContext/uniformBlockBinding)

Assigns binding points for active uniform blocks.

## [Vertex array objects](#vertex_array_objects)

Methods for working with [WebGLVertexArrayObject](/en-US/docs/Web/API/WebGLVertexArrayObject) (VAO) objects.

[WebGL2RenderingContext.createVertexArray()](/en-US/docs/Web/API/WebGL2RenderingContext/createVertexArray)

Creates a new [WebGLVertexArrayObject](/en-US/docs/Web/API/WebGLVertexArrayObject).

[WebGL2RenderingContext.deleteVertexArray()](/en-US/docs/Web/API/WebGL2RenderingContext/deleteVertexArray)

Deletes a given [WebGLVertexArrayObject](/en-US/docs/Web/API/WebGLVertexArrayObject).

[WebGL2RenderingContext.isVertexArray()](/en-US/docs/Web/API/WebGL2RenderingContext/isVertexArray)

Returns `true` if a given object is a valid [WebGLVertexArrayObject](/en-US/docs/Web/API/WebGLVertexArrayObject).

[WebGL2RenderingContext.bindVertexArray()](/en-US/docs/Web/API/WebGL2RenderingContext/bindVertexArray)

Binds a given [WebGLVertexArrayObject](/en-US/docs/Web/API/WebGLVertexArrayObject) to the buffer.

## [Specifications](#specifications)

Specification
[WebGL 2.0 Specification# 3.7](https://registry.khronos.org/webgl/specs/latest/2.0/#3.7)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement)
- [WebGLRenderingContext](/en-US/docs/Web/API/WebGLRenderingContext)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 16, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WebGL2RenderingContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webgl2renderingcontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL2RenderingContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebgl2renderingcontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL2RenderingContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebgl2renderingcontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F72a2131decd44410a5c2acb9d4d5c1c7c6340e6a%0A*+Document+last+modified%3A+2024-10-16T04%3A56%3A41.000Z%0A%0A%3C%2Fdetails%3E)
