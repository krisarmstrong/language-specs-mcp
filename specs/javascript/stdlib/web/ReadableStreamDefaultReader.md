# ReadableStreamDefaultReader

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamDefaultReader&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReadableStreamDefaultReader` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a default reader that can be used to read stream data supplied from a network (such as a fetch request).

A `ReadableStreamDefaultReader` can be used to read from a [ReadableStream](/en-US/docs/Web/API/ReadableStream) that has an underlying source of any type (unlike a [ReadableStreamBYOBReader](/en-US/docs/Web/API/ReadableStreamBYOBReader), which can only be used with readable streams that have an underlying byte source).

Note however that zero-copy transfer from an underlying source is only supported for underlying byte sources that autoallocate buffers. In other words, the stream must have been [constructed](/en-US/docs/Web/API/ReadableStream/ReadableStream) specifying both [type="bytes"](/en-US/docs/Web/API/ReadableStream/ReadableStream#type) and [autoAllocateChunkSize](/en-US/docs/Web/API/ReadableStream/ReadableStream#autoallocatechunksize). For any other underlying source, the stream will always satisfy read requests with data from internal queues.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ReadableStreamDefaultReader()](/en-US/docs/Web/API/ReadableStreamDefaultReader/ReadableStreamDefaultReader)

Creates and returns a `ReadableStreamDefaultReader` object instance.

## [Instance properties](#instance_properties)

[ReadableStreamDefaultReader.closed](/en-US/docs/Web/API/ReadableStreamDefaultReader/closed)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills when the stream closes, or rejects if the stream throws an error or the reader's lock is released. This property enables you to write code that responds to an end to the streaming process.

## [Instance methods](#instance_methods)

[ReadableStreamDefaultReader.cancel()](/en-US/docs/Web/API/ReadableStreamDefaultReader/cancel)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the stream is canceled. Calling this method signals a loss of interest in the stream by a consumer. The supplied `reason` argument will be given to the underlying source, which may or may not use it.

[ReadableStreamDefaultReader.read()](/en-US/docs/Web/API/ReadableStreamDefaultReader/read)

Returns a promise providing access to the next chunk in the stream's internal queue.

[ReadableStreamDefaultReader.releaseLock()](/en-US/docs/Web/API/ReadableStreamDefaultReader/releaseLock)

Releases the reader's lock on the stream.

## [Examples](#examples)

In the following example, an artificial [Response](/en-US/docs/Web/API/Response) is created to stream HTML fragments fetched from another resource to the browser.

It demonstrates the usage of a [ReadableStream](/en-US/docs/Web/API/ReadableStream) in combination with a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array).

js

```
fetch("https://www.example.org/").then((response) => {
  const reader = response.body.getReader();
  const stream = new ReadableStream({
    start(controller) {
      // The following function handles each data chunk
      function push() {
        // "done" is a Boolean and value a "Uint8Array"
        return reader.read().then(({ done, value }) => {
          // Is there no more data to read?
          if (done) {
            // Tell the browser that we have finished sending data
            controller.close();
            return;
          }

          // Get the data and send it to the browser via the controller
          controller.enqueue(value);
          push();
        });
      }

      push();
    },
  });

  return new Response(stream, { headers: { "Content-Type": "text/html" } });
});
```

## [Specifications](#specifications)

Specification
[Streams# default-reader-class](https://streams.spec.whatwg.org/#default-reader-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API concepts](/en-US/docs/Web/API/Streams_API)
- [Using readable streams](/en-US/docs/Web/API/Streams_API/Using_readable_streams)
- [ReadableStream](/en-US/docs/Web/API/ReadableStream)
- [Web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReadableStreamDefaultReader/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/readablestreamdefaultreader/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamDefaultReader&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freadablestreamdefaultreader%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamDefaultReader%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freadablestreamdefaultreader%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
