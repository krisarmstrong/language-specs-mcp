# RTCIceParameters

The `RTCIceParameters` dictionary specifies the username fragment and password assigned to an [ICE](/en-US/docs/Glossary/ICE) session.

During ICE negotiation, each peer's username fragment and password are recorded in an `RTCIceParameters` object, which can be obtained from the [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) by calling its [getLocalParameters()](/en-US/docs/Web/API/RTCIceTransport/getLocalParameters) or [getRemoteParameters()](/en-US/docs/Web/API/RTCIceTransport/getRemoteParameters) method, depending on which end interests you.

## In this article

- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)

## [Instance properties](#instance_properties)

[usernameFragment](/en-US/docs/Web/API/RTCIceParameters/usernameFragment)

A string specifying the value of the ICE session's username fragment field, `ufrag`.

[password](/en-US/docs/Web/API/RTCIceParameters/password)

A string specifying the session's password string.

## [Usage notes](#usage_notes)

The username fragment and password uniquely identify the remote peer for the duration of the ICE session, and are used to both ensure security and to avoid crosstalk across multiple ongoing ICE sessions. See [RTCIceCandidate.usernameFragment](/en-US/docs/Web/API/RTCIceCandidate/usernameFragment) for further information.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtciceparameters](https://w3c.github.io/webrtc-pc/#rtciceparameters)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCIceParameters/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtciceparameters/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceParameters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtciceparameters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceParameters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtciceparameters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa0719c8102153b8bfc89f9c82126349e1db69461%0A*+Document+last+modified%3A+2025-03-30T20%3A55%3A04.000Z%0A%0A%3C%2Fdetails%3E)
