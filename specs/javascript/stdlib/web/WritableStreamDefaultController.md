# WritableStreamDefaultController

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStreamDefaultController&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WritableStreamDefaultController` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a controller allowing control of a [WritableStream](/en-US/docs/Web/API/WritableStream)'s state. When constructing a `WritableStream`, the underlying sink is given a corresponding `WritableStreamDefaultController` instance to manipulate.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

None. `WritableStreamDefaultController` instances are created automatically during `WritableStream` construction.

## [Instance properties](#instance_properties)

[WritableStreamDefaultController.signal](/en-US/docs/Web/API/WritableStreamDefaultController/signal)Read only

Returns the [AbortSignal](/en-US/docs/Web/API/AbortSignal) associated with the controller.

## [Instance methods](#instance_methods)

[WritableStreamDefaultController.error()](/en-US/docs/Web/API/WritableStreamDefaultController/error)

Causes any future interactions with the associated stream to error.

## [Examples](#examples)

js

```
const writableStream = new WritableStream({
  start(controller) {
    // do stuff with controller

    // error stream if necessary
    controller.error("My stream is broken");
  },
  write(chunk, controller) {
    // …
  },
  close(controller) {
    // …
  },
  abort(err) {
    // …
  },
});
```

## [Specifications](#specifications)

Specification
[Streams# ws-default-controller-class](https://streams.spec.whatwg.org/#ws-default-controller-class)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WritableStreamDefaultController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/writablestreamdefaultcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStreamDefaultController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwritablestreamdefaultcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStreamDefaultController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwritablestreamdefaultcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F759102220c07fb140b3e06971cd5981d8f0f134f%0A*+Document+last+modified%3A+2025-04-28T15%3A45%3A41.000Z%0A%0A%3C%2Fdetails%3E)
