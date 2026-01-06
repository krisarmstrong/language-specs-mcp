# ReadableStreamBYOBRequest

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamBYOBRequest&level=not)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReadableStreamBYOBRequest` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a "pull request" for data from an underlying source that will made as a zero-copy transfer to a consumer (bypassing the stream's internal queues).

`ReadableStreamBYOBRequest` objects are created in "BYOB mode" when a consumer makes a request for data and the stream's internal queue is empty. (The stream will resolve the consumer's request directly if it already has buffered data). An underlying byte source can access active BYOB requests through its controller's [ReadableByteStreamController.byobRequest](/en-US/docs/Web/API/ReadableByteStreamController/byobRequest) property, which will be set to `null` if there is no outstanding request.

An underlying source that supports "BYOB mode" should check for [ReadableByteStreamController.byobRequest](/en-US/docs/Web/API/ReadableByteStreamController/byobRequest) and must use it for transferring data, if present. If data arrives from the underlying source when [ReadableByteStreamController.byobRequest](/en-US/docs/Web/API/ReadableByteStreamController/byobRequest) is `null`, it can be queued using [ReadableByteStreamController.enqueue()](/en-US/docs/Web/API/ReadableByteStreamController/enqueue). This might happen when an underlying push source receives new data when the stream's internal buffers are not empty.

An underlying source uses the request by writing data to the BYOB request's [view](/en-US/docs/Web/API/ReadableStreamBYOBRequest/view) and then calling [respond()](/en-US/docs/Web/API/ReadableStreamBYOBRequest/respond), or by calling [respondWithNewView()](/en-US/docs/Web/API/ReadableStreamBYOBRequest/respondWithNewView) and passing a new view as an argument. Note that the "new view" must actually be a view over the same buffer as the original `view`, starting at the same offset. This might be used to return a shorter buffer if the underlying source is unable to fill the entire original view.

Note that a [ReadableByteStreamController](/en-US/docs/Web/API/ReadableByteStreamController) is only created for underlying sources when `type="bytes"` is specified for the source in the [ReadableStream() constructor](/en-US/docs/Web/API/ReadableStream/ReadableStream#type). "BYOB mode" is enabled when either [autoAllocateChunkSize](/en-US/docs/Web/API/ReadableStream/ReadableStream#autoallocatechunksize) is specified in the [ReadableController() constructor](/en-US/docs/Web/API/ReadableStream/ReadableStream#autoallocatechunksize) or when using a [ReadableStreamBYOBReader](/en-US/docs/Web/API/ReadableStreamBYOBReader) (typically constructed by calling [ReadableStream.getReader()](/en-US/docs/Web/API/ReadableStream/getReader) with the argument `{ mode: 'byob' }`).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

None. `ReadableStreamBYOBRequest` instance is created automatically by `ReadableByteStreamController` as needed.

## [Instance properties](#instance_properties)

[ReadableStreamBYOBRequest.view](/en-US/docs/Web/API/ReadableStreamBYOBRequest/view)Read only

Returns the current view. This is a view on a buffer that will be transferred to the consumer when `ReadableStreamBYOBRequest.respond()` is called.

## [Instance methods](#instance_methods)

[ReadableStreamBYOBRequest.respond()](/en-US/docs/Web/API/ReadableStreamBYOBRequest/respond)

Signals the associated readable byte stream that the specified number of bytes were written into the current [view](/en-US/docs/Web/API/ReadableStreamBYOBRequest/view), which then causes the pending request from the consumer to be resolved. Note that after this method is called the `view` is transferred and no longer modifiable.

[ReadableStreamBYOBRequest.respondWithNewView()](/en-US/docs/Web/API/ReadableStreamBYOBRequest/respondWithNewView)

Signals to the associated readable byte stream view passed as an argument should be transferred to the consumer of the readable byte stream. This new view must use the same buffer as the original [view](/en-US/docs/Web/API/ReadableStreamBYOBRequest/view), start at the same offset, and be the same length or shorter. Note that after this method is called the `view` is transferred and no longer modifiable.

## [Examples](#examples)

The following code is taken from the live example in [Using readable byte streams > Creating a readable socket push byte stream](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams#creating_a_readable_socket_push_byte_stream).

A push underlying byte source with data to transfer should first check that [controller.byobRequest](/en-US/docs/Web/API/ReadableByteStreamController/byobRequest) is non-`null`. Pul A pull underlying byte source would only need this check if auto chunk allocation was not enabled and it was used with a default reader.

js

```
if (controller.byobRequest) {
  /* code to transfer data */
}
```

There are two ways to read data into a `ReadableStreamBYOBRequest` and then transfer it. The first is to write the data into the [ReadableStreamBYOBRequest.view](/en-US/docs/Web/API/ReadableStreamBYOBRequest/view) property and then call [ReadableStreamBYOBRequest.respond()](/en-US/docs/Web/API/ReadableStreamBYOBRequest/respond) to indicate the amount of data to be transferred. After the operation the `byobRequest.view` is detached and the request should be discarded.

The code below shows this case using a hypothetical `readInto()` method to copy data into the view:

js

```
const v = controller.byobRequest.view;
bytesRead = socket.readInto(v.buffer, v.byteOffset, v.byteLength);
controller.byobRequest.respond(bytesRead);
```

The other approach is to call [ReadableStreamBYOBRequest.respondWithNewView()](/en-US/docs/Web/API/ReadableStreamBYOBRequest/respondWithNewView) passing your own view on the same underlying backing data. Note that this just another way of specifying the range of the underlying buffer/memory backing that is actually transferred. The `respondWithNewView` equivalent to the code above would be:

js

```
const v = controller.byobRequest.view;
bytesRead = socket.readInto(v.buffer, v.byteOffset, v.byteLength);
const newView = new Uint8Array(v.buffer, v.byteOffset, bytesRead);
controller.byobRequest.respondWithNewView(newView);
```

## [Specifications](#specifications)

Specification
[Streams# rs-byob-request-class](https://streams.spec.whatwg.org/#rs-byob-request-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using readable byte stream](/en-US/docs/Web/API/Streams_API/Using_readable_byte_streams)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReadableStreamBYOBRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/readablestreambyobrequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamBYOBRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freadablestreambyobrequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamBYOBRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freadablestreambyobrequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
