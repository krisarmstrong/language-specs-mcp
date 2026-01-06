# MediaMetadata

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaMetadata&level=not)

The `MediaMetadata` interface of the [Media Session API](/en-US/docs/Web/API/Media_Session_API) allows a web page to provide rich media metadata for display in a platform UI.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[MediaMetadata()](/en-US/docs/Web/API/MediaMetadata/MediaMetadata)

Creates a new `MediaMetaData` object.

## [Instance properties](#instance_properties)

[MediaMetadata.album](/en-US/docs/Web/API/MediaMetadata/album)

Returns or sets the name of the album or collection containing the media to be played.

[MediaMetadata.artist](/en-US/docs/Web/API/MediaMetadata/artist)

Returns or sets the name of the artist, group, creator, etc. of the media to be played.

[MediaMetadata.artwork](/en-US/docs/Web/API/MediaMetadata/artwork)

Returns or sets an array of images associated with playing media.

[MediaMetadata.chapterInfo](/en-US/docs/Web/API/MediaMetadata/chapterInfo)Read onlyExperimental

Returns an array of chapter information metadata associated with playing media, represented by [ChapterInformation](/en-US/docs/Web/API/ChapterInformation) object instances.

[MediaMetadata.title](/en-US/docs/Web/API/MediaMetadata/title)

Returns or sets the title of the media to be played.

## [Examples](#examples)

The following example checks for browser compatibility and sets the current metadata for the media session.

js

```
if ("mediaSession" in navigator) {
  navigator.mediaSession.metadata = new MediaMetadata({
    title: "Unforgettable",
    artist: "Nat King Cole",
    album: "The Ultimate Collection (Remastered)",
    artwork: [
      {
        src: "https://dummyimage.com/96x96",
        sizes: "96x96",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/128x128",
        sizes: "128x128",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/192x192",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/256x256",
        sizes: "256x256",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/384x384",
        sizes: "384x384",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/512x512",
        sizes: "512x512",
        type: "image/png",
      },
    ],
  });
}
```

## [Specifications](#specifications)

Specification
[Media Session# the-mediametadata-interface](https://w3c.github.io/mediasession/#the-mediametadata-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaMetadata/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediametadata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaMetadata&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediametadata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaMetadata%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediametadata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb60bc79c7ad36c56dddf6760d2fd4dbb642d2023%0A*+Document+last+modified%3A+2024-08-08T11%3A52%3A10.000Z%0A%0A%3C%2Fdetails%3E)
