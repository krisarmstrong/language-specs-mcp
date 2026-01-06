# RemotePlayback

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRemotePlayback&level=not)

The `RemotePlayback` interface of the [Remote Playback API](/en-US/docs/Web/API/Remote_Playback_API) allows the page to detect availability of remote playback devices, then connect to and control playing on these devices.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[RemotePlayback.state](/en-US/docs/Web/API/RemotePlayback/state)Read only

Represents the `RemotePlayback` connection's state. One of:

["connecting"](#connecting)

The user agent is attempting to initiate remote playback with the selected device.

["connected"](#connected)

The transition from local to remote playback has happened, all commands will now take place on the remote device.

["disconnected"](#disconnected)

The remote playback has not been initiated, has failed to initiate, or has been stopped.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[RemotePlayback.watchAvailability()](/en-US/docs/Web/API/RemotePlayback/watchAvailability)

Watches the list of available remote playback devices and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a `callbackId` of an available remote playback device.

[RemotePlayback.cancelWatchAvailability()](/en-US/docs/Web/API/RemotePlayback/cancelWatchAvailability)

Cancels the request to monitor the availability of remote playback devices.

[RemotePlayback.prompt()](/en-US/docs/Web/API/RemotePlayback/prompt)

Prompts the user to select and give permission to connect to a remote playback device.

## [Events](#events)

Also inherits events from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[connecting](/en-US/docs/Web/API/RemotePlayback/connecting_event)

Fired when the user agent initiates remote playback.

[connect](/en-US/docs/Web/API/RemotePlayback/connect_event)

Fired when the user agent successfully connects to the remote device.

[disconnect](/en-US/docs/Web/API/RemotePlayback/disconnect_event)

Fired when the user agent disconnects from the remote device.

## [Examples](#examples)

The following example demonstrates a player with custom controls that support remote playback. Initially the button used to select a device is hidden:

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

The [RemotePlayback.watchAvailability()](/en-US/docs/Web/API/RemotePlayback/watchAvailability) method is used to watch for available remote playback devices. If a device is available, use the callback to show the button.

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
  deviceBtn.classList.remove("hidden");
});
```

## [Specifications](#specifications)

Specification
[Remote Playback API# remoteplayback-interface](https://w3c.github.io/remote-playback/#remoteplayback-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/RemotePlayback/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/remoteplayback/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRemotePlayback&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fremoteplayback%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FRemotePlayback%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fremoteplayback%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
