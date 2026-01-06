# PopStateEvent

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPopStateEvent&level=high)

`PopStateEvent` is an interface for the [popstate](/en-US/docs/Web/API/Window/popstate_event) event.

A `popstate` event is dispatched to the window every time the active history entry changes between two history entries for the same document. If the history entry being activated was created by a call to `history.pushState()` or was affected by a call to `history.replaceState()`, the `popstate` event's `state` property contains a copy of the history entry's state object.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PopStateEvent()](/en-US/docs/Web/API/PopStateEvent/PopStateEvent)

Creates a new `PopStateEvent` object.

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent, [Event](/en-US/docs/Web/API/Event).

[PopStateEvent.state](/en-US/docs/Web/API/PopStateEvent/state)Read only

Returns a copy of the information that was provided to `pushState()` or `replaceState()`.

[hasUAVisualTransition](/en-US/docs/Web/API/PopStateEvent/hasUAVisualTransition)Read only

Returns `true` if the user agent performed a visual transition for this navigation before dispatching this event, or `false` otherwise.

## [Instance methods](#instance_methods)

This interface has no methods of its own, but inherits the methods of its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[HTML# the-popstateevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-popstateevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [popstate](/en-US/docs/Web/API/Window/popstate_event) event
- [hashchange](/en-US/docs/Web/API/Window/hashchange_event) event

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PopStateEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/popstateevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPopStateEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpopstateevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPopStateEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpopstateevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F082221e2a29b7bea7a3029cd71442c8f294a8422%0A*+Document+last+modified%3A+2025-01-08T07%3A46%3A40.000Z%0A%0A%3C%2Fdetails%3E)
