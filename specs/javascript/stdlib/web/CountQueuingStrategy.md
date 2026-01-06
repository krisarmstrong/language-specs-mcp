# CountQueuingStrategy

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCountQueuingStrategy&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `CountQueuingStrategy` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) provides a built-in chunk counting queuing strategy that can be used when constructing streams.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CountQueuingStrategy()](/en-US/docs/Web/API/CountQueuingStrategy/CountQueuingStrategy)

Creates a new `CountQueuingStrategy` object instance.

## [Instance properties](#instance_properties)

[CountQueuingStrategy.highWaterMark](/en-US/docs/Web/API/CountQueuingStrategy/highWaterMark)Read only

The total number of chunks that can be contained in the internal queue before [backpressure](/en-US/docs/Web/API/Streams_API/Concepts#backpressure) is applied.

## [Instance methods](#instance_methods)

[CountQueuingStrategy.size()](/en-US/docs/Web/API/CountQueuingStrategy/size)

Always returns `1`.

## [Examples](#examples)

js

```
const queueingStrategy = new CountQueuingStrategy({ highWaterMark: 1 });

const writableStream = new WritableStream(
  {
    // Implement the sink
    write(chunk) {
      // …
    },
    close() {
      // …
    },
    abort(err) {
      console.log("Sink error:", err);
    },
  },
  queueingStrategy,
);

const size = queueingStrategy.size();
```

## [Specifications](#specifications)

Specification
[Streams# cqs-class](https://streams.spec.whatwg.org/#cqs-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API](/en-US/docs/Web/API/Streams_API)
- [CountQueuingStrategy()](/en-US/docs/Web/API/CountQueuingStrategy/CountQueuingStrategy) constructor
- [Internal queues and queuing strategies](/en-US/docs/Web/API/Streams_API/Concepts#internal_queues_and_queuing_strategies)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CountQueuingStrategy/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/countqueuingstrategy/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCountQueuingStrategy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcountqueuingstrategy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCountQueuingStrategy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcountqueuingstrategy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8b4431bfde42f1bc195239ea1f378d763f8163e%0A*+Document+last+modified%3A+2024-04-22T06%3A16%3A40.000Z%0A%0A%3C%2Fdetails%3E)
