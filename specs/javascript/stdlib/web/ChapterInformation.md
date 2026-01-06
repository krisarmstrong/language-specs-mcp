# ChapterInformation

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChapterInformation&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `ChapterInformation` interface of the [Media Session API](/en-US/docs/Web/API/Media_Session_API) represents the metadata for an individual chapter of a media resource (i.e., a video or audio file).

The chapter information for a given media resource is set when it is first created, via the `chapterInfo` property of the [MediaMetadata()](/en-US/docs/Web/API/MediaMetadata/MediaMetadata) constructor's initialization object. The property takes an array of `ChapterInformation` objects as its value.

You can access the chapter information for an existing [MediaMetadata](/en-US/docs/Web/API/MediaMetadata) object via its [chapterInfo](/en-US/docs/Web/API/MediaMetadata/chapterInfo) property. This returns an array of `ChapterInformation` objects.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[ChapterInformation.artwork](/en-US/docs/Web/API/ChapterInformation/artwork)Read onlyExperimental

Returns an [Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) of objects representing images associated with the chapter.

[ChapterInformation.startTime](/en-US/docs/Web/API/ChapterInformation/startTime)Read onlyExperimental

Returns a number, in seconds, representing the start time of the chapter.

[ChapterInformation.title](/en-US/docs/Web/API/ChapterInformation/title)Read onlyExperimental

Returns a string representing the title of the chapter.

## [Examples](#examples)

The sample code below from [Video / Media Session Sample](https://googlechrome.github.io/samples/media-session/video.html) shows a typical structure for the `ChapterInformation` object:

js

```
const BASE_URL = "https://storage.googleapis.com/media-session/";

const metadata = {
  // …
  chapterInfo: [
    {
      title: "Chapter 1",
      startTime: 0,
      artwork: [
        {
          src: `${BASE_URL}sintel/chapter1-128.png`,
          sizes: "128x128",
          type: "image/png",
        },
        {
          src: `${BASE_URL}sintel/chapter1-512.png`,
          sizes: "512x512",
          type: "image/png",
        },
      ],
    },
    {
      title: "Chapter 2",
      startTime: 37,
      artwork: [
        {
          src: `${BASE_URL}sintel/chapter2-128.png`,
          sizes: "128x128",
          type: "image/png",
        },
        {
          src: `${BASE_URL}sintel/chapter2-512.png`,
          sizes: "512x512",
          type: "image/png",
        },
      ],
    },
  ],
};
```

The following snippet shows how it can be used inside Media Session code (the above object property is part of the `playlist` object referenced below):

js

```
function updateMetadata() {
  const track = playlist[index];

  log(`Playing ${track.title} track...`);
  navigator.mediaSession.metadata = new MediaMetadata({
    title: track.title,
    artist: track.artist,
    artwork: track.artwork,
    chapterInfo: track.chapterInfo,
  });

  // …
}
```

## [Specifications](#specifications)

Specification
[Media Session# chapterinformation](https://w3c.github.io/mediasession/#chapterinformation)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [MediaMetadata](/en-US/docs/Web/API/MediaMetadata)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ChapterInformation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/chapterinformation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChapterInformation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fchapterinformation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FChapterInformation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fchapterinformation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6d2000984203c51f1aad49107ebcebe14d3c1238%0A*+Document+last+modified%3A+2025-05-30T14%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E)
