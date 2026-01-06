# GPU

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPU&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPU` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is the starting point for using WebGPU. It can be used to return a [GPUAdapter](/en-US/docs/Web/API/GPUAdapter) from which you can request devices, configure features and limits, and more.

The `GPU` object for the current context is accessed via the [Navigator.gpu](/en-US/docs/Web/API/Navigator/gpu) or [WorkerNavigator.gpu](/en-US/docs/Web/API/WorkerNavigator/gpu) properties.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[wgslLanguageFeatures](/en-US/docs/Web/API/GPU/wgslLanguageFeatures)Read only

A [WGSLLanguageFeatures](/en-US/docs/Web/API/WGSLLanguageFeatures) object that reports the [WGSL language extensions](https://gpuweb.github.io/gpuweb/wgsl/#language-extension) supported by the WebGPU implementation.

## [Instance methods](#instance_methods)

[requestAdapter()](/en-US/docs/Web/API/GPU/requestAdapter)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [GPUAdapter](/en-US/docs/Web/API/GPUAdapter) object instance. From this you can request a [GPUDevice](/en-US/docs/Web/API/GPUDevice), which is the primary interface for using WebGPU functionality.

[getPreferredCanvasFormat()](/en-US/docs/Web/API/GPU/getPreferredCanvasFormat)

Returns the optimal canvas texture format for displaying 8-bit depth, standard dynamic range content on the current system.

## [Examples](#examples)

### [Requesting an adapter and a device](#requesting_an_adapter_and_a_device)

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

### [Configuring a GPUCanvasContext with the optimal texture format](#configuring_a_gpucanvascontext_with_the_optimal_texture_format)

js

```
const canvas = document.querySelector("#gpuCanvas");
const context = canvas.getContext("webgpu");

context.configure({
  device,
  format: navigator.gpu.getPreferredCanvasFormat(),
  alphaMode: "premultiplied",
});
```

## [Specifications](#specifications)

Specification
[WebGPU# gpu-interface](https://gpuweb.github.io/gpuweb/#gpu-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPU/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpu/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPU&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpu%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPU%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpu%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
