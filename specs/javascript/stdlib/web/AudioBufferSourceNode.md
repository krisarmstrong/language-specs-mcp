# AudioBufferSourceNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioBufferSourceNode&level=high)

The `AudioBufferSourceNode` interface is an [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode) which represents an audio source consisting of in-memory audio data, stored in an [AudioBuffer](/en-US/docs/Web/API/AudioBuffer).

This interface is especially useful for playing back audio which has particularly stringent timing accuracy requirements, such as for sounds that must match a specific rhythm and can be kept in memory rather than being played from disk or the network. To play sounds which require accurate timing but must be streamed from the network or played from disk, use an [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) to implement its playback.

An `AudioBufferSourceNode` has no inputs and exactly one output, which has the same number of channels as the `AudioBuffer` indicated by its [buffer](/en-US/docs/Web/API/AudioBufferSourceNode/buffer) property. If there's no buffer set—that is, if `buffer` is `null`—the output contains a single channel of silence (every sample is 0).

An `AudioBufferSourceNode` can only be played once; after each call to [start()](/en-US/docs/Web/API/AudioBufferSourceNode/start), you have to create a new node if you want to play the same sound again. Fortunately, these nodes are very inexpensive to create, and the actual `AudioBuffer`s can be reused for multiple plays of the sound. Indeed, you can use these nodes in a "fire and forget" manner: create the node, call `start()` to begin playing the sound, and don't even bother to hold a reference to it. It will automatically be garbage-collected at an appropriate time, which won't be until sometime after the sound has finished playing.

Multiple calls to [stop()](/en-US/docs/Web/API/AudioScheduledSourceNode/stop) are allowed. The most recent call replaces the previous one, if the `AudioBufferSourceNode` has not already reached the end of the buffer.

Number of inputs`0`Number of outputs`1`Channel countdefined by the associated [AudioBuffer](/en-US/docs/Web/API/AudioBuffer)

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AudioBufferSourceNode()](/en-US/docs/Web/API/AudioBufferSourceNode/AudioBufferSourceNode)

Creates and returns a new `AudioBufferSourceNode` object. As an alternative, you can use the [BaseAudioContext.createBufferSource()](/en-US/docs/Web/API/BaseAudioContext/createBufferSource) factory method; see [Creating an AudioNode](/en-US/docs/Web/API/AudioNode#creating_an_audionode).

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode).

[AudioBufferSourceNode.buffer](/en-US/docs/Web/API/AudioBufferSourceNode/buffer)

An [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) that defines the audio asset to be played, or when set to the value `null`, defines a single channel of silence (in which every sample is 0.0).

[AudioBufferSourceNode.detune](/en-US/docs/Web/API/AudioBufferSourceNode/detune)

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) representing detuning of playback in [cents](https://en.wikipedia.org/wiki/Cent_%28music%29). This value is compounded with `playbackRate` to determine the speed at which the sound is played. Its default value is `0` (meaning no detuning), and its nominal range is -∞ to ∞.

[AudioBufferSourceNode.loop](/en-US/docs/Web/API/AudioBufferSourceNode/loop)

A Boolean attribute indicating if the audio asset must be replayed when the end of the [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) is reached. Its default value is `false`.

[AudioBufferSourceNode.loopStart](/en-US/docs/Web/API/AudioBufferSourceNode/loopStart)Optional

A floating-point value indicating the time, in seconds, at which playback of the [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) must begin when `loop` is `true`. Its default value is `0` (meaning that at the beginning of each loop, playback begins at the start of the audio buffer).

[AudioBufferSourceNode.loopEnd](/en-US/docs/Web/API/AudioBufferSourceNode/loopEnd)Optional

A floating-point number indicating the time, in seconds, at which playback of the [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) stops and loops back to the time indicated by `loopStart`, if `loop` is `true`. The default value is `0`.

[AudioBufferSourceNode.playbackRate](/en-US/docs/Web/API/AudioBufferSourceNode/playbackRate)

A [k-rate](/en-US/docs/Web/API/AudioParam#k-rate)[AudioParam](/en-US/docs/Web/API/AudioParam) that defines the speed factor at which the audio asset will be played, where a value of 1.0 is the sound's natural sampling rate. Since no pitch correction is applied on the output, this can be used to change the pitch of the sample. This value is compounded with `detune` to determine the final playback rate.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode), and overrides the following method:.

[start()](/en-US/docs/Web/API/AudioBufferSourceNode/start)

Schedules playback of the audio data contained in the buffer, or begins playback immediately. Additionally allows the start offset and play duration to be set.

## [Examples](#examples)

In this example, we create a two-second buffer, fill it with white noise, and then play it using an `AudioBufferSourceNode`. The comments should clearly explain what is going on.

Note: You can also [run the code live](https://mdn.github.io/webaudio-examples/audio-buffer/), or [view the source](https://github.com/mdn/webaudio-examples/blob/main/audio-buffer/index.html).

js

```
const audioCtx = new AudioContext();

// Create an empty three-second stereo buffer at the sample rate of the AudioContext
const myArrayBuffer = audioCtx.createBuffer(
  2,
  audioCtx.sampleRate * 3,
  audioCtx.sampleRate,
);

// Fill the buffer with white noise;
// just random values between -1.0 and 1.0
for (let channel = 0; channel < myArrayBuffer.numberOfChannels; channel++) {
  // This gives us the actual ArrayBuffer that contains the data
  const nowBuffering = myArrayBuffer.getChannelData(channel);
  for (let i = 0; i < myArrayBuffer.length; i++) {
    // Math.random() is in [0; 1.0]
    // audio needs to be in [-1.0; 1.0]
    nowBuffering[i] = Math.random() * 2 - 1;
  }
}

// Get an AudioBufferSourceNode.
// This is the AudioNode to use when we want to play an AudioBuffer
const source = audioCtx.createBufferSource();
// set the buffer in the AudioBufferSourceNode
source.buffer = myArrayBuffer;
// connect the AudioBufferSourceNode to the
// destination so we can hear the sound
source.connect(audioCtx.destination);
// start the source playing
source.start();
```

Note: For a `decodeAudioData()` example, see the [AudioContext.decodeAudioData()](/en-US/docs/Web/API/BaseAudioContext/decodeAudioData) page.

## [Specifications](#specifications)

Specification
[Web Audio API# AudioBufferSourceNode](https://webaudio.github.io/web-audio-api/#AudioBufferSourceNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioBufferSourceNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiobuffersourcenode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioBufferSourceNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiobuffersourcenode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioBufferSourceNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiobuffersourcenode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
