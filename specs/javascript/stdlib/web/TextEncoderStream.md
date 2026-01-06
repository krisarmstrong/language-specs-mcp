# TextEncoderStream

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2022⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextEncoderStream&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TextEncoderStream` interface of the [Encoding API](/en-US/docs/Web/API/Encoding_API) converts a stream of strings into bytes in the UTF-8 encoding. It is the streaming equivalent of [TextEncoder](/en-US/docs/Web/API/TextEncoder). It implements the same shape as a [TransformStream](/en-US/docs/Web/API/TransformStream), allowing it to be used in [ReadableStream.pipeThrough()](/en-US/docs/Web/API/ReadableStream/pipeThrough) and similar methods.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TextEncoderStream()](/en-US/docs/Web/API/TextEncoderStream/TextEncoderStream)

Creates a new `TextEncoderStream` object.

## [Instance properties](#instance_properties)

[TextEncoderStream.encoding](/en-US/docs/Web/API/TextEncoderStream/encoding)Read only

Always returns `"utf-8"`.

[TextEncoderStream.readable](/en-US/docs/Web/API/TextEncoderStream/readable)Read only

Returns the [ReadableStream](/en-US/docs/Web/API/ReadableStream) instance controlled by this object.

[TextEncoderStream.writable](/en-US/docs/Web/API/TextEncoderStream/writable)Read only

Returns the [WritableStream](/en-US/docs/Web/API/WritableStream) instance controlled by this object.

## [Examples](#examples)

[Examples of streaming structured data and HTML](https://streams.spec.whatwg.org/demos/)

## [Specifications](#specifications)

Specification
[Encoding# interface-textencoderstream](https://encoding.spec.whatwg.org/#interface-textencoderstream)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [TextDecoderStream](/en-US/docs/Web/API/TextDecoderStream)
- [TextEncoder](/en-US/docs/Web/API/TextEncoder)
- [TransformStream](/en-US/docs/Web/API/TransformStream)
- [Streams API Concepts](/en-US/docs/Web/API/Streams_API/Concepts)
- [Experimenting with the Streams API](https://deanhume.com/experimenting-with-the-streams-api/)
- [Streaming requests with the fetch API](https://developer.chrome.com/docs/capabilities/web-apis/fetch-streaming-requests), developer.chrome.com (2020)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TextEncoderStream/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textencoderstream/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextEncoderStream&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextencoderstream%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextEncoderStream%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextencoderstream%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fae6626ec9a5729a51f202b77586f37958088ed77%0A*+Document+last+modified%3A+2025-11-26T01%3A57%3A30.000Z%0A%0A%3C%2Fdetails%3E)
