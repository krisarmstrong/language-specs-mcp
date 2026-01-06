# RTCAudioSourceStats

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2023⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCAudioSourceStats&level=high)

The `RTCAudioSourceStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides statistics information about an audio track ([MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack)) that is attached to one or more senders ([RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)).

These statistics can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCRtpSender.getStats()](/en-US/docs/Web/API/RTCRtpSender/getStats) or [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find a report with the [type](/en-US/docs/Web/API/RTCAudioSourceStats/type) of `media-source` and a [kind](/en-US/docs/Web/API/RTCAudioSourceStats/kind) of `audio`.

Note: For audio information about remotely sourced tracks (that are being received), see [RTCInboundRtpStreamStats](/en-US/docs/Web/API/RTCInboundRtpStreamStats).

## In this article

- [Instance properties](#instance_properties)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[audioLevel](/en-US/docs/Web/API/RTCAudioSourceStats/audioLevel)ExperimentalOptional

A number that represents the audio level of the media source.

[totalAudioEnergy](/en-US/docs/Web/API/RTCAudioSourceStats/totalAudioEnergy)ExperimentalOptional

A number that represents the total audio energy of the media source over the lifetime of the stats object.

[totalSamplesDuration](/en-US/docs/Web/API/RTCAudioSourceStats/totalSamplesDuration)ExperimentalOptional

A number that represents the total duration of all samples produced by the media source over the lifetime of the stats object.

### [Common media-source properties](#common_media-source_properties)

The following properties are present in both `RTCAudioSourceStats` and [RTCVideoSourceStats](/en-US/docs/Web/API/RTCVideoSourceStats): 

[trackIdentifier](/en-US/docs/Web/API/RTCAudioSourceStats/trackIdentifier)

A string that contains the [id](/en-US/docs/Web/API/MediaStreamTrack/id) value of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) associated with the audio source.

[kind](/en-US/docs/Web/API/RTCAudioSourceStats/kind)

A string indicating whether this object represents stats for a video source or a media source. For an `RTCAudioSourceStats` this will always be `audio`.

### [Common instance properties](#common_instance_properties)

The following properties are common to all statistics objects. 

[id](/en-US/docs/Web/API/RTCAudioSourceStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCAudioSourceStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCAudioSourceStats/type)

A string with the value `"media-source"`, indicating that the object is an instance of either `RTCAudioSourceStats` or [RTCVideoSourceStats](/en-US/docs/Web/API/RTCVideoSourceStats).

## [Description](#description)

The interface provides statistics about an audio media source attached to one or more senders. The information includes the current audio level, averaged over a short (implementation dependent) duration.

The statistics also include the accumulated total energy and total sample duration, at a particular timestamp. The totals can be used to determine the average audio level over the lifetime of the stats object. You can calculate a root mean square (RMS) value in the same units as `audioLevel` using the following formula:

totalAudioEnergytotalSamplesDuration\sqrt{\frac{totalAudioEnergy}{totalSamplesDuration}}

You can also use the accumulated totals to calculate the average audio level over an arbitrary time period.

The total audio energy of the stats object is accumulated by adding the energy of every sample over the lifetime of the stats object, while the total duration is accumulated by adding the duration of each sample. The energy of each sample is determined using the following formula, where `sample_level` is the level of the sample, `max_level` is the highest-intensity encodable value, and `duration` is the duration of the sample in seconds:

duration×(sample_levelmax_level)2duration \times⁢ \left(\left(\right. \frac{sample{\_}level}{max{\_}level} \left.\right)\right)^{2}

The average audio level between any two different `getStats()` calls, over any duration, can be calculated using the following equation:

totalAudioEnergy2-totalAudioEnergy1totalSamplesDuration2-totalSamplesDuration1\sqrt{\frac{\left(totalAudioEnergy\right)_{2} - \left(totalAudioEnergy\right)_{1}}{\left(totalSamplesDuration\right)_{2} - \left(totalSamplesDuration\right)_{1}}}

## [Examples](#examples)

This example shows how you might iterate the stats object returned from `RTCRtpSender.getStats()` to get the audio source stats, and then extract the `audioLevel`.

js

```
// where sender is an RTCRtpSender
const stats = await sender.getStats();
let audioSourceStats = null;

stats.forEach((report) => {
  if (report.type === "media-source" && report.kind==="audio") {
    audioSourceStats = report;
    break;
  }
});

const audioLevel = audioSourceStats?.audioLevel;
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcaudiosourcestats](https://w3c.github.io/webrtc-stats/#dom-rtcaudiosourcestats)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCAudioSourceStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcaudiosourcestats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCAudioSourceStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcaudiosourcestats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCAudioSourceStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcaudiosourcestats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
