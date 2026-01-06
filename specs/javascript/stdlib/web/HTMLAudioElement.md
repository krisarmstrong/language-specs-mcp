# HTMLAudioElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAudioElement&level=high)

The `HTMLAudioElement` interface provides access to the properties of [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) elements, as well as methods to manipulate them.

This element is based on, and inherits properties and methods from, the [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement) interface.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Audio()](/en-US/docs/Web/API/HTMLAudioElement/Audio)

Creates and returns a new `HTMLAudioElement` object, optionally starting the process of loading an audio file into it if the file URL is given.

## [Instance properties](#instance_properties)

No specific properties; inherits properties from its parent, [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), and from [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), and from [HTMLElement](/en-US/docs/Web/API/HTMLElement). It offers no methods of its own.

## [Examples](#examples)

### [Basic usage](#basic_usage)

You can create a `HTMLAudioElement` entirely with JavaScript using the [Audio()](/en-US/docs/Web/API/HTMLAudioElement/Audio) constructor:

js

```
const audioElement = new Audio("car_horn.wav");
```

then you can invoke the `play()` method on the element

js

```
audioElement.play();
```

Note: A common gotcha is trying to play an audio element immediately on page load. Modern browser's default autoplay policy will block that from happening. Refer to [Firefox](https://hacks.mozilla.org/2019/02/firefox-66-to-block-automatically-playing-audible-video-and-audio/) and [chrome](https://developer.chrome.com/blog/autoplay/) for best practices and workarounds.

Some of the more commonly used properties of the audio element include [src](/en-US/docs/Web/API/HTMLMediaElement/src), [currentTime](/en-US/docs/Web/API/HTMLMediaElement/currentTime), [duration](/en-US/docs/Web/API/HTMLMediaElement/duration), [paused](/en-US/docs/Web/API/HTMLMediaElement/paused), [muted](/en-US/docs/Web/API/HTMLMediaElement/muted), and [volume](/en-US/docs/Web/API/HTMLMediaElement/volume). This snippet copies the audio file's duration to a variable:

js

```
const audioElement = new Audio("car_horn.wav");
audioElement.addEventListener("loadeddata", () => {
  let duration = audioElement.duration;
  // The duration variable now holds the duration (in seconds) of the audio clip
});
```

## [Events](#events)

Inherits methods from its parent, [HTMLMediaElement](/en-US/docs/Web/API/HTMLMediaElement), and from its ancestor [HTMLElement](/en-US/docs/Web/API/HTMLElement). Listen to events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

## [Specifications](#specifications)

Specification
[HTML# htmlaudioelement](https://html.spec.whatwg.org/multipage/media.html#htmlaudioelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web media technologies](/en-US/docs/Web/Media)
- [Audio and Video Delivery](/en-US/docs/Web/Media/Guides/Audio_and_video_delivery)
- HTML element implementing this interface: [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLAudioElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlaudioelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAudioElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlaudioelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLAudioElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlaudioelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbe1922d62a0d31e4e3441db0e943aed8df736481%0A*+Document+last+modified%3A+2025-04-28T14%3A28%3A26.000Z%0A%0A%3C%2Fdetails%3E)
