# NavigateEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigateEvent&level=not)

The `NavigateEvent` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) is the event object for the [navigate](/en-US/docs/Web/API/Navigation/navigate_event) event, which fires when [any type of navigation](https://github.com/WICG/navigation-api#appendix-types-of-navigations) is initiated (this includes usage of [History API](/en-US/docs/Web/API/History_API) features like [History.go()](/en-US/docs/Web/API/History/go)). `NavigateEvent` provides access to information about that navigation, and allows developers to intercept and control the navigation handling.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[NavigateEvent()](/en-US/docs/Web/API/NavigateEvent/NavigateEvent)

Creates a new `NavigateEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[canIntercept](/en-US/docs/Web/API/NavigateEvent/canIntercept)Read only

Returns `true` if the navigation can be intercepted, or `false` otherwise (e.g., you can't intercept a cross-origin navigation).

[destination](/en-US/docs/Web/API/NavigateEvent/destination)Read only

Returns a [NavigationDestination](/en-US/docs/Web/API/NavigationDestination) object representing the destination being navigated to.

[downloadRequest](/en-US/docs/Web/API/NavigateEvent/downloadRequest)Read only

Returns the filename of the file requested for download, in the case of a download navigation (e.g., an [<a>](/en-US/docs/Web/HTML/Reference/Elements/a) or [<area>](/en-US/docs/Web/HTML/Reference/Elements/area) element with a `download` attribute), or `null` otherwise.

[formData](/en-US/docs/Web/API/NavigateEvent/formData)Read only

Returns the [FormData](/en-US/docs/Web/API/FormData) object representing the submitted data in the case of a `POST` form submission, or `null` otherwise.

[hashChange](/en-US/docs/Web/API/NavigateEvent/hashChange)Read only

Returns `true` if the navigation is a fragment navigation (i.e., to a fragment identifier in the same document), or `false` otherwise.

[hasUAVisualTransition](/en-US/docs/Web/API/NavigateEvent/hasUAVisualTransition)Read only

Returns `true` if the user agent performed a visual transition for this navigation before dispatching this event, or `false` otherwise.

[info](/en-US/docs/Web/API/NavigateEvent/info)Read only

Returns the `info` data value passed by the initiating navigation operation (e.g., [Navigation.back()](/en-US/docs/Web/API/Navigation/back), or [Navigation.navigate()](/en-US/docs/Web/API/Navigation/navigate)), or `undefined` if no `info` data was passed.

[navigationType](/en-US/docs/Web/API/NavigateEvent/navigationType)Read only

Returns the type of the navigation — `push`, `reload`, `replace`, or `traverse`.

[signal](/en-US/docs/Web/API/NavigateEvent/signal)Read only

Returns an [AbortSignal](/en-US/docs/Web/API/AbortSignal), which will become aborted if the navigation is cancelled (e.g., by the user pressing the browser's "Stop" button, or another navigation starting and thus cancelling the ongoing one).

[sourceElement](/en-US/docs/Web/API/NavigateEvent/sourceElement)Read only

When the navigation was initiated by an element (for example clicking a link), returns an [Element](/en-US/docs/Web/API/Element) object representing the initiating element.

[userInitiated](/en-US/docs/Web/API/NavigateEvent/userInitiated)Read only

Returns `true` if the navigation was initiated by the user (e.g., by clicking a link, submitting a form, or pressing the browser's "Back"/"Forward" buttons), or `false` otherwise.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

[intercept()](/en-US/docs/Web/API/NavigateEvent/intercept)

Intercepts this navigation, turning it into a same-document navigation to the [destination](/en-US/docs/Web/API/NavigationDestination/url) URL. It can accept handler functions that define what the navigation handling behavior should be, plus `focusReset` and `scroll` options to enable or disable the browser's default focus and scrolling behavior as desired.

[scroll()](/en-US/docs/Web/API/NavigateEvent/scroll)

Can be called to manually trigger the browser-driven scrolling behavior that occurs in response to the navigation, if you want it to happen before the navigation handling has completed.

## [Examples](#examples)

### [Handling a navigation using intercept()](#handling_a_navigation_using_intercept)

js

```
navigation.addEventListener("navigate", (event) => {
  // Exit early if this navigation shouldn't be intercepted,
  // e.g. if the navigation is cross-origin, or a download request
  if (shouldNotIntercept(event)) return;

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

Note: Before the Navigation API was available, to do something similar you'd have to listen for all click events on links, run `e.preventDefault()`, perform the appropriate [History.pushState()](/en-US/docs/Web/API/History/pushState) call, then set up the page view based on the new URL. And this wouldn't handle all navigations — only user-initiated link clicks.

### [Handling scrolling using scroll()](#handling_scrolling_using_scroll)

In this example of intercepting a navigation, the `handler()` function starts by fetching and rendering some article content, but then fetches and renders some secondary content afterwards. It makes sense to scroll the page to the main article content as soon as it is available so the user can interact with it, rather than waiting until the secondary content is also rendered. To achieve this, we have added a [scroll()](/en-US/docs/Web/API/NavigateEvent/scroll) call between the two.

js

```
navigation.addEventListener("navigate", (event) => {
  if (shouldNotIntercept(navigateEvent)) return;
  const url = new URL(event.destination.url);

  if (url.pathname.startsWith("/articles/")) {
    event.intercept({
      async handler() {
        const articleContent = await getArticleContent(url.pathname);
        renderArticlePage(articleContent);

        event.scroll();

        const secondaryContent = await getSecondaryContent(url.pathname);
        addSecondaryContent(secondaryContent);
      },
    });
  }
});
```

## [Specifications](#specifications)

Specification
[HTML# the-navigateevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-navigateevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)
- [Navigation API explainer](https://github.com/WICG/navigation-api/blob/main/README.md)
- [Navigation API live demo](https://mdn.github.io/dom-examples/navigation-api/) ([view demo source](https://github.com/mdn/dom-examples/tree/main/navigation-api))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigateEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigateevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigateEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigateevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigateEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigateevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
