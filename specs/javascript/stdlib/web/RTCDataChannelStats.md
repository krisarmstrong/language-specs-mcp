# RTCDataChannelStats

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannelStats&level=not)

The `RTCDataChannelStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides statistics related to one [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) object on the connection.

The report can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find an entry with the [type](/en-US/docs/Web/API/RTCDataChannelStats/type) of `data-channel`.

The data channels statistics may be correlated to a particular channel by comparing the [dataChannelIdentifier](/en-US/docs/Web/API/RTCDataChannelStats/dataChannelIdentifier) property to a matching [RTCDataChannel.id](/en-US/docs/Web/API/RTCDataChannel/id).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[bytesSent](/en-US/docs/Web/API/RTCDataChannelStats/bytesSent)Optional

A positive integer value indicating the total number of payload bytes sent on the associated `RTCDataChannel`.

[bytesReceived](/en-US/docs/Web/API/RTCDataChannelStats/bytesReceived)Optional

A positive integer value indicating the total number of payload bytes received on the associated `RTCDataChannel`.

[dataChannelIdentifier](/en-US/docs/Web/API/RTCDataChannelStats/dataChannelIdentifier)Optional

A positive integer value containing the [id](/en-US/docs/Web/API/RTCDataChannel/id) of the associated `RTCDataChannel`.

[label](/en-US/docs/Web/API/RTCDataChannelStats/label)Optional

A string containing the [label](/en-US/docs/Web/API/RTCDataChannel/label) of the associated `RTCDataChannel`.

[messagesReceived](/en-US/docs/Web/API/RTCDataChannelStats/messagesReceived)Optional

A positive integer value indicating the total number of [message events](/en-US/docs/Web/API/RTCDataChannel/message_event) fired for received messages on the associated `RTCDataChannel`.

[messagesSent](/en-US/docs/Web/API/RTCDataChannelStats/messagesSent)Optional

A positive integer value indicating the total number of [message events](/en-US/docs/Web/API/RTCDataChannel/message_event) fired for sent messages on the channel.

[protocol](/en-US/docs/Web/API/RTCDataChannelStats/protocol)Optional

A string containing the [protocol](/en-US/docs/Web/API/RTCDataChannel/protocol) of the associated `RTCDataChannel`.

[state](/en-US/docs/Web/API/RTCDataChannelStats/state)

The [readyState](/en-US/docs/Web/API/RTCDataChannel/readyState) of the associated `RTCDataChannel`.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects (See [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport#common_instance_properties) for more information).

[id](/en-US/docs/Web/API/RTCDataChannelStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCDataChannelStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCDataChannelStats/type)

A string with the value `"data-channel"`, indicating the type of statistics that the object contains.

## [Examples](#examples)

Given a variable `myPeerConnection`, which is an instance of [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), the code below uses `await` to wait for the statistics report, and then iterates it using `RTCStatsReport.forEach()`. It then filters the dictionaries for just those reports that have the type of `data-channel` and logs the result.

js

```
const stats = await myPeerConnection.getStats();

stats.forEach((report) => {
  if (report.type === "data-channel") {
    // Log the channel information
    console.log(report);
  }
});
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-data-channel](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-data-channel)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCDataChannelStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcdatachannelstats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannelStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcdatachannelstats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannelStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcdatachannelstats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
