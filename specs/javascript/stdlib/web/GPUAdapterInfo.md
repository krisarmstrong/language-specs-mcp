# GPUAdapterInfo

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUAdapterInfo&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUAdapterInfo` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) contains identifying information about a [GPUAdapter](/en-US/docs/Web/API/GPUAdapter).

An adapter's `GPUAdapterInfo` can be retrieved using the [GPUAdapter.info](/en-US/docs/Web/API/GPUAdapter/info) property of the adapter itself, or the [GPUDevice.adapterInfo](/en-US/docs/Web/API/GPUDevice/adapterInfo) property of a device that originated from the adapter.

This object allows developers to access specific details about the user's GPU so that they can preemptively apply workarounds for GPU-specific bugs, or provide different codepaths to better suit different GPU architectures. Providing such information does present a security risk — it could be used for fingerprinting — therefore the information shared is kept at a minimum, and different browser vendors are likely to share different information types and granularities.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[architecture](/en-US/docs/Web/API/GPUAdapterInfo/architecture)Read only

The name of the family or class of GPUs the adapter belongs to. Returns an empty string if it is not available.

[description](/en-US/docs/Web/API/GPUAdapterInfo/description)Read only

A human-readable string describing the adapter. Returns an empty string if it is not available.

[device](/en-US/docs/Web/API/GPUAdapterInfo/device)Read only

A vendor-specific identifier for the adapter. Returns an empty string if it is not available.

[isFallbackAdapter](/en-US/docs/Web/API/GPUAdapterInfo/isFallbackAdapter)Read only

A boolean value. Returns `true` if the adapter is a [fallback adapter](/en-US/docs/Web/API/GPU/requestAdapter#fallback_adapters), and `false` if not.

[subgroupMaxSize](/en-US/docs/Web/API/GPUAdapterInfo/subgroupMaxSize)Read only

The maximum supported [subgroup size](https://gpuweb.github.io/gpuweb/wgsl/#subgroup-size) for the [GPUAdapter](/en-US/docs/Web/API/GPUAdapter).

[subgroupMinSize](/en-US/docs/Web/API/GPUAdapterInfo/subgroupMinSize)Read only

The minimum supported [subgroup size](https://gpuweb.github.io/gpuweb/wgsl/#subgroup-size) for the [GPUAdapter](/en-US/docs/Web/API/GPUAdapter).

[vendor](/en-US/docs/Web/API/GPUAdapterInfo/vendor)Read only

The name of the adapter vendor. Returns an empty string if it is not available.

## [Examples](#examples)

### [Access GPUAdapterInfo via GPUAdapter.info](#access_gpuadapterinfo_via_gpuadapter.info)

js

```
const adapter = await navigator.gpu.requestAdapter();
if (!adapter) {
  throw Error("Couldn't request WebGPU adapter.");
}

const adapterInfo = adapter.info;
console.log(adapterInfo.vendor);
console.log(adapterInfo.architecture);
```

### [Access GPUAdapterInfo via GPUDevice.adapterInfo](#access_gpuadapterinfo_via_gpudevice.adapterinfo)

js

```
const adapter = await navigator.gpu.requestAdapter();
if (!adapter) {
  throw Error("Couldn't request WebGPU adapter.");
}

const myDevice = await adapter.requestDevice();

function optimizeForGpuDevice(device) {
  if (device.adapterInfo.vendor === "amd") {
    // Use AMD-specific optimizations
  } else if (device.adapterInfo.architecture.includes("turing")) {
    // Optimize for NVIDIA Turing architecture
  }
}

optimizeForGpuDevice(myDevice);
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuadapterinfo](https://gpuweb.github.io/gpuweb/#gpuadapterinfo)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [GPUAdapter.info](/en-US/docs/Web/API/GPUAdapter/info)
- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 20, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUAdapterInfo/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuadapterinfo/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUAdapterInfo&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuadapterinfo%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUAdapterInfo%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuadapterinfo%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc03dee2dd8e7e28ba041b899de4db10f002d6645%0A*+Document+last+modified%3A+2025-10-20T15%3A12%3A22.000Z%0A%0A%3C%2Fdetails%3E)
