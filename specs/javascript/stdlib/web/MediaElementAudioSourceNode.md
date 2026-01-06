# MediaElementAudioSourceNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaElementAudioSourceNode&level=high)

The `MediaElementAudioSourceNode` interface represents an audio source consisting of an HTML [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) or [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element. It is an [AudioNode](/en-US/docs/Web/API/AudioNode) that acts as an audio source.

A `MediaElementAudioSourceNode` has no inputs and exactly one output, and is created using the [AudioContext.createMediaElementSource()](/en-US/docs/Web/API/AudioContext/createMediaElementSource) method. The number of channels in the output equals the number of channels of the audio referenced by the [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) used in the creation of the node, or is 1 if the [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) has no audio.

Number of inputs`0`Number of outputs`1`Channel count 2 (but note that [AudioNode.channelCount](/en-US/docs/Web/API/AudioNode/channelCount) is only used for up-mixing and down-mixing [AudioNode](/en-US/docs/Web/API/AudioNode) inputs, and `MediaElementAudioSourceNode` doesn't have any input) 

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaElementAudioSourceNode()](/en-US/docs/Web/API/MediaElementAudioSourceNode/MediaElementAudioSourceNode)

Creates a new `MediaElementAudioSourceNode` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[mediaElement](/en-US/docs/Web/API/MediaElementAudioSourceNode/mediaElement)Read only

The [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) used when constructing this `MediaStreamAudioSourceNode`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [AudioContext.createMediaElementSource()](/en-US/docs/Web/API/AudioContext/createMediaElementSource#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# MediaElementAudioSourceNode](https://webaudio.github.io/web-audio-api/#MediaElementAudioSourceNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaElementAudioSourceNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediaelementaudiosourcenode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaElementAudioSourceNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediaelementaudiosourcenode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaElementAudioSourceNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediaelementaudiosourcenode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
