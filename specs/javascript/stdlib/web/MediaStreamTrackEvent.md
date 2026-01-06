# MediaStreamTrackEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackEvent&level=high)

The `MediaStreamTrackEvent` interface of the [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) represents events which indicate that a [MediaStream](/en-US/docs/Web/API/MediaStream) has had tracks added to or removed from the stream through calls to [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API) methods. These events are sent to the stream when these changes occur.

The events based on this interface are [addtrack](/en-US/docs/Web/API/MediaStream/addtrack_event) and [removetrack](/en-US/docs/Web/API/MediaStream/removetrack_event).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaStreamTrackEvent()](/en-US/docs/Web/API/MediaStreamTrackEvent/MediaStreamTrackEvent)

Constructs a new `MediaStreamTrackEvent` with the specified configuration.

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[MediaStreamTrackEvent.track](/en-US/docs/Web/API/MediaStreamTrackEvent/track)Read only

Returns a [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack) object representing the track associated with the event.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[Media Capture and Streams# mediastreamtrackevent](https://w3c.github.io/mediacapture-main/#mediastreamtrackevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MediaStream](/en-US/docs/Web/API/MediaStream): [addtrack](/en-US/docs/Web/API/MediaStream/addtrack_event) and [removetrack](/en-US/docs/Web/API/MediaStream/removetrack_event) events
- [MediaStreamTrack](/en-US/docs/Web/API/MediaStreamTrack)
- [Media Capture and Streams API](/en-US/docs/Web/API/Media_Capture_and_Streams_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 25, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamTrackEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamtrackevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamtrackevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamTrackEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamtrackevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fac67e6f05d337e52e39f02a978b8c00bc43d583b%0A*+Document+last+modified%3A+2023-12-25T07%3A08%3A46.000Z%0A%0A%3C%2Fdetails%3E)
