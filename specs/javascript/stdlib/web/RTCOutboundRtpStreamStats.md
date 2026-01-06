# RTCOutboundRtpStreamStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨February 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCOutboundRtpStreamStats&level=high)

The `RTCOutboundRtpStreamStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to report metrics and statistics related to an outbound [RTP](/en-US/docs/Glossary/RTP) stream being sent by an [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender).

The statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) or [RTCRtpSender.getStats()](/en-US/docs/Web/API/RTCRtpSender/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/type) of `outbound-rtp`.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[active](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/active)Experimental

A boolean that indicates whether this RTP stream is configured to be sent, or is disabled.

[frameHeight](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/frameHeight)

An integer indicating the height of the last encoded frame, in pixels. Undefined for audio streams.

[frameWidth](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/frameWidth)

An integer indicating the width of the last encoded frame, in pixels. Undefined for audio streams.

[framesEncoded](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/framesEncoded)

The number of frames that have been successfully encoded so far for sending on this RTP stream. Undefined for audio streams.

[framesPerSecond](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/framesPerSecond)

A number that represents the encoded frames sent in the last second. Undefined for audio streams.

[framesSent](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/framesSent)

A positive integer that represents the total number of encoded frames sent on this RTP stream. Undefined for audio streams.

[headerBytesSent](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/headerBytesSent)

A positive integer that represents the total number of RTP header and padding bytes sent for this SSRC.

[keyFramesEncoded](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/keyFramesEncoded)Experimental

A positive integer that represents the total number of key frames successfully encoded in this RTP media stream. Undefined for audio streams.

[mediaSourceId](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/mediaSourceId)

A string that represents the id of the stats object of the track currently attached to the sender of this stream.

[mid](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/mid)

A string that uniquely identifies the pairing of source and destination of the transceiver's stream. This is the value of the corresponding [RTCRtpTransceiver.mid](/en-US/docs/Web/API/RTCRtpTransceiver/mid) unless that is null, in which case the statistic property is not present.

[nackCount](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/nackCount)

An integer value indicating the total number of Negative ACKnowledgement (NACK) packets this `RTCRtpSender` has received from the remote [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver). This locally-computed value provides an indication of the error resiliency of the connection.

[qpSum](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/qpSum)

A 64-bit value containing the sum of the QP values for every frame encoded by this [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender). This locally-computed value provides an indication of how heavily compressed the data is. Undefined for audio streams.

[qualityLimitationDurations](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/qualityLimitationDurations)Experimental

A map of the reasons that a media stream's resolution or framerate has been reduced, and the time that the quality was reduced for each reason. Undefined for audio streams.

[qualityLimitationReason](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/qualityLimitationReason)Experimental

A string indicating the reason why the stream is being quality-limited. One of: `none`, `cpu`, `bandwidth`, or `other`. Undefined for audio streams.

[remoteId](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/remoteId)

A string which identifies the [RTCRemoteInboundRtpStreamStats](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats) object that provides statistics for the remote peer for this same SSRC. This ID is stable across multiple calls to `getStats()`.

[retransmittedBytesSent](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/retransmittedBytesSent)

A positive integer that represents the total number of payload bytes retransmitted for the source associated with this stream.

[retransmittedPacketsSent](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/retransmittedPacketsSent)

A positive integer that represents the total number of packets retransmitted for the source associated with this stream.

[rid](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/rid)

A string that indicates the RTP stream ID for a corresponding video stream.

[scalabilityMode](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/scalabilityMode)Experimental

A string that represents the scalability mode for the RTP stream, if one has been configured.

[targetBitrate](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/targetBitrate)

A number that represents the bit rate that the `RTCRtpSender`'s codec is currently attempting to achieve for the stream.

[totalEncodeTime](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/totalEncodeTime)

A number that represents the total number of seconds that have been spent encoding the frames encoded for this stream [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender). Undefined for audio streams.

[totalEncodedBytesTarget](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/totalEncodedBytesTarget)Experimental

A cumulative sum of the target frame sizes for all of the frames encoded so far. This will likely differ from the total of the actual frame sizes. Undefined for audio streams.

[totalPacketSendDelay](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/totalPacketSendDelay)

A number that represents the total time in seconds that packets have spent buffered locally before being transmitted.

### [Sent RTP stream statistics](#sent_rtp_stream_statistics)

[bytesSent](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/bytesSent)Optional

A positive integer indicating the total number of bytes sent for this SSRC, including retransmissions. 

[packetsSent](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/packetsSent)Optional

A positive integer indicating the total number of RTP packets sent for this SSRC, including retransmissions. 

### [Common RTP stream statistics](#common_rtp_stream_statistics)

[codecId](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/codecId)Optional

A string that uniquely identifies the object that was inspected to produce the [RTCCodecStats](/en-US/docs/Web/API/RTCCodecStats) object associated with this [RTP](/en-US/docs/Glossary/RTP) stream.

[kind](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/kind)

A string indicating whether the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) associated with the stream is an audio or a video track.

[ssrc](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/ssrc)

A positive integer that identifies the SSRC of the RTP packets in this stream.

[transportId](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/transportId)Optional

A string that uniquely identifies the object which was inspected to produce the [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats) object associated with this RTP stream.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/type)

A string with the value `"outbound-rtp"`, indicating the type of statistics that the object contains.

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-outbound-rtp](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-outbound-rtp)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCOutboundRtpStreamStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcoutboundrtpstreamstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCOutboundRtpStreamStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcoutboundrtpstreamstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCOutboundRtpStreamStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcoutboundrtpstreamstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
