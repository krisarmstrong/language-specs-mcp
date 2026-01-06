# AudioProcessingEvent

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `AudioProcessingEvent` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents events that occur when a [ScriptProcessorNode](/en-US/docs/Web/API/ScriptProcessorNode) input buffer is ready to be processed.

An `audioprocess` event with this interface is fired on a [ScriptProcessorNode](/en-US/docs/Web/API/ScriptProcessorNode) when audio processing is required. During audio processing, the input buffer is read and processed to produce output audio data, which is then written to the output buffer.

Warning: This feature has been deprecated and should be replaced by an [AudioWorklet](/en-US/docs/Web/API/AudioWorklet).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AudioProcessingEvent()](/en-US/docs/Web/API/AudioProcessingEvent/AudioProcessingEvent)Deprecated

Creates a new `AudioProcessingEvent` object.

## [Instance properties](#instance_properties)

Also implements the properties inherited from its parent, [Event](/en-US/docs/Web/API/Event).

[playbackTime](/en-US/docs/Web/API/AudioProcessingEvent/playbackTime)Read onlyDeprecated

A double representing the time when the audio will be played, as defined by the time of [AudioContext.currentTime](/en-US/docs/Web/API/BaseAudioContext/currentTime).

[inputBuffer](/en-US/docs/Web/API/AudioProcessingEvent/inputBuffer)Read onlyDeprecated

An [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) that is the buffer containing the input audio data to be processed. The number of channels is defined as a parameter `numberOfInputChannels`, of the factory method [AudioContext.createScriptProcessor()](/en-US/docs/Web/API/BaseAudioContext/createScriptProcessor). Note that the returned `AudioBuffer` is only valid in the scope of the event handler.

[outputBuffer](/en-US/docs/Web/API/AudioProcessingEvent/outputBuffer)Read onlyDeprecated

An [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) that is the buffer where the output audio data should be written. The number of channels is defined as a parameter, `numberOfOutputChannels`, of the factory method [AudioContext.createScriptProcessor()](/en-US/docs/Web/API/BaseAudioContext/createScriptProcessor). Note that the returned `AudioBuffer` is only valid in the scope of the event handler.

## [Examples](#examples)

### [Adding white noise using a script processor](#adding_white_noise_using_a_script_processor)

The following example shows how to use of a `ScriptProcessorNode` to take a track loaded via [AudioContext.decodeAudioData()](/en-US/docs/Web/API/BaseAudioContext/decodeAudioData), process it, adding a bit of white noise to each audio sample of the input track (buffer) and play it through the [AudioDestinationNode](/en-US/docs/Web/API/AudioDestinationNode). For each channel and each sample frame, the `scriptNode.onaudioprocess` function takes the associated `audioProcessingEvent` and uses it to loop through each channel of the input buffer, and each sample in each channel, and add a small amount of white noise, before setting that result to be the output sample in each case.

Note: For a full working example, see our [script-processor-node](https://mdn.github.io/webaudio-examples/script-processor-node/) GitHub repo. (You can also access the [source code](https://github.com/mdn/webaudio-examples/tree/main/script-processor-node).)

js

```
const myScript = document.querySelector("script");
const myPre = document.querySelector("pre");
const playButton = document.querySelector("button");

// Create AudioContext and buffer source
let audioCtx;

async function init() {
  audioCtx = new AudioContext();
  const source = audioCtx.createBufferSource();

  // Create a ScriptProcessorNode with a bufferSize of 4096 and
  // a single input and output channel
  const scriptNode = audioCtx.createScriptProcessor(4096, 1, 1);

  // Load in an audio track using fetch() and decodeAudioData()
  try {
    const response = await fetch("viper.ogg");
    const arrayBuffer = await response.arrayBuffer();
    source.buffer = await audioCtx.decodeAudioData(arrayBuffer);
  } catch (err) {
    console.error(
      `Unable to fetch the audio file: ${name} Error: ${err.message}`,
    );
  }

  // Give the node a function to process audio events
  scriptNode.addEventListener("audioprocess", (audioProcessingEvent) => {
    // The input buffer is the song we loaded earlier
    let inputBuffer = audioProcessingEvent.inputBuffer;

    // The output buffer contains the samples that will be modified
    // and played
    let outputBuffer = audioProcessingEvent.outputBuffer;

    // Loop through the output channels (in this case there is only one)
    for (let channel = 0; channel < outputBuffer.numberOfChannels; channel++) {
      let inputData = inputBuffer.getChannelData(channel);
      let outputData = outputBuffer.getChannelData(channel);

      // Loop through the 4096 samples
      for (let sample = 0; sample < inputBuffer.length; sample++) {
        // make output equal to the same as the input
        outputData[sample] = inputData[sample];

        // add noise to each output sample
        outputData[sample] += (Math.random() * 2 - 1) * 0.1;
      }
    }
  });

  source.connect(scriptNode);
  scriptNode.connect(audioCtx.destination);
  source.start();

  // When the buffer source stops playing, disconnect everything
  source.addEventListener("ended", () => {
    source.disconnect(scriptNode);
    scriptNode.disconnect(audioCtx.destination);
  });
}

// wire up play button
playButton.addEventListener("click", () => {
  if (!audioCtx) {
    init();
  }
});
```

## [Specifications](#specifications)

Specification
[Web Audio API# dom-audioprocessingevent-playbacktime](https://webaudio.github.io/web-audio-api/#dom-audioprocessingevent-playbacktime)
[Web Audio API# dom-audioprocessingevent-audioprocessingevent](https://webaudio.github.io/web-audio-api/#dom-audioprocessingevent-audioprocessingevent)
[Web Audio API# dom-audioprocessingevent-outputbuffer](https://webaudio.github.io/web-audio-api/#dom-audioprocessingevent-outputbuffer)
[Web Audio API# dom-audioprocessingevent-inputbuffer](https://webaudio.github.io/web-audio-api/#dom-audioprocessingevent-inputbuffer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioProcessingEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioprocessingevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioProcessingEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioprocessingevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioProcessingEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioprocessingevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7265fc3effa7c25b9997135104370c057a65293%0A*+Document+last+modified%3A+2025-09-25T16%3A11%3A52.000Z%0A%0A%3C%2Fdetails%3E)
