# RTCIceCandidatePairStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidatePairStats&level=high)

The `RTCIceCandidatePairStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to report statistics that provide insight into the quality and performance of an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) while connected and configured as described by the specified pair of [ICE](/en-US/docs/Glossary/ICE) candidates.

The statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find an entry with the [type](/en-US/docs/Web/API/RTCIceCandidatePairStats/type) of `"candidate-pair"`.

## In this article

- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[availableIncomingBitrate](/en-US/docs/Web/API/RTCIceCandidatePairStats/availableIncomingBitrate)Optional

A number representing the available inbound capacity of the network. This reports the total number of bits per second available for all of the candidate pair's incoming [RTP](/en-US/docs/Glossary/RTP) streams. It does not take into account the size of the Internet Protocol (IP) overhead, nor any other transport layers such as [TCP](/en-US/docs/Glossary/TCP) or [UDP](/en-US/docs/Glossary/UDP).

[availableOutgoingBitrate](/en-US/docs/Web/API/RTCIceCandidatePairStats/availableOutgoingBitrate)Optional

A number representing the approximate available outbound capacity of the network. This reports the total number of bits per second available for all of the candidate pair's outgoing [RTP](/en-US/docs/Glossary/RTP) streams. It does not take into account the size of the IP overhead, nor any other transport layers such as [TCP](/en-US/docs/Glossary/TCP) or [UDP](/en-US/docs/Glossary/UDP).

[bytesDiscardedOnSend](/en-US/docs/Web/API/RTCIceCandidatePairStats/bytesDiscardedOnSend)OptionalExperimental

An integer representing the total number of bytes discarded due to socket errors on this candidate pair.

[bytesReceived](/en-US/docs/Web/API/RTCIceCandidatePairStats/bytesReceived)Optional

An integer representing the total number of payload bytes received on this candidate pair.

[bytesSent](/en-US/docs/Web/API/RTCIceCandidatePairStats/bytesSent)Optional

An integer representing the total number of payload bytes sent on this candidate pair (the total number of bytes sent excluding any headers, padding, or other protocol overhead).

[consentRequestsSent](/en-US/docs/Web/API/RTCIceCandidatePairStats/consentRequestsSent)OptionalExperimental

An integer representing the total number of [STUN](/en-US/docs/Web/API/WebRTC_API/Protocols#stun) consent requests sent on this candidate pair.

[currentRoundTripTime](/en-US/docs/Web/API/RTCIceCandidatePairStats/currentRoundTripTime)Optional

A number representing the total time, in seconds, that elapsed between the most recently-sent STUN request and the response being received. This may be based upon requests that were involved in confirming permission to open the connection.

[lastPacketReceivedTimestamp](/en-US/docs/Web/API/RTCIceCandidatePairStats/lastPacketReceivedTimestamp)Optional

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) value indicating the time at which the last packet was received by the local peer from the remote peer for this candidate pair. Timestamps are not recorded for STUN packets.

[lastPacketSentTimestamp](/en-US/docs/Web/API/RTCIceCandidatePairStats/lastPacketSentTimestamp)Optional

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) value indicating the time at which the last packet was sent from the local peer to the remote peer for this candidate pair. Timestamps are not recorded for STUN packets.

[localCandidateId](/en-US/docs/Web/API/RTCIceCandidatePairStats/localCandidateId)Optional

A string representing the unique ID corresponding to the [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate) from the data included in the [RTCIceCandidateStats](/en-US/docs/Web/API/RTCIceCandidateStats) object providing statistics for the candidate pair's local candidate.

[nominated](/en-US/docs/Web/API/RTCIceCandidatePairStats/nominated)Optional

A Boolean value which, if `true`, indicates that the candidate pair described by this object is one which has been proposed for use, and will be (or was) used if its priority is the highest among the nominated candidate pairs. See [RFC 5245, section 7.1.3.2.4](https://datatracker.ietf.org/doc/html/rfc5245#section-7.1.3.2.4) for details.

[packetsDiscardedOnSend](/en-US/docs/Web/API/RTCIceCandidatePairStats/packetsDiscardedOnSend)OptionalExperimental

An integer representing the total number of packets discarded due to socket errors on this candidate pair.

[packetsReceived](/en-US/docs/Web/API/RTCIceCandidatePairStats/packetsReceived)OptionalExperimental

An integer representing the total number of packets received on this candidate pair.

[packetsSent](/en-US/docs/Web/API/RTCIceCandidatePairStats/packetsSent)OptionalExperimental

An integer representing the total number of packets sent on this candidate pair.

[remoteCandidateId](/en-US/docs/Web/API/RTCIceCandidatePairStats/remoteCandidateId)Optional

A string containing a unique ID corresponding to the remote candidate from which data was taken to construct the `RTCIceCandidateStats` object describing the remote end of the connection.

[requestsReceived](/en-US/docs/Web/API/RTCIceCandidatePairStats/requestsReceived)Optional

An integer representing the total number of connectivity check requests that have been received, including retransmissions. This value includes both connectivity checks and STUN consent checks.

[requestsSent](/en-US/docs/Web/API/RTCIceCandidatePairStats/requestsSent)Optional

An integer representing the total number of connectivity check requests that have been sent, not including retransmissions.

[responsesReceived](/en-US/docs/Web/API/RTCIceCandidatePairStats/responsesReceived)Optional

An integer representing the total number of connectivity check responses that have been received.

[responsesSent](/en-US/docs/Web/API/RTCIceCandidatePairStats/responsesSent)Optional

An integer representing the total number of connectivity check responses that have been sent. This includes both connectivity check requests and STUN consent requests.

[state](/en-US/docs/Web/API/RTCIceCandidatePairStats/state)Optional

A string which indicates the state of the connection between the two candidates.

[totalRoundTripTime](/en-US/docs/Web/API/RTCIceCandidatePairStats/totalRoundTripTime)Optional

A number indicating the total time, in seconds, that has elapsed between sending STUN requests and receiving responses to them, for all such requests made to date on this candidate pair. This includes both connectivity check and consent check requests. You can compute the average round trip time (RTT) by dividing this value by [responsesReceived](/en-US/docs/Web/API/RTCIceCandidatePairStats/responsesReceived).

[transportId](/en-US/docs/Web/API/RTCIceCandidatePairStats/transportId)Optional

A string that uniquely identifies the [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) that was inspected to obtain the transport-related statistics (as found in [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats)) used in generating this object.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCIceCandidatePairStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCIceCandidatePairStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCIceCandidatePairStats/type)

A string with the value `"candidate-pair"`, indicating the type of statistics that the object contains.

### [Deprecated properties](#deprecated_properties)

The following properties have been removed from the specification and should no longer be used. You should update any existing code to avoid using them as soon as is practical. Check the [compatibility table](#browser_compatibility) for details on which browsers support them and in which versions.

[priority](/en-US/docs/Web/API/RTCIceCandidatePairStats/priority)DeprecatedOptionalNon-standard

An integer value indicating the candidate pair's priority.

[readable](/en-US/docs/Web/API/RTCIceCandidatePairStats/readable)DeprecatedOptionalNon-standard

A Boolean value indicating whether or not data can be sent over the connection described by the candidate pair.

[writable](/en-US/docs/Web/API/RTCIceCandidatePairStats/writable)DeprecatedOptionalNon-standard

A Boolean value indicating whether or not data can be received on the connection described by the candidate pair.

### [Non-standard properties](#non-standard_properties)

[selected](/en-US/docs/Web/API/RTCIceCandidatePairStats/selected)Non-standardOptional

A Firefox-specific Boolean value which is `true` if the candidate pair described by this object is the one currently in use. The spec-compliant way to determine the selected candidate pair is to look for a stats object of type `transport`, which is an [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats) object. That object's [selectedCandidatePairId](/en-US/docs/Web/API/RTCTransportStats/selectedCandidatePairId) property indicates whether or not the specified transport is the one being used.

## [Usage notes](#usage_notes)

The currently-active ICE candidate pair—if any—can be obtained by calling the [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) method [getSelectedCandidatePair()](/en-US/docs/Web/API/RTCIceTransport/getSelectedCandidatePair), which returns an [RTCIceCandidatePair](/en-US/docs/Web/API/RTCIceCandidatePair) object, or `null` if there isn't a pair selected. The active candidate pair describes the current configuration of the two ends of the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

Any candidate pair that isn't the active pair of candidates for a transport gets deleted if the [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) performs an ICE restart, at which point the [state](/en-US/docs/Web/API/RTCIceTransport/state) of the ICE transport returns to `new` and negotiation starts once again. For more information, see [ICE restart](/en-US/docs/Web/API/WebRTC_API/Session_lifetime#ice_restart).

## [Example](#example)

This example computes the average time elapsed between connectivity checks.

js

```
if (rtcStats && rtcStats.type === "candidate-pair") {
  let elapsed =
    (rtcStats.lastRequestTimestamp - rtcStats.firstRequestTimestamp) /
    rtcStats.requestsSent;

  console.log(`Average time between ICE connectivity checks: ${elapsed} ms.`);
}
```

The code begins by looking at `rtcStats` to see if its [type](/en-US/docs/Web/API/RTCIceCandidatePairStats/type) is `candidate-pair`. If it is, then we know that `rtcStats` is in fact an `RTCIceCandidatePairStats` object. We can then compute the average time elapsed between STUN connectivity checks and log that information.

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-candidate-pair](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-candidate-pair)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCIceCandidatePairStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcicecandidatepairstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidatePairStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcicecandidatepairstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidatePairStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcicecandidatepairstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
