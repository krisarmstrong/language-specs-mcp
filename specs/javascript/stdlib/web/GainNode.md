# GainNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGainNode&level=high)

The `GainNode` interface represents a change in volume. It is an [AudioNode](/en-US/docs/Web/API/AudioNode) audio-processing module that causes a given gain to be applied to the input data before its propagation to the output. A `GainNode` always has exactly one input and one output, both with the same number of channels.

The gain is a unitless value, changing with time, that is multiplied to each corresponding sample of all input channels. If modified, the new gain is instantly applied, causing unaesthetic 'clicks' in the resulting audio. To prevent this from happening, never change the value directly but use the exponential interpolation methods on the [AudioParam](/en-US/docs/Web/API/AudioParam) interface.

Number of inputs`1`Number of outputs`1`Channel count mode`"max"`Channel count`2` (not used in the default count mode)Channel interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[GainNode()](/en-US/docs/Web/API/GainNode/GainNode)

Creates and returns a new `GainNode` object. As an alternative, you can use the [BaseAudioContext.createGain()](/en-US/docs/Web/API/BaseAudioContext/createGain) factory method; see [Creating an AudioNode](/en-US/docs/Web/API/AudioNode#creating_an_audionode).

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[GainNode.gain](/en-US/docs/Web/API/GainNode/gain)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the amount of gain to apply. You have to set [AudioParam.value](/en-US/docs/Web/API/AudioParam/value) or use the methods of `AudioParam` to change the effect of gain.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [BaseAudioContext.createGain()](/en-US/docs/Web/API/BaseAudioContext/createGain#examples) for example code showing how to use an `AudioContext` to create a `GainNode`.

## [Specifications](#specifications)

Specification
[Web Audio API# GainNode](https://webaudio.github.io/web-audio-api/#GainNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 6, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/GainNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gainnode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGainNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgainnode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGainNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgainnode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffa1301aead2cee37516b7ad5a5ec2fb21e004227%0A*+Document+last+modified%3A+2023-04-06T05%3A00%3A32.000Z%0A%0A%3C%2Fdetails%3E)
