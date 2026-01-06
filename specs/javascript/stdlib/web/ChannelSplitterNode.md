# ChannelSplitterNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannelSplitterNode&level=high)

The `ChannelSplitterNode` interface, often used in conjunction with its opposite, [ChannelMergerNode](/en-US/docs/Web/API/ChannelMergerNode), separates the different channels of an audio source into a set of mono outputs. This is useful for accessing each channel separately, e.g., for performing channel mixing where gain must be separately controlled on each channel.

If your `ChannelSplitterNode` always has one single input, the amount of outputs is defined by a parameter on its constructor and the call to [AudioContext.createChannelSplitter()](/en-US/docs/Web/API/BaseAudioContext/createChannelSplitter). In the case that no value is given, it will default to `6`. If there are fewer channels in the input than there are outputs, supernumerary outputs are silent.

Number of inputs`1`Number of outputsvariable; default to `6`.Channel count mode`"explicit"` Older implementations, as per earlier versions of the spec use `"max"`. Channel count Fixed to the number of outputs. Older implementations, as per earlier versions of the spec use `2` (not used in the default count mode). Channel interpretation`"discrete"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ChannelSplitterNode()](/en-US/docs/Web/API/ChannelSplitterNode/ChannelSplitterNode)

Creates a new `ChannelSplitterNode` object instance.

## [Instance properties](#instance_properties)

No specific property; inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [BaseAudioContext.createChannelSplitter()](/en-US/docs/Web/API/BaseAudioContext/createChannelSplitter#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# ChannelSplitterNode](https://webaudio.github.io/web-audio-api/#ChannelSplitterNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ChannelSplitterNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/channelsplitternode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannelSplitterNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fchannelsplitternode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChannelSplitterNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fchannelsplitternode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
