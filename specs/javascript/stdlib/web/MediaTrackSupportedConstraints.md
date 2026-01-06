# MediaTrackSupportedConstraints

The `MediaTrackSupportedConstraints` dictionary establishes the list of constrainable properties recognized by the [user agent](/en-US/docs/Glossary/User_agent) or browser in its implementation of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) object. An object conforming to `MediaTrackSupportedConstraints` is returned by [MediaDevices.getSupportedConstraints()](/en-US/docs/Web/API/MediaDevices/getSupportedConstraints).

Because of the way interface definitions in WebIDL work, if a constraint is requested but not supported, no error will occur. Instead, the specified constraints will be applied, with any unrecognized constraints stripped from the request. That can lead to confusing and hard to debug errors, so be sure to use `getSupportedConstraints()` to retrieve this information before attempting to establish constraints if you need to know the difference between silently ignoring a constraint and a constraint being accepted.

An actual constraint set is described using an object based on the [MediaTrackConstraints](/en-US/docs/Web/API/MediaTrackConstraints) dictionary.

To learn more about how constraints work, see [Capabilities, constraints, and settings](/en-US/docs/Web/API/Media_Capture_and_Streams_API/Constraints).

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Some combination—but not necessarily all—of the following properties will exist on the object.

[aspectRatio](/en-US/docs/Web/API/MediaTrackSupportedConstraints/aspectRatio)

A Boolean that is `true` if the [aspectRatio](/en-US/docs/Web/API/MediaTrackConstraints/aspectRatio) constraint is supported in the current environment.

[autoGainControl](/en-US/docs/Web/API/MediaTrackSupportedConstraints/autoGainControl)

A Boolean that is `true` if the [autoGainControl](/en-US/docs/Web/API/MediaTrackConstraints/autoGainControl) constraint is supported in the current environment.

[channelCount](/en-US/docs/Web/API/MediaTrackSupportedConstraints/channelCount)

A Boolean that is `true` if the [channelCount](/en-US/docs/Web/API/MediaTrackConstraints/channelCount) constraint is supported in the current environment.

[deviceId](/en-US/docs/Web/API/MediaTrackSupportedConstraints/deviceId)

A Boolean that is `true` if the [deviceId](/en-US/docs/Web/API/MediaTrackConstraints/deviceId) constraint is supported in the current environment.

[echoCancellation](/en-US/docs/Web/API/MediaTrackSupportedConstraints/echoCancellation)

A Boolean that is `true` if the [echoCancellation](/en-US/docs/Web/API/MediaTrackConstraints/echoCancellation) constraint is supported in the current environment.

[facingMode](/en-US/docs/Web/API/MediaTrackSupportedConstraints/facingMode)

A Boolean that is `true` if the [facingMode](/en-US/docs/Web/API/MediaTrackConstraints/facingMode) constraint is supported in the current environment.

[frameRate](/en-US/docs/Web/API/MediaTrackSupportedConstraints/frameRate)

A Boolean that is `true` if the [frameRate](/en-US/docs/Web/API/MediaTrackConstraints/frameRate) constraint is supported in the current environment.

[groupId](/en-US/docs/Web/API/MediaTrackSupportedConstraints/groupId)

A Boolean that is `true` if the [groupId](/en-US/docs/Web/API/MediaTrackConstraints/groupId) constraint is supported in the current environment.

[height](/en-US/docs/Web/API/MediaTrackSupportedConstraints/height)

A Boolean that is `true` if the [height](/en-US/docs/Web/API/MediaTrackConstraints/height) constraint is supported in the current environment.

[latency](/en-US/docs/Web/API/MediaTrackSupportedConstraints/latency)

A Boolean that is `true` if the [latency](/en-US/docs/Web/API/MediaTrackConstraints/latency) constraint is supported in the current environment.

[noiseSuppression](/en-US/docs/Web/API/MediaTrackSupportedConstraints/noiseSuppression)

A Boolean that is `true` if the [noiseSuppression](/en-US/docs/Web/API/MediaTrackConstraints/noiseSuppression) constraint is supported in the current environment.

[restrictOwnAudio](/en-US/docs/Web/API/MediaTrackSupportedConstraints/restrictOwnAudio)

A Boolean that is `true` if the [restrictOwnAudio](/en-US/docs/Web/API/MediaTrackConstraints/restrictOwnAudio) constraint is supported in the current environment.

`resizeMode`

A Boolean that is `true` if the `resizeMode` constraint is supported in the current environment.

[sampleRate](/en-US/docs/Web/API/MediaTrackSupportedConstraints/sampleRate)

A Boolean that is `true` if the [sampleRate](/en-US/docs/Web/API/MediaTrackConstraints/sampleRate) constraint is supported in the current environment.

[sampleSize](/en-US/docs/Web/API/MediaTrackSupportedConstraints/sampleSize)

A Boolean that is `true` if the [sampleSize](/en-US/docs/Web/API/MediaTrackConstraints/sampleSize) constraint is supported in the current environment.

[suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackSupportedConstraints/suppressLocalAudioPlayback)

A Boolean that is `true` if the [suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackConstraints/suppressLocalAudioPlayback) constraint is supported in the current environment.

[volume](/en-US/docs/Web/API/MediaTrackSupportedConstraints/volume)DeprecatedNon-standard

A Boolean that is `true` if the [volume](/en-US/docs/Web/API/MediaTrackConstraints/volume) constraint is supported in the current environment.

[width](/en-US/docs/Web/API/MediaTrackSupportedConstraints/width)

A Boolean that is `true` if the [width](/en-US/docs/Web/API/MediaTrackConstraints/width) constraint is supported in the current environment.

### [Instance properties specific to shared screen tracks](#instance_properties_specific_to_shared_screen_tracks)

For tracks containing video sources from the user's screen, the following additional properties may be included, in addition to those available for video tracks:

[displaySurface](/en-US/docs/Web/API/MediaTrackSupportedConstraints/displaySurface)

A Boolean that is `true` if the [displaySurface](/en-US/docs/Web/API/MediaTrackConstraints/displaySurface) constraint is supported in the current environment.

[logicalSurface](/en-US/docs/Web/API/MediaTrackSupportedConstraints/logicalSurface)

A Boolean that is `true` if the [logicalSurface](/en-US/docs/Web/API/MediaTrackConstraints/logicalSurface) constraint is supported in the current environment.

## [Specifications](#specifications)

Specification
[Media Capture and Streams# media-track-supported-constraints](https://w3c.github.io/mediacapture-main/#media-track-supported-constraints)

## [See also](#see_also)

- [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API)
- [Capabilities, constraints, and settings](/en-US/docs/Web/API/Media_Capture_and_Streams_API/Constraints)
- [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API)
- [Using the Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API/Using_Screen_Capture)
- [MediaTrackConstraints](/en-US/docs/Web/API/MediaTrackConstraints)
- [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [MediaStreamTrack.getConstraints()](/en-US/docs/Web/API/MediaStreamTrack/getConstraints)
- [MediaStreamTrack.applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints)
- [MediaStreamTrack.getSettings()](/en-US/docs/Web/API/MediaStreamTrack/getSettings)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaTrackSupportedConstraints/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediatracksupportedconstraints/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackSupportedConstraints&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediatracksupportedconstraints%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackSupportedConstraints%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediatracksupportedconstraints%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa439453bab9f5508b5268a4062a42fc760a2f20b%0A*+Document+last+modified%3A+2025-10-15T10%3A00%3A35.000Z%0A%0A%3C%2Fdetails%3E)
