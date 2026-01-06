# RTCDTMFSender

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDTMFSender&level=high)

The `RTCDTMFSender` interface provides a mechanism for transmitting [DTMF](/en-US/docs/Glossary/DTMF) codes on a [WebRTC](/en-US/docs/Web/API/WebRTC_API)[RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection). You gain access to the connection's `RTCDTMFSender` through the [RTCRtpSender.dtmf](/en-US/docs/Web/API/RTCRtpSender/dtmf) property on the audio track you wish to send DTMF with.

The primary purpose for WebRTC's DTMF support is to allow WebRTC-based communication clients to be connected to a [public-switched telephone network (PSTN)](https://en.wikipedia.org/wiki/Public_switched_telephone_network) or other legacy telephone service, including extant voice over IP (VoIP) services. For that reason, DTMF can't be used between two WebRTC-based devices, because there is no mechanism provided by WebRTC for receiving DTMF codes.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[RTCDTMFSender.canInsertDTMF](/en-US/docs/Web/API/RTCDTMFSender/canInsertDTMF)Read only

A boolean value which is `true` if the `RTCDTMFSender` is capable of sending DTMF tones, or `false` if it is not.

[RTCDTMFSender.toneBuffer](/en-US/docs/Web/API/RTCDTMFSender/toneBuffer)Read only

A string which contains the list of DTMF tones currently in the queue to be transmitted (tones which have already been played are no longer included in the string). See [toneBuffer](/en-US/docs/Web/API/RTCDTMFSender/toneBuffer) for details on the format of the tone buffer.

## [Instance methods](#instance_methods)

[RTCDTMFSender.insertDTMF()](/en-US/docs/Web/API/RTCDTMFSender/insertDTMF)

Given a string describing a set of DTMF codes and, optionally, the duration of and inter-tone gap between the tones, `insertDTMF()` starts sending the specified tones. Calling `insertDTMF()` replaces any already-pending tones from the `toneBuffer`. You can abort sending queued tones by specifying an empty string (`""`) as the set of tones to play.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[tonechange](/en-US/docs/Web/API/RTCDTMFSender/tonechange_event)

The `tonechange` event is sent to the `RTCDTMFSender` instance's event handler to indicate that a tone has either started or stopped playing.

## [Example](#example)

See the article [Using DTMF with WebRTC](/en-US/docs/Web/API/WebRTC_API/Using_DTMF) for a full example.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcdtmfsender](https://w3c.github.io/webrtc-pc/#rtcdtmfsender)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [Using DTMF with WebRTC](/en-US/docs/Web/API/WebRTC_API/Using_DTMF)
- [RTCRtpSender.dtmf](/en-US/docs/Web/API/RTCRtpSender/dtmf)
- [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)
- [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCDTMFSender/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcdtmfsender/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDTMFSender&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcdtmfsender%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDTMFSender%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcdtmfsender%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
