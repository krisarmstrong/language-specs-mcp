# TimeRanges

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTimeRanges&level=high)

When loading a media resource for use by an [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) or [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element, the `TimeRanges` interface is used for representing the time ranges of the media resource that have been buffered, the time ranges that have been played, and the time ranges that are seekable.

A `TimeRanges` object includes one or more ranges of time, each specified by a starting time offset and an ending time offset. You reference each time range by using the `start()` and `end()` methods, passing the index number of the time range you want to retrieve.

## In this article

- [Normalized TimeRanges objects](#normalized_timeranges_objects)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Normalized TimeRanges objects](#normalized_timeranges_objects)

Several members of [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) objects return a normalized TimeRanges object — which [the spec describes](https://html.spec.whatwg.org/multipage/media.html#normalised-timeranges-object) as having the following characteristics:

The ranges in such an object are ordered, don't overlap, and don't touch (adjacent ranges are folded into one bigger range). A range can be empty (referencing just a single moment in time).

## [Instance properties](#instance_properties)

[TimeRanges.length](/en-US/docs/Web/API/TimeRanges/length)Read only

Returns an `unsigned long` representing the number of time ranges represented by the time range object.

## [Instance methods](#instance_methods)

[TimeRanges.start()](/en-US/docs/Web/API/TimeRanges/start)

Returns the time for the start of the range with the specified index.

[TimeRanges.end()](/en-US/docs/Web/API/TimeRanges/end)

Returns the time for the end of the specified range.

## [Specifications](#specifications)

Specification
[HTML# time-ranges](https://html.spec.whatwg.org/multipage/media.html#time-ranges)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TimeRanges/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/timeranges/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTimeRanges&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftimeranges%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTimeRanges%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftimeranges%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F87440643d71bf81a5bf4b8fa21db9e3d56ead395%0A*+Document+last+modified%3A+2025-10-13T15%3A53%3A24.000Z%0A%0A%3C%2Fdetails%3E)
