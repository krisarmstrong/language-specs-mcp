# BiquadFilterNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBiquadFilterNode&level=high)

The `BiquadFilterNode` interface represents a simple low-order filter, and is created using the [BaseAudioContext/createBiquadFilter](/en-US/docs/Web/API/BaseAudioContext/createBiquadFilter) method. It is an [AudioNode](/en-US/docs/Web/API/AudioNode) that can represent different kinds of filters, tone control devices, and graphic equalizers. A `BiquadFilterNode` always has exactly one input and one output.

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

[BiquadFilterNode()](/en-US/docs/Web/API/BiquadFilterNode/BiquadFilterNode)

Creates a new instance of a `BiquadFilterNode` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

Note: Though the `AudioParam` objects returned are read-only, the values they represent are not.

[BiquadFilterNode.frequency](/en-US/docs/Web/API/BiquadFilterNode/frequency)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam), a double representing a frequency in the current filtering algorithm measured in hertz (Hz).

[BiquadFilterNode.detune](/en-US/docs/Web/API/BiquadFilterNode/detune)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing detuning of the frequency in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29).

[BiquadFilterNode.Q](/en-US/docs/Web/API/BiquadFilterNode/Q)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam), a double representing a [Q factor](https://en.wikipedia.org/wiki/Q_factor), or quality factor.

[BiquadFilterNode.gain](/en-US/docs/Web/API/BiquadFilterNode/gain)Read only

An [a-rate](/en-US/docs/Web/API/AudioParam#a-rate)[AudioParam](/en-US/docs/Web/API/AudioParam), a double representing the [gain](https://en.wikipedia.org/wiki/Gain) used in the current filtering algorithm.

[BiquadFilterNode.type](/en-US/docs/Web/API/BiquadFilterNode/type)

A string value defining the kind of filtering algorithm the node is implementing.

 The meaning of the different parameters depending on the type of the filter (detune has the same meaning regardless, so isn't listed below) `type`Description`frequency``Q``gain``lowpass` Standard second-order resonant lowpass filter with 12dB/octave rolloff. Frequencies below the cutoff pass through; frequencies above it are attenuated. The cutoff frequency. Indicates how peaked the frequency is around the cutoff. The greater the value is, the greater is the peak. Not used`highpass` Standard second-order resonant highpass filter with 12dB/octave rolloff. Frequencies below the cutoff are attenuated; frequencies above it pass through. The cutoff frequency. Indicates how peaked the frequency is around the cutoff. The greater the value, the greater the peak. Not used`bandpass` Standard second-order bandpass filter. Frequencies outside the given range of frequencies are attenuated; the frequencies inside it pass through. The center of the range of frequencies. Controls the width of the frequency band. The greater the `Q` value, the smaller the frequency band. Not used`lowshelf` Standard second-order lowshelf filter. Frequencies lower than the frequency get a boost, or an attenuation; frequencies over it are unchanged.  The upper limit of the frequencies getting a boost or an attenuation. Not used The boost, in dB, to be applied; if negative, it will be an attenuation. `highshelf` Standard second-order highshelf filter. Frequencies higher than the frequency get a boost or an attenuation; frequencies lower than it are unchanged.  The lower limit of the frequencies getting a boost or an attenuation. Not used The boost, in dB, to be applied; if negative, it will be an attenuation. `peaking` Frequencies inside the range get a boost or an attenuation; frequencies outside it are unchanged.  The middle of the frequency range getting a boost or an attenuation.  Controls the width of the frequency band. The greater the `Q` value, the smaller the frequency band.  The boost, in dB, to be applied; if negative, it will be an attenuation. `notch` Standard [notch](https://en.wikipedia.org/wiki/Band-stop_filter) filter, also called a band-stop or band-rejection filter. It is the opposite of a bandpass filter: frequencies outside the give range of frequencies pass through; frequencies inside it are attenuated. The center of the range of frequencies. Controls the width of the frequency band. The greater the `Q` value, the smaller the frequency band. Not used`allpass` Standard second-order [allpass](https://en.wikipedia.org/wiki/All-pass_filter#Digital_Implementation) filter. It lets all frequencies through, but changes the phase-relationship between the various frequencies.  The frequency with the maximal [group delay](https://en.wikipedia.org/wiki/Group_delay_and_phase_delay), that is, the frequency where the center of the phase transition occurs.  Controls how sharp the transition is at the medium frequency. The larger this parameter is, the sharper and larger the transition will be. Not used

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[BiquadFilterNode.getFrequencyResponse()](/en-US/docs/Web/API/BiquadFilterNode/getFrequencyResponse)

From the current filter parameter settings this method calculates the frequency response for frequencies specified in the provided array of frequencies.

## [Example](#example)

See [AudioContext.createBiquadFilter](/en-US/docs/Web/API/BaseAudioContext/createBiquadFilter#examples) for example code that shows how to use an `AudioContext` to create a Biquad filter node.

## [Specifications](#specifications)

Specification
[Web Audio API# BiquadFilterNode](https://webaudio.github.io/web-audio-api/#BiquadFilterNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/BiquadFilterNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/biquadfilternode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBiquadFilterNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbiquadfilternode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBiquadFilterNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbiquadfilternode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
