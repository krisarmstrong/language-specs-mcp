# GPURenderPassEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderPassEncoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPURenderPassEncoder` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) encodes commands related to controlling the vertex and fragment shader stages, as issued by a [GPURenderPipeline](/en-US/docs/Web/API/GPURenderPipeline). It forms part of the overall encoding activity of a [GPUCommandEncoder](/en-US/docs/Web/API/GPUCommandEncoder).

A render pipeline renders graphics to [GPUTexture](/en-US/docs/Web/API/GPUTexture) attachments, typically intended for display in a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element, but it could also render to textures used for other purposes that never appear onscreen. It has two main stages:

- 

A vertex stage, in which a vertex shader takes positioning data fed into the GPU and uses it to position a series of vertices in 3D space by applying specified effects like rotation, translation, or perspective. The vertices are then assembled into primitives such as triangles (the basic building block of rendered graphics) and rasterized by the GPU to figure out what pixels each one should cover on the drawing canvas.

- 

A fragment stage, in which a fragment shader computes the color for each pixel covered by the primitives produced by the vertex shader. These computations frequently use inputs such as images (in the form of textures) that provide surface details and the position and color of virtual lights.

A `GPURenderPassEncoder` object instance is created via the [GPUCommandEncoder.beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPURenderPassEncoder/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Instance methods](#instance_methods)

[beginOcclusionQuery()](/en-US/docs/Web/API/GPURenderPassEncoder/beginOcclusionQuery)

Begins an occlusion query at the specified index of the relevant [GPUQuerySet](/en-US/docs/Web/API/GPUQuerySet) (provided as the value of the `occlusionQuerySet` descriptor property when invoking [GPUCommandEncoder.beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass) to run the render pass).

[draw()](/en-US/docs/Web/API/GPURenderPassEncoder/draw)

Draw primitives based on the vertex buffers provided by [setVertexBuffer()](/en-US/docs/Web/API/GPURenderPassEncoder/setVertexBuffer).

[drawIndexed()](/en-US/docs/Web/API/GPURenderPassEncoder/drawIndexed)

Draw indexed primitives based on the vertex and index buffers provided by [setVertexBuffer()](/en-US/docs/Web/API/GPURenderPassEncoder/setVertexBuffer) and [setIndexBuffer()](/en-US/docs/Web/API/GPURenderPassEncoder/setIndexBuffer)

[drawIndirect()](/en-US/docs/Web/API/GPURenderPassEncoder/drawIndirect)

Draw primitives using parameters read from a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer).

[drawIndexedIndirect()](/en-US/docs/Web/API/GPURenderPassEncoder/drawIndexedIndirect)

Draw indexed primitives using parameters read from a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer).

[end()](/en-US/docs/Web/API/GPURenderPassEncoder/end)

Completes recording of the current render pass command sequence.

[endOcclusionQuery()](/en-US/docs/Web/API/GPURenderPassEncoder/endOcclusionQuery)

Ends an active occlusion query previously started with [beginOcclusionQuery()](/en-US/docs/Web/API/GPURenderPassEncoder/beginOcclusionQuery).

[executeBundles()](/en-US/docs/Web/API/GPURenderPassEncoder/executeBundles)

Executes commands previously recorded into the referenced [GPURenderBundle](/en-US/docs/Web/API/GPURenderBundle)s, as part of this render pass.

[insertDebugMarker()](/en-US/docs/Web/API/GPURenderPassEncoder/insertDebugMarker)

Marks a specific point in a series of encoded commands with a label.

[popDebugGroup()](/en-US/docs/Web/API/GPURenderPassEncoder/popDebugGroup)

Ends a debug group, which is begun with a [pushDebugGroup()](/en-US/docs/Web/API/GPURenderPassEncoder/pushDebugGroup) call.

[pushDebugGroup()](/en-US/docs/Web/API/GPURenderPassEncoder/pushDebugGroup)

Begins a debug group, which is marked with a specified label, and will contain all subsequent encoded commands up until a [popDebugGroup()](/en-US/docs/Web/API/GPURenderPassEncoder/popDebugGroup) method is invoked.

[setBindGroup()](/en-US/docs/Web/API/GPURenderPassEncoder/setBindGroup)

Sets the [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup) to use for subsequent render commands, for a given index.

[setBlendConstant()](/en-US/docs/Web/API/GPURenderPassEncoder/setBlendConstant)

Sets the constant blend color and alpha values used with `"constant"` and `"one-minus-constant"` blend factors (as set in the descriptor of the [GPUDevice.createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline) method, in the `blend` property).

[setIndexBuffer()](/en-US/docs/Web/API/GPURenderPassEncoder/setIndexBuffer)

Sets the current [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) that will provide index data for subsequent drawing commands.

[setPipeline()](/en-US/docs/Web/API/GPURenderPassEncoder/setPipeline)

Sets the [GPURenderPipeline](/en-US/docs/Web/API/GPURenderPipeline) to use for this render pass.

[setScissorRect()](/en-US/docs/Web/API/GPURenderPassEncoder/setScissorRect)

Sets the scissor rectangle used during the rasterization stage. After transformation into viewport coordinates any fragments that fall outside the scissor rectangle will be discarded.

[setStencilReference()](/en-US/docs/Web/API/GPURenderPassEncoder/setStencilReference)

Sets the stencil reference value using during stencil tests with the `"replace"` stencil operation (as set in the descriptor of the [GPUDevice.createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline) method, in the properties defining the various stencil operations).

[setVertexBuffer()](/en-US/docs/Web/API/GPURenderPassEncoder/setVertexBuffer)

Sets or unsets the current [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) that will provide vertex data for subsequent drawing commands.

[setViewport()](/en-US/docs/Web/API/GPURenderPassEncoder/setViewport)

Sets the viewport used during the rasterization stage to linearly map from normalized device coordinates to viewport coordinates.

## [Examples](#examples)

In our [basic render demo](https://mdn.github.io/dom-examples/webgpu-render-demo/), several commands are recorded via a [GPUCommandEncoder](/en-US/docs/Web/API/GPUCommandEncoder). Most of these commands originate from the `GPURenderPassEncoder` created via [GPUCommandEncoder.beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass).

js

```
// …

const renderPipeline = device.createRenderPipeline(pipelineDescriptor);

// Create GPUCommandEncoder to issue commands to the GPU
// Note: render pass descriptor, command encoder, etc. are destroyed after use, fresh one needed for each frame.
const commandEncoder = device.createCommandEncoder();

// Create GPURenderPassDescriptor to tell WebGPU which texture to draw into, then initiate render pass
const renderPassDescriptor = {
  colorAttachments: [
    {
      clearValue: clearColor,
      loadOp: "clear",
      storeOp: "store",
      view: context.getCurrentTexture().createView(),
    },
  ],
};

const passEncoder = commandEncoder.beginRenderPass(renderPassDescriptor);

// Draw the triangle
passEncoder.setPipeline(renderPipeline);
passEncoder.setVertexBuffer(0, vertexBuffer);
passEncoder.draw(3);

// End the render pass
passEncoder.end();

// End frame by passing array of command buffers to command queue for execution
device.queue.submit([commandEncoder.finish()]);

// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpurenderpassencoder](https://gpuweb.github.io/gpuweb/#gpurenderpassencoder)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPURenderPassEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpurenderpassencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderPassEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpurenderpassencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderPassEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpurenderpassencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
