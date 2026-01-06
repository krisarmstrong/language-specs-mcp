# ViewTransition

 Baseline  2025  * Newly available

 Since ⁨October 2025⁩, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTransition&level=low)

The `ViewTransition` interface of the [View Transition API](/en-US/docs/Web/API/View_Transition_API) represents an active view transition, and provides functionality to react to the transition reaching different states (e.g., ready to run the animation, or animation finished) or skip the transition altogether.

This object type is made available in the following ways:

- Via the [Document.activeViewTransition](/en-US/docs/Web/API/Document/activeViewTransition) property. This provides a consistent way to access the active view transition in any context, without having to worry about saving it for easy access later on.
- In the case of same-document (SPA) transitions, it is also returned by the [document.startViewTransition()](/en-US/docs/Web/API/Document/startViewTransition) method.
- In the case of cross-document (MPA) transitions, it is also made available: 

  - In the outgoing page via the [pageswap](/en-US/docs/Web/API/Window/pageswap_event) event object's [PageSwapEvent.viewTransition](/en-US/docs/Web/API/PageSwapEvent/viewTransition) property.
  - In the inbound page via the [pagereveal](/en-US/docs/Web/API/Window/pagereveal_event) event object's [PageRevealEvent.viewTransition](/en-US/docs/Web/API/PageRevealEvent/viewTransition) property.

When a view transition is triggered by a `startViewTransition()` call (or a page navigation in the case of MPA transitions), a sequence of steps is followed as explained in [The view transition process](/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_process). This also explains when the different promises fulfill.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[ViewTransition.finished](/en-US/docs/Web/API/ViewTransition/finished)Read only

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills once the transition animation is finished, and the new page view is visible and interactive to the user.

[ViewTransition.ready](/en-US/docs/Web/API/ViewTransition/ready)Read only

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills once the pseudo-element tree is created and the transition animation is about to start.

[ViewTransition.types](/en-US/docs/Web/API/ViewTransition/types)Read only

A [ViewTransitionTypeSet](/en-US/docs/Web/API/ViewTransitionTypeSet) that allows the types set on the view transition to be accessed and modified.

[ViewTransition.updateCallbackDone](/en-US/docs/Web/API/ViewTransition/updateCallbackDone)Read only

A [Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that fulfills when the promise returned by the [document.startViewTransition()](/en-US/docs/Web/API/Document/startViewTransition) method's callback fulfills.

## [Instance methods](#instance_methods)

[skipTransition()](/en-US/docs/Web/API/ViewTransition/skipTransition)

Skips the animation part of the view transition, but doesn't skip running the [document.startViewTransition()](/en-US/docs/Web/API/Document/startViewTransition) callback that updates the DOM.

## [Examples](#examples)

In the following SPA example, the [ViewTransition.ready](/en-US/docs/Web/API/ViewTransition/ready) promise is used to trigger a custom circular reveal view transition emanating from the position of the user's cursor on click, with animation provided by the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API).

js

```
// Store the last click event
let lastClick;
addEventListener("click", (event) => (lastClick = event));

function spaNavigate(data) {
  // Fallback for browsers that don't support this API:
  if (!document.startViewTransition) {
    updateTheDOMSomehow(data);
    return;
  }

  // Get the click position, or fallback to the middle of the screen
  const x = lastClick?.clientX ?? innerWidth / 2;
  const y = lastClick?.clientY ?? innerHeight / 2;
  // Get the distance to the furthest corner
  const endRadius = Math.hypot(
    Math.max(x, innerWidth - x),
    Math.max(y, innerHeight - y),
  );

  // Create a transition:
  const transition = document.startViewTransition(() => {
    updateTheDOMSomehow(data);
  });

  // Wait for the pseudo-elements to be created:
  transition.ready.then(() => {
    // Animate the root's new view
    document.documentElement.animate(
      {
        clipPath: [
          `circle(0 at ${x}px ${y}px)`,
          `circle(${endRadius}px at ${x}px ${y}px)`,
        ],
      },
      {
        duration: 500,
        easing: "ease-in",
        // Specify which pseudo-element to animate
        pseudoElement: "::view-transition-new(root)",
      },
    );
  });
}
```

This animation also requires the following CSS, to turn off the default CSS animation and stop the old and new view states from blending in any way (the new state "wipes" right over the top of the old state, rather than transitioning in):

css

```
::view-transition-image-pair(root) {
  isolation: auto;
}

::view-transition-old(root),
::view-transition-new(root) {
  animation: none;
  mix-blend-mode: normal;
  display: block;
}
```

## [Specifications](#specifications)

Specification
[CSS View Transitions Module Level 1# viewtransition](https://drafts.csswg.org/css-view-transitions/#viewtransition)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [View Transition API](/en-US/docs/Web/API/View_Transition_API)
- [Using the View Transition API](/en-US/docs/Web/API/View_Transition_API/Using)
- [Using view transition types](/en-US/docs/Web/API/View_Transition_API/Using_types)
- [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ViewTransition/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/viewtransition/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTransition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fviewtransition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTransition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fviewtransition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbaf0cb6bfe8bf2418122300d3f93e3aa94f72dca%0A*+Document+last+modified%3A+2025-12-09T12%3A19%3A47.000Z%0A%0A%3C%2Fdetails%3E)
