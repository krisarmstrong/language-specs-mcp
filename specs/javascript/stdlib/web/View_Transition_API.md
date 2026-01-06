# View Transition API

The View Transition API provides a mechanism for easily creating animated transitions between different website views. This includes animating between DOM states in a single-page app (SPA), and animating the navigation between documents in a multi-page app (MPA).

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [HTML additions](#html_additions)
- [CSS additions](#css_additions)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

View transitions are a popular design choice for reducing users' cognitive load, helping them stay in context, and reducing perceived loading latency as they move between states or views of an application.

However, creating view transitions on the web has historically been difficult:

- Transitions between states in single-page apps (SPAs) tend to involve writing significant CSS and JavaScript to: 

  - Handle the loading and positioning of the old and new content.
  - Animate the old and new states to create the transition.
  - Stop accidental user interactions with the old content from causing problems.
  - Remove the old content once the transition is complete. Accessibility issues like loss of reading position, focus confusion, and strange live region announcement behavior can also result from having the new and old content both present in the DOM at once.

- Cross-document view transitions (i.e., across navigations between different pages in MPAs) have historically been impossible.

The View Transition API provides an easy way of handling the required view changes and transition animations for both the above use cases.

Creating a view transition that uses the browser's default transition animations is very quick to do, and there are features that allow you to both customize the transition animation and manipulate the view transition itself (for example specify circumstances under which the animation is skipped), for both SPA and MPA view transitions.

See [Using the View Transition API](/en-US/docs/Web/API/View_Transition_API/Using) for more information.

## [Interfaces](#interfaces)

[CSSViewTransitionRule](/en-US/docs/Web/API/CSSViewTransitionRule)

Represents a [@view-transition](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)[at-rule](/en-US/docs/Web/CSS/Guides/Syntax/At-rules).

[ViewTransition](/en-US/docs/Web/API/ViewTransition)

Represents a view transition, and provides functionality to react to the transition reaching different states (e.g., ready to run the animation, or animation finished) or skip the transition altogether.

[ViewTransitionTypeSet](/en-US/docs/Web/API/ViewTransitionTypeSet)

A [set-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) representing the types of an active view transition, which enables the types to be queried or modified on-the-fly during a transition.

## [Extensions to other interfaces](#extensions_to_other_interfaces)

[Document.startViewTransition()](/en-US/docs/Web/API/Document/startViewTransition)

Starts a new same-document (SPA) view transition and returns a [ViewTransition](/en-US/docs/Web/API/ViewTransition) object to represent it.

[PageRevealEvent](/en-US/docs/Web/API/PageRevealEvent)

The event object for the [pagereveal](/en-US/docs/Web/API/Window/pagereveal_event) event. During a cross-document navigation, it allows you to manipulate the related view transition (providing access to the relevant [ViewTransition](/en-US/docs/Web/API/ViewTransition) object) from the document being navigated to, if a view transition was triggered by the navigation.

[PageSwapEvent](/en-US/docs/Web/API/PageSwapEvent)

The event object for the [pageswap](/en-US/docs/Web/API/Window/pageswap_event) event. During a cross-document navigation, it allows you to manipulate the related view transition (providing access to the relevant [ViewTransition](/en-US/docs/Web/API/ViewTransition) object) from the document being navigated from, if a view transition was triggered by the navigation. It also provides access to information on the navigation type and current and destination document history entries.

The [Window](/en-US/docs/Web/API/Window)[pagereveal](/en-US/docs/Web/API/Window/pagereveal_event) event

Fired when a document is first rendered, either when loading a fresh document from the network or activating a document (either from [back/forward cache](/en-US/docs/Glossary/bfcache) (bfcache) or [prerender](/en-US/docs/Glossary/Prerender)).

The [Window](/en-US/docs/Web/API/Window)[pageswap](/en-US/docs/Web/API/Window/pageswap_event) event

Fired when a document is about to be unloaded due to a navigation.

## [HTML additions](#html_additions)

[<link rel="expect">](/en-US/docs/Web/HTML/Reference/Attributes/rel#expect)

Identifies the most critical content in the associated document for the user's initial view of the page. Document rendering will be blocked until the critical content has been parsed, ensuring a consistent first paint — and therefore, view transition — across all supporting browsers.

## [CSS additions](#css_additions)

### [At-rules](#at-rules)

[@view-transition](/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)

In the case of a cross-document navigation, `@view-transition` is used to opt in the current and destination documents to undergo a view transition.

### [Properties](#properties)

[view-transition-name](/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)

Specifies the view transition snapshot that selected elements will participate in, which enables an element to be animated separately from the rest of the page during a view transition.

[view-transition-class](/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)

Provides an additional method of styling selected elements that have a `view-transition-name`.

### [Pseudo-classes](#pseudo-classes)

[:active-view-transition](/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)

Matches elements when a view transition is in progress.

[:active-view-transition-type()](/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type)

Matches elements when a view transition with one or more specific types is in progress.

### [Pseudo-elements](#pseudo-elements)

[::view-transition](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)

The root of the view transitions overlay, which contains all view transitions and sits over the top of all other page content.

[::view-transition-group()](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)

The root of a single view transition.

[::view-transition-image-pair()](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)

The container for a view transition's old and new views — before and after the transition.

[::view-transition-old()](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)

A static snapshot of the old view, before the transition.

[::view-transition-new()](/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)

A live representation of the new view, after the transition.

## [Examples](#examples)

- [Basic View Transitions SPA demo](https://mdn.github.io/dom-examples/view-transitions/spa/): A basic image gallery demo with view transitions, featuring separate animations between old and new images, and old and new captions.
- [Basic View Transitions MPA demo](https://mdn.github.io/dom-examples/view-transitions/mpa/): A sample two-page site that demonstrates usage of cross-document (MPA) view transitions, providing a custom "swipe up" transition when the two pages are navigated between.
- [View transitions match-element demo](/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#using_the_match-element_value): An SPA featuring animated list items, demonstrating the use of the `match-element` value of the `view-transition-name` property to animate individual elements.
- [HTTP 203 playlist](https://http203-playlist.netlify.app/): A video player demo app that features several different SPA view transitions, many of which are explained in [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/).
- [Chrome DevRel view transitions demos](https://view-transitions.chrome.dev/): A series of View Transition API demos.

## [Specifications](#specifications)

Specification[CSS View Transitions Module Level 2](https://drafts.csswg.org/css-view-transitions-2/)[CSS View Transitions Module Level 1](https://drafts.csswg.org/css-view-transitions/)

## [Browser compatibility](#browser_compatibility)

### [api.Document.startViewTransition](#api.Document.startViewTransition)

### [css.at-rules.view-transition](#css.at-rules.view-transition)

## [See also](#see_also)

- [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/) on developer.chrome.com (2024)
- [View Transition API: Creating Smooth Page Transitions](https://stackdiary.com/view-transitions-api/) on stackdiary.com (2023)
- [View Transitions API: Single Page Apps Without a Framework](https://www.debugbear.com/blog/view-transitions-spa-without-framework) on DebugBear (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/View_Transition_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/view_transition_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FView_Transition_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fview_transition_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FView_Transition_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fview_transition_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbaf0cb6bfe8bf2418122300d3f93e3aa94f72dca%0A*+Document+last+modified%3A+2025-12-09T12%3A19%3A47.000Z%0A%0A%3C%2Fdetails%3E)
