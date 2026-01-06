# RTCSessionDescription

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription&level=high)

The `RTCSessionDescription` interface describes one end of a connection—or potential connection—and how it's configured. Each `RTCSessionDescription` consists of a description [type](/en-US/docs/Web/API/RTCSessionDescription/type) indicating which part of the offer/answer negotiation process it describes and of the [SDP](/en-US/docs/Glossary/SDP) descriptor of the session.

The process of negotiating a connection between two peers involves exchanging `RTCSessionDescription` objects back and forth, with each description suggesting one combination of connection configuration options that the sender of the description supports. Once the two peers agree upon a configuration for the connection, negotiation is complete.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[RTCSessionDescription()](/en-US/docs/Web/API/RTCSessionDescription/RTCSessionDescription)Deprecated

Creates a new `RTCSessionDescription` by specifying the `type` and `sdp`. All methods that accept `RTCSessionDescription` objects also accept objects with the same properties, so you can use a plain object instead of creating an `RTCSessionDescription` instance.

## [Instance properties](#instance_properties)

The `RTCSessionDescription` interface doesn't inherit any properties.

[RTCSessionDescription.type](/en-US/docs/Web/API/RTCSessionDescription/type)Read only

An enum describing the session description's type.

[RTCSessionDescription.sdp](/en-US/docs/Web/API/RTCSessionDescription/sdp)Read only

A string containing the [SDP](/en-US/docs/Glossary/SDP) describing the session.

## [Instance methods](#instance_methods)

The `RTCSessionDescription` doesn't inherit any methods.

[RTCSessionDescription.toJSON()](/en-US/docs/Web/API/RTCSessionDescription/toJSON)

Returns a [JSON](/en-US/docs/Glossary/JSON) description of the object. The values of both properties, [type](/en-US/docs/Web/API/RTCSessionDescription/type) and [sdp](/en-US/docs/Web/API/RTCSessionDescription/sdp), are contained in the generated JSON.

## [Example](#example)

js

```
signalingChannel.onmessage = (evt) => {
  if (!pc) start(false);

  const message = JSON.parse(evt.data);
  if (message.type && message.sdp) {
    pc.setRemoteDescription(
      new RTCSessionDescription(message),
      () => {
        // if we received an offer, we need to answer
        if (pc.remoteDescription.type === "offer") {
          pc.createAnswer(localDescCreated, logError);
        }
      },
      logError,
    );
  } else {
    pc.addIceCandidate(
      new RTCIceCandidate(message.candidate),
      () => {},
      logError,
    );
  }
};
```

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# rtcsessiondescription-class](https://w3c.github.io/webrtc-pc/#rtcsessiondescription-class)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- [RTCPeerConnection.setLocalDescription()](/en-US/docs/Web/API/RTCPeerConnection/setLocalDescription) and [RTCPeerConnection.setRemoteDescription()](/en-US/docs/Web/API/RTCPeerConnection/setRemoteDescription)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 23, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCSessionDescription/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcsessiondescription/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcsessiondescription%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCSessionDescription%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcsessiondescription%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb913cece0d35b5a7d1b5d3f4c628dcbbddfc7435%0A*+Document+last+modified%3A+2024-09-23T04%3A05%3A03.000Z%0A%0A%3C%2Fdetails%3E)
