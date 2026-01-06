# GPUCommandBuffer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCommandBuffer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUCommandBuffer` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a pre-recorded list of GPU commands that can be submitted to a [GPUQueue](/en-US/docs/Web/API/GPUQueue) for execution.

A `GPUCommandBuffer` is created via the [GPUCommandEncoder.finish()](/en-US/docs/Web/API/GPUCommandEncoder/finish) method; the GPU commands recorded within are submitted for execution by passing the `GPUCommandBuffer` into the parameter of a [GPUQueue.submit()](/en-US/docs/Web/API/GPUQueue/submit) call.

Note: Once a `GPUCommandBuffer` object has been submitted, it cannot be used again.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPUCommandBuffer/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Examples](#examples)

js

```
// …

const commandBuffer = commandEncoder.finish();
device.queue.submit([commandBuffer]);
```

Note: Study the [WebGPU samples](https://webgpu.github.io/webgpu-samples/) to find complete examples.

## [Specifications](#specifications)

Specification
[WebGPU# gpucommandbuffer](https://gpuweb.github.io/gpuweb/#gpucommandbuffer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUCommandBuffer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpucommandbuffer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCommandBuffer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpucommandbuffer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCommandBuffer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpucommandbuffer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
