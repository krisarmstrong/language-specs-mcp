# Streams API

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Streams API allows JavaScript to programmatically access streams of data received over the network and process them as desired by the developer.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Stream interfaces](#stream_interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Streaming involves breaking a resource that you want to receive over a network down into small chunks, then processing it bit by bit. Browsers already do this when receiving media assets — videos buffer and play as more of the content downloads, and sometimes you'll see images display gradually as more is loaded too.

But this capability has never been available to JavaScript before. Previously, if we wanted to process a resource of some kind (video, text file, etc.), we'd have to download the entire file, wait for it to be deserialized into a suitable format, then process all the data.

With the Streams API, you can start processing raw data with JavaScript bit by bit, as soon as it is available, without needing to generate a buffer, string, or blob.

There are more advantages too — you can detect when streams start or end, chain streams together, handle errors and cancel streams as required, and react to the speed at which the stream is being read.

The usage of Streams hinges on making responses available as streams. For example, the response body returned by a successful [fetch request](/en-US/docs/Web/API/Window/fetch) is a [ReadableStream](/en-US/docs/Web/API/ReadableStream) that can be read by a reader created with [ReadableStream.getReader()](/en-US/docs/Web/API/ReadableStream/getReader).

More complicated uses involve creating your own stream using the [ReadableStream()](/en-US/docs/Web/API/ReadableStream/ReadableStream) constructor, for example to process data inside a [service worker](/en-US/docs/Web/API/Service_Worker_API).

You can also write data to streams using [WritableStream](/en-US/docs/Web/API/WritableStream).

Note: You can find a lot more details about the theory and practice of streams in our articles — [Streams API concepts](/en-US/docs/Web/API/Streams_API/Concepts), [Using readable streams](/en-US/docs/Web/API/Streams_API/Using_readable_streams), [Using readable byte streams](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams), and [Using writable streams](/en-US/docs/Web/API/Streams_API/Using_writable_streams).

## [Stream interfaces](#stream_interfaces)

### [Readable streams](#readable_streams)

[ReadableStream](/en-US/docs/Web/API/ReadableStream)

Represents a readable stream of data. It can be used to handle response streams of the [Fetch API](/en-US/docs/Web/API/Fetch_API), or developer-defined streams (e.g., a custom [ReadableStream()](/en-US/docs/Web/API/ReadableStream/ReadableStream) constructor).

[ReadableStreamDefaultReader](/en-US/docs/Web/API/ReadableStreamDefaultReader)

Represents a default reader that can be used to read stream data supplied from a network (e.g., a fetch request).

[ReadableStreamDefaultController](/en-US/docs/Web/API/ReadableStreamDefaultController)

Represents a controller allowing control of a [ReadableStream](/en-US/docs/Web/API/ReadableStream)'s state and internal queue. Default controllers are for streams that are not byte streams.

### [Writable streams](#writable_streams)

[WritableStream](/en-US/docs/Web/API/WritableStream)

Provides a standard abstraction for writing streaming data to a destination, known as a sink. This object comes with built-in backpressure and queuing.

[WritableStreamDefaultWriter](/en-US/docs/Web/API/WritableStreamDefaultWriter)

Represents a default writable stream writer that can be used to write chunks of data to a writable stream.

[WritableStreamDefaultController](/en-US/docs/Web/API/WritableStreamDefaultController)

Represents a controller allowing control of a [WritableStream](/en-US/docs/Web/API/WritableStream)'s state. When constructing a `WritableStream`, the underlying sink is given a corresponding `WritableStreamDefaultController` instance to manipulate.

### [Transform Streams](#transform_streams)

[TransformStream](/en-US/docs/Web/API/TransformStream)

Represents an abstraction for a stream object that transforms data as it passes through a [pipe chain](/en-US/docs/Web/API/Streams_API/Concepts#pipe_chains) of stream objects.

[TransformStreamDefaultController](/en-US/docs/Web/API/TransformStreamDefaultController)

Provides methods to manipulate the [ReadableStream](/en-US/docs/Web/API/ReadableStream) and [WritableStream](/en-US/docs/Web/API/WritableStream) associated with a transform stream.

### [Related stream APIs and operations](#related_stream_apis_and_operations)

[ByteLengthQueuingStrategy](/en-US/docs/Web/API/ByteLengthQueuingStrategy)

Provides a built-in byte length queuing strategy that can be used when constructing streams.

[CountQueuingStrategy](/en-US/docs/Web/API/CountQueuingStrategy)

Provides a built-in chunk counting queuing strategy that can be used when constructing streams.

### [Extensions to other APIs](#extensions_to_other_apis)

[Request](/en-US/docs/Web/API/Request)

When a new `Request` object is constructed, you can pass it a [ReadableStream](/en-US/docs/Web/API/ReadableStream) in the `body` property of its `RequestInit` dictionary. This `Request` could then be passed to a [fetch()](/en-US/docs/Web/API/Window/fetch) to commence fetching the stream.

[Response.body](/en-US/docs/Web/API/Response/body)

The response body returned by a successful [fetch request](/en-US/docs/Web/API/Window/fetch) is exposed by default as a [ReadableStream](/en-US/docs/Web/API/ReadableStream), and can have a reader attached to it, etc.

### [ByteStream-related interfaces](#bytestream-related_interfaces)

[ReadableStreamBYOBReader](/en-US/docs/Web/API/ReadableStreamBYOBReader)

Represents a BYOB ("bring your own buffer") reader that can be used to read stream data supplied by the developer (e.g., a custom [ReadableStream()](/en-US/docs/Web/API/ReadableStream/ReadableStream) constructor).

[ReadableByteStreamController](/en-US/docs/Web/API/ReadableByteStreamController)

Represents a controller allowing control of a [ReadableStream](/en-US/docs/Web/API/ReadableStream)'s state and internal queue. Byte stream controllers are for byte streams.

[ReadableStreamBYOBRequest](/en-US/docs/Web/API/ReadableStreamBYOBRequest)

Represents a pull into request in a [ReadableByteStreamController](/en-US/docs/Web/API/ReadableByteStreamController).

## [Examples](#examples)

We have created a directory of examples to go along with the Streams API documentation — see [mdn/dom-examples/streams](https://github.com/mdn/dom-examples/tree/main/streams). The examples are as follows:

- [Simple stream pump](https://mdn.github.io/dom-examples/streams/simple-pump/): This example shows how to consume a ReadableStream and pass its data to another.
- [Grayscale a PNG](https://mdn.github.io/dom-examples/streams/grayscale-png/): This example shows how a ReadableStream of a PNG can be turned into grayscale.
- [Simple random stream](https://mdn.github.io/dom-examples/streams/simple-random-stream/): This example shows how to use a custom stream to generate random strings, enqueue them as chunks, and then read them back out again.
- [Simple tee example](https://mdn.github.io/dom-examples/streams/simple-tee-example/): This example extends the Simple random stream example, showing how a stream can be teed and both resulting streams can be read independently.
- [Simple writer](https://mdn.github.io/dom-examples/streams/simple-writer/): This example shows how to write to a writable stream, then decode the stream and write the contents to the UI.
- [Unpack chunks of a PNG](https://mdn.github.io/dom-examples/streams/png-transform-stream/): This example shows how [pipeThrough()](/en-US/docs/Web/API/ReadableStream/pipeThrough) can be used to transform a ReadableStream into a stream of other data types by transforming a data of a PNG file into a stream of PNG chunks.

Examples from other developers:

- [Progress Indicators with Streams, Service Workers, & Fetch](https://fetch-progress.anthum.com/).

## [Specifications](#specifications)

Specification
[Streams# rs-class](https://streams.spec.whatwg.org/#rs-class)
[Streams# ws-class](https://streams.spec.whatwg.org/#ws-class)

## [Browser compatibility](#browser_compatibility)

### [api.ReadableStream](#api.ReadableStream)

### [api.WritableStream](#api.WritableStream)

## [See also](#see_also)

- [Streams API concepts](/en-US/docs/Web/API/Streams_API/Concepts)
- [Using readable streams](/en-US/docs/Web/API/Streams_API/Using_readable_streams)
- [Using readable byte streams](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams)
- [Using writable streams](/en-US/docs/Web/API/Streams_API/Using_writable_streams)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Streams_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/streams_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStreams_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstreams_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStreams_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstreams_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
