# GPUTexture

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUTexture&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUTexture` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a container used to store 1D, 2D, or 3D arrays of data, such as images, to use in GPU rendering operations.

A `GPUTexture` object instance is created using the [GPUDevice.createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[depthOrArrayLayers](/en-US/docs/Web/API/GPUTexture/depthOrArrayLayers)Read only

A number representing the depth or layer count of the `GPUTexture` (pixels, or number of layers).

[dimension](/en-US/docs/Web/API/GPUTexture/dimension)Read only

An enumerated value representing the dimension of the set of texels for each `GPUTexture` subresource.

[format](/en-US/docs/Web/API/GPUTexture/format)Read only

An enumerated value representing the format of the `GPUTexture`. See the [Texture formats](https://gpuweb.github.io/gpuweb/#enumdef-gputextureformat) section of the specification for all the possible values. Also see [Tier 1 and Tier 2 texture formats](/en-US/docs/Web/API/GPUDevice/createTexture#tier_1_and_tier_2_texture_formats).

[height](/en-US/docs/Web/API/GPUTexture/height)Read only

A number representing the height of the `GPUTexture` in pixels.

[label](/en-US/docs/Web/API/GPUTexture/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

[mipLevelCount](/en-US/docs/Web/API/GPUTexture/mipLevelCount)Read only

A number representing the number of mip levels of the `GPUTexture`.

[sampleCount](/en-US/docs/Web/API/GPUTexture/sampleCount)Read only

A number representing the sample count of the `GPUTexture`.

[usage](/en-US/docs/Web/API/GPUTexture/usage)Read only

The [bitwise flags](/en-US/docs/Glossary/Bitwise_flags) representing the allowed usages of the `GPUTexture`.

[width](/en-US/docs/Web/API/GPUTexture/width)Read only

A number representing the width of the `GPUTexture` in pixels.

## [Instance methods](#instance_methods)

[createView()](/en-US/docs/Web/API/GPUTexture/createView)

Creates a [GPUTextureView](/en-US/docs/Web/API/GPUTextureView) representing a specific view of the `GPUTexture`.

[destroy()](/en-US/docs/Web/API/GPUTexture/destroy)

Destroys the `GPUTexture`.

## [Examples](#examples)

In the WebGPU samples [Textured Cube sample](https://webgpu.github.io/webgpu-samples/samples/texturedCube/), a texture to use on the faces of a cube is created by:

- Loading the image into an [HTMLImageElement](/en-US/docs/Web/API/HTMLImageElement) and creating an image bitmap using [createImageBitmap()](/en-US/docs/Web/API/Window/createImageBitmap).
- Creating a new `GPUTexture` using `createTexture()`.
- Copying the image bitmap into the texture using [GPUQueue.copyExternalImageToTexture()](/en-US/docs/Web/API/GPUQueue/copyExternalImageToTexture).

js

```
// …
let cubeTexture;
{
  const img = document.createElement("img");

  img.src = new URL(
    "../../../assets/img/Di-3d.png",
    import.meta.url,
  ).toString();

  await img.decode();

  const imageBitmap = await createImageBitmap(img);

  cubeTexture = device.createTexture({
    size: [imageBitmap.width, imageBitmap.height, 1],
    format: "rgba8unorm",
    usage:
      GPUTextureUsage.TEXTURE_BINDING |
      GPUTextureUsage.COPY_DST |
      GPUTextureUsage.RENDER_ATTACHMENT,
  });

  device.queue.copyExternalImageToTexture(
    { source: imageBitmap },
    { texture: cubeTexture },
    [imageBitmap.width, imageBitmap.height],
  );
}
// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gputexture](https://gpuweb.github.io/gpuweb/#gputexture)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUTexture/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gputexture/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUTexture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgputexture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUTexture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgputexture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F78c41c9b5211cc5bfba793c72a9adcac852e07f9%0A*+Document+last+modified%3A+2025-10-21T10%3A07%3A03.000Z%0A%0A%3C%2Fdetails%3E)
