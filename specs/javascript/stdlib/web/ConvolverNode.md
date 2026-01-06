# ConvolverNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConvolverNode&level=high)

The `ConvolverNode` interface is an [AudioNode](/en-US/docs/Web/API/AudioNode) that performs a Linear Convolution on a given [AudioBuffer](/en-US/docs/Web/API/AudioBuffer), often used to achieve a reverb effect. A `ConvolverNode` always has exactly one input and one output.

Note: For more information on the theory behind Linear Convolution, see the [Convolution article on Wikipedia](https://en.wikipedia.org/wiki/Convolution).

Number of inputs`1`Number of outputs`1`Channel count mode`"clamped-max"`Channel count`1`, `2`, or `4`Channel interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ConvolverNode()](/en-US/docs/Web/API/ConvolverNode/ConvolverNode)

Creates a new `ConvolverNode` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[ConvolverNode.buffer](/en-US/docs/Web/API/ConvolverNode/buffer)

A mono, stereo, or 4-channel [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) containing the (possibly multichannel) impulse response used by the `ConvolverNode` to create the reverb effect.

[ConvolverNode.normalize](/en-US/docs/Web/API/ConvolverNode/normalize)

A boolean that controls whether the impulse response from the buffer will be scaled by an equal-power normalization when the `buffer` attribute is set, or not.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Examples](#examples)

The following example shows basic usage of an AudioContext to create a convolver node. You will need to find an impulse response to complete the example below. See our [HolySpaceCow](https://mdn.github.io/webaudio-examples/holy-space-cow/) example for a complete, applied example.

js

```
let audioCtx = new window.AudioContext();

async function createReverb() {
  let convolver = audioCtx.createConvolver();

  // load impulse response from file
  let response = await fetch("path/to/impulse-response.wav");
  let arraybuffer = await response.arrayBuffer();
  convolver.buffer = await audioCtx.decodeAudioData(arraybuffer);

  return convolver;
}

// …

let reverb = await createReverb();

// someOtherAudioNode -> reverb -> destination
someOtherAudioNode.connect(reverb);
reverb.connect(audioCtx.destination);
```

## [Specifications](#specifications)

Specification
[Web Audio API# ConvolverNode](https://webaudio.github.io/web-audio-api/#ConvolverNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ConvolverNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/convolvernode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConvolverNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fconvolvernode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConvolverNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fconvolvernode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F90e5b796c5741c209aaa674e9ff86d4d7c8e0427%0A*+Document+last+modified%3A+2025-07-28T17%3A57%3A39.000Z%0A%0A%3C%2Fdetails%3E)
