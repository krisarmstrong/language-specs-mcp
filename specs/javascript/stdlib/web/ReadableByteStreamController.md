# ReadableByteStreamController

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableByteStreamController&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReadableByteStreamController` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a controller for a [readable byte stream](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams). It allows control of the state and internal queue of a [ReadableStream](/en-US/docs/Web/API/ReadableStream) with an underlying byte source, and enables efficient zero-copy transfer of data from the underlying source to a consumer when the stream's internal queue is empty.

An instance of this controller type is created if an `underlyingSource` object with the property `type="bytes"` is passed as an argument to the [ReadableStream() constructor](/en-US/docs/Web/API/ReadableStream/ReadableStream#type). The `underlyingSource` object may also define [start()](/en-US/docs/Web/API/ReadableStream/ReadableStream#start) and [pull()](/en-US/docs/Web/API/ReadableStream/ReadableStream#pull) callback functions. These are called with the controller as a parameter, in order to set up the underlying source, and request data when needed.

The underlying source uses the controller to supply data to the stream via its [byobRequest](/en-US/docs/Web/API/ReadableByteStreamController/byobRequest) property or [enqueue()](/en-US/docs/Web/API/ReadableByteStreamController/enqueue) method. `byobRequest` is a [ReadableStreamBYOBRequest](/en-US/docs/Web/API/ReadableStreamBYOBRequest) object that represents a pending request from a consumer to make a zero-copy transfer of data direct to a consumer. `byobRequest` must be used to copy data if it exists (do not use `enqueue()` in this case)! If the underlying source needs to pass data to the stream and `byobRequest` is `null` then the source can call `enqueue()` to add the data to the stream's internal queues.

Note that the `byobRequest` is only created in "BYOB mode" when there is a request from a reader and the stream's internal queue is empty. "BYOB mode" is enabled when using a [ReadableStreamBYOBReader](/en-US/docs/Web/API/ReadableStreamBYOBReader) (typically constructed by calling [ReadableStream.getReader()](/en-US/docs/Web/API/ReadableStream/getReader) with the argument `{ mode: 'byob' }`). It is also enabled when using a default reader and [autoAllocateChunkSize](/en-US/docs/Web/API/ReadableStream/ReadableStream#autoallocatechunksize) is specified in the [ReadableStream() constructor](/en-US/docs/Web/API/ReadableStream/ReadableStream).

An underlying byte source can also use the controller to [close()](/en-US/docs/Web/API/ReadableByteStreamController/close) the stream when all the data has been sent and report errors from the underlying source using [error()](/en-US/docs/Web/API/ReadableByteStreamController/error). The controller's [desiredSize](/en-US/docs/Web/API/ReadableByteStreamController/desiredSize) property is used to apply "backpressure", informing the underlying source of the size of the internal queue (small values indicate that the queue is filling up, hinting to the underlying source that it is be desirable to pause or throttle the inflow).

Note that even though the controller is primarily used by the underlying byte source, there is no reason it cannot be stored used by other parts of the system to signal the stream.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

None. `ReadableByteStreamController` instances are automatically created if an `underlyingSource` with the property `type="bytes"` is passed to the [ReadableStream() constructor](/en-US/docs/Web/API/ReadableStream/ReadableStream#type).

## [Instance properties](#instance_properties)

[ReadableByteStreamController.byobRequest](/en-US/docs/Web/API/ReadableByteStreamController/byobRequest)Read only

Returns the current BYOB pull request, or `null` if there no outstanding request.

[ReadableByteStreamController.desiredSize](/en-US/docs/Web/API/ReadableByteStreamController/desiredSize)Read only

Returns the desired size required to fill the stream's internal queue.

## [Instance methods](#instance_methods)

[ReadableByteStreamController.close()](/en-US/docs/Web/API/ReadableByteStreamController/close)

Closes the associated stream.

[ReadableByteStreamController.enqueue()](/en-US/docs/Web/API/ReadableByteStreamController/enqueue)

Enqueues a given chunk in the associated stream.

[ReadableByteStreamController.error()](/en-US/docs/Web/API/ReadableByteStreamController/error)

Causes any future interactions with the associated stream to error.

## [Examples](#examples)

The controller is used by an underlying source to transfer or enqueue data, to signal that the stream has no more data (has closed) or has errored. It is also used to signal the underlying source from "upstream" of the desired data rate, using [desiredSize](/en-US/docs/Web/API/ReadableByteStreamController/desiredSize).

The example in [Using readable byte streams](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams), in particular [Creating a readable socket push byte stream](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams#creating_a_readable_socket_push_byte_stream), show most of these cases.

## [Specifications](#specifications)

Specification
[Streams# rbs-controller-class](https://streams.spec.whatwg.org/#rbs-controller-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API concepts](/en-US/docs/Web/API/Streams_API)
- [Using readable byte streams](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams)
- [ReadableStream](/en-US/docs/Web/API/ReadableStream)
- [Web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReadableByteStreamController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/readablebytestreamcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableByteStreamController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freadablebytestreamcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableByteStreamController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freadablebytestreamcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
