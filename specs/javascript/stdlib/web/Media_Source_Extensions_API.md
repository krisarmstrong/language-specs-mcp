# Media Source API

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The Media Source API, formally known as Media Source Extensions (MSE), provides functionality enabling plugin-free web-based streaming media. Using MSE, media streams can be created via JavaScript, and played using [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) and [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) elements.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

Playing video and audio has been available in web applications without plugins for a few years now, but the basic features offered have really only been useful for playing single whole tracks. We can't, for example, combine/split arraybuffers. Streaming media has up until recently been the domain of Flash, with technologies like Flash Media Server serving video streams using the RTMP protocol.

### [The MSE standard](#the_mse_standard)

With Media Source Extensions (MSE), this is changing. MSE allows us to replace the usual single progressive `src` URI fed to media elements with a reference to a `MediaSource` object, which is a container for information like the ready state of the media for being played, and references to multiple `SourceBuffer` objects that represent the different chunks of media that make up the entire stream. MSE gives us finer-grained control over how much and how often content is fetched, and some control over memory usage details, such as when buffers are evicted. It lays the groundwork for adaptive bitrate streaming clients (such as those using DASH or HLS) to be built on its extensible API.

Creating assets that work with MSE in modern browsers is a laborious process, taking significant time, computing power, and energy. The usage of external utilities to massage the content into a suitable format is required. While browser support for the various media containers with MSE is spotty, usage of the H.264 video codec, AAC audio codec, and MP4 container format is a common baseline. MSE also provides an API for runtime detection of container and codec support.

If you do not require explicit control of video quality over time, the rate at which content is fetched, or the rate at which memory is evicted, then the [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) and [<source>](/en-US/docs/Web/HTML/Reference/Elements/source) tags may well be a simple and adequate solution.

### [DASH](#dash)

Dynamic Adaptive Streaming over HTTP (DASH) is a protocol for specifying how adaptive content should be fetched. It is effectively a layer built on top of MSE for building adaptive bitrate streaming clients. While there are other protocols available (such as HTTP Live Streaming (HLS)), DASH has the most platform support.

DASH moves lots of logic out of the network protocol and into the client side application logic, using the simpler HTTP protocol to fetch files. Indeed, one can support DASH with a simple static file server, which is also great for CDNs. This is in direct contrast with previous streaming solutions that required expensive licenses for proprietary non-standard client/server protocol implementations.

The two most common use cases for DASH involve watching content "on demand" or "live." On demand allows a developer to take their time transcoding the assets into multiple resolutions of various quality.

Live profile content can introduce latency due to its transcoding and broadcasting, so DASH is not suitable for real time communication like [WebRTC](/en-US/docs/Web/API/WebRTC_API) is. It can however support significantly more client connections than WebRTC.

There are numerous available free and open source tools for transcoding content and preparing it for use with DASH, DASH file servers, and DASH client libraries written in JavaScript. The [DASH Adaptive Streaming for HTML video](/en-US/docs/Web/API/Media_Source_Extensions_API/DASH_Adaptive_Streaming) article provides an example of how to use DASH with MSE.

### [Availability in workers](#availability_in_workers)

Starting with Chrome 108, MSE features are available in dedicated [web workers](/en-US/docs/Web/API/Web_Workers_API), which allows for improved performance when manipulating [MediaSource](/en-US/docs/Web/API/MediaSource)s and [SourceBuffer](/en-US/docs/Web/API/SourceBuffer)s. To play back the media, the [MediaSource.handle](/en-US/docs/Web/API/MediaSource/handle) property is used to get a reference to a [MediaSourceHandle](/en-US/docs/Web/API/MediaSourceHandle) object, a proxy for the `MediaSource` that can be transferred back to the main thread and attached to a media element via its [HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject) property.

See [MSE-in-Workers Demo by Matt Wolenetz](https://wolenetz.github.io/mse-in-workers-demo/mse-in-workers-demo.html) for a live example.

## [Interfaces](#interfaces)

[MediaSource](/en-US/docs/Web/API/MediaSource)

Represents a media source to be played via an [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) object.

[MediaSourceHandle](/en-US/docs/Web/API/MediaSourceHandle)

A proxy for a [MediaSource](/en-US/docs/Web/API/MediaSource) that can be transferred from a dedicated worker back to the main thread and attached to a media element via its [HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject) property.

[SourceBuffer](/en-US/docs/Web/API/SourceBuffer)

Represents a chunk of media to be passed into an [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) via a `MediaSource` object.

[SourceBufferList](/en-US/docs/Web/API/SourceBufferList)

A simple container list for multiple `SourceBuffer` objects.

[VideoPlaybackQuality](/en-US/docs/Web/API/VideoPlaybackQuality)

Contains information about the quality of video being played by a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element, such as number of dropped or corrupted frames. Returned by the [HTMLVideoElement.getVideoPlaybackQuality()](/en-US/docs/Web/API/HTMLVideoElement/getVideoPlaybackQuality) method.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

[HTMLMediaElement.buffered](/en-US/docs/Web/API/HTMLMediaElement/buffered)

Returns a [TimeRanges](/en-US/docs/Web/API/TimeRanges) object that indicates the ranges of the media source that the browser has buffered (if any) at the moment the `buffered` property is accessed.

[HTMLMediaElement.seekable](/en-US/docs/Web/API/HTMLMediaElement/seekable)

Returns a [TimeRanges](/en-US/docs/Web/API/TimeRanges) object that contains the time ranges that the user is able to seek to, if any.

[HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject)

A media provider object representing the media resource to play or that has played in the current `HTMLMediaElement`, or `null` if not assigned.

[HTMLVideoElement.getVideoPlaybackQuality()](/en-US/docs/Web/API/HTMLVideoElement/getVideoPlaybackQuality)

Returns a [VideoPlaybackQuality](/en-US/docs/Web/API/VideoPlaybackQuality) object for the currently played video.

[AudioTrack.sourceBuffer](/en-US/docs/Web/API/AudioTrack/sourceBuffer), [VideoTrack.sourceBuffer](/en-US/docs/Web/API/VideoTrack/sourceBuffer), [TextTrack.sourceBuffer](/en-US/docs/Web/API/TextTrack/sourceBuffer)

Returns the [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) that created the track in question.

## [Specifications](#specifications)

Specification[Media Source Extensions™](https://w3c.github.io/media-source/)[Media Playback Quality](https://w3c.github.io/media-playback-quality/)

## [See also](#see_also)

- [Transcoding assets for Media Source Extensions](/en-US/docs/Web/API/Media_Source_Extensions_API/Transcoding_assets_for_MSE)
- Using MSE to create a basic streaming service (TBD)
- Using MPEG DASH to create a streaming application (TBD)
- The [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) and [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) elements.
- [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement), [HTMLAudioElement](/en-US/docs/Web/API/HTMLAudioElement).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Media_Source_Extensions_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/media_source_extensions_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Source_Extensions_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmedia_source_extensions_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Source_Extensions_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmedia_source_extensions_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdb01d0c8b4cbf8a4467b1db65e17f6724d0ce710%0A*+Document+last+modified%3A+2025-07-12T01%3A26%3A27.000Z%0A%0A%3C%2Fdetails%3E)
