# TextTrackCue

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackCue&level=high)

The `TextTrackCue` interface of the [WebVTT API](/en-US/docs/Web/API/WebVTT_API) is the abstract base class for the various derived cue types, such as [VTTCue](/en-US/docs/Web/API/VTTCue); you will work with these derived types rather than the base class.

These cues represent strings of text presented for some duration of time during the performance of a [TextTrack](/en-US/docs/Web/API/TextTrack). The cue includes the start time (the time at which the text will be displayed) and the end time (the time at which it will be removed from the display), as well as other information.

## In this article

- [Instance properties](#instance_properties)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from [EventTarget](/en-US/docs/Web/API/EventTarget).

[TextTrackCue.track](/en-US/docs/Web/API/TextTrackCue/track)Read only

The [TextTrack](/en-US/docs/Web/API/TextTrack) that this cue belongs to, or `null` if it doesn't belong to any.

[TextTrackCue.id](/en-US/docs/Web/API/TextTrackCue/id)

A string that identifies the cue.

[TextTrackCue.startTime](/en-US/docs/Web/API/TextTrackCue/startTime)

A `double` that represents the video time that the cue will start being displayed, in seconds.

[TextTrackCue.endTime](/en-US/docs/Web/API/TextTrackCue/endTime)

A `double` that represents the video time that the cue will stop being displayed, in seconds.

[TextTrackCue.pauseOnExit](/en-US/docs/Web/API/TextTrackCue/pauseOnExit)

A `boolean` for whether the video will pause when this cue stops being displayed.

## [Events](#events)

[enter](/en-US/docs/Web/API/TextTrackCue/enter_event)

Fired when a cue becomes active.

[exit](/en-US/docs/Web/API/TextTrackCue/exit_event)

Fired when the cue has stopped being active.

## [Specifications](#specifications)

Specification
[HTML# texttrackcue](https://html.spec.whatwg.org/multipage/media.html#texttrackcue)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/TextTrackCue/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/texttrackcue/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackCue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftexttrackcue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextTrackCue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftexttrackcue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3975bcf6caa09c9c5f7fddf2eef2be6c021d00f6%0A*+Document+last+modified%3A+2024-07-12T06%3A45%3A00.000Z%0A%0A%3C%2Fdetails%3E)
