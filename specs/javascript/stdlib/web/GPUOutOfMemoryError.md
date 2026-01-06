# GPUOutOfMemoryError

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUOutOfMemoryError&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUOutOfMemoryError` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) describes an out-of-memory (oom) error indicating that there was not enough free memory to complete the requested operation.

It represents one of the types of errors surfaced by [GPUDevice.popErrorScope](/en-US/docs/Web/API/GPUDevice/popErrorScope) and the [uncapturederror](/en-US/docs/Web/API/GPUDevice/uncapturederror_event) event.

Out-of-memory errors should be relatively rare in a well-behaved app but are less predictable than [GPUValidationError](/en-US/docs/Web/API/GPUValidationError)s. This is because they are dependent on the device your app is running on as well as other apps that are using GPU resources at the time.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[GPUOutOfMemoryError()](/en-US/docs/Web/API/GPUOutOfMemoryError/GPUOutOfMemoryError)

Creates a new `GPUOutOfMemoryError` object instance.

## [Instance properties](#instance_properties)

The `message` property is inherited from its parent, [GPUError](/en-US/docs/Web/API/GPUError):

[message](/en-US/docs/Web/API/GPUError/message)ExperimentalRead only

A string providing a human-readable message that explains why the error occurred.

## [Examples](#examples)

The following example uses an error scope to capture an out-of-memory error, logging it to the console.

js

```
device.pushErrorScope("out-of-memory");

let buffer = device.createBuffer({
  size: 100_000_000_000, // 100GB; far too big
  usage: GPUBufferUsage.COPY_SRC | GPUBufferUsage.MAP_WRITE,
});

device.popErrorScope().then((error) => {
  if (error) {
    // error is a GPUOutOfMemoryError object instance
    buffer = null;
    console.error(`Out of memory, buffer too large. Error: ${error.message}`);
  }
});
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuoutofmemoryerror](https://gpuweb.github.io/gpuweb/#gpuoutofmemoryerror)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)
- [WebGPU Error Handling best practices](https://toji.dev/webgpu-best-practices/error-handling)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUOutOfMemoryError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuoutofmemoryerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUOutOfMemoryError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuoutofmemoryerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUOutOfMemoryError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuoutofmemoryerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
