# RTCTransportStats

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTransportStats&level=not)

The `RTCTransportStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides information about the transport ([RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport) and its underlying [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport)) used by a particular candidate pair.

The BUNDLE feature is an SDP extension that allows negotiation to use a single transport for sending and receiving media described by multiple SDP media descriptions. If the remote endpoint is aware of this feature, all [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) and data channels are bundled onto a single transport at the completion of negotiation. This is true for current browsers, but if connecting to an older endpoint that is not BUNDLE-aware, then separate transports might be used for different media. The policy to use in the negotiation is configured in the [RTCPeerConnection constructor](/en-US/docs/Web/API/RTCPeerConnection/RTCPeerConnection).

These statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCTransportStats/type) of `transport`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[bytesReceived](/en-US/docs/Web/API/RTCTransportStats/bytesReceived)Optional

The total number of payload bytes received on this transport (bytes received, not including headers, padding or ICE connectivity checks).

[bytesSent](/en-US/docs/Web/API/RTCTransportStats/bytesSent)Optional

The total number of payload bytes sent on this transport (bytes sent, not including headers, padding or ICE connectivity checks).

[dtlsCipher](/en-US/docs/Web/API/RTCTransportStats/dtlsCipher)Optional

A string indicating the name of the cipher suite used for the DTLS transport, such as `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`.

[dtlsRole](/en-US/docs/Web/API/RTCTransportStats/dtlsRole)OptionalExperimental

A string indicating the DTLS role of the associated [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection). This is one of: `client`, `server`, `unknown` (before the DTLS negotiation starts).

[dtlsState](/en-US/docs/Web/API/RTCTransportStats/dtlsState)

A string indicating the current [state](/en-US/docs/Web/API/RTCDtlsTransport/state) of the underlying [RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport). This is one of: `new`, `connecting`, `connected`, `closed`, `failed`.

[iceLocalUsernameFragment](/en-US/docs/Web/API/RTCTransportStats/iceLocalUsernameFragment)OptionalExperimental

A string indicating the local username fragment that uniquely identifies the ICE interaction session managed by this transport.

[iceRole](/en-US/docs/Web/API/RTCTransportStats/iceRole)OptionalExperimental

A string indicating the ICE [role](/en-US/docs/Web/API/RTCIceTransport/role) of the underlying [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport). This is one of: `controlled`, `controlling`, or `unknown`.

[iceState](/en-US/docs/Web/API/RTCTransportStats/iceState)OptionalExperimental

A string indicating the current [state](/en-US/docs/Web/API/RTCIceTransport/state) of the underlying [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport). This is one of: `new`, `checking`, `connected`, `completed`, `disconnected`, `failed`, or `closed`.

[localCertificateId](/en-US/docs/Web/API/RTCTransportStats/localCertificateId)Optional

A string containing the id of the local certificate used by this transport. Only present for DTLS transports, and after DTLS has been negotiated.

[packetsReceived](/en-US/docs/Web/API/RTCTransportStats/packetsReceived)OptionalExperimental

The total number of packets received on this transport.

[packetsSent](/en-US/docs/Web/API/RTCTransportStats/packetsSent)OptionalExperimental

The total number of packets sent over this transport.

[remoteCertificateId](/en-US/docs/Web/API/RTCTransportStats/remoteCertificateId)Optional

A string containing the id or the remote certificate used by this transport. Only present for DTLS transports, and after DTLS has been negotiated.

[selectedCandidatePairChanges](/en-US/docs/Web/API/RTCTransportStats/selectedCandidatePairChanges)Optional

The number of times that the selected candidate pair of this transport has changed. The value is initially zero and increases whenever a candidate pair selected or lost.

[selectedCandidatePairId](/en-US/docs/Web/API/RTCTransportStats/selectedCandidatePairId)Optional

A string containing the unique identifier for the object that was inspected to produce the [RTCIceCandidatePairStats](/en-US/docs/Web/API/RTCIceCandidatePairStats) associated with this transport.

[srtpCipher](/en-US/docs/Web/API/RTCTransportStats/srtpCipher)Optional

A string indicating the descriptive name of the protection profile used for the [Secure Real-time Transport Protocol (SRTP)](/en-US/docs/Glossary/RTP) transport.

[tlsVersion](/en-US/docs/Web/API/RTCTransportStats/tlsVersion)Optional

A string containing the negotiated TLS version. This is present for DTLS transports, and only exists after DTLS has been negotiated.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCTransportStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCTransportStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCTransportStats/type)

A string with the value `"transport"`, indicating the type of statistics that the object contains.

## [Examples](#examples)

This example shows a function to return the transport statistics, or `null` if no statistics are provided.

The function waits for the result of a call to [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) and then iterates the returned [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) to get just the stats of type `"transport"`. It then returns the statistics, or `null`, using the data in the report.

js

```
async function numberOpenConnections (peerConnection) {
  const stats = await peerConnection.getStats();
  let transportStats = null;

  stats.forEach((report) => {
    if (report.type === "transport") {
      transportStats = report;
      break;
    }
  });

return transportStats
}
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-transport](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-transport)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCTransportStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtctransportstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTransportStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtctransportstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCTransportStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtctransportstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F185acd0fe4bd6d0f4a5c6d79fa46b1b748d09ea1%0A*+Document+last+modified%3A+2025-06-24T00%3A46%3A19.000Z%0A%0A%3C%2Fdetails%3E)
