# BlobEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBlobEvent&level=high)

The `BlobEvent` interface of the [MediaStream Recording API](/en-US/docs/Web/API/MediaStream_Recording_API) represents events associated with a [Blob](/en-US/docs/Web/API/Blob). These blobs are typically, but not necessarily, associated with media content.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[BlobEvent()](/en-US/docs/Web/API/BlobEvent/BlobEvent)

Creates a `BlobEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[BlobEvent.data](/en-US/docs/Web/API/BlobEvent/data)Read only

A [Blob](/en-US/docs/Web/API/Blob) representing the data associated with the event. The event was fired on the [EventTarget](/en-US/docs/Web/API/EventTarget) because of something happening on that specific [Blob](/en-US/docs/Web/API/Blob).

[BlobEvent.timecode](/en-US/docs/Web/API/BlobEvent/timecode)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) indicating the difference between the timestamp of the first chunk in data and the timestamp of the first chunk in the first BlobEvent produced by this recorder. Note that the timecode in the first produced BlobEvent does not need to be zero.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[MediaStream Recording# blobevent-section](https://w3c.github.io/mediacapture-record/#blobevent-section)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [Event](/en-US/docs/Web/API/Event) base interface.
- [MediaStream Recording API](/en-US/docs/Web/API/MediaStream_Recording_API): Sends `BlobEvent` objects each time a chunk of media is ready.
- [Using the MediaStream Recording API](/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 22, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/BlobEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/blobevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBlobEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fblobevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBlobEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fblobevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1c9d35561671086a47fa501a34ec7af2cf8182cf%0A*+Document+last+modified%3A+2023-12-22T23%3A18%3A19.000Z%0A%0A%3C%2Fdetails%3E)
