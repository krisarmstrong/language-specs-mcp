# VideoPlaybackQuality

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoPlaybackQuality&level=high)

A `VideoPlaybackQuality` object is returned by the [HTMLVideoElement.getVideoPlaybackQuality()](/en-US/docs/Web/API/HTMLVideoElement/getVideoPlaybackQuality) method and contains metrics that can be used to determine the playback quality of a video.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `VideoPlaybackQuality` interface doesn't inherit properties from any other interfaces.

[creationTime](/en-US/docs/Web/API/VideoPlaybackQuality/creationTime)Read only

A [DOMHighResTimeStamp](/en-US/docs/Web/API/DOMHighResTimeStamp) containing the time in milliseconds between the start of the navigation and the creation of the object.

[droppedVideoFrames](/en-US/docs/Web/API/VideoPlaybackQuality/droppedVideoFrames)Read only

An `unsigned long` giving the number of video frames dropped since the creation of the associated [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

[totalVideoFrames](/en-US/docs/Web/API/VideoPlaybackQuality/totalVideoFrames)Read only

An `unsigned long` giving the number of video frames created and dropped since the creation of the associated [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement).

### [Obsolete properties](#obsolete_properties)

[corruptedVideoFrames](/en-US/docs/Web/API/VideoPlaybackQuality/corruptedVideoFrames)Read onlyDeprecated

An `unsigned long` giving the number of video frames corrupted since the creation of the associated [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement). A corrupted frame may be created or dropped.

[totalFrameDelay](/en-US/docs/Web/API/VideoPlaybackQuality/totalFrameDelay)Read onlyDeprecatedNon-standard

A `double` containing the sum of the frame delay since the creation of the associated [HTMLVideoElement](/en-US/docs/Web/API/HTMLVideoElement). The frame delay is the difference between a frame's theoretical presentation time and its effective display time.

## [Instance methods](#instance_methods)

The `VideoPlaybackQuality` interface has no methods, and does not inherit any.

## [Specifications](#specifications)

Specification
[Media Playback Quality# videoplaybackquality-interface](https://w3c.github.io/media-playback-quality/#videoplaybackquality-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [HTMLVideoElement.getVideoPlaybackQuality()](/en-US/docs/Web/API/HTMLVideoElement/getVideoPlaybackQuality) method to get a `VideoPlaybackQuality` object
- [MediaSource](/en-US/docs/Web/API/MediaSource)
- [SourceBuffer](/en-US/docs/Web/API/SourceBuffer)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/VideoPlaybackQuality/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videoplaybackquality/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoPlaybackQuality&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideoplaybackquality%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoPlaybackQuality%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideoplaybackquality%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbc46402e6a78656881da7060812387fb6a5bb0e3%0A*+Document+last+modified%3A+2023-02-19T08%3A44%3A46.000Z%0A%0A%3C%2Fdetails%3E)
