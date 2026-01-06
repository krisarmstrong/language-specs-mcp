# SharedWorkerGlobalScope

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedWorkerGlobalScope&level=not)

The `SharedWorkerGlobalScope` object (the [SharedWorker](/en-US/docs/Web/API/SharedWorker) global scope) is accessible through the [self](/en-US/docs/Web/API/Window/self) keyword. Some additional global functions, namespaces objects, and constructors, not typically associated with the worker global scope, but available on it, are listed in the [JavaScript Reference](/en-US/docs/Web/JavaScript/Reference). See the complete list of [functions available to workers](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits properties from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[SharedWorkerGlobalScope.name](/en-US/docs/Web/API/SharedWorkerGlobalScope/name)Read only

The name that the [SharedWorker](/en-US/docs/Web/API/SharedWorker) was (optionally) given when it was created using the [SharedWorker()](/en-US/docs/Web/API/SharedWorker/SharedWorker) constructor. This is mainly useful for debugging purposes.

## [Instance methods](#instance_methods)

This interface inherits methods from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[SharedWorkerGlobalScope.close()](/en-US/docs/Web/API/SharedWorkerGlobalScope/close)

Discards any tasks queued in the `SharedWorkerGlobalScope`'s event loop, effectively closing this particular scope.

## [Events](#events)

Listen to this event using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[connect](/en-US/docs/Web/API/SharedWorkerGlobalScope/connect_event)

Fired on shared workers when a new client connects.

## [Specifications](#specifications)

Specification
[HTML# shared-workers-and-the-sharedworkerglobalscope-interface](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworkerglobalscope-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [SharedWorker](/en-US/docs/Web/API/SharedWorker)
- [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope)
- [Using Web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [Functions available to workers](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 3, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/SharedWorkerGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/sharedworkerglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedWorkerGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsharedworkerglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSharedWorkerGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsharedworkerglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe76119da66eebf2d8ea5f572ab5dd8e1698ae414%0A*+Document+last+modified%3A+2023-12-03T08%3A07%3A48.000Z%0A%0A%3C%2Fdetails%3E)
