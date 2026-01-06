# StereoPannerNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStereoPannerNode&level=high)

The `StereoPannerNode` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents a simple stereo panner node that can be used to pan an audio stream left or right. It is an [AudioNode](/en-US/docs/Web/API/AudioNode) audio-processing module that positions an incoming audio stream in a stereo image using a low-cost equal-power [panning algorithm](https://webaudio.github.io/web-audio-api/#panning-algorithm).

The [pan](/en-US/docs/Web/API/StereoPannerNode/pan) property takes a unitless value between `-1` (full left pan) and `1` (full right pan). This interface was introduced as a much simpler way to apply a simple panning effect than having to use a full [PannerNode](/en-US/docs/Web/API/PannerNode).

Number of inputs`1`Number of outputs`1`Channel count mode`"clamped-max"`Channel count`2`Channel interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[StereoPannerNode()](/en-US/docs/Web/API/StereoPannerNode/StereoPannerNode)

Creates a new instance of a `StereoPannerNode` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[StereoPannerNode.pan](/en-US/docs/Web/API/StereoPannerNode/pan)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the amount of panning to apply.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [BaseAudioContext.createStereoPanner()](/en-US/docs/Web/API/BaseAudioContext/createStereoPanner#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# stereopannernode](https://webaudio.github.io/web-audio-api/#stereopannernode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 6, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/StereoPannerNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/stereopannernode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStereoPannerNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fstereopannernode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStereoPannerNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fstereopannernode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffa1301aead2cee37516b7ad5a5ec2fb21e004227%0A*+Document+last+modified%3A+2023-04-06T05%3A00%3A32.000Z%0A%0A%3C%2Fdetails%3E)
