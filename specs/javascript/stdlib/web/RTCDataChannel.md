# RTCDataChannel

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannel&level=high)

The `RTCDataChannel` interface represents a network channel which can be used for bidirectional peer-to-peer transfers of arbitrary data. Every data channel is associated with an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), and each peer connection can have up to a theoretical maximum of 65,534 data channels (the actual limit may vary from browser to browser).

To create a data channel and ask a remote peer to join you, call the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)'s [createDataChannel()](/en-US/docs/Web/API/RTCPeerConnection/createDataChannel) method. The peer being invited to exchange data receives a [datachannel](/en-US/docs/Web/API/RTCPeerConnection/datachannel_event) event (which has type [RTCDataChannelEvent](/en-US/docs/Web/API/RTCDataChannelEvent)) to let it know the data channel has been added to the connection.

`RTCDataChannel` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Data format](#data_format)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from [EventTarget](/en-US/docs/Web/API/EventTarget).

[binaryType](/en-US/docs/Web/API/RTCDataChannel/binaryType)

A string specifying the type of object that should be used to represent binary data received on the `RTCDataChannel`. Values are the same as allowed on the [WebSocket.binaryType](/en-US/docs/Web/API/WebSocket/binaryType) property: `blob` if [Blob](/en-US/docs/Web/API/Blob) objects are being used, or `arraybuffer` if [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) objects are being used. The default is `arraybuffer`.

[bufferedAmount](/en-US/docs/Web/API/RTCDataChannel/bufferedAmount)Read only

Returns the number of bytes of data currently queued to be sent over the data channel.

[bufferedAmountLowThreshold](/en-US/docs/Web/API/RTCDataChannel/bufferedAmountLowThreshold)

Specifies the number of bytes of buffered outgoing data that is considered "low". The default value is 0.

[id](/en-US/docs/Web/API/RTCDataChannel/id)Read only

Returns an ID number (between 0 and 65,534) which uniquely identifies the `RTCDataChannel`.

[label](/en-US/docs/Web/API/RTCDataChannel/label)Read only

Returns a string that contains a name describing the data channel. These labels are not required to be unique.

[maxPacketLifeTime](/en-US/docs/Web/API/RTCDataChannel/maxPacketLifeTime)Read only

Returns the amount of time, in milliseconds, the browser is allowed to take to attempt to transmit a message, as set when the data channel was created, or `null`.

[maxRetransmits](/en-US/docs/Web/API/RTCDataChannel/maxRetransmits)Read only

Returns the maximum number of times the browser should try to retransmit a message before giving up, as set when the data channel was created, or `null`, which indicates that there is no maximum.

[negotiated](/en-US/docs/Web/API/RTCDataChannel/negotiated)Read only

Indicates whether the `RTCDataChannel`'s connection was negotiated by the Web app (`true`) or by the WebRTC layer (`false`). The default is `false`.

[ordered](/en-US/docs/Web/API/RTCDataChannel/ordered)Read only

Indicates whether or not the data channel guarantees in-order delivery of messages; the default is `true`, which indicates that the data channel is indeed ordered.

[protocol](/en-US/docs/Web/API/RTCDataChannel/protocol)Read only

Returns a string containing the name of the subprotocol in use. If no protocol was specified when the data channel was created, then this property's value is the empty string (`""`).

[readyState](/en-US/docs/Web/API/RTCDataChannel/readyState)Read only

Returns a string which indicates the state of the data channel's underlying data connection. It can have one of the following values: `connecting`, `open`, `closing`, or `closed`.

### [Obsolete properties](#obsolete_properties)

[reliable](/en-US/docs/Web/API/RTCDataChannel/reliable)Read onlyDeprecatedNon-standard

Indicates whether or not the data channel is reliable.

## [Instance methods](#instance_methods)

Also inherits methods from [EventTarget](/en-US/docs/Web/API/EventTarget).

[close()](/en-US/docs/Web/API/RTCDataChannel/close)

Closes the `RTCDataChannel`. Either peer is permitted to call this method to initiate closure of the channel.

[send()](/en-US/docs/Web/API/RTCDataChannel/send)

Sends data across the data channel to the remote peer.

## [Events](#events)

[bufferedamountlow](/en-US/docs/Web/API/RTCDataChannel/bufferedamountlow_event)

Sent when the number of bytes of data in the outgoing data buffer falls below the value specified by [bufferedAmountLowThreshold](/en-US/docs/Web/API/RTCDataChannel/bufferedAmountLowThreshold).

[close](/en-US/docs/Web/API/RTCDataChannel/close_event)

Sent when the underlying data transport closes.

[closing](/en-US/docs/Web/API/RTCDataChannel/closing_event)

Sent when the underlying data transport is about to start closing.

[error](/en-US/docs/Web/API/RTCDataChannel/error_event)

Sent when an error occurs on the data channel.

[message](/en-US/docs/Web/API/RTCDataChannel/message_event)

Sent when a message has been received from the remote peer. The message contents can be found in the event's [data](/en-US/docs/Web/API/MessageEvent/data) property.

[open](/en-US/docs/Web/API/RTCDataChannel/open_event)

Sent when the data channel is first opened, or when an existing data channel's underlying connection re-opens.

## [Data format](#data_format)

The underlying data format is defined by the IEEE specification [SDP Offer/Answer Procedures for SCTP over DTLS Transport(RFC 8841)](https://datatracker.ietf.org/doc/rfc8841/). The current format specifies its protocol as either `"UDP/DTLS/SCTP"` (UDP carrying DTLS carrying SCTP) or `"TCP/DTLS/SCTP"` (TCP carrying DTLS carrying SCTP). Older browsers may only specify `"DTLS/SCTP"`.

## [Example](#example)

js

```
const pc = new RTCPeerConnection();
const dc = pc.createDataChannel("my channel");

dc.onmessage = (event) => {
  console.log(`received: ${event.data}`);
};

dc.onopen = () => {
  console.log("datachannel open");
};

dc.onclose = () => {
  console.log("datachannel close");
};
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcdatachannel](https://w3c.github.io/webrtc-pc/#rtcdatachannel)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 29, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCDataChannel/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcdatachannel/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcdatachannel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDataChannel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcdatachannel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fea27e601462e6435fa35773a5b0504fe78b5cfa5%0A*+Document+last+modified%3A+2025-01-29T00%3A48%3A15.000Z%0A%0A%3C%2Fdetails%3E)
