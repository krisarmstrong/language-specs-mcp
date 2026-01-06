# NavigationDestination

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationDestination&level=not)

The `NavigationDestination` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) represents the destination being navigated to in the current navigation.

It is accessed via the [NavigateEvent.destination](/en-US/docs/Web/API/NavigateEvent/destination) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[id](/en-US/docs/Web/API/NavigationDestination/id)Read only

Returns the [id](/en-US/docs/Web/API/NavigationHistoryEntry/id) value of the destination [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) if the [NavigateEvent.navigationType](/en-US/docs/Web/API/NavigateEvent/navigationType) is `traverse`, or an empty string otherwise.

[index](/en-US/docs/Web/API/NavigationDestination/index)Read only

Returns the [index](/en-US/docs/Web/API/NavigationHistoryEntry/index) value of the destination [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) if the [NavigateEvent.navigationType](/en-US/docs/Web/API/NavigateEvent/navigationType) is `traverse`, or `-1` otherwise.

[key](/en-US/docs/Web/API/NavigationDestination/key)Read only

Returns the [key](/en-US/docs/Web/API/NavigationHistoryEntry/key) value of the destination [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) if the [NavigateEvent.navigationType](/en-US/docs/Web/API/NavigateEvent/navigationType) is `traverse`, or an empty string otherwise.

[sameDocument](/en-US/docs/Web/API/NavigationDestination/sameDocument)Read only

Returns `true` if the navigation is to the same `document` as the current [Document](/en-US/docs/Web/API/Document) value, or `false` otherwise.

[url](/en-US/docs/Web/API/NavigationDestination/url)Read only

Returns the URL being navigated to.

## [Instance methods](#instance_methods)

[getState()](/en-US/docs/Web/API/NavigationDestination/getState)

Returns a clone of the available state associated with the destination [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry), or navigation operation (e.g., [navigate()](/en-US/docs/Web/API/Navigation/navigate)) as appropriate.

## [Examples](#examples)

js

```
navigation.addEventListener("navigate", (event) => {
  // Exit early if this navigation shouldn't be intercepted,
  // e.g. if the navigation is cross-origin, or a download request
  if (shouldNotIntercept(event)) {
    return;
  }

  // Returns a URL() object constructed from the
  // NavigationDestination.url value
  const url = new URL(event.destination.url);

  if (url.pathname.startsWith("/articles/")) {
    event.intercept({
      async handler() {
        // The URL has already changed, so show a placeholder while
        // fetching the new content, such as a spinner or loading page
        renderArticlePagePlaceholder();

        // Fetch the new content and display when ready
        const articleContent = await getArticleContent(url.pathname);
        renderArticlePage(articleContent);
      },
    });
  }
});
```

## [Specifications](#specifications)

Specification
[HTML# the-navigationdestination-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-navigationdestination-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)
- [Navigation API explainer](https://github.com/WICG/navigation-api/blob/main/README.md)
- [Navigation API live demo](https://mdn.github.io/dom-examples/navigation-api/) ([view demo source](https://github.com/mdn/dom-examples/tree/main/navigation-api))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigationDestination/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigationdestination/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationDestination&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigationdestination%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationDestination%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigationdestination%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
