# IIRFilterNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIIRFilterNode&level=high)

The `IIRFilterNode` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) is an [AudioNode](/en-US/docs/Web/API/AudioNode) processor which implements a general [infinite impulse response](https://en.wikipedia.org/wiki/Infinite_impulse_response) (IIR) filter; this type of filter can be used to implement tone control devices and graphic equalizers as well. It lets the parameters of the filter response be specified, so that it can be tuned as needed.

Number of inputs`1`Number of outputs`1`Channel count mode`"max"`Channel countSame as on the inputChannel interpretation`"speakers"`

Typically, it's best to use the [BiquadFilterNode](/en-US/docs/Web/API/BiquadFilterNode) interface to implement higher-order filters. There are several reasons why:

- Biquad filters are typically less sensitive to numeric quirks.
- The filter parameters of biquad filters can be automated.
- All even-ordered IIR filters can be created using [BiquadFilterNode](/en-US/docs/Web/API/BiquadFilterNode).

However, if you need to create an odd-ordered IIR filter, you'll need to use `IIRFilterNode`. You may also find this interface useful if you don't need automation, or for other reasons.

Note: Once the node has been created, you can't change its coefficients.

`IIRFilterNode`s have a tail-time reference; they continue to output non-silent audio with zero input. As an IIR filter, the non-zero input continues forever, but this can be limited after some finite time in practice, when the output has approached zero closely enough. The actual time that takes depends on the filter coefficients provided.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[IIRFilterNode()](/en-US/docs/Web/API/IIRFilterNode/IIRFilterNode)

Creates a new instance of an IIRFilterNode object.

## [Instance properties](#instance_properties)

This interface has no properties of its own; however, it inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode). It also has the following additional methods:

[getFrequencyResponse()](/en-US/docs/Web/API/IIRFilterNode/getFrequencyResponse)

Uses the filter's current parameter settings to calculate the response for frequencies specified in the provided array of frequencies.

## [Examples](#examples)

You can find a [simple IIR filter demo live](https://mdn.github.io/webaudio-examples/iirfilter-node/). Also see the [source code on GitHub](https://github.com/mdn/webaudio-examples/tree/main/iirfilter-node). It includes some different coefficient values for different lowpass frequencies — you can change the value of the `filterNumber` constant to a value between 0 and 3 to check out the different available effects.

Also see our [Using IIR filters](/en-US/docs/Web/API/Web_Audio_API/Using_IIR_filters) guide for a full explanation.

## [Specifications](#specifications)

Specification
[Web Audio API# IIRFilterNode](https://webaudio.github.io/web-audio-api/#IIRFilterNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [AudioNode](/en-US/docs/Web/API/AudioNode)
- [BiquadFilterNode](/en-US/docs/Web/API/BiquadFilterNode)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/IIRFilterNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/iirfilternode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIIRFilterNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fiirfilternode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIIRFilterNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fiirfilternode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
