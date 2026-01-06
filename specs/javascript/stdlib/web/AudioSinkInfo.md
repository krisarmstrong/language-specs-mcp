# AudioSinkInfo

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioSinkInfo&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `AudioSinkInfo` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents information describing an [AudioContext](/en-US/docs/Web/API/AudioContext)'s sink ID, retrieved via [AudioContext.sinkId](/en-US/docs/Web/API/AudioContext/sinkId).

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[type](/en-US/docs/Web/API/AudioSinkInfo/type)Read onlyExperimental

Returns the type of the audio output device.

## [Examples](#examples)

If a new [AudioContext](/en-US/docs/Web/API/AudioContext) is created with a `sinkId` value of `{ type: 'none' }`, calling [AudioContext.sinkId](/en-US/docs/Web/API/AudioContext/sinkId) later in the code will return an `AudioSinkInfo` object containing `type: 'none'`. This is currently the only value available.

js

```
audioCtx = new window.AudioContext({
  sinkId: { type: "none" },
});

// …

audioCtx.sinkId;
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioSinkInfo](https://webaudio.github.io/web-audio-api/#AudioSinkInfo)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [SetSinkId test example](https://mdn.github.io/dom-examples/audiocontext-setsinkid/) (check out the [source code](https://github.com/mdn/dom-examples/tree/main/audiocontext-setsinkid))
- [AudioContext.setSinkId()](/en-US/docs/Web/API/AudioContext/setSinkId)
- [AudioContext.sinkId](/en-US/docs/Web/API/AudioContext/sinkId)
- [sinkchange](/en-US/docs/Web/API/AudioContext/sinkchange_event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioSinkInfo/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiosinkinfo/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioSinkInfo&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiosinkinfo%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioSinkInfo%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiosinkinfo%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E)
