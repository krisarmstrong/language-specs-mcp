# HashChangeEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHashChangeEvent&level=high)

The `HashChangeEvent` interface represents events that fire when the fragment identifier of the URL has changed.

The fragment identifier is the part of the URL that follows (and includes) the `#` symbol.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [Related events](#related_events)

## [Constructor](#constructor)

[HashChangeEvent()](/en-US/docs/Web/API/HashChangeEvent/HashChangeEvent)

Creates a new `HashChangeEvent` object.

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent, [Event](/en-US/docs/Web/API/Event).

[HashChangeEvent.newURL](/en-US/docs/Web/API/HashChangeEvent/newURL)Read only

The new URL to which the window is navigating.

[HashChangeEvent.oldURL](/en-US/docs/Web/API/HashChangeEvent/oldURL)Read only

The previous URL from which the window was navigated.

## [Instance methods](#instance_methods)

This interface has no methods of its own, but inherits the methods of its parent, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

### [Basic example](#basic_example)

js

```
function locationHashChanged() {
  if (location.hash === "#some-cool-feature") {
    someCoolFeature();
  }
}

window.addEventListener("hashchange", locationHashChanged);
```

## [Specifications](#specifications)

Specification
[HTML# the-hashchangeevent-interface](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-hashchangeevent-interface)

## [Browser compatibility](#browser_compatibility)

## [Related events](#related_events)

- [hashchange](/en-US/docs/Web/API/Window/hashchange_event)
- [popstate](/en-US/docs/Web/API/Window/popstate_event)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 27, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/HashChangeEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/hashchangeevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHashChangeEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhashchangeevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHashChangeEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhashchangeevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbff3a6a2e6b3c13dd8bb0c80a1eb9da08cce5dc6%0A*+Document+last+modified%3A+2024-10-27T23%3A53%3A01.000Z%0A%0A%3C%2Fdetails%3E)
