# AudioDecoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioDecoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `AudioDecoder` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) decodes chunks of audio.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[AudioDecoder()](/en-US/docs/Web/API/AudioDecoder/AudioDecoder)

Creates a new `AudioDecoder` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AudioDecoder.decodeQueueSize](/en-US/docs/Web/API/AudioDecoder/decodeQueueSize)Read only

An integer representing the number of decode queue requests.

[AudioDecoder.state](/en-US/docs/Web/API/AudioDecoder/state)Read only

Represents the state of the underlying codec and whether it is configured for decoding.

### [Events](#events)

[dequeue](/en-US/docs/Web/API/AudioDecoder/dequeue_event)

Fires to signal a decrease in [AudioDecoder.decodeQueueSize](/en-US/docs/Web/API/AudioDecoder/decodeQueueSize).

## [Static methods](#static_methods)

[AudioDecoder.isConfigSupported()](/en-US/docs/Web/API/AudioDecoder/isConfigSupported_static)

Returns a promise indicating whether the provided `AudioDecoderConfig` is supported.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AudioDecoder.configure()](/en-US/docs/Web/API/AudioDecoder/configure)

Enqueues a control message to configure the audio decoder for decoding chunks.

[AudioDecoder.decode()](/en-US/docs/Web/API/AudioDecoder/decode)

Enqueues a control message to decode a given chunk of audio.

[AudioDecoder.flush()](/en-US/docs/Web/API/AudioDecoder/flush)

Returns a promise that resolves once all pending messages in the queue have been completed.

[AudioDecoder.reset()](/en-US/docs/Web/API/AudioDecoder/reset)

Resets all states including configuration, control messages in the control message queue, and all pending callbacks.

[AudioDecoder.close()](/en-US/docs/Web/API/AudioDecoder/close)

Ends all pending work and releases system resources.

## [Specifications](#specifications)

Specification
[WebCodecs# audiodecoder-interface](https://w3c.github.io/webcodecs/#audiodecoder-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AudioDecoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiodecoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioDecoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiodecoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioDecoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiodecoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06b418a190b8e4a46682ab706d14984e7db34862%0A*+Document+last+modified%3A+2024-09-11T03%3A36%3A25.000Z%0A%0A%3C%2Fdetails%3E)
