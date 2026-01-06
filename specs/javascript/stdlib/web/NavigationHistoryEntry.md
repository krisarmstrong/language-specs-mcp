# NavigationHistoryEntry

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationHistoryEntry&level=not)

The `NavigationHistoryEntry` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) represents a single navigation history entry.

These objects are commonly accessed via the [Navigation.currentEntry](/en-US/docs/Web/API/Navigation/currentEntry) property and [Navigation.entries()](/en-US/docs/Web/API/Navigation/entries) method.

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

[id](/en-US/docs/Web/API/NavigationHistoryEntry/id)Read only

Returns the `id` of the history entry. This is a unique, UA-generated value that always represents a specific history entry, useful to correlate it with an external resource such as a storage cache.

[index](/en-US/docs/Web/API/NavigationHistoryEntry/index)Read only

Returns the index of the history entry in the history entries list (that is, the list returned by [Navigation.entries()](/en-US/docs/Web/API/Navigation/entries)), or `-1` if the entry does not appear in the list.

[key](/en-US/docs/Web/API/NavigationHistoryEntry/key)Read only

Returns the `key` of the history entry. This is a unique, UA-generated value that represents the history entry's slot in the entries list rather than the entry itself. It is used to navigate that particular slot via [Navigation.traverseTo()](/en-US/docs/Web/API/Navigation/traverseTo). The `key` will be reused by other entries that replace the entry in the list (that is, if the [NavigateEvent.navigationType](/en-US/docs/Web/API/NavigateEvent/navigationType) is `replace`).

[sameDocument](/en-US/docs/Web/API/NavigationHistoryEntry/sameDocument)Read only

Returns `true` if this history entry is for the same `document` as the current [Document](/en-US/docs/Web/API/Document) value, or `false` otherwise.

[url](/en-US/docs/Web/API/NavigationHistoryEntry/url)Read only

Returns the absolute URL of this history entry. If the entry corresponds to a different document than the current one (like `sameDocument` property is `false`), and that document was fetched with a [Referrer-Policy](/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy) header set to `no-referrer` or `origin`, the property returns `null`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [EventTarget](/en-US/docs/Web/API/EventTarget).

[getState()](/en-US/docs/Web/API/NavigationHistoryEntry/getState)

Returns a clone of the available state associated with this history entry.

## [Events](#events)

[dispose](/en-US/docs/Web/API/NavigationHistoryEntry/dispose_event)

Fires when the entry is no longer part of the history entry list.

## [Examples](#examples)

js

```
function initHomeBtn() {
  // Get the key of the first loaded entry
  // so the user can always go back to this view.
  const { key } = navigation.currentEntry;
  backToHomeButton.onclick = () => {
    navigation.traverseTo(key);
  };
}
// Intercept navigate events, such as link clicks, and
// replace them with single-page navigations
navigation.addEventListener("navigate", (event) => {
  event.intercept({
    async handler() {
      // Navigate to a different view,
      // but the "home" button will always work.
    },
  });
});
```

## [Specifications](#specifications)

Specification
[HTML# the-navigationhistoryentry-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-navigationhistoryentry-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)
- [Navigation API explainer](https://github.com/WICG/navigation-api/blob/main/README.md)
- [Navigation API live demo](https://mdn.github.io/dom-examples/navigation-api/) ([view demo source](https://github.com/mdn/dom-examples/tree/main/navigation-api))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigationHistoryEntry/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigationhistoryentry/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationHistoryEntry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigationhistoryentry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationHistoryEntry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigationhistoryentry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0563b7d83916b234fa637483211889e573df9440%0A*+Document+last+modified%3A+2025-12-11T12%3A09%3A51.000Z%0A%0A%3C%2Fdetails%3E)
