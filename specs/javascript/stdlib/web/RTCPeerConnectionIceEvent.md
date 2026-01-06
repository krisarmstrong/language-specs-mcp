# RTCPeerConnectionIceEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2018⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionIceEvent&level=high)

The `RTCPeerConnectionIceEvent` interface represents events that occur in relation to [ICE](/en-US/docs/Glossary/ICE) candidates with the target, usually an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

Only one event is of this type: [icecandidate](/en-US/docs/Web/API/RTCPeerConnection/icecandidate_event).

## In this article

- [Instance properties](#instance_properties)
- [Constructors](#constructors)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

A `RTCPeerConnectionIceEvent` being an [Event](/en-US/docs/Web/API/Event), this event also implements these properties.

[RTCPeerConnectionIceEvent.candidate](/en-US/docs/Web/API/RTCPeerConnectionIceEvent/candidate)Read only

Contains the [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate) containing the candidate associated with the event, or `null` if this event indicates that there are no further candidates to come.

## [Constructors](#constructors)

[RTCPeerConnectionIceEvent()](/en-US/docs/Web/API/RTCPeerConnectionIceEvent/RTCPeerConnectionIceEvent)

Returns a new `RTCPeerConnectionIceEvent`. It takes two parameters, the first being a string representing the type of the event; the second a dictionary containing the [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate) it refers to.

## [Instance methods](#instance_methods)

A `RTCPeerConnectionIceEvent` being an [Event](/en-US/docs/Web/API/Event), this event also implements these properties. There is no specific [RTCDataChannelEvent](/en-US/docs/Web/API/RTCDataChannelEvent) method.

## [Examples](#examples)

js

```
pc.onicecandidate = (ev) => {
  console.log(
    `The ICE candidate ('${ev.candidate.candidate}') added to connection.`,
  );
};
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcpeerconnectioniceevent](https://w3c.github.io/webrtc-pc/#rtcpeerconnectioniceevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- Its usual target: [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 16, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCPeerConnectionIceEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcpeerconnectioniceevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionIceEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcpeerconnectioniceevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCPeerConnectionIceEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcpeerconnectioniceevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F00f46adb5616d826821d63b11eac285faf1cf4a5%0A*+Document+last+modified%3A+2024-10-16T07%3A58%3A28.000Z%0A%0A%3C%2Fdetails%3E)
