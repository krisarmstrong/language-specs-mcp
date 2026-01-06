# PresentationConnection

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnection&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PresentationConnection` interface of the [Presentation API](/en-US/docs/Web/API/Presentation_API) provides methods and properties for managing a single presentation. Each [presentation connection](https://www.w3.org/TR/presentation-api/#dfn-presentation-connection) is represented by a `PresentationConnection` object. Both the [controlling user agent](https://www.w3.org/TR/presentation-api/#dfn-controlling-user-agent) and [receiving user agent](https://www.w3.org/TR/presentation-api/#dfn-receiving-user-agent)MUST implement `PresentationConnection`.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[PresentationConnection.binaryType](/en-US/docs/Web/API/PresentationConnection/binaryType)Experimental

Returns either blob or arrayBuffer. When a `PresentationConnection` object is created, its [binaryType](https://www.w3.org/TR/presentation-api/#idl-def-presentationconnection-binarytype) IDL attribute MUST be set to the string ["arraybuffer"](https://www.w3.org/TR/presentation-api/#dom-binarytype-arraybuffer).

[PresentationConnection.id](/en-US/docs/Web/API/PresentationConnection/id)Read onlyExperimental

Provides the presentation connection identifier.

[PresentationConnection.state](/en-US/docs/Web/API/PresentationConnection/state)Read onlyExperimental

Returns the [presentation connection](https://www.w3.org/TR/presentation-api/#dfn-presentation-connection)'s current state.

[PresentationConnection.url](/en-US/docs/Web/API/PresentationConnection/url)Read onlyExperimental

Returns the URL used to create or reconnect to the presentation.

## [Instance methods](#instance_methods)

[PresentationConnection.close()](/en-US/docs/Web/API/PresentationConnection/close)Experimental

Closes the current connection and sends a [PresentationConnectionCloseEvent](/en-US/docs/Web/API/PresentationConnectionCloseEvent) to [close](/en-US/docs/Web/API/PresentationConnection/close) event.

[PresentationConnection.send()](/en-US/docs/Web/API/PresentationConnection/send)Experimental

Sends either binary or text data between a controlling browsing context and a presenting browsing context.

[PresentationConnection.terminate()](/en-US/docs/Web/API/PresentationConnection/terminate)Experimental

Terminates the current connection and fires `terminate` event.

## [Events](#events)

`close`Experimental

Fired when there is a call to [PresentationConnection.close()](/en-US/docs/Web/API/PresentationConnection/close).

`connect`Experimental

Fired when a presentation connection is established.

`message`Experimental

Fired when there is a call to [PresentationConnection.send()](/en-US/docs/Web/API/PresentationConnection/send).

`terminate`Experimental

Fired when there is a call to [PresentationConnection.terminate()](/en-US/docs/Web/API/PresentationConnection/terminate).

## [Specifications](#specifications)

Specification
[Presentation API# interface-presentationconnection](https://w3c.github.io/presentation-api/#interface-presentationconnection)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PresentationConnection/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/presentationconnection/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpresentationconnection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpresentationconnection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5bd9fe2b25c6eee2a14d0406ce7116998fa48c13%0A*+Document+last+modified%3A+2024-09-25T13%3A57%3A00.000Z%0A%0A%3C%2Fdetails%3E)
