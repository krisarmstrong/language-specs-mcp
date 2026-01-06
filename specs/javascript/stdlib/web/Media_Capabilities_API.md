# Media Capabilities API

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Capabilities_API&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The Media Capabilities API allows developers to determine decoding and encoding abilities of the device, exposing information such as whether media is supported and whether playback should be smooth and power efficient, with real time feedback about playback to better enable adaptive streaming, and access to display property information.

## In this article

- [Concepts](#concepts)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts](#concepts)

There are a myriad of video and audio codecs. Different browsers support different media types and new media types are always being developed. With the Media Capabilities API, developers can ensure each user is getting the best bitrate and storage savings for their browser, device, and OS capabilities.

Whether a device uses hardware or software decoding impacts how smooth and power efficient the video decoding is and how efficient the playback will be. The Media Capabilities API enables determining which codecs are supported and how performant a media file will be both in terms of smoothness and power efficiency.

The Media Capabilities API provide more powerful features than say [MediaRecorder.isTypeSupported()](/en-US/docs/Web/API/MediaRecorder/isTypeSupported_static) or [HTMLMediaElement.canPlayType()](/en-US/docs/Web/API/HTMLMediaElement/canPlayType), which only address general browser support, not performance. The API also provides abilities to access display property information such as supported color [gamut](/en-US/docs/Glossary/Gamut), dynamic range abilities, and real-time feedback about the playback.

To test support, smoothness, and power efficiency for encoding and decoding video or audio content, you use the [MediaCapabilities](/en-US/docs/Web/API/MediaCapabilities) interface's [encodingInfo()](/en-US/docs/Web/API/MediaCapabilities/encodingInfo) and [decodingInfo()](/en-US/docs/Web/API/MediaCapabilities/decodingInfo) methods.

Media capabilities information enables websites to enable adaptive streaming to alter the quality of content based on actual user-perceived quality, and react to a pick of CPU/GPU usage in real time.

## [Interfaces](#interfaces)

[MediaCapabilities](/en-US/docs/Web/API/MediaCapabilities)

Provides information about the decoding abilities of the device, system and browser based on codecs, profile, resolution, and bitrates. The information can be used to serve optimal media streams to the user and determine if playback should be smooth and power efficient.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[Navigator.mediaCapabilities](/en-US/docs/Web/API/Navigator/mediaCapabilities)Read only

A [MediaCapabilities](/en-US/docs/Web/API/MediaCapabilities) object that can expose information about the decoding and encoding capabilities for a given media format and output capabilities.

[WorkerNavigator.mediaCapabilities](/en-US/docs/Web/API/WorkerNavigator/mediaCapabilities)Read only

A [MediaCapabilities](/en-US/docs/Web/API/MediaCapabilities) object that can expose information about the decoding and encoding capabilities for a given media format and output capabilities.

## [Examples](#examples)

### [Detect audio file support and expected performance](#detect_audio_file_support_and_expected_performance)

This example defines an audio configuration then checks to see if the user agent supports decoding that media configuration, and whether it will perform well in terms of smoothness and power efficiency.

js

```
if ("mediaCapabilities" in navigator) {
  const audioFileConfiguration = {
    type: "file",
    audio: {
      contentType: "audio/mp3",
      channels: 2,
      bitrate: 132700,
      samplerate: 5200,
    },
  };

  navigator.mediaCapabilities
    .decodingInfo(audioFileConfiguration)
    .then((result) => {
      console.log(
        `This configuration is ${result.supported ? "" : "not "}supported,`,
      );
      console.log(`${result.smooth ? "" : "not "}smooth, and`);
      console.log(`${result.powerEfficient ? "" : "not "}power efficient.`);
    })
    .catch(() => {
      console.log(`decodingInfo error: ${contentType}`);
    });
}
```

## [Specifications](#specifications)

Specification
[Media Capabilities# media-capabilities-interface](https://w3c.github.io/media-capabilities/#media-capabilities-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement)'s method [canPlayType()](/en-US/docs/Web/API/HTMLMediaElement/canPlayType)
- [MediaSource](/en-US/docs/Web/API/MediaSource)'s method [isTypeSupported()](/en-US/docs/Web/API/MediaSource/isTypeSupported_static)
- [Using the Media Capabilities API](/en-US/docs/Web/API/Media_Capabilities_API/Using_the_Media_Capabilities_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Media_Capabilities_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/media_capabilities_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Capabilities_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmedia_capabilities_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Capabilities_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmedia_capabilities_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F49f6e40b12be0d6d897d3dab09caafbc093f7677%0A*+Document+last+modified%3A+2024-10-08T19%3A37%3A56.000Z%0A%0A%3C%2Fdetails%3E)
