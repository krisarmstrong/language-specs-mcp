# InputDeviceInfo

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceInfo&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `InputDeviceInfo` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) gives access to the capabilities of the input device that it represents.

`InputDeviceInfo` objects are returned by [MediaDevices.enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices) if the returned device is an audio or video input device.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [MediaDeviceInfo](/en-US/docs/Web/API/MediaDeviceInfo).

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [MediaDeviceInfo](/en-US/docs/Web/API/MediaDeviceInfo).

[InputDeviceInfo.getCapabilities()](/en-US/docs/Web/API/InputDeviceInfo/getCapabilities)

Returns a `MediaTrackCapabilities` object describing the primary audio or video track of a device's `MediaStream`.

## [Examples](#examples)

The following example gets all media devices with [MediaDevices.enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices). If any of the devices are input devices then `console.log(device)` will print an `InputDeviceInfo` object to the console.

js

```
navigator.mediaDevices.enumerateDevices().then((devices) => {
  devices.forEach((device) => {
    console.log(device); // an InputDeviceInfo object if the device is an input device, otherwise a MediaDeviceInfo object.
  });
});
```

## [Specifications](#specifications)

Specification
[Media Capture and Streams# dom-inputdeviceinfo](https://w3c.github.io/mediacapture-main/#dom-inputdeviceinfo)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 6, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/InputDeviceInfo/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/inputdeviceinfo/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceInfo&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Finputdeviceinfo%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FInputDeviceInfo%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Finputdeviceinfo%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4232f4067388fc9b2c55c5f9200dddf05bd99b74%0A*+Document+last+modified%3A+2024-01-06T06%3A27%3A18.000Z%0A%0A%3C%2Fdetails%3E)
