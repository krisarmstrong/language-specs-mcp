# RTCRemoteInboundRtpStreamStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨February 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRemoteInboundRtpStreamStats&level=high)

The `RTCRemoteInboundRtpStreamStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to report statistics from the remote endpoint about a particular incoming RTP stream. These will correspond to an outgoing RTP stream at the local end of the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

The statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) or [RTCRtpReceiver.getStats()](/en-US/docs/Web/API/RTCRtpReceiver/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/type) of `remote-inbound-rtp`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

### [Remote inbound specific statistics](#remote_inbound_specific_statistics)

[fractionLost](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/fractionLost)Optional

A number indicating the fraction of packets lost for this SSRC since the last sender or receiver report.

[localId](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/localId)Optional

A string that is used to find the local [RTCOutboundRtpStreamStats](/en-US/docs/Web/API/RTCOutboundRtpStreamStats) object that shares the same [synchronization source (SSRC)](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/ssrc).

[roundTripTime](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/roundTripTime)Optional

A number that indicates the estimated round trip time (RTT) for this SSRC, in seconds. This property will not exist until valid RTT data has been received.

[roundTripTimeMeasurements](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/roundTripTimeMeasurements)Optional

A positive integer indicating the total number of valid round trip time measurements received for this [synchronization source (SSRC)](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/ssrc).

[totalRoundTripTime](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/totalRoundTripTime)Optional

A number indicating the cumulative sum of all round trip time measurements since the beginning of the session, in seconds. The average round trip time can be computed by dividing `totalRoundTripTime` by [roundTripTimeMeasurements](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/roundTripTimeMeasurements).

### [Received RTP stream statistics](#received_rtp_stream_statistics)

[jitter](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/jitter)Optional

A number indicating the [packet jitter](/en-US/docs/Glossary/Jitter) for this synchronization source, measured in seconds.

[packetsLost](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/packetsLost)Optional

An integer indicating the total number of RTP packets lost for this SSRC, as measured at the remote endpoint. This value can be negative if duplicate packets were received.

[packetsReceived](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/packetsReceived)OptionalExperimental

A positive integer indicating the total number of RTP packets received for this SSRC, including retransmissions.

### [Common RTP stream statistics](#common_rtp_stream_statistics)

[codecId](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/codecId)Optional

A string that uniquely identifies the object that was inspected to produce the [RTCCodecStats](/en-US/docs/Web/API/RTCCodecStats) object associated with this [RTP](/en-US/docs/Glossary/RTP) stream.

[kind](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/kind)

A string indicating whether the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) associated with the stream is an audio or a video track.

[ssrc](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/ssrc)

A positive integer that identifies the SSRC of the RTP packets in this stream.

[transportId](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/transportId)Optional

A string that uniquely identifies the object which was inspected to produce the [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats) object associated with this RTP stream.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/type)

A string with the value `"inbound-rtp"`, indicating the type of statistics that the object contains.

## [Examples](#examples)

Given a variable `peerConnection` that is an instance of an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), the code below uses `await` to wait for the statistics report, and then iterates it using `RTCStatsReport.forEach()`. It then filters the dictionaries for just those reports that have the type of `remote-inbound-rtp` and logs the result.

js

```
const stats = await myPeerConnection.getStats();

stats.forEach((report) => {
  if (report.type === "remote-inbound-rtp") {
    console.log("Remote Inbound RTP Stream Stats:");
    console.log(`id: ${report.id}`);
    console.log(`timestamp: ${report.timestamp}`);
    console.log(`transportId: ${report.transportId}`);
    console.log(`ssrc: ${report.ssrc}`);
    console.log(`kind: ${report.kind}`);
    console.log(`codecId: ${report.codecId}`);
    console.log(`packetsReceived: ${report.packetsReceived}`);
    console.log(`packetsLost: ${report.packetsLost}`);
    console.log(`jitter: ${report.jitter}`);
    console.log(`totalRoundTripTime: ${report.totalRoundTripTime}`);
    console.log(
      `roundTripTimeMeasurements: ${report.roundTripTimeMeasurements}`,
    );
    console.log(`roundTripTime: ${report.roundTripTime}`);
    console.log(`localId: ${report.localId}`);
    console.log(`fractionLost: ${report.fractionLost}`);
  }
});
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-remote-inbound-rtp](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-remote-inbound-rtp)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcremoteinboundrtpstreamstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRemoteInboundRtpStreamStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcremoteinboundrtpstreamstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRemoteInboundRtpStreamStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcremoteinboundrtpstreamstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
