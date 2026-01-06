# HTMLMediaElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement&level=high)

The `HTMLMediaElement` interface adds to [HTMLElement](/en-US/docs/Web/API/HTMLElement) the properties and methods needed to support basic media-related capabilities that are common to audio and video.

The [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) and [HTMLAudioElement](/en-US/docs/Web/API/HTMLAudioElement) elements both inherit this interface.

## In this article

- [Instance properties](#instance_properties)
- [Obsolete properties](#obsolete_properties)
- [Instance methods](#instance_methods)
- [Obsolete methods](#obsolete_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its ancestors [HTMLElement](/en-US/docs/Web/API/HTMLElement), [Element](/en-US/docs/Web/API/Element), [Node](/en-US/docs/Web/API/Node), and [EventTarget](/en-US/docs/Web/API/EventTarget).

[HTMLMediaElement.audioTracks](/en-US/docs/Web/API/HTMLMediaElement/audioTracks)Read only

An [AudioTrackList](/en-US/docs/Web/API/AudioTrackList) that lists the [AudioTrack](/en-US/docs/Web/API/AudioTrack) objects contained in the element.

[HTMLMediaElement.autoplay](/en-US/docs/Web/API/HTMLMediaElement/autoplay)

A boolean value that reflects the [autoplay](/en-US/docs/Web/HTML/Reference/Elements/video#autoplay) HTML attribute, indicating whether playback should automatically begin as soon as enough media is available to do so without interruption.

Note: Automatically playing audio when the user doesn't expect or desire it is a poor user experience and should be avoided in most cases, though there are exceptions. See the [Autoplay guide for media and Web Audio APIs](/en-US/docs/Web/Media/Guides/Autoplay) for more information. Keep in mind that browsers may ignore autoplay requests, so you should ensure that your code isn't dependent on autoplay working.

[HTMLMediaElement.buffered](/en-US/docs/Web/API/HTMLMediaElement/buffered)Read only

Returns a [TimeRanges](/en-US/docs/Web/API/TimeRanges) object that indicates the ranges of the media source that the browser has buffered (if any) at the moment the `buffered` property is accessed.

[HTMLMediaElement.controls](/en-US/docs/Web/API/HTMLMediaElement/controls)

A boolean that reflects the [controls](/en-US/docs/Web/HTML/Reference/Elements/video#controls) HTML attribute, indicating whether user interface items for controlling the resource should be displayed.

[HTMLMediaElement.controlsList](/en-US/docs/Web/API/HTMLMediaElement/controlsList)

Returns a [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that helps the user agent select what controls to show on the media element whenever the user agent shows its own set of controls. The `DOMTokenList` takes one or more of three possible values: `nodownload`, `nofullscreen`, and `noremoteplayback`.

[HTMLMediaElement.crossOrigin](/en-US/docs/Web/API/HTMLMediaElement/crossOrigin)

A string indicating the [CORS setting](/en-US/docs/Web/HTML/Reference/Attributes/crossorigin) for this media element.

[HTMLMediaElement.currentSrc](/en-US/docs/Web/API/HTMLMediaElement/currentSrc)Read only

Returns a string with the absolute URL of the chosen media resource.

[HTMLMediaElement.currentTime](/en-US/docs/Web/API/HTMLMediaElement/currentTime)

A double-precision floating-point value indicating the current playback time in seconds; if the media has not started to play and has not been seeked, this value is the media's initial playback time. Setting this value seeks the media to the new time. The time is specified relative to the media's timeline.

[HTMLMediaElement.defaultMuted](/en-US/docs/Web/API/HTMLMediaElement/defaultMuted)

A boolean that reflects the [muted](/en-US/docs/Web/HTML/Reference/Elements/video#muted) HTML attribute, which indicates whether the media element's audio output should be muted by default.

[HTMLMediaElement.defaultPlaybackRate](/en-US/docs/Web/API/HTMLMediaElement/defaultPlaybackRate)

A `double` indicating the default playback rate for the media.

[HTMLMediaElement.disableRemotePlayback](/en-US/docs/Web/API/HTMLMediaElement/disableRemotePlayback)

A boolean that sets or returns the remote playback state, indicating whether the media element is allowed to have a remote playback UI.

[HTMLMediaElement.duration](/en-US/docs/Web/API/HTMLMediaElement/duration)Read only

A read-only double-precision floating-point value indicating the total duration of the media in seconds. If no media data is available, the returned value is `NaN`. If the media is of indefinite length (such as streamed live media, a WebRTC call's media, or similar), the value is `Infinity`.

[HTMLMediaElement.ended](/en-US/docs/Web/API/HTMLMediaElement/ended)Read only

Returns a boolean that indicates whether the media element has finished playing.

[HTMLMediaElement.error](/en-US/docs/Web/API/HTMLMediaElement/error)Read only

Returns a [MediaError](/en-US/docs/Web/API/MediaError) object for the most recent error, or `null` if there has not been an error.

[HTMLMediaElement.loop](/en-US/docs/Web/API/HTMLMediaElement/loop)

A boolean that reflects the [loop](/en-US/docs/Web/HTML/Reference/Elements/video#loop) HTML attribute, which indicates whether the media element should start over when it reaches the end.

[HTMLMediaElement.mediaKeys](/en-US/docs/Web/API/HTMLMediaElement/mediaKeys)Read onlySecure context

Returns a [MediaKeys](/en-US/docs/Web/API/MediaKeys) object, that is a set of keys that the element can use for decryption of media data during playback. If no key is available, it can be `null`.

[HTMLMediaElement.muted](/en-US/docs/Web/API/HTMLMediaElement/muted)

A boolean that determines whether audio is muted. `true` if the audio is muted and `false` otherwise.

[HTMLMediaElement.networkState](/en-US/docs/Web/API/HTMLMediaElement/networkState)Read only

Returns a `unsigned short` (enumeration) indicating the current state of fetching the media over the network.

[HTMLMediaElement.paused](/en-US/docs/Web/API/HTMLMediaElement/paused)Read only

Returns a boolean that indicates whether the media element is paused.

[HTMLMediaElement.playbackRate](/en-US/docs/Web/API/HTMLMediaElement/playbackRate)

A `double` that indicates the rate at which the media is being played back.

[HTMLMediaElement.played](/en-US/docs/Web/API/HTMLMediaElement/played)Read only

Returns a [TimeRanges](/en-US/docs/Web/API/TimeRanges) object that contains the ranges of the media source that the browser has played, if any.

[HTMLMediaElement.preload](/en-US/docs/Web/API/HTMLMediaElement/preload)

A string that reflects the [preload](/en-US/docs/Web/HTML/Reference/Elements/video#preload) HTML attribute, indicating what data should be preloaded, if any. Possible values are: `none`, `metadata`, `auto`.

[HTMLMediaElement.preservesPitch](/en-US/docs/Web/API/HTMLMediaElement/preservesPitch)

A boolean value that determines if the pitch of the sound will be preserved. If set to `false`, the pitch will adjust to the speed of the audio.

[HTMLMediaElement.readyState](/en-US/docs/Web/API/HTMLMediaElement/readyState)Read only

Returns a `unsigned short` (enumeration) indicating the readiness state of the media.

[HTMLMediaElement.remote](/en-US/docs/Web/API/HTMLMediaElement/remote)Read only

Return a [RemotePlayback](/en-US/docs/Web/API/RemotePlayback) object instance associated with the media element.

[HTMLMediaElement.seekable](/en-US/docs/Web/API/HTMLMediaElement/seekable)Read only

Returns a [TimeRanges](/en-US/docs/Web/API/TimeRanges) object that contains the time ranges that the user is able to seek to, if any.

[HTMLMediaElement.seeking](/en-US/docs/Web/API/HTMLMediaElement/seeking)Read only

Returns a boolean that indicates whether the media is in the process of seeking to a new position.

[HTMLMediaElement.sinkId](/en-US/docs/Web/API/HTMLMediaElement/sinkId)Read onlySecure context

Returns a string that is the unique ID of the audio device delivering output, or an empty string if the user agent default audio device is being used.

[HTMLMediaElement.src](/en-US/docs/Web/API/HTMLMediaElement/src)

A string that reflects the [src](/en-US/docs/Web/HTML/Reference/Elements/video#src) HTML attribute, which contains the URL of a media resource to use.

[HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject)

An object which serves as the source of the media associated with the `HTMLMediaElement`, or `null` if not assigned.

[HTMLMediaElement.textTracks](/en-US/docs/Web/API/HTMLMediaElement/textTracks)Read only

Returns a [TextTrackList](/en-US/docs/Web/API/TextTrackList) object containing the list of [TextTrack](/en-US/docs/Web/API/TextTrack) objects contained in the element.

[HTMLMediaElement.videoTracks](/en-US/docs/Web/API/HTMLMediaElement/videoTracks)Read only

Returns a [VideoTrackList](/en-US/docs/Web/API/VideoTrackList) object containing the list of [VideoTrack](/en-US/docs/Web/API/VideoTrack) objects contained in the element.

[HTMLMediaElement.volume](/en-US/docs/Web/API/HTMLMediaElement/volume)

A `double` indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).

## [Obsolete properties](#obsolete_properties)

These properties are obsolete and should not be used, even if a browser still supports them.

[HTMLMediaElement.controller](/en-US/docs/Web/API/HTMLMediaElement/controller)DeprecatedNon-standard

A `MediaController` object that represents the media controller assigned to the element, or `null` if none is assigned.

[HTMLMediaElement.mediaGroup](/en-US/docs/Web/API/HTMLMediaElement/mediaGroup)DeprecatedNon-standard

A string that reflects the `mediagroup` HTML attribute, which indicates the name of the group of elements it belongs to. A group of media elements shares a common `MediaController`.

`HTMLMediaElement.mozAudioCaptured`Read onlyNon-standardDeprecated

Returns a boolean. Related to audio stream capture.

`HTMLMediaElement.mozFragmentEnd`Non-standardDeprecated

A `double` that provides access to the fragment end time if the media element has a fragment URI for `currentSrc`, otherwise it is equal to the media duration.

## [Instance methods](#instance_methods)

This interface also inherits methods from its ancestors [HTMLElement](/en-US/docs/Web/API/HTMLElement), [Element](/en-US/docs/Web/API/Element), [Node](/en-US/docs/Web/API/Node), and [EventTarget](/en-US/docs/Web/API/EventTarget).

[HTMLMediaElement.addTextTrack()](/en-US/docs/Web/API/HTMLMediaElement/addTextTrack)

Adds a new [TextTrack](/en-US/docs/Web/API/TextTrack) object (such as a track for subtitles) to a media element. This is a programmatic interface only and does not affect the DOM.

[HTMLMediaElement.captureStream()](/en-US/docs/Web/API/HTMLMediaElement/captureStream)

Returns [MediaStream](/en-US/docs/Web/API/MediaStream), captures a stream of the media content.

[HTMLMediaElement.canPlayType()](/en-US/docs/Web/API/HTMLMediaElement/canPlayType)

Given a string specifying a MIME media type (potentially with the [codecs parameter](/en-US/docs/Web/Media/Guides/Formats/codecs_parameter) included), `canPlayType()` returns the string `probably` if the media should be playable, `maybe` if there's not enough information to determine whether the media will play or not, or an empty string if the media cannot be played.

[HTMLMediaElement.fastSeek()](/en-US/docs/Web/API/HTMLMediaElement/fastSeek)

Quickly seeks to the given time with low precision.

[HTMLMediaElement.load()](/en-US/docs/Web/API/HTMLMediaElement/load)

Resets the media to the beginning and selects the best available source from the sources provided using the [src](/en-US/docs/Web/HTML/Reference/Elements/video#src) attribute or the [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) element.

[HTMLMediaElement.pause()](/en-US/docs/Web/API/HTMLMediaElement/pause)

Pauses the media playback.

[HTMLMediaElement.play()](/en-US/docs/Web/API/HTMLMediaElement/play)

Begins playback of the media.

[HTMLMediaElement.seekToNextFrame()](/en-US/docs/Web/API/HTMLMediaElement/seekToNextFrame)DeprecatedNon-standard

Seeks to the next frame in the media. This non-standard, experimental method makes it possible to manually drive reading and rendering of media at a custom speed, or to move through the media frame-by-frame to perform filtering or other operations.

[HTMLMediaElement.setMediaKeys()](/en-US/docs/Web/API/HTMLMediaElement/setMediaKeys)Secure context

Returns [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). Sets the [MediaKeys](/en-US/docs/Web/API/MediaKeys) keys to use when decrypting media during playback.

[HTMLMediaElement.setSinkId()](/en-US/docs/Web/API/HTMLMediaElement/setSinkId)Secure context

Sets the ID of the audio device to use for output and returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). This only works when the application is authorized to use the specified device.

## [Obsolete methods](#obsolete_methods)

These methods are obsolete and should not be used, even if a browser still supports them.

[HTMLMediaElement.mozCaptureStream()](/en-US/docs/Web/API/HTMLMediaElement/captureStream)Non-standard

The Firefox-prefixed equivalent of [HTMLMediaElement.captureStream()](/en-US/docs/Web/API/HTMLMediaElement/captureStream). See its [browser compatibility](/en-US/docs/Web/API/HTMLMediaElement/captureStream#browser_compatibility) for details.

`HTMLMediaElement.mozCaptureStreamUntilEnded()`Non-standardDeprecated

[enter description]

`HTMLMediaElement.mozGetMetadata()`Non-standardDeprecated

Returns [Object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object), which contains properties that represent metadata from the playing media resource as `{key: value}` pairs. A separate copy of the data is returned each time the method is called. This method must be called after the [loadedmetadata](/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event) event fires.

## [Events](#events)

Inherits events from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[abort](/en-US/docs/Web/API/HTMLMediaElement/abort_event)

Fired when the resource was not fully loaded, but not as the result of an error.

[canplay](/en-US/docs/Web/API/HTMLMediaElement/canplay_event)

Fired when the user agent can play the media, but estimates that not enough data has been loaded to play the media up to its end without having to stop for further buffering of content.

[canplaythrough](/en-US/docs/Web/API/HTMLMediaElement/canplaythrough_event)

Fired when the user agent can play the media, and estimates that enough data has been loaded to play the media up to its end without having to stop for further buffering of content.

[durationchange](/en-US/docs/Web/API/HTMLMediaElement/durationchange_event)

Fired when the duration property has been updated.

[emptied](/en-US/docs/Web/API/HTMLMediaElement/emptied_event)

Fired when the media has become empty; for example, when the media has already been loaded (or partially loaded), and the [HTMLMediaElement.load()](/en-US/docs/Web/API/HTMLMediaElement/load) method is called to reload it.

[encrypted](/en-US/docs/Web/API/HTMLMediaElement/encrypted_event)

Fired when initialization data is found in the media that indicates the media is encrypted.

[ended](/en-US/docs/Web/API/HTMLMediaElement/ended_event)

Fired when playback stops when end of the media (<audio> or <video>) is reached or because no further data is available.

[error](/en-US/docs/Web/API/HTMLMediaElement/error_event)

Fired when the resource could not be loaded due to an error.

[loadeddata](/en-US/docs/Web/API/HTMLMediaElement/loadeddata_event)

Fired when the first frame of the media has finished loading.

[loadedmetadata](/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event)

Fired when the metadata has been loaded.

[loadstart](/en-US/docs/Web/API/HTMLMediaElement/loadstart_event)

Fired when the browser has started to load a resource.

[pause](/en-US/docs/Web/API/HTMLMediaElement/pause_event)

Fired when a request to pause play is handled and the activity has entered its paused state, most commonly occurring when the media's [HTMLMediaElement.pause()](/en-US/docs/Web/API/HTMLMediaElement/pause) method is called.

[play](/en-US/docs/Web/API/HTMLMediaElement/play_event)

Fired when the `paused` property is changed from `true` to `false`, as a result of the [HTMLMediaElement.play()](/en-US/docs/Web/API/HTMLMediaElement/play) method, or the `autoplay` attribute.

[playing](/en-US/docs/Web/API/HTMLMediaElement/playing_event)

Fired when playback is ready to start after having been paused or delayed due to lack of data.

[progress](/en-US/docs/Web/API/HTMLMediaElement/progress_event)

Fired periodically as the browser loads a resource.

[ratechange](/en-US/docs/Web/API/HTMLMediaElement/ratechange_event)

Fired when the playback rate has changed.

[seeked](/en-US/docs/Web/API/HTMLMediaElement/seeked_event)

Fired when a seek operation completes.

[seeking](/en-US/docs/Web/API/HTMLMediaElement/seeking_event)

Fired when a seek operation begins.

[stalled](/en-US/docs/Web/API/HTMLMediaElement/stalled_event)

Fired when the user agent is trying to fetch media data, but data is unexpectedly not forthcoming.

[suspend](/en-US/docs/Web/API/HTMLMediaElement/suspend_event)

Fired when the media data loading has been suspended.

[timeupdate](/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event)

Fired when the time indicated by the [currentTime](/en-US/docs/Web/API/HTMLMediaElement/currentTime) property has been updated.

[volumechange](/en-US/docs/Web/API/HTMLMediaElement/volumechange_event)

Fired when the volume has changed.

[waiting](/en-US/docs/Web/API/HTMLMediaElement/waiting_event)

Fired when playback has stopped because of a temporary lack of data.

[waitingforkey](/en-US/docs/Web/API/HTMLMediaElement/waitingforkey_event)

Fired when playback is first blocked while waiting for a key.

## [Specifications](#specifications)

Specification
[HTML# htmlmediaelement](https://html.spec.whatwg.org/multipage/media.html#htmlmediaelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

### [References](#references)

- [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) and [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) HTML elements
- [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement) and [HTMLAudioElement](/en-US/docs/Web/API/HTMLAudioElement) interfaces, derived from `HTMLMediaElement`

### [Guides](#guides)

- [Web media technologies](/en-US/docs/Web/Media)
- Learning area: [HTML video and audio](/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
- [Media type and format guide](/en-US/docs/Web/Media/Guides/Formats)
- [Handling media support issues in web content](/en-US/docs/Web/Media/Guides/Formats/Support_issues)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLMediaElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlmediaelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlmediaelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLMediaElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlmediaelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2406bfdc031740afbd500a1fc953a76a4b7f8484%0A*+Document+last+modified%3A+2025-09-04T00%3A22%3A02.000Z%0A%0A%3C%2Fdetails%3E)
