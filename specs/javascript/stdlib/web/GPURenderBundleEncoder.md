# GPURenderBundleEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderBundleEncoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPURenderBundleEncoder` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is used to pre-record bundles of commands.

The command bundles are encoded by calling the methods of `GPURenderBundleEncoder`; once the desired commands have been encoded, they are recorded into a [GPURenderBundle](/en-US/docs/Web/API/GPURenderBundle) object instance using the [GPURenderBundleEncoder.finish()](/en-US/docs/Web/API/GPURenderBundleEncoder/finish) method. These render bundles can then be reused across multiple render passes by passing the `GPURenderBundle` objects into [GPURenderPassEncoder.executeBundles()](/en-US/docs/Web/API/GPURenderPassEncoder/executeBundles) calls.

In effect, this is like a partial render pass — `GPURenderBundleEncoder`s have all the same functionality available as [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder)s, except that they can't begin and end occlusion queries, and can't set the scissor rect, viewport, blend constant, and stencil reference. The `GPURenderBundle` will inherit all these values from the [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder) that executes it.

Note: Currently set vertex buffers, index buffers, bind groups, and pipeline are all cleared prior to executing a render bundle, and once the render bundle has finished executing.

Reusing pre-recoded commands can significantly improve app performance in situations where JavaScript draw call overhead is a bottleneck. Render bundles are most effective in situations where a batch of objects will be drawn the same way across multiple views or frames, with the only differences being the buffer content being used (such as updated matrix uniforms). A good example is VR rendering. Recording the rendering as a render bundle and then tweaking the view matrix and replaying it for each eye is a more efficient way to issue draw calls for both renderings of the scene.

A `GPURenderBundleEncoder` object instance is created via the [GPUDevice.createRenderBundleEncoder()](/en-US/docs/Web/API/GPUDevice/createRenderBundleEncoder) property.

Note: The methods of `GPURenderBundleEncoder` are functionally identical to their equivalents available on [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder), except for [GPURenderBundleEncoder.finish()](/en-US/docs/Web/API/GPURenderBundleEncoder/finish), which is similar in purpose to [GPUCommandEncoder.finish()](/en-US/docs/Web/API/GPUCommandEncoder/finish).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPURenderBundleEncoder/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Instance methods](#instance_methods)

[draw()](/en-US/docs/Web/API/GPURenderBundleEncoder/draw)

Draw primitives based on the vertex buffers provided by [setVertexBuffer()](/en-US/docs/Web/API/GPURenderBundleEncoder/setVertexBuffer).

[drawIndexed()](/en-US/docs/Web/API/GPURenderBundleEncoder/drawIndexed)

Draw indexed primitives based on the vertex and index buffers provided by [setVertexBuffer()](/en-US/docs/Web/API/GPURenderBundleEncoder/setVertexBuffer) and [setIndexBuffer()](/en-US/docs/Web/API/GPURenderBundleEncoder/setIndexBuffer)

[drawIndirect()](/en-US/docs/Web/API/GPURenderBundleEncoder/drawIndirect)

Draw primitives using parameters read from a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer).

[drawIndexedIndirect()](/en-US/docs/Web/API/GPURenderBundleEncoder/drawIndexedIndirect)

Draw indexed primitives using parameters read from a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer).

[finish()](/en-US/docs/Web/API/GPURenderBundleEncoder/finish)

Completes recording of the current render pass command sequence.

[insertDebugMarker()](/en-US/docs/Web/API/GPURenderBundleEncoder/insertDebugMarker)

Marks a specific point in a series of encoded commands with a label.

[popDebugGroup()](/en-US/docs/Web/API/GPURenderBundleEncoder/popDebugGroup)

Ends a debug group, which is begun with a [pushDebugGroup()](/en-US/docs/Web/API/GPURenderBundleEncoder/pushDebugGroup) call.

[pushDebugGroup()](/en-US/docs/Web/API/GPURenderBundleEncoder/pushDebugGroup)

