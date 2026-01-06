# BaseAudioContext

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBaseAudioContext&level=high)

The `BaseAudioContext` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) acts as a base definition for online and offline audio-processing graphs, as represented by [AudioContext](/en-US/docs/Web/API/AudioContext) and [OfflineAudioContext](/en-US/docs/Web/API/OfflineAudioContext) respectively. You wouldn't use `BaseAudioContext` directly — you'd use its features via one of these two inheriting interfaces.

A `BaseAudioContext` can be a target of events, therefore it implements the [EventTarget](/en-US/docs/Web/API/EventTarget) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[BaseAudioContext.audioWorklet](/en-US/docs/Web/API/BaseAudioContext/audioWorklet)Read onlySecure context

Returns the [AudioWorklet](/en-US/docs/Web/API/AudioWorklet) object, which can be used to create and manage [AudioNode](/en-US/docs/Web/API/AudioNode)s in which JavaScript code implementing the [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor) interface are run in the background to process audio data.

[BaseAudioContext.currentTime](/en-US/docs/Web/API/BaseAudioContext/currentTime)Read only

Returns a double representing an ever-increasing hardware time in seconds used for scheduling. It starts at `0`.

[BaseAudioContext.destination](/en-US/docs/Web/API/BaseAudioContext/destination)Read only

Returns an [AudioDestinationNode](/en-US/docs/Web/API/AudioDestinationNode) representing the final destination of all audio in the context. It can be thought of as the audio-rendering device.

[BaseAudioContext.listener](/en-US/docs/Web/API/BaseAudioContext/listener)Read only

Returns the [AudioListener](/en-US/docs/Web/API/AudioListener) object, used for 3D spatialization.

[BaseAudioContext.sampleRate](/en-US/docs/Web/API/BaseAudioContext/sampleRate)Read only

Returns a float representing the sample rate (in samples per second) used by all nodes in this context. The sample-rate of an [AudioContext](/en-US/docs/Web/API/AudioContext) cannot be changed.

[BaseAudioContext.state](/en-US/docs/Web/API/BaseAudioContext/state)Read only

Returns the current state of the `AudioContext`.

## [Instance methods](#instance_methods)

Also implements methods from the interface[EventTarget](/en-US/docs/Web/API/EventTarget).

[BaseAudioContext.createAnalyser()](/en-US/docs/Web/API/BaseAudioContext/createAnalyser)

Creates an [AnalyserNode](/en-US/docs/Web/API/AnalyserNode), which can be used to expose audio time and frequency data and for example to create data visualizations.

[BaseAudioContext.createBiquadFilter()](/en-US/docs/Web/API/BaseAudioContext/createBiquadFilter)

Creates a [BiquadFilterNode](/en-US/docs/Web/API/BiquadFilterNode), which represents a second order filter configurable as several different common filter types: high-pass, low-pass, band-pass, etc

[BaseAudioContext.createBuffer()](/en-US/docs/Web/API/BaseAudioContext/createBuffer)

Creates a new, empty [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) object, which can then be populated by data and played via an [AudioBufferSourceNode](/en-US/docs/Web/API/AudioBufferSourceNode).

[BaseAudioContext.createBufferSource()](/en-US/docs/Web/API/BaseAudioContext/createBufferSource)

Creates an [AudioBufferSourceNode](/en-US/docs/Web/API/AudioBufferSourceNode), which can be used to play and manipulate audio data contained within an [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) object. [AudioBuffer](/en-US/docs/Web/API/AudioBuffer)s are created using [AudioContext.createBuffer()](/en-US/docs/Web/API/BaseAudioContext/createBuffer) or returned by [AudioContext.decodeAudioData()](/en-US/docs/Web/API/BaseAudioContext/decodeAudioData) when it successfully decodes an audio track.

[BaseAudioContext.createConstantSource()](/en-US/docs/Web/API/BaseAudioContext/createConstantSource)

Creates a [ConstantSourceNode](/en-US/docs/Web/API/ConstantSourceNode) object, which is an audio source that continuously outputs a monaural (one-channel) sound signal whose samples all have the same value.

[BaseAudioContext.createChannelMerger()](/en-US/docs/Web/API/BaseAudioContext/createChannelMerger)

Creates a [ChannelMergerNode](/en-US/docs/Web/API/ChannelMergerNode), which is used to combine channels from multiple audio streams into a single audio stream.

[BaseAudioContext.createChannelSplitter()](/en-US/docs/Web/API/BaseAudioContext/createChannelSplitter)

Creates a [ChannelSplitterNode](/en-US/docs/Web/API/ChannelSplitterNode), which is used to access the individual channels of an audio stream and process them separately.

