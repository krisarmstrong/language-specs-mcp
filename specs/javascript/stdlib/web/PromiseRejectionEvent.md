# PromiseRejectionEvent

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `PromiseRejectionEvent` interface represents events which are sent to the global script context when JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)s are rejected. These events are particularly useful for telemetry and debugging purposes.

For details, see [Promise rejection events](/en-US/docs/Web/JavaScript/Guide/Using_promises#promise_rejection_events).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PromiseRejectionEvent()](/en-US/docs/Web/API/PromiseRejectionEvent/PromiseRejectionEvent)

Creates a `PromiseRejectionEvent` event, given the type of event ([unhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event) or [rejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)) and other details.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[PromiseRejectionEvent.promise](/en-US/docs/Web/API/PromiseRejectionEvent/promise)Read only

The JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that was rejected.

[PromiseRejectionEvent.reason](/en-US/docs/Web/API/PromiseRejectionEvent/reason)Read only

A value or [Object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) indicating why the promise was rejected, as passed to [Promise.reject()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject).

## [Instance methods](#instance_methods)

This interface has no unique methods; inherits methods from its parent [Event](/en-US/docs/Web/API/Event).

## [Events](#events)

[rejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)

Fired when a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected, and after the rejection is handled by the promise's rejection handling code.

[unhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event)

Fired when a JavaScript [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is rejected but there is no rejection handler to deal with the rejection.

## [Examples](#examples)

This simple example catches unhandled promise rejections and logs them for debugging purposes.

js

```
window.onunhandledrejection = (e) => {
  console.log(e.reason);
};
```

## [Specifications](#specifications)

Specification
[HTML# promiserejectionevent](https://html.spec.whatwg.org/multipage/webappapis.html#promiserejectionevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using promises](/en-US/docs/Web/JavaScript/Guide/Using_promises)
- [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [rejectionhandled](/en-US/docs/Web/API/Window/rejectionhandled_event)
- [unhandledrejection](/en-US/docs/Web/API/Window/unhandledrejection_event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PromiseRejectionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/promiserejectionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPromiseRejectionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpromiserejectionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPromiseRejectionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpromiserejectionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb3ff5a0fd5080c2ce109d0eb17831b6ef57a2d%0A*+Document+last+modified%3A+2024-10-08T19%3A32%3A27.000Z%0A%0A%3C%2Fdetails%3E)
