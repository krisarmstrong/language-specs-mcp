# BeforeUnloadEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBeforeUnloadEvent&level=high)

The `BeforeUnloadEvent` interface represents the event object for the [beforeunload](/en-US/docs/Web/API/Window/beforeunload_event) event, which is fired when the current window, contained document, and associated resources are about to be unloaded.

See the [beforeunload](/en-US/docs/Web/API/Window/beforeunload_event) event reference for detailed guidance on using this event.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[returnValue](/en-US/docs/Web/API/BeforeUnloadEvent/returnValue)Deprecated

When set to a [truthy](/en-US/docs/Glossary/Truthy) value, triggers a browser-controlled confirmation dialog asking users to confirm if they want to leave the page when they try to close or reload it. This is a legacy feature, and best practice is to trigger the dialog by invoking `event.preventDefault()`, while also setting `returnValue` to support legacy cases.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[HTML# the-beforeunloadevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-beforeunloadevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [beforeunload](/en-US/docs/Web/API/Window/beforeunload_event) event

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/BeforeUnloadEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/beforeunloadevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBeforeUnloadEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fbeforeunloadevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FBeforeUnloadEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fbeforeunloadevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa7265fc3effa7c25b9997135104370c057a65293%0A*+Document+last+modified%3A+2025-09-25T16%3A11%3A52.000Z%0A%0A%3C%2Fdetails%3E)
