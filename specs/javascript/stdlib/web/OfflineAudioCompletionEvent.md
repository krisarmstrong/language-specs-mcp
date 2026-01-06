# OfflineAudioCompletionEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOfflineAudioCompletionEvent&level=high)

The [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)`OfflineAudioCompletionEvent` interface represents events that occur when the processing of an [OfflineAudioContext](/en-US/docs/Web/API/OfflineAudioContext) is terminated. The [complete](/en-US/docs/Web/API/OfflineAudioContext/complete_event) event uses this interface.

Note: This interface is marked as deprecated; it is still supported for legacy reasons, but it will soon be superseded when the promise version of [OfflineAudioContext.startRendering](/en-US/docs/Web/API/OfflineAudioContext/startRendering) is supported in browsers, which will no longer need it.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[OfflineAudioCompletionEvent()](/en-US/docs/Web/API/OfflineAudioCompletionEvent/OfflineAudioCompletionEvent)

Creates a new `OfflineAudioCompletionEvent` object instance.

## [Instance properties](#instance_properties)

Also inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[OfflineAudioCompletionEvent.renderedBuffer](/en-US/docs/Web/API/OfflineAudioCompletionEvent/renderedBuffer)Read only

An [AudioBuffer](/en-US/docs/Web/API/AudioBuffer) containing the result of processing an [OfflineAudioContext](/en-US/docs/Web/API/OfflineAudioContext).

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[Web Audio API# OfflineAudioCompletionEvent](https://webaudio.github.io/web-audio-api/#OfflineAudioCompletionEvent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/OfflineAudioCompletionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/offlineaudiocompletionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOfflineAudioCompletionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fofflineaudiocompletionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FOfflineAudioCompletionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fofflineaudiocompletionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
