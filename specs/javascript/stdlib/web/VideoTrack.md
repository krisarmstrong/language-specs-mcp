# VideoTrack

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoTrack&level=not)

The `VideoTrack` interface represents a single video track from a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element.

The most common use for accessing a `VideoTrack` object is to toggle its [selected](/en-US/docs/Web/API/VideoTrack/selected) property in order to make it the active video track for its [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element.

## In this article

- [Instance properties](#instance_properties)
- [Usage notes](#usage_notes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[selected](/en-US/docs/Web/API/VideoTrack/selected)

A Boolean value which controls whether or not the video track is active. Only a single video track can be active at any given time, so setting this property to `true` for one track while another track is active will make that other track inactive.

[id](/en-US/docs/Web/API/VideoTrack/id)Read only

A string which uniquely identifies the track within the media. This ID can be used to locate a specific track within a video track list by calling [VideoTrackList.getTrackById()](/en-US/docs/Web/API/VideoTrackList/getTrackById). The ID can also be used as the fragment part of the URL if the media supports seeking by media fragment per the [Media Fragments URI specification](https://www.w3.org/TR/media-frags/).

[kind](/en-US/docs/Web/API/VideoTrack/kind)Read only

A string specifying the category into which the track falls. For example, the main video track would have a `kind` of `"main"`.

[label](/en-US/docs/Web/API/VideoTrack/label)Read only

A string providing a human-readable label for the track. For example, a track whose `kind` is `"sign"` might have a `label` of `"A sign-language interpretation"`. This string is empty if no label is provided.

[language](/en-US/docs/Web/API/VideoTrack/language)Read only

A string specifying the video track's primary language, or an empty string if unknown. The language is specified as a [BCP 47 language tag](/en-US/docs/Glossary/BCP_47_language_tag) such as `"en-US"` or `"pt-BR"`.

[sourceBuffer](/en-US/docs/Web/API/VideoTrack/sourceBuffer)Read only

The [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) that created the track. Returns null if the track was not created by a [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) or the [SourceBuffer](/en-US/docs/Web/API/SourceBuffer) has been removed from the [MediaSource.sourceBuffers](/en-US/docs/Web/API/MediaSource/sourceBuffers) attribute of its parent media source.

## [Usage notes](#usage_notes)

To get a `VideoTrack` for a given media element, use the element's [videoTracks](/en-US/docs/Web/API/HTMLMediaElement/videoTracks) property, which returns a [VideoTrackList](/en-US/docs/Web/API/VideoTrackList) object from which you can get the individual tracks contained in the media:

js

```
const el = document.querySelector("video");
const tracks = el.videoTracks;
```

You can then access the media's individual tracks using either array syntax or functions such as [forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach).

This first example gets the first video track on the media:

js

```
const firstTrack = tracks[0];
```

The next example scans through all of the media's video tracks, activating the first video track that is in the user's preferred language (taken from a variable `userLanguage`).

js

```
for (const track of tracks) {
  if (track.language === userLanguage) {
    track.selected = true;
    break;
  }
}
```

The [language](/en-US/docs/Web/API/VideoTrack/language) is specified as a valid [BCP 47 language tag](/en-US/docs/Glossary/BCP_47_language_tag), for example `"en-US"` for US English.

## [Specifications](#specifications)

Specification
[HTML# videotrack](https://html.spec.whatwg.org/multipage/media.html#videotrack)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 24, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VideoTrack/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/videotrack/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoTrack&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvideotrack%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVideoTrack%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvideotrack%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E)
