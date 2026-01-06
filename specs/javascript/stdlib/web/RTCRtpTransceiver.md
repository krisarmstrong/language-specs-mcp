# RTCRtpTransceiver

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨October 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpTransceiver&level=high)

The WebRTC interface `RTCRtpTransceiver` describes a permanent pairing of an [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) and an [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver), along with some shared state.

Each [SDP](/en-US/docs/Glossary/SDP) media section describes one bidirectional SRTP ("Secure Real Time Protocol") stream (excepting the media section for [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel), if present). This pairing of send and receive SRTP streams is significant for some applications, so `RTCRtpTransceiver` is used to represent this pairing, along with other important state from the media section. Each non-disabled SRTP media section is always represented by exactly one transceiver.

A transceiver is uniquely identified using its [mid](/en-US/docs/Web/API/RTCRtpTransceiver/mid) property, which is the same as the media ID (`mid`) of its corresponding m-line. An `RTCRtpTransceiver` is associated with an m-line if its `mid` is non-null; otherwise it's considered disassociated.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[currentDirection](/en-US/docs/Web/API/RTCRtpTransceiver/currentDirection)Read only

A read-only string which indicates the transceiver's current negotiated directionality, or `null` if the transceiver has never participated in an exchange of offers and answers. To change the transceiver's directionality, set the value of the [direction](/en-US/docs/Web/API/RTCRtpTransceiver/direction) property.

[direction](/en-US/docs/Web/API/RTCRtpTransceiver/direction)

A string which is used to set the transceiver's desired direction.

[mid](/en-US/docs/Web/API/RTCRtpTransceiver/mid)Read only

The media ID of the m-line associated with this transceiver. This association is established, when possible, whenever either a local or remote description is applied. This field is `null` if neither a local or remote description has been applied, or if its associated m-line is rejected by either a remote offer or any answer.

[receiver](/en-US/docs/Web/API/RTCRtpTransceiver/receiver)Read only

The [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) object that handles receiving and decoding incoming media.

[sender](/en-US/docs/Web/API/RTCRtpTransceiver/sender)Read only

The [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) object responsible for encoding and sending data to the remote peer.

[stopped](/en-US/docs/Web/API/RTCRtpTransceiver/stopped)Deprecated

Indicates whether or not sending and receiving using the paired `RTCRtpSender` and `RTCRtpReceiver` has been permanently disabled, either due to SDP offer/answer, or due to a call to [stop()](/en-US/docs/Web/API/RTCRtpTransceiver/stop).

## [Instance methods](#instance_methods)

[setCodecPreferences()](/en-US/docs/Web/API/RTCRtpTransceiver/setCodecPreferences)

Configures the transceiver's preferred list of codecs, overriding [user agent](/en-US/docs/Glossary/User_agent) settings.

[stop()](/en-US/docs/Web/API/RTCRtpTransceiver/stop)

Permanently stops the `RTCRtpTransceiver`. The associated sender stops sending data, and the associated receiver likewise stops receiving and decoding incoming data.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcrtptransceiver-interface](https://w3c.github.io/webrtc-pc/#rtcrtptransceiver-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [Introduction to the Real-time Transport Protocol (RTP)](/en-US/docs/Web/API/WebRTC_API/Intro_to_RTP)
- [RTCPeerConnection.addTrack()](/en-US/docs/Web/API/RTCPeerConnection/addTrack) and [RTCPeerConnection.addTransceiver()](/en-US/docs/Web/API/RTCPeerConnection/addTransceiver) both create transceivers
- [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) and [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 17, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCRtpTransceiver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcrtptransceiver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpTransceiver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcrtptransceiver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpTransceiver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcrtptransceiver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe82d46feb66ed523ed8f74bd0bd6f4153c87acbb%0A*+Document+last+modified%3A+2024-06-17T05%3A53%3A24.000Z%0A%0A%3C%2Fdetails%3E)
