# PageSwapEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageSwapEvent&level=not)

The `PageSwapEvent` event object is made available inside handler functions for the [pageswap](/en-US/docs/Web/API/Window/pageswap_event) event.

The `pageswap` event is fired when you navigate across documents, when the previous document is about to unload. During a cross-document navigation, the `PageSwapEvent` event object allows you to manipulate the related [view transition](/en-US/docs/Web/API/View_Transition_API) (providing access to the relevant [ViewTransition](/en-US/docs/Web/API/ViewTransition) object) from the document being navigated from, if a view transition was triggered by the navigation. It also provides access to information on the navigation type and current and destination documents.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PageSwapEvent()](/en-US/docs/Web/API/PageSwapEvent/PageSwapEvent)

Creates a new `PageSwapEvent` object instance.

## [Instance properties](#instance_properties)

[activation](/en-US/docs/Web/API/PageSwapEvent/activation)Read only

Contains a [NavigationActivation](/en-US/docs/Web/API/NavigationActivation) object containing the navigation type and current and destination document history entries for a same-origin navigation. If the navigation has a cross-origin URL anywhere in the redirect chain, it returns `null`.

[viewTransition](/en-US/docs/Web/API/PageSwapEvent/viewTransition)Read only

Contains a [ViewTransition](/en-US/docs/Web/API/ViewTransition) object representing the active view transition for the cross-document navigation.

## [Examples](#examples)

js

```
window.addEventListener("pageswap", async (e) => {
  // Only run this if an active view transition exists
  if (e.viewTransition) {
    const currentUrl = e.activation.from?.url
      ? new URL(e.activation.from.url)
      : null;
    const targetUrl = new URL(e.activation.entry.url);

    // Going from profile page to homepage
    // ~> The big img and title are the ones!
    if (isProfilePage(currentUrl) && isHomePage(targetUrl)) {
      // Set view-transition-name values on the elements to animate
      document.querySelector(`#detail main h1`).style.viewTransitionName =
        "name";
      document.querySelector(`#detail main img`).style.viewTransitionName =
        "avatar";

      // Remove view-transition-names after snapshots have been taken
      // Stops naming conflicts resulting from the page state persisting in BFCache
      await e.viewTransition.finished;
      document.querySelector(`#detail main h1`).style.viewTransitionName =
        "none";
      document.querySelector(`#detail main img`).style.viewTransitionName =
        "none";
    }

    // Going to profile page
    // ~> The clicked items are the ones!
    if (isProfilePage(targetUrl)) {
      const profile = extractProfileNameFromUrl(targetUrl);

      // Set view-transition-name values on the elements to animate
      document.querySelector(`#${profile} span`).style.viewTransitionName =
        "name";
      document.querySelector(`#${profile} img`).style.viewTransitionName =
        "avatar";

      // Remove view-transition-names after snapshots have been taken
      // Stops naming conflicts resulting from the page state persisting in BFCache
      await e.viewTransition.finished;
      document.querySelector(`#${profile} span`).style.viewTransitionName =
        "none";
      document.querySelector(`#${profile} img`).style.viewTransitionName =
        "none";
    }
  }
});
```

Note: See [List of Chrome DevRel team members](https://view-transitions.chrome.dev/profiles/mpa/) for the live demo this code is taken from.

## [Specifications](#specifications)

Specification
[HTML# the-pageswapevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-pageswapevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [View Transition API](/en-US/docs/Web/API/View_Transition_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PageSwapEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pageswapevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageSwapEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpageswapevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageSwapEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpageswapevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3a95c239db50c88fdde48daacb6c279006a422b9%0A*+Document+last+modified%3A+2024-12-19T23%3A23%3A15.000Z%0A%0A%3C%2Fdetails%3E)
