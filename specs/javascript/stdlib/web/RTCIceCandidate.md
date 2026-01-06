# RTCIceCandidate

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidate&level=high)

The `RTCIceCandidate` interface—part of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API)—represents a candidate Interactive Connectivity Establishment ([ICE](/en-US/docs/Glossary/ICE)) configuration which may be used to establish an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

An ICE candidate describes the protocols and routing needed for WebRTC to be able to communicate with a remote device. When starting a WebRTC peer connection, typically a number of candidates are proposed by each end of the connection, until they mutually agree upon one which describes the connection they decide will be best. WebRTC then uses that candidate's details to initiate the connection.

For details on how the ICE process works, see [Lifetime of a WebRTC session](/en-US/docs/Web/API/WebRTC_API/Session_lifetime). The article [WebRTC connectivity](/en-US/docs/Web/API/WebRTC_API/Connectivity) provides additional useful details.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[RTCIceCandidate()](/en-US/docs/Web/API/RTCIceCandidate/RTCIceCandidate)

Creates an `RTCIceCandidate` object to represent a single ICE candidate, optionally configured based on a configuration object.

Note: For backwards compatibility, the constructor also accepts as input a string containing the value of the [candidate](/en-US/docs/Web/API/RTCIceCandidate/candidate) property instead of the configuration object.

## [Instance properties](#instance_properties)

[address](/en-US/docs/Web/API/RTCIceCandidate/address)Read only

A string containing the IP address of the candidate.

[candidate](/en-US/docs/Web/API/RTCIceCandidate/candidate)Read only

A string representing the transport address for the candidate that can be used for connectivity checks. The format of this address is a `candidate-attribute` as defined in [RFC 5245](https://datatracker.ietf.org/doc/html/rfc5245). This string is empty (`""`) if the `RTCIceCandidate` is an "end of candidates" indicator.

[component](/en-US/docs/Web/API/RTCIceCandidate/component)Read only

A string which indicates whether the candidate is an RTP or an RTCP candidate; its value is either `rtp` or `rtcp`, and is derived from the `"component-id"` field in the `candidate` a-line string.

[foundation](/en-US/docs/Web/API/RTCIceCandidate/foundation)Read only

Returns a string containing a unique identifier that is the same for any candidates of the same type, share the same base (the address from which the ICE agent sent the candidate), and come from the same [STUN](/en-US/docs/Glossary/STUN) server. This is used to help optimize ICE performance while prioritizing and correlating candidates that appear on multiple [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) objects.

[port](/en-US/docs/Web/API/RTCIceCandidate/port)Read only

An integer value indicating the candidate's port number.

[priority](/en-US/docs/Web/API/RTCIceCandidate/priority)Read only

A long integer value indicating the candidate's priority.

[protocol](/en-US/docs/Web/API/RTCIceCandidate/protocol)Read only

A string indicating whether the candidate's protocol is `"tcp"` or `"udp"`.

[relatedAddress](/en-US/docs/Web/API/RTCIceCandidate/relatedAddress)Read only

If the candidate is derived from another candidate, `relatedAddress` is a string containing that host candidate's IP address. For host candidates, this value is `null`.

[relatedPort](/en-US/docs/Web/API/RTCIceCandidate/relatedPort)Read only

For a candidate that is derived from another, such as a relay or reflexive candidate, the `relatedPort` is a number indicating the port number of the candidate from which this candidate is derived. For host candidates, the `relatedPort` property is `null`.

[sdpMid](/en-US/docs/Web/API/RTCIceCandidate/sdpMid)Read only

A string specifying the candidate's media stream identification tag which uniquely identifies the media stream within the component with which the candidate is associated, or `null` if no such association exists.

[sdpMLineIndex](/en-US/docs/Web/API/RTCIceCandidate/sdpMLineIndex)Read only

If not `null`, `sdpMLineIndex` indicates the zero-based index number of the media description (as defined in [RFC 4566](https://datatracker.ietf.org/doc/html/rfc4566)) in the [SDP](/en-US/docs/Glossary/SDP) with which the candidate is associated.

[tcpType](/en-US/docs/Web/API/RTCIceCandidate/tcpType)Read only

If `protocol` is `"tcp"`, `tcpType` represents the type of TCP candidate. Otherwise, `tcpType` is `null`.

[type](/en-US/docs/Web/API/RTCIceCandidate/type)Read only

A string indicating the type of candidate as one of the strings listed on [RTCIceCandidate.type](/en-US/docs/Web/API/RTCIceCandidate/type#value).

[usernameFragment](/en-US/docs/Web/API/RTCIceCandidate/usernameFragment)Read only

A string containing a randomly-generated username fragment ("ice-ufrag") which ICE uses for message integrity along with a randomly-generated password ("ice-pwd"). You can use this string to verify generations of ICE generation; each generation of the same ICE process will use the same `usernameFragment`, even across ICE restarts.

## [Instance methods](#instance_methods)

[toJSON()](/en-US/docs/Web/API/RTCIceCandidate/toJSON)

Returns a [JSON](/en-US/docs/Glossary/JSON) representation of the `RTCIceCandidate`'s current configuration. The format of the representation is the same as the `candidateInfo` object that can optionally be passed to the [RTCIceCandidate()](/en-US/docs/Web/API/RTCIceCandidate/RTCIceCandidate) constructor to configure a candidate.

## [Examples](#examples)

For examples, see the article [Signaling and video calling](/en-US/docs/Web/API/WebRTC_API/Signaling_and_video_calling), which demonstrates the entire process.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcicecandidate-interface](https://w3c.github.io/webrtc-pc/#rtcicecandidate-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCIceCandidate/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcicecandidate/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcicecandidate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcicecandidate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
