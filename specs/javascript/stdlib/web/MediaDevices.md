# MediaDevices

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `MediaDevices` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) provides access to connected media input devices like cameras and microphones, as well as screen sharing. In essence, it lets you obtain access to any hardware source of media data.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices)

Obtains an array of information about the media input and output devices available on the system.

[getSupportedConstraints()](/en-US/docs/Web/API/MediaDevices/getSupportedConstraints)

Returns an object conforming to [MediaTrackSupportedConstraints](/en-US/docs/Web/API/MediaTrackSupportedConstraints) indicating which constrainable properties are supported on the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) interface. See [Media Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API/Constraints) to learn more about constraints and how to use them.

[getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)

Prompts the user to select a display or portion of a display (such as a window) to capture as a [MediaStream](/en-US/docs/Web/API/MediaStream) for sharing or recording purposes. Returns a promise that resolves to a `MediaStream`.

[getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)

With the user's permission through a prompt, turns on a camera and/or a microphone on the system and provides a [MediaStream](/en-US/docs/Web/API/MediaStream) containing a video track and/or an audio track with the input.

[selectAudioOutput()](/en-US/docs/Web/API/MediaDevices/selectAudioOutput)Experimental

Prompts the user to select a specific audio output device.

## [Events](#events)

[devicechange](/en-US/docs/Web/API/MediaDevices/devicechange_event)

Fired when a media input or output device is attached to or removed from the user's computer.

## [Example](#example)

js

```
// Put variables in global scope to make them available to the browser console.
const video = document.querySelector("video");
const constraints = {
  audio: false,
  video: true,
};

navigator.mediaDevices
  .getUserMedia(constraints)
  .then((stream) => {
    const videoTracks = stream.getVideoTracks();
    console.log("Got stream with constraints:", constraints);
    console.log(`Using video device: ${videoTracks[0].label}`);
    stream.onremovetrack = () => {
      console.log("Stream ended");
    };
    video.srcObject = stream;
  })
  .catch((error) => {
    if (error.name === "OverconstrainedError") {
      console.error(
        `The resolution ${constraints.video.width.exact}x${constraints.video.height.exact} px is not supported by your device.`,
      );
    } else if (error.name === "NotAllowedError") {
      console.error(
        "You need to grant this page permission to access your camera and microphone.",
      );
    } else {
      console.error(`getUserMedia error: ${error.name}`, error);
    }
  });
```

## [Specifications](#specifications)

Specification
[Media Capture and Streams# mediadevices](https://w3c.github.io/mediacapture-main/#mediadevices)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API): The API this interface is part of.
- [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API): The API defining the [getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia) method.
- [WebRTC API](/en-US/docs/Web/API/WebRTC_API)
- [Navigator.mediaDevices](/en-US/docs/Web/API/Navigator/mediaDevices): Returns a reference to a `MediaDevices` object that can be used to access devices.
- [CameraCaptureJS:](https://github.com/chrisjohndigital/CameraCaptureJS) HTML video capture and playback using `MediaDevices` and the MediaStream Recording API
- [OpenLang](https://github.com/chrisjohndigital/OpenLang): HTML video language lab web application using `MediaDevices` and the MediaStream Recording API for video recording

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 5, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaDevices/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediadevices/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediadevices%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaDevices%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediadevices%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb2875dbaa70efb5850084b9802803b439db325f5%0A*+Document+last+modified%3A+2024-02-05T22%3A31%3A22.000Z%0A%0A%3C%2Fdetails%3E)
