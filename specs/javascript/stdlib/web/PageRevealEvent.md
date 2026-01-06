# PageRevealEvent

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageRevealEvent&level=not)

The `PageRevealEvent` event object is made available inside handler functions for the [pagereveal](/en-US/docs/Web/API/Window/pagereveal_event) event.

During a cross-document navigation, it allows you to manipulate a related [view transition](/en-US/docs/Web/API/View_Transition_API) (providing access to the relevant [ViewTransition](/en-US/docs/Web/API/ViewTransition) object) from the document being navigated to, if a view transition was triggered by the navigation.

Outside view transitions, this event is also useful for cases such as triggering a startup animation, or reporting a page view. It's equivalent to the first [Window.requestAnimationFrame()](/en-US/docs/Web/API/Window/requestAnimationFrame) run after a cross-document navigation, if you were to trigger `requestAnimationFrame()` in the [<head>](/en-US/docs/Web/HTML/Reference/Elements/head) of the document. For example, if you ran the following `reveal()` function in the `<head>`:

js

```
function reveal() {
  // Include startup animation here
}
/* This will fire in the first rendered frame after loading */
requestAnimationFrame(() => reveal());

/* This will fire if the page is restored from BFCache */
window.onpagehide = () => requestAnimationFrame(() => reveal());
```

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PageRevealEvent()](/en-US/docs/Web/API/PageRevealEvent/PageRevealEvent)

Creates a new `PageRevealEvent` object instance.

## [Instance properties](#instance_properties)

[viewTransition](/en-US/docs/Web/API/PageRevealEvent/viewTransition)Read only

Contains a [ViewTransition](/en-US/docs/Web/API/ViewTransition) object representing the active view transition for the cross-document navigation.

## [Examples](#examples)

js

```
window.addEventListener("pagereveal", async (e) => {
  // If the "from" history entry does not exist, return
  if (!navigation.activation.from) return;

  // Only run this if an active view transition exists
  if (e.viewTransition) {
    const fromUrl = new URL(navigation.activation.from.url);
    const currentUrl = new URL(navigation.activation.entry.url);

    // Went from profile page to homepage
    // ~> Set VT names on the relevant list item
    if (isProfilePage(fromUrl) && isHomePage(currentUrl)) {
      const profile = extractProfileNameFromUrl(fromUrl);

      // Set view-transition-name values on the elements to animate
      document.querySelector(`#${profile} span`).style.viewTransitionName =
        "name";
      document.querySelector(`#${profile} img`).style.viewTransitionName =
        "avatar";

      // Remove names after snapshots have been taken
      // so that we're ready for the next navigation
      await e.viewTransition.ready;
      document.querySelector(`#${profile} span`).style.viewTransitionName =
        "none";
      document.querySelector(`#${profile} img`).style.viewTransitionName =
        "none";
    }

    // Went to profile page
    // ~> Set VT names on the main title and image
    if (isProfilePage(currentUrl)) {
      // Set view-transition-name values on the elements to animate
      document.querySelector(`#detail main h1`).style.viewTransitionName =
        "name";
      document.querySelector(`#detail main img`).style.viewTransitionName =
        "avatar";

      // Remove names after snapshots have been taken
      // so that we're ready for the next navigation
      await e.viewTransition.ready;
      document.querySelector(`#detail main h1`).style.viewTransitionName =
        "none";
      document.querySelector(`#detail main img`).style.viewTransitionName =
        "none";
    }
  }
});
```

Note: See [List of Chrome DevRel team members](https://view-transitions.chrome.dev/profiles/mpa/) for the live demo this code is taken from.

## [Specifications](#specifications)

Specification
[HTML# the-pagerevealevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-pagerevealevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [View Transition API](/en-US/docs/Web/API/View_Transition_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 19, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PageRevealEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pagerevealevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageRevealEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpagerevealevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageRevealEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpagerevealevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3a95c239db50c88fdde48daacb6c279006a422b9%0A*+Document+last+modified%3A+2024-12-19T23%3A23%3A15.000Z%0A%0A%3C%2Fdetails%3E)
