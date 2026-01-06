# RTCDTMFToneChangeEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDTMFToneChangeEvent&level=high)

The `RTCDTMFToneChangeEvent` interface represents events sent to indicate that [DTMF](/en-US/docs/Glossary/DTMF) tones have started or finished playing. This interface is used by the [tonechange](/en-US/docs/Web/API/RTCDTMFSender/tonechange_event) event.

## In this article

- [Instance properties](#instance_properties)
- [Constructors](#constructors)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

In addition to the properties of [Event](/en-US/docs/Web/API/Event), this interface offers the following:

[RTCDTMFToneChangeEvent.tone](/en-US/docs/Web/API/RTCDTMFToneChangeEvent/tone)Read only

A string specifying the tone which has begun playing, or an empty string (`""`) if the previous tone has finished playing.

## [Constructors](#constructors)

[RTCDTMFToneChangeEvent()](/en-US/docs/Web/API/RTCDTMFToneChangeEvent/RTCDTMFToneChangeEvent)

Returns a new `RTCDTMFToneChangeEvent`. It takes two parameters, the first being a string representing the type of the event (always `"tonechange"`); the second a dictionary containing the initial state of the properties of the event.

## [Instance methods](#instance_methods)

Supports the methods defined in [Event](/en-US/docs/Web/API/Event). There are no additional methods.

## [Examples](#examples)

This snippet is derived loosely from the full, working example you'll find in the section on [When a tone finishes playing](/en-US/docs/Web/API/WebRTC_API/Using_DTMF#when_a_tone_finishes_playing). It appends each tone to a display box as it's played, and, once all tones have been sent, re-enabled a previously-disabled "Send" button, allowing the next DTMF string to be entered.

js

```
dtmfSender.addEventListener("change", (event) => {
  if (event.tone !== "") {
    dialStringBox.innerText += event.tone;
  } else {
    sendDTMFButton.disabled = false;
  }
});
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtcdtmftonechangeevent](https://w3c.github.io/webrtc-pc/#dom-rtcdtmftonechangeevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- Its usual target: [RTCDTMFSender](/en-US/docs/Web/API/RTCDTMFSender).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCDTMFToneChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcdtmftonechangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDTMFToneChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcdtmftonechangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDTMFToneChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcdtmftonechangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff71683f74da0078d9371c4d0c1ff9d3898fc7b59%0A*+Document+last+modified%3A+2025-09-19T15%3A38%3A24.000Z%0A%0A%3C%2Fdetails%3E)
