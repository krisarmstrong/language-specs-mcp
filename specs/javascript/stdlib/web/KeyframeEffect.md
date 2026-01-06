# KeyframeEffect

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyframeEffect&level=high)

The `KeyframeEffect` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) lets us create sets of animatable properties and values, called keyframes. These can then be played using the [Animation()](/en-US/docs/Web/API/Animation/Animation) constructor.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[KeyframeEffect()](/en-US/docs/Web/API/KeyframeEffect/KeyframeEffect)

Returns a new `KeyframeEffect` object instance, and also allows you to clone an existing keyframe effect object instance.

## [Instance properties](#instance_properties)

[KeyframeEffect.target](/en-US/docs/Web/API/KeyframeEffect/target)

Gets and sets the element, or originating element of the pseudo-element, being animated by this object. This may be `null` for animations that do not target a specific element or pseudo-element.

[KeyframeEffect.pseudoElement](/en-US/docs/Web/API/KeyframeEffect/pseudoElement)

Gets and sets the selector of the pseudo-element being animated by this object. This may be `null` for animations that do not target a pseudo-element.

[KeyframeEffect.iterationComposite](/en-US/docs/Web/API/KeyframeEffect/iterationComposite)

Gets and sets the iteration composite operation for resolving the property value changes of this keyframe effect.

[KeyframeEffect.composite](/en-US/docs/Web/API/KeyframeEffect/composite)

Gets and sets the composite operation property for resolving the property value changes between this and other keyframe effects.

## [Instance methods](#instance_methods)

This interface inherits some of its methods from its parent, [AnimationEffect](/en-US/docs/Web/API/AnimationEffect).

[AnimationEffect.getComputedTiming()](/en-US/docs/Web/API/AnimationEffect/getComputedTiming)

Returns the calculated, current timing values for this keyframe effect.

[KeyframeEffect.getKeyframes()](/en-US/docs/Web/API/KeyframeEffect/getKeyframes)

Returns the computed keyframes that make up this effect along with their computed keyframe offsets.

[AnimationEffect.getTiming()](/en-US/docs/Web/API/AnimationEffect/getTiming)

Returns the object associated with the animation containing all the animation's timing values.

[KeyframeEffect.setKeyframes()](/en-US/docs/Web/API/KeyframeEffect/setKeyframes)

Replaces the set of keyframes that make up this effect.

[AnimationEffect.updateTiming()](/en-US/docs/Web/API/AnimationEffect/updateTiming)

Updates the specified timing properties.

## [Examples](#examples)

In the following example, the KeyframeEffect constructor is used to create a set of keyframes that dictate how the rofl emoji should roll on the floor:

js

```
const emoji = document.querySelector("div"); // element to animate

const rollingKeyframes = new KeyframeEffect(
  emoji,
  [
    { transform: "translateX(0) rotate(0)" }, // keyframe
    { transform: "translateX(200px) rotate(1.3turn)" }, // keyframe
  ],
  {
    // keyframe options
    duration: 2000,
    direction: "alternate",
    easing: "ease-in-out",
    iterations: "Infinity",
  },
);

const rollingAnimation = new Animation(rollingKeyframes, document.timeline);

// play rofl animation
rollingAnimation.play();
```

html

```
<div>🤣</div>
```

```
body {
  box-shadow: 0 5px 5px pink;
}

div {
  width: fit-content;
  margin-left: calc(50% - 132px);
  font-size: 64px;
  user-select: none;
  margin-top: 1rem;
}
```

## [Specifications](#specifications)

Specification
[Web Animations# the-keyframeeffect-interface](https://drafts.csswg.org/web-animations-1/#the-keyframeeffect-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Animations API](/en-US/docs/Web/API/Web_Animations_API)
- [Animation](/en-US/docs/Web/API/Animation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 12, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/KeyframeEffect/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/keyframeeffect/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyframeEffect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fkeyframeeffect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FKeyframeEffect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fkeyframeeffect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8c04dd43cc39e6726e3b15416d8498f8514cd071%0A*+Document+last+modified%3A+2024-07-12T13%3A38%3A19.000Z%0A%0A%3C%2Fdetails%3E)
