# WritableStreamDefaultWriter

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStreamDefaultWriter&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WritableStreamDefaultWriter` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) is the object returned by [WritableStream.getWriter()](/en-US/docs/Web/API/WritableStream/getWriter) and once created locks the writer to the `WritableStream` ensuring that no other streams can write to the underlying sink.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[WritableStreamDefaultWriter()](/en-US/docs/Web/API/WritableStreamDefaultWriter/WritableStreamDefaultWriter)

Creates a new `WritableStreamDefaultWriter` object instance.

## [Instance properties](#instance_properties)

[WritableStreamDefaultWriter.closed](/en-US/docs/Web/API/WritableStreamDefaultWriter/closed)Read only

Allows you to write code that responds to an end to the streaming process. Returns a promise that fulfills if the stream becomes closed, or rejects if the stream errors or the writer's lock is released.

[WritableStreamDefaultWriter.desiredSize](/en-US/docs/Web/API/WritableStreamDefaultWriter/desiredSize)Read only

Returns the desired size required to fill the stream's internal queue.

[WritableStreamDefaultWriter.ready](/en-US/docs/Web/API/WritableStreamDefaultWriter/ready)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the desired size of the stream's internal queue transitions from non-positive to positive, signaling that it is no longer applying backpressure.

## [Instance methods](#instance_methods)

[WritableStreamDefaultWriter.abort()](/en-US/docs/Web/API/WritableStreamDefaultWriter/abort)

Aborts the stream, signaling that the producer can no longer successfully write to the stream and it is to be immediately moved to an error state, with any queued writes discarded.

[WritableStreamDefaultWriter.close()](/en-US/docs/Web/API/WritableStreamDefaultWriter/close)

Closes the associated writable stream.

[WritableStreamDefaultWriter.releaseLock()](/en-US/docs/Web/API/WritableStreamDefaultWriter/releaseLock)

Releases the writer's lock on the corresponding stream. After the lock is released, the writer is no longer active. If the associated stream is errored when the lock is released, the writer will appear errored in the same way from now on; otherwise, the writer will appear closed.

[WritableStreamDefaultWriter.write()](/en-US/docs/Web/API/WritableStreamDefaultWriter/write)

Writes a passed chunk of data to a [WritableStream](/en-US/docs/Web/API/WritableStream) and its underlying sink, then returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to indicate the success or failure of the write operation.

## [Examples](#examples)

The following example shows the creation of a `WritableStream` with a custom sink and an API-supplied queuing strategy. It then calls a function called `sendMessage()`, passing the newly created stream and a string. Inside this function it calls the stream's `getWriter()` method, which returns an instance of `WritableStreamDefaultWriter`. A `forEach()` call is used to write each chunk of the string to the stream. Finally, `write()` and `close()` return promises that are processed to deal with success or failure of chunks and streams.

js

```
const list = document.querySelector("ul");

async function sendMessage(message, writableStream) {
  // defaultWriter is of type WritableStreamDefaultWriter
  const defaultWriter = writableStream.getWriter();
  const encoder = new TextEncoder();
  const encoded = encoder.encode(message);

  try {
    for (const chunk of encoded) {
      await defaultWriter.ready;
      await defaultWriter.write(chunk);
      console.log("Chunk written to sink.");
    }
    // Call ready again to ensure that all chunks are written
    // before closing the writer.
    await defaultWriter.ready;
    await defaultWriter.close();
    console.log("All chunks written");
  } catch (err) {
    console.log("Error:", err);
  }
}

const decoder = new TextDecoder("utf-8");
const queuingStrategy = new CountQueuingStrategy({ highWaterMark: 1 });
let result = "";
const writableStream = new WritableStream(
  {
    // Implement the sink
    write(chunk) {
      return new Promise((resolve, reject) => {
        const buffer = new ArrayBuffer(1);
        const view = new Uint8Array(buffer);
        view[0] = chunk;
        const decoded = decoder.decode(view, { stream: true });
        const listItem = document.createElement("li");
        listItem.textContent = `Chunk decoded: ${decoded}`;
        list.appendChild(listItem);
        result += decoded;
        resolve();
      });
    },
    close() {
      const listItem = document.createElement("li");
      listItem.textContent = `[MESSAGE RECEIVED] ${result}`;
      list.appendChild(listItem);
    },
    abort(err) {
      console.log("Sink error:", err);
    },
  },
  queuingStrategy,
);

sendMessage("Hello, world.", writableStream);
```

You can find the full code in our [Simple writer example](https://mdn.github.io/dom-examples/streams/simple-writer/).

## [Specifications](#specifications)

Specification
[Streams# default-writer-class](https://streams.spec.whatwg.org/#default-writer-class)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WritableStreamDefaultWriter/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/writablestreamdefaultwriter/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStreamDefaultWriter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwritablestreamdefaultwriter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWritableStreamDefaultWriter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwritablestreamdefaultwriter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
