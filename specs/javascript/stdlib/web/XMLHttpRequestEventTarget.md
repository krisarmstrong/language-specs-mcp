# XMLHttpRequestEventTarget

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequestEventTarget&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API), except for [Service Workers](/en-US/docs/Web/API/Service_Worker_API).

`XMLHttpRequestEventTarget` is the interface that describes the event handlers shared on [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and [XMLHttpRequestUpload](/en-US/docs/Web/API/XMLHttpRequestUpload).

You don't use `XMLHttpRequestEventTarget` directly; instead you interact with the sub classes.

## In this article

- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Events](#events)

The following events are made available to [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and [XMLHttpRequestUpload](/en-US/docs/Web/API/XMLHttpRequestUpload):

[abort](/en-US/docs/Web/API/XMLHttpRequestEventTarget/abort_event)

Fired when a request has been aborted, for example because the program called [XMLHttpRequest.abort()](/en-US/docs/Web/API/XMLHttpRequest/abort). Also available via the `onabort` event handler property.

[error](/en-US/docs/Web/API/XMLHttpRequestEventTarget/error_event)

Fired when the request encountered an error. Also available via the `onerror` event handler property.

[load](/en-US/docs/Web/API/XMLHttpRequestEventTarget/load_event)

Fired when a request transaction completes successfully. Also available via the `onload` event handler property.

[loadend](/en-US/docs/Web/API/XMLHttpRequestEventTarget/loadend_event)

Fired when a request has completed, whether successfully (after [load](/en-US/docs/Web/API/XMLHttpRequestEventTarget/load_event)) or unsuccessfully (after [abort](/en-US/docs/Web/API/XMLHttpRequestEventTarget/abort_event) or [error](/en-US/docs/Web/API/XMLHttpRequestEventTarget/error_event)). Also available via the `onloadend` event handler property.

[loadstart](/en-US/docs/Web/API/XMLHttpRequestEventTarget/loadstart_event)

Fired when a request has started to load data. Also available via the `onloadstart` event handler property.

[progress](/en-US/docs/Web/API/XMLHttpRequestEventTarget/progress_event)

Fired periodically when a request receives more data. Also available via the `onprogress` event handler property.

[timeout](/en-US/docs/Web/API/XMLHttpRequestEventTarget/timeout_event)

Fired when progress is terminated due to preset time expiring. Also available via the `ontimeout` event handler property.

## [Specifications](#specifications)

Specification
[XMLHttpRequest# xmlhttprequesteventtarget](https://xhr.spec.whatwg.org/#xmlhttprequesteventtarget)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest)
- [XMLHttpRequestUpload](/en-US/docs/Web/API/XMLHttpRequestUpload)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 26, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XMLHttpRequestEventTarget/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xmlhttprequesteventtarget/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequestEventTarget&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxmlhttprequesteventtarget%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequestEventTarget%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxmlhttprequesteventtarget%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0cc63ce1d7f43eb98746a908a9aba68ef6a36f7b%0A*+Document+last+modified%3A+2025-08-26T12%3A44%3A08.000Z%0A%0A%3C%2Fdetails%3E)
