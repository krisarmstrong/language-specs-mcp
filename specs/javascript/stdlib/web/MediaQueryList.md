# MediaQueryList

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaQueryList&level=high)

A `MediaQueryList` object stores information on a [media query](/en-US/docs/Web/CSS/Guides/Media_queries) applied to a document, with support for both immediate and event-driven matching against the state of the document.

You can create a `MediaQueryList` by calling [matchMedia()](/en-US/docs/Web/API/Window/matchMedia) on the [window](/en-US/docs/Web/API/Window) object. The resulting object handles sending notifications to listeners when the media query state changes (i.e., when the media query test starts or stops evaluating to `true`).

This is very useful for adaptive design, since this makes it possible to observe a document to detect when its media queries change, instead of polling the values periodically, and allows you to programmatically make changes to a document based on media query status.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

The `MediaQueryList` interface inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[matches](/en-US/docs/Web/API/MediaQueryList/matches)Read only

A boolean value that returns `true` if the [document](/en-US/docs/Web/API/Document) currently matches the media query list, or `false` if not.

[media](/en-US/docs/Web/API/MediaQueryList/media)Read only

A string representing a serialized media query.

## [Instance methods](#instance_methods)

The `MediaQueryList` interface inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[addListener()](/en-US/docs/Web/API/MediaQueryList/addListener)Deprecated

Adds to the `MediaQueryList` a callback which is invoked whenever the media query status—whether or not the document matches the media queries in the list—changes. This method exists primarily for backward compatibility; if possible, you should instead use [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) to watch for the [change](/en-US/docs/Web/API/MediaQueryList/change_event) event.

[removeListener()](/en-US/docs/Web/API/MediaQueryList/removeListener)Deprecated

Removes the specified listener callback from the callbacks to be invoked when the `MediaQueryList` changes media query status, which happens any time the document switches between matching and not matching the media queries listed in the `MediaQueryList`. This method has been kept for backward compatibility; if possible, you should generally use [removeEventListener()](/en-US/docs/Web/API/EventTarget/removeEventListener) to remove change notification callbacks (which should have previously been added using `addEventListener()`).

## [Events](#events)

The following events are delivered to `MediaQueryList` objects:

[change](/en-US/docs/Web/API/MediaQueryList/change_event)

Sent to the `MediaQueryList` when the result of running the media query against the document changes. For example, if the media query is `(width >= 400px)`, the `change` event is fired any time the width of the document's [viewport](/en-US/docs/Glossary/Viewport) changes such that its width moves across the 400px boundary in either direction.

## [Examples](#examples)

This example creates a `MediaQueryList` and then sets up a listener to detect when the media query status changes, running a custom function when it does to change the appearance of the page.

js

```
const para = document.querySelector("p");
const mql = window.matchMedia("(width <= 600px)");

function screenTest(e) {
  if (e.matches) {
    /* the viewport is 600 pixels wide or less */
    para.textContent = "This is a narrow screen — less than 600px wide.";
    document.body.style.backgroundColor = "red";
  } else {
    /* the viewport is more than 600 pixels wide */
    para.textContent = "This is a wide screen — more than 600px wide.";
    document.body.style.backgroundColor = "blue";
  }
}

mql.addEventListener("change", screenTest);
```

Note: You can find this example on GitHub (see the [source code](https://github.com/mdn/dom-examples/blob/main/mediaquerylist/index.html), and also see it [running live](https://mdn.github.io/dom-examples/mediaquerylist/index.html)).

You can find other examples on the individual property and method pages.

## [Specifications](#specifications)

Specification
[CSSOM View Module# the-mediaquerylist-interface](https://drafts.csswg.org/cssom-view/#the-mediaquerylist-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Media queries](/en-US/docs/Web/CSS/Guides/Media_queries/Using)
- [Using media queries from code](/en-US/docs/Web/CSS/Guides/Media_queries/Testing)
- [window.matchMedia()](/en-US/docs/Web/API/Window/matchMedia)
- [MediaQueryListEvent](/en-US/docs/Web/API/MediaQueryListEvent)
- The article [Window.devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio) also has a useful example

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/MediaQueryList/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediaquerylist/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaQueryList&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediaquerylist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaQueryList%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediaquerylist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
