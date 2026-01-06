# MediaSourceHandle

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaSourceHandle&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `MediaSourceHandle` interface of the [Media Source Extensions API](/en-US/docs/Web/API/Media_Source_Extensions_API) is a proxy for a [MediaSource](/en-US/docs/Web/API/MediaSource) that can be transferred from a dedicated worker back to the main thread and attached to a media element via its [HTMLMediaElement.srcObject](/en-US/docs/Web/API/HTMLMediaElement/srcObject) property. `MediaSource` objects are not transferable because they are event targets, hence the need for `MediaSourceHandle`s.

It can be accessed via the [MediaSource.handle](/en-US/docs/Web/API/MediaSource/handle) property.

Each `MediaSource` object created inside a dedicated worker has its own distinct `MediaSourceHandle`. The `MediaSource.handle` getter will always return the `MediaSourceHandle` instance specific to the associated dedicated worker `MediaSource` instance. If the handle has already been transferred to the main thread using [postMessage()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage), the handle instance in the worker is technically detached and can't be transferred again.

`MediaSourceHandle` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

None.

## [Instance methods](#instance_methods)

None.

## [Examples](#examples)

The [handle](/en-US/docs/Web/API/MediaSource/handle) property can be accessed inside a dedicated worker and the resulting `MediaSourceHandle` object is then transferred over to the thread that created the worker (in this case the main thread) via a [postMessage()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage) call:

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

Note:`MediaSourceHandle`s cannot be successfully transferred into or via a shared worker or service worker.

## [Specifications](#specifications)

Specification
[Media Source Extensions™# mediasourcehandle](https://w3c.github.io/media-source/#mediasourcehandle)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MSE-in-Workers Demo by Matt Wolenetz](https://wolenetz.github.io/mse-in-workers-demo/mse-in-workers-demo.html)
- [Media Source Extensions API](/en-US/docs/Web/API/Media_Source_Extensions_API)
- [MediaSource](/en-US/docs/Web/API/MediaSource)
- [SourceBuffer](/en-US/docs/Web/API/SourceBuffer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaSourceHandle/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediasourcehandle/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaSourceHandle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediasourcehandle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaSourceHandle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediasourcehandle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa84b606ffd77c40a7306be6c932a74ab9ce6ab96%0A*+Document+last+modified%3A+2025-06-24T06%3A12%3A11.000Z%0A%0A%3C%2Fdetails%3E)
