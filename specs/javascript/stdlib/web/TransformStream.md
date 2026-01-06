# TransformStream

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨June 2022⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransformStream&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TransformStream` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a concrete implementation of the [pipe chain](/en-US/docs/Web/API/Streams_API/Concepts#pipe_chains)transform stream concept.

It may be passed to the [ReadableStream.pipeThrough()](/en-US/docs/Web/API/ReadableStream/pipeThrough) method in order to transform a stream of data from one format into another. For example, it might be used to decode (or encode) video frames, decompress data, or convert the stream from XML to JSON.

A transformation algorithm may be provided as an optional argument to the object constructor. If not supplied, data is not modified when piped through the stream.

`TransformStream` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TransformStream()](/en-US/docs/Web/API/TransformStream/TransformStream)

Creates and returns a transform stream object, optionally specifying a transformation object and queuing strategies for the streams.

## [Instance properties](#instance_properties)

[TransformStream.readable](/en-US/docs/Web/API/TransformStream/readable)Read only

The `readable` end of a `TransformStream`.

[TransformStream.writable](/en-US/docs/Web/API/TransformStream/writable)Read only

The `writable` end of a `TransformStream`.

## [Instance methods](#instance_methods)

None

## [Examples](#examples)

### [Anything-to-uint8array stream](#anything-to-uint8array_stream)

In the following example, a transform stream passes through all chunks it receives as [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) values.

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

### [Chaining multiple ReadableStreams together](#chaining_multiple_readablestreams_together)

This is a useful one, where multiple streams can be conjoined. Examples include building a PWA with progressive loading and progressive streaming.

js

```
let responses = [
  /* conjoined response tree */
];
let { readable, writable } = new TransformStream();

responses.reduce(
  (a, res, i, arr) =>
    a.then(() => res.pipeTo(writable, { preventClose: i + 1 !== arr.length })),
  Promise.resolve(),
);
```

Note that this is not resilient to other influences.

## [Specifications](#specifications)

Specification
[Streams# ts-class](https://streams.spec.whatwg.org/#ts-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams—The Definitive Guide](https://web.dev/articles/streams)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TransformStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/transformstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransformStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftransformstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransformStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftransformstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d37e07f04c40ecbfd424d6fce0766ef3d2f7db4%0A*+Document+last+modified%3A+2025-07-03T11%3A20%3A06.000Z%0A%0A%3C%2Fdetails%3E)
