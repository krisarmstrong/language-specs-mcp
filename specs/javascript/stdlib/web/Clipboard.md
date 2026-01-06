# Clipboard

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboard&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Clipboard` interface of the [Clipboard API](/en-US/docs/Web/API/Clipboard_API) provides read and write access to the contents of the system clipboard. This allows a web application to implement cut, copy, and paste features.

The system clipboard is exposed through the global [Navigator.clipboard](/en-US/docs/Web/API/Navigator/clipboard) property.

All of the Clipboard API methods operate asynchronously; they return a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which is resolved once the clipboard access has been completed. The promise is rejected if clipboard access is denied.

All the methods require a [secure context](/en-US/docs/Web/Security/Defenses/Secure_Contexts). Additional requirements for using the API are discussed in the [Security consideration](/en-US/docs/Web/API/Clipboard_API#security_considerations) section of the API overview topic.

## In this article

- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

`Clipboard` is based on the [EventTarget](/en-US/docs/Web/API/EventTarget) interface, and includes its methods.

[read()](/en-US/docs/Web/API/Clipboard/read)

Requests arbitrary data (such as images) from the clipboard, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with an array of [ClipboardItem](/en-US/docs/Web/API/ClipboardItem) objects containing the clipboard's contents.

[readText()](/en-US/docs/Web/API/Clipboard/readText)

Requests text from the system clipboard, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that is fulfilled with a string containing the clipboard's text once it's available.

[write()](/en-US/docs/Web/API/Clipboard/write)

Writes arbitrary data to the system clipboard, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves when the operation completes.

[writeText()](/en-US/docs/Web/API/Clipboard/writeText)

Writes text to the system clipboard, returning a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that is resolved once the text is fully copied into the clipboard.

## [Specifications](#specifications)

Specification
[Clipboard API and events# clipboard-interface](https://w3c.github.io/clipboard-apis/#clipboard-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Document.execCommand()](/en-US/docs/Web/API/Document/execCommand)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 30, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Clipboard/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/clipboard/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboard&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fclipboard%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClipboard%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fclipboard%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E)
