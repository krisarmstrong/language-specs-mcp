# GPURenderPipeline

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderPipeline&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPURenderPipeline` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a pipeline that controls the vertex and fragment shader stages and can be used in a [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder) or [GPURenderBundleEncoder](/en-US/docs/Web/API/GPURenderBundleEncoder).

A `GPURenderPipeline` object instance can be created using the [GPUDevice.createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline) or [GPUDevice.createRenderPipelineAsync()](/en-US/docs/Web/API/GPUDevice/createRenderPipelineAsync) methods.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPURenderPipeline/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Instance methods](#instance_methods)

[getBindGroupLayout()](/en-US/docs/Web/API/GPURenderPipeline/getBindGroupLayout)

Returns the pipeline's [GPUBindGroupLayout](/en-US/docs/Web/API/GPUBindGroupLayout) object with the given index (i.e., included in the originating [GPUDevice.createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline) or [GPUDevice.createRenderPipelineAsync()](/en-US/docs/Web/API/GPUDevice/createRenderPipelineAsync) call's pipeline layout).

## [Examples](#examples)

Note: The [WebGPU samples](https://webgpu.github.io/webgpu-samples/) feature many more examples.

### [Basic example](#basic_example)

Our [basic render demo](https://mdn.github.io/dom-examples/webgpu-render-demo/) provides an example of the construction of a valid render pipeline descriptor object, which is then used to create a `GPURenderPipeline` via a `createRenderPipeline()` call.

js

```
// …

const vertexBuffers = [
  {
    attributes: [
      {
        shaderLocation: 0, // position
        offset: 0,
        format: "float32x4",
      },
      {
        shaderLocation: 1, // color
        offset: 16,
        format: "float32x4",
      },
    ],
    arrayStride: 32,
    stepMode: "vertex",
  },
];

const pipelineDescriptor = {
  vertex: {
    module: shaderModule,
    entryPoint: "vertex_main",
    buffers: vertexBuffers,
  },
  fragment: {
    module: shaderModule,
    entryPoint: "fragment_main",
    targets: [
      {
        format: navigator.gpu.getPreferredCanvasFormat(),
      },
    ],
  },
  primitive: {
    topology: "triangle-list",
  },
  layout: "auto",
};

const renderPipeline = device.createRenderPipeline(pipelineDescriptor);

// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpurenderpipeline](https://gpuweb.github.io/gpuweb/#gpurenderpipeline)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPURenderPipeline/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpurenderpipeline/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderPipeline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpurenderpipeline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPURenderPipeline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpurenderpipeline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
