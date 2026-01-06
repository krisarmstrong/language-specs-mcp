# MediaTrackConstraints

The `MediaTrackConstraints` dictionary is used to describe a set of media capabilities and the value or values each can take on.

A constraints dictionary is passed into the [applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints) method of the [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) interface to allow a script to establish a set of exact (required) values or ranges and/or preferred values or ranges of values for the track.

The most recently-requested set of custom constraints can be retrieved by calling [getConstraints()](/en-US/docs/Web/API/MediaStreamTrack/getConstraints).

Objects of this type may also be passed to:

- 

The [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia) method, to specify constraints on a media stream requested from hardware such as a camera or microphone.

- 

The [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia) method, to specify constraints on a media stream requested from a screen or window capture.

## In this article

- [Constraints](#constraints)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [See also](#see_also)

## [Constraints](#constraints)

The following types are used to specify a constraint for a property. They allow you to specify one or more `exact` values from which one must be the parameter's value, or a set of `ideal` values which should be used if possible. You can also specify a single value (or an array of values) which the user agent will do its best to match once all more stringent constraints have been applied.

To learn more about how constraints work, see [Capabilities, constraints, and settings](/en-US/docs/Web/API/Media_Capture_and_Streams_API/Constraints).

Note:`min` and `exact` values are not permitted in constraints used in [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia) calls — they produce a `TypeError` — but they are allowed in constraints used in [MediaStreamTrack.applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints) calls.

### [ConstrainBoolean](#constrainboolean)

The `ConstrainBoolean` constraint type is used to specify a constraint for a property whose value is a Boolean value. Its value may either be set to a Boolean (`true` or `false`) or an object containing the following properties:

[exact](#exact)

A Boolean which must be the value of the property. If the property can't be set to this value, matching will fail.

[ideal](#ideal)

A Boolean specifying an ideal value for the property. If possible, this value will be used, but if it's not possible, the user agent will use the closest possible match.

### [ConstrainBooleanOrDOMString](#constrainbooleanordomstring)

The `ConstrainBooleanOrDOMString` constraint type is used to specify a constraint for a property whose value is a Boolean or string value. It can take values as specified in the [ConstrainBoolean](#constrainboolean) and [ConstrainDOMString](#constraindomstring) sections.

### [ConstrainDouble](#constraindouble)

The `ConstrainDouble` constraint type is used to specify a constraint for a property whose value is a double-precision floating-point number. Its value may either be set to a number or an object containing the following properties:

[max](#max)

A decimal number specifying the largest permissible value of the property it describes. If the value cannot remain equal to or less than this value, matching will fail.

[min](#min)

A decimal number specifying the smallest permissible value of the property it describes. If the value cannot remain equal to or greater than this value, matching will fail.

[exact](#exact_2)

A decimal number specifying a specific, required, value the property must have to be considered acceptable.

[ideal](#ideal_2)

A decimal number specifying an ideal value for the property. If possible, this value will be used, but if it's not possible, the user agent will use the closest possible match.

### [ConstrainDOMString](#constraindomstring)

The `ConstrainDOMString` constraint type is used to specify a constraint for a property whose value is a string. Its value may either be set to a string, an array of strings, or an object containing the following properties:

[exact](#exact_3)

A string or an array of strings, one of which must be the value of the property. If the property can't be set to one of the listed values, matching will fail.

[ideal](#ideal_3)

A string or an array of strings, specifying ideal values for the property. If possible, one of the listed values will be used, but if it's not possible, the user agent will use the closest possible match.

### [ConstrainULong](#constrainulong)

The `ConstrainULong` constraint type is used to specify a constraint for a property whose value is an integer. Its value may either be set to a number or an object containing the following properties:

[max](#max_2)

An integer specifying the largest permissible value of the property it describes. If the value cannot remain equal to or less than this value, matching will fail.

[min](#min_2)

An integer specifying the smallest permissible value of the property it describes. If the value cannot remain equal to or greater than this value, matching will fail.

[exact](#exact_4)

An integer specifying a specific, required, value the property must have to be considered acceptable.

[ideal](#ideal_4)

An integer specifying an ideal value for the property. If possible, this value will be used, but if it's not possible, the user agent will use the closest possible match.

## [Instance properties](#instance_properties)

Some combination—but not necessarily all—of the following properties will exist on the object. This may be because a given browser doesn't support the property, or because it doesn't apply For example, because [RTP](/en-US/docs/Glossary/RTP) doesn't provide some of these values during negotiation of a WebRTC connection, a track associated with a [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection) will not include certain values, such as [facingMode](/en-US/docs/Web/API/MediaTrackConstraints/facingMode) or [groupId](/en-US/docs/Web/API/MediaTrackConstraints/groupId).

### [Instance properties of all media tracks](#instance_properties_of_all_media_tracks)

[deviceId](/en-US/docs/Web/API/MediaTrackConstraints/deviceId)

A [ConstrainDOMString](#constraindomstring) object specifying a device ID or an array of device IDs which are acceptable and/or required.

[groupId](/en-US/docs/Web/API/MediaTrackConstraints/groupId)

A [ConstrainDOMString](#constraindomstring) object specifying a group ID or an array of group IDs which are acceptable and/or required.

### [Instance properties of audio tracks](#instance_properties_of_audio_tracks)

[autoGainControl](/en-US/docs/Web/API/MediaTrackConstraints/autoGainControl)

A [ConstrainBoolean](#constrainboolean) object which specifies whether automatic gain control is preferred and/or required.

[channelCount](/en-US/docs/Web/API/MediaTrackConstraints/channelCount)

A [ConstrainULong](#constrainulong) specifying the channel count or range of channel counts which are acceptable and/or required.

[echoCancellation](/en-US/docs/Web/API/MediaTrackConstraints/echoCancellation)

A [ConstrainBooleanOrDOMString](#constrainbooleanordomstring) object specifying whether or not echo cancellation is preferred and/or required, and if supported, what type.

[latency](/en-US/docs/Web/API/MediaTrackConstraints/latency)

A [ConstrainDouble](#constraindouble) specifying the latency or range of latencies which are acceptable and/or required.

[noiseSuppression](/en-US/docs/Web/API/MediaTrackConstraints/noiseSuppression)

A [ConstrainBoolean](#constrainboolean) which specifies whether noise suppression is preferred and/or required.

[sampleRate](/en-US/docs/Web/API/MediaTrackConstraints/sampleRate)

A [ConstrainULong](#constrainulong) specifying the sample rate or range of sample rates which are acceptable and/or required.

[sampleSize](/en-US/docs/Web/API/MediaTrackConstraints/sampleSize)

A [ConstrainULong](#constrainulong) specifying the sample size or range of sample sizes which are acceptable and/or required.

[volume](/en-US/docs/Web/API/MediaTrackConstraints/volume)DeprecatedNon-standard

A [ConstrainDouble](#constraindouble) specifying the volume or range of volumes which are acceptable and/or required.

### [Instance properties of image tracks](#instance_properties_of_image_tracks)

[whiteBalanceMode](#whitebalancemode)

A [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) specifying one of `"none"`, `"manual"`, `"single-shot"`, or `"continuous"`.

[exposureMode](#exposuremode)

A [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) specifying one of `"none"`, `"manual"`, `"single-shot"`, or `"continuous"`.

[focusMode](#focusmode)

A [String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) specifying one of `"none"`, `"manual"`, `"single-shot"`, or `"continuous"`.

[pointsOfInterest](#pointsofinterest)

The pixel coordinates on the sensor of one or more points of interest. This is either an object in the form { x:value, y:value } or an array of such objects, where value is a double-precision integer.

[exposureCompensation](#exposurecompensation)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying f-stop adjustment by up to ±3.

[colorTemperature](#colortemperature)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying a desired color temperature in degrees kelvin.

[iso](#iso)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying a desired iso setting.

[brightness](#brightness)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying a desired brightness setting.

[contrast](#contrast)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying the degree of difference between light and dark.

[saturation](#saturation)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying the degree of color intensity.

[sharpness](#sharpness)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying the intensity of edges.

[focusDistance](#focusdistance)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying distance to a focused object.

[zoom](#zoom)

A [ConstrainDouble](#constraindouble) (a double-precision integer) specifying the desired focal length.

[torch](#torch)

A boolean value defining whether the fill light is continuously connected, meaning it stays on as long as the track is active.

### [Instance properties of video tracks](#instance_properties_of_video_tracks)

[aspectRatio](/en-US/docs/Web/API/MediaTrackConstraints/aspectRatio)

A [ConstrainDouble](#constraindouble) specifying the video [aspect ratio](/en-US/docs/Glossary/Aspect_ratio) or range of aspect ratios which are acceptable and/or required.

[facingMode](/en-US/docs/Web/API/MediaTrackConstraints/facingMode)

A [ConstrainDOMString](#constraindomstring) object specifying a facing or an array of facings which are acceptable and/or required.

[frameRate](/en-US/docs/Web/API/MediaTrackConstraints/frameRate)

A [ConstrainDouble](#constraindouble) specifying the frame rate or range of frame rates which are acceptable and/or required.

[height](/en-US/docs/Web/API/MediaTrackConstraints/height)

A [ConstrainULong](#constrainulong) specifying the video height or range of heights which are acceptable and/or required.

[width](/en-US/docs/Web/API/MediaTrackConstraints/width)

A [ConstrainULong](#constrainulong) specifying the video width or range of widths which are acceptable and/or required.

[resizeMode](#resizemode)

A [ConstrainDOMString](#constraindomstring) object specifying a mode or an array of modes the UA can use to derive the resolution and frame rate of a video track. Allowed values are:

[crop-and-scale](#crop-and-scale)

The user agent can use cropping and downscaling of resolution or frame rate on the raw output from the hardware/OS, in order to satisfy other constraints. This constraint allows developers to get a downscaled video even if the particular format indicated by their constraints is not natively supported by the hardware.

[none](#none)

The user agent uses the resolution provided by the underlying hardware, such as a camera or its driver, or the OS.

If `resizeMode` is unspecified the browser will choose a resolution based on a [fitness distance](https://w3c.github.io/mediacapture-main/#dfn-fitness-distance) that considers the specified constraints and both of the allowed values.

### [Instance properties of shared screen tracks](#instance_properties_of_shared_screen_tracks)

These constraints apply to the `video` property of the object passed into [getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia) to obtain a stream for screen sharing.

[displaySurface](/en-US/docs/Web/API/MediaTrackConstraints/displaySurface)

A [ConstrainDOMString](#constraindomstring) which specifies the types of display surface that may be selected by the user. This may be a single one of the following strings, or a list of them to allow multiple source surfaces:

[browser](#browser)

The stream contains the contents of a single browser tab selected by the user.

[monitor](#monitor)

The stream's video track contains the entire contents of one or more of the user's screens.

[window](#window)

The stream contains a single window selected by the user for sharing.

[logicalSurface](/en-US/docs/Web/API/MediaTrackConstraints/logicalSurface)

A [ConstrainBoolean](#constrainboolean) value which may contain a single Boolean value or a set of them, indicating whether or not to allow the user to choose source surfaces which do not directly correspond to display areas. These may include backing buffers for windows to allow capture of window contents that are hidden by other windows in front of them, or buffers containing larger documents that need to be scrolled through to see the entire contents in their windows.

[suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackConstraints/suppressLocalAudioPlayback)Experimental

A [ConstrainBoolean](#constrainboolean) value describing the requested or mandatory constraints placed upon the value of the [suppressLocalAudioPlayback](/en-US/docs/Web/API/MediaTrackSettings/suppressLocalAudioPlayback) constrainable property. This property controls whether the audio playing in a tab will continue to be played out of a user's local speakers when the tab is captured.

[restrictOwnAudio](/en-US/docs/Web/API/MediaTrackConstraints/restrictOwnAudio)Experimental

A [ConstrainBoolean](#constrainboolean) value that specifies the requested or mandatory constraints placed on the value of the [restrictOwnAudio](/en-US/docs/Web/API/MediaTrackSettings/restrictOwnAudio) constrainable property. This property controls whether the system audio originating from the capturing tab is filtered out of the screen capture.

## [Specifications](#specifications)

Specification
[Media Capture and Streams# dom-mediatrackconstraints](https://w3c.github.io/mediacapture-main/#dom-mediatrackconstraints)
[Screen Capture# extensions-to-mediatrackconstraintset](https://w3c.github.io/mediacapture-screen-share/#extensions-to-mediatrackconstraintset)

## [See also](#see_also)

- [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API)
- [Capabilities, constraints, and settings](/en-US/docs/Web/API/Media_Capture_and_Streams_API/Constraints)
- [Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API)
- [Using the Screen Capture API](/en-US/docs/Web/API/Screen_Capture_API/Using_Screen_Capture)
- [MediaStreamTrack.getConstraints()](/en-US/docs/Web/API/MediaStreamTrack/getConstraints)
- [MediaStreamTrack.applyConstraints()](/en-US/docs/Web/API/MediaStreamTrack/applyConstraints)
- [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [MediaDevices.getDisplayMedia()](/en-US/docs/Web/API/MediaDevices/getDisplayMedia)
- [MediaDevices.getSupportedConstraints()](/en-US/docs/Web/API/MediaDevices/getSupportedConstraints)
- [MediaTrackSupportedConstraints](/en-US/docs/Web/API/MediaTrackSupportedConstraints)
- [MediaStreamTrack.getSettings()](/en-US/docs/Web/API/MediaStreamTrack/getSettings)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 15, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaTrackConstraints/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediatrackconstraints/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackConstraints&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediatrackconstraints%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaTrackConstraints%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediatrackconstraints%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa439453bab9f5508b5268a4062a42fc760a2f20b%0A*+Document+last+modified%3A+2025-10-15T10%3A00%3A35.000Z%0A%0A%3C%2Fdetails%3E)
