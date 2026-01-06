# NavigationPrecommitController

The `NavigationPrecommitController` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) defines redirect behavior for a navigation [precommit handler](/en-US/docs/Web/API/NavigateEvent/intercept#precommithandler).

## In this article

- [Instance methods](#instance_methods)
- [Description](#description)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[redirect()](/en-US/docs/Web/API/NavigationPrecommitController/redirect)

Redirects the browser to a specified URL and specifies history behavior and any desired state information.

## [Description](#description)

When specifying same-document navigation behavior via the [NavigateEvent.intercept()](/en-US/docs/Web/API/NavigateEvent/intercept) method, it is possible to specify navigation precommit actions via the [precommitHandler](/en-US/docs/Web/API/NavigateEvent/intercept#precommithandler) callback. Precommit actions are used to modify or cancel in-flight navigation, or to perform work while the navigation is ongoing and before it is committed (see [Basic precommit navigation example](#basic_precommit_navigation_example)).

To specify the redirect behavior, you pass a `NavigationPrecommitController` object into the `precommitHandler` callback function. Inside the function body, you can call the `NavigationPrecommitController.redirect()` method, which takes as an argument an object containing the redirect URL, plus any required history behavior and state information.

See the [intercept() description](/en-US/docs/Web/API/NavigateEvent/intercept#description) for additional context.

## [Examples](#examples)

### [Basic precommit navigation example](#basic_precommit_navigation_example)

The following snippet shows how you would redirect the browser to a sign-in page if the user navigates to a restricted page and is not signed in.

js

```
navigation.addEventListener("navigate", (event) => {
  const url = new URL(event.destination.url);

  if (url.pathname.startsWith("/restricted/") && !userSignedIn) {
    event.intercept({
      async precommitHandler(controller) {
        controller.redirect("/signin/", {
          state: "signin-redirect",
          history: "push",
        });
      },
    });
  }
});
```

This pattern is simpler than the alternative of canceling the original navigation and starting a new one to the redirect location, because it avoids exposing the intermediate state. For example, only one [navigatesuccess](/en-US/docs/Web/API/Navigation/navigatesuccess_event) or [navigateerror](/en-US/docs/Web/API/Navigation/navigateerror_event) event fires, and if the navigation was triggered by a call to [Navigation.navigate()](/en-US/docs/Web/API/Navigation/navigate), the promise only fulfills once the redirect destination is reached.

## [Specifications](#specifications)

Specification
[HTML# the-navigationprecommitcontroller-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-navigationprecommitcontroller-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigationPrecommitController/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigationprecommitcontroller/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationPrecommitController&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigationprecommitcontroller%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationPrecommitController%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigationprecommitcontroller%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0563b7d83916b234fa637483211889e573df9440%0A*+Document+last+modified%3A+2025-12-11T12%3A09%3A51.000Z%0A%0A%3C%2Fdetails%3E)
