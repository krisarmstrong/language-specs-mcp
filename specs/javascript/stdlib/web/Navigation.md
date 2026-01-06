# Navigation

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigation&level=not)

The `Navigation` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) allows control over all navigation actions for the current `window` in one central place, including initiating navigations programmatically, examining navigation history entries, and managing navigations as they happen.

It is accessed via the [Window.navigation](/en-US/docs/Web/API/Window/navigation) property.

The Navigation API only exposes history entries created in the current browsing context that have the same origin as the current page (e.g., not navigations inside embedded [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe)s, or cross-origin navigations), providing an accurate list of all previous history entries just for your app. This makes traversing the history a much less fragile proposition than with the older [History API](/en-US/docs/Web/API/History_API).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Inherits properties from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[activation](/en-US/docs/Web/API/Navigation/activation)Read only

Returns a [NavigationActivation](/en-US/docs/Web/API/NavigationActivation) object containing information about the most recent cross-document navigation, which "activated" this Document.

[canGoBack](/en-US/docs/Web/API/Navigation/canGoBack)Read only

Returns `true` if it is possible to navigate backwards in the navigation history (i.e., the [currentEntry](/en-US/docs/Web/API/Navigation/currentEntry) is not the first one in the history entry list), and `false` if it is not.

[canGoForward](/en-US/docs/Web/API/Navigation/canGoForward)Read only

Returns `true` if it is possible to navigate forwards in the navigation history (i.e., the [currentEntry](/en-US/docs/Web/API/Navigation/currentEntry) is not the last one in the history entry list), and `false` if it is not.

[currentEntry](/en-US/docs/Web/API/Navigation/currentEntry)Read only

Returns a [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) object representing the location the user is currently navigated to right now.

[transition](/en-US/docs/Web/API/Navigation/transition)Read only

Returns a [NavigationTransition](/en-US/docs/Web/API/NavigationTransition) object representing the status of an in-progress navigation, which can be used to track it. Returns `null` if no navigation is currently in progress.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[back()](/en-US/docs/Web/API/Navigation/back)

Navigates backwards by one entry in the navigation history.

[entries()](/en-US/docs/Web/API/Navigation/entries)

Returns an array of [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) objects representing all existing history entries.

[forward()](/en-US/docs/Web/API/Navigation/forward)

Navigates forwards by one entry in the navigation history.

[navigate()](/en-US/docs/Web/API/Navigation/navigate)

Navigates to a specific URL, updating any provided state in the history entries list.

[reload()](/en-US/docs/Web/API/Navigation/reload)

Reloads the current URL, updating any provided state in the history entries list.

[traverseTo()](/en-US/docs/Web/API/Navigation/traverseTo)

Navigates to a specific [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) identified by [key](/en-US/docs/Web/API/NavigationHistoryEntry/key).

[updateCurrentEntry()](/en-US/docs/Web/API/Navigation/updateCurrentEntry)

Updates the state of the [currentEntry](/en-US/docs/Web/API/Navigation/currentEntry); used in cases where the state change will be independent from a navigation or reload.

## [Events](#events)

Inherits events from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[currententrychange](/en-US/docs/Web/API/Navigation/currententrychange_event)Experimental

Fired when the [Navigation.currentEntry](/en-US/docs/Web/API/Navigation/currentEntry) has changed.

[navigate](/en-US/docs/Web/API/Navigation/navigate_event)Experimental

Fired when [any type of navigation](https://github.com/WICG/navigation-api#appendix-types-of-navigations) is initiated, allowing you to intercept as required.

[navigateerror](/en-US/docs/Web/API/Navigation/navigateerror_event)Experimental

Fired when a navigation fails.

[navigatesuccess](/en-US/docs/Web/API/Navigation/navigatesuccess_event)Experimental

Fired when a successful navigation has finished.

## [Examples](#examples)

### [Moving forwards and backwards in the history](#moving_forwards_and_backwards_in_the_history)

js

```
async function backHandler() {
  if (navigation.canGoBack) {
    await navigation.back().finished;
    // Handle any required clean-up after
    // navigation has finished
  } else {
    displayBanner("You are on the first page");
  }
}

async function forwardHandler() {
  if (navigation.canGoForward) {
    await navigation.forward().finished;
    // Handle any required clean-up after
    // navigation has finished
  } else {
    displayBanner("You are on the last page");
  }
}
```

### [Traversing to a specific history entry](#traversing_to_a_specific_history_entry)

js

```
// On JS startup, get the key of the first loaded page
// so the user can always go back there.
const { key } = navigation.currentEntry;
backToHomeButton.onclick = () => navigation.traverseTo(key);

// Navigate away, but the button will always work.
await navigation.navigate("/another_url").finished;
```

### [Navigating and updating state](#navigating_and_updating_state)

js

```
navigation.navigate(url, { state: newState });
```

Or

js

```
navigation.reload({ state: newState });
```

Or if the state is independent from a navigation or reload:

js

```
navigation.updateCurrentEntry({ state: newState });
```

## [Specifications](#specifications)

Specification
[HTML# navigation-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)
- [Navigation API explainer](https://github.com/WICG/navigation-api/blob/main/README.md)
- [Navigation API live demo](https://mdn.github.io/dom-examples/navigation-api/) ([view demo source](https://github.com/mdn/dom-examples/tree/main/navigation-api))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Navigation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
