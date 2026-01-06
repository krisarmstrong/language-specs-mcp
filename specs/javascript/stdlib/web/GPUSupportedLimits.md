# GPUSupportedLimits

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUSupportedLimits&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUSupportedLimits` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) describes the limits supported by a [GPUAdapter](/en-US/docs/Web/API/GPUAdapter).

The `GPUSupportedLimits` object for the current adapter is accessed via the [GPUAdapter.limits](/en-US/docs/Web/API/GPUAdapter/limits) property.

You should note that, rather than reporting the exact limits of each GPU, browsers will likely report different tier values of different limits to reduce the unique information available to drive-by fingerprinting. For example, the tiers of a certain limit might be 2048, 8192, and 32768. If your GPU's actual limit is 16384, the browser will still report 8192.

Given that different browsers will handle this differently and the tier values may change over time, it is hard to provide an accurate account of what limit values to expect — thorough testing is advised.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The following limits are represented by properties in a `GPUSupportedLimits` object. See the [Limits](https://gpuweb.github.io/gpuweb/#limits) section of the specification for detailed descriptions of what the limits relate to.

Limit nameDefault value`maxTextureDimension1D`8192`maxTextureDimension2D`8192`maxTextureDimension3D`2048`maxTextureArrayLayers`256`maxBindGroups`4`maxBindingsPerBindGroup`640`maxDynamicUniformBuffersPerPipelineLayout`8`maxDynamicStorageBuffersPerPipelineLayout`4`maxSampledTexturesPerShaderStage`16`maxSamplersPerShaderStage`16`maxStorageBuffersPerShaderStage`8`maxStorageTexturesPerShaderStage`4`maxUniformBuffersPerShaderStage`12`maxUniformBufferBindingSize`65536 bytes`maxStorageBufferBindingSize`134217728 bytes (128 MB)`minUniformBufferOffsetAlignment`256 bytes`minStorageBufferOffsetAlignment`256 bytes`maxVertexBuffers`8`maxBufferSize`268435456 bytes (256 MB)`maxVertexAttributes`16`maxVertexBufferArrayStride`2048 bytes`maxInterStageShaderComponents`DeprecatedNon-standard (use `maxInterStageShaderVariables` instead, see [deprecation notice](https://developer.chrome.com/blog/new-in-webgpu-133#deprecate_maxinterstageshadercomponents_limit) for more info)60`maxInterStageShaderVariables`16`maxColorAttachments`8`maxColorAttachmentBytesPerSample`32`maxComputeWorkgroupStorageSize`16384 bytes`maxComputeInvocationsPerWorkgroup`256`maxComputeWorkgroupSizeX`256`maxComputeWorkgroupSizeY`256`maxComputeWorkgroupSizeZ`64`maxComputeWorkgroupsPerDimension`65535

## [Examples](#examples)

In the following code we query the `GPUAdapter.limits` value of `maxBindGroups` to see if it is equal to or greater than 6. Our theoretical example app ideally needs 6 bind groups, so if the returned value is >= 6, we add a maximum limit of 6 to the `requiredLimits` object. We then request a device with that limit requirement using [GPUAdapter.requestDevice()](/en-US/docs/Web/API/GPUAdapter/requestDevice):

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

  const requiredLimits = {};

  // App ideally needs 6 bind groups, so we'll try to request what the app needs
  if (adapter.limits.maxBindGroups >= 6) {
    requiredLimits.maxBindGroups = 6;
  }

  const device = await adapter.requestDevice({
    requiredLimits,
  });

  // …
}
```

## [Specifications](#specifications)

Specification
[WebGPU# gpusupportedlimits](https://gpuweb.github.io/gpuweb/#gpusupportedlimits)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUSupportedLimits/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpusupportedlimits/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUSupportedLimits&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpusupportedlimits%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUSupportedLimits%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpusupportedlimits%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
