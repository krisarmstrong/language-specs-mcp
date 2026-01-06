# GPUPipelineError

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUPipelineError&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUPipelineError` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) describes a pipeline failure. This is the value received when a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) returned by a [GPUDevice.createComputePipelineAsync()](/en-US/docs/Web/API/GPUDevice/createComputePipelineAsync) or [GPUDevice.createRenderPipelineAsync()](/en-US/docs/Web/API/GPUDevice/createRenderPipelineAsync) call rejects.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[GPUPipelineError()](/en-US/docs/Web/API/GPUPipelineError/GPUPipelineError)

Creates a new `GPUPipelineError` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [DOMException](/en-US/docs/Web/API/DOMException).

[reason](/en-US/docs/Web/API/GPUPipelineError/reason)Read only

An enumerated value that defines the reason the pipeline creation failed in a machine-readable way.

## [Examples](#examples)

In the following snippet we are attempting to create a [GPUComputePipeline](/en-US/docs/Web/API/GPUComputePipeline) using [GPUDevice.createComputePipelineAsync()](/en-US/docs/Web/API/GPUDevice/createComputePipelineAsync). However, we have misspelt our compute pipeline `entryPoint` as `"maijn"` (it should be `"main"`), therefore pipeline creation fails, and our `catch` block prints the resulting reason and error message to the console.

js

```
// …

let computePipeline;

try {
  computePipeline = await device.createComputePipelineAsync({
    layout: device.createPipelineLayout({
      bindGroupLayouts: [bindGroupLayout],
    }),
    compute: {
      module: shaderModule,
      entryPoint: "maijn",
    },
  });
} catch (error) {
  // error is a GPUPipelineError object instance
  console.error(error.reason);
  console.error(`Pipeline creation failed: ${error.message}`);
}

// …
```

In this case, the given `reason` is `"Validation"`, and the `message` is `"Entry point "maijn" doesn't exist in the shader module [ShaderModule]."`

## [Specifications](#specifications)

Specification
[WebGPU# gpupipelineerror](https://gpuweb.github.io/gpuweb/#gpupipelineerror)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)
- [WebGPU Error Handling best practices](https://toji.dev/webgpu-best-practices/error-handling)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUPipelineError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpupipelineerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUPipelineError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpupipelineerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUPipelineError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpupipelineerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
