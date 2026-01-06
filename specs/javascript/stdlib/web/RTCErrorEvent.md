# RTCErrorEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCErrorEvent&level=not)

The WebRTC API's `RTCErrorEvent` interface represents an error sent to a WebRTC object. It's based on the standard [Event](/en-US/docs/Web/API/Event) interface, but adds RTC-specific information describing the error, as shown below.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Description](#description)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

`RTCErrorEvent()`

Creates and returns a new `RTCErrorEvent` object.

## [Instance properties](#instance_properties)

In addition to the standard properties available on the [Event](/en-US/docs/Web/API/Event) interface, `RTCErrorEvent` also includes the following:

[error](/en-US/docs/Web/API/RTCErrorEvent/error)Read only

An [RTCError](/en-US/docs/Web/API/RTCError) object specifying the error which occurred; this object includes the type of error that occurred, information about where the error occurred (such as which line number in the [SDP](/en-US/docs/Glossary/SDP) or what [SCTP](/en-US/docs/Glossary/SCTP) cause code was at issue).

## [Instance methods](#instance_methods)

No additional methods are provided beyond any found on the parent interface, [Event](/en-US/docs/Web/API/Event).

## [Description](#description)

There are other data types used for error events in WebRTC, as needed for errors with special information sharing requirements. The most common of these is probably [RTCPeerConnectionIceErrorEvent](/en-US/docs/Web/API/RTCPeerConnectionIceErrorEvent), used by the [icecandidateerror](/en-US/docs/Web/API/RTCPeerConnection/icecandidateerror_event) event, which signals an error that has occurred while gathering ICE candidates during connection negotiation.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtcerrorevent](https://w3c.github.io/webrtc-pc/#dom-rtcerrorevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- WebRTC API
- [RTCError](/en-US/docs/Web/API/RTCError)
- The `error` event occurs on the following interfaces: [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) and [RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport)
- [RTCPeerConnectionIceErrorEvent](/en-US/docs/Web/API/RTCPeerConnectionIceErrorEvent)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCErrorEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcerrorevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCErrorEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcerrorevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCErrorEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcerrorevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11f58a4cd8758f89056900a6fb7c21e2d42fa6f1%0A*+Document+last+modified%3A+2024-08-06T16%3A16%3A02.000Z%0A%0A%3C%2Fdetails%3E)
