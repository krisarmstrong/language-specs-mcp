# GPUBuffer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUBuffer&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUBuffer` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) represents a block of memory that can be used to store raw data to use in GPU operations.

A `GPUBuffer` object instance is created using the [GPUDevice.createBuffer()](/en-US/docs/Web/API/GPUDevice/createBuffer) method.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[label](/en-US/docs/Web/API/GPUBuffer/label)

A string providing a label that can be used to identify the object, for example in [GPUError](/en-US/docs/Web/API/GPUError) messages or console warnings.

[mapState](/en-US/docs/Web/API/GPUBuffer/mapState)Read only

An enumerated value representing the mapped state of the `GPUBuffer`.

[size](/en-US/docs/Web/API/GPUBuffer/size)Read only

A number representing the length of the `GPUBuffer`'s memory allocation, in bytes.

[usage](/en-US/docs/Web/API/GPUBuffer/usage)Read only

The [bitwise flags](/en-US/docs/Glossary/Bitwise_flags) representing the allowed usages of the `GPUBuffer`.

## [Instance methods](#instance_methods)

[destroy()](/en-US/docs/Web/API/GPUBuffer/destroy)

Destroys the `GPUBuffer`.

[getMappedRange()](/en-US/docs/Web/API/GPUBuffer/getMappedRange)

Returns an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing the mapped contents of the `GPUBuffer` in the specified range.

[mapAsync()](/en-US/docs/Web/API/GPUBuffer/mapAsync)

Maps the specified range of the `GPUBuffer`. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the `GPUBuffer`'s content is ready to be accessed with [GPUBuffer.getMappedRange()](/en-US/docs/Web/API/GPUBuffer/getMappedRange).

[unmap()](/en-US/docs/Web/API/GPUBuffer/unmap)

Unmaps the mapped range of the `GPUBuffer`, making its contents available for use by the GPU again.

## [Examples](#examples)

In our [basic compute demo](https://mdn.github.io/dom-examples/webgpu-compute-demo/), we create an output buffer to read GPU calculations to, and a staging buffer to be mapped for JavaScript access.

js

```
const output = device.createBuffer({
  size: BUFFER_SIZE,
  usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_SRC,
});

const stagingBuffer = device.createBuffer({
  size: BUFFER_SIZE,
  usage: GPUBufferUsage.MAP_READ | GPUBufferUsage.COPY_DST,
});
```

Later on, once the `stagingBuffer` contains the results of the GPU computation, a combination of `GPUBuffer` methods are used to read the data back to JavaScript so that it can then be logged to the console:

- [GPUBuffer.mapAsync()](/en-US/docs/Web/API/GPUBuffer/mapAsync) is used to map the `GPUBuffer` for reading.
- [GPUBuffer.getMappedRange()](/en-US/docs/Web/API/GPUBuffer/getMappedRange) is used to return an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing the `GPUBuffer`'s contents.
- [GPUBuffer.unmap()](/en-US/docs/Web/API/GPUBuffer/unmap) is used to unmap the `GPUBuffer` again, once we have read the content into JavaScript as needed.

js

```
// map staging buffer to read results back to JS
await stagingBuffer.mapAsync(
  GPUMapMode.READ,
  0, // Offset
  BUFFER_SIZE, // Length
);

const copyArrayBuffer = stagingBuffer.getMappedRange(0, BUFFER_SIZE);
const data = copyArrayBuffer.slice(0);
stagingBuffer.unmap();
console.log(new Float32Array(data));
```

## [Specifications](#specifications)

Specification
[WebGPU# gpubuffer](https://gpuweb.github.io/gpuweb/#gpubuffer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUBuffer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpubuffer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUBuffer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpubuffer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUBuffer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpubuffer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