[BaseAudioContext.createConvolver()](/en-US/docs/Web/API/BaseAudioContext/createConvolver)

Creates a [ConvolverNode](/en-US/docs/Web/API/ConvolverNode), which can be used to apply convolution effects to your audio graph, for example a reverberation effect.

[BaseAudioContext.createDelay()](/en-US/docs/Web/API/BaseAudioContext/createDelay)

Creates a [DelayNode](/en-US/docs/Web/API/DelayNode), which is used to delay the incoming audio signal by a certain amount. This node is also useful to create feedback loops in a Web Audio API graph.

[BaseAudioContext.createDynamicsCompressor()](/en-US/docs/Web/API/BaseAudioContext/createDynamicsCompressor)

Creates a [DynamicsCompressorNode](/en-US/docs/Web/API/DynamicsCompressorNode), which can be used to apply acoustic compression to an audio signal.

[BaseAudioContext.createGain()](/en-US/docs/Web/API/BaseAudioContext/createGain)

Creates a [GainNode](/en-US/docs/Web/API/GainNode), which can be used to control the overall volume of the audio graph.

[BaseAudioContext.createIIRFilter()](/en-US/docs/Web/API/BaseAudioContext/createIIRFilter)

Creates an [IIRFilterNode](/en-US/docs/Web/API/IIRFilterNode), which represents a second order filter configurable as several different common filter types.

[BaseAudioContext.createOscillator()](/en-US/docs/Web/API/BaseAudioContext/createOscillator)

Creates an [OscillatorNode](/en-US/docs/Web/API/OscillatorNode), a source representing a periodic waveform. It basically generates a tone.

[BaseAudioContext.createPanner()](/en-US/docs/Web/API/BaseAudioContext/createPanner)

Creates a [PannerNode](/en-US/docs/Web/API/PannerNode), which is used to spatialize an incoming audio stream in 3D space.

[BaseAudioContext.createPeriodicWave()](/en-US/docs/Web/API/BaseAudioContext/createPeriodicWave)

Creates a [PeriodicWave](/en-US/docs/Web/API/PeriodicWave), used to define a periodic waveform that can be used to determine the output of an [OscillatorNode](/en-US/docs/Web/API/OscillatorNode).

[BaseAudioContext.createScriptProcessor()](/en-US/docs/Web/API/BaseAudioContext/createScriptProcessor)Deprecated

Creates a [ScriptProcessorNode](/en-US/docs/Web/API/ScriptProcessorNode), which can be used for direct audio processing via JavaScript.

[BaseAudioContext.createStereoPanner()](/en-US/docs/Web/API/BaseAudioContext/createStereoPanner)

Creates a [StereoPannerNode](/en-US/docs/Web/API/StereoPannerNode), which can be used to apply stereo panning to an audio source.

[BaseAudioContext.createWaveShaper()](/en-US/docs/Web/API/BaseAudioContext/createWaveShaper)

Creates a [WaveShaperNode](/en-US/docs/Web/API/WaveShaperNode), which is used to implement non-linear distortion effects.

[BaseAudioContext.decodeAudioData()](/en-US/docs/Web/API/BaseAudioContext/decodeAudioData)

Asynchronously decodes audio file data contained in an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer). In this case, the `ArrayBuffer` is usually loaded from an [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest)'s `response` attribute after setting the `responseType` to `arraybuffer`. This method only works on complete files, not fragments of audio files.

## [Events](#events)

[statechange](/en-US/docs/Web/API/BaseAudioContext/statechange_event)

Fired when the `AudioContext`'s state changes due to the calling of one of the state change methods ([AudioContext.suspend](/en-US/docs/Web/API/AudioContext/suspend), [AudioContext.resume](/en-US/docs/Web/API/AudioContext/resume), or [AudioContext.close](/en-US/docs/Web/API/AudioContext/close)).

## [Examples](#examples)

js

```
const audioContext = new AudioContext();

const oscillatorNode = audioContext.createOscillator();
const gainNode = audioContext.createGain();
const finish = audioContext.destination;
```

## [Specifications](#specifications)

Specification
[Web Audio API# BaseAudioContext](https://webaudio.github.io/web-audio-api/#BaseAudioContext)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [AudioContext](/en-US/docs/Web/API/AudioContext)
- [OfflineAudioContext](/en-US/docs/Web/API/OfflineAudioContext)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 21, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/BaseAudioContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/baseaudiocontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBaseAudioContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbaseaudiocontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBaseAudioContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbaseaudiocontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca3afa7533ac5bc2d552b0c7926d672fe79d71de%0A*+Document+last+modified%3A+2024-07-21T13%3A28%3A48.000Z%0A%0A%3C%2Fdetails%3E)
