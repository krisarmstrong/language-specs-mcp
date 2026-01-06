# DedicatedWorkerGlobalScope

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDedicatedWorkerGlobalScope&level=high)

Note: This feature is only available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `DedicatedWorkerGlobalScope` object (the [Worker](/en-US/docs/Web/API/Worker) global scope) is accessible through the [self](/en-US/docs/Web/API/WorkerGlobalScope/self) keyword. Some additional global functions, namespaces objects, and constructors, not typically associated with the worker global scope, but available on it, are listed in the [JavaScript Reference](/en-US/docs/Web/JavaScript/Reference). See also: [Functions available to workers](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface inherits properties from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[DedicatedWorkerGlobalScope.name](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/name)Read only

The name that the [Worker](/en-US/docs/Web/API/Worker) was (optionally) given when it was created using the [Worker()](/en-US/docs/Web/API/Worker/Worker) constructor. This is mainly useful for debugging purposes.

## [Instance methods](#instance_methods)

This interface inherits methods from the [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope) interface, and its parent [EventTarget](/en-US/docs/Web/API/EventTarget).

[DedicatedWorkerGlobalScope.close()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/close)

Discards any tasks queued in the `WorkerGlobalScope`'s event loop, effectively closing this particular scope.

[DedicatedWorkerGlobalScope.postMessage()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage)

Sends a message — which can consist of `any` JavaScript object — to the parent document that first spawned the worker.

[DedicatedWorkerGlobalScope.cancelAnimationFrame()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/cancelAnimationFrame)

Cancels an animation frame request previously scheduled through a call to [requestAnimationFrame()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/requestAnimationFrame).

[DedicatedWorkerGlobalScope.requestAnimationFrame()](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/requestAnimationFrame)

Perform an animation frame request and call a user-supplied callback function before the next repaint.

## [Events](#events)

Listen to this event using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface.

[message](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/message_event)

Fired when the worker receives a message from its parent.

[messageerror](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/messageerror_event)

Fired when a worker receives a message that can't be deserialized.

[rtctransform](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/rtctransform_event)

Fired when an encoded video or audio frame has been queued for processing by a [WebRTC Encoded Transform](/en-US/docs/Web/API/WebRTC_API/Using_Encoded_Transforms).

## [Specifications](#specifications)

Specification
[HTML# dedicated-workers-and-the-dedicatedworkerglobalscope-interface](https://html.spec.whatwg.org/multipage/workers.html#dedicated-workers-and-the-dedicatedworkerglobalscope-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Worker](/en-US/docs/Web/API/Worker)
- [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
- [Functions available to workers](/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 22, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/DedicatedWorkerGlobalScope/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/dedicatedworkerglobalscope/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDedicatedWorkerGlobalScope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fdedicatedworkerglobalscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FDedicatedWorkerGlobalScope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fdedicatedworkerglobalscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe6457c34ac16790d4e62bc9ba21e899ac560089c%0A*+Document+last+modified%3A+2024-04-22T08%3A48%3A14.000Z%0A%0A%3C%2Fdetails%3E)