Begins a debug group, which is marked with a specified label, and will contain all subsequent encoded commands up until a [popDebugGroup()](/en-US/docs/Web/API/GPURenderBundleEncoder/popDebugGroup) method is invoked.

[setBindGroup()](/en-US/docs/Web/API/GPURenderBundleEncoder/setBindGroup)

Sets the [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup) to use for subsequent render bundle commands, for a given index.

[setIndexBuffer()](/en-US/docs/Web/API/GPURenderBundleEncoder/setIndexBuffer)

Sets the current [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) that will provide index data for subsequent drawing commands.

[setPipeline()](/en-US/docs/Web/API/GPURenderBundleEncoder/setPipeline)

Sets the [GPURenderPipeline](/en-US/docs/Web/API/GPURenderPipeline) to use for this render bundle.

[setVertexBuffer()](/en-US/docs/Web/API/GPURenderBundleEncoder/setVertexBuffer)

Sets or unsets the current [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) that will provide vertex data for subsequent drawing commands.

## [Examples](#examples)

In the WebGPU Samples [Animometer example](https://webgpu.github.io/webgpu-samples/samples/animometer/), a lot of like operations are done on many different objects simultaneously. A bundle of commands is encoded using the following function:

js

```
function recordRenderPass(
  passEncoder: GPURenderBundleEncoder | GPURenderPassEncoder
) {
  if (settings.dynamicOffsets) {
    passEncoder.setPipeline(dynamicPipeline);
  } else {
    passEncoder.setPipeline(pipeline);
  }
  passEncoder.setVertexBuffer(0, vertexBuffer);
  passEncoder.setBindGroup(0, timeBindGroup);
  const dynamicOffsets = [0];
  for (let i = 0; i < numTriangles; ++i) {
    if (settings.dynamicOffsets) {
      dynamicOffsets[0] = i * alignedUniformBytes;
      passEncoder.setBindGroup(1, dynamicBindGroup, dynamicOffsets);
    } else {
      passEncoder.setBindGroup(1, bindGroups[i]);
    }
    passEncoder.draw(3, 1, 0, 0);
  }
}
```

Later on, a `GPURenderBundleEncoder` is created, the function is invoked, and the command bundle is recorded into a [GPURenderBundle](/en-US/docs/Web/API/GPURenderBundle) using [GPURenderBundleEncoder.finish()](/en-US/docs/Web/API/GPURenderBundleEncoder/finish):

js

```
const renderBundleEncoder = device.createRenderBundleEncoder({
  colorFormats: [presentationFormat],
});
recordRenderPass(renderBundleEncoder);
const renderBundle = renderBundleEncoder.finish();
```

[GPURenderPassEncoder.executeBundles()](/en-US/docs/Web/API/GPURenderPassEncoder/executeBundles) is then used to reuse the work across multiple render passes to improve performance. Study the example code listing for the full context.

js

```
// …

return function doDraw(timestamp) {
  if (startTime === undefined) {
    startTime = timestamp;
  }
  uniformTime[0] = (timestamp - startTime) / 1000;
  device.queue.writeBuffer(uniformBuffer, timeOffset, uniformTime.buffer);

  renderPassDescriptor.colorAttachments[0].view = context
    .getCurrentTexture()
    .createView();

  const commandEncoder = device.createCommandEncoder();
  const passEncoder = commandEncoder.beginRenderPass(renderPassDescriptor);

  if (settings.renderBundles) {
    passEncoder.executeBundles([renderBundle]);
  } else {
    recordRenderPass(passEncoder);
  }

  passEncoder.end();
  device.queue.submit([commandEncoder.finish()]);
};

// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpurenderbundle](https://gpuweb.github.io/gpuweb/#gpurenderbundle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPURenderBundleEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpurenderbundleencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderBundleEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpurenderbundleencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderBundleEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpurenderbundleencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
