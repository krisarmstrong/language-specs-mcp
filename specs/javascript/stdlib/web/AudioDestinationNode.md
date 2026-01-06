# AudioDestinationNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioDestinationNode&level=high)

The `AudioDestinationNode` interface represents the end destination of an audio graph in a given context — usually the speakers of your device. It can also be the node that will "record" the audio data when used with an `OfflineAudioContext`.

`AudioDestinationNode` has no output (as it is the output, no more `AudioNode` can be linked after it in the audio graph) and one input. The number of channels in the input must be between `0` and the `maxChannelCount` value or an exception is raised.

The `AudioDestinationNode` of a given `AudioContext` can be retrieved using the [AudioContext.destination](/en-US/docs/Web/API/BaseAudioContext/destination) property.

Number of inputs`1`Number of outputs`0`Channel count mode`"explicit"`Channel count`2`Channel interpretation`"speakers"`

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[AudioDestinationNode.maxChannelCount](/en-US/docs/Web/API/AudioDestinationNode/maxChannelCount)

An `unsigned long` defining the maximum number of channels that the physical device can handle.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

There is no complex set up for using an `AudioDestinationNode` — by default, this represents the output of the user's system (e.g., their speakers), so you can get it hooked up inside an audio graph using only a few lines of code:

js

```
const audioCtx = new AudioContext();
const source = audioCtx.createMediaElementSource(myMediaElement);
source.connect(gainNode);
gainNode.connect(audioCtx.destination);
```

To see a more complete implementation, check out one of our MDN Web Audio examples, such as [Voice-change-o-matic](https://mdn.github.io/webaudio-examples/voice-change-o-matic/) or [Violent Theremin](https://github.com/mdn/webaudio-examples/tree/main/violent-theremin).

## [Specifications](#specifications)

Specification
[Web Audio API# AudioDestinationNode](https://webaudio.github.io/web-audio-api/#AudioDestinationNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioDestinationNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiodestinationnode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioDestinationNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiodestinationnode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioDestinationNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiodestinationnode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
