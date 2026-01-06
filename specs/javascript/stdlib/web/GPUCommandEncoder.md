# GPUCommandEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCommandEncoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUCommandEncoder` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents an encoder that collects a sequence of GPU commands to be issued to the GPU.

A `GPUCommandEncoder` object instance is created via the [GPUDevice.createCommandEncoder()](/en-US/docs/Web/API/GPUDevice/createCommandEncoder) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPUCommandEncoder/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Instance methods](#instance_methods)

[beginComputePass()](/en-US/docs/Web/API/GPUCommandEncoder/beginComputePass)

Starts encoding a compute pass, returning a [GPUComputePassEncoder](/en-US/docs/Web/API/GPUComputePassEncoder) that can be used to control computation.

[beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass)

Starts encoding a render pass, returning a [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder) that can be used to control rendering.

[clearBuffer()](/en-US/docs/Web/API/GPUCommandEncoder/clearBuffer)

Encodes a command that fills a region of a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) with zeroes.

[copyBufferToBuffer()](/en-US/docs/Web/API/GPUCommandEncoder/copyBufferToBuffer)

Encodes a command that copies data from one [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) to another.

[copyBufferToTexture()](/en-US/docs/Web/API/GPUCommandEncoder/copyBufferToTexture)

Encodes a command that copies data from a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) to a [GPUTexture](/en-US/docs/Web/API/GPUTexture).

[copyTextureToBuffer()](/en-US/docs/Web/API/GPUCommandEncoder/copyTextureToBuffer)

Encodes a command that copies data from a [GPUTexture](/en-US/docs/Web/API/GPUTexture) to a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer).

[copyTextureToTexture()](/en-US/docs/Web/API/GPUCommandEncoder/copyTextureToTexture)

Encodes a command that copies data from one [GPUTexture](/en-US/docs/Web/API/GPUTexture) to another.

[finish()](/en-US/docs/Web/API/GPUCommandEncoder/finish)

Completes recording of the command sequence encoded on this `GPUCommandEncoder`, returning a corresponding [GPUCommandBuffer](/en-US/docs/Web/API/GPUCommandBuffer).

[insertDebugMarker()](/en-US/docs/Web/API/GPUCommandEncoder/insertDebugMarker)

Marks a specific point in a series of encoded commands with a label.

[popDebugGroup()](/en-US/docs/Web/API/GPUCommandEncoder/popDebugGroup)

Ends a debug group, which is begun with a [pushDebugGroup()](/en-US/docs/Web/API/GPUCommandEncoder/pushDebugGroup) call.

[pushDebugGroup()](/en-US/docs/Web/API/GPUCommandEncoder/pushDebugGroup)

Begins a debug group, which is marked with a specified label, and will contain all subsequent encoded commands up until a [popDebugGroup()](/en-US/docs/Web/API/GPUCommandEncoder/popDebugGroup) method is invoked.

[resolveQuerySet()](/en-US/docs/Web/API/GPUCommandEncoder/resolveQuerySet)

Encodes a command that resolves a [GPUQuerySet](/en-US/docs/Web/API/GPUQuerySet), copying the results into a specified [GPUBuffer](/en-US/docs/Web/API/GPUBuffer).

[writeTimestamp()](/en-US/docs/Web/API/GPUCommandEncoder/writeTimestamp)Non-standardDeprecated

Encodes a command that writes a timestamp into a [GPUQuerySet](/en-US/docs/Web/API/GPUQuerySet) once the previous commands recorded into the same queued [GPUCommandBuffer](/en-US/docs/Web/API/GPUCommandBuffer) have been executed by the GPU.

## [Examples](#examples)

In our [basic render demo](https://mdn.github.io/dom-examples/webgpu-render-demo/), several commands are recorded via a `GPUCommandEncoder`:

js

```
// …

// Create GPUCommandEncoder
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

// Draw a triangle

passEncoder.setPipeline(renderPipeline);
passEncoder.setVertexBuffer(0, vertexBuffer);
passEncoder.draw(3);

// End the render pass

passEncoder.end();

// …
```

The commands encoded by the `GPUCommandEncoder` are recorded into a [GPUCommandBuffer](/en-US/docs/Web/API/GPUCommandBuffer) using the [GPUCommandEncoder.finish()](/en-US/docs/Web/API/GPUCommandEncoder/finish) method. The command buffer is then passed into the queue via a [submit()](/en-US/docs/Web/API/GPUQueue/submit) call, ready to be processed by the GPU.

js

```
device.queue.submit([commandEncoder.finish()]);
```

Note: Study the [WebGPU samples](https://webgpu.github.io/webgpu-samples/) to find more command encoding examples.

## [Specifications](#specifications)

Specification
[WebGPU# gpucommandencoder](https://gpuweb.github.io/gpuweb/#gpucommandencoder)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUCommandEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpucommandencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCommandEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpucommandencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCommandEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpucommandencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ede6c458a7f2fd3b217e01062354748bda4992f%0A*+Document+last+modified%3A+2025-06-24T06%3A58%3A47.000Z%0A%0A%3C%2Fdetails%3E)
