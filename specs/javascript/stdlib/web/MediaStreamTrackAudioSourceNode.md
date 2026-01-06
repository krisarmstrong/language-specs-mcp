# MediaStreamTrackAudioSourceNode

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackAudioSourceNode&level=not)

The `MediaStreamTrackAudioSourceNode` interface is a type of [AudioNode](/en-US/docs/Web/API/AudioNode) which represents a source of audio data taken from a specific [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) obtained through the [WebRTC](/en-US/docs/Web/API/WebRTC_API) or [Media Capture and Streams](/en-US/docs/Web/API/Media_Capture_and_Streams_API) APIs.

The audio itself might be input from a microphone or other audio sampling device, or might be received through a [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), among other possible options.

A `MediaStreamTrackAudioSourceNode` has no inputs and exactly one output, and is created using the [AudioContext.createMediaStreamTrackSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamTrackSource) method. This interface is similar to [MediaStreamAudioSourceNode](/en-US/docs/Web/API/MediaStreamAudioSourceNode), except it lets you specifically state the track to use, rather than assuming the first audio track on a stream.

Number of inputs`0`Number of outputs`1`Channel count defined by the first audio [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) passed to the [AudioContext.createMediaStreamTrackSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamTrackSource) method that created it. 

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaStreamTrackAudioSourceNode()](/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode/MediaStreamTrackAudioSourceNode)

Creates a new `MediaStreamTrackAudioSourceNode` object instance with the specified options.

## [Instance properties](#instance_properties)

The `MediaStreamTrackAudioSourceNode` interface has no properties of its own; however, it inherits the properties of its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [AudioContext.createMediaStreamSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamSource#examples) for example code that uses this object.

## [Specifications](#specifications)

Specification
[Web Audio API# MediaStreamTrackAudioSourceNode](https://webaudio.github.io/web-audio-api/#MediaStreamTrackAudioSourceNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [Media Capture and Streams API (Media Streams)](/en-US/docs/Web/API/Media_Capture_and_Streams_API)
- [MediaStreamAudioSourceNode](/en-US/docs/Web/API/MediaStreamAudioSourceNode)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamtrackaudiosourcenode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackAudioSourceNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamtrackaudiosourcenode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackAudioSourceNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamtrackaudiosourcenode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F73b2b6ee411ac094b9fc57dafac6f9c232fc20d9%0A*+Document+last+modified%3A+2024-07-26T02%3A14%3A04.000Z%0A%0A%3C%2Fdetails%3E)
