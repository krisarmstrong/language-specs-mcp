# ErrorEvent

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `ErrorEvent` interface represents events providing information related to errors in scripts or in files.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ErrorEvent()](/en-US/docs/Web/API/ErrorEvent/ErrorEvent)

Creates an `ErrorEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[ErrorEvent.message](/en-US/docs/Web/API/ErrorEvent/message)Read only

A string containing a human-readable error message describing the problem.

[ErrorEvent.filename](/en-US/docs/Web/API/ErrorEvent/filename)Read only

A string containing the name of the script file in which the error occurred.

[ErrorEvent.lineno](/en-US/docs/Web/API/ErrorEvent/lineno)Read only

An integer containing the line number of the script file on which the error occurred.

[ErrorEvent.colno](/en-US/docs/Web/API/ErrorEvent/colno)Read only

An integer containing the column number of the script file on which the error occurred.

[ErrorEvent.error](/en-US/docs/Web/API/ErrorEvent/error)Read only

A JavaScript value, such as an [Error](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) or [DOMException](/en-US/docs/Web/API/DOMException), representing the error associated with this event.

## [Instance methods](#instance_methods)

Inherits methods from its parent [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[HTML# errorevent](https://html.spec.whatwg.org/multipage/webappapis.html#errorevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), most likely objects to raise such an event.
- [Window](/en-US/docs/Web/API/Window): [error](/en-US/docs/Web/API/Window/error_event) event
- [Navigation](/en-US/docs/Web/API/Navigation): [navigateerror](/en-US/docs/Web/API/Navigation/navigateerror_event) event

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 15, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ErrorEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/errorevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FErrorEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ferrorevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FErrorEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ferrorevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc51a68c737afbd68787f4450f0c00da2dbdd5317%0A*+Document+last+modified%3A+2024-10-15T16%3A04%3A22.000Z%0A%0A%3C%2Fdetails%3E)
