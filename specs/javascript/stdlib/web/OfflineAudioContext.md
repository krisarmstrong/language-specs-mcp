# OfflineAudioContext

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOfflineAudioContext&level=high)

The `OfflineAudioContext` interface is an [AudioContext](/en-US/docs/Web/API/AudioContext) interface representing an audio-processing graph built from linked together [AudioNode](/en-US/docs/Web/API/AudioNode)s. In contrast with a standard [AudioContext](/en-US/docs/Web/API/AudioContext), an `OfflineAudioContext` doesn't render the audio to the device hardware; instead, it generates it, as fast as it can, and outputs the result to an [AudioBuffer](/en-US/docs/Web/API/AudioBuffer).

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

[OfflineAudioContext()](/en-US/docs/Web/API/OfflineAudioContext/OfflineAudioContext)

Creates a new `OfflineAudioContext` instance.

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext).

[OfflineAudioContext.length](/en-US/docs/Web/API/OfflineAudioContext/length)Read only

An integer representing the size of the buffer in sample-frames.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext).

[OfflineAudioContext.suspend()](/en-US/docs/Web/API/OfflineAudioContext/suspend)

Schedules a suspension of the time progression in the audio context at the specified time and returns a promise.

[OfflineAudioContext.startRendering()](/en-US/docs/Web/API/OfflineAudioContext/startRendering)

Starts rendering the audio, taking into account the current connections and the current scheduled changes. This page covers both the event-based version and the promise-based version.

### [Deprecated methods](#deprecated_methods)

[OfflineAudioContext.resume()](/en-US/docs/Web/API/OfflineAudioContext/resume)

Resumes the progression of time in an audio context that has previously been suspended.

Note: The `resume()` method is still available — it is now defined on the [BaseAudioContext](/en-US/docs/Web/API/BaseAudioContext) interface (see [AudioContext.resume](/en-US/docs/Web/API/AudioContext/resume)) and thus can be accessed by both the [AudioContext](/en-US/docs/Web/API/AudioContext) and `OfflineAudioContext` interfaces.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[complete](/en-US/docs/Web/API/OfflineAudioContext/complete_event)

Fired when the rendering of an offline audio context is complete.

## [Examples](#examples)

### [Playing audio with an offline audio context](#playing_audio_with_an_offline_audio_context)

In this example, we declare both an [AudioContext](/en-US/docs/Web/API/AudioContext) and an `OfflineAudioContext` object. We use the `AudioContext` to load an audio track [fetch()](/en-US/docs/Web/API/Window/fetch), then the `OfflineAudioContext` to render the audio into an [AudioBufferSourceNode](/en-US/docs/Web/API/AudioBufferSourceNode) and play the track through. After the offline audio graph is set up, we render it to an [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) using `OfflineAudioContext.startRendering()`.

When the `startRendering()` promise resolves, rendering has completed and the output `AudioBuffer` is returned out of the promise.

At this point we create another audio context, create an [AudioBufferSourceNode](/en-US/docs/Web/API/AudioBufferSourceNode) inside it, and set its buffer to be equal to the promise `AudioBuffer`. This is then played as part of a simple standard audio graph.

Note: You can [run the full example live](https://mdn.github.io/webaudio-examples/offline-audio-context-promise/), or [view the source](https://github.com/mdn/webaudio-examples/tree/main/offline-audio-context-promise).

js

```
// Define both online and offline audio contexts
let audioCtx; // Must be initialized after a user interaction
const offlineCtx = new OfflineAudioContext(2, 44100 * 40, 44100);

// Define constants for dom nodes
const play = document.querySelector("#play");

function getData() {
  // Fetch an audio track, decode it and stick it in a buffer.
  // Then we put the buffer into the source and can play it.
  fetch("viper.ogg")
    .then((response) => response.arrayBuffer())
    .then((downloadedBuffer) => audioCtx.decodeAudioData(downloadedBuffer))
    .then((decodedBuffer) => {
      console.log("File downloaded successfully.");
      const source = new AudioBufferSourceNode(offlineCtx, {
        buffer: decodedBuffer,
      });
      source.connect(offlineCtx.destination);
      return source.start();
    })
    .then(() => offlineCtx.startRendering())
    .then((renderedBuffer) => {
      console.log("Rendering completed successfully.");
      play.disabled = false;
      const song = new AudioBufferSourceNode(audioCtx, {
        buffer: renderedBuffer,
      });
      song.connect(audioCtx.destination);

      // Start the song
      song.start();
    })
    .catch((err) => {
      console.error(`Error encountered: ${err}`);
    });
}

// Activate the play button
play.onclick = () => {
  play.disabled = true;
  // We can initialize the context as the user clicked.
  audioCtx = new AudioContext();

  // Fetch the data and start the song
  getData();
};
```

## [Specifications](#specifications)

Specification
[Web Audio API# OfflineAudioContext](https://webaudio.github.io/web-audio-api/#OfflineAudioContext)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 4, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/OfflineAudioContext/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/offlineaudiocontext/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOfflineAudioContext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fofflineaudiocontext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOfflineAudioContext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fofflineaudiocontext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff2088b8912ef205a737551441d54b73507bd3ac6%0A*+Document+last+modified%3A+2024-08-04T23%3A19%3A14.000Z%0A%0A%3C%2Fdetails%3E)
