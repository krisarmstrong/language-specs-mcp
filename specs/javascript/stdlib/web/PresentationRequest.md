# PresentationRequest

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationRequest&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

A `PresentationRequest` object is used to initiate or reconnect to a presentation made by a [controlling browsing context](https://www.w3.org/TR/presentation-api/#dfn-controlling-browsing-context). The `PresentationRequest` object MUST be implemented in a [controlling browsing context](https://www.w3.org/TR/presentation-api/#dfn-controlling-browsing-context) provided by a [controlling user agent](https://www.w3.org/TR/presentation-api/#dfn-controlling-user-agent).

When a `PresentationRequest` is constructed, the given `urls`MUST be used as the list of presentation request URLs which are each a possible [presentation URL](https://www.w3.org/TR/presentation-api/#dfn-presentation-url) for the `PresentationRequest` instance.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[PresentationRequest()](/en-US/docs/Web/API/PresentationRequest/PresentationRequest)Experimental

Creates a `PresentationRequest`.

## [Instance properties](#instance_properties)

None

## [Instance methods](#instance_methods)

[PresentationRequest.start()](/en-US/docs/Web/API/PresentationRequest/start)Experimental

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves with a [PresentationConnection](/en-US/docs/Web/API/PresentationConnection) after the user agent prompts the user to select a display and grant permission to use that display.

[PresentationRequest.reconnect()](/en-US/docs/Web/API/PresentationRequest/reconnect)Experimental

When the `reconnect(presentationId)` method is called on a `PresentationRequest`presentationRequest, the [user agent](https://www.w3.org/TR/presentation-api/#dfn-user-agents)MUST run the following steps to reconnect to a presentation.

[PresentationRequest.getAvailability()](/en-US/docs/Web/API/PresentationRequest/getAvailability)Experimental

When the `getAvailability()` method is called, the user agent MUST run the steps as the link.

## [Specifications](#specifications)

Specification
[Presentation API# interface-presentationrequest](https://w3c.github.io/presentation-api/#interface-presentationrequest)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 4, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/PresentationRequest/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/presentationrequest/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationRequest&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpresentationrequest%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationRequest%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpresentationrequest%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56c76424a5edb45f6716ac4ee48861dac8e7ae38%0A*+Document+last+modified%3A+2023-08-04T07%3A12%3A32.000Z%0A%0A%3C%2Fdetails%3E)
