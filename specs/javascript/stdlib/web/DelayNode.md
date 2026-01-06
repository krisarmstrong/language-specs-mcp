# DelayNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDelayNode&level=high)

The `DelayNode` interface represents a [delay-line](https://en.wikipedia.org/wiki/Digital_delay_line); an [AudioNode](/en-US/docs/Web/API/AudioNode) audio-processing module that causes a delay between the arrival of an input data and its propagation to the output.

A `DelayNode` always has exactly one input and one output, both with the same amount of channels.

When creating a graph that has a cycle, it is mandatory to have at least one `DelayNode` in the cycle, or the nodes taking part in the cycle will be muted.

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

[DelayNode()](/en-US/docs/Web/API/DelayNode/DelayNode)

Creates a new instance of a DelayNode object instance. As an alternative, you can use the [BaseAudioContext.createDelay()](/en-US/docs/Web/API/BaseAudioContext/createDelay) factory method; see [Creating an AudioNode](/en-US/docs/Web/API/AudioNode#creating_an_audionode).

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[DelayNode.delayTime](/en-US/docs/Web/API/DelayNode/delayTime)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing the amount of delay to apply, specified in seconds.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Example](#example)

See [BaseAudioContext.createDelay()](/en-US/docs/Web/API/BaseAudioContext/createDelay#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# DelayNode](https://webaudio.github.io/web-audio-api/#DelayNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DelayNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/delaynode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDelayNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdelaynode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDelayNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdelaynode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
