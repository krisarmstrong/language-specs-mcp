# ChannelMergerNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannelMergerNode&level=high)

The `ChannelMergerNode` interface, often used in conjunction with its opposite, [ChannelSplitterNode](/en-US/docs/Web/API/ChannelSplitterNode), reunites different mono inputs into a single output. Each input is used to fill a channel of the output. This is useful for accessing each channels separately, e.g., for performing channel mixing where gain must be separately controlled on each channel.

If `ChannelMergerNode` has one single output, but as many inputs as there are channels to merge; the number of inputs is defined as a parameter of its constructor and the call to [AudioContext.createChannelMerger()](/en-US/docs/Web/API/BaseAudioContext/createChannelMerger). In the case that no value is given, it will default to `6`.

Using a `ChannelMergerNode`, it is possible to create outputs with more channels than the rendering hardware is able to process. In that case, when the signal is sent to the [AudioContext.listener](/en-US/docs/Web/API/BaseAudioContext/listener) object, supernumerary channels will be ignored.

Number of inputsvariable; default to `6`.Number of outputs`1`Channel count mode`"explicit"`Channel count`2` (not used in the default count mode)Channel interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ChannelMergerNode()](/en-US/docs/Web/API/ChannelMergerNode/ChannelMergerNode)

Creates a new `ChannelMergerNode` object instance.

## [Instance properties](#instance_properties)

No specific property; inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [BaseAudioContext.createChannelMerger()](/en-US/docs/Web/API/BaseAudioContext/createChannelMerger#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# ChannelMergerNode](https://webaudio.github.io/web-audio-api/#ChannelMergerNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ChannelMergerNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/channelmergernode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannelMergerNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fchannelmergernode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannelMergerNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fchannelmergernode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
