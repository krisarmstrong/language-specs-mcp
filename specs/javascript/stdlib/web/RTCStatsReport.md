# RTCStatsReport

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCStatsReport&level=high)

The `RTCStatsReport` interface of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides a statistics report for a [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender), or [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver).

An `RTCStatsReport` instance is a read-only [Map-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis), in which each key is an identifier for an object for which statistics are being reported, and the corresponding value is a dictionary object providing the statistics.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[RTCStatsReport.size](/en-US/docs/Web/API/RTCStatsReport/size)

Returns the number of items in the `RTCStatsReport` object.

## [Instance methods](#instance_methods)

[RTCStatsReport.entries()](/en-US/docs/Web/API/RTCStatsReport/entries)

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains a two-member array of `[id, statistic-dictionary]` for each element in the `RTCStatsReport` object, in insertion order.

[RTCStatsReport.forEach()](/en-US/docs/Web/API/RTCStatsReport/forEach)

Calls `callbackFn` once for each key-value pair present in the `RTCStatsReport` object, in insertion order. If a `thisArg` parameter is provided to `forEach`, it will be used as the `this` value for each callback.

[RTCStatsReport.get()](/en-US/docs/Web/API/RTCStatsReport/get)

Returns the statistics dictionary associated with the passed `id`, or `undefined` if there is none.

[RTCStatsReport.has()](/en-US/docs/Web/API/RTCStatsReport/has)

Returns a boolean indicating whether the `RTCStatsReport` contains a statistics dictionary associated with the specified `id`.

[RTCStatsReport.keys()](/en-US/docs/Web/API/RTCStatsReport/keys)

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains the keys (IDs) for each element in the `RTCStatsReport` object, in insertion order.

[RTCStatsReport.values()](/en-US/docs/Web/API/RTCStatsReport/values)

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains the values (statistics object) for each element in the `RTCStatsReport` object, in insertion order.

[RTCStatsReport[Symbol.iterator]()](/en-US/docs/Web/API/RTCStatsReport/Symbol.iterator)

Returns a new [Iterator](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) object that contains a two-member array of `[id, statistic-dictionary]` for each element in the `RTCStatsReport` object, in insertion order.

## [Description](#description)

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an `RTCStatsReport` is returned from the [RTCRtpReceiver.getStats()](/en-US/docs/Web/API/RTCRtpReceiver/getStats), [RTCRtpSender.getStats()](/en-US/docs/Web/API/RTCRtpSender/getStats) and [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) methods. Calling `getStats()` on an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) lets you specify whether you wish to obtain outbound statistics, inbound statistics, or statistics for the whole connection. The [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) and [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) versions of `getStats()` only return inbound and outbound statistics, respectively.

The statistics report is a read-only [Map-like](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) object: an ordered dictionary, where the properties are `id` strings that uniquely identify the WebRTC object that was inspected to produce a particular set of statistics, and the value is a dictionary object containing those statistics. A `RTCStatsReport` can be iterated and used the same ways as a read-only `Map`.

