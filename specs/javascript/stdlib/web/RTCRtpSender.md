# RTCRtpSender

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpSender&level=high)

The `RTCRtpSender` interface provides the ability to control and obtain details about how a particular [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) is encoded and sent to a remote peer.

With it, you can configure the encoding used for the corresponding track, get information about the device's media capabilities, and so forth. You can also obtain access to an [RTCDTMFSender](/en-US/docs/Web/API/RTCDTMFSender) which can be used to send [DTMF](/en-US/docs/Glossary/DTMF) codes (to simulate the user pressing buttons on a telephone's dial pad) to the remote peer.

## In this article

- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[RTCRtpSender.dtmf](/en-US/docs/Web/API/RTCRtpSender/dtmf)Read only

An [RTCDTMFSender](/en-US/docs/Web/API/RTCDTMFSender) which can be used to send [DTMF](/en-US/docs/Glossary/DTMF) tones using `telephone-event` payloads on the [RTP](/en-US/docs/Glossary/RTP) session represented by the `RTCRtpSender` object. If `null`, the track and/or the connection doesn't support DTMF. Only audio tracks can support DTMF.

[RTCRtpSender.track](/en-US/docs/Web/API/RTCRtpSender/track)Read only

The [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) which is being handled by the `RTCRtpSender`. If `track` is `null`, the `RTCRtpSender` doesn't transmit anything.

[RTCRtpSender.transport](/en-US/docs/Web/API/RTCRtpSender/transport)Read only

The [RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport) over which the sender is exchanging the RTP and RTCP packets used to manage transmission of media and control data. This value is `null` until the transport is established. When bundling is in use, more than transceiver may be sharing the same transport object.

[RTCRtpSender.transform](/en-US/docs/Web/API/RTCRtpSender/transform)

An [RTCRtpScriptTransform](/en-US/docs/Web/API/RTCRtpScriptTransform) is used to insert a transform stream ([TransformStream](/en-US/docs/Web/API/TransformStream)) running in a worker thread into the sender pipeline, allowing stream transforms to be applied to encoded video and audio frames after they are output by a codec, and before they are sent.

### [Obsolete properties](#obsolete_properties)

[rtcpTransport 
Deprecated](#rtcptransport)

This property has been removed; the RTP and RTCP transports have been combined into a single transport. Use the [transport](/en-US/docs/Web/API/RTCRtpSender/transport) property instead.

## [Static methods](#static_methods)

[RTCRtpSender.getCapabilities()](/en-US/docs/Web/API/RTCRtpSender/getCapabilities_static)

Returns an object describing the system's capabilities for sending a specified kind of media data.

## [Instance methods](#instance_methods)

[RTCRtpSender.getParameters()](/en-US/docs/Web/API/RTCRtpSender/getParameters)

Returns an object describing the current configuration for the encoding and transmission of media on the `track`.

[RTCRtpSender.getStats()](/en-US/docs/Web/API/RTCRtpSender/getStats)

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is fulfilled with a [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) which provides statistics data for all outbound streams being sent using this `RTCRtpSender`.

[RTCRtpSender.setParameters()](/en-US/docs/Web/API/RTCRtpSender/setParameters)

Applies changes to parameters which configure how the `track` is encoded and transmitted to the remote peer.

[RTCRtpSender.setStreams()](/en-US/docs/Web/API/RTCRtpSender/setStreams)

Sets the [stream(s)](/en-US/docs/Web/API/MediaStream) associated with the [track](/en-US/docs/Web/API/RTCRtpSender/track) being transmitted by this sender.

[RTCRtpSender.replaceTrack()](/en-US/docs/Web/API/RTCRtpSender/replaceTrack)

Attempts to replace the track currently being sent by the `RTCRtpSender` with another track, without performing renegotiation. This method can be used, for example, to toggle between the front- and rear-facing cameras on a device.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcrtpsender-interface](https://w3c.github.io/webrtc-pc/#rtcrtpsender-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- WebRTC API
- [RTCPeerConnection.addTrack()](/en-US/docs/Web/API/RTCPeerConnection/addTrack)
- [RTCPeerConnection.getSenders()](/en-US/docs/Web/API/RTCPeerConnection/getSenders)
- [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCRtpSender/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcrtpsender/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpSender&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcrtpsender%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCRtpSender%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcrtpsender%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7972ac25580ffbfb160e6d40013bbab3013d7cbe%0A*+Document+last+modified%3A+2024-08-12T07%3A02%3A43.000Z%0A%0A%3C%2Fdetails%3E)
