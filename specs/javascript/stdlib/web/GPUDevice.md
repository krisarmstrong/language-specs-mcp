# GPUDevice

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUDevice&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUDevice` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a logical GPU device. This is the main interface through which the majority of WebGPU functionality is accessed.

A `GPUDevice` object is requested using the [GPUAdapter.requestDevice()](/en-US/docs/Web/API/GPUAdapter/requestDevice) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[adapterInfo](/en-US/docs/Web/API/GPUDevice/adapterInfo)Read only

A [GPUAdapterInfo](/en-US/docs/Web/API/GPUAdapterInfo) object containing identifying information about the device's originating adapter.

[features](/en-US/docs/Web/API/GPUDevice/features)Read only

A [GPUSupportedFeatures](/en-US/docs/Web/API/GPUSupportedFeatures) object that describes additional functionality supported by the device.

[label](/en-US/docs/Web/API/GPUDevice/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

[limits](/en-US/docs/Web/API/GPUDevice/limits)Read only

A [GPUSupportedLimits](/en-US/docs/Web/API/GPUSupportedLimits) object that describes the limits supported by the device.

[lost](/en-US/docs/Web/API/GPUDevice/lost)Read only

Contains a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that remains pending throughout the device's lifetime and resolves with a [GPUDeviceLostInfo](/en-US/docs/Web/API/GPUDeviceLostInfo) object when the device is lost.

[queue](/en-US/docs/Web/API/GPUDevice/queue)Read only

Returns the primary [GPUQueue](/en-US/docs/Web/API/GPUQueue) for the device.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[createBindGroup()](/en-US/docs/Web/API/GPUDevice/createBindGroup)

Creates a [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup) based on a [GPUBindGroupLayout](/en-US/docs/Web/API/GPUBindGroupLayout) that defines a set of resources to be bound together in a group and how those resources are used in shader stages.

[createBindGroupLayout()](/en-US/docs/Web/API/GPUDevice/createBindGroupLayout)

Creates a [GPUBindGroupLayout](/en-US/docs/Web/API/GPUBindGroupLayout) that defines the structure and purpose of related GPU resources such as buffers that will be used in a pipeline, and is used as a template when creating [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup)s.

[createBuffer()](/en-US/docs/Web/API/GPUDevice/createBuffer)

Creates a [GPUBuffer](/en-US/docs/Web/API/GPUBuffer) in which to store raw data to use in GPU operations.

[createCommandEncoder()](/en-US/docs/Web/API/GPUDevice/createCommandEncoder)

Creates a [GPUCommandEncoder](/en-US/docs/Web/API/GPUCommandEncoder), which is used to encode commands to be issued to the GPU.

[createComputePipeline()](/en-US/docs/Web/API/GPUDevice/createComputePipeline)

Creates a [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline) that can control the compute shader stage and be used in a [GPUComputePassEncoder](/en-US/docs/Web/API/GPUComputePassEncoder).

[createComputePipelineAsync()](/en-US/docs/Web/API/GPUDevice/createComputePipelineAsync)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline), which can control the compute shader stage and be used in a [GPUComputePassEncoder](/en-US/docs/Web/API/GPUComputePassEncoder), once the pipeline can be used without any stalling.

[createPipelineLayout()](/en-US/docs/Web/API/GPUDevice/createPipelineLayout)

Creates a [GPUPipelineLayout](/en-US/docs/Web/API/GPUPipelineLayout) that defines the [GPUBindGroupLayout](/en-US/docs/Web/API/GPUBindGroupLayout)s used by a pipeline. [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup)s used with the pipeline during command encoding must have compatible [GPUBindGroupLayout](/en-US/docs/Web/API/GPUBindGroupLayout)s.

[createQuerySet()](/en-US/docs/Web/API/GPUDevice/createQuerySet)

Creates a [GPUQuerySet](/en-US/docs/Web/API/GPUQuerySet) that can be used to record the results of queries on passes, such as occlusion or timestamp queries.

[createRenderBundleEncoder()](/en-US/docs/Web/API/GPUDevice/createRenderBundleEncoder)

Creates a [GPURenderBundleEncoder](/en-US/docs/Web/API/GPURenderBundleEncoder) that can be used to pre-record bundles of commands. These can be reused in [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder)s via the [executeBundles()](/en-US/docs/Web/API/GPURenderPassEncoder/executeBundles) method, as many times as required.

[createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline)

Creates a [GPURenderPipeline](/en-US/docs/Web/API/GPURenderPipeline) that can control the vertex and fragment shader stages and be used in a [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder) or [GPURenderBundleEncoder](/en-US/docs/Web/API/GPURenderBundleEncoder).

[createRenderPipelineAsync()](/en-US/docs/Web/API/GPUDevice/createRenderPipelineAsync)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [GPURenderPipeline](/en-US/docs/Web/API/GPURenderPipeline), which can control the vertex and fragment shader stages and be used in a [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder) or [GPURenderBundleEncoder](/en-US/docs/Web/API/GPURenderBundleEncoder), once the pipeline can be used without any stalling.

[createSampler()](/en-US/docs/Web/API/GPUDevice/createSampler)

Creates a [GPUSampler](/en-US/docs/Web/API/GPUSampler), which controls how shaders transform and filter texture resource data.

[createShaderModule()](/en-US/docs/Web/API/GPUDevice/createShaderModule)

Creates a [GPUShaderModule](/en-US/docs/Web/API/GPUShaderModule) from a string of WGSL source code.

[createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture)

Creates a [GPUTexture](/en-US/docs/Web/API/GPUTexture) in which to store texture data to use in GPU rendering operations.

[destroy()](/en-US/docs/Web/API/GPUDevice/destroy)

Destroys the device, preventing further operations on it.

[importExternalTexture()](/en-US/docs/Web/API/GPUDevice/importExternalTexture)

Takes an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) as an input and returns a [GPUExternalTexture](/en-US/docs/Web/API/GPUExternalTexture) wrapper object containing a snapshot of the video that can be used in GPU rendering operations.

[popErrorScope()](/en-US/docs/Web/API/GPUDevice/popErrorScope)

Pops an existing GPU error scope from the error scope stack and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an object ([GPUInternalError](/en-US/docs/Web/API/GPUInternalError), [GPUOutOfMemoryError](/en-US/docs/Web/API/GPUOutOfMemoryError), or [GPUValidationError](/en-US/docs/Web/API/GPUValidationError)) describing the first error captured in the scope, or `null` if no error occurred.

[pushErrorScope()](/en-US/docs/Web/API/GPUDevice/pushErrorScope)

Pushes a new GPU error scope onto the device's error scope stack, allowing you to capture errors of a particular type.

## [Events](#events)

[uncapturederror](/en-US/docs/Web/API/GPUDevice/uncapturederror_event)

Fired when an error is thrown that has not been observed by a GPU error scope, to provide a way to report unexpected errors. Known error cases should be handled using [pushErrorScope()](/en-US/docs/Web/API/GPUDevice/pushErrorScope) and [popErrorScope()](/en-US/docs/Web/API/GPUDevice/popErrorScope).

## [Examples](#examples)

js

```
async function init() {
  if (!navigator.gpu) {
    throw Error("WebGPU not supported.");
  }

  const adapter = await navigator.gpu.requestAdapter();
  if (!adapter) {
    throw Error("Couldn't request WebGPU adapter.");
  }

  const device = await adapter.requestDevice();

  const shaderModule = device.createShaderModule({
    code: shaders,
  });

  // …
}
```

See the individual member pages listed above and the following demo sites for a lot more examples of `GPUDevice` usage:

- [Basic compute demo](https://mdn.github.io/dom-examples/webgpu-compute-demo/)
- [Basic render demo](https://mdn.github.io/dom-examples/webgpu-render-demo/)
- [WebGPU samples](https://webgpu.github.io/webgpu-samples/)

## [Specifications](#specifications)

Specification
[WebGPU# gpudevice](https://gpuweb.github.io/gpuweb/#gpudevice)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUDevice/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpudevice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUDevice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpudevice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUDevice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpudevice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F66f1ba7918610f1145cde4a1d2d7ecb3baea5f65%0A*+Document+last+modified%3A+2025-07-28T03%3A22%3A33.000Z%0A%0A%3C%2Fdetails%3E)
