# RTCCertificateStats

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCertificateStats&level=not)

The `RTCCertificateStats` dictionary of the [WebRTC API](/en-US/docs/Web/API/WebRTC_API) is used to report information about a certificate used by an [RTCDtlsTransport](/en-US/docs/Web/API/RTCDtlsTransport) and its underlying [RTCIceTransport](/en-US/docs/Web/API/RTCIceTransport).

The report can be obtained by iterating the [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport) returned by [RTCPeerConnection.getStats()](/en-US/docs/Web/API/RTCPeerConnection/getStats) until you find an entry with the [type](/en-US/docs/Web/API/RTCCertificateStats/type) of `certificate`.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[fingerprint](/en-US/docs/Web/API/RTCCertificateStats/fingerprint)

A string containing the certificate fingerprint, which is calculated using the hash function specified in [fingerprintAlgorithm](/en-US/docs/Web/API/RTCCertificateStats/fingerprintAlgorithm).

[fingerprintAlgorithm](/en-US/docs/Web/API/RTCCertificateStats/fingerprintAlgorithm)

A string containing the hash function used to compute the certificate [fingerprint](/en-US/docs/Web/API/RTCCertificateStats/fingerprint), such as "sha-256".

[base64Certificate](/en-US/docs/Web/API/RTCCertificateStats/base64Certificate)

A string containing the base-64 representation of the DER-encoded certificate.

### [Common instance properties](#common_instance_properties)

The following properties are common to all WebRTC statistics objects (See [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport#common_instance_properties) for more information).

[id](/en-US/docs/Web/API/RTCCertificateStats/id)

A string that uniquely identifies the object that is being monitored to produce this set of statistics.

[timestamp](/en-US/docs/Web/API/RTCCertificateStats/timestamp)

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) object indicating the time at which the sample was taken for this statistics object.

[type](/en-US/docs/Web/API/RTCCertificateStats/type)

A string with the value `"certificate"`, indicating the type of statistics that the object contains.

## [Examples](#examples)

Given a variable `myPeerConnection`, which is an instance of [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection), the code below uses `await` to wait for the statistics report, and then iterates it using `RTCStatsReport.forEach()`. It then filters the dictionaries for just those reports that have the type of `certificate` and logs the result.

js

```
const stats = await myPeerConnection.getStats();

stats.forEach((report) => {
  if (report.type === "certificate") {
    // Log the certificate information
    console.log(report);
  }
});
```

## [Specifications](#specifications)

Specification
[Identifiers for WebRTC's Statistics API# dom-rtcstatstype-certificate](https://w3c.github.io/webrtc-stats/#dom-rtcstatstype-certificate)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [RTCStatsReport](/en-US/docs/Web/API/RTCStatsReport)
- [RTCCertificate](/en-US/docs/Web/API/RTCCertificate)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 2, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RTCCertificateStats/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/rtccertificatestats/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCertificateStats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Frtccertificatestats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRTCCertificateStats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Frtccertificatestats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F848771d9efdc57ad84d643081cf91e89355c751b%0A*+Document+last+modified%3A+2025-04-02T13%3A22%3A23.000Z%0A%0A%3C%2Fdetails%3E)
