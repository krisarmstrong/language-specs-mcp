# VideoDecoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoDecoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `VideoDecoder` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) decodes chunks of video.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[VideoDecoder()](/en-US/docs/Web/API/VideoDecoder/VideoDecoder)

Creates a new `VideoDecoder` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VideoDecoder.decodeQueueSize](/en-US/docs/Web/API/VideoDecoder/decodeQueueSize)Read only

An integer representing the number of queued decode requests.

[VideoDecoder.state](/en-US/docs/Web/API/VideoDecoder/state)Read only

Indicates the current state of decoder. Possible values are:

- `"unconfigured"`
- `"configured"`
- `"closed"`

### [Events](#events)

[dequeue](/en-US/docs/Web/API/VideoDecoder/dequeue_event)

Fires to signal a decrease in [VideoDecoder.decodeQueueSize](/en-US/docs/Web/API/VideoDecoder/decodeQueueSize).

## [Static methods](#static_methods)

[VideoDecoder.isConfigSupported()](/en-US/docs/Web/API/VideoDecoder/isConfigSupported_static)

Returns a promise indicating whether the provided `VideoDecoderConfig` is supported.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VideoDecoder.configure()](/en-US/docs/Web/API/VideoDecoder/configure)

Enqueues a control message to configure the video decoder for decoding chunks.

[VideoDecoder.decode()](/en-US/docs/Web/API/VideoDecoder/decode)

Enqueues a control message to decode a given chunk of video.

[VideoDecoder.flush()](/en-US/docs/Web/API/VideoDecoder/flush)

Returns a promise that resolves once all pending messages in the queue have been completed.

[VideoDecoder.reset()](/en-US/docs/Web/API/VideoDecoder/reset)

Resets all states including configuration, control messages in the control message queue, and all pending callbacks.

[VideoDecoder.close()](/en-US/docs/Web/API/VideoDecoder/close)

Ends all pending work and releases system resources.

## [Specifications](#specifications)

Specification
[WebCodecs# videodecoder-interface](https://w3c.github.io/webcodecs/#videodecoder-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Video processing with WebCodecs](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs)
- [WebCodecs API Samples](https://w3c.github.io/webcodecs/samples/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VideoDecoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videodecoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoDecoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideodecoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoDecoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideodecoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3789de65bd11453c4cb24625723f81a7e8fcdd56%0A*+Document+last+modified%3A+2024-05-08T04%3A36%3A35.000Z%0A%0A%3C%2Fdetails%3E)
