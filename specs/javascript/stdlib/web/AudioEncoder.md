# AudioEncoder

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioEncoder&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `AudioEncoder` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) encodes [AudioData](/en-US/docs/Web/API/AudioData) objects.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[AudioEncoder()](/en-US/docs/Web/API/AudioEncoder/AudioEncoder)

Creates a new `AudioEncoder` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AudioEncoder.encodeQueueSize](/en-US/docs/Web/API/AudioEncoder/encodeQueueSize)Read only

An integer representing the number of encode queue requests.

[AudioEncoder.state](/en-US/docs/Web/API/AudioEncoder/state)Read only

Represents the state of the underlying codec and whether it is configured for encoding.

### [Events](#events)

[dequeue](/en-US/docs/Web/API/AudioEncoder/dequeue_event)

Fires to signal a decrease in [AudioEncoder.encodeQueueSize](/en-US/docs/Web/API/AudioEncoder/encodeQueueSize).

## [Static methods](#static_methods)

[AudioEncoder.isConfigSupported()](/en-US/docs/Web/API/AudioEncoder/isConfigSupported_static)

Returns a promise indicating whether the provided `AudioEncoderConfig` is supported.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[AudioEncoder.configure()](/en-US/docs/Web/API/AudioEncoder/configure)

Enqueues a control message to configure the audio encoder for encoding chunks.

[AudioEncoder.encode()](/en-US/docs/Web/API/AudioEncoder/encode)

Enqueues a control message to encode a given [AudioData](/en-US/docs/Web/API/AudioData) objects.

[AudioEncoder.flush()](/en-US/docs/Web/API/AudioEncoder/flush)

Returns a promise that resolves once all pending messages in the queue have been completed.

[AudioEncoder.reset()](/en-US/docs/Web/API/AudioEncoder/reset)

Resets all states including configuration, control messages in the control message queue, and all pending callbacks.

[AudioEncoder.close()](/en-US/docs/Web/API/AudioEncoder/close)

Ends all pending work and releases system resources.

## [Specifications](#specifications)

Specification
[WebCodecs# audioencoder-interface](https://w3c.github.io/webcodecs/#audioencoder-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 11, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AudioEncoder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioencoder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioEncoder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioencoder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioEncoder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioencoder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06b418a190b8e4a46682ab706d14984e7db34862%0A*+Document+last+modified%3A+2024-09-11T03%3A36%3A25.000Z%0A%0A%3C%2Fdetails%3E)
