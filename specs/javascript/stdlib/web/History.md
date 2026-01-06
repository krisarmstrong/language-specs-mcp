# History

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHistory&level=high)

The `History` interface of the [History API](/en-US/docs/Web/API/History_API) allows manipulation of the browser session history, that is the pages visited in the tab or frame that the current page is loaded in.

There is only one instance of `history` (It is a singleton.) accessible via the global object [history](/en-US/docs/Web/API/Window/history).

Note: This interface is only available on the main thread ([Window](/en-US/docs/Web/API/Window)). It cannot be accessed in [Worker](/en-US/docs/Web/API/Worker) or [Worklet](/en-US/docs/Web/API/Worklet) contexts.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `History` interface doesn't inherit any property.

[length](/en-US/docs/Web/API/History/length)Read only

Returns an `Integer` representing the number of elements in the session history, including the currently loaded page. For example, for a page loaded in a new tab this property returns `1`.

[scrollRestoration](/en-US/docs/Web/API/History/scrollRestoration)

Allows web applications to explicitly set default scroll restoration behavior on history navigation. This property can be either `auto` or `manual`.

[state](/en-US/docs/Web/API/History/state)Read only

Returns an `any` value representing the state at the top of the history stack. This is a way to look at the state without having to wait for a [popstate](/en-US/docs/Web/API/Window/popstate_event) event.

## [Instance methods](#instance_methods)

The `History`interface doesn't inherit any methods.

[back()](/en-US/docs/Web/API/History/back)

This asynchronous method goes to the previous page in session history, the same action as when the user clicks the browser's Back button. Equivalent to `history.go(-1)`.

Calling this method to go back beyond the first page in the session history has no effect and doesn't raise an exception.

[forward()](/en-US/docs/Web/API/History/forward)

This asynchronous method goes to the next page in session history, the same action as when the user clicks the browser's Forward button; this is equivalent to `history.go(1)`.

Calling this method to go forward beyond the most recent page in the session history has no effect and doesn't raise an exception.

[go()](/en-US/docs/Web/API/History/go)

Asynchronously loads a page from the session history, identified by its relative location to the current page, for example `-1` for the previous page or `1` for the next page. If you specify an out-of-bounds value (for instance, specifying `-1` when there are no previously-visited pages in the session history), this method silently has no effect. Calling `go()` without parameters or a value of `0` reloads the current page.

[pushState()](/en-US/docs/Web/API/History/pushState)

Pushes the given data onto the session history stack with the specified title (and, if provided, URL). The data is treated as opaque by the DOM; you may specify any JavaScript object that can be serialized. Note that all browsers but Safari currently ignore the title parameter. For more information, see [Working with the History API](/en-US/docs/Web/API/History_API/Working_with_the_History_API).

[replaceState()](/en-US/docs/Web/API/History/replaceState)

Updates the most recent entry on the history stack to have the specified data, title, and, if provided, URL. The data is treated as opaque by the DOM; you may specify any JavaScript object that can be serialized. Note that all browsers but Safari currently ignore the title parameter. For more information, see [Working with the History API](/en-US/docs/Web/API/History_API/Working_with_the_History_API).

## [Specifications](#specifications)

Specification
[HTML# the-history-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-history-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [history](/en-US/docs/Web/API/Window/history) global object

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jun 23, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/History/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/history/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHistory&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhistory%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHistory%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhistory%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3e543cdfe8dddfb4774a64bf3decdcbab42a4111%0A*+Document+last+modified%3A+2025-06-23T16%3A41%3A39.000Z%0A%0A%3C%2Fdetails%3E)
