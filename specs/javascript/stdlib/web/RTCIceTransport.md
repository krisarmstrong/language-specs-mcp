# RTCIceTransport

 Baseline  2024  * Newly available

 Since ⁨April 2024⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceTransport&level=low)

The `RTCIceTransport` interface provides access to information about the [ICE](/en-US/docs/Glossary/ICE) transport layer over which the data is being sent and received. This is particularly useful if you need to access state information about the connection.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

The `RTCIceTransport` interface inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget). It also offers the following properties:

[component](/en-US/docs/Web/API/RTCIceTransport/component)Read only

The ICE component being used by the transport. The value is one of the strings from the `RTCIceTransport` enumerated type: ["RTP"](/en-US/docs/Glossary/RTP) or `"RTSP"`.

[gatheringState](/en-US/docs/Web/API/RTCIceTransport/gatheringState)Read only

A string indicating which current gathering state of the ICE agent: `"new"`, `"gathering"`, or `"complete"`.

[role](/en-US/docs/Web/API/RTCIceTransport/role)Read only

Returns a string whose value is either `"controlling"` or `"controlled"`; this indicates whether the ICE agent is the one that makes the final decision as to the candidate pair to use or not.

[state](/en-US/docs/Web/API/RTCIceTransport/state)Read only

A string indicating what the current state of the ICE agent is. The value of `state` can be used to determine whether the ICE agent has made an initial connection using a viable candidate pair (`"connected"`), made its final selection of candidate pairs (`"completed"`), or in an error state (`"failed"`), among other states.

## [Instance methods](#instance_methods)

Also includes methods from [EventTarget](/en-US/docs/Web/API/EventTarget), the parent interface.

[getLocalCandidates()](/en-US/docs/Web/API/RTCIceTransport/getLocalCandidates)

Returns an array of [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate) objects, each describing one of the ICE candidates that have been gathered so far for the local device. These are the same candidates which have already been sent to the remote peer by sending an [icecandidate](/en-US/docs/Web/API/RTCPeerConnection/icecandidate_event) event to the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) for transmission.

[getLocalParameters()](/en-US/docs/Web/API/RTCIceTransport/getLocalParameters)

Returns a [RTCIceParameters](/en-US/docs/Web/API/RTCIceParameters) object describing the ICE parameters established by a call to the [RTCPeerConnection.setLocalDescription()](/en-US/docs/Web/API/RTCPeerConnection/setLocalDescription) method. Returns `null` if parameters have not yet been received.

[getRemoteCandidates()](/en-US/docs/Web/API/RTCIceTransport/getRemoteCandidates)

Returns an array of [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate) objects, one for each of the remote device's ICE candidates that have been received by the local end of the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) and delivered to ICE by calling [addIceCandidate()](/en-US/docs/Web/API/RTCPeerConnection/addIceCandidate).

[getRemoteParameters()](/en-US/docs/Web/API/RTCIceTransport/getRemoteParameters)

Returns a [RTCIceParameters](/en-US/docs/Web/API/RTCIceParameters) object containing the ICE parameters for the remote device, as set by a call to [RTCPeerConnection.setRemoteDescription()](/en-US/docs/Web/API/RTCPeerConnection/setRemoteDescription). If `setRemoteDescription()` hasn't been called yet, the return value is `null`.

[getSelectedCandidatePair()](/en-US/docs/Web/API/RTCIceTransport/getSelectedCandidatePair)

Returns a [RTCIceCandidatePair](/en-US/docs/Web/API/RTCIceCandidatePair) object that identifies the two candidates—one for each end of the connection—that have been selected so far. It's possible that a better pair will be found and selected later; if you need to keep up with this, watch for the [selectedcandidatepairchange](/en-US/docs/Web/API/RTCIceTransport/selectedcandidatepairchange_event) event. If no candidate pair has been selected yet, the return value is `null`.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[gatheringstatechange](/en-US/docs/Web/API/RTCIceTransport/gatheringstatechange_event)

Sent to the `RTCIceTransport` object to indicate that the value of the [gatheringState](/en-US/docs/Web/API/RTCIceTransport/gatheringState) property has changed, indicating a change in this transport's ICE candidate negotiation process. Also available through the [ongatheringstatechange](/en-US/docs/Web/API/RTCIceTransport/gatheringstatechange_event) event handler property.

[selectedcandidatepairchange](/en-US/docs/Web/API/RTCIceTransport/selectedcandidatepairchange_event)

Sent to the `RTCIceTransport` when a new, better pair of candidates has been selected to describe the connectivity between the two peers. This occurs during negotiation or renegotiation, including after an ICE restart, which reuses the existing `RTCIceTransport` objects. The current candidate pair can be obtained using [getSelectedCandidatePair()](/en-US/docs/Web/API/RTCIceTransport/getSelectedCandidatePair). Also available using the [onselectedcandidatepairchange](/en-US/docs/Web/API/RTCIceTransport/selectedcandidatepairchange_event) event handler property.

[statechange](/en-US/docs/Web/API/RTCIceTransport/statechange_event)

Sent to the `RTCIceTransport` instance when the value of the [state](/en-US/docs/Web/API/RTCIceTransport/state) property has changed, indicating that the ICE gathering process has changed state. Also available through the [onstatechange](/en-US/docs/Web/API/RTCIceTransport/statechange_event) event handler property.

## [Examples](#examples)

tbd

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtcicetransport](https://w3c.github.io/webrtc-pc/#dom-rtcicetransport)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCIceTransport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcicetransport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceTransport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcicetransport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceTransport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcicetransport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
