# ReadableStreamDefaultController

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamDefaultController&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ReadableStreamDefaultController` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) represents a controller allowing control of a [ReadableStream](/en-US/docs/Web/API/ReadableStream)'s state and internal queue. Default controllers are for streams that are not byte streams.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

None. `ReadableStreamDefaultController` instances are created automatically during `ReadableStream` construction.

## [Instance properties](#instance_properties)

[ReadableStreamDefaultController.desiredSize](/en-US/docs/Web/API/ReadableStreamDefaultController/desiredSize)Read only

Returns the desired size required to fill the stream's internal queue.

## [Instance methods](#instance_methods)

[ReadableStreamDefaultController.close()](/en-US/docs/Web/API/ReadableStreamDefaultController/close)

Closes the associated stream.

[ReadableStreamDefaultController.enqueue()](/en-US/docs/Web/API/ReadableStreamDefaultController/enqueue)

Enqueues a given chunk in the associated stream.

[ReadableStreamDefaultController.error()](/en-US/docs/Web/API/ReadableStreamDefaultController/error)

Causes any future interactions with the associated stream to error.

## [Examples](#examples)

In the following simple example, a custom `ReadableStream` is created using a constructor (see our [Simple random stream example](https://mdn.github.io/dom-examples/streams/simple-random-stream/) for the full code). The `start()` function generates a random string of text every second and enqueues it into the stream. A `cancel()` function is also provided to stop the generation if [ReadableStream.cancel()](/en-US/docs/Web/API/ReadableStream/cancel) is called for any reason.

Note that a `ReadableStreamDefaultController` object is provided as the parameter of the `start()` and `pull()` functions.

When a button is pressed, the generation is stopped, the stream is closed using [ReadableStreamDefaultController.close()](/en-US/docs/Web/API/ReadableStreamDefaultController/close), and another function is run, which reads the data back out of the stream.

js

```
let interval;
const stream = new ReadableStream({
  start(controller) {
    interval = setInterval(() => {
      let string = randomChars();

      // Add the string to the stream
      controller.enqueue(string);

      // show it on the screen
      let listItem = document.createElement("li");
      listItem.textContent = string;
      list1.appendChild(listItem);
    }, 1000);

    button.addEventListener("click", () => {
      clearInterval(interval);
      fetchStream();
      controller.close();
    });
  },
  pull(controller) {
    // We don't really need a pull in this example
  },
  cancel() {
    // This is called if the reader cancels,
    // so we should stop generating strings
    clearInterval(interval);
  },
});
```

## [Specifications](#specifications)

Specification
[Streams# rs-default-controller-class](https://streams.spec.whatwg.org/#rs-default-controller-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API concepts](/en-US/docs/Web/API/Streams_API)
- [Using readable streams](/en-US/docs/Web/API/Streams_API/Using_readable_streams)
- [ReadableStream](/en-US/docs/Web/API/ReadableStream)
- [Web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ReadableStreamDefaultController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/readablestreamdefaultcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamDefaultController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Freadablestreamdefaultcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FReadableStreamDefaultController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Freadablestreamdefaultcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ca040b6a9cfd931558bd1d3a402707abddc1924%0A*+Document+last+modified%3A+2025-09-08T12%3A26%3A52.000Z%0A%0A%3C%2Fdetails%3E)
