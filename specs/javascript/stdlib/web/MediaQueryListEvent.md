# MediaQueryListEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaQueryListEvent&level=high)

The `MediaQueryListEvent` object stores information on the changes that have happened to a [MediaQueryList](/en-US/docs/Web/API/MediaQueryList) object — instances are available as the event object on a function referenced by a [change](/en-US/docs/Web/API/MediaQueryList/change_event) event.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaQueryListEvent()](/en-US/docs/Web/API/MediaQueryListEvent/MediaQueryListEvent)

Creates a new `MediaQueryListEvent` instance.

## [Instance properties](#instance_properties)

The `MediaQueryListEvent` interface inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[MediaQueryListEvent.matches](/en-US/docs/Web/API/MediaQueryListEvent/matches)Read only

A boolean value that is `true` if the [document](/en-US/docs/Web/API/Document) currently matches the media query list, or `false` if not.

[MediaQueryListEvent.media](/en-US/docs/Web/API/MediaQueryListEvent/media)Read only

A string representing a serialized media query.

## [Instance methods](#instance_methods)

The `MediaQueryListEvent` interface inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

js

```
const para = document.querySelector("p"); // This is the UI element where to display the text
const mql = window.matchMedia("(width <= 600px)");

mql.addEventListener("change", (event) => {
  if (event.matches) {
    // The viewport is 600 pixels wide or less
    para.textContent = "This is a narrow screen — less than 600px wide.";
    document.body.style.backgroundColor = "red";
  } else {
    // The viewport is more than 600 pixels wide
    para.textContent = "This is a wide screen — more than 600px wide.";
    document.body.style.backgroundColor = "blue";
  }
});
```

## [Specifications](#specifications)

Specification
[CSSOM View Module# the-mediaquerylist-interface](https://drafts.csswg.org/cssom-view/#the-mediaquerylist-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Media queries](/en-US/docs/Web/CSS/Guides/Media_queries/Using)
- [Using media queries from code](/en-US/docs/Web/CSS/Guides/Media_queries/Testing)
- [window.matchMedia()](/en-US/docs/Web/API/Window/matchMedia)
- [MediaQueryList](/en-US/docs/Web/API/MediaQueryList)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaQueryListEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediaquerylistevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaQueryListEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediaquerylistevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaQueryListEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediaquerylistevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
