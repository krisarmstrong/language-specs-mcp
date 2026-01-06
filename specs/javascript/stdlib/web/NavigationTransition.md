# NavigationTransition

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationTransition&level=not)

The `NavigationTransition` interface of the [Navigation API](/en-US/docs/Web/API/Navigation_API) represents an ongoing navigation, that is, a navigation that hasn't yet reached the [navigatesuccess](/en-US/docs/Web/API/Navigation/navigatesuccess_event) or [navigateerror](/en-US/docs/Web/API/Navigation/navigateerror_event) stage.

It is accessed via the [Navigation.transition](/en-US/docs/Web/API/Navigation/transition) property.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[finished](/en-US/docs/Web/API/NavigationTransition/finished)Read only

Returns a [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills at the same time the [navigatesuccess](/en-US/docs/Web/API/Navigation/navigatesuccess_event) event fires, or rejects at the same time the [navigateerror](/en-US/docs/Web/API/Navigation/navigateerror_event) event fires.

[from](/en-US/docs/Web/API/NavigationTransition/from)Read only

Returns the [NavigationHistoryEntry](/en-US/docs/Web/API/NavigationHistoryEntry) that the transition is coming from.

[navigationType](/en-US/docs/Web/API/NavigationTransition/navigationType)Read only

Returns the type of the ongoing navigation.

## [Examples](#examples)

js

```
async function cleanupNavigation() {
  await navigation.transition.finished;
  // Navigation has completed successfully
  // Cleanup any ongoing monitoring
}
```

## [Specifications](#specifications)

Specification
[HTML# navigationtransition](https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigationtransition)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Modern client-side routing: the Navigation API](https://developer.chrome.com/docs/web-platform/navigation-api/)
- [Navigation API explainer](https://github.com/WICG/navigation-api/blob/main/README.md)
- [Navigation API live demo](https://mdn.github.io/dom-examples/navigation-api/) ([view demo source](https://github.com/mdn/dom-examples/tree/main/navigation-api))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/NavigationTransition/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/navigationtransition/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationTransition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fnavigationtransition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNavigationTransition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fnavigationtransition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E)
