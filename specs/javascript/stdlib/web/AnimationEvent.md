# AnimationEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimationEvent&level=high)

The `AnimationEvent` interface represents events providing information related to [animations](/en-US/docs/Web/CSS/Guides/Animations/Using).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[AnimationEvent()](/en-US/docs/Web/API/AnimationEvent/AnimationEvent)

Creates an `AnimationEvent` event with the given parameters.

## [Instance properties](#instance_properties)

Also inherits properties from its parent [Event](/en-US/docs/Web/API/Event).

[AnimationEvent.animationName](/en-US/docs/Web/API/AnimationEvent/animationName)Read only

A string containing the value of the [animation-name](/en-US/docs/Web/CSS/Reference/Properties/animation-name) that generated the animation.

[AnimationEvent.elapsedTime](/en-US/docs/Web/API/AnimationEvent/elapsedTime)Read only

A `float` giving the amount of time the animation has been running, in seconds, when this event fired, excluding any time the animation was paused. For an `animationstart` event, `elapsedTime` is `0.0` unless there was a negative value for [animation-delay](/en-US/docs/Web/CSS/Reference/Properties/animation-delay), in which case the event will be fired with `elapsedTime` containing `(-1 * delay)`.

[AnimationEvent.pseudoElement](/en-US/docs/Web/API/AnimationEvent/pseudoElement)Read only

A string, starting with `'::'`, containing the name of the [pseudo-element](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) the animation runs on. If the animation doesn't run on a pseudo-element but on the element, an empty string: `''`.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [Event](/en-US/docs/Web/API/Event).

## [Specifications](#specifications)

Specification
[CSS Animations Level 1# interface-animationevent](https://drafts.csswg.org/css-animations/#interface-animationevent)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using CSS animations](/en-US/docs/Web/CSS/Guides/Animations/Using)
- Animation-related CSS properties and at-rules: [animation](/en-US/docs/Web/CSS/Reference/Properties/animation), [animation-composition](/en-US/docs/Web/CSS/Reference/Properties/animation-composition), [animation-delay](/en-US/docs/Web/CSS/Reference/Properties/animation-delay), [animation-direction](/en-US/docs/Web/CSS/Reference/Properties/animation-direction), [animation-duration](/en-US/docs/Web/CSS/Reference/Properties/animation-duration), [animation-fill-mode](/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode), [animation-iteration-count](/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count), [animation-name](/en-US/docs/Web/CSS/Reference/Properties/animation-name), [animation-play-state](/en-US/docs/Web/CSS/Reference/Properties/animation-play-state), [animation-timing-function](/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function), [@keyframes](/en-US/docs/Web/CSS/Reference/At-rules/@keyframes).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AnimationEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/animationevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimationEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fanimationevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimationEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fanimationevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
