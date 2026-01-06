# AudioWorkletGlobalScope

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletGlobalScope&level=high)

The `AudioWorkletGlobalScope` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents a global execution context for user-supplied code, which defines custom [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor)-derived classes.

Each [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext) has a single [AudioWorklet](/en-US/docs/Web/API/AudioWorklet) available under the [audioWorklet](/en-US/docs/Web/API/BaseAudioContext/audioWorklet) property, which runs its code in a single `AudioWorkletGlobalScope`.

As the global execution context is shared across the current `BaseAudioContext`, it's possible to define any other variables and perform any actions allowed in worklets — apart from defining `AudioWorkletProcessor` derived classes.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties defined on its parent interface, [WorkletGlobalScope](/en-US/docs/Web/API/WorkletGlobalScope).

[currentFrame](/en-US/docs/Web/API/AudioWorkletGlobalScope/currentFrame)Read only

Returns an integer that represents the ever-increasing current sample-frame of the audio block being processed. It is incremented by 128 (the size of a render quantum) after the processing of each audio block.

[currentTime](/en-US/docs/Web/API/AudioWorkletGlobalScope/currentTime)Read only

Returns a double that represents the ever-increasing context time of the audio block being processed. It is equal to the [currentTime](/en-US/docs/Web/API/BaseAudioContext/currentTime) property of the [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext) the worklet belongs to.

[sampleRate](/en-US/docs/Web/API/AudioWorkletGlobalScope/sampleRate)Read only

Returns a float that represents the sample rate of the associated [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext).

[port](/en-US/docs/Web/API/AudioWorkletGlobalScope/port)Read onlyExperimental

Returns a [MessagePort](/en-US/docs/Web/API/MessagePort) for custom, asynchronous communication between code in the main thread and the global scope of an audio worklet. This allows for custom messages, such as sending and receiving control data or global settings.

## [Instance methods](#instance_methods)

This interface also inherits methods defined on its parent interface, [WorkletGlobalScope](/en-US/docs/Web/API/WorkletGlobalScope).

[registerProcessor()](/en-US/docs/Web/API/AudioWorkletGlobalScope/registerProcessor)

Registers a class derived from the [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor) interface. The class can then be used by creating an [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode), providing its registered name.

## [Examples](#examples)

In this example we output all global properties into the console in the constructor of a custom [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor).

First we need to define the processor, and register it. Note that this should be done in a separate file.

js

```
// AudioWorkletProcessor defined in : test-processor.js
class TestProcessor extends AudioWorkletProcessor {
  constructor() {
    super();

    // Logs the current sample-frame and time at the moment of instantiation.
    // They are accessible from the AudioWorkletGlobalScope.
    console.log(currentFrame);
    console.log(currentTime);
  }

  // The process method is required - output silence,
  // which the outputs are already filled with.
  process(inputs, outputs, parameters) {
    return true;
  }
}

// Logs the sample rate, that is not going to change ever,
// because it's a read-only property of a BaseAudioContext
// and is set only during its instantiation.
console.log(sampleRate);

// You can declare any variables and use them in your processors
// for example it may be an ArrayBuffer with a wavetable
const usefulVariable = 42;
console.log(usefulVariable);

registerProcessor("test-processor", TestProcessor);
```

Next, in our main scripts file we'll load the processor, create an instance of [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) — passing the name of the processor to it — and connect the node to an audio graph. We should see the output of [console.log()](/en-US/docs/Web/API/console/log_static) calls in the console:

js

```
const audioContext = new AudioContext();
await audioContext.audioWorklet.addModule("test-processor.js");
const testNode = new AudioWorkletNode(audioContext, "test-processor");
testNode.connect(audioContext.destination);
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioWorkletGlobalScope](https://webaudio.github.io/web-audio-api/#AudioWorkletGlobalScope)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)
- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [Using AudioWorklet](/en-US/docs/Web/API/Web_Audio_API/Using_AudioWorklet)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioWorkletGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioworkletglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioworkletglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorkletGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioworkletglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa61be259435257328a25c462cb0f42bc91981a6f%0A*+Document+last+modified%3A+2025-05-09T10%3A10%3A27.000Z%0A%0A%3C%2Fdetails%3E)
