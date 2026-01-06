# PresentationConnectionCloseEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnectionCloseEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PresentationConnectionCloseEvent` interface of the [Presentation API](/en-US/docs/Web/API/Presentation_API) is fired on a [PresentationConnection](/en-US/docs/Web/API/PresentationConnection) when it is closed.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

`PresentationConnectionCloseEvent()`Experimental

Creates a new PresentationConnectionCloseEvent.

## [Instance properties](#instance_properties)

`PresentationConnectionCloseEvent.message`Read onlyExperimental

A human-readable message that provides more information about why the connection was closed.

`PresentationConnectionCloseEvent.reason`Read onlyExperimental

Indicates why the connection was closed. This property takes one of the following values: `error`, `closed`, or `wentaway`.

## [Specifications](#specifications)

Specification
[Presentation API# interface-presentationconnectioncloseevent](https://w3c.github.io/presentation-api/#interface-presentationconnectioncloseevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/PresentationConnectionCloseEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/presentationconnectioncloseevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnectionCloseEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpresentationconnectioncloseevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnectionCloseEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpresentationconnectioncloseevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F95dff5ec1195f072b8e48a2273294933670b1e99%0A*+Document+last+modified%3A+2023-02-19T10%3A18%3A31.000Z%0A%0A%3C%2Fdetails%3E)
