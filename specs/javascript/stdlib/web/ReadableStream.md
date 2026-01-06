# ReadableStream

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2019⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStream&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReadableStream` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a readable stream of byte data. The [Fetch API](/en-US/docs/Web/API/Fetch_API) offers a concrete instance of a `ReadableStream` through the [body](/en-US/docs/Web/API/Response/body) property of a [Response](/en-US/docs/Web/API/Response) object.

`ReadableStream` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Async iteration](#async_iteration)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ReadableStream()](/en-US/docs/Web/API/ReadableStream/ReadableStream)

Creates and returns a readable stream object from the given handlers.

## [Instance properties](#instance_properties)

[ReadableStream.locked](/en-US/docs/Web/API/ReadableStream/locked)Read only

Returns a boolean indicating whether or not the readable stream is locked to a reader.

## [Static methods](#static_methods)

[ReadableStream.from()](/en-US/docs/Web/API/ReadableStream/from_static)Experimental

Returns `ReadableStream` from a provided iterable or async iterable object, such as an array, a set, an async generator, and so on.

## [Instance methods](#instance_methods)

[ReadableStream.cancel()](/en-US/docs/Web/API/ReadableStream/cancel)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the stream is canceled. Calling this method signals a loss of interest in the stream by a consumer. The supplied `reason` argument will be given to the underlying source, which may or may not use it.

[ReadableStream.getReader()](/en-US/docs/Web/API/ReadableStream/getReader)

Creates a reader and locks the stream to it. While the stream is locked, no other reader can be acquired until this one is released.

[ReadableStream.pipeThrough()](/en-US/docs/Web/API/ReadableStream/pipeThrough)

Provides a chainable way of piping the current stream through a transform stream or any other writable/readable pair.

[ReadableStream.pipeTo()](/en-US/docs/Web/API/ReadableStream/pipeTo)

Pipes the current ReadableStream to a given [WritableStream](/en-US/docs/Web/API/WritableStream) and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills when the piping process completes successfully, or rejects if any errors were encountered.

[ReadableStream.tee()](/en-US/docs/Web/API/ReadableStream/tee)

The `tee` method [tees](https://streams.spec.whatwg.org/#tee-a-readable-stream) this readable stream, returning a two-element array containing the two resulting branches as new `ReadableStream` instances. Each of those streams receives the same incoming data.

## [Async iteration](#async_iteration)

`ReadableStream` implements the [async iterable protocol](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols). This enables asynchronous iteration over the chunks in a stream using the [for await...of](/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of) syntax:

js

```
const stream = new ReadableStream(getSomeSource());

for await (const chunk of stream) {
  // Do something with each 'chunk'
}
```

The async iterator consumes the stream until it runs out of data or otherwise terminates. The loop can also exit early due to a `break`, `throw`, or `return` statement.

While iterating, the stream is locked to prevent other consumers from acquiring a reader (attempting to iterate over a stream that is already locked will throw a `TypeError`). This lock is released when the loop exits.

By default, exiting the loop will also cancel the stream, so that it can no longer be used. To continue to use a stream after exiting the loop, pass `{ preventCancel: true }` to the stream's `values()` method:

js

```
for await (const chunk of stream.values({ preventCancel: true })) {
  // Do something with 'chunk'
  break;
}
// Acquire a reader for the stream and continue reading ...
```

## [Examples](#examples)

### [Fetch stream](#fetch_stream)

In the following example, an artificial [Response](/en-US/docs/Web/API/Response) is created to stream HTML fragments fetched from another resource to the browser.

It demonstrates the usage of a `ReadableStream` in combination with a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array).

js

```
fetch("https://www.example.org")
  .then((response) => response.body)
  .then((rb) => {
    const reader = rb.getReader();

    return new ReadableStream({
      start(controller) {
        // The following function handles each data chunk
        function push() {
          // "done" is a Boolean and value a "Uint8Array"
          reader.read().then(({ done, value }) => {
            // If there is no more data to read
            if (done) {
              console.log("done", done);
              controller.close();
              return;
            }
            // Get the data and send it to the browser via the controller
            controller.enqueue(value);
            // Check chunks by logging to the console
            console.log(done, value);
            push();
          });
        }

        push();
      },
    });
  })
  .then((stream) =>
    // Respond with our stream
    new Response(stream, { headers: { "Content-Type": "text/html" } }).text(),
  )
  .then((result) => {
    // Do things with result
    console.log(result);
  });
```

### [Convert an iterator or async iterator to a stream](#convert_an_iterator_or_async_iterator_to_a_stream)

The [from()](/en-US/docs/Web/API/ReadableStream/from_static) static method can convert an iterator, such as an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) or [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), or an [(async) iterator](/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators) to a readable stream:

js

```
const myReadableStream = ReadableStream.from(iteratorOrAsyncIterator);
```

On browsers that don't support the `from()` method you can instead create your own [custom readable stream](/en-US/docs/Web/API/Streams_API/Using_readable_streams#creating_your_own_custom_readable_stream) to achieve the same result:

js

```
function iteratorToStream(iterator) {
  return new ReadableStream({
    async pull(controller) {
      const { value, done } = await iterator.next();

      if (value) {
        controller.enqueue(value);
      }
      if (done) {
        controller.close();
      }
    },
  });
}
```

Warning: This example assumes that the return value (`value` when `done` is `true`), if present, is also a chunk to be enqueued. Some iterator APIs may use the return value for different purposes. You may need to adjust the code based on the API you are interacting with.

### [Async iteration of a stream using for await...of](#async_iteration_of_a_stream_using_for_await...of)

This example shows how you can process the `fetch()` response using a [for await...of](/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of) loop to iterate through the arriving chunks.

js

```
const response = await fetch("https://www.example.org");
let total = 0;

// Iterate response.body (a ReadableStream) asynchronously
for await (const chunk of response.body) {
  // Do something with each chunk
  // Here we just accumulate the size of the response.
  total += chunk.length;
}

// Do something with the total
console.log(total);
```

## [Specifications](#specifications)

Specification
[Streams# rs-class](https://streams.spec.whatwg.org/#rs-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API concepts](/en-US/docs/Web/API/Streams_API)
- [Using readable streams](/en-US/docs/Web/API/Streams_API/Using_readable_streams)
- [Using readable byte stream](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams)
- [Web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReadableStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/readablestream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freadablestream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freadablestream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
