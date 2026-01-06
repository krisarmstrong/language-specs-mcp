# MediaCapabilities

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaCapabilities&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `MediaCapabilities` interface of the [Media Capabilities API](/en-US/docs/Web/API/Media_Capabilities_API) provides information about the decoding abilities of the device, system and browser. The API can be used to query the browser about the decoding abilities of the device based on codecs, profile, resolution, and bitrates. The information can be used to serve optimal media streams to the user and determine if playback should be smooth and power efficient.

The information is accessed through the `mediaCapabilities` property of the [Navigator](/en-US/docs/Web/API/Navigator) and [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator) interface.

## In this article

- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[MediaCapabilities.encodingInfo()](/en-US/docs/Web/API/MediaCapabilities/encodingInfo)

When passed a valid media configuration, it returns a promise with information as to whether the media type is supported, and whether encoding such media would be smooth and power efficient.

[MediaCapabilities.decodingInfo()](/en-US/docs/Web/API/MediaCapabilities/decodingInfo)

When passed a valid media configuration, it returns a promise with information as to whether the media type is supported, and whether decoding such media would be smooth and power efficient.

## [Specifications](#specifications)

Specification
[Media Capabilities# media-capabilities-interface](https://w3c.github.io/media-capabilities/#media-capabilities-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement)'s method [canPlayType()](/en-US/docs/Web/API/HTMLMediaElement/canPlayType)
- [MediaSource](/en-US/docs/Web/API/MediaSource)'s method [isTypeSupported()](/en-US/docs/Web/API/MediaSource/isTypeSupported_static)
- [Navigator](/en-US/docs/Web/API/Navigator) interface

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaCapabilities/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediacapabilities/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaCapabilities&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediacapabilities%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaCapabilities%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediacapabilities%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F49f6e40b12be0d6d897d3dab09caafbc093f7677%0A*+Document+last+modified%3A+2024-10-08T19%3A37%3A56.000Z%0A%0A%3C%2Fdetails%3E)
