# RTCPeerConnectionIceErrorEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionIceErrorEvent&level=not)

The `RTCPeerConnectionIceErrorEvent` interface—based upon the [Event](/en-US/docs/Web/API/Event) interface—provides details pertaining to an [ICE](/en-US/docs/Glossary/ICE) error announced by sending an [icecandidateerror](/en-US/docs/Web/API/RTCPeerConnection/icecandidateerror_event) event to the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) object.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`RTCPeerConnectionIceErrorEvent()`

Creates and returns a new `RTCPeerConnectionIceErrorEvent` object, with its `type` and other properties initialized as specified in the parameters. You will not normally create an object of this type yourself.

## [Instance properties](#instance_properties)

The `RTCPeerConnectionIceErrorEvent` interface includes the properties found on the [Event](/en-US/docs/Web/API/Event) interface, as well as the following properties:

[address](/en-US/docs/Web/API/RTCPeerConnectionIceErrorEvent/address)Read only

A string providing the local IP address used to communicate with the [STUN](/en-US/docs/Glossary/STUN) or [TURN](/en-US/docs/Glossary/TURN) server being used to negotiate the connection, or `null` if the local IP address has not yet been exposed as part of a local ICE candidate.

`errorCode`Read only

An unsigned integer value stating the numeric [STUN error code](https://www.iana.org/assignments/stun-parameters/stun-parameters.xhtml#stun-parameters-6) returned by the STUN or TURN server. If no host candidate can reach the server, this property is set to the number 701, which is outside the range of valid STUN error codes. The 701 error is fired only once per server URL, and only while the [iceGatheringState](/en-US/docs/Web/API/RTCPeerConnection/iceGatheringState) is `gathering`.

`errorText`Read only

A string containing the STUN reason text returned by the STUN or TURN server. If communication with the STUN or TURN server couldn't be established at all, this string will be a browser-specific string explaining the error.

`port`Read only

An unsigned integer value giving the port number over which communication with the STUN or TURN server is taking place, using the IP address given in `address`. `null` if the connection hasn't been established (that is, if `address` is `null`).

`url`Read only

A string indicating the URL of the STUN or TURN server with which the error occurred.

## [Instance methods](#instance_methods)

`RTCPeerConnectionIceErrorEvent` has no methods other than any provided by the parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

TBD

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcpeerconnectioniceerrorevent](https://w3c.github.io/webrtc-pc/#rtcpeerconnectioniceerrorevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 16, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCPeerConnectionIceErrorEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcpeerconnectioniceerrorevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionIceErrorEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcpeerconnectioniceerrorevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionIceErrorEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcpeerconnectioniceerrorevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F00f46adb5616d826821d63b11eac285faf1cf4a5%0A*+Document+last+modified%3A+2024-10-16T07%3A58%3A28.000Z%0A%0A%3C%2Fdetails%3E)
