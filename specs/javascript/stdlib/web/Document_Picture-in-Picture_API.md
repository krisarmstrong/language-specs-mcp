# Document Picture-in-Picture API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument_Picture-in-Picture_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The Document Picture-in-Picture API makes it possible to open an always-on-top window that can be populated with arbitrary HTML content — for example a video with custom controls or a set of streams showing the participants of a video conference call. It extends the earlier [Picture-in-Picture API for <video>](/en-US/docs/Web/API/Picture-in-Picture_API), which specifically enables an HTML [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element to be put into an always-on-top window.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [CSS additions](#css_additions)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Concepts and usage](#concepts_and_usage)

It is often helpful to have a different window available to a web app in addition to the main window in which the app is running. You might want to browse other windows while keeping specific app content in view, or you might want to give that content its own space while keeping the main app window freed up to display other content. You could handle this by just opening a regular new browser window, but this has two major issues:

1. You have to handle sharing of state information between the two windows.
2. The additional app window doesn't always stay on top, and can therefore get hidden by other windows.

To solve these problems, web browsers have introduced APIs allowing apps to spawn an always-on-top window that is part of the same session. The first recognized use case was keeping video content playing in a separate window so that the user can continue to consume it while looking at other content. This is handled using the [Picture-in-Picture API for <video>](/en-US/docs/Web/API/Picture-in-Picture_API), which is directly used on a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element to place it into the separate window.

However, this API has been found to be somewhat limiting — you can only put a single `<video>` element into the always-on-top window, with minimal browser-generated controls. To provide more flexibility, the Document Picture-in-Picture API has been introduced. This allows any content to be placed in the always-on-top window for a wide range of use cases, including:

- An always-on-top custom video player showing one or multiple videos with custom controls and styling.
- A video conferencing system that allows the user to always see the other participant's streams, plus controls for presenting content, muting, ending calls, etc.
- Always-visible productivity tools such as timers, notes, to-do lists, messenger tools, etc.
- A separate window in which to keep additional content while the main app window is kept free of clutter. For example, you might have an action or roleplaying game running where you want to show the game controls, instructions, or lore in an additional window, keeping the main window free for displaying the game locations and map.

### [How does it work?](#how_does_it_work)

A new [DocumentPictureInPicture](/en-US/docs/Web/API/DocumentPictureInPicture) object instance representing the always-on-top Picture-in-Picture window for the current document context is available via [Window.documentPictureInPicture](/en-US/docs/Web/API/Window/documentPictureInPicture). The Picture-in-Picture window is opened by calling the [DocumentPictureInPicture.requestWindow()](/en-US/docs/Web/API/DocumentPictureInPicture/requestWindow) method, which returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills with the window's own [Window](/en-US/docs/Web/API/Window) object.

The Picture-in-Picture window is similar to a blank same-origin window opened via [Window.open()](/en-US/docs/Web/API/Window/open), with some differences:

- The Picture-in-Picture window floats on top of other windows.
- The Picture-in-Picture window never outlives the opening window.
- The Picture-in-Picture window cannot be navigated.
- The Picture-in-Picture window position cannot be set by the website.
- The Picture-in-Picture window is limited to one per browser tab at a time, with the user agent potentially further restricting the global number of Picture-in-Picture windows open.

Apart from that, you can manipulate the Picture-in-Picture window's `Window` instance however you want, for example appending the content you want to display there onto its DOM, and copying stylesheets to it so that the appended content will be styled the same way as when it is in the main window. You can also close the Picture-in-Picture window (by clicking the browser-provided control, or by running [Window.close()](/en-US/docs/Web/API/Window/close) on it), and then react to it closing using the standard [pagehide](/en-US/docs/Web/API/Window/pagehide_event). When it closes, you'll want to put the content it was showing back into the main app window.

See [Using the Document Picture-in-Picture API](/en-US/docs/Web/API/Document_Picture-in-Picture_API/Using) for a detailed usage guide.

## [Interfaces](#interfaces)

[DocumentPictureInPicture](/en-US/docs/Web/API/DocumentPictureInPicture)

The entry point for creating and handling document Picture-in-Picture windows.

[DocumentPictureInPictureEvent](/en-US/docs/Web/API/DocumentPictureInPictureEvent)

Event object for the [enter](/en-US/docs/Web/API/DocumentPictureInPicture/enter_event) event, which fires when the Picture-in-Picture window is opened.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[Window.documentPictureInPicture](/en-US/docs/Web/API/Window/documentPictureInPicture)

Returns a reference to the [DocumentPictureInPicture](/en-US/docs/Web/API/DocumentPictureInPicture) object for the current document context.

## [CSS additions](#css_additions)

[display-mode](/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode), the `picture-in-picture` value

A [CSS](/en-US/docs/Web/CSS)[media feature](/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features) value that allows developers to apply CSS to a document based on whether it is being displayed in Picture-in-Picture mode.

## [Examples](#examples)

See [Document Picture-in-Picture API Example](https://mdn.github.io/dom-examples/document-picture-in-picture/) for a full working demo (see the full [source code](https://github.com/mdn/dom-examples/tree/main/document-picture-in-picture) also).

## [Specifications](#specifications)

Specification
[Document Picture-in-Picture Specification# dom-window-documentpictureinpicture](https://wicg.github.io/document-picture-in-picture/#dom-window-documentpictureinpicture)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Document_Picture-in-Picture_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/document_picture-in-picture_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument_Picture-in-Picture_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdocument_picture-in-picture_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDocument_Picture-in-Picture_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdocument_picture-in-picture_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fad9776a6cf53eaf570ac0515402247e82ecefcfe%0A*+Document+last+modified%3A+2025-11-04T17%3A21%3A06.000Z%0A%0A%3C%2Fdetails%3E)
