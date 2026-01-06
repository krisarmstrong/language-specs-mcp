# AbortController

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2019⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAbortController&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `AbortController` interface represents a controller object that allows you to abort one or more Web requests as and when desired.

You can create a new `AbortController` object using the [AbortController()](/en-US/docs/Web/API/AbortController/AbortController) constructor. Communicating with an asynchronous operation is done using an [AbortSignal](/en-US/docs/Web/API/AbortSignal) object.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AbortController()](/en-US/docs/Web/API/AbortController/AbortController)

Creates a new `AbortController` object instance.

## [Instance properties](#instance_properties)

[AbortController.signal](/en-US/docs/Web/API/AbortController/signal)Read only

Returns an [AbortSignal](/en-US/docs/Web/API/AbortSignal) object instance, which can be used to communicate with, or to abort, an asynchronous operation.

## [Instance methods](#instance_methods)

[AbortController.abort()](/en-US/docs/Web/API/AbortController/abort)

Aborts an asynchronous operation before it has completed. This is able to abort [fetch requests](/en-US/docs/Web/API/Window/fetch), consumption of any response bodies, and streams.

## [Examples](#examples)

See the [AbortSignal page](/en-US/docs/Web/API/AbortSignal#examples) for usage examples.

You can find a [full working example on GitHub](https://github.com/mdn/dom-examples/tree/main/abort-api); you can also see it [running live](https://mdn.github.io/dom-examples/abort-api/).

## [Specifications](#specifications)

Specification
[DOM# interface-abortcontroller](https://dom.spec.whatwg.org/#interface-abortcontroller)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Fetch API](/en-US/docs/Web/API/Fetch_API)
- [Abortable Fetch](https://developer.chrome.com/blog/abortable-fetch/) by Jake Archibald

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 17, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AbortController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/abortcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAbortController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fabortcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAbortController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fabortcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fd602696976d79d8690f9c86a2a1c1f2b9b9eb%0A*+Document+last+modified%3A+2025-09-17T01%3A18%3A50.000Z%0A%0A%3C%2Fdetails%3E)
