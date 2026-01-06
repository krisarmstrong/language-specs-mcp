# NDEFMessage

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFMessage&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `NDEFMessage` interface of the [Web NFC API](/en-US/docs/Web/API/Web_NFC_API) represents the content of an NDEF message that has been read from or could be written to an NFC tag. An instance is acquired by calling the `NDEFMessage()` constructor or from the [NDEFReadingEvent.message](/en-US/docs/Web/API/NDEFReadingEvent/message) property, which is passed to the [reading](/en-US/docs/Web/API/NDEFReader/reading_event) event.

## In this article

- [Constructor](#constructor)
- [Attributes](#attributes)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[NDEFMessage()](/en-US/docs/Web/API/NDEFMessage/NDEFMessage)Experimental

Creates a new `NDEFMessage` object, initialized with the given NDEF records.

## [Attributes](#attributes)

[NDEFMessage.records](/en-US/docs/Web/API/NDEFMessage/records)Read onlyExperimental

Returns the list of NDEF records contained in the message.

## [Specifications](#specifications)

Specification
[Web NFC# dom-ndefmessage](https://w3c.github.io/web-nfc/#dom-ndefmessage)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 20, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/NDEFMessage/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ndefmessage/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFMessage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fndefmessage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFMessage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fndefmessage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbb60fadaa7423d2195ae8727f197fa4361aa09df%0A*+Document+last+modified%3A+2023-02-20T08%3A52%3A54.000Z%0A%0A%3C%2Fdetails%3E)
