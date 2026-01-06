# NDEFReadingEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFReadingEvent&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `NDEFReadingEvent` interface of the [Web NFC API](/en-US/docs/Web/API/Web_NFC_API) represents events dispatched on new NFC readings obtained by [NDEFReader](/en-US/docs/Web/API/NDEFReader).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[NDEFReadingEvent.NDEFReadingEvent()](/en-US/docs/Web/API/NDEFReadingEvent/NDEFReadingEvent)Experimental

Creates a new `NDEFReadingEvent`.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[NDEFReadingEvent.message](/en-US/docs/Web/API/NDEFReadingEvent/message)Read onlyExperimental

Returns an [NDEFMessage](/en-US/docs/Web/API/NDEFMessage) object containing the received message.

[NDEFReadingEvent.serialNumber](/en-US/docs/Web/API/NDEFReadingEvent/serialNumber)Read onlyExperimental

Returns the serial number of the device, which is used for anti-collision and identification, or an empty string if no serial number is available.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[Web NFC# dom-ndefreadingevent](https://w3c.github.io/web-nfc/#dom-ndefreadingevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NDEFReadingEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/ndefreadingevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFReadingEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fndefreadingevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNDEFReadingEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fndefreadingevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7265fc3effa7c25b9997135104370c057a65293%0A*+Document+last+modified%3A+2025-09-25T16%3A11%3A52.000Z%0A%0A%3C%2Fdetails%3E)
