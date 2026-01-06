# MediaStreamAudioDestinationNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨October 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamAudioDestinationNode&level=high)

The `MediaStreamAudioDestinationNode` interface represents an audio destination consisting of a [WebRTC](/en-US/docs/Web/API/WebRTC_API)[MediaStream](/en-US/docs/Web/API/MediaStream) with a single `AudioMediaStreamTrack`, which can be used in a similar way to a `MediaStream` obtained from [navigator.mediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia).

It is an [AudioNode](/en-US/docs/Web/API/AudioNode) that acts as an audio destination, created using the [AudioContext.createMediaStreamDestination()](/en-US/docs/Web/API/AudioContext/createMediaStreamDestination) method.

Number of inputs`1`Number of outputs`0`Channel count`2`Channel count mode`"explicit"`Channel count interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaStreamAudioDestinationNode()](/en-US/docs/Web/API/MediaStreamAudioDestinationNode/MediaStreamAudioDestinationNode)

Creates a new `MediaStreamAudioDestinationNode` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[MediaStreamAudioDestinationNode.stream](/en-US/docs/Web/API/MediaStreamAudioDestinationNode/stream)

A [MediaStream](/en-US/docs/Web/API/MediaStream) containing a single [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) whose [kind](/en-US/docs/Web/API/MediaStreamTrack/kind) is `audio` and with the same number of channels as the node. You can use this property to get a stream out of the audio graph and feed it into another construct, such as a [Media Recorder](/en-US/docs/Web/API/MediaStream_Recording_API).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [AudioContext.createMediaStreamDestination()](/en-US/docs/Web/API/AudioContext/createMediaStreamDestination#examples) for example code that creates a `MediaStreamAudioDestinationNode` and uses it as a source for audio to be recorded.

## [Specifications](#specifications)

Specification
[Web Audio API# MediaStreamAudioDestinationNode](https://webaudio.github.io/web-audio-api/#MediaStreamAudioDestinationNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamAudioDestinationNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamaudiodestinationnode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamAudioDestinationNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamaudiodestinationnode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamAudioDestinationNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamaudiodestinationnode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a91b0b63f0cbaca9125bd48d4e5bc8afed2a7a3%0A*+Document+last+modified%3A+2024-03-07T17%3A23%3A45.000Z%0A%0A%3C%2Fdetails%3E)
