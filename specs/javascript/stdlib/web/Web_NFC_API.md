# Web NFC API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_NFC_API&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The Web NFC API allows exchanging data over NFC via light-weight NFC Data Exchange Format (NDEF) messages.

Note: Devices and tags have to be formatted and recorded specifically to support NDEF record format to be used with Web NFC. Low-level operations are currently not supported by the API, however there is a public discussion about API that would add such functionality.

## In this article

- [Interfaces](#interfaces)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Interfaces](#interfaces)

[NDEFMessage](/en-US/docs/Web/API/NDEFMessage)

Interface that represents NDEF messages that can be received from or sent to a compatible tag via a `NDEFReader` object. A message is composed of metadata and NDEF Records.

[NDEFReader](/en-US/docs/Web/API/NDEFReader)Experimental

Interface that enables reading and writing messages from compatible NFC tags. The messages are represented as `NDEFMessage` objects.

[NDEFRecord](/en-US/docs/Web/API/NDEFRecord)

Interface that represents NDEF records that can be included in an NDEF message.

## [Specifications](#specifications)

Specification
[Web NFC# the-ndefreader-object](https://w3c.github.io/web-nfc/#the-ndefreader-object)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Web_NFC_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_nfc_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_NFC_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_nfc_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_NFC_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_nfc_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44c4ec928281dc2d7c5ea42b7d2c74a2013f16ac%0A*+Document+last+modified%3A+2024-07-26T15%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E)
