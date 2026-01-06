# AudioScheduledSourceNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioScheduledSourceNode&level=high)

The `AudioScheduledSourceNode` interface—part of the Web Audio API—is a parent interface for several types of audio source node interfaces which share the ability to be started and stopped, optionally at specified times. Specifically, this interface defines the [start()](/en-US/docs/Web/API/AudioScheduledSourceNode/start) and [stop()](/en-US/docs/Web/API/AudioScheduledSourceNode/stop) methods, as well as the [ended](/en-US/docs/Web/API/AudioScheduledSourceNode/ended_event) event.

Note: You can't create an `AudioScheduledSourceNode` object directly. Instead, use an interface which extends it, such as [AudioBufferSourceNode](/en-US/docs/Web/API/AudioBufferSourceNode), [OscillatorNode](/en-US/docs/Web/API/OscillatorNode) or [ConstantSourceNode](/en-US/docs/Web/API/ConstantSourceNode).

Unless stated otherwise, nodes based upon `AudioScheduledSourceNode` output silence when not playing (that is, before `start()` is called and after `stop()` is called). Silence is represented, as always, by a stream of samples with the value zero (0).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent interface, [AudioNode](/en-US/docs/Web/API/AudioNode).

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [AudioNode](/en-US/docs/Web/API/AudioNode), and adds the following methods:

[start()](/en-US/docs/Web/API/AudioScheduledSourceNode/start)

Schedules the node to begin playing the constant sound at the specified time. If no time is specified, the node begins playing immediately.

[stop()](/en-US/docs/Web/API/AudioScheduledSourceNode/stop)

Schedules the node to stop playing at the specified time. If no time is specified, the node stops playing at once.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[ended](/en-US/docs/Web/API/AudioScheduledSourceNode/ended_event)

Fired when the source node has stopped playing, either because it's reached a predetermined stop time, the full duration of the audio has been performed, or because the entire buffer has been played.

## [Specifications](#specifications)

Specification
[Web Audio API# AudioScheduledSourceNode](https://webaudio.github.io/web-audio-api/#AudioScheduledSourceNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [AudioNode](/en-US/docs/Web/API/AudioNode)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AudioScheduledSourceNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioscheduledsourcenode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioScheduledSourceNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioscheduledsourcenode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioScheduledSourceNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioscheduledsourcenode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fec1006afdf68a5808a48ab6301f9ccff3cd7ecc2%0A*+Document+last+modified%3A+2024-07-26T03%3A17%3A12.000Z%0A%0A%3C%2Fdetails%3E)
