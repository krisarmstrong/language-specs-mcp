# RTCDtlsTransport

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2022⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDtlsTransport&level=high)

The `RTCDtlsTransport` interface provides access to information about the Datagram Transport Layer Security ([DTLS](/en-US/docs/Glossary/DTLS)) transport over which a [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection)'s [RTP](/en-US/docs/Glossary/RTP) and [RTCP](/en-US/docs/Glossary/RTCP) packets are sent and received by its [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) and [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver) objects.

A `RTCDtlsTransport` object is also used to provide information about [SCTP](/en-US/docs/Glossary/SCTP) packets transmitted and received by a connection's [data channels](/en-US/docs/Web/API/RTCDataChannel).

Features of the DTLS transport include the addition of security to the underlying transport; the `RTCDtlsTransport` interface can be used to obtain information about the underlying transport and the security added to it by the DTLS layer.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from [EventTarget](/en-US/docs/Web/API/EventTarget).

[iceTransport](/en-US/docs/Web/API/RTCDtlsTransport/iceTransport)Read only

Returns a reference to the underlying [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport) object.

[state](/en-US/docs/Web/API/RTCDtlsTransport/state)Read only

Returns a string which describes the underlying Datagram Transport Layer Security ([DTLS](/en-US/docs/Glossary/DTLS)) transport state. It can be one of the following values: `new`, `connecting`, `connected`, `closed`, or `failed`.

## [Instance methods](#instance_methods)

Also inherits methods from [EventTarget](/en-US/docs/Web/API/EventTarget).

`getRemoteCertificates()`

Returns an array of [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) containing the certificates of the remote peer of the connection.

## [Events](#events)

[error](/en-US/docs/Web/API/RTCDtlsTransport/error_event)

Sent when a transport-level error occurs on the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

`statechange`

Sent when the [state](/en-US/docs/Web/API/RTCDtlsTransport/state) of the DTLS transport changes.

## [Description](#description)

### [Allocation of DTLS transports](#allocation_of_dtls_transports)

`RTCDtlsTransport` objects are created when an app calls either [setLocalDescription()](/en-US/docs/Web/API/RTCPeerConnection/setLocalDescription) or [setRemoteDescription()](/en-US/docs/Web/API/RTCPeerConnection/setRemoteDescription). The number of DTLS transports created and how they're used depends on the bundling mode used when creating the [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

Whether bundling is used depends on what the other endpoint is able to negotiate. All browsers support bundling, so when both endpoints are browsers, you can rest assured that bundling will be used.

Some non-browser legacy endpoints, however, may not support bundle. To be able to negotiate with such endpoints (or to exclude them entirely), the `bundlePolicy` property may be provided when creating the connection. The `bundlePolicy` lets you control how to negotiate with these legacy endpoints. The default policy is `"balanced"`, which provides a balance between performance and compatibility.

For example, to create the connection using the highest level of bundling:

js

```
const rtcConfig = {
  bundlePolicy: "max-bundle",
};

const pc = new RTCPeerConnection(rtcConfig);
```

[Bundling](https://datatracker.ietf.org/doc/rfc8843/) lets you use one `RTCDtlsTransport` to carry the data for multiple higher-level transports, such as multiple [RTCRtpTransceiver](/en-US/docs/Web/API/RTCRtpTransceiver)s.

#### When not using BUNDLE

When the connection is created without using BUNDLE, each RTP or RTCP component of each [RTCRtpTransceiver](/en-US/docs/Web/API/RTCRtpTransceiver) has its own `RTCDtlsTransport`; that is, every [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender) and [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver), has its own transport, and all [RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel) objects share a transport dedicated to SCTP.

#### When using BUNDLE

When the connection is using BUNDLE, each `RTCDtlsTransport` object represents a group of [RTCRtpTransceiver](/en-US/docs/Web/API/RTCRtpTransceiver) objects. If the connection was created using `max-compat` mode, each transport is responsible for handling all communication for a given type of media (audio, video, or data channel). Thus, a connection with any number of audio and video channels will always have exactly one DTLS transport for audio and one for video communications.

Because transports are established early in the negotiation process, it's likely that it won't be known until after they're created whether or not the remote peer supports bundling. For this reason, you'll sometimes see separate transports created at first, one for each track, then see them get bundled up once it's known that bundling is possible. If your code accesses [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)s and/or [RTCRtpReceiver](/en-US/docs/Web/API/RTCRtpReceiver)s directly, you may encounter situations where they're initially separate, then half or more of them get closed and the senders and receivers updated to refer to the appropriate remaining `RTCDtlsTransport` objects.

### [Data channels](#data_channels)

[RTCDataChannel](/en-US/docs/Web/API/RTCDataChannel)s use [SCTP](/en-US/docs/Glossary/SCTP) to communicate. All of a peer connection's data channels share a single [RTCSctpTransport](/en-US/docs/Web/API/RTCSctpTransport), found in the connection's [sctp](/en-US/docs/Web/API/RTCPeerConnection/sctp) property.

You can, in turn, identify the `RTCDtlsTransport` used to securely encapsulate the data channels' SCTP communications by looking at the `RTCSctpTransport` object's [transport](/en-US/docs/Web/API/RTCSctpTransport/transport) property.

## [Examples](#examples)

This example presents a function, `tallySenders()`, which iterates over an `RTCPeerConnection`'s [RTCRtpSender](/en-US/docs/Web/API/RTCRtpSender)s, tallying up how many of them are in various states. The function returns an object containing properties whose values indicate how many senders are in each state.

js

```
let pc = new RTCPeerConnection({ bundlePolicy: "max-bundle" });

// …

function tallySenders(pc) {
  let results = {
    transportMissing: 0,
    connectionPending: 0,
    connected: 0,
    closed: 0,
    failed: 0,
    unknown: 0,
  };

  let senderList = pc.getSenders();
  senderList.forEach((sender) => {
    let transport = sender.transport;

    if (!transport) {
      results.transportMissing++;
    } else {
      switch (transport.state) {
        case "new":
        case "connecting":
          results.connectionPending++;
          break;
        case "connected":
          results.connected++;
          break;
        case "closed":
          results.closed++;
          break;
        case "failed":
          results.failed++;
          break;
        default:
          results.unknown++;
          break;
      }
    }
  });
  return results;
}
```

Note that in this code, the `new` and `connecting` states are being treated as a single `connectionPending` status in the returned object.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtcdtlstransport](https://w3c.github.io/webrtc-pc/#dom-rtcdtlstransport)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCRtpSender.transport](/en-US/docs/Web/API/RTCRtpSender/transport) and [RTCRtpReceiver.transport](/en-US/docs/Web/API/RTCRtpReceiver/transport)
- [RTCSctpTransport.transport](/en-US/docs/Web/API/RTCSctpTransport/transport)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCDtlsTransport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcdtlstransport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDtlsTransport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcdtlstransport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCDtlsTransport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcdtlstransport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
