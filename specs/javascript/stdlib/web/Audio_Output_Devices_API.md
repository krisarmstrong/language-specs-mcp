# Audio Output Devices API

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Audio Output Devices API allows web applications to prompt users about what output device should be used for audio playback.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Security requirements](#security_requirements)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

Operating systems commonly allow users to specify that audio should be played from speakers, a Bluetooth headset, or some other audio output device. This API allows applications to provide this same functionality from within a web page.

Even if allowed by a permission policy, access to a particular audio output device still requires explicit user permission, as the user may be in a location where playing audio through some output devices is not appropriate.

The API provides the [MediaDevices.selectAudioOutput()](/en-US/docs/Web/API/MediaDevices/selectAudioOutput) method that allows users to select their desired audio output from those that are allowed by the [speaker-selection](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/speaker-selection) directive of the [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) HTTP header for the document. The selected device then has user permission, allowing it to be enumerated with [MediaDevices.enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices) and set as the audio output device using [HTMLMediaElement.setSinkId()](/en-US/docs/Web/API/HTMLMediaElement/setSinkId).

Audio devices may arbitrarily connect and disconnect. Applications that wish to react to this kind of change can listen to the [devicechange](/en-US/docs/Web/API/MediaDevices/devicechange_event) event and use [enumerateDevices()](/en-US/docs/Web/API/MediaDevices/enumerateDevices) to determine if `sinkId` is present in the returned devices. This might trigger, for example, pausing or unpausing playback.

## [Interfaces](#interfaces)

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The Audio Output Devices API extends the following APIs, adding the listed features:

#### MediaDevices

[MediaDevices.selectAudioOutput()](/en-US/docs/Web/API/MediaDevices/selectAudioOutput)

This method prompts the user to select a specific audio output device, for example a speaker or headset. Selecting a device grants user permission to use that device and returns information about the device, including its ID.

#### HTMLMediaElement

[HTMLMediaElement.setSinkId()](/en-US/docs/Web/API/HTMLMediaElement/setSinkId)

This method sets the ID of the audio device to use for output, which will be used if permitted.

[HTMLMediaElement.sinkId](/en-US/docs/Web/API/HTMLMediaElement/sinkId)

This property returns the unique ID of the audio device being used for output, or an empty string if the default user agent device is being used.

## [Security requirements](#security_requirements)

Access to the API is subject to the following constraints:

- 

All methods and properties may only be called in a [secure context](/en-US/docs/Web/Security/Defenses/Secure_Contexts).

- 

[MediaDevices.selectAudioOutput()](/en-US/docs/Web/API/MediaDevices/selectAudioOutput) grants user permission for a selected device to be used as the audio output sink:

  - Access may be gated by the [speaker-selection](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/speaker-selection) HTTP [Permission Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy).
  - [Transient user activation](/en-US/docs/Web/Security/Defenses/User_activation) is required. The user has to interact with the page or a UI element for the method to be called.

- 

[HTMLMediaElement.setSinkId()](/en-US/docs/Web/API/HTMLMediaElement/setSinkId) sets a permitted ID as the audio output:

  - Access may be gated by the [speaker-selection](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy/speaker-selection) HTTP [Permission Policy](/en-US/docs/Web/HTTP/Guides/Permissions_Policy).
  - User permission is required to set a non-default device ID. 

    - This can come from selection in the prompt launched by `MediaDevices.selectAudioOutput()`
    - User permission to set the output device is also implicitly granted if the user has already granted permission to use a media input device in the same group with [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia).

## [Examples](#examples)

Here's an example of using `selectAudioOutput()`, within a function that is triggered by a button click, and then setting the selected device as the audio output.

The code first checks if `selectAudioOutput()` is supported, and if it is, uses it to select an output and return a [device ID](/en-US/docs/Web/API/MediaDeviceInfo/deviceId). We then play some audio using the default output, and then call `setSinkId()` in order to switch to the selected output device.

js

```
document.querySelector("#myButton").addEventListener("click", async () => {
  if (!navigator.mediaDevices.selectAudioOutput) {
    console.log("selectAudioOutput() not supported or not in secure context.");
    return;
  }

  // Display prompt to select device
  const audioDevice = await navigator.mediaDevices.selectAudioOutput();

  // Create an audio element and start playing audio on the default device
  const audio = document.createElement("audio");
  audio.src = "https://example.com/audio.mp3";
  audio.play();

  // Change the sink to the selected audio output device.
  audio.setSinkId(audioDevice.deviceId);
});
```

Note that if you log the output details, they might look something like this:

js

```
console.log(
  `${audioDevice.kind}: ${audioDevice.label} id = ${audioDevice.deviceId}`,
);
// audiooutput: Realtek Digital Output (Realtek(R) Audio) id = 0wE6fURSZ20H0N2NbxqgowQJLWbwo+5ablCVVJwRM3k=
```

## [Specifications](#specifications)

Specification[Audio Output Devices API](https://w3c.github.io/mediacapture-output/)

## [Browser compatibility](#browser_compatibility)

### [api.MediaDevices.selectAudioOutput](#api.MediaDevices.selectAudioOutput)

### [api.HTMLMediaElement.setSinkId](#api.HTMLMediaElement.setSinkId)

### [api.HTMLMediaElement.sinkId](#api.HTMLMediaElement.sinkId)

### [http.headers.Permissions-Policy.speaker-selection](#http.headers.Permissions-Policy.speaker-selection)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Audio_Output_Devices_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audio_output_devices_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudio_Output_Devices_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudio_output_devices_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudio_Output_Devices_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudio_output_devices_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
