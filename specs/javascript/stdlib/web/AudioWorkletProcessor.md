# AudioWorkletProcessor

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletProcessor&level=high)

The `AudioWorkletProcessor` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents an audio processing code behind a custom [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode). It lives in the [AudioWorkletGlobalScope](/en-US/docs/Web/API/AudioWorkletGlobalScope) and runs on the Web Audio rendering thread. In turn, an [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) based on it runs on the main thread.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

Note: The `AudioWorkletProcessor` and classes that derive from it cannot be instantiated directly from a user-supplied code. Instead, they are created only internally by the creation of an associated [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode)s. The constructor of the deriving class is getting called with an options object, so you can perform a custom initialization procedures — see constructor page for details.

[AudioWorkletProcessor()](/en-US/docs/Web/API/AudioWorkletProcessor/AudioWorkletProcessor)

Creates a new instance of an `AudioWorkletProcessor` object.

## [Instance properties](#instance_properties)

[port](/en-US/docs/Web/API/AudioWorkletProcessor/port)Read only

Returns a [MessagePort](/en-US/docs/Web/API/MessagePort) used for bidirectional communication between the processor and the [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) which it belongs to. The other end is available under the [port](/en-US/docs/Web/API/AudioWorkletNode/port) property of the node.

## [Instance methods](#instance_methods)

The `AudioWorkletProcessor` interface does not define any methods of its own. However, you must provide a [process()](/en-US/docs/Web/API/AudioWorkletProcessor/process) method, which is called in order to process the audio stream.

## [Events](#events)

The `AudioWorkletProcessor` interface doesn't respond to any events.

## [Usage notes](#usage_notes)

### [Deriving classes](#deriving_classes)

To define custom audio processing code you have to derive a class from the `AudioWorkletProcessor` interface. Although not defined on the interface, the deriving class must have the [process](/en-US/docs/Web/API/AudioWorkletProcessor/process) method. This method gets called for each block of 128 sample-frames and takes input and output arrays and calculated values of custom [AudioParam](/en-US/docs/Web/API/AudioParam)s (if they are defined) as parameters. You can use inputs and audio parameter values to fill the outputs array, which by default holds silence.

Optionally, if you want custom [AudioParam](/en-US/docs/Web/API/AudioParam)s on your node, you can supply a [parameterDescriptors](/en-US/docs/Web/API/AudioWorkletProcessor/parameterDescriptors_static) property as a static getter on the processor. The array of [AudioParamDescriptor](/en-US/docs/Web/API/AudioParamDescriptor)-based objects returned is used internally to create the [AudioParam](/en-US/docs/Web/API/AudioParam)s during the instantiation of the `AudioWorkletNode`.

The resulting `AudioParam`s reside in the [parameters](/en-US/docs/Web/API/AudioWorkletNode/parameters) property of the node and can be automated using standard methods such as [linearRampToValueAtTime](/en-US/docs/Web/API/AudioParam/linearRampToValueAtTime). Their calculated values will be passed into the [process()](/en-US/docs/Web/API/AudioWorkletProcessor/process) method of the processor for you to shape the node output accordingly.

### [Processing audio](#processing_audio)

An example algorithm of creating a custom audio processing mechanism is:

1. 

Create a separate file;

2. 

In the file:

  1. Extend the `AudioWorkletProcessor` class (see ["Deriving classes" section](#deriving_classes)) and supply your own [process()](/en-US/docs/Web/API/AudioWorkletProcessor/process) method in it;
  2. Register the processor using [AudioWorkletGlobalScope.registerProcessor()](/en-US/docs/Web/API/AudioWorkletGlobalScope/registerProcessor) method;

3. 

Load the file using [addModule()](/en-US/docs/Web/API/Worklet/addModule) method on your audio context's [audioWorklet](/en-US/docs/Web/API/BaseAudioContext/audioWorklet) property;

4. 

Create an [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) based on the processor. The processor will be instantiated internally by the `AudioWorkletNode` constructor.

5. 

Connect the node to the other nodes.

## [Examples](#examples)

In the example below we create a custom [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) that outputs white noise.

First, we need to define a custom `AudioWorkletProcessor`, which will output white noise, and register it. Note that this should be done in a separate file.

js

```
// white-noise-processor.js
class WhiteNoiseProcessor extends AudioWorkletProcessor {
  process(inputs, outputs, parameters) {
    const output = outputs[0];
    output.forEach((channel) => {
      for (let i = 0; i < channel.length; i++) {
        channel[i] = Math.random() * 2 - 1;
      }
    });
    return true;
  }
}

registerProcessor("white-noise-processor", WhiteNoiseProcessor);
```

Next, in our main script file we'll load the processor, create an instance of [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode), passing it the name of the processor, then connect the node to an audio graph.

js

```
const audioContext = new AudioContext();
await audioContext.audioWorklet.addModule("white-noise-processor.js");
const whiteNoiseNode = new AudioWorkletNode(
  audioContext,
  "white-noise-processor",
);
whiteNoiseNode.connect(audioContext.destination);
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioWorkletProcessor](https://webaudio.github.io/web-audio-api/#AudioWorkletProcessor)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)
- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [Using AudioWorklet](/en-US/docs/Web/API/Web_Audio_API/Using_AudioWorklet)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioWorkletProcessor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioworkletprocessor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletProcessor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioworkletprocessor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletProcessor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioworkletprocessor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
