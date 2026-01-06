# GPUUncapturedErrorEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUUncapturedErrorEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUUncapturedErrorEvent` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is the event object type for the [GPUDevice](/en-US/docs/Web/API/GPUDevice)[uncapturederror](/en-US/docs/Web/API/GPUDevice/uncapturederror_event) event, used for telemetry and to report unexpected errors.

Known error cases should be handled using [pushErrorScope()](/en-US/docs/Web/API/GPUDevice/pushErrorScope) and [popErrorScope()](/en-US/docs/Web/API/GPUDevice/popErrorScope).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[GPUUncapturedErrorEvent()](/en-US/docs/Web/API/GPUUncapturedErrorEvent/GPUUncapturedErrorEvent)

Creates a new `GPUUncapturedErrorEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[error](/en-US/docs/Web/API/GPUUncapturedErrorEvent/error)Read only

A [GPUError](/en-US/docs/Web/API/GPUError) object instance providing access to the details of the error.

## [Examples](#examples)

You could use something like the following as a global mechanism to pick up any errors that aren't handled by error scopes and capture them.

js

```
// …

device.addEventListener("uncapturederror", (event) => {
  // Re-surface the error
  console.error("A WebGPU error was not captured:", event.error.message);
  reportErrorToServer({
    type: event.error.constructor.name,
    message: event.error.message,
  });
});

// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuuncapturederrorevent](https://gpuweb.github.io/gpuweb/#gpuuncapturederrorevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)
- [WebGPU Error Handling best practices](https://toji.dev/webgpu-best-practices/error-handling)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 18, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUUncapturedErrorEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpuuncapturederrorevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUUncapturedErrorEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpuuncapturederrorevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUUncapturedErrorEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpuuncapturederrorevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f226b6f08c5cff7f96b7cc49a164fdc43d11a0c%0A*+Document+last+modified%3A+2025-06-18T11%3A40%3A13.000Z%0A%0A%3C%2Fdetails%3E)
