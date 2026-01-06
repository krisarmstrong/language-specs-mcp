# GPUCanvasContext

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCanvasContext&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUCanvasContext` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents the WebGPU rendering context of a [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element, returned via an [HTMLCanvasElement.getContext()](/en-US/docs/Web/API/HTMLCanvasElement/getContext) call with a `contextType` of `"webgpu"`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[canvas](/en-US/docs/Web/API/GPUCanvasContext/canvas)Read only

Returns a reference to the canvas that the context was created from.

## [Instance methods](#instance_methods)

[configure()](/en-US/docs/Web/API/GPUCanvasContext/configure)

Configures the context to use for rendering with a given [GPUDevice](/en-US/docs/Web/API/GPUDevice) and clears the canvas to transparent black.

[getConfiguration()](/en-US/docs/Web/API/GPUCanvasContext/getConfiguration)

Returns the current configuration set for the context.

[getCurrentTexture()](/en-US/docs/Web/API/GPUCanvasContext/getCurrentTexture)

Returns the next [GPUTexture](/en-US/docs/Web/API/GPUTexture) to be composited to the document by the canvas context.

[unconfigure()](/en-US/docs/Web/API/GPUCanvasContext/unconfigure)

Removes any previously-set context configuration, and destroys any textures produced while the canvas context was configured.

## [Examples](#examples)

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
[WebGPU# gpucanvascontext](https://gpuweb.github.io/gpuweb/#gpucanvascontext)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUCanvasContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpucanvascontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCanvasContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpucanvascontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUCanvasContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpucanvascontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
