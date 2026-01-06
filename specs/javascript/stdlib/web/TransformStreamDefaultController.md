# TransformStreamDefaultController

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨June 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransformStreamDefaultController&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TransformStreamDefaultController` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) provides methods to manipulate the associated [ReadableStream](/en-US/docs/Web/API/ReadableStream) and [WritableStream](/en-US/docs/Web/API/WritableStream).

When constructing a [TransformStream](/en-US/docs/Web/API/TransformStream), the `TransformStreamDefaultController` is created. It therefore has no constructor. The way to get an instance of `TransformStreamDefaultController` is via the callback methods of [TransformStream()](/en-US/docs/Web/API/TransformStream/TransformStream).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[TransformStreamDefaultController.desiredSize](/en-US/docs/Web/API/TransformStreamDefaultController/desiredSize)Read only

Returns the desired size to fill the readable side of the stream's internal queue.

## [Instance methods](#instance_methods)

[TransformStreamDefaultController.enqueue()](/en-US/docs/Web/API/TransformStreamDefaultController/enqueue)

Enqueues a chunk (single piece of data) in the readable side of the stream.

[TransformStreamDefaultController.error()](/en-US/docs/Web/API/TransformStreamDefaultController/error)

Errors both the readable and writable side of the transform stream.

[TransformStreamDefaultController.terminate()](/en-US/docs/Web/API/TransformStreamDefaultController/terminate)

Closes the readable side and errors the writable side of the stream.

## [Examples](#examples)

In the following example, a transform stream passes through all chunks it receives as [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) values, using the [error()](/en-US/docs/Web/API/TransformStreamDefaultController/error) and [enqueue()](/en-US/docs/Web/API/TransformStreamDefaultController/enqueue) methods.

js

```
const transformContent = {
  start() {}, // required.
  async transform(chunk, controller) {
    chunk = await chunk;
    switch (typeof chunk) {
      case "object":
        // just say the stream is done I guess
        if (chunk === null) {
          controller.terminate();
        } else if (ArrayBuffer.isView(chunk)) {
          controller.enqueue(
            new Uint8Array(chunk.buffer, chunk.byteOffset, chunk.byteLength),
          );
        } else if (
          Array.isArray(chunk) &&
          chunk.every((value) => typeof value === "number")
        ) {
          controller.enqueue(new Uint8Array(chunk));
        } else if (
          typeof chunk.valueOf === "function" &&
          chunk.valueOf() !== chunk
        ) {
          this.transform(chunk.valueOf(), controller); // hack
        } else if ("toJSON" in chunk) {
          this.transform(JSON.stringify(chunk), controller);
        }
        break;
      case "symbol":
        controller.error("Cannot send a symbol as a chunk part");
        break;
      case "undefined":
        controller.error("Cannot send undefined as a chunk part");
        break;
      default:
        controller.enqueue(this.textencoder.encode(String(chunk)));
        break;
    }
  },
  flush() {
    /* do any destructor work here */
  },
};

class AnyToU8Stream extends TransformStream {
  constructor() {
    super({ ...transformContent, textencoder: new TextEncoder() });
  }
}
```

## [Specifications](#specifications)

Specification
[Streams# ts-default-controller-class](https://streams.spec.whatwg.org/#ts-default-controller-class)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TransformStreamDefaultController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/transformstreamdefaultcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransformStreamDefaultController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftransformstreamdefaultcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransformStreamDefaultController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftransformstreamdefaultcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8b4431bfde42f1bc195239ea1f378d763f8163e%0A*+Document+last+modified%3A+2024-04-22T06%3A16%3A40.000Z%0A%0A%3C%2Fdetails%3E)
