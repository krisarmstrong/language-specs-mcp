# SourceBuffer

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSourceBuffer&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `SourceBuffer` interface represents a chunk of media to be passed into an [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) and played, via a [MediaSource](/en-US/docs/Web/API/MediaSource) object. This can be made up of one or several media segments.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[SourceBuffer.appendWindowEnd](/en-US/docs/Web/API/SourceBuffer/appendWindowEnd)

Controls the timestamp for the end of the append window.

[SourceBuffer.appendWindowStart](/en-US/docs/Web/API/SourceBuffer/appendWindowStart)

Controls the timestamp for the start of the [append window](https://w3c.github.io/media-source/#append-window). This is a timestamp range that can be used to filter what media data is appended to the `SourceBuffer`. Coded media frames with timestamps within this range will be appended, whereas those outside the range will be filtered out.

[SourceBuffer.audioTracks](/en-US/docs/Web/API/SourceBuffer/audioTracks)Read only

A list of the audio tracks currently contained inside the `SourceBuffer`.

[SourceBuffer.buffered](/en-US/docs/Web/API/SourceBuffer/buffered)Read only

Returns the time ranges that are currently buffered in the `SourceBuffer`.

[SourceBuffer.mode](/en-US/docs/Web/API/SourceBuffer/mode)

Controls how the order of media segments in the `SourceBuffer` is handled, in terms of whether they can be appended in any order, or they have to be kept in a strict sequence.

[SourceBuffer.textTracks](/en-US/docs/Web/API/SourceBuffer/textTracks)Read onlyExperimental

A list of the text tracks currently contained inside the `SourceBuffer`.

[SourceBuffer.timestampOffset](/en-US/docs/Web/API/SourceBuffer/timestampOffset)

Controls the offset applied to timestamps inside media segments that are subsequently appended to the `SourceBuffer`.

[SourceBuffer.updating](/en-US/docs/Web/API/SourceBuffer/updating)Read only

A boolean indicating whether the `SourceBuffer` is currently being updated — i.e., whether an [appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) or [remove()](/en-US/docs/Web/API/SourceBuffer/remove) operation is currently in progress.

[SourceBuffer.videoTracks](/en-US/docs/Web/API/SourceBuffer/videoTracks)Read only

A list of the video tracks currently contained inside the `SourceBuffer`.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[SourceBuffer.abort()](/en-US/docs/Web/API/SourceBuffer/abort)

Aborts the current segment and resets the segment parser.

[SourceBuffer.appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer)

Appends media segment data from an [ArrayBuffer](/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), a [TypedArray](/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) or a [DataView](/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) object to the `SourceBuffer`.

[SourceBuffer.appendBufferAsync()](/en-US/docs/Web/API/SourceBuffer/appendBufferAsync)Non-standardExperimental

Starts the process of asynchronously appending the specified buffer to the `SourceBuffer`. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is fulfilled once the buffer has been appended.

[SourceBuffer.changeType()](/en-US/docs/Web/API/SourceBuffer/changeType)

Changes the [MIME type](/en-US/docs/Glossary/MIME_type) that future calls to [appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) will expect the new data to conform to.

[SourceBuffer.remove()](/en-US/docs/Web/API/SourceBuffer/remove)

Removes media segments within a specific time range from the `SourceBuffer`.

[SourceBuffer.removeAsync()](/en-US/docs/Web/API/SourceBuffer/removeAsync)Non-standardExperimental

Starts the process of asynchronously removing media segments in the specified range from the `SourceBuffer`. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is fulfilled once all matching segments have been removed.

## [Events](#events)

[abort](/en-US/docs/Web/API/SourceBuffer/abort_event)

Fired when the buffer appending is aborted, because the [SourceBuffer.abort()](/en-US/docs/Web/API/SourceBuffer/abort) or [MediaSource.removeSourceBuffer()](/en-US/docs/Web/API/MediaSource/removeSourceBuffer) method is called while the [SourceBuffer.appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) algorithm is still running. [SourceBuffer.updating](/en-US/docs/Web/API/SourceBuffer/updating) changes from `true` to `false`.

[error](/en-US/docs/Web/API/SourceBuffer/error_event)

Fired when an error occurs during the processing of an [appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) operation. [SourceBuffer.updating](/en-US/docs/Web/API/SourceBuffer/updating) changes from `true` to `false`.

[update](/en-US/docs/Web/API/SourceBuffer/update_event)

Fired whenever [SourceBuffer.appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) or [SourceBuffer.remove()](/en-US/docs/Web/API/SourceBuffer/remove) completes. [SourceBuffer.updating](/en-US/docs/Web/API/SourceBuffer/updating) changes from `true` to `false`.

[updateend](/en-US/docs/Web/API/SourceBuffer/updateend_event)

Fired after the (not necessarily successful) completion of an [appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) or [remove()](/en-US/docs/Web/API/SourceBuffer/remove) operation. This event is fired after the `update`, `error`, or `abort` events.

[updatestart](/en-US/docs/Web/API/SourceBuffer/updatestart_event)

Fired when an [appendBuffer()](/en-US/docs/Web/API/SourceBuffer/appendBuffer) or [remove()](/en-US/docs/Web/API/SourceBuffer/remove) operation begins. [updating](/en-US/docs/Web/API/SourceBuffer/updating) changes from `false` to `true`.

## [Examples](#examples)

### [Loading a video chunk by chunk](#loading_a_video_chunk_by_chunk)

The following example loads a video chunk by chunk as fast as possible, playing it as soon as it can.

You can see the complete code at [https://github.com/mdn/dom-examples/tree/main/sourcebuffer](https://github.com/mdn/dom-examples/tree/main/sourcebuffer) and try the demo live at [https://mdn.github.io/dom-examples/sourcebuffer/](https://mdn.github.io/dom-examples/sourcebuffer/).

js

```
const video = document.querySelector("video");

const assetURL = "frag_bunny.mp4";
// Need to be specific for Blink regarding codecs
const mimeCodec = 'video/mp4; codecs="avc1.42E01E, mp4a.40.2"';

function loadVideo() {
  if (MediaSource.isTypeSupported(mimeCodec)) {
    const mediaSource = new MediaSource();
    console.log(mediaSource.readyState); // closed
    video.src = URL.createObjectURL(mediaSource);
    mediaSource.addEventListener("sourceopen", sourceOpen);
  } else {
    console.error("Unsupported MIME type or codec: ", mimeCodec);
  }
}

async function sourceOpen() {
  console.log(this.readyState); // open
  const sourceBuffer = this.addSourceBuffer(mimeCodec);
  const response = await fetch(assetURL);
  const buffer = await response.arrayBuffer();
  sourceBuffer.addEventListener("updateend", () => {
    this.endOfStream();
    video.play();
    console.log(this.readyState); // ended
  });
  sourceBuffer.appendBuffer(buffer);
}

const load = document.querySelector("#load");
load.addEventListener("click", loadVideo);
```

## [Specifications](#specifications)

Specification
[Media Source Extensions™# sourcebuffer](https://w3c.github.io/media-source/#sourcebuffer)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MediaSource](/en-US/docs/Web/API/MediaSource)
- [SourceBufferList](/en-US/docs/Web/API/SourceBufferList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/SourceBuffer/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sourcebuffer/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSourceBuffer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsourcebuffer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSourceBuffer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsourcebuffer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
