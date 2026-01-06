# AudioContext

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioContext&level=high)

The `AudioContext` interface represents an audio-processing graph built from audio modules linked together, each represented by an [AudioNode](/en-US/docs/Web/API/AudioNode).

An audio context controls both the creation of the nodes it contains and the execution of the audio processing, or decoding. You need to create an `AudioContext` before you do anything else, as everything happens inside a context. It's recommended to create one AudioContext and reuse it instead of initializing a new one each time, and it's OK to use a single `AudioContext` for several different audio sources and pipeline concurrently.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AudioContext()](/en-US/docs/Web/API/AudioContext/AudioContext)

Creates and returns a new `AudioContext` object.

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext).

[AudioContext.baseLatency](/en-US/docs/Web/API/AudioContext/baseLatency)Read only

Returns the number of seconds of processing latency incurred by the `AudioContext` passing the audio from the [AudioDestinationNode](/en-US/docs/Web/API/AudioDestinationNode) to the audio subsystem.

[AudioContext.outputLatency](/en-US/docs/Web/API/AudioContext/outputLatency)Read only

Returns an estimation of the output latency of the current audio context.

[AudioContext.sinkId](/en-US/docs/Web/API/AudioContext/sinkId)Read onlyExperimentalSecure context

Returns the sink ID of the current output audio device.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext).

[AudioContext.close()](/en-US/docs/Web/API/AudioContext/close)

Closes the audio context, releasing any system audio resources that it uses.

[AudioContext.createMediaElementSource()](/en-US/docs/Web/API/AudioContext/createMediaElementSource)

Creates a [MediaElementAudioSourceNode](/en-US/docs/Web/API/MediaElementAudioSourceNode) associated with an [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement). This can be used to play and manipulate audio from [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) or [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) elements.

[AudioContext.createMediaStreamSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamSource)

Creates a [MediaStreamAudioSourceNode](/en-US/docs/Web/API/MediaStreamAudioSourceNode) associated with a [MediaStream](/en-US/docs/Web/API/MediaStream) representing an audio stream which may come from the local computer microphone or other sources.

[AudioContext.createMediaStreamDestination()](/en-US/docs/Web/API/AudioContext/createMediaStreamDestination)

Creates a [MediaStreamAudioDestinationNode](/en-US/docs/Web/API/MediaStreamAudioDestinationNode) associated with a [MediaStream](/en-US/docs/Web/API/MediaStream) representing an audio stream which may be stored in a local file or sent to another computer.

[AudioContext.createMediaStreamTrackSource()](/en-US/docs/Web/API/AudioContext/createMediaStreamTrackSource)

Creates a [MediaStreamTrackAudioSourceNode](/en-US/docs/Web/API/MediaStreamTrackAudioSourceNode) associated with a [MediaStream](/en-US/docs/Web/API/MediaStream) representing a media stream track.

[AudioContext.getOutputTimestamp()](/en-US/docs/Web/API/AudioContext/getOutputTimestamp)

Returns a new `AudioTimestamp` object containing two audio timestamp values relating to the current audio context.

[AudioContext.resume()](/en-US/docs/Web/API/AudioContext/resume)

Resumes the progression of time in an audio context that has previously been suspended/paused.

[AudioContext.setSinkId()](/en-US/docs/Web/API/AudioContext/setSinkId)ExperimentalSecure context

Sets the output audio device for the `AudioContext`.

[AudioContext.suspend()](/en-US/docs/Web/API/AudioContext/suspend)

Suspends the progression of time in the audio context, temporarily halting audio hardware access and reducing CPU/battery usage in the process.

## [Events](#events)

[sinkchange](/en-US/docs/Web/API/AudioContext/sinkchange_event)Experimental

Fired when the output audio device (and therefore, the [AudioContext.sinkId](/en-US/docs/Web/API/AudioContext/sinkId)) has changed.

## [Examples](#examples)

Basic audio context declaration:

js

```
const audioCtx = new AudioContext();

const oscillatorNode = audioCtx.createOscillator();
const gainNode = audioCtx.createGain();
const finish = audioCtx.destination;
// etc.
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioContext](https://webaudio.github.io/web-audio-api/#AudioContext)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [OfflineAudioContext](/en-US/docs/Web/API/OfflineAudioContext)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiocontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiocontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiocontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
