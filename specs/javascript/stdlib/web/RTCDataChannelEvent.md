# RTCDataChannelEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannelEvent&level=high)

The `RTCDataChannelEvent` interface represents an event related to a specific [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[RTCDataChannelEvent()](/en-US/docs/Web/API/RTCDataChannelEvent/RTCDataChannelEvent)

Creates a new `RTCDataChannelEvent`.

## [Instance properties](#instance_properties)

Also inherits properties from [Event](/en-US/docs/Web/API/Event).

[channel](/en-US/docs/Web/API/RTCDataChannelEvent/channel)Read only

Returns the [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) associated with the event.

## [Examples](#examples)

In this example, the `datachannel` event handler is set up to save the data channel reference and set up handlers for the events which need to be monitored. The [channel](/en-US/docs/Web/API/RTCDataChannelEvent/channel) property provides the [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) representing the connection to the other peer.

js

```
pc.ondatachannel = (event) => {
  inboundDataChannel = event.channel;
  inboundDataChannel.onmessage = handleIncomingMessage;
  inboundDataChannel.onopen = handleChannelOpen;
  inboundDataChannel.onclose = handleChannelClose;
};
```

See [A simple RTCDataChannel sample](/en-US/docs/Web/API/WebRTC_API/Simple_RTCDataChannel_sample) for another, more complete, example of how to use data channels.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcdatachannelevent](https://w3c.github.io/webrtc-pc/#rtcdatachannelevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel)
- [A simple RTCDataChannel sample](/en-US/docs/Web/API/WebRTC_API/Simple_RTCDataChannel_sample)
- [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) (the target interface for [datachannel](/en-US/docs/Web/API/RTCPeerConnection/datachannel_event) events)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 1, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/RTCDataChannelEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcdatachannelevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannelEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcdatachannelevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannelEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcdatachannelevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3b22c657f659c249cbe6e4fc6794370a5cb67a72%0A*+Document+last+modified%3A+2023-03-01T11%3A11%3A40.000Z%0A%0A%3C%2Fdetails%3E)
