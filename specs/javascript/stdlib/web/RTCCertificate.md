# RTCCertificate

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCertificate&level=high)

The `RTCCertificate` interface of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) provides an object representing a certificate that an [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) uses to authenticate.

`RTCCertificate` is a [serializable object](/en-US/docs/Glossary/Serializable_object), so it can be cloned with [structuredClone()](/en-US/docs/Web/API/Window/structuredClone) or copied between [Workers](/en-US/docs/Web/API/Worker) using [postMessage()](/en-US/docs/Web/API/Worker/postMessage).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[RTCCertificate.expires](/en-US/docs/Web/API/RTCCertificate/expires)Read only

Returns the expiration date of the certificate.

## [Instance methods](#instance_methods)

[RTCCertificate.getFingerprints()](/en-US/docs/Web/API/RTCCertificate/getFingerprints)

Returns an array of certificate fingerprints, calculated using the different algorithms supported by the browser.

## [Specifications](#specifications)

Specification
[WebRTC: Real-Time Communication in Browsers# dom-rtccertificate](https://w3c.github.io/webrtc-pc/#dom-rtccertificate)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCPeerConnection.RTCPeerConnection() argument configuration.certificates](/en-US/docs/Web/API/RTCPeerConnection/RTCPeerConnection#certificates)
- [RTCPeerConnection.generateCertificate()](/en-US/docs/Web/API/RTCPeerConnection/generateCertificate_static)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/RTCCertificate/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtccertificate/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCertificate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtccertificate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCertificate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtccertificate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8b6cec0ceff01e7a9d6865cf5306788e15cce4b8%0A*+Document+last+modified%3A+2024-09-26T23%3A32%3A56.000Z%0A%0A%3C%2Fdetails%3E)
