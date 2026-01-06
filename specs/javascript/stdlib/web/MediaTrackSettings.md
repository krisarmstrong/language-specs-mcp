# MediaTrackSettings

The `MediaTrackSettings` dictionary is used to return the current values configured for each of a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack)'s settings. These values will adhere as closely as possible to any constraints previously described using a [MediaTrackConstraints](/en-US/docs/Web/API/MediaTrackConstraints) object and set using [applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints), and will adhere to the default constraints for any properties whose constraints haven't been changed, or whose customized constraints couldn't be matched.

To learn more about how constraints and settings work, see [Capabilities, constraints, and settings](/en-US/docs/Web/API/Media_Capture_and_Streams_API/Constraints).

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Some or all of the following will be included in the object, either because it's not supported by the browser or because it's not available due to context. For example, because [RTP](/en-US/docs/Glossary/RTP) doesn't provide some of these values during negotiation of a WebRTC connection, a track associated with a [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) will not include certain values, such as [facingMode](/en-US/docs/Web/API/MediaTrackSettings/facingMode) or [groupId](/en-US/docs/Web/API/MediaTrackSettings/groupId).

### [Instance properties of all media tracks](#instance_properties_of_all_media_tracks)

[deviceId](/en-US/docs/Web/API/MediaTrackSettings/deviceId)

A string indicating the current value of the [deviceId](/en-US/docs/Web/API/MediaTrackConstraints/deviceId) property. The device ID is an origin-unique string identifying the source of the track; this is usually a [GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). This value is specific to the source of the track's data and is not usable for setting constraints; it can, however, be used for initially selecting media when calling [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia).

[groupId](/en-US/docs/Web/API/MediaTrackSettings/groupId)

A string indicating the current value of the [groupId](/en-US/docs/Web/API/MediaTrackConstraints/groupId) property. The group ID is a browsing session-unique string identifying the source group of the track. Two devices (as identified by the [deviceId](/en-US/docs/Web/API/MediaTrackSettings/deviceId)) are considered part of the same group if they are from the same physical device. For instance, the audio input and output devices for the speaker and microphone built into a phone would share the same group ID, since they're part of the same physical device. The microphone on a headset would have a different ID, though. This value is specific to the source of the track's data and is not usable for setting constraints; it can, however, be used for initially selecting media when calling [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia).

### [Instance properties of audio tracks](#instance_properties_of_audio_tracks)

[autoGainControl](/en-US/docs/Web/API/MediaTrackSettings/autoGainControl)

A Boolean which indicates the current value of the [autoGainControl](/en-US/docs/Web/API/MediaTrackConstraints/autoGainControl) property, which is `true` if automatic gain control is enabled and is `false` otherwise.

[channelCount](/en-US/docs/Web/API/MediaTrackSettings/channelCount)

A long integer value indicating the current value of the [channelCount](/en-US/docs/Web/API/MediaTrackConstraints/channelCount) property, specifying the number of audio channels present on the track (therefore indicating how many audio samples exist in each audio frame). This is 1 for mono, 2 for stereo, and so forth.

[echoCancellation](/en-US/docs/Web/API/MediaTrackSettings/echoCancellation)

A Boolean indicating the current value of the [echoCancellation](/en-US/docs/Web/API/MediaTrackConstraints/echoCancellation) property, specifying `true` if echo cancellation is enabled, otherwise `false`.

[latency](/en-US/docs/Web/API/MediaTrackSettings/latency)

A double-precision floating point value indicating the current value of the [latency](/en-US/docs/Web/API/MediaTrackConstraints/latency) property, specifying the audio latency, in seconds. Latency is the amount of time which elapses between the start of processing the audio and the data being available to the next stop in the audio utilization process. This value is a target value; actual latency may vary to some extent for various reasons.

[noiseSuppression](/en-US/docs/Web/API/MediaTrackSettings/noiseSuppression)

A Boolean indicating the current value of the [noiseSuppression](/en-US/docs/Web/API/MediaTrackConstraints/noiseSuppression) property: `true` if noise suppression is enabled, and is `false` otherwise.

[restrictOwnAudio](/en-US/docs/Web/API/MediaTrackSettings/restrictOwnAudio)

A Boolean indicating the current value of the [restrictOwnAudio](/en-US/docs/Web/API/MediaTrackConstraints/restrictOwnAudio) property: `true` if the browser will attempt to filter out system audio originating from the capturing tab during screen capture, and `false` otherwise.

[sampleRate](/en-US/docs/Web/API/MediaTrackSettings/sampleRate)

A long integer value indicating the current value of the [sampleRate](/en-US/docs/Web/API/MediaTrackConstraints/sampleRate) property, specifying the sample rate in samples per second of the audio data. Standard CD-quality audio, for example, has a sample rate of 41,000 samples per second.

[sampleSize](/en-US/docs/Web/API/MediaTrackSettings/sampleSize)

A long integer value indicating the current value of the [sampleSize](/en-US/docs/Web/API/MediaTrackConstraints/sampleSize) property, specifying the linear size, in bits, of each audio sample. CD-quality audio, for example, is 16-bit, so this value would be 16 in that case.

[suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackSettings/suppressLocalAudioPlayback)

Controls whether the audio playing in a tab will continue to be played out of a user's local speakers when the tab is captured.

[volume](/en-US/docs/Web/API/MediaTrackSettings/volume)DeprecatedNon-standard

