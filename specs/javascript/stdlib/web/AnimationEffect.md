# AnimationEffect

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimationEffect&level=high)

The `AnimationEffect` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) is an interface representing animation effects.

`AnimationEffect` is an abstract interface and so isn't directly instantiable. However, concrete interfaces such as [KeyframeEffect](/en-US/docs/Web/API/KeyframeEffect) inherit from it, and instances of these interfaces can be passed to [Animation](/en-US/docs/Web/API/Animation) objects for playing, and may also be used by [CSS Animations](/en-US/docs/Web/CSS/Guides/Animations) and [Transitions](/en-US/docs/Web/CSS/Guides/Transitions).

## In this article

- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[AnimationEffect.getTiming()](/en-US/docs/Web/API/AnimationEffect/getTiming)

Returns the object associated with the animation containing all the animation's timing values.

[AnimationEffect.getComputedTiming()](/en-US/docs/Web/API/AnimationEffect/getComputedTiming)

Returns the calculated timing properties for this `AnimationEffect`.

[AnimationEffect.updateTiming()](/en-US/docs/Web/API/AnimationEffect/updateTiming)

Updates the specified timing properties of this `AnimationEffect`.

## [Specifications](#specifications)

Specification
[Web Animations# the-animationeffect-interface](https://drafts.csswg.org/web-animations-1/#the-animationeffect-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Animations API](/en-US/docs/Web/API/Web_Animations_API)
- [Animation.effect](/en-US/docs/Web/API/Animation/effect)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AnimationEffect/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/animationeffect/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimationEffect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fanimationeffect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimationEffect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fanimationeffect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
