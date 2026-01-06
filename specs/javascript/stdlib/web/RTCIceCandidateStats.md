# RTCIceCandidateStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨February 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidateStats&level=high)

The `RTCIceCandidateStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to report statistics related to an [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate).

The statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCIceCandidateStats/type) of `local-candidate`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[address](/en-US/docs/Web/API/RTCIceCandidateStats/address)Optional

A string containing the address of the candidate. This value may be an IPv4 address, an IPv6 address, or a fully-qualified domain name. This property was previously named `ip` and only accepted IP addresses. Corresponds to [RTCIceCandidate.address](/en-US/docs/Web/API/RTCIceCandidate/address).

[candidateType](/en-US/docs/Web/API/RTCIceCandidateStats/candidateType)

A string matching one of the values in [RTCIceCandidate.type](/en-US/docs/Web/API/RTCIceCandidate/type#value), indicating what kind of candidate the object provides statistics for.

[deleted](/en-US/docs/Web/API/RTCIceCandidateStats/deleted)

A boolean indicating whether or not the candidate has been deleted or released.

[foundation](/en-US/docs/Web/API/RTCIceCandidateStats/foundation)OptionalExperimental

A string that uniquely identifies the candidate across multiple transports. Corresponds to [RTCIceCandidate.foundation](/en-US/docs/Web/API/RTCIceCandidate/foundation).

[port](/en-US/docs/Web/API/RTCIceCandidateStats/port)Optional

The network port number used by the candidate. Corresponds to [RTCIceCandidate.port](/en-US/docs/Web/API/RTCIceCandidate/port).

[priority](/en-US/docs/Web/API/RTCIceCandidateStats/priority)Optional

The candidate's priority. Corresponds to [RTCIceCandidate.priority](/en-US/docs/Web/API/RTCIceCandidate/priority).

[protocol](/en-US/docs/Web/API/RTCIceCandidateStats/protocol)Optional

A string specifying the protocol (`tcp` or `udp`) used to transmit data on the `port`. Corresponds to [RTCIceCandidate.protocol](/en-US/docs/Web/API/RTCIceCandidate/protocol).

[relayProtocol](/en-US/docs/Web/API/RTCIceCandidateStats/relayProtocol)

A string specifying the protocol being used by a local [ICE](/en-US/docs/Glossary/ICE) candidate to communicate with the [TURN](/en-US/docs/Glossary/TURN) server.

[transportId](/en-US/docs/Web/API/RTCIceCandidateStats/transportId)

A string uniquely identifying the transport object that was inspected in order to obtain the [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats) associated with the candidate corresponding to these statistics.

[url](/en-US/docs/Web/API/RTCIceCandidateStats/url)Optional

A string specifying the URL of the [ICE](/en-US/docs/Glossary/ICE) server from which the described candidate was obtained. This property is only available for local candidates.

[usernameFragment](/en-US/docs/Web/API/RTCIceCandidateStats/usernameFragment)OptionalExperimental

A string containing the ICE username fragment ("ice-ufrag"). Corresponds to [RTCIceCandidate.usernameFragment](/en-US/docs/Web/API/RTCIceCandidate/usernameFragment).

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCIceCandidateStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCIceCandidateStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCIceCandidateStats/type)

A string with the value `"local-candidate"`, indicating the type of statistics that the object contains.

## [Examples](#examples)

Given a variable `myPeerConnection`, which is an instance of [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), the code below uses `await` to wait for the statistics report, and then iterates it using `RTCStatsReport.forEach()`. It then filters the dictionaries for just those reports that have the type of `local-candidate` and logs the result.

js

```
const stats = await myPeerConnection.getStats();

stats.forEach((report) => {
  if (report.type === "local-candidate") {
    // Log the ICE candidate information
    console.log(report);
  }
});
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-local-candidate](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-local-candidate)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 14, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCIceCandidateStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcicecandidatestats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidateStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcicecandidatestats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidateStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcicecandidatestats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd9e11f88996e97a259d2ec47f47a660062c12c4f%0A*+Document+last+modified%3A+2025-05-14T14%3A51%3A28.000Z%0A%0A%3C%2Fdetails%3E)
