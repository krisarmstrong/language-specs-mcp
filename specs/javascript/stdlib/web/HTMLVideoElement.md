# HTMLVideoElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLVideoElement&level=high)

Implemented by the [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element, the `HTMLVideoElement` interface provides special properties and methods for manipulating video objects. It also inherits properties and methods of [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) and [HTMLElement](/en-US/docs/Web/API/HTMLElement).

The list of [supported media formats](/en-US/docs/Web/Media/Guides/Formats) varies from one browser to the other. You should either provide your video in a single format that all the relevant browsers supports, or provide multiple video sources in enough different formats that all the browsers you need to support are covered.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent interface, [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), and [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLVideoElement.disablePictureInPicture](/en-US/docs/Web/API/HTMLVideoElement/disablePictureInPicture)

Indicates if the user agent should suggest the picture-in-picture to users, or not.

[HTMLVideoElement.height](/en-US/docs/Web/API/HTMLVideoElement/height)

A string that reflects the [height](/en-US/docs/Web/HTML/Reference/Elements/video#height) HTML attribute, which specifies the height of the display area, in CSS pixels.

[HTMLVideoElement.poster](/en-US/docs/Web/API/HTMLVideoElement/poster)

A string that reflects the [poster](/en-US/docs/Web/HTML/Reference/Elements/video#poster) HTML attribute, which specifies an image to show while no video data is available.

[HTMLVideoElement.videoHeight](/en-US/docs/Web/API/HTMLVideoElement/videoHeight)Read only

Returns an unsigned integer value indicating the intrinsic height of the resource in CSS pixels, or 0 if no media is available yet.

[HTMLVideoElement.videoWidth](/en-US/docs/Web/API/HTMLVideoElement/videoWidth)Read only

Returns an unsigned integer value indicating the intrinsic width of the resource in CSS pixels, or 0 if no media is available yet.

[HTMLVideoElement.width](/en-US/docs/Web/API/HTMLVideoElement/width)

A string that reflects the [width](/en-US/docs/Web/HTML/Reference/Elements/video#width) HTML attribute, which specifies the width of the display area, in CSS pixels.

### [Firefox-specific properties](#firefox-specific_properties)

`HTMLVideoElement.mozParsedFrames`Non-standardRead onlyDeprecated

Returns an `unsigned long` with the count of video frames that have been parsed from the media resource.

`HTMLVideoElement.mozDecodedFrames`Non-standardRead onlyDeprecated

Returns an `unsigned long` with the count of parsed video frames that have been decoded into images.

`HTMLVideoElement.mozPresentedFrames`Non-standardRead onlyDeprecated

Returns an `unsigned long` with the count of decoded frames that have been presented to the rendering pipeline for painting.

`HTMLVideoElement.mozPaintedFrames`Non-standardRead onlyDeprecated

Returns an `unsigned long` with the count of presented frames which were painted on the screen.

`HTMLVideoElement.mozFrameDelay`Non-standardRead onlyDeprecated

Returns a `double` with the time which the last painted video frame was late by, in seconds.

`HTMLVideoElement.mozHasAudio`Non-standardRead onlyDeprecated

Returns a boolean indicating if there is some audio associated with the video.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), and [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLVideoElement.cancelVideoFrameCallback()](/en-US/docs/Web/API/HTMLVideoElement/cancelVideoFrameCallback)

Cancels a previously-registered video frame callback (see [requestVideoFrameCallback()](/en-US/docs/Web/API/HTMLVideoElement/requestVideoFrameCallback)).

[HTMLVideoElement.getVideoPlaybackQuality()](/en-US/docs/Web/API/HTMLVideoElement/getVideoPlaybackQuality)

Returns a [VideoPlaybackQuality](/en-US/docs/Web/API/VideoPlaybackQuality) object that contains the current playback metrics. This information includes things like the number of dropped or corrupted frames, as well as the total number of frames.

[HTMLVideoElement.requestPictureInPicture()](/en-US/docs/Web/API/HTMLVideoElement/requestPictureInPicture)

Requests that the user agent enters the video into picture-in-picture mode.

[HTMLVideoElement.requestVideoFrameCallback()](/en-US/docs/Web/API/HTMLVideoElement/requestVideoFrameCallback)

Registers a callback function that runs when a new video frame is sent to the compositor. This enables developers to perform efficient operations on each video frame.

## [Events](#events)

Inherits events from its parent interface, [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), and [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[enterpictureinpicture](/en-US/docs/Web/API/HTMLVideoElement/enterpictureinpicture_event)

Fired when the `HTMLVideoElement` enters picture-in-picture mode successfully.

[leavepictureinpicture](/en-US/docs/Web/API/HTMLVideoElement/leavepictureinpicture_event)

Fired when the `HTMLVideoElement` leaves picture-in-picture mode successfully.

[resize](/en-US/docs/Web/API/HTMLVideoElement/resize_event)

Fires when one or both of the [videoWidth](/en-US/docs/Web/API/HTMLVideoElement/videoWidth) and [videoHeight](/en-US/docs/Web/API/HTMLVideoElement/videoHeight) properties have just been updated.

## [Specifications](#specifications)

Specification
[HTML# htmlvideoelement](https://html.spec.whatwg.org/multipage/media.html#htmlvideoelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- HTML element implementing this interface: [<video>](/en-US/docs/Web/HTML/Reference/Elements/video).
- [Supported media formats](/en-US/docs/Web/Media/Guides/Formats)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLVideoElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlvideoelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLVideoElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlvideoelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLVideoElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlvideoelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
