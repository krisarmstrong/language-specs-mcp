# ReadableStreamBYOBReader

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamBYOBReader&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReadableStreamBYOBReader` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) defines a reader for a [ReadableStream](/en-US/docs/Web/API/ReadableStream) that supports zero-copy reading from an underlying byte source. It is used for efficient copying from underlying sources where the data is delivered as an "anonymous" sequence of bytes, such as files.

An instance of this reader type should usually be obtained by calling [ReadableStream.getReader()](/en-US/docs/Web/API/ReadableStream/getReader) on the stream, specifying `mode: "byob"` in the options parameter. The readable stream must have an underlying byte source. In other words, it must have been [constructed](/en-US/docs/Web/API/ReadableStream/ReadableStream) specifying an underlying source with [type: "bytes"](/en-US/docs/Web/API/ReadableStream/ReadableStream#type)).

Using this kind of reader, a [read()](/en-US/docs/Web/API/ReadableStreamBYOBReader/read) request when the readable stream's internal queues are empty will result in a zero copy transfer from the underlying source (bypassing the stream's internal queues). If the internal queues are not empty, a `read()` will satisfy the request from the buffered data.

Note that the methods and properties are similar to those for the default reader ([ReadableStreamDefaultReader](/en-US/docs/Web/API/ReadableStreamDefaultReader)). The `read()` method differs in that it provides a view into which data should be written.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ReadableStreamBYOBReader()](/en-US/docs/Web/API/ReadableStreamBYOBReader/ReadableStreamBYOBReader)

Creates and returns a `ReadableStreamBYOBReader` object instance.

## [Instance properties](#instance_properties)

[ReadableStreamBYOBReader.closed](/en-US/docs/Web/API/ReadableStreamBYOBReader/closed)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills when the stream closes, or rejects if the stream throws an error or the reader's lock is released. This property enables you to write code that responds to an end to the streaming process.

## [Instance methods](#instance_methods)

[ReadableStreamBYOBReader.cancel()](/en-US/docs/Web/API/ReadableStreamBYOBReader/cancel)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the stream is canceled. Calling this method signals a loss of interest in the stream by a consumer. The supplied `reason` argument will be given to the underlying source, which may or may not use it.

[ReadableStreamBYOBReader.read()](/en-US/docs/Web/API/ReadableStreamBYOBReader/read)

Passes a view into which data must be written, and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with the next chunk in the stream or rejects with an indication that the stream is closed or has errored.

[ReadableStreamBYOBReader.releaseLock()](/en-US/docs/Web/API/ReadableStreamBYOBReader/releaseLock)

Releases the reader's lock on the stream.

## [Examples](#examples)

The example below is taken from the live examples in [Using readable byte streams](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams#examples).

First create the reader using [ReadableStream.getReader()](/en-US/docs/Web/API/ReadableStream/getReader) on the stream, specifying `mode: "byob"` in the options parameter. As this is a "Bring Your Own Buffer" reader, we also need to create an `ArrayBuffer` to read into.

js

```
const reader = stream.getReader({ mode: "byob" });
let buffer = new ArrayBuffer(200);
```

A function that uses the reader is shown below. This calls the `read()` method recursively to read data into the buffer. The method takes a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)[typed array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) which is a view over the part of the original array buffer that has not yet been written. The parameters of the view are calculated from the data that was received in previous calls, which define an offset into the original array buffer.

js

```
readStream(reader);

function readStream(reader) {
  let bytesReceived = 0;
  let offset = 0;

  // read() returns a promise that resolves when a value has been received
  reader
    .read(new Uint8Array(buffer, offset, buffer.byteLength - offset))
    .then(function processText({ done, value }) {
      // Result objects contain two properties:
      // done  - true if the stream has already given all its data.
      // value - some data. Always undefined when done is true.

      if (done) {
        logConsumer(`readStream() complete. Total bytes: ${bytesReceived}`);
        return;
      }

      buffer = value.buffer;
      offset += value.byteLength;
      bytesReceived += value.byteLength;

      logConsumer(
        `Read ${value.byteLength} (${bytesReceived}) bytes: ${value}`,
      );
      result += value;

      // Read some more, and call this function again
      return reader
        .read(new Uint8Array(buffer, offset, buffer.byteLength - offset))
        .then(processText);
    });
}
```

When there is no more data in the stream, the `read()` method resolves with an object with the property `done` set to `true`, and the function returns.

The [ReadableStreamBYOBReader.closed](/en-US/docs/Web/API/ReadableStreamBYOBReader/closed) property returns a promise that can be used to monitor for the stream being closed or errored, or the reader lock being released.

js

```
reader.closed
  .then(() => {
    // Resolved - code to handle stream closing
  })
  .catch(() => {
    // Rejected - code to handle error
  });
```

To cancel the stream call [ReadableStreamBYOBReader.cancel()](/en-US/docs/Web/API/ReadableStreamBYOBReader/cancel), optionally specifying a reason. This returns a promise that will resolve when the stream has been cancelled. When the stream is cancelled the controller will in turn call `cancel()` on the underlying source, passing in the optional reason.

The example code in [Using readable byte streams](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams#examples) calls the cancel method when a button is pressed, as shown:

js

```
button.addEventListener("click", () => {
  reader.cancel("user choice").then(() => console.log("cancel complete"));
});
```

The consumer can also call `releaseLock()` to release the reader's hold on the stream, but only when no read is pending:

js

```
reader.releaseLock();
```

## [Specifications](#specifications)

Specification
[Streams# byob-reader-class](https://streams.spec.whatwg.org/#byob-reader-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API concepts](/en-US/docs/Web/API/Streams_API)
- [Using readable byte stream](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams)
- [ReadableStream](/en-US/docs/Web/API/ReadableStream)
- [Web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReadableStreamBYOBReader/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/readablestreambyobreader/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamBYOBReader&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freadablestreambyobreader%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamBYOBReader%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freadablestreambyobreader%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
