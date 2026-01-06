# VideoEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoEncoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `VideoEncoder` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) encodes [VideoFrame](/en-US/docs/Web/API/VideoFrame) objects into [EncodedVideoChunk](/en-US/docs/Web/API/EncodedVideoChunk)s.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[VideoEncoder()](/en-US/docs/Web/API/VideoEncoder/VideoEncoder)

Creates a new `VideoEncoder` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VideoEncoder.encodeQueueSize](/en-US/docs/Web/API/VideoEncoder/encodeQueueSize)Read only

An integer representing the number of encode queue requests.

[VideoEncoder.state](/en-US/docs/Web/API/VideoEncoder/state)Read only

Represents the state of the underlying codec and whether it is configured for encoding.

### [Events](#events)

[dequeue](/en-US/docs/Web/API/VideoEncoder/dequeue_event)

Fires to signal a decrease in [VideoEncoder.encodeQueueSize](/en-US/docs/Web/API/VideoEncoder/encodeQueueSize).

## [Static methods](#static_methods)

[VideoEncoder.isConfigSupported()](/en-US/docs/Web/API/VideoEncoder/isConfigSupported_static)

Returns a promise indicating whether the provided `VideoEncoderConfig` is supported.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VideoEncoder.configure()](/en-US/docs/Web/API/VideoEncoder/configure)

Asynchronously prepares the encoder to accept video frames for encoding with the specified parameters.

[VideoEncoder.encode()](/en-US/docs/Web/API/VideoEncoder/encode)

Asynchronously encodes a [VideoFrame](/en-US/docs/Web/API/VideoFrame).

[VideoEncoder.flush()](/en-US/docs/Web/API/VideoEncoder/flush)

Returns a promise that resolves once all pending encodes have been completed.

[VideoEncoder.reset()](/en-US/docs/Web/API/VideoEncoder/reset)

Cancels all pending encodes and callbacks.

[VideoEncoder.close()](/en-US/docs/Web/API/VideoEncoder/close)

Ends all pending work and releases system resources.

## [Specifications](#specifications)

Specification
[WebCodecs# videoencoder-interface](https://w3c.github.io/webcodecs/#videoencoder-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

[Video processing with WebCodecs](https://developer.chrome.com/docs/web-platform/best-practices/webcodecs)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/VideoEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videoencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideoencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideoencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3789de65bd11453c4cb24625723f81a7e8fcdd56%0A*+Document+last+modified%3A+2024-05-08T04%3A36%3A35.000Z%0A%0A%3C%2Fdetails%3E)
