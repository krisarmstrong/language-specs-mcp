# AnalyserNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnalyserNode&level=high)

The `AnalyserNode` interface represents a node able to provide real-time frequency and time-domain analysis information. It is an [AudioNode](/en-US/docs/Web/API/AudioNode) that passes the audio stream unchanged from the input to the output, but allows you to take the generated data, process it, and create audio visualizations.

An `AnalyserNode` has exactly one input and one output. The node works even if the output is not connected.

Number of inputs`1`Number of outputs`1` (but may be left unconnected)Channel count mode`"max"`Channel count`2`Channel interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AnalyserNode()](/en-US/docs/Web/API/AnalyserNode/AnalyserNode)

Creates a new instance of an `AnalyserNode` object.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[AnalyserNode.fftSize](/en-US/docs/Web/API/AnalyserNode/fftSize)

An unsigned long value representing the size of the FFT ([Fast Fourier Transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)) to be used to determine the frequency domain.

[AnalyserNode.frequencyBinCount](/en-US/docs/Web/API/AnalyserNode/frequencyBinCount)Read only

An unsigned long value half that of the FFT size. This generally equates to the number of data values you will have to play with for the visualization.

[AnalyserNode.minDecibels](/en-US/docs/Web/API/AnalyserNode/minDecibels)

A double value representing the minimum power value in the scaling range for the FFT analysis data, for conversion to unsigned byte values — basically, this specifies the minimum value for the range of results when using `getByteFrequencyData()`.

[AnalyserNode.maxDecibels](/en-US/docs/Web/API/AnalyserNode/maxDecibels)

A double value representing the maximum power value in the scaling range for the FFT analysis data, for conversion to unsigned byte values — basically, this specifies the maximum value for the range of results when using `getByteFrequencyData()`.

[AnalyserNode.smoothingTimeConstant](/en-US/docs/Web/API/AnalyserNode/smoothingTimeConstant)

A double value representing the averaging constant with the last analysis frame — basically, it makes the transition between values over time smoother.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[AnalyserNode.getFloatFrequencyData()](/en-US/docs/Web/API/AnalyserNode/getFloatFrequencyData)

Copies the current frequency data into a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) array passed into it.

[AnalyserNode.getByteFrequencyData()](/en-US/docs/Web/API/AnalyserNode/getByteFrequencyData)

Copies the current frequency data into a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) (unsigned byte array) passed into it.

[AnalyserNode.getFloatTimeDomainData()](/en-US/docs/Web/API/AnalyserNode/getFloatTimeDomainData)

Copies the current waveform, or time-domain, data into a [Float32Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) array passed into it.

[AnalyserNode.getByteTimeDomainData()](/en-US/docs/Web/API/AnalyserNode/getByteTimeDomainData)

Copies the current waveform, or time-domain, data into a [Uint8Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) (unsigned byte array) passed into it.

## [Examples](#examples)

Note: See the guide [Visualizations with Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API) for more information on creating audio visualizations.

### [Basic usage](#basic_usage)

The following example shows basic usage of an [AudioContext](/en-US/docs/Web/API/AudioContext) to create an `AnalyserNode`, then [requestAnimationFrame](/en-US/docs/Web/API/Window/requestAnimationFrame) and [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) to collect time domain data repeatedly and draw an "oscilloscope style" output of the current audio input. For more complete applied examples/information, check out our [Voice-change-O-matic](https://mdn.github.io/webaudio-examples/voice-change-o-matic/) demo (see [app.js lines 108-193](https://github.com/mdn/webaudio-examples/blob/main/voice-change-o-matic/scripts/app.js#L108-L193) for relevant code).

js

```
const audioCtx = new AudioContext();

// …

const analyser = audioCtx.createAnalyser();
analyser.fftSize = 2048;

const bufferLength = analyser.frequencyBinCount;
const dataArray = new Uint8Array(bufferLength);
analyser.getByteTimeDomainData(dataArray);

// Connect the source to be analyzed
source.connect(analyser);

// Get a canvas defined with ID "oscilloscope"
const canvas = document.getElementById("oscilloscope");
const canvasCtx = canvas.getContext("2d");

// draw an oscilloscope of the current audio source

function draw() {
  requestAnimationFrame(draw);

  analyser.getByteTimeDomainData(dataArray);

  canvasCtx.fillStyle = "rgb(200 200 200)";
  canvasCtx.fillRect(0, 0, canvas.width, canvas.height);

  canvasCtx.lineWidth = 2;
  canvasCtx.strokeStyle = "rgb(0 0 0)";

  canvasCtx.beginPath();

  const sliceWidth = (canvas.width * 1.0) / bufferLength;
  let x = 0;

  for (let i = 0; i < bufferLength; i++) {
    const v = dataArray[i] / 128.0;
    const y = (v * canvas.height) / 2;

    if (i === 0) {
      canvasCtx.moveTo(x, y);
    } else {
      canvasCtx.lineTo(x, y);
    }

    x += sliceWidth;
  }

  canvasCtx.lineTo(canvas.width, canvas.height / 2);
  canvasCtx.stroke();
}

draw();
```

## [Specifications](#specifications)

Specification
[Web Audio API# AnalyserNode](https://webaudio.github.io/web-audio-api/#AnalyserNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AnalyserNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/analysernode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnalyserNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fanalysernode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnalyserNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fanalysernode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff3c4fc42e8817d0b8f703cf83957c33cd5342019%0A*+Document+last+modified%3A+2024-10-08T03%3A44%3A01.000Z%0A%0A%3C%2Fdetails%3E)
