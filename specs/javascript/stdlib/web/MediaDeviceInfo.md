# MediaDeviceInfo

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDeviceInfo&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MediaDeviceInfo` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) contains information that describes a single media input or output device.

The list of devices obtained by calling [navigator.mediaDevices.enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices) is an array of `MediaDeviceInfo` objects, one per media device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[MediaDeviceInfo.deviceId](/en-US/docs/Web/API/MediaDeviceInfo/deviceId)Read only

Returns a string that is an identifier for the represented device that is persisted across sessions. It is un-guessable by other applications and unique to the origin of the calling application. It is reset when the user clears cookies (for Private Browsing, a different identifier is used that is not persisted across sessions).

[MediaDeviceInfo.groupId](/en-US/docs/Web/API/MediaDeviceInfo/groupId)Read only

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.

[MediaDeviceInfo.kind](/en-US/docs/Web/API/MediaDeviceInfo/kind)Read only

Returns an enumerated value that is either `"videoinput"`, `"audioinput"` or `"audiooutput"`.

[MediaDeviceInfo.label](/en-US/docs/Web/API/MediaDeviceInfo/label)Read only

Returns a string describing this device (for example "External USB Webcam").

Note: For security reasons, the `label` field is always blank unless an active media stream exists or the user has granted persistent permission for media device access. The set of device labels could otherwise be used as part of a [fingerprinting](/en-US/docs/Glossary/Fingerprinting) mechanism to identify a user.

## [Instance methods](#instance_methods)

[MediaDeviceInfo.toJSON()](/en-US/docs/Web/API/MediaDeviceInfo/toJSON)

Returns a JSON representation of the `MediaDeviceInfo` object.

## [Example](#example)

Here's an example that uses [enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices) to get a list of devices.

js

```
if (!navigator.mediaDevices || !navigator.mediaDevices.enumerateDevices) {
  console.log("enumerateDevices() not supported.");
} else {
  // List cameras and microphones.
  navigator.mediaDevices
    .enumerateDevices()
    .then((devices) => {
      devices.forEach((device) => {
        console.log(`${device.kind}: ${device.label} id = ${device.deviceId}`);
      });
    })
    .catch((err) => {
      console.log(`${err.name}: ${err.message}`);
    });
}
```

This might produce:

bash

```
videoinput: id = csO9c0YpAf274OuCPUA53CNE0YHlIr2yXCi+SqfBZZ8=
audioinput: id = RKxXByjnabbADGQNNZqLVLdmXlS0YkETYCIbg+XxnvM=
audioinput: id = r2/xw1xUPIyZunfV1lGrKOma5wTOvCkWfZ368XCndm0=
```

or if one or more media streams are active, or if persistent permissions have been granted:

bash

```
videoinput: FaceTime HD Camera (Built-in) id=csO9c0YpAf274OuCPUA53CNE0YHlIr2yXCi+SqfBZZ8=
audioinput: default (Built-in Microphone) id=RKxXByjnabbADGQNNZqLVLdmXlS0YkETYCIbg+XxnvM=
audioinput: Built-in Microphone id=r2/xw1xUPIyZunfV1lGrKOma5wTOvCkWfZ368XCndm0=
```

## [Specifications](#specifications)

Specification
[Media Capture and Streams# device-info](https://w3c.github.io/mediacapture-main/#device-info)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [navigator.mediaDevices.enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices)
- [navigator.mediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaDeviceInfo/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediadeviceinfo/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDeviceInfo&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediadeviceinfo%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDeviceInfo%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediadeviceinfo%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfb7587e3e3122630ad6cbd94d834ecadbe0a746%0A*+Document+last+modified%3A+2024-07-26T03%3A44%3A38.000Z%0A%0A%3C%2Fdetails%3E)
