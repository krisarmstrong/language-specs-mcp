# PresentationConnectionAvailableEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnectionAvailableEvent&level=not)

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `PresentationConnectionAvailableEvent` interface of the [Presentation API](/en-US/docs/Web/API/Presentation_API) is fired on a [PresentationRequest](/en-US/docs/Web/API/PresentationRequest) when a connection associated with the object is created.

A [controlling user agent](https://www.w3.org/TR/presentation-api/#dfn-controlling-user-agent)[fires](https://www.w3.org/TR/presentation-api/#dfn-firing-an-event) a [trusted event](https://www.w3.org/TR/presentation-api/#dfn-trusted-event) named [connectionavailable](https://www.w3.org/TR/presentation-api/#dfn-connectionavailable) on a [PresentationRequest](https://www.w3.org/TR/presentation-api/#idl-def-presentationrequest) when a connection associated with the object is created. It is fired at the `PresentationRequest` instance, using the [PresentationConnectionAvailableEvent](https://www.w3.org/TR/presentation-api/#idl-def-presentationconnectionavailableevent) interface, with the [connection](https://www.w3.org/TR/presentation-api/#idl-def-presentationconnectionavailableevent-connection) attribute set to the [PresentationConnection](https://www.w3.org/TR/presentation-api/#idl-def-presentationconnection) object that was created. The event is fired for each connection that is created for the [controller](https://www.w3.org/TR/presentation-api/#dfn-controller), either by the [controller](https://www.w3.org/TR/presentation-api/#dfn-controller) calling `start()` or `reconnect()`, or by the [controlling user agent](https://www.w3.org/TR/presentation-api/#dfn-controlling-user-agent) creating a connection on the controller's behalf via [defaultRequest](https://www.w3.org/TR/presentation-api/#dom-presentation-defaultrequest).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[PresentationConnectionAvailableEvent()](/en-US/docs/Web/API/PresentationConnectionAvailableEvent/PresentationConnectionAvailableEvent)Experimental

Creates a new PresentationConnectionAvailableEvent.

## [Instance properties](#instance_properties)

[PresentationConnectionAvailableEvent.connection](/en-US/docs/Web/API/PresentationConnectionAvailableEvent/connection)Read onlyExperimental

Returns a references to the [PresentationConnection](/en-US/docs/Web/API/PresentationConnection) object that fired the event.

## [Specifications](#specifications)

Specification
[Presentation API# interface-presentationconnectionavailableevent](https://w3c.github.io/presentation-api/#interface-presentationconnectionavailableevent)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/PresentationConnectionAvailableEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/presentationconnectionavailableevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnectionAvailableEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpresentationconnectionavailableevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPresentationConnectionAvailableEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpresentationconnectionavailableevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F95dff5ec1195f072b8e48a2273294933670b1e99%0A*+Document+last+modified%3A+2023-02-19T10%3A18%3A31.000Z%0A%0A%3C%2Fdetails%3E)