A double-precision floating point value indicating the current value of the [volume](/en-US/docs/Web/API/MediaTrackConstraints/volume) property, specifying the volume level of the track. This value will be between 0.0 (silent) to 1.0 (maximum supported volume).

### [Instance properties of video tracks](#instance_properties_of_video_tracks)

[aspectRatio](/en-US/docs/Web/API/MediaTrackSettings/aspectRatio)

A double-precision floating point value indicating the current value of the [aspectRatio](/en-US/docs/Web/API/MediaTrackConstraints/aspectRatio) property, specified precisely to 10 decimal places. This is the width of the image in pixels divided by its height in pixels. Common values include 1.3333333333 (for the classic television 4:3 "standard" [aspect ratio](/en-US/docs/Glossary/Aspect_ratio), also used on tablets such as Apple's iPad), 1.7777777778 (for the 16:9 high-definition widescreen aspect ratio), and 1.6 (for the 16:10 aspect ratio common among widescreen computers and tablets).

[facingMode](/en-US/docs/Web/API/MediaTrackSettings/facingMode)

A string indicating the current value of the [facingMode](/en-US/docs/Web/API/MediaTrackConstraints/facingMode) property, specifying the direction the camera is facing. The value will be one of:

["user"](#user)

A camera facing the user (commonly known as a "selfie cam"), used for self-portraiture and video calling.

["environment"](#environment)

A camera facing away from the user (when the user is looking at the screen). This is typically the highest quality camera on the device, used for general photography.

["left"](#left)

A camera facing toward the environment to the user's left.

["right"](#right)

A camera facing toward the environment to the user's right.

[frameRate](/en-US/docs/Web/API/MediaTrackSettings/frameRate)

A double-precision floating point value indicating the current value of the [frameRate](/en-US/docs/Web/API/MediaTrackConstraints/frameRate) property, specifying how many frames of video per second the track includes. If the value can't be determined for any reason, the value will match the vertical sync rate of the device the user agent is running on.

[height](/en-US/docs/Web/API/MediaTrackSettings/height)

A long integer value indicating the current value of the [height](/en-US/docs/Web/API/MediaTrackConstraints/height) property, specifying the height of the track's video data in pixels.

[width](/en-US/docs/Web/API/MediaTrackSettings/width)

A long integer value indicating the current value of the [width](/en-US/docs/Web/API/MediaTrackSettings/width) property, specifying the width of the track's video data in pixels.

`resizeMode`

A string indicating the current value of the `resizeMode` property, specifying the mode used by the user agent to derive the resolution of the track. The value will be one of:

["none"](#none)

The track has the resolution offered by the camera, its driver or the OS.

["crop-and-scale"](#crop-and-scale)

The track's resolution might be the result of the user agent using cropping or downscaling from a higher camera resolution.

### [Instance properties of shared screen tracks](#instance_properties_of_shared_screen_tracks)

Tracks containing video shared from a user's screen (regardless of whether the screen data comes from the entire screen or a portion of a screen, like a window or tab) are generally treated like video tracks, with the exception that they also support the following added settings:

[cursor](/en-US/docs/Web/API/MediaTrackSettings/cursor)

A string which indicates whether or not the mouse cursor is being included in the generated stream and under what conditions. Possible values are:

[always](#always)

The mouse is always visible in the video content of the {domxref("MediaStream"), unless the mouse has moved outside the area of the content.

[motion](#motion)

The mouse cursor is always included in the video if it's moving, and for a short time after it stops moving.

[never](#never)

The mouse cursor is never included in the shared video.

[displaySurface](/en-US/docs/Web/API/MediaTrackSettings/displaySurface)

A string which specifies the type of source the track contains; one of:

[browser](#browser)

The stream contains the contents of a single browser tab selected by the user.

[monitor](#monitor)

The stream's video track contains the entire contents of one or more of the user's screens.

[window](#window)

The stream contains a single window selected by the user for sharing.

[logicalSurface](/en-US/docs/Web/API/MediaTrackSettings/logicalSurface)

A Boolean value which, if `true`, indicates that the video contained in the stream's video track contains a background rendering context, rather than a user-visible one. This is `false` if the video being captured is coming from a foreground (user-visible) source.

[screenPixelRatio](/en-US/docs/Web/API/MediaTrackSettings/screenPixelRatio)

A number representing the ratio of the physical size of a pixel on the captured display surface (displayed at its physical resolution) to the logical size of a CSS pixel on the capturing screen (displayed at its logical resolution). It cannot be used as a constraint or capability.

## [Specifications](#specifications)

Specification
[Media Capture and Streams# media-track-settings](https://w3c.github.io/mediacapture-main/#media-track-settings)
[Screen Capture# extensions-to-mediatracksettings](https://w3c.github.io/mediacapture-screen-share/#extensions-to-mediatracksettings)

## [See also](#see_also)

- [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)
- [MediaStreamTrack.getConstraints()](/en-US/docs/Web/API/MediaStreamTrack/getConstraints)
- [MediaStreamTrack.applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints)
- [MediaStreamTrack.getSettings()](/en-US/docs/Web/API/MediaStreamTrack/getSettings)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaTrackSettings/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediatracksettings/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackSettings&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediatracksettings%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackSettings%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediatracksettings%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa439453bab9f5508b5268a4062a42fc760a2f20b%0A*+Document+last+modified%3A+2025-10-15T10%3A00%3A35.000Z%0A%0A%3C%2Fdetails%3E)
