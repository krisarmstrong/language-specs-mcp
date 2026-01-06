# RTCVideoSourceStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCVideoSourceStats&level=high)

The `RTCVideoSourceStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides statistics information about a video track ([MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack)) that is attached to one or more senders ([RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)).

These statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCRtpSender.getStats()](/en-US/docs/Web/API/RTCRtpSender/getStats) or [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCVideoSourceStats/type) of `media-source` and a [kind](/en-US/docs/Web/API/RTCVideoSourceStats/kind) of `video`.

Note: For video information about remotely sourced tracks (that are being received), see [RTCInboundRtpStreamStats](/en-US/docs/Web/API/RTCInboundRtpStreamStats).

## In this article

- [Instance properties](#instance_properties)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[frames](/en-US/docs/Web/API/RTCVideoSourceStats/frames)Optional

A positive number that indicates the total number of frames originating from this video source.

[framesPerSecond](/en-US/docs/Web/API/RTCVideoSourceStats/framesPerSecond)Optional

A positive number that represents the number of frames originating from this video source in the last second. This property is not defined on this stats object for the first second of its existence.

[height](/en-US/docs/Web/API/RTCVideoSourceStats/height)Optional

A number that represents the height, in pixels, of the last frame originating from this source. This property is not defined on this stats object until after the first frame has been produced.

[width](/en-US/docs/Web/API/RTCVideoSourceStats/width)Optional

A number that represents the width, in pixels, of the most recent frame originating from this source. This property is not defined on this stats object until after the first frame has been produced.

### [Common media-source properties](#common_media-source_properties)

The following properties are present in both `RTCVideoSourceStats` and [RTCAudioSourceStats](/en-US/docs/Web/API/RTCAudioSourceStats): 

[trackIdentifier](/en-US/docs/Web/API/RTCVideoSourceStats/trackIdentifier)

A string that contains the [id](/en-US/docs/Web/API/MediaStreamTrack/id) value of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) associated with the video source.

[kind](/en-US/docs/Web/API/RTCVideoSourceStats/kind)

A string indicating whether this object represents stats for a video source or a media source. For an `RTCVideoSourceStats` this will always be `video`.

### [Common instance properties](#common_instance_properties)

The following properties are common to all statistics objects. 

[id](/en-US/docs/Web/API/RTCVideoSourceStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCVideoSourceStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCVideoSourceStats/type)

A string with the value `"media-source"`, indicating that the object is an instance of either [RTCAudioSourceStats](/en-US/docs/Web/API/RTCAudioSourceStats) or `RTCVideoSourceStats`.

## [Description](#description)

The interface provides statistics about a video media source attached to one or more senders. The information includes an identifier for the associated `MediaStreamTrack`, along with the height and width of the last frame sent from the source, the number of frames sent from the source, and the frame rate.

## [Examples](#examples)

This example shows how you might iterate the stats object returned from `RTCRtpSender.getStats()` to get the video-specific media-source stats.

js

```
// where sender is an RTCRtpSender
const stats = await sender.getStats();
let videoSourceStats = null;

stats.forEach((report) => {
  if (report.type === "media-source" && report.kind==="video") {
    videoSourceStats = report;
    break;
  }
});

// videoSourceStats will be null if the report did not include video source stats
const frames = videoSourceStats?.frames;
const fps = videoSourceStats?.framesPerSecond;
const width = videoSourceStats?.width;
const height = videoSourceStats?.height;
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcvideosourcestats](https://w3c.github.io/webrtc-stats/#dom-rtcvideosourcestats)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCVideoSourceStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcvideosourcestats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCVideoSourceStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcvideosourcestats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCVideoSourceStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcvideosourcestats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
