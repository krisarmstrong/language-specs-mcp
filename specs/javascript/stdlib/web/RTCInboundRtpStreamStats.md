# RTCInboundRtpStreamStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCInboundRtpStreamStats&level=high)

The `RTCInboundRtpStreamStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to report statistics related to the receiving end of an RTP stream on the local end of the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

The statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) or [RTCRtpReceiver.getStats()](/en-US/docs/Web/API/RTCRtpReceiver/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCInboundRtpStreamStats/type) of `inbound-rtp`.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[audioLevel](/en-US/docs/Web/API/RTCInboundRtpStreamStats/audioLevel)

A number that indicates the audio level of the received track. Undefined for video streams.

[bytesReceived](/en-US/docs/Web/API/RTCInboundRtpStreamStats/bytesReceived)

A positive integer that indicates the total number of bytes that have been received so far for this media source.

[concealedSamples](/en-US/docs/Web/API/RTCInboundRtpStreamStats/concealedSamples)

A positive integer that indicates the number of samples that had to be concealed because they were in packets that were lost or arrived too late to be played out. Undefined for video streams.

[concealmentEvents](/en-US/docs/Web/API/RTCInboundRtpStreamStats/concealmentEvents)

A positive integer that indicates the number of concealment events, where a single event is counted for all consecutive concealed samples following a non-concealed sample. Undefined for video streams.

[estimatedPlayoutTimestamp](/en-US/docs/Web/API/RTCInboundRtpStreamStats/estimatedPlayoutTimestamp)Experimental

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that indicates the estimated playout time of this receiver's track.

[fecPacketsDiscarded](/en-US/docs/Web/API/RTCInboundRtpStreamStats/fecPacketsDiscarded)

A positive integer value that indicates the number of RTP Forward Error Correction (FEC) packets which have been received for this source, for which the error correction payload was discarded.

[fecPacketsReceived](/en-US/docs/Web/API/RTCInboundRtpStreamStats/fecPacketsReceived)

A positive integer value that indicates the total number of Forward Error Correction (FEC) packets received for this source.

[frameHeight](/en-US/docs/Web/API/RTCInboundRtpStreamStats/frameHeight)

A positive integer that indicates the height of the last decoded frame, in pixels. Undefined for audio streams and before the first frame is decoded.

[framesAssembledFromMultiplePackets](/en-US/docs/Web/API/RTCInboundRtpStreamStats/framesAssembledFromMultiplePackets)Experimental

A positive integer that indicates the total number of correctly decoded frames for this RTP stream that consist of more than one RTP packet. Undefined for audio streams.

[framesDecoded](/en-US/docs/Web/API/RTCInboundRtpStreamStats/framesDecoded)

A long integer value that indicates the total number of frames of video which have been correctly decoded so far for this media source. This is the number of frames that would have been rendered if none were dropped. Undefined for audio streams.

[framesPerSecond](/en-US/docs/Web/API/RTCInboundRtpStreamStats/framesPerSecond)

A positive integer that indicates the number of frames decoded in the last second. Undefined for audio streams.

[framesReceived](/en-US/docs/Web/API/RTCInboundRtpStreamStats/framesReceived)

A positive integer that indicates the total number of complete frames received on this RTP stream. Undefined for audio streams.

[frameWidth](/en-US/docs/Web/API/RTCInboundRtpStreamStats/frameWidth)

A positive integer that indicates the width of the last decoded frame, in pixels. Undefined for audio streams and before the first frame is decoded.

[freezeCount](/en-US/docs/Web/API/RTCInboundRtpStreamStats/freezeCount)Experimental

A positive integer that indicates the total number of video freezes experienced by this receiver. Undefined for audio streams.

[headerBytesReceived](/en-US/docs/Web/API/RTCInboundRtpStreamStats/headerBytesReceived)

A positive integer that indicates the total number of RTP header and padding bytes received for this SSRC, including retransmissions.

[insertedSamplesForDeceleration](/en-US/docs/Web/API/RTCInboundRtpStreamStats/insertedSamplesForDeceleration)

A positive integer that indicates the number of samples inserted to slow playout from the jitter buffer. Undefined for video streams.

[jitterBufferDelay](/en-US/docs/Web/API/RTCInboundRtpStreamStats/jitterBufferDelay)

A number that indicates the accumulated time that all audio samples and complete video frames have spent in the jitter buffer, in seconds.

[jitterBufferEmittedCount](/en-US/docs/Web/API/RTCInboundRtpStreamStats/jitterBufferEmittedCount)

A positive integer indicating the total number of audio samples and/or video frames that have come out of the jitter buffer.

[jitterBufferMinimumDelay](/en-US/docs/Web/API/RTCInboundRtpStreamStats/jitterBufferMinimumDelay)

A number that indicates the minimum delay that might be achieved given only the network characteristics such as jitter and packet loss.

[jitterBufferTargetDelay](/en-US/docs/Web/API/RTCInboundRtpStreamStats/jitterBufferTargetDelay)

A number that indicates the accumulated target jitter buffer delay.

[keyFramesDecoded](/en-US/docs/Web/API/RTCInboundRtpStreamStats/keyFramesDecoded)

A positive integer that indicates the total number of key frames successfully decoded for this RTP media stream. Undefined for audio streams.

[lastPacketReceivedTimestamp](/en-US/docs/Web/API/RTCInboundRtpStreamStats/lastPacketReceivedTimestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that indicates the time at which the last packet was received for this source. The [timestamp](/en-US/docs/Web/API/RTCInboundRtpStreamStats/timestamp) property, on the other hand, indicates the time at which the statistics object was generated.

[mid](/en-US/docs/Web/API/RTCInboundRtpStreamStats/mid)

A string that uniquely identifies the pairing of source and destination of the transceiver's stream. This is the value of the corresponding [RTCRtpTransceiver.mid](/en-US/docs/Web/API/RTCRtpTransceiver/mid) unless that is null, in which case the statistic property is not present.

[packetsDiscarded](/en-US/docs/Web/API/RTCInboundRtpStreamStats/packetsDiscarded)

A positive integer that indicates the total number of RTP packets discarded by the jitter buffer due to late or early-arrival.

[pauseCount](/en-US/docs/Web/API/RTCInboundRtpStreamStats/pauseCount)Experimental

A positive integer that indicates the number of video pauses experienced by this receiver. Undefined for audio streams.

[playoutId](/en-US/docs/Web/API/RTCInboundRtpStreamStats/playoutId)Experimental

A string that identifies the corresponding `RTCAudioPlayoutStats` for an audio stream. Undefined for video streams.

[remoteId](/en-US/docs/Web/API/RTCInboundRtpStreamStats/remoteId)

A string that identifies the [RTCRemoteOutboundRtpStreamStats](/en-US/docs/Web/API/RTCRemoteOutboundRtpStreamStats) object that provides statistics for the remote peer for this same SSRC. This ID is stable across multiple calls to `getStats()`.

[removedSamplesForAcceleration](/en-US/docs/Web/API/RTCInboundRtpStreamStats/removedSamplesForAcceleration)

A positive integer that indicates the number of samples removed from to speed up playout from the jitter buffer. Undefined for video streams.

[silentConcealedSamples](/en-US/docs/Web/API/RTCInboundRtpStreamStats/silentConcealedSamples)

A positive integer that indicates the number of silent concealed samples. Undefined for video streams.

[totalAssemblyTime](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalAssemblyTime)Experimental

A number that indicates the total time spent assembling successfully decoded video frames that were transported in multiple RTP packets, in seconds. Undefined for audio streams.

[totalAudioEnergy](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalAudioEnergy)

A number that represents the total audio energy of the received track over the lifetime of the stats object. Undefined for video streams.

[totalDecodeTime](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalDecodeTime)

A number that indicates the total time spent decoding frames in this stream, in seconds. Undefined for audio streams.

[totalFreezesDuration](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalFreezesDuration)Experimental

A positive number that indicates the total time that the stream has spent frozen, in seconds. Undefined for audio streams.

[totalInterFrameDelay](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalInterFrameDelay)

A positive number that indicates the total time spent between consecutively rendered frames, recorded just after a frame has been rendered. Undefined for audio streams.

[totalPausesDuration](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalPausesDuration)Experimental

A positive number that indicates the total time that the stream has spent with paused video, in seconds. Undefined for audio streams.

[totalProcessingDelay](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalProcessingDelay)

A positive number that indicates the total time spent processing audio or video samples, in seconds.

[totalSamplesDuration](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalSamplesDuration)

A positive number that indicates the total duration of all samples that have been received, in seconds. Undefined for video streams.

[totalSamplesReceived](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalSamplesReceived)

A positive integer that indicates the total number of samples received on this stream. Undefined for video streams.

[totalSquaredInterFrameDelay](/en-US/docs/Web/API/RTCInboundRtpStreamStats/totalSquaredInterFrameDelay)

A positive number that indicates the sum of the square of inter-frame delays between consecutively rendered frames, recorded just after a frame has been rendered. Undefined for audio streams.

[trackIdentifier](/en-US/docs/Web/API/RTCInboundRtpStreamStats/trackIdentifier)

A string that provides the [id](/en-US/docs/Web/API/MediaStreamTrack/id) value of the `MediaStreamTrack` associated with the inbound stream.

### [Local-only measurements](#local-only_measurements)

These properties are computed locally, and are only available to the device receiving the media stream. Their primary purpose is to examine the error resiliency of the connection, as they provide information about lost packets, lost frames, and how heavily compressed the data is.

[nackCount](/en-US/docs/Web/API/RTCInboundRtpStreamStats/nackCount)

A number that indicates the number of times the receiver notified the sender that one or more RTP packets has been lost by sending a Negative ACKnowledgement (NACK, also called "Generic NACK") packet to the sender. This value is only available to the receiver.

[qpSum](/en-US/docs/Web/API/RTCInboundRtpStreamStats/qpSum)

A positive integer that provides the sum of the QP values for every frame decoded by this RTP receiver to date on the video track described by this statistics object. Valid only for video streams.

### [Statistics measured at the receiver of an RTP stream](#statistics_measured_at_the_receiver_of_an_rtp_stream)

These statistics are measured at the receiving end of an RTP stream, regardless of whether it's local or remote.

[packetsReceived](/en-US/docs/Web/API/RTCInboundRtpStreamStats/packetsReceived)

The total number of RTP packets received for this [synchronizing source (SSRC)](/en-US/docs/Web/API/RTCInboundRtpStreamStats/ssrc), including retransmissions.

[packetsLost](/en-US/docs/Web/API/RTCInboundRtpStreamStats/packetsLost)

The total number of RTP packets lost for this [synchronizing source (SSRC)](/en-US/docs/Web/API/RTCInboundRtpStreamStats/ssrc). Note that this can be negative, as more packets may be received than the receiver expects.

[jitter](/en-US/docs/Web/API/RTCInboundRtpStreamStats/jitter)

Packet jitter for this [synchronizing source (SSRC)](/en-US/docs/Web/API/RTCInboundRtpStreamStats/ssrc), measured in seconds.

### [Common RTP stream statistics](#common_rtp_stream_statistics)

[codecId](/en-US/docs/Web/API/RTCInboundRtpStreamStats/codecId)

A string that uniquely identifies the object which was inspected to produce the [RTCCodecStats](/en-US/docs/Web/API/RTCCodecStats) object associated with this [RTP](/en-US/docs/Glossary/RTP) stream.

[kind](/en-US/docs/Web/API/RTCInboundRtpStreamStats/kind)

A string that indicates whether the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) associated with the stream is an audio or a video track.

[ssrc](/en-US/docs/Web/API/RTCInboundRtpStreamStats/ssrc)

The 32-bit integer that identifies the source of the RTP packets this object provides. This value is generated per the [RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550) specification.

[transportId](/en-US/docs/Web/API/RTCInboundRtpStreamStats/transportId)

A string that uniquely identifies the object which was inspected to produce the [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats) object associated with this RTP stream.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCInboundRtpStreamStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCInboundRtpStreamStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object that indicates the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCInboundRtpStreamStats/type)

A string with the value `"inbound-rtp"`, which indicates the type of statistics that the object contains.

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-inbound-rtp](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-inbound-rtp)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 19, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCInboundRtpStreamStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcinboundrtpstreamstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCInboundRtpStreamStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcinboundrtpstreamstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCInboundRtpStreamStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcinboundrtpstreamstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F74e7902b0875b6378d77df6d2d925a2d09d19f5d%0A*+Document+last+modified%3A+2025-08-19T00%3A21%3A41.000Z%0A%0A%3C%2Fdetails%3E)
