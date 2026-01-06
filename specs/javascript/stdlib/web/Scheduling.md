# Scheduling

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `Scheduling` object provides methods and properties to control scheduling tasks within the current document.

Warning: The `Scheduling` interface has been superseded by the [Scheduler](/en-US/docs/Web/API/Scheduler) interface, the features of which are better designed for addressing scheduling tasks. See [Don't use isInputPending()](https://web.dev/articles/optimize-long-tasks#isinputpending) for more details.

## In this article

- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[isInputPending()](/en-US/docs/Web/API/Scheduling/isInputPending)Experimental

Returns a boolean that indicates whether there are pending input events in the event queue, meaning that the user is attempting to interact with the page.

## [Example](#example)

See the [Scheduling.isInputPending()](/en-US/docs/Web/API/Scheduling/isInputPending) page for a full example.

## [Specifications](#specifications)

Specification
[Early detection of input events# the-scheduling-interface](https://wicg.github.io/is-input-pending/#the-scheduling-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Scheduler](/en-US/docs/Web/API/Scheduler) interface
- [Prioritized Task Scheduling API](/en-US/docs/Web/API/Prioritized_Task_Scheduling_API)
- [Faster input events with Facebook's first browser API contribution](https://engineering.fb.com/2019/04/22/developer-tools/isinputpending-api/) on engineering.fb.com (2019)
- [Better JS scheduling with isInputPending()](https://developer.chrome.com/docs/capabilities/web-apis/isinputpending) on developer.chrome.com (2020)
- [Optimizing long tasks](https://web.dev/articles/optimize-long-tasks) on web.dev (2022)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Sep 27, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Scheduling/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/scheduling/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScheduling&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscheduling%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScheduling%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscheduling%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa966a8b4eade72a13de8a688c13f2d5056321f02%0A*+Document+last+modified%3A+2024-09-27T10%3A24%3A11.000Z%0A%0A%3C%2Fdetails%3E)
