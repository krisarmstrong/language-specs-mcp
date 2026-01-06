# AudioWorkletNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletNode&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: Although the interface is available outside [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts), the [BaseAudioContext.audioWorklet](/en-US/docs/Web/API/BaseAudioContext/audioWorklet) property is not, thus custom [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor)s cannot be defined outside them.

The `AudioWorkletNode` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents a base class for a user-defined [AudioNode](/en-US/docs/Web/API/AudioNode), which can be connected to an audio routing graph along with other nodes. It has an associated [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor), which does the actual audio processing in a Web Audio rendering thread.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AudioWorkletNode()](/en-US/docs/Web/API/AudioWorkletNode/AudioWorkletNode)

Creates a new instance of an `AudioWorkletNode` object.

## [Instance properties](#instance_properties)

Also Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[AudioWorkletNode.port](/en-US/docs/Web/API/AudioWorkletNode/port)Read only

Returns a [MessagePort](/en-US/docs/Web/API/MessagePort) used for bidirectional communication between the node and its associated [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor). The other end is available under the [port](/en-US/docs/Web/API/AudioWorkletProcessor/port) property of the processor.

[AudioWorkletNode.parameters](/en-US/docs/Web/API/AudioWorkletNode/parameters)Read only

Returns an [AudioParamMap](/en-US/docs/Web/API/AudioParamMap) — a collection of [AudioParam](/en-US/docs/Web/API/AudioParam) objects. They are instantiated during the creation of the underlying `AudioWorkletProcessor`. If the `AudioWorkletProcessor` has a static [parameterDescriptors](/en-US/docs/Web/API/AudioWorkletProcessor/parameterDescriptors_static) getter, the [AudioParamDescriptor](/en-US/docs/Web/API/AudioParamDescriptor) array returned from it is used to create `AudioParam` objects on the `AudioWorkletNode`. With this mechanism it is possible to make your own `AudioParam` objects accessible from your `AudioWorkletNode`. You can then use their values in the associated `AudioWorkletProcessor`.

### [Events](#events)

[processorerror](/en-US/docs/Web/API/AudioWorkletNode/processorerror_event)

Fired when an error is thrown in associated [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor). Once fired, the processor and consequently the node will output silence throughout its lifetime.

## [Instance methods](#instance_methods)

Also inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

The `AudioWorkletNode` interface does not define any methods of its own.

## [Examples](#examples)

In this example we create a custom `AudioWorkletNode` that outputs random noise.

First, we need to define a custom [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor), which will output random noise, and register it. Note that this should be done in a separate file.

js

```
// random-noise-processor.js
class RandomNoiseProcessor extends AudioWorkletProcessor {
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

registerProcessor("random-noise-processor", RandomNoiseProcessor);
```

Next, in our main script file we'll load the processor, create an instance of `AudioWorkletNode` passing it the name of the processor, and connect the node to an audio graph.

js

```
const audioContext = new AudioContext();
await audioContext.audioWorklet.addModule("random-noise-processor.js");
const randomNoiseNode = new AudioWorkletNode(
  audioContext,
  "random-noise-processor",
);
randomNoiseNode.connect(audioContext.destination);
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioWorkletNode](https://webaudio.github.io/web-audio-api/#AudioWorkletNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)
- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [Using AudioWorklet](/en-US/docs/Web/API/Web_Audio_API/Using_AudioWorklet)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioWorkletNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioworkletnode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioworkletnode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioworkletnode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
