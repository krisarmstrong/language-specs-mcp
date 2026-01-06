# Client

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2018⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClient&level=high)

Note: This feature is only available in [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

The `Client` interface represents an executable context such as a [Worker](/en-US/docs/Web/API/Worker), or a [SharedWorker](/en-US/docs/Web/API/SharedWorker). [Window](/en-US/docs/Web/API/Window) clients are represented by the more-specific [WindowClient](/en-US/docs/Web/API/WindowClient). You can get `Client`/`WindowClient` objects from methods such as [Clients.matchAll()](/en-US/docs/Web/API/Clients/matchAll) and [Clients.get()](/en-US/docs/Web/API/Clients/get).

## In this article

- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[Client.postMessage()](/en-US/docs/Web/API/Client/postMessage)

Sends a message to the client.

## [Instance properties](#instance_properties)

[Client.frameType](/en-US/docs/Web/API/Client/frameType)Read only

The client's frame type as a string. It can be `"auxiliary"`, `"top-level"`, `"nested"`, or `"none"`.

[Client.id](/en-US/docs/Web/API/Client/id)Read only

The universally unique identifier of the client as a string.

[Client.type](/en-US/docs/Web/API/Client/type)Read only

The client's type as a string. It can be `"window"`, `"worker"`, or `"sharedworker"`.

[Client.url](/en-US/docs/Web/API/Client/url)Read only

The URL of the client as a string.

## [Specifications](#specifications)

Specification
[Service Workers Nightly# client-interface](https://w3c.github.io/ServiceWorker/#client-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using Service Workers](/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 13, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Client/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/client/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClient&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fclient%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FClient%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fclient%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ef36a6d6f380e79c88bc3a80033e1d3c4629994%0A*+Document+last+modified%3A+2024-05-13T06%3A21%3A16.000Z%0A%0A%3C%2Fdetails%3E)
