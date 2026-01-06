# PageTransitionEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageTransitionEvent&level=high)

The `PageTransitionEvent` event object is available inside handler functions for the [pageshow](/en-US/docs/Web/API/Window/pageshow_event) and [pagehide](/en-US/docs/Web/API/Window/pagehide_event) events, fired when a document is being loaded or unloaded.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PageTransitionEvent()](/en-US/docs/Web/API/PageTransitionEvent/PageTransitionEvent)

Creates a new `PageTransitionEvent` object.

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [Event](/en-US/docs/Web/API/Event).

[PageTransitionEvent.persisted](/en-US/docs/Web/API/PageTransitionEvent/persisted)Read only

Indicates if the document is loading from a cache.

## [Example](#example)

js

```
window.addEventListener("pageshow", (event) => {
  if (event.persisted) {
    alert("The page was cached by the browser");
  } else {
    alert("The page was NOT cached by the browser");
  }
});
```

## [Specifications](#specifications)

Specification
[HTML# the-pagetransitionevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-pagetransitionevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [pageshow](/en-US/docs/Web/API/Window/pageshow_event) event
- [pagehide](/en-US/docs/Web/API/Window/pagehide_event) event

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 31, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/PageTransitionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pagetransitionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageTransitionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpagetransitionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPageTransitionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpagetransitionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9f7e7e9075e9f2b1937d2c8000f52a8ff76bff52%0A*+Document+last+modified%3A+2025-10-31T15%3A27%3A28.000Z%0A%0A%3C%2Fdetails%3E)
