# RTCRtpReceiver

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpReceiver&level=high)

The `RTCRtpReceiver` interface of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) manages the reception and decoding of data for a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) on an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[RTCRtpReceiver.jitterBufferTarget](/en-US/docs/Web/API/RTCRtpReceiver/jitterBufferTarget)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) that indicates an application's preferred hold time for media in the jitter buffer, allowing it influence the tradeoff between playout delay and the risk of running out of audio or video frames due to network jitter.

[RTCRtpReceiver.track](/en-US/docs/Web/API/RTCRtpReceiver/track)Read only

Returns the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) associated with the current `RTCRtpReceiver` instance.

[RTCRtpReceiver.transport](/en-US/docs/Web/API/RTCRtpReceiver/transport)Read only

Returns the [RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport) instance over which the media for the receiver's track is received.

[RTCRtpReceiver.transform](/en-US/docs/Web/API/RTCRtpReceiver/transform)

An [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform) is used to insert a transform stream ([TransformStream](/en-US/docs/Web/API/TransformStream)) running in a worker thread into the receiver pipeline, allowing stream transforms to be applied to incoming encoded video and audio frames.

### [Obsolete properties](#obsolete_properties)

[rtcpTransport 
Deprecated](#rtcptransport)

This property has been removed; the RTP and RTCP transports have been combined into a single transport. Use the [transport](/en-US/docs/Web/API/RTCRtpReceiver/transport) property instead.

## [Static methods](#static_methods)

[RTCRtpReceiver.getCapabilities()](/en-US/docs/Web/API/RTCRtpReceiver/getCapabilities_static)

Returns the most optimistic view of the capabilities of the system for receiving media of the given kind.

## [Instance methods](#instance_methods)

[RTCRtpReceiver.getContributingSources()](/en-US/docs/Web/API/RTCRtpReceiver/getContributingSources)

Returns an array that contains an object for each unique CSRC (contributing source) identifier received by the current `RTCRtpReceiver` in the last ten seconds.

[RTCRtpReceiver.getParameters()](/en-US/docs/Web/API/RTCRtpReceiver/getParameters)

Returns an object that contains information about how the RTC data is to be decoded.

[RTCRtpReceiver.getStats()](/en-US/docs/Web/API/RTCRtpReceiver/getStats)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) whose fulfillment handler receives a [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) which contains statistics about the incoming streams and their dependencies.

[RTCRtpReceiver.getSynchronizationSources()](/en-US/docs/Web/API/RTCRtpReceiver/getSynchronizationSources)

Returns an array that contains an object for each unique SSRC (synchronization source) identifier received by the current `RTCRtpReceiver` in the last ten seconds.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcrtpreceiver-interface](https://w3c.github.io/webrtc-pc/#rtcrtpreceiver-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport)
- [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)
- [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCRtpReceiver/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcrtpreceiver/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpReceiver&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcrtpreceiver%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpReceiver%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcrtpreceiver%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa9ed68046545018031dcf77330d901e2cf7054e9%0A*+Document+last+modified%3A+2024-05-02T08%3A34%3A54.000Z%0A%0A%3C%2Fdetails%3E)
