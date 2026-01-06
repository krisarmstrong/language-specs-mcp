# Remote Playback API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRemote_Playback_API&level=not)

The Remote Playback API extends the [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) to enable the control of media played on a remote device.

## In this article

- [Concepts and Usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and Usage](#concepts_and_usage)

Remote playback devices are connected devices such as TVs, projectors, or speakers. The API takes into account wired devices connected via HDMI or DVI, and wireless devices, for example Chromecast or AirPlay.

The API enables a page, which has a media element such as a video or audio file, to initiate and control playback of that media on a connected remote device. For example, playing a video on a connected TV.

Note: Safari for iOS has some APIs which enable remote playback on AirPlay. Details of these can be found in [the Safari 9.0 release notes](https://developer.apple.com/library/archive/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_0.html#//apple_ref/doc/uid/TP40014305-CH9-SW16).

Android versions of Firefox and Chrome also contain some remote playback features. These devices will show a Cast button if there is a Cast device available in the local network.

## [Interfaces](#interfaces)

[RemotePlayback](/en-US/docs/Web/API/RemotePlayback)

Allows the page to detect availability of remote playback devices, then connect to and control playing on these devices.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[HTMLMediaElement.disableRemotePlayback](/en-US/docs/Web/API/HTMLMediaElement/disableRemotePlayback)

A boolean that sets or returns the remote playback state, indicating whether the media element is allowed to have a remote playback UI.

[HTMLMediaElement.remote](/en-US/docs/Web/API/HTMLMediaElement/remote)Read only

Return a [RemotePlayback](/en-US/docs/Web/API/RemotePlayback) object instance associated with the media element.

## [Examples](#examples)

The following example demonstrates a player with custom controls that supports remote playback. Initially the button used to select a device is hidden.

html

```
<video id="videoElement" src="https://example.org/media.ext">
  <button id="deviceBtn" class="hidden">Pick device</button>
</video>
```

css

```
.hidden {
  display: none;
}
```

The [RemotePlayback.watchAvailability()](/en-US/docs/Web/API/RemotePlayback/watchAvailability) method watches for available remote playback devices. If a device is available, use the callback to show the button.

js

```
const deviceBtn = document.getElementById("deviceBtn");
const videoElem = document.getElementById("videoElement");

function availabilityCallback(available) {
  // Show or hide the device picker button depending on device availability.
  if (available) {
    deviceBtn.classList.remove("hidden");
  } else {
    deviceBtn.classList.add("hidden");
  }
}

videoElem.remote.watchAvailability(availabilityCallback).catch(() => {
  // If the device cannot continuously watch available,
  // show the button to allow the user to try to prompt for a connection.
  deviceBtn.style.display = "inline";
});
```

## [Specifications](#specifications)

Specification[Remote Playback API](https://w3c.github.io/remote-playback/)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Remote_Playback_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/remote_playback_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRemote_Playback_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fremote_playback_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRemote_Playback_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fremote_playback_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F754b68246f4e69e404309fee4a1699e047e43994%0A*+Document+last+modified%3A+2025-11-17T16%3A52%3A01.000Z%0A%0A%3C%2Fdetails%3E)
