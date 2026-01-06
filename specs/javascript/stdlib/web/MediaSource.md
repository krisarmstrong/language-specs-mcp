# MediaSource

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaSource&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `MediaSource` interface of the [Media Source Extensions API](/en-US/docs/Web/API/Media_Source_Extensions_API) represents a source of media data for an [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) object. A `MediaSource` object can be attached to a [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) to be played in the user agent.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static properties](#static_properties)
- [Instance methods](#instance_methods)
- [Static methods](#static_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaSource()](/en-US/docs/Web/API/MediaSource/MediaSource)

Constructs and returns a new `MediaSource` object with no associated source buffers.

## [Instance properties](#instance_properties)

[MediaSource.activeSourceBuffers](/en-US/docs/Web/API/MediaSource/activeSourceBuffers)Read only

Returns a [SourceBufferList](/en-US/docs/Web/API/SourceBufferList) object containing a subset of the [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects contained within [MediaSource.sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers) — the list of objects providing the selected video track, enabled audio tracks, and shown/hidden text tracks.

[MediaSource.duration](/en-US/docs/Web/API/MediaSource/duration)

Gets and sets the duration of the current media being presented.

[MediaSource.handle](/en-US/docs/Web/API/MediaSource/handle)Read only

Inside a dedicated worker, returns a [MediaSourceHandle](/en-US/docs/Web/API/MediaSourceHandle) object, a proxy for the `MediaSource` that can be transferred from the worker back to the main thread and attached to a media element via its [HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject) property.

[MediaSource.readyState](/en-US/docs/Web/API/MediaSource/readyState)Read only

Returns an enum representing the state of the current `MediaSource`, whether it is not currently attached to a media element (`closed`), attached and ready to receive [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects (`open`), or attached but the stream has been ended via [MediaSource.endOfStream()](/en-US/docs/Web/API/MediaSource/endOfStream) (`ended`.)

[MediaSource.sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers)Read only

Returns a [SourceBufferList](/en-US/docs/Web/API/SourceBufferList) object containing the list of [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects associated with this `MediaSource`.

## [Static properties](#static_properties)

[MediaSource.canConstructInDedicatedWorker](/en-US/docs/Web/API/MediaSource/canConstructInDedicatedWorker_static)Read only

A boolean; returns `true` if `MediaSource` worker support is implemented, providing a low-latency feature detection mechanism.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[MediaSource.addSourceBuffer()](/en-US/docs/Web/API/MediaSource/addSourceBuffer)

Creates a new [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) of the given MIME type and adds it to the [MediaSource.sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers) list.

[MediaSource.clearLiveSeekableRange()](/en-US/docs/Web/API/MediaSource/clearLiveSeekableRange)

Clears a seekable range previously set with a call to `setLiveSeekableRange()`.

[MediaSource.endOfStream()](/en-US/docs/Web/API/MediaSource/endOfStream)

Signals the end of the stream.

[MediaSource.removeSourceBuffer()](/en-US/docs/Web/API/MediaSource/removeSourceBuffer)

Removes the given [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) from the [MediaSource.sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers) list.

[MediaSource.setLiveSeekableRange()](/en-US/docs/Web/API/MediaSource/setLiveSeekableRange)

Sets the range that the user can seek to in the media element.

## [Static methods](#static_methods)

[MediaSource.isTypeSupported()](/en-US/docs/Web/API/MediaSource/isTypeSupported_static)

Returns a boolean value indicating if the given MIME type is supported by the current user agent — this is, if it can successfully create [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects for that MIME type.

## [Events](#events)

[sourceclose](/en-US/docs/Web/API/MediaSource/sourceclose_event)

Fired when the `MediaSource` instance is not attached to a media element anymore.

[sourceended](/en-US/docs/Web/API/MediaSource/sourceended_event)

Fired when the `MediaSource` instance is still attached to a media element, but [endOfStream()](/en-US/docs/Web/API/MediaSource/endOfStream) has been called.

[sourceopen](/en-US/docs/Web/API/MediaSource/sourceopen_event)

Fired when the `MediaSource` instance has been opened by a media element and is ready for data to be appended to the [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects in [sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers).

## [Examples](#examples)

### [Complete basic example](#complete_basic_example)

The following simple example loads a video with [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest), playing it as soon as it can. This example was written by Nick Desaulniers and can be [viewed live here](https://nickdesaulniers.github.io/netfix/demo/bufferAll.html) (you can also [download the source](https://github.com/nickdesaulniers/netfix/blob/gh-pages/demo/bufferAll.html) for further investigation). The function `getMediaSource()`, which is not defined here, returns a `MediaSource`.

js

```
const video = document.querySelector("video");

const assetURL = "frag_bunny.mp4";
// Need to be specific for Blink regarding codecs
// ./mp4info frag_bunny.mp4 | grep Codec
const mimeCodec = 'video/mp4; codecs="avc1.42E01E, mp4a.40.2"';
let mediaSource;

if ("MediaSource" in window && MediaSource.isTypeSupported(mimeCodec)) {
  mediaSource = getMediaSource();
  console.log(mediaSource.readyState); // closed
  video.src = URL.createObjectURL(mediaSource);
  mediaSource.addEventListener("sourceopen", sourceOpen);
} else {
  console.error("Unsupported MIME type or codec: ", mimeCodec);
}

function sourceOpen() {
  console.log(this.readyState); // open
  const sourceBuffer = mediaSource.addSourceBuffer(mimeCodec);
  fetchAB(assetURL, (buf) => {
    sourceBuffer.addEventListener("updateend", () => {
      mediaSource.endOfStream();
      video.play();
      console.log(mediaSource.readyState); // ended
    });
    sourceBuffer.appendBuffer(buf);
  });
}

function fetchAB(url, cb) {
  console.log(url);
  const xhr = new XMLHttpRequest();
  xhr.open("get", url);
  xhr.responseType = "arraybuffer";
  xhr.onload = () => {
    cb(xhr.response);
  };
  xhr.send();
}
```

### [Constructing a MediaSource in a dedicated worker and passing it to the main thread](#constructing_a_mediasource_in_a_dedicated_worker_and_passing_it_to_the_main_thread)

The [handle](/en-US/docs/Web/API/MediaSource/handle) property can be accessed inside a dedicated worker and the resulting [MediaSourceHandle](/en-US/docs/Web/API/MediaSourceHandle) object is then transferred over to the thread that created the worker (in this case the main thread) via a [postMessage()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage) call:

js

```
// Inside dedicated worker
let mediaSource = new MediaSource();
let handle = mediaSource.handle;
// Transfer the handle to the context that created the worker
postMessage({ arg: handle }, [handle]);

mediaSource.addEventListener("sourceopen", () => {
  // Await sourceopen on MediaSource before creating SourceBuffers
  // and populating them with fetched media — MediaSource won't
  // accept creation of SourceBuffers until it is attached to the
  // HTMLMediaElement and its readyState is "open"
});
```

Over in the main thread, we receive the handle via a [message](/en-US/docs/Web/API/Worker/message_event) event handler, attach it to a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) via its [HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject) property, and [play](/en-US/docs/Web/API/HTMLMediaElement/play) the video:

js

```
worker.addEventListener("message", (msg) => {
  let mediaSourceHandle = msg.data.arg;
  video.srcObject = mediaSourceHandle;
  video.play();
});
```

Note:[MediaSourceHandle](/en-US/docs/Web/API/MediaSourceHandle)s cannot be successfully transferred into or via a shared worker or service worker.

## [Specifications](#specifications)

Specification
[Media Source Extensions™# mediasource](https://w3c.github.io/media-source/#mediasource)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [SourceBuffer](/en-US/docs/Web/API/SourceBuffer)
- [SourceBufferList](/en-US/docs/Web/API/SourceBufferList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaSource/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediasource/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaSource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediasource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaSource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediasource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
