# AudioParam

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParam&level=high)

The Web Audio API's `AudioParam` interface represents an audio-related parameter, usually a parameter of an [AudioNode](/en-US/docs/Web/API/AudioNode) (such as [GainNode.gain](/en-US/docs/Web/API/GainNode/gain)).

An `AudioParam` can be set to a specific value or a change in value, and can be scheduled to happen at a specific time and following a specific pattern.

Each `AudioParam` has a list of events, initially empty, that define when and how values change. When this list is not empty, changes using the `AudioParam.value` attributes are ignored. This list of events allows us to schedule changes that have to happen at very precise times, using arbitrary timeline-based automation curves. The time used is the one defined in [AudioContext.currentTime](/en-US/docs/Web/API/BaseAudioContext/currentTime).

## In this article

- [AudioParam types](#audioparam_types)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [AudioParam types](#audioparam_types)

There are two `AudioParam` kinds: a-rate and k-rate parameters. Each [AudioNode](/en-US/docs/Web/API/AudioNode) defines which of its parameters are a-rate or k-rate in the spec.

### [a-rate](#a-rate)

An a-rate`AudioParam` takes the current audio parameter value for each [sample frame](/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API#audio_buffers_frames_samples_and_channels) of the audio signal.

### [k-rate](#k-rate)

A k-rate`AudioParam` uses the same initial audio parameter value for the whole block processed; that is, 128 sample frames. In other words, the same value applies to every frame in the audio as it's processed by the node.

## [Instance properties](#instance_properties)

[AudioParam.defaultValue](/en-US/docs/Web/API/AudioParam/defaultValue)Read only

Represents the initial value of the attribute as defined by the specific [AudioNode](/en-US/docs/Web/API/AudioNode) creating the `AudioParam`.

[AudioParam.maxValue](/en-US/docs/Web/API/AudioParam/maxValue)Read only

Represents the maximum possible value for the parameter's nominal (effective) range.

[AudioParam.minValue](/en-US/docs/Web/API/AudioParam/minValue)Read only

Represents the minimum possible value for the parameter's nominal (effective) range.

[AudioParam.value](/en-US/docs/Web/API/AudioParam/value)

Represents the parameter's current value as of the current time; initially set to the value of [defaultValue](/en-US/docs/Web/API/AudioParam/defaultValue).

## [Instance methods](#instance_methods)

[AudioParam.setValueAtTime()](/en-US/docs/Web/API/AudioParam/setValueAtTime)

Schedules an instant change to the value of the `AudioParam` at a precise time, as measured against [AudioContext.currentTime](/en-US/docs/Web/API/BaseAudioContext/currentTime). The new value is given by the `value` parameter.

[AudioParam.linearRampToValueAtTime()](/en-US/docs/Web/API/AudioParam/linearRampToValueAtTime)

Schedules a gradual linear change in the value of the `AudioParam`. The change starts at the time specified for the previous event, follows a linear ramp to the new value given in the `value` parameter, and reaches the new value at the time given in the `endTime` parameter.

[AudioParam.exponentialRampToValueAtTime()](/en-US/docs/Web/API/AudioParam/exponentialRampToValueAtTime)

Schedules a gradual exponential change in the value of the `AudioParam`. The change starts at the time specified for the previous event, follows an exponential ramp to the new value given in the `value` parameter, and reaches the new value at the time given in the `endTime` parameter.

[AudioParam.setTargetAtTime()](/en-US/docs/Web/API/AudioParam/setTargetAtTime)

Schedules the start of a change to the value of the `AudioParam`. The change starts at the time specified in `startTime` and exponentially moves towards the value given by the `target` parameter. The exponential decay rate is defined by the `timeConstant` parameter, which is a time measured in seconds.

[AudioParam.setValueCurveAtTime()](/en-US/docs/Web/API/AudioParam/setValueCurveAtTime)

Schedules the values of the `AudioParam` to follow a set of values, defined by an array of floating-point numbers scaled to fit into the given interval, starting at a given start time and spanning a given duration of time.

[AudioParam.cancelScheduledValues()](/en-US/docs/Web/API/AudioParam/cancelScheduledValues)

Cancels all scheduled future changes to the `AudioParam`.

[AudioParam.cancelAndHoldAtTime()](/en-US/docs/Web/API/AudioParam/cancelAndHoldAtTime)

Cancels all scheduled future changes to the `AudioParam` but holds its value at a given time until further changes are made using other methods.

## [Examples](#examples)

First, a basic example showing a [GainNode](/en-US/docs/Web/API/GainNode) having its `gain` value set. `gain` is an example of an a-rate`AudioParam`, as the value can potentially be set differently for each sample frame of the audio.

js

```
const audioCtx = new AudioContext();

const gainNode = audioCtx.createGain();
gainNode.gain.value = 0;
```

Next, an example showing a [DynamicsCompressorNode](/en-US/docs/Web/API/DynamicsCompressorNode) having some param values manipulated. These are examples of k-rate`AudioParam` types, as the values are set for the entire audio block at once.

js

```
const compressor = audioCtx.createDynamicsCompressor();
compressor.threshold.setValueAtTime(-50, audioCtx.currentTime);
compressor.knee.setValueAtTime(40, audioCtx.currentTime);
compressor.ratio.setValueAtTime(12, audioCtx.currentTime);
compressor.attack.setValueAtTime(0, audioCtx.currentTime);
compressor.release.setValueAtTime(0.25, audioCtx.currentTime);
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioParam](https://webaudio.github.io/web-audio-api/#AudioParam)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 30, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/AudioParam/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioparam/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParam&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioparam%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParam%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioparam%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4adfb71916dac6948dd4aafc8e2bf95f00f1def3%0A*+Document+last+modified%3A+2023-07-30T22%3A24%3A20.000Z%0A%0A%3C%2Fdetails%3E)
