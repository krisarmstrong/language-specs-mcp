# ScriptProcessorNode

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

The `ScriptProcessorNode` interface allows the generation, processing, or analyzing of audio using JavaScript.

Note: This feature was replaced by [AudioWorklets](/en-US/docs/Web/API/AudioWorklet) and the [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) interface.

The `ScriptProcessorNode` interface is an [AudioNode](/en-US/docs/Web/API/AudioNode) audio-processing module that is linked to two buffers, one containing the input audio data, one containing the processed output audio data. An event, implementing the [AudioProcessingEvent](/en-US/docs/Web/API/AudioProcessingEvent) interface, is sent to the object each time the input buffer contains new data, and the event handler terminates when it has filled the output buffer with data.

The size of the input and output buffer are defined at the creation time, when the [BaseAudioContext.createScriptProcessor](/en-US/docs/Web/API/BaseAudioContext/createScriptProcessor) method is called (both are defined by [BaseAudioContext.createScriptProcessor](/en-US/docs/Web/API/BaseAudioContext/createScriptProcessor)'s `bufferSize` parameter). The buffer size must be a power of 2 between `256` and `16384`, that is `256`, `512`, `1024`, `2048`, `4096`, `8192` or `16384`. Small numbers lower the latency, but large number may be necessary to avoid audio breakup and glitches.

If the buffer size is not defined, which is recommended, the browser will pick one that its heuristic deems appropriate.

Number of inputs`1`Number of outputs`1`Channel count mode`"max"`Channel count`2` (not used in the default count mode)Channel interpretation`"speakers"`

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[ScriptProcessorNode.bufferSize](/en-US/docs/Web/API/ScriptProcessorNode/bufferSize)Read onlyDeprecated

Returns an integer representing both the input and output buffer size. Its value can be a power of 2 value in the range `256` – `16384`.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[audioprocess](/en-US/docs/Web/API/ScriptProcessorNode/audioprocess_event)Deprecated

Fired when an input buffer of a `ScriptProcessorNode` is ready to be processed. Also available via the `onaudioprocess` event handler property.

## [Examples](#examples)

See [BaseAudioContext.createScriptProcessor()](/en-US/docs/Web/API/BaseAudioContext/createScriptProcessor#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# dom-scriptprocessornode-buffersize](https://webaudio.github.io/web-audio-api/#dom-scriptprocessornode-buffersize)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ScriptProcessorNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/scriptprocessornode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScriptProcessorNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscriptprocessornode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScriptProcessorNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscriptprocessornode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F941ade970fd7ebad52af692b6ac27cfd96f94100%0A*+Document+last+modified%3A+2025-05-28T14%3A25%3A52.000Z%0A%0A%3C%2Fdetails%3E)
