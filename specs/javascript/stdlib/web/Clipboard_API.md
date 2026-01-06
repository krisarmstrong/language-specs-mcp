# Clipboard API

The Clipboard API provides the ability to respond to clipboard commands (cut, copy, and paste), as well as to asynchronously read from and write to the system clipboard.

Note: Use this API in preference to the deprecated [document.execCommand()](/en-US/docs/Web/API/Document/execCommand) method for accessing the clipboard.

Note: This API is not available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API) (not exposed via [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator)).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Security considerations](#security_considerations)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The system clipboard is a data buffer belonging to the operating system hosting the browser, which is used for short-term data storage and/or data transfers between documents or applications. It is usually implemented as an anonymous, temporary [data buffer](https://en.wikipedia.org/wiki/Data_buffer), sometimes called the paste buffer, that can be accessed from most or all programs within the environment via defined programming interfaces.

The Clipboard API allows users to programmatically read and write text and other kinds of data to and from the system clipboard in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts), provided the user has met the criteria outlined in the [Security considerations](#security_considerations).

Events are fired as the result of [cut](/en-US/docs/Web/API/Element/cut_event), [copy](/en-US/docs/Web/API/Element/copy_event), and [paste](/en-US/docs/Web/API/Element/paste_event) operations modifying the clipboard. The events have a default action, for example the `copy` action copies the current selection to the system clipboard by default. The default action can be overridden by the event handler — see each of the events for more information.

## [Interfaces](#interfaces)

[Clipboard](/en-US/docs/Web/API/Clipboard)Secure context

Provides an interface for reading and writing text and data to or from the system clipboard. The specification refers to this as the 'Async Clipboard API'.

[ClipboardEvent](/en-US/docs/Web/API/ClipboardEvent)

Represents events providing information related to modification of the clipboard, that is [cut](/en-US/docs/Web/API/Element/cut_event), [copy](/en-US/docs/Web/API/Element/copy_event), and [paste](/en-US/docs/Web/API/Element/paste_event) events. The specification refers to this as the 'Clipboard Event API'.

[ClipboardItem](/en-US/docs/Web/API/ClipboardItem)Secure context

Represents a single item format, used when reading or writing data.

### [Extensions to other interfaces](#extensions_to_other_interfaces)

The Clipboard API extends the following APIs, adding the listed features.

[Navigator.clipboard](/en-US/docs/Web/API/Navigator/clipboard)Read onlySecure context

Returns a [Clipboard](/en-US/docs/Web/API/Clipboard) object that provides read and write access to the system clipboard.

`Element`[copy](/en-US/docs/Web/API/Element/copy_event) event

An event fired whenever the user initiates a copy action.

`Element`[cut](/en-US/docs/Web/API/Element/cut_event) event

An event fired whenever the user initiates a cut action.

`Element`[paste](/en-US/docs/Web/API/Element/paste_event) event

An event fired whenever the user initiates a paste action.

## [Security considerations](#security_considerations)

The Clipboard API allows users to programmatically read and write text and other kinds of data to and from the system clipboard in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts).

When reading from the clipboard, the specification requires that a user has recently interacted with the page ([transient user activation](/en-US/docs/Web/Security/Defenses/User_activation)) and that the call is made as a result of the user interacting with a browser or OS "paste element" (such as choosing "Paste" on a native context menu). In practice, browsers often allow read operations that do not satisfy these requirements, while placing other requirements instead (such as a permission or per-operation prompt). For writing to the clipboard the specification expects that the page has been granted the [Permissions API](/en-US/docs/Web/API/Permissions_API)`clipboard-write` permission, and the browser may also require [transient user activation](/en-US/docs/Web/Security/Defenses/User_activation). Browsers may place additional restrictions over use of the methods to access the clipboard.

Browser implementations have diverged from the specification. The differences are captured in the [Browser compatibility](#browser_compatibility) section and the current state is summarized below:

Chromium browsers:

- If a read isn't allowed by the spec and the document has focus, it triggers a request to use permission `clipboard-read`, and succeeds if the permission is granted (either because the user accepted the prompt, or because the permission was granted already).
- Writing requires either the `clipboard-write` permission or transient activation. If the permission is granted, it persists, and further transient activation is not required.
- The HTTP [Permissions-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy) permissions `clipboard-read` and `clipboard-write` must be allowed for [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe) elements that access the clipboard.

Firefox & Safari:

- If a read isn't allowed by the spec but transient user activation is still met, it triggers a user prompt in the form of an ephemeral context menu with a single "Paste" option (which becomes enabled after 1 second) and succeeds if the user chooses the option.
- Writing requires transient activation.
- The paste-prompt is suppressed if reading same-origin clipboard content, but not cross-origin content.
- The `clipboard-read` and `clipboard-write` permissions are not supported (and not planned to be supported) by Firefox or Safari.

Firefox [Web Extensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard):

- Reading text is only available for extensions with the Web Extension [clipboardRead](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions#clipboardread) permission. With this permission the extension does not require transient activation or a paste prompt.
- Writing text is available in secure context and with transient activation. With the Web Extension [clipboardWrite](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions#clipboardwrite) permission transient activation is not required.

## [Examples](#examples)

### [Accessing the clipboard](#accessing_the_clipboard)

The system clipboard is accessed through the [Navigator.clipboard](/en-US/docs/Web/API/Navigator/clipboard) global.

This snippet fetches the text from the clipboard and appends it to the first element found with the class `editor`. Since [readText()](/en-US/docs/Web/API/Clipboard/readText) returns an empty string if the clipboard isn't text, this code is safe.

js

```
navigator.clipboard
  .readText()
  .then(
    (clipText) => (document.querySelector(".editor").innerText += clipText),
  );
```

## [Specifications](#specifications)

Specification
[Clipboard API and events# clipboard-interface](https://w3c.github.io/clipboard-apis/#clipboard-interface)
[Clipboard API and events# clipboard-event-interfaces](https://w3c.github.io/clipboard-apis/#clipboard-event-interfaces)
[Clipboard API and events# clipboarditem](https://w3c.github.io/clipboard-apis/#clipboarditem)

## [Browser compatibility](#browser_compatibility)

### [api.Clipboard](#api.Clipboard)

### [api.ClipboardEvent](#api.ClipboardEvent)

### [api.ClipboardItem](#api.ClipboardItem)

## [See also](#see_also)

- [Image support for Async Clipboard article](https://web.dev/articles/async-clipboard)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Clipboard_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/clipboard_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboard_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fclipboard_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboard_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fclipboard_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
