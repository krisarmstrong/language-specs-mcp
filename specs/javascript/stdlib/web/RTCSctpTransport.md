# RTCSctpTransport

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨May 2023⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCSctpTransport&level=high)

The `RTCSctpTransport` interface provides information which describes a Stream Control Transmission Protocol ([SCTP](/en-US/docs/Glossary/SCTP)) transport. This provides information about limitations of the transport, but also provides a way to access the underlying Datagram Transport Layer Security ([DTLS](/en-US/docs/Glossary/DTLS)) transport over which SCTP packets for all of an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)'s data channels are sent and received.

You don't create `RTCSctpTransport` objects yourself; instead, you get access to the `RTCSctpTransport` for a given `RTCPeerConnection` through its [sctp](/en-US/docs/Web/API/RTCPeerConnection/sctp) property.

Possibly the most useful property on this interface is its [maxMessageSize](/en-US/docs/Web/API/RTCSctpTransport/maxMessageSize) property, which you can use to determine the upper limit on the size of messages you can send over a data channel on the peer connection.

## In this article

- [Instance properties](#instance_properties)
- [Events](#events)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from: [EventTarget](/en-US/docs/Web/API/EventTarget).

[RTCSctpTransport.maxChannels](/en-US/docs/Web/API/RTCSctpTransport/maxChannels)Read only

An integer value indicating the maximum number of [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) objects that can be opened simultaneously.

[RTCSctpTransport.maxMessageSize](/en-US/docs/Web/API/RTCSctpTransport/maxMessageSize)Read only

An integer value indicating the maximum size, in bytes, of a message which can be sent using the [RTCDataChannel.send()](/en-US/docs/Web/API/RTCDataChannel/send) method.

[RTCSctpTransport.state](/en-US/docs/Web/API/RTCSctpTransport/state)Read only

A string enumerated value indicating the state of the SCTP transport.

[RTCSctpTransport.transport](/en-US/docs/Web/API/RTCSctpTransport/transport)Read only

An [RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport) object representing the [DTLS](/en-US/docs/Glossary/DTLS) transport used for the transmission and receipt of data packets.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[statechange](/en-US/docs/Web/API/RTCSctpTransport/statechange_event)

Sent when the [RTCSctpTransport.state](/en-US/docs/Web/API/RTCSctpTransport/state) changes.

## [Instance methods](#instance_methods)

This interface has no methods, but inherits methods from: [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Example](#example)

TBD

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcsctptransport-interface](https://w3c.github.io/webrtc-pc/#rtcsctptransport-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)
- [RTCPeerConnection.sctp](/en-US/docs/Web/API/RTCPeerConnection/sctp)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCSctpTransport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcsctptransport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCSctpTransport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcsctptransport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCSctpTransport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcsctptransport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
