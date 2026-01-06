# WritableStream

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2022⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStream&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WritableStream` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) provides a standard abstraction for writing streaming data to a destination, known as a sink. This object comes with built-in backpressure and queuing.

`WritableStream` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[WritableStream()](/en-US/docs/Web/API/WritableStream/WritableStream)

Creates a new `WritableStream` object.

## [Instance properties](#instance_properties)

[WritableStream.locked](/en-US/docs/Web/API/WritableStream/locked)Read only

A boolean indicating whether the `WritableStream` is locked to a writer.

## [Instance methods](#instance_methods)

[WritableStream.abort()](/en-US/docs/Web/API/WritableStream/abort)

Aborts the stream, signaling that the producer can no longer successfully write to the stream and it is to be immediately moved to an error state, with any queued writes discarded.

[WritableStream.close()](/en-US/docs/Web/API/WritableStream/close)

Closes the stream.

[WritableStream.getWriter()](/en-US/docs/Web/API/WritableStream/getWriter)

Returns a new instance of [WritableStreamDefaultWriter](/en-US/docs/Web/API/WritableStreamDefaultWriter) and locks the stream to that instance. While the stream is locked, no other writer can be acquired until this one is released.

## [Examples](#examples)

The following example illustrates several features of this interface. It creates the `WritableStream` with a custom sink. It then calls the stream's `getWriter()` method, which returns an instance of [WritableStreamDefaultWriter](/en-US/docs/Web/API/WritableStreamDefaultWriter). Next, several strings are written to the stream. Finally, `close()` returns a promise that resolves when all the writes have successfully completed.

js

```
const writableStream = new WritableStream(
  // Implement the sink
  {
    write(chunk) {
      const textElement = document.getElementById("text-output");
      textElement.textContent += chunk;
    },
  },
);

const writer = writableStream.getWriter();

try {
  writer.write("Hello, ");
  writer.write("world!\n");
  writer.write("This has been a demo!\n");

  await writer.close(); // wait for all chunks to be written
  console.log("All chunks written");
} catch (error) {
  console.error("Stream error: ", error);
}
```

This example does not support the [backpressure](/en-US/docs/Web/API/Streams_API/Concepts#backpressure) feature of Streams.

## [Specifications](#specifications)

Specification
[Streams# ws-class](https://streams.spec.whatwg.org/#ws-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams—The Definitive Guide](https://web.dev/articles/streams)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WritableStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/writablestream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwritablestream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwritablestream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d37e07f04c40ecbfd424d6fce0766ef3d2f7db4%0A*+Document+last+modified%3A+2025-07-03T11%3A20%3A06.000Z%0A%0A%3C%2Fdetails%3E)
