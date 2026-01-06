# DynamicsCompressorNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDynamicsCompressorNode&level=high)

The `DynamicsCompressorNode` interface provides a compression effect, which lowers the volume of the loudest parts of the signal in order to help prevent clipping and distortion that can occur when multiple sounds are played and multiplexed together at once. This is often used in musical production and game audio. `DynamicsCompressorNode` is an [AudioNode](/en-US/docs/Web/API/AudioNode) that has exactly one input and one output.

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

[DynamicsCompressorNode()](/en-US/docs/Web/API/DynamicsCompressorNode/DynamicsCompressorNode)

Creates a new instance of a `DynamicsCompressorNode` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[DynamicsCompressorNode.threshold](/en-US/docs/Web/API/DynamicsCompressorNode/threshold)Read only

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the decibel value above which the compression will start taking effect.

[DynamicsCompressorNode.knee](/en-US/docs/Web/API/DynamicsCompressorNode/knee)Read only

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) containing a decibel value representing the range above the threshold where the curve smoothly transitions to the compressed portion.

[DynamicsCompressorNode.ratio](/en-US/docs/Web/API/DynamicsCompressorNode/ratio)Read only

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the amount of change, in dB, needed in the input for a 1 dB change in the output.

[DynamicsCompressorNode.reduction](/en-US/docs/Web/API/DynamicsCompressorNode/reduction)Read only

A `float` representing the amount of gain reduction currently applied by the compressor to the signal.

[DynamicsCompressorNode.attack](/en-US/docs/Web/API/DynamicsCompressorNode/attack)Read only

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the amount of time, in seconds, required to reduce the gain by 10 dB.

[DynamicsCompressorNode.release](/en-US/docs/Web/API/DynamicsCompressorNode/release)Read only

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the amount of time, in seconds, required to increase the gain by 10 dB.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [BaseAudioContext.createDynamicsCompressor()](/en-US/docs/Web/API/BaseAudioContext/createDynamicsCompressor#examples) example code.

## [Specifications](#specifications)

Specification
[Web Audio API# DynamicsCompressorNode](https://webaudio.github.io/web-audio-api/#DynamicsCompressorNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DynamicsCompressorNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dynamicscompressornode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDynamicsCompressorNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdynamicscompressornode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDynamicsCompressorNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdynamicscompressornode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
