# CloseEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCloseEvent&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

A `CloseEvent` is sent to clients using [WebSockets](/en-US/docs/Glossary/WebSockets) when the connection is closed. This is delivered to the listener indicated by the `WebSocket` object's `onclose` attribute.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[CloseEvent()](/en-US/docs/Web/API/CloseEvent/CloseEvent)

Creates a new `CloseEvent`.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[CloseEvent.code](/en-US/docs/Web/API/CloseEvent/code)Read only

Returns an `unsigned short` containing the close code.

[CloseEvent.reason](/en-US/docs/Web/API/CloseEvent/reason)Read only

Returns a string indicating the reason the server closed the connection. This is specific to the particular server and sub-protocol.

[CloseEvent.wasClean](/en-US/docs/Web/API/CloseEvent/wasClean)Read only

Returns a boolean value that Indicates whether or not the connection was cleanly closed.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[WebSockets# the-closeevent-interface](https://websockets.spec.whatwg.org/#the-closeevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebSocket](/en-US/docs/Web/API/WebSocket)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/CloseEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/closeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCloseEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcloseevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCloseEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcloseevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffb311d7305937497570966f015d8cc0eb1a0c29c%0A*+Document+last+modified%3A+2024-09-25T06%3A05%3A22.000Z%0A%0A%3C%2Fdetails%3E)
