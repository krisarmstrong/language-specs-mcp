# GPUQuerySet

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUQuerySet&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUQuerySet` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is used to record the results of queries on passes, such as occlusion or timestamp queries.

- 

Occlusion queries are available on render passes to query whether any fragment samples pass all the per-fragment tests for a set of drawing commands (including scissor, sample mask, alpha to coverage, stencil, and depth tests). To run an occlusion query, an appropriate `GPUQuerySet` must be provided as the value of the `occlusionQuerySet` descriptor property when invoking [GPUCommandEncoder.beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass) to run a render pass.

- 

Timestamp queries allow applications to write timestamps to a `GPUQuerySet`. To run a timestamp query, appropriate `GPUQuerySet`s must be provided inside the value of the `timestampWrites` descriptor property when invoking [GPUCommandEncoder.beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass) to run a render pass, or [GPUCommandEncoder.beginComputePass()](/en-US/docs/Web/API/GPUCommandEncoder/beginComputePass) to run a compute pass.

Note: The `timestamp-query`[feature](/en-US/docs/Web/API/GPUSupportedFeatures) needs to be enabled to use timestamp queries.

A `GPUQuerySet` object instance is created using the [GPUDevice.createQuerySet()](/en-US/docs/Web/API/GPUDevice/createQuerySet) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[count](/en-US/docs/Web/API/GPUQuerySet/count)Read only

A number specifying the number of queries managed by the `GPUQuerySet`.

[label](/en-US/docs/Web/API/GPUQuerySet/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

[type](/en-US/docs/Web/API/GPUQuerySet/type)Read only

An enumerated value specifying the type of queries managed by the `GPUQuerySet`.

## [Instance methods](#instance_methods)

[destroy()](/en-US/docs/Web/API/GPUQuerySet/destroy)

Destroys the `GPUQuerySet`.

## [Examples](#examples)

The following snippet creates a `GPUQuerySet` that holds 32 occlusion query results, and then returns the `type` and `count`:

js

```
const querySet = device.createQuerySet({
  type: "occlusion",
  count: 32,
});

console.log(querySet.count); // 32
console.log(querySet.type); // "occlusion"
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuqueryset](https://gpuweb.github.io/gpuweb/#gpuqueryset)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUQuerySet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuqueryset/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUQuerySet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuqueryset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUQuerySet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuqueryset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
