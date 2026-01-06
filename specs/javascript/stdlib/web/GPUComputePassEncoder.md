# GPUComputePassEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUComputePassEncoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUComputePassEncoder` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) encodes commands related to controlling the compute shader stage, as issued by a [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline). It forms part of the overall encoding activity of a [GPUCommandEncoder](/en-US/docs/Web/API/GPUCommandEncoder).

A compute pipeline contains a single compute stage in which a compute shader takes general data, processes it in parallel across a specified number of workgroups, then returns the result in one or more buffers.

A `GPUComputePassEncoder` object instance is created via the [GPUCommandEncoder.beginComputePass()](/en-US/docs/Web/API/GPUCommandEncoder/beginComputePass) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPUComputePassEncoder/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Instance methods](#instance_methods)

[dispatchWorkgroups()](/en-US/docs/Web/API/GPUComputePassEncoder/dispatchWorkgroups)

Dispatches a specific grid of workgroups to perform the work being done by the current [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline).

[dispatchWorkgroupsIndirect()](/en-US/docs/Web/API/GPUComputePassEncoder/dispatchWorkgroupsIndirect)

Dispatches a grid of workgroups, defined by the parameters of a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer), to perform the work being done by the current [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline).

[end()](/en-US/docs/Web/API/GPUComputePassEncoder/end)

Completes recording of the current compute pass command sequence.

[insertDebugMarker()](/en-US/docs/Web/API/GPUComputePassEncoder/insertDebugMarker)

Marks a specific point in a series of encoded commands with a label.

[popDebugGroup()](/en-US/docs/Web/API/GPUComputePassEncoder/popDebugGroup)

Ends a debug group, which is begun with a [pushDebugGroup()](/en-US/docs/Web/API/GPUComputePassEncoder/pushDebugGroup) call.

[pushDebugGroup()](/en-US/docs/Web/API/GPUComputePassEncoder/pushDebugGroup)

Begins a debug group, which is marked with a specified label, and will contain all subsequent encoded commands up until a [popDebugGroup()](/en-US/docs/Web/API/GPUComputePassEncoder/popDebugGroup) method is invoked.

[setBindGroup()](/en-US/docs/Web/API/GPUComputePassEncoder/setBindGroup)

Sets the [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup) to use for subsequent compute commands, for a given index.

[setPipeline()](/en-US/docs/Web/API/GPUComputePassEncoder/setPipeline)

Sets the [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline) to use for this compute pass.

## [Examples](#examples)

In our [basic compute demo](https://mdn.github.io/dom-examples/webgpu-compute-demo/), several commands are recorded via a [GPUCommandEncoder](/en-US/docs/Web/API/GPUCommandEncoder). Most of these commands originate from the `GPUComputePassEncoder` created via [GPUCommandEncoder.beginComputePass()](/en-US/docs/Web/API/GPUCommandEncoder/beginComputePass).

js

```
// …

// Create GPUCommandEncoder to encode commands to issue to the GPU
const commandEncoder = device.createCommandEncoder();

// Create GPUComputePassEncoder to initiate compute pass
const passEncoder = commandEncoder.beginComputePass();

// Issue commands
passEncoder.setPipeline(computePipeline);
passEncoder.setBindGroup(0, bindGroup);
passEncoder.dispatchWorkgroups(Math.ceil(BUFFER_SIZE / 64));

// End the compute pass
passEncoder.end();

// Copy output buffer to staging buffer
commandEncoder.copyBufferToBuffer(
  output,
  0, // Source offset
  stagingBuffer,
  0, // Destination offset
  BUFFER_SIZE,
);

// End frame by passing array of command buffers to command queue for execution
device.queue.submit([commandEncoder.finish()]);

// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpucomputepassencoder](https://gpuweb.github.io/gpuweb/#gpucomputepassencoder)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUComputePassEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpucomputepassencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUComputePassEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpucomputepassencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUComputePassEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpucomputepassencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
