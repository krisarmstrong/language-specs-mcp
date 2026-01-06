# AudioBuffer

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioBuffer&level=high)

The `AudioBuffer` interface represents a short audio asset residing in memory, created from an audio file using the [AudioContext.decodeAudioData()](/en-US/docs/Web/API/BaseAudioContext/decodeAudioData) method, or from raw data using [AudioContext.createBuffer()](/en-US/docs/Web/API/BaseAudioContext/createBuffer). Once put into an AudioBuffer, the audio can then be played by being passed into an [AudioBufferSourceNode](/en-US/docs/Web/API/AudioBufferSourceNode).

Objects of these types are designed to hold small audio snippets, typically less than 45 s. For longer sounds, objects implementing the [MediaElementAudioSourceNode](/en-US/docs/Web/API/MediaElementAudioSourceNode) are more suitable. The buffer contains the audio signal waveform encoded as a series of amplitudes in the following format: non-interleaved IEEE754 32-bit linear PCM with a nominal range between `-1` and `+1`, that is, a 32-bit floating point buffer, with each sample between -1.0 and 1.0. If the `AudioBuffer` has multiple channels, they are stored in separate buffers.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AudioBuffer()](/en-US/docs/Web/API/AudioBuffer/AudioBuffer)

Creates and returns a new `AudioBuffer` object instance.

## [Instance properties](#instance_properties)

[AudioBuffer.sampleRate](/en-US/docs/Web/API/AudioBuffer/sampleRate)Read only

Returns a float representing the sample rate, in samples per second, of the PCM data stored in the buffer.

[AudioBuffer.length](/en-US/docs/Web/API/AudioBuffer/length)Read only

Returns an integer representing the length, in sample-frames, of the PCM data stored in the buffer.

[AudioBuffer.duration](/en-US/docs/Web/API/AudioBuffer/duration)Read only

Returns a double representing the duration, in seconds, of the PCM data stored in the buffer.

[AudioBuffer.numberOfChannels](/en-US/docs/Web/API/AudioBuffer/numberOfChannels)Read only

Returns an integer representing the number of discrete audio channels described by the PCM data stored in the buffer.

## [Instance methods](#instance_methods)

[AudioBuffer.getChannelData()](/en-US/docs/Web/API/AudioBuffer/getChannelData)

Returns a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) containing the PCM data associated with the channel, defined by the `channel` parameter (with `0` representing the first channel).

[AudioBuffer.copyFromChannel()](/en-US/docs/Web/API/AudioBuffer/copyFromChannel)

Copies the samples from the specified channel of the `AudioBuffer` to the `destination` array.

[AudioBuffer.copyToChannel()](/en-US/docs/Web/API/AudioBuffer/copyToChannel)

Copies the samples to the specified channel of the `AudioBuffer`, from the `source` array.

## [Example](#example)

The following simple example shows how to create an `AudioBuffer` and fill it with random white noise. You can find the full source code at our [webaudio-examples](https://github.com/mdn/webaudio-examples) repository; a [running live](https://mdn.github.io/webaudio-examples/audio-buffer/) version is also available.

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
  // This gives us the actual array that contains the data
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

## [Specifications](#specifications)

Specification
[Web Audio API# AudioBuffer](https://webaudio.github.io/web-audio-api/#AudioBuffer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AudioBuffer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiobuffer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioBuffer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiobuffer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioBuffer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiobuffer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
