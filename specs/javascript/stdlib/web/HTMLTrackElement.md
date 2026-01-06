# HTMLTrackElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTrackElement&level=high)

The `HTMLTrackElement` interface represents an [HTML](/en-US/docs/Glossary/HTML)[<track>](/en-US/docs/Web/HTML/Reference/Elements/track) element within the [DOM](/en-US/docs/Glossary/DOM). This element can be used as a child of either [<audio>](/en-US/docs/Web/HTML/Reference/Elements/audio) or [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) to specify a text track containing information such as closed captions or subtitles.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLTrackElement.kind](/en-US/docs/Web/API/HTMLTrackElement/kind)

A string that reflects the [kind](/en-US/docs/Web/HTML/Reference/Elements/track#kind) HTML attribute, indicating how the text track is meant to be used. Possible values are: `subtitles`, `captions`, `descriptions`, `chapters`, or `metadata`.

[HTMLTrackElement.src](/en-US/docs/Web/API/HTMLTrackElement/src)

A string that reflects the [src](/en-US/docs/Web/HTML/Reference/Elements/track#src) HTML attribute, indicating the address of the text track data.

[HTMLTrackElement.srclang](/en-US/docs/Web/API/HTMLTrackElement/srclang)

A string that reflects the [srclang](/en-US/docs/Web/HTML/Reference/Elements/track#srclang) HTML attribute, indicating the language of the text track data.

[HTMLTrackElement.label](/en-US/docs/Web/API/HTMLTrackElement/label)

A string that reflects the [label](/en-US/docs/Web/HTML/Reference/Elements/track#label) HTML attribute, indicating a user-readable title for the track.

[HTMLTrackElement.default](/en-US/docs/Web/API/HTMLTrackElement/default)

A boolean value reflecting the [default](/en-US/docs/Web/HTML/Reference/Elements/track#default) attribute, indicating that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate.

[HTMLTrackElement.readyState](/en-US/docs/Web/API/HTMLTrackElement/readyState)Read only

Returns an `unsigned short` that show the readiness state of the track:

ConstantValueDescription`NONE`0Indicates that the text track's cues have not been obtained.`LOADING`1Indicates that the text track is loading and there have been no fatal errors encountered so far. Further cues might still be added to the track by the parser.`LOADED`2Indicates that the text track has been loaded with no fatal errors.`ERROR`3Indicates that the text track was enabled, but when the user agent attempted to obtain it, this failed in some way. Some or all of the cues are likely missing and will not be obtained.[HTMLTrackElement.track](/en-US/docs/Web/API/HTMLTrackElement/track)Read only

Returns [TextTrack](/en-US/docs/Web/API/TextTrack) is the track element's text track data.

## [Instance methods](#instance_methods)

No specific method; inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

## [Events](#events)

Inherits events from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[cuechange](/en-US/docs/Web/API/HTMLTrackElement/cuechange_event)

Sent when the underlying [TextTrack](/en-US/docs/Web/API/TextTrack) has changed the currently-presented cues. This event is always sent to the `TextTrack` but is also sent to the `HTMLTrackElement` if one is associated with the track. You may also use the `oncuechange` event handler to establish a handler for this event.

## [Usage notes](#usage_notes)

### [Loading of the track's text resource](#loading_of_the_tracks_text_resource)

The WebVTT or TTML data describing the actual cues for the text track isn't loaded if the track's [mode](/en-US/docs/Web/API/TextTrack/mode) is initially in the `disabled` state. If you need to be able to perform any processing on the track after the `<track>` is set up, you should instead ensure that the track's `mode` is either `hidden` (if you don't want it to start out being presented to the user) or `showing` (to initially display the track). You can then change the mode as desired later.

## [Specifications](#specifications)

Specification
[HTML# htmltrackelement](https://html.spec.whatwg.org/multipage/media.html#htmltrackelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<track>](/en-US/docs/Web/HTML/Reference/Elements/track).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTrackElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltrackelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTrackElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltrackelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTrackElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltrackelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
