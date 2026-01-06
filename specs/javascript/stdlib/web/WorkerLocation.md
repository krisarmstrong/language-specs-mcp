# WorkerLocation

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerLocation&level=high)

Note: This feature is only available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WorkerLocation` interface defines the absolute location of the script executed by the [Worker](/en-US/docs/Web/API/Worker). Such an object is initialized for each worker and is available via the [WorkerGlobalScope.location](/en-US/docs/Web/API/WorkerGlobalScope/location) property obtained by calling `self.location`.

This interface is only visible from inside a JavaScript script executed in the context of a Web worker.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[WorkerLocation.href](/en-US/docs/Web/API/WorkerLocation/href)Read only

Returns a string containing the serialized [URL](/en-US/docs/Web/API/URL) for the worker's location.

[WorkerLocation.protocol](/en-US/docs/Web/API/WorkerLocation/protocol)Read only

Returns the [protocol](/en-US/docs/Web/API/URL/protocol) part of the worker's location.

[WorkerLocation.host](/en-US/docs/Web/API/WorkerLocation/host)Read only

Returns the [host](/en-US/docs/Web/API/URL/host) part of the worker's location.

[WorkerLocation.hostname](/en-US/docs/Web/API/WorkerLocation/hostname)Read only

Returns the [hostname](/en-US/docs/Web/API/URL/hostname) part of the worker's location.

[WorkerLocation.origin](/en-US/docs/Web/API/WorkerLocation/origin)Read only

Returns the worker's [origin](/en-US/docs/Web/API/URL/origin).

[WorkerLocation.port](/en-US/docs/Web/API/WorkerLocation/port)Read only

Returns the [port](/en-US/docs/Web/API/URL/port) part of the worker's location.

[WorkerLocation.pathname](/en-US/docs/Web/API/WorkerLocation/pathname)Read only

Returns the [pathname](/en-US/docs/Web/API/URL/pathname) part of the worker's location.

[WorkerLocation.search](/en-US/docs/Web/API/WorkerLocation/search)Read only

Returns the [search](/en-US/docs/Web/API/URL/search) part of the worker's location.

[WorkerLocation.hash](/en-US/docs/Web/API/WorkerLocation/hash)Read only

Returns the [hash](/en-US/docs/Web/API/URL/hash) part of the worker's location.

## [Instance methods](#instance_methods)

[WorkerLocation.toString()](/en-US/docs/Web/API/WorkerLocation/toString)

Returns a string containing the serialized [URL](/en-US/docs/Web/API/URL) for the worker's location. It is a synonym for [WorkerLocation.href](/en-US/docs/Web/API/WorkerLocation/href).

## [Specifications](#specifications)

Specification
[HTML# worker-locations](https://html.spec.whatwg.org/multipage/workers.html#worker-locations)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Other Worker-related interfaces: [Worker](/en-US/docs/Web/API/Worker), [WorkerNavigator](/en-US/docs/Web/API/WorkerNavigator), and [WorkerGlobalScope](/en-US/docs/Web/API/WorkerGlobalScope)
- [Using web workers](/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 29, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/WorkerLocation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/workerlocation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerLocation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fworkerlocation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorkerLocation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fworkerlocation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe8fe043f7d2ad7cd9804d1bf96e0310949f1dac7%0A*+Document+last+modified%3A+2024-08-29T00%3A59%3A00.000Z%0A%0A%3C%2Fdetails%3E)
