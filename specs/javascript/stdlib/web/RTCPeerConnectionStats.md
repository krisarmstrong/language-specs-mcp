# RTCPeerConnectionStats

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionStats&level=high)

The `RTCPeerConnectionStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides information about the high level peer connection ([RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)).

In particular, it provides the number of unique data channels that have been opened, and the number of opened channels that have been closed. This allows the current number of open channels to be calculated.

These statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCPeerConnectionStats/type) of `peer-connection`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[dataChannelsOpened](/en-US/docs/Web/API/RTCPeerConnectionStats/dataChannelsOpened)

A positive integer value indicating the number of unique [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) objects that have entered the [open](/en-US/docs/Web/API/RTCDataChannel/readyState#open) state during their lifetime.

[dataChannelsClosed](/en-US/docs/Web/API/RTCPeerConnectionStats/dataChannelsClosed)

A positive integer value indicating the number of unique [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) objects that have left the [open](/en-US/docs/Web/API/RTCDataChannel/readyState#open) state during their lifetime (channels that transition to [closing](/en-US/docs/Web/API/RTCDataChannel/readyState#closing) or [closed](/en-US/docs/Web/API/RTCDataChannel/readyState#closed) without ever being `open` are not counted in this number). A channel will leave the `open` state if either end of the connection or the underlying transport is closed.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects.

[id](/en-US/docs/Web/API/RTCPeerConnectionStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCPeerConnectionStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCPeerConnectionStats/type)

A string with the value `"peer-connection"`, indicating the type of statistics that the object contains.

## [Examples](#examples)

This example shows a function to return the total number of open connections, or `null` if no statistics are provided. This might be called in a loop, similar to the approach used in [RTCPeerConnection.getStats() example](/en-US/docs/Web/API/RTCPeerConnection/getStats#examples)

The function waits for the result of a call to [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) and then iterates the returned [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) to get just the stats of type `"peer-connection"`. It then returns the total number of open channels, or `null`, using the data in the report.

js

```
async function numberOpenConnections (peerConnection) {
  const stats = await peerConnection.getStats();
  let peerConnectionStats = null;

  stats.forEach((report) => {
    if (report.type === "peer-connection") {
      peerConnectionStats = report;
      break;
    }
  });

result = (typeof peerConnectionStats.dataChannelsOpened === 'undefined' || typeof peerConnectionStats.dataChannelsClosed=== 'undefined') ? null : peerConnectionStats.dataChannelsOpened - peerConnectionStats.dataChannelsClosed;
return result
}
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-peer-connection](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-peer-connection)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCPeerConnectionStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcpeerconnectionstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcpeerconnectionstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcpeerconnectionstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
