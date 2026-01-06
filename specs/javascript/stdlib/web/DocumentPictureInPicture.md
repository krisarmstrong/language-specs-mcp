# DocumentPictureInPicture

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentPictureInPicture&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `DocumentPictureInPicture` interface of the [Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API) is the entry point for creating and handling document picture-in-picture windows.

It is accessed via the [Window.documentPictureInPicture](/en-US/docs/Web/API/Window/documentPictureInPicture) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[window](/en-US/docs/Web/API/DocumentPictureInPicture/window)Read onlyExperimental

Returns a [Window](/en-US/docs/Web/API/Window) instance representing the browsing context inside the Picture-in-Picture window.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[requestWindow()](/en-US/docs/Web/API/DocumentPictureInPicture/requestWindow)Experimental

Opens the Picture-in-Picture window for the current main browsing context. Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with a [Window](/en-US/docs/Web/API/Window) instance representing the browsing context inside the Picture-in-Picture window.

## [Events](#events)

Inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[enter](/en-US/docs/Web/API/DocumentPictureInPicture/enter_event)Experimental

Fired when the Picture-in-Picture window is successfully opened.

## [Examples](#examples)

js

```
const videoPlayer = document.getElementById("player");

// …

// Open a Picture-in-Picture window.
const pipWindow = await window.documentPictureInPicture.requestWindow({
  width: videoPlayer.clientWidth,
  height: videoPlayer.clientHeight,
});

// …
```

See [Document Picture-in-Picture API Example](https://mdn.github.io/dom-examples/document-picture-in-picture/) for a full working demo (see the full [source code](https://github.com/mdn/dom-examples/tree/main/document-picture-in-picture) also).

## [Specifications](#specifications)

Specification
[Document Picture-in-Picture Specification# documentpictureinpicture](https://wicg.github.io/document-picture-in-picture/#documentpictureinpicture)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API)
- [Using the Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API/Using)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/DocumentPictureInPicture/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/documentpictureinpicture/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentPictureInPicture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdocumentpictureinpicture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentPictureInPicture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdocumentpictureinpicture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F759102220c07fb140b3e06971cd5981d8f0f134f%0A*+Document+last+modified%3A+2025-04-28T15%3A45%3A41.000Z%0A%0A%3C%2Fdetails%3E)
