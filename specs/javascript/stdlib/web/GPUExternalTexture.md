# GPUExternalTexture

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUExternalTexture&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUExternalTexture` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a wrapper object containing an [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) snapshot that can be used as a texture in GPU rendering operations.

A `GPUExternalTexture` object instance is created using [GPUDevice.importExternalTexture()](/en-US/docs/Web/API/GPUDevice/importExternalTexture).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPUExternalTexture/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

## [Examples](#examples)

In the WebGPU samples [Video Uploading sample](https://webgpu.github.io/webgpu-samples/samples/videoUploading/), a `GPUExternalTexture` object (created via a [GPUDevice.importExternalTexture()](/en-US/docs/Web/API/GPUDevice/importExternalTexture) call) is used as the value of a bind group entry `resource`, specified when creating a [GPUBindGroup](/en-US/docs/Web/API/GPUBindGroup) via a [GPUDevice.createBindGroup()](/en-US/docs/Web/API/GPUDevice/createBindGroup) call:

js

```
// …
const uniformBindGroup = device.createBindGroup({
  layout: pipeline.getBindGroupLayout(0),
  entries: [
    {
      binding: 1,
      resource: sampler,
    },
    {
      binding: 2,
      resource: device.importExternalTexture({
        source: video,
      }),
    },
  ],
});
// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuexternaltexture](https://gpuweb.github.io/gpuweb/#gpuexternaltexture)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUExternalTexture/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuexternaltexture/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUExternalTexture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuexternaltexture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUExternalTexture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuexternaltexture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
