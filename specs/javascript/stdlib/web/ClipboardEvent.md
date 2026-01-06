# ClipboardEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2017⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboardEvent&level=high)

The `ClipboardEvent` interface of the [Clipboard API](/en-US/docs/Web/API/Clipboard_API) represents events providing information related to modification of the clipboard, that is [cut](/en-US/docs/Web/API/Element/cut_event), [copy](/en-US/docs/Web/API/Element/copy_event), and [paste](/en-US/docs/Web/API/Element/paste_event) events.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ClipboardEvent()](/en-US/docs/Web/API/ClipboardEvent/ClipboardEvent)

Creates a `ClipboardEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[ClipboardEvent.clipboardData](/en-US/docs/Web/API/ClipboardEvent/clipboardData)Read only

A [DataTransfer](/en-US/docs/Web/API/DataTransfer) object containing the data affected by the user-initiated [cut](/en-US/docs/Web/API/Element/cut_event), [copy](/en-US/docs/Web/API/Element/copy_event), or [paste](/en-US/docs/Web/API/Element/paste_event) operation, along with its MIME type.

## [Instance methods](#instance_methods)

No specific methods; inherits methods from its parent [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[Clipboard API and events# clipboard-event-interfaces](https://w3c.github.io/clipboard-apis/#clipboard-event-interfaces)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Copy-related events: [copy](/en-US/docs/Web/API/Element/copy_event), [cut](/en-US/docs/Web/API/Element/cut_event), [paste](/en-US/docs/Web/API/Element/paste_event)
- [Clipboard API](/en-US/docs/Web/API/Clipboard_API)
- [Image support for Async Clipboard article](https://web.dev/articles/async-clipboard)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 9, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ClipboardEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/clipboardevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboardEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fclipboardevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboardEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fclipboardevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7087ffd50a4d81d1b91fe603c26456e9ce398574%0A*+Document+last+modified%3A+2024-01-09T04%3A36%3A06.000Z%0A%0A%3C%2Fdetails%3E)
