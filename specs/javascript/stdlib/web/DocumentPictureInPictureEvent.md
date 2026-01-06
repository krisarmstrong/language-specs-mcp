# DocumentPictureInPictureEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentPictureInPictureEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `DocumentPictureInPictureEvent` interface of the [Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API) is the event object for the [enter](/en-US/docs/Web/API/DocumentPictureInPicture/enter_event) event, which fires when the Picture-in-Picture window is opened.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[DocumentPictureInPictureEvent()](/en-US/docs/Web/API/DocumentPictureInPictureEvent/DocumentPictureInPictureEvent)Experimental

Creates a new `DocumentPictureInPictureEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[window](/en-US/docs/Web/API/DocumentPictureInPictureEvent/window)Read onlyExperimental

Returns a [Window](/en-US/docs/Web/API/Window) instance representing the browsing context inside the `DocumentPictureInPicture` window the event was fired on.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

js

```
documentPictureInPicture.addEventListener("enter", (event) => {
  const pipWindow = event.window;
  console.log("Video player has entered the pip window");

  const pipMuteButton = pipWindow.document.createElement("button");
  pipMuteButton.textContent = "Mute";
  pipMuteButton.addEventListener("click", () => {
    const pipVideo = pipWindow.document.querySelector("#video");
    if (!pipVideo.muted) {
      pipVideo.muted = true;
      pipMuteButton.textContent = "Unmute";
    } else {
      pipVideo.muted = false;
      pipMuteButton.textContent = "Mute";
    }
  });

  pipWindow.document.body.append(pipMuteButton);
});
```

## [Specifications](#specifications)

Specification
[Document Picture-in-Picture Specification# documentpictureinpictureevent](https://wicg.github.io/document-picture-in-picture/#documentpictureinpictureevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API)
- [Using the Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API/Using)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DocumentPictureInPictureEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/documentpictureinpictureevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentPictureInPictureEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdocumentpictureinpictureevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocumentPictureInPictureEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdocumentpictureinpictureevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbac20b9ed34bf5b6427ba9274c99c1737dc309ff%0A*+Document+last+modified%3A+2024-10-08T15%3A13%3A09.000Z%0A%0A%3C%2Fdetails%3E)
