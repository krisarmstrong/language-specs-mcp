# RTCCodecStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCodecStats&level=high)

The `RTCCodecStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides statistics about a codec used by [RTP](/en-US/docs/Glossary/RTP) streams that are being sent or received by the associated [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) object.

These statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) object returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find an entry with the [type](/en-US/docs/Web/API/RTCCodecStats/type) of `codec`.

The codec statistics can be correlated with the inbound or outbound stream statistics (both local and remote) by matching their `codecId` property to the codec's `id`. For example, if [RTCInboundRtpStreamStats.codecId](/en-US/docs/Web/API/RTCInboundRtpStreamStats/codecId) matches an [RTCCodecStats.id](/en-US/docs/Web/API/RTCCodecStats/id) in the same report, then we know that the codec is being used on this peer connection's inbound stream. If no stream `codecId` references a codec statistic, then that codec statistic object is deleted — if the codec is used again, the statistics object will be recreated with the same `id`.

Codec objects may be referenced by multiple RTP streams in media sections using the same transport. In fact, user agents are expected to consolidate information into a single "codec" entry per payload type per transport (unless [sdpFmtpLine](/en-US/docs/Web/API/RTCCodecStats/sdpFmtpLine) is different when sending or receiving, in which case, different codecs will be needed for encoding and decoding). Note that other transports will use their own distinct `RTCCodecStats` objects.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[channels](/en-US/docs/Web/API/RTCCodecStats/channels)Optional

A positive number indicating the number of channels supported by the codec.

[clockRate](/en-US/docs/Web/API/RTCCodecStats/clockRate)Optional

A positive number containing the media sampling rate.

[mimeType](/en-US/docs/Web/API/RTCCodecStats/mimeType)

A string containing the media MIME type/subtype, such as video/VP8.

[payloadType](/en-US/docs/Web/API/RTCCodecStats/payloadType)

A positive integer value in the range of 0 to 127 indicating the payload type used in RTP encoding or decoding.

[sdpFmtpLine](/en-US/docs/Web/API/RTCCodecStats/sdpFmtpLine)Optional

A string containing the format-specific parameters of the `"a=fmtp"` line in the codec's [SDP](/en-US/docs/Glossary/SDP) (if present).

[transportId](/en-US/docs/Web/API/RTCCodecStats/transportId)

A string containing the unique identifier of the transport on which this codec is being used. This can be used to match to the corresponding [RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats) object.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects (see [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport#common_instance_properties) for more information):

[id](/en-US/docs/Web/API/RTCCodecStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCCodecStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCCodecStats/type)

A string with the value `"codec"`, indicating the type of statistics the object contains.

## [Examples](#examples)

Given a variable `myPeerConnection`, which is an instance of [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), the code below uses `await` to wait for the statistics report, and then iterates it using `RTCStatsReport.forEach()`. It then filters the dictionaries for just those reports that have the type of `codec` and logs the result.

js

```
const stats = await myPeerConnection.getStats();

stats.forEach((report) => {
  if (report.type === "codec") {
    // Log the codec information
    console.log(report);
  }
});
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-codec](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-codec)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport)
- `codecs` option in parameter passed to [RTCRtpTransceiver.setCodecPreferences()](/en-US/docs/Web/API/RTCRtpTransceiver/setCodecPreferences) and [RTCRtpSender.setParameters()()](/en-US/docs/Web/API/RTCRtpSender/setParameters).
- `codecs` property in object returned by [RTCRtpSender.getParameters()](/en-US/docs/Web/API/RTCRtpSender/getParameters) and [RTCRtpReceiver.getParameters()](/en-US/docs/Web/API/RTCRtpReceiver/getParameters).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCCodecStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtccodecstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCodecStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtccodecstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCodecStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtccodecstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
