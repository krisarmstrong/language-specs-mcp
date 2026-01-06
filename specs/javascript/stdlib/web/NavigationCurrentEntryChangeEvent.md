# NavigationCurrentEntryChangeEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationCurrentEntryChangeEvent&level=not)

The `NavigationCurrentEntryChangeEvent` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) is the event object for the [currententrychange](/en-US/docs/Web/API/Navigation/currententrychange_event) event, which fires when the [Navigation.currentEntry](/en-US/docs/Web/API/Navigation/currentEntry) has changed.

This event will fire for same-document navigations (e.g., [back()](/en-US/docs/Web/API/Navigation/back) or [traverseTo()](/en-US/docs/Web/API/Navigation/traverseTo)), replacements (i.e., a [navigate()](/en-US/docs/Web/API/Navigation/navigate) call with `history` set to `replace`), or other calls that change the entry's state (e.g., [updateCurrentEntry()](/en-US/docs/Web/API/Navigation/updateCurrentEntry), or the [History API](/en-US/docs/Web/API/History_API)'s [History.replaceState()](/en-US/docs/Web/API/History/replaceState)).

This event fires after the navigation is committed, meaning that the visible URL has changed and the [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) update has occurred. It is useful for migrating from usage of older API features like the [hashchange](/en-US/docs/Web/API/Window/hashchange_event) or [popstate](/en-US/docs/Web/API/Window/popstate_event) events.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[NavigationCurrentEntryChangeEvent()](/en-US/docs/Web/API/NavigationCurrentEntryChangeEvent/NavigationCurrentEntryChangeEvent)

Creates a new `NavigationCurrentEntryChangeEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[from](/en-US/docs/Web/API/NavigationCurrentEntryChangeEvent/from)Read only

Returns the [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) that was navigated from.

[navigationType](/en-US/docs/Web/API/NavigationCurrentEntryChangeEvent/navigationType)Read only

Returns the type of the navigation that resulted in the change.

## [Examples](#examples)

Navigation data reporting:

js

```
navigation.addEventListener("currententrychange", () => {
  const data = navigation.currentEntry.getState();
  submitAnalyticsData(data.analytics);
});
```

Setting up a per-entry event:

js

```
navigation.addEventListener("currententrychange", () => {
  navigation.currentEntry.addEventListener("dispose", genericDisposeHandler);
});
```

## [Specifications](#specifications)

Specification
[HTML# the-navigationcurrententrychangeevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-navigationcurrententrychangeevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)
- [Navigation API explainer](https://github.com/WICG/navigation-api/blob/main/README.md)
- [Navigation API live demo](https://mdn.github.io/dom-examples/navigation-api/) ([view demo source](https://github.com/mdn/dom-examples/tree/main/navigation-api))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigationCurrentEntryChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigationcurrententrychangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationCurrentEntryChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigationcurrententrychangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationCurrentEntryChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigationcurrententrychangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
