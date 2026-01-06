# GPUError

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUError&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUError` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is the base interface for errors surfaced by [GPUDevice.popErrorScope](/en-US/docs/Web/API/GPUDevice/popErrorScope) and the [uncapturederror](/en-US/docs/Web/API/GPUDevice/uncapturederror_event) event.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[message](/en-US/docs/Web/API/GPUError/message)Read only

A string providing a human-readable message that explains why the error occurred.

## [Examples](#examples)

For usage examples of error objects based on `GPUError`, see:

- [GPUDevice.popErrorScope](/en-US/docs/Web/API/GPUDevice/popErrorScope#examples)
- [The GPUDevice uncapturederror event](/en-US/docs/Web/API/GPUDevice/uncapturederror_event#examples)
- [GPUInternalError](/en-US/docs/Web/API/GPUInternalError), [GPUOutOfMemoryError](/en-US/docs/Web/API/GPUOutOfMemoryError), and [GPUValidationError](/en-US/docs/Web/API/GPUValidationError)

## [Specifications](#specifications)

Specification
[WebGPU# gpuerror](https://gpuweb.github.io/gpuweb/#gpuerror)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)
- [WebGPU Error Handling best practices](https://toji.dev/webgpu-best-practices/error-handling)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUError/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuerror/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUError&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuerror%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUError%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuerror%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbec7ef59277e752985de0ee963c86f6e8e4b3400%0A*+Document+last+modified%3A+2025-06-25T18%3A43%3A22.000Z%0A%0A%3C%2Fdetails%3E)
