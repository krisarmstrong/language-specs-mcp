# AudioNode

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioNode&level=high)

The `AudioNode` interface is a generic interface for representing an audio processing module.

Examples include:

- an audio source (e.g., an HTML [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) or [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element, an [OscillatorNode](/en-US/docs/Web/API/OscillatorNode), etc.),
- the audio destination,
- intermediate processing module (e.g., a filter like [BiquadFilterNode](/en-US/docs/Web/API/BiquadFilterNode) or [ConvolverNode](/en-US/docs/Web/API/ConvolverNode)), or
- volume control (like [GainNode](/en-US/docs/Web/API/GainNode))

Note: An `AudioNode` can be target of events, therefore it implements the [EventTarget](/en-US/docs/Web/API/EventTarget) interface.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Description](#description)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[AudioNode.context](/en-US/docs/Web/API/AudioNode/context)Read only

Returns the associated [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext), that is the object representing the processing graph the node is participating in.

[AudioNode.numberOfInputs](/en-US/docs/Web/API/AudioNode/numberOfInputs)Read only

Returns the number of inputs feeding the node. Source nodes are defined as nodes having a `numberOfInputs` property with a value of `0`.

[AudioNode.numberOfOutputs](/en-US/docs/Web/API/AudioNode/numberOfOutputs)Read only

Returns the number of outputs coming out of the node. Destination nodes — like [AudioDestinationNode](/en-US/docs/Web/API/AudioDestinationNode) — have a value of `0` for this attribute.

[AudioNode.channelCount](/en-US/docs/Web/API/AudioNode/channelCount)

Represents an integer used to determine how many channels are used when [up-mixing and down-mixing](/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API#up-mixing_and_down-mixing) connections to any inputs to the node. Its usage and precise definition depend on the value of [AudioNode.channelCountMode](/en-US/docs/Web/API/AudioNode/channelCountMode).

[AudioNode.channelCountMode](/en-US/docs/Web/API/AudioNode/channelCountMode)

Represents an enumerated value describing the way channels must be matched between the node's inputs and outputs.

[AudioNode.channelInterpretation](/en-US/docs/Web/API/AudioNode/channelInterpretation)

Represents an enumerated value describing the meaning of the channels. This interpretation will define how audio [up-mixing and down-mixing](/en-US/docs/Web/API/Web_Audio_API/Basic_concepts_behind_Web_Audio_API#up-mixing_and_down-mixing) will happen. The possible values are `"speakers"` or `"discrete"`.

## [Instance methods](#instance_methods)

Also implements methods from the interface[EventTarget](/en-US/docs/Web/API/EventTarget).

[AudioNode.connect()](/en-US/docs/Web/API/AudioNode/connect)

Allows us to connect the output of this node to be input into another node, either as audio data or as the value of an [AudioParam](/en-US/docs/Web/API/AudioParam).

[AudioNode.disconnect()](/en-US/docs/Web/API/AudioNode/disconnect)

Allows us to disconnect the current node from another one it is already connected to.

## [Description](#description)

### [The audio routing graph](#the_audio_routing_graph)

Each `AudioNode` has inputs and outputs, and multiple audio nodes are connected to build a processing graph. This graph is contained in an [AudioContext](/en-US/docs/Web/API/AudioContext), and each audio node can only belong to one audio context.

A source node has zero inputs but one or multiple outputs, and can be used to generate sound. On the other hand, a destination node has no outputs; instead, all its inputs are directly played back on the speakers (or whatever audio output device the audio context uses). In addition, there are processing nodes which have inputs and outputs. The exact processing done varies from one `AudioNode` to another but, in general, a node reads its inputs, does some audio-related processing, and generates new values for its outputs, or lets the audio pass through (for example in the [AnalyserNode](/en-US/docs/Web/API/AnalyserNode), where the result of the processing is accessed separately).

The more nodes in a graph, the higher the latency will be. For example, if your graph has a latency of 500ms, when the source node plays a sound, it will take half a second until that sound can be heard on your speakers (or even longer because of latency in the underlying audio device). Therefore, if you need to have interactive audio, keep the graph as small as possible, and put user-controlled audio nodes at the end of a graph. For example, a volume control (`GainNode`) should be the last node so that volume changes take immediate effect.

Each input and output has a given amount of channels. For example, mono audio has one channel, while stereo audio has two channels. The Web Audio API will up-mix or down-mix the number of channels as required; check the Web Audio spec for details.

For a list of all audio nodes, see the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) homepage.

### [Creating an AudioNode](#creating_an_audionode)

There are two ways to create an `AudioNode`: via the constructor and via the factory method.

js

```
// constructor
const analyserNode = new AnalyserNode(audioCtx, {
  fftSize: 2048,
  maxDecibels: -25,
  minDecibels: -60,
  smoothingTimeConstant: 0.5,
});
```

js

```
// factory method
const analyserNode = audioCtx.createAnalyser();
analyserNode.fftSize = 2048;
analyserNode.maxDecibels = -25;
analyserNode.minDecibels = -60;
analyserNode.smoothingTimeConstant = 0.5;
```

You are free to use either constructors or factory methods, or mix both, however there are advantages to using the constructors:

- All parameters can be set during construction time and don't need to be set individually.
- You can [sub-class an audio node](https://github.com/WebAudio/web-audio-api/issues/251). While the actual processing is done internally by the browser and cannot be altered, you could write a wrapper around an audio node to provide custom properties and methods.
- Slightly better performance: In both Chrome and Firefox, the factory methods call the constructors internally.

Brief history: The first version of the Web Audio spec only defined the factory methods. After a [design review in October 2013](https://github.com/WebAudio/web-audio-api/issues/250), it was decided to add constructors because they have numerous benefits over factory methods. The constructors were added to the spec from August to October 2016. Factory methods continue to be included in the spec and are not deprecated.

## [Example](#example)

This simple snippet of code shows the creation of some audio nodes, and how the `AudioNode` properties and methods can be used. You can find examples of such usage on any of the examples linked to on the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) landing page (for example [Violent Theremin](https://github.com/mdn/webaudio-examples/tree/main/violent-theremin)).

js

```
const audioCtx = new AudioContext();

const oscillator = new OscillatorNode(audioCtx);
const gainNode = new GainNode(audioCtx);

oscillator.connect(gainNode).connect(audioCtx.destination);

oscillator.context;
oscillator.numberOfInputs;
oscillator.numberOfOutputs;
oscillator.channelCount;
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioNode](https://webaudio.github.io/web-audio-api/#AudioNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audionode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudionode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudionode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F702cd9e4d2834e13aea345943efc8d0c03d92ec9%0A*+Document+last+modified%3A+2025-04-03T04%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
