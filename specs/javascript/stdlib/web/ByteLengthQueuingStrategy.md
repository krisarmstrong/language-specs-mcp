# ByteLengthQueuingStrategy

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FByteLengthQueuingStrategy&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ByteLengthQueuingStrategy` interface of the [Streams API](/en-US/docs/Web/API/Streams_API) provides a built-in byte length queuing strategy that can be used when constructing streams.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ByteLengthQueuingStrategy()](/en-US/docs/Web/API/ByteLengthQueuingStrategy/ByteLengthQueuingStrategy)

Creates a new `ByteLengthQueuingStrategy` object instance.

## [Instance properties](#instance_properties)

[ByteLengthQueuingStrategy.highWaterMark](/en-US/docs/Web/API/ByteLengthQueuingStrategy/highWaterMark)Read only

The total number of bytes that can be contained in the internal queue before [backpressure](/en-US/docs/Web/API/Streams_API/Concepts#backpressure) is applied.

## [Instance methods](#instance_methods)

[ByteLengthQueuingStrategy.size()](/en-US/docs/Web/API/ByteLengthQueuingStrategy/size)

Returns the given chunk's `byteLength` property.

## [Examples](#examples)

js

```
const queueingStrategy = new ByteLengthQueuingStrategy({ highWaterMark: 1024 });

const readableStream = new ReadableStream(
  {
    start(controller) {
      // …
    },
    pull(controller) {
      // …
    },
    cancel(err) {
      console.log("stream error:", err);
    },
  },
  queueingStrategy,
);

const size = queueingStrategy.size(chunk);
```

## [Specifications](#specifications)

Specification
[Streams# blqs-class](https://streams.spec.whatwg.org/#blqs-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Streams API](/en-US/docs/Web/API/Streams_API)
- [Internal queues and queuing strategies](/en-US/docs/Web/API/Streams_API/Concepts#internal_queues_and_queuing_strategies)
- [ByteLengthQueuingStrategy()](/en-US/docs/Web/API/ByteLengthQueuingStrategy/ByteLengthQueuingStrategy) constructor

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ByteLengthQueuingStrategy/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/bytelengthqueuingstrategy/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FByteLengthQueuingStrategy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbytelengthqueuingstrategy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FByteLengthQueuingStrategy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbytelengthqueuingstrategy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd8b4431bfde42f1bc195239ea1f378d763f8163e%0A*+Document+last+modified%3A+2024-04-22T06%3A16%3A40.000Z%0A%0A%3C%2Fdetails%3E)
