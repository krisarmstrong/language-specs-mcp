# RTCIceCandidatePair

The `RTCIceCandidatePair` dictionary describes a pair of ICE candidates which together comprise a description of a viable connection between two WebRTC endpoints. It is used as the return value from [RTCIceTransport.getSelectedCandidatePair()](/en-US/docs/Web/API/RTCIceTransport/getSelectedCandidatePair) to identify the currently-selected candidate pair identified by the ICE agent.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[local](/en-US/docs/Web/API/RTCIceCandidatePair/local)

An [RTCIceCandidate](/en-US/docs/Web/API/RTCIceCandidate) describing the configuration of the local end of the connection.

[remote](/en-US/docs/Web/API/RTCIceCandidatePair/remote)

The `RTCIceCandidate` describing the configuration of the remote end of the connection.

## [Examples](#examples)

See [RTCIceTransport.onselectedcandidatepairchange](/en-US/docs/Web/API/RTCIceTransport/selectedcandidatepairchange_event#examples) for example code.

## [Specifications](#specifications)

This feature does not appear to be defined in any specification.

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 6, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/RTCIceCandidatePair/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtcicecandidatepair/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidatePair&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtcicecandidatepair%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCIceCandidatePair%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtcicecandidatepair%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffa1301aead2cee37516b7ad5a5ec2fb21e004227%0A*+Document+last+modified%3A+2023-04-06T05%3A00%3A32.000Z%0A%0A%3C%2Fdetails%3E)
