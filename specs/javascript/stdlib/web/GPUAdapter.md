# GPUAdapter

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUAdapter&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUAdapter` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a GPU adapter. From this you can request a [GPUDevice](/en-US/docs/Web/API/GPUDevice), adapter info, features, and limits.

A `GPUAdapter` object is requested using the [GPU.requestAdapter()](/en-US/docs/Web/API/GPU/requestAdapter) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[features](/en-US/docs/Web/API/GPUAdapter/features)Read only

A [GPUSupportedFeatures](/en-US/docs/Web/API/GPUSupportedFeatures) object that describes additional functionality supported by the adapter.

[info](/en-US/docs/Web/API/GPUAdapter/info)Read only

A [GPUAdapterInfo](/en-US/docs/Web/API/GPUAdapterInfo) object containing identifying information about the adapter.

[limits](/en-US/docs/Web/API/GPUAdapter/limits)Read only

A [GPUSupportedLimits](/en-US/docs/Web/API/GPUSupportedLimits) object that describes the limits supported by the adapter.

### [Deprecated properties](#deprecated_properties)

[isFallbackAdapter](/en-US/docs/Web/API/GPUAdapter/isFallbackAdapter)Read onlyDeprecatedNon-standard

A boolean value. Returns `true` if the adapter is a [fallback adapter](/en-US/docs/Web/API/GPU/requestAdapter#fallback_adapters), and `false` if not. This property has been removed from the web platform. Use [GPUAdapterInfo.isFallbackAdapter](/en-US/docs/Web/API/GPUAdapterInfo/isFallbackAdapter) instead.

## [Instance methods](#instance_methods)

[requestAdapterInfo()](/en-US/docs/Web/API/GPUAdapter/requestAdapterInfo)DeprecatedNon-standard

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [GPUAdapterInfo](/en-US/docs/Web/API/GPUAdapterInfo) object containing identifying information about the adapter.

[requestDevice()](/en-US/docs/Web/API/GPUAdapter/requestDevice)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [GPUDevice](/en-US/docs/Web/API/GPUDevice) object, which is the primary interface for communicating with the GPU.

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

  // …
}
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuadapter](https://gpuweb.github.io/gpuweb/#gpuadapter)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUAdapter/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuadapter/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUAdapter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuadapter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUAdapter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuadapter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc03dee2dd8e7e28ba041b899de4db10f002d6645%0A*+Document+last+modified%3A+2025-10-20T15%3A12%3A22.000Z%0A%0A%3C%2Fdetails%3E)