The report may contain many different categories of statistics, including inbound and outbound statistics for both the current and remote ends of the peer connection, information about codecs, certificates and media used, and so on. Each category of statistic is provided in a different type of statistics dictionary object, which can be identified from its [type](#type) property.

### [Common instance properties](#common_instance_properties)

All the dictionary types have the following properties:

[id](#id)

A string that uniquely identifies the object was monitored to produce the set of statistics. This value persists across reports for (at least) the lifetime of the connection. Note however that for some statistics the ID may vary between browsers and for subsequent connections, even to the same peer.

[timestamp](#timestamp)

A high resolution timestamp object ([DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp)) object indicating the time at which the sample was taken. Many reported statistics are cumulative values; the timestamp allows rates and averages to be calculated between any two reports, at any desired reporting rate.

[type](#type)

A string with a value that indicates the type of statistics that the object contains, such as `candidate-pair`, `inbound-rtp`, `certificate`, and so on. The [types of statistics and their corresponding objects](#the_statistic_types) are listed below.

Users typically iterate a `RTCStatsReport`, using a [forEach()](/en-US/docs/Web/API/RTCStatsReport/forEach) or [for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of) loop, selecting the statistics of interest using the `type` property. Once a particular statistic object has been identified using its `type`, the `id` property can subsequently be used with [get()](/en-US/docs/Web/API/RTCStatsReport/get) to obtain the same statistic report at a different time.

The timestamp can be used to calculate average values for statistics that accumulate over the lifetime of a connection.

### [The statistic types](#the_statistic_types)

The statistics `type` values and their corresponding dictionaries are listed below.

typeDictionaryDescription`candidate-pair`[RTCIceCandidatePairStats](/en-US/docs/Web/API/RTCIceCandidatePairStats)Statistics describing the change from one [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) to another, such as during an [ICE restart](/en-US/docs/Web/API/WebRTC_API/Session_lifetime#ice_restart).`certificate`[RTCCertificateStats](/en-US/docs/Web/API/RTCCertificateStats)Statistics about a certificate being used by an [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport).`codec`[RTCCodecStats](/en-US/docs/Web/API/RTCCodecStats)Statistics about a specific codec being used by streams being sent or received by this connection.`data-channel`[RTCDataChannelStats](/en-US/docs/Web/API/RTCDataChannelStats)Statistics related to one [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) on the connection.`inbound-rtp`[RTCInboundRtpStreamStats](/en-US/docs/Web/API/RTCInboundRtpStreamStats)Statistics describing the state of one of the connection's inbound data streams.`local-candidate`[RTCIceCandidateStats](/en-US/docs/Web/API/RTCIceCandidateStats)Statistics about a local ICE candidate associated with the connection's [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport)s.`media-source`[RTCAudioSourceStats](/en-US/docs/Web/API/RTCAudioSourceStats) or [RTCVideoSourceStats](/en-US/docs/Web/API/RTCVideoSourceStats)Statistics about the media produced by the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) attached to an RTP sender. The dictionary this key maps to depends on the track's [kind](/en-US/docs/Web/API/MediaStreamTrack/kind).`outbound-rtp`[RTCOutboundRtpStreamStats](/en-US/docs/Web/API/RTCOutboundRtpStreamStats)Statistics describing the state of one of the outbound data streams on this connection.`peer-connection`[RTCPeerConnectionStats](/en-US/docs/Web/API/RTCPeerConnectionStats)Statistics describing the state of the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).`remote-candidate`[RTCIceCandidateStats](/en-US/docs/Web/API/RTCIceCandidateStats)Statistics about a remote ICE candidate associated with the connection's [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport)s.`remote-inbound-rtp`[RTCRemoteInboundRtpStreamStats](/en-US/docs/Web/API/RTCRemoteInboundRtpStreamStats)Statistics describing the state of the inbound data stream from the perspective of the remote peer.`remote-outbound-rtp`[RTCRemoteOutboundRtpStreamStats](/en-US/docs/Web/API/RTCRemoteOutboundRtpStreamStats)Statistics describing the state of the outbound data stream from the perspective of the remote peer.`transport`[RTCTransportStats](/en-US/docs/Web/API/RTCTransportStats)Statistics about a transport used by the connection.

## [Examples](#examples)

### [Iterate report from an RTCPeerConnection using forEach loop](#iterate_report_from_an_rtcpeerconnection_using_foreach_loop)

This example logs shows how you might log video-related statistics for the local [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) responsible for receiving streamed media.

Given a variable `myPeerConnection`, which is an instance of `RTCPeerConnection`, the code uses `await` to wait for the statistics report, and then iterates it using [RTCStatsReport.forEach()](/en-US/docs/Web/API/RTCStatsReport/forEach). It then filters the dictionaries for just those reports that have the `type` of `inbound-rtp` and `kind` of `video`.

js

```
const stats = await myPeerConnection.getStats();

stats.forEach((report) => {
  if (report.type === "inbound-rtp" && report.kind === "video") {
    // Log the frame rate
    console.log(report.framesPerSecond);
  }
});
```

### [Iterate report from an RTCRtpSender using a for...of loop](#iterate_report_from_an_rtcrtpsender_using_a_for...of_loop)

This example shows how you might iterate the outbound statistics from an [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender).

The code follows a similar pattern to the previous example, but iterates using a `for...of`-loop on the [RTCStatsReport.values()](/en-US/docs/Web/API/RTCStatsReport/values), and filters on the `type` of `outbound-rtp`. It assumes you already have an `RTCRtpSender` object named "sender".

js

```
const stats = await sender.getStats();

for (const stat of stats.values()) {
  if (stat.type !== "outbound-rtp") continue;
  Object.keys(stat).forEach((statName) => {
    console.log(`${statName}: ${stat[statName]}`);
  });
}
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcstatsreport-object](https://w3c.github.io/webrtc-pc/#rtcstatsreport-object)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)
- [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats), [RTCRtpReceiver.getStats()](/en-US/docs/Web/API/RTCRtpReceiver/getStats), and [RTCRtpSender.getStats()](/en-US/docs/Web/API/RTCRtpSender/getStats)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCStatsReport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcstatsreport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCStatsReport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcstatsreport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCStatsReport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcstatsreport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe25bb407abfff31b10c1e20c077c96da647b663d%0A*+Document+last+modified%3A+2025-09-08T13%3A17%3A51.000Z%0A%0A%3C%2Fdetails%3E)
