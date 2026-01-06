# MediaStreamAudioSourceNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamAudioSourceNode&level=high)

The `MediaStreamAudioSourceNode` interface is a type of [AudioNode](/en-US/docs/Web/API/AudioNode) which operates as an audio source whose media is received from a [MediaStream](/en-US/docs/Web/API/MediaStream) obtained using the WebRTC or Media Capture and Streams APIs.

This media could be from a microphone (through [getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)) or from a remote peer on a WebRTC call (using the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)'s audio tracks).

A `MediaStreamAudioSourceNode` has no inputs and exactly one output, and is created using the [AudioContext.createMediaStreamSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamSource) method.

The `MediaStreamAudioSourceNode` takes the audio from the first[MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) whose [kind](/en-US/docs/Web/API/MediaStreamTrack/kind) attribute's value is `audio`. See [Track ordering](#track_ordering) for more information about the order of tracks.

The number of channels output by the node matches the number of tracks found in the selected audio track.

Number of inputs`0`Number of outputs`1`Channel count 2 (but note that [AudioNode.channelCount](/en-US/docs/Web/API/AudioNode/channelCount) is only used for up-mixing and down-mixing [AudioNode](/en-US/docs/Web/API/AudioNode) inputs, and `MediaStreamAudioSourceNode` doesn't have any input) 

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Usage notes](#usage_notes)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaStreamAudioSourceNode()](/en-US/docs/Web/API/MediaStreamAudioSourceNode/MediaStreamAudioSourceNode)

Creates a new `MediaStreamAudioSourceNode` object instance with the specified options.

## [Instance properties](#instance_properties)

In addition to the following properties, `MediaStreamAudioSourceNode` inherits the properties of its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[mediaStream](/en-US/docs/Web/API/MediaStreamAudioSourceNode/mediaStream)Read only

The [MediaStream](/en-US/docs/Web/API/MediaStream) used when constructing this `MediaStreamAudioSourceNode`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Usage notes](#usage_notes)

### [Track ordering](#track_ordering)

For the purposes of the `MediaStreamTrackAudioSourceNode` interface, the order of the audio tracks on the stream is determined by taking the tracks whose [kind](/en-US/docs/Web/API/MediaStreamTrack/kind) is `audio`, then sorting the tracks by their [id](/en-US/docs/Web/API/MediaStreamTrack/id) property's values, in Unicode code point order (essentially, in alphabetical or lexicographical order, for IDs which are simple alphanumeric strings).

The first track, then, is the track whose `id` comes first when the tracks' IDs are all sorted by Unicode code point.

However, it's important to note that the rule establishing this ordering was added long after this interface was first introduced into the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API). As such, you can't easily rely on the order matching between any two browsers or browser versions.

The [MediaStreamTrackAudioSourceNode](/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode) interface is similar to `MediaStreamAudioSourceNode`, but avoids this problem by letting you specify which track you want to use.

## [Example](#example)

See [AudioContext.createMediaStreamSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamSource#examples) for example code that uses this object.

## [Specifications](#specifications)

Specification
[Web Audio API# MediaStreamAudioSourceNode](https://webaudio.github.io/web-audio-api/#MediaStreamAudioSourceNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [Media Capture and Streams API (Media Streams)](/en-US/docs/Web/API/Media_Capture_and_Streams_API)
- [MediaStreamTrackAudioSourceNode](/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamAudioSourceNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamaudiosourcenode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamAudioSourceNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamaudiosourcenode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamAudioSourceNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamaudiosourcenode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F73b2b6ee411ac094b9fc57dafac6f9c232fc20d9%0A*+Document+last+modified%3A+2024-07-26T02%3A14%3A04.000Z%0A%0A%3C%2Fdetails%3E)
