# TransitionEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransitionEvent&level=high)

The `TransitionEvent` interface represents events providing information related to [transitions](/en-US/docs/Web/CSS/Guides/Transitions/Using).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Types of TransitionEvent](#types_of_transitionevent)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[TransitionEvent()](/en-US/docs/Web/API/TransitionEvent/TransitionEvent)

Creates a `TransitionEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[TransitionEvent.propertyName](/en-US/docs/Web/API/TransitionEvent/propertyName)Read only

A string containing the name CSS property associated with the transition.

[TransitionEvent.elapsedTime](/en-US/docs/Web/API/TransitionEvent/elapsedTime)Read only

A `float` giving the amount of time the transition has been running, in seconds, when this event fired. This value is not affected by the [transition-delay](/en-US/docs/Web/CSS/Reference/Properties/transition-delay) property.

[TransitionEvent.pseudoElement](/en-US/docs/Web/API/TransitionEvent/pseudoElement)Read only

A string, starting with `::`, containing the name of the [pseudo-element](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) the animation runs on. If the transition doesn't run on a pseudo-element but on the element, an empty string: `''`.

## [Types of TransitionEvent](#types_of_transitionevent)

[transitioncancel](/en-US/docs/Web/API/Element/transitioncancel_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) has been cancelled.

[transitionend](/en-US/docs/Web/API/Element/transitionend_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) has finished playing.

[transitionrun](/en-US/docs/Web/API/Element/transitionrun_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) is created (i.e., when it is added to a set of running transitions), though not necessarily started.

[transitionstart](/en-US/docs/Web/API/Element/transitionstart_event)

An [Event](/en-US/docs/Web/API/Event) fired when a [CSS transition](/en-US/docs/Web/CSS/Guides/Transitions) has started transitioning.

## [Instance methods](#instance_methods)

Also inherits methods from its parent [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[CSS Transitions# interface-transitionevent](https://drafts.csswg.org/css-transitions/#interface-transitionevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using CSS transitions](/en-US/docs/Web/CSS/Guides/Transitions/Using)
- CSS properties: [transition](/en-US/docs/Web/CSS/Reference/Properties/transition), [transition-delay](/en-US/docs/Web/CSS/Reference/Properties/transition-delay), [transition-duration](/en-US/docs/Web/CSS/Reference/Properties/transition-duration), [transition-property](/en-US/docs/Web/CSS/Reference/Properties/transition-property), [transition-timing-function](/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
- CSS at-rules: [@starting-style](/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TransitionEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/transitionevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransitionEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftransitionevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransitionEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftransitionevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
