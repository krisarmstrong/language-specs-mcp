# SourceBufferList

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSourceBufferList&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `SourceBufferList` interface represents a simple container list for multiple [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects.

The source buffer list containing the `SourceBuffer`s appended to a particular `MediaSource` can be retrieved using the [MediaSource.sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers) property.

The individual source buffers can be accessed using the [bracket notation](/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation)`[]`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[SourceBufferList.length](/en-US/docs/Web/API/SourceBufferList/length)Read only

Returns the number of [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) objects in the list.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

`addsourcebuffer`

Fired when a [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) is added to the list.

`removesourcebuffer`

Fired when a [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) is removed from the list.

## [Examples](#examples)

This example shows how to access the active source buffers of the [MediaSource](/en-US/docs/Web/API/MediaSource) connected to an already playing [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

js

```
// Video is an already playing video using a MediaSource srcObject
const video = document.querySelector("video");
const mediaSource = video.srcObject;
const sourceBufferList = mediaSource.activeSourceBuffers;
for (const sourceBuffer of sourceBufferList) {
  // Do something with each SourceBuffer, such as call abort()
  sourceBuffer.abort();
}
```

## [Specifications](#specifications)

Specification
[Media Source Extensions™# sourcebufferlist](https://w3c.github.io/media-source/#sourcebufferlist)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MediaSource](/en-US/docs/Web/API/MediaSource)
- [SourceBuffer](/en-US/docs/Web/API/SourceBuffer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/SourceBufferList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sourcebufferlist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSourceBufferList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsourcebufferlist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSourceBufferList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsourcebufferlist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1573959d78591b4079500af13019f901faaaca02%0A*+Document+last+modified%3A+2024-09-25T06%3A13%3A49.000Z%0A%0A%3C%2Fdetails%3E)
