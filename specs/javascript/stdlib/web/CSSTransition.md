# CSSTransition

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransition&level=high)

The `CSSTransition` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) represents an [Animation](/en-US/docs/Web/API/Animation) object used for a [CSS Transition](/en-US/docs/Web/CSS/Guides/Transitions).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [Animation](/en-US/docs/Web/API/Animation).

[CSSTransition.transitionProperty](/en-US/docs/Web/API/CSSTransition/transitionProperty)Read only

Returns the transition CSS property name as a string.

## [Instance methods](#instance_methods)

This interface inherits methods from its parent, [Animation](/en-US/docs/Web/API/Animation).

No specific methods.

## [Examples](#examples)

### [Inspecting the returned CSSTransition](#inspecting_the_returned_csstransition)

The transition in the following example changes the width of the box on hover. Calling [Element.getAnimations()](/en-US/docs/Web/API/Element/getAnimations) returns an array of all [Animation](/en-US/docs/Web/API/Animation) objects. In our case this returns a `CSSTransition` object, representing the animation created.

css

```
.box {
  background-color: #165baa;
  color: white;
  width: 100px;
  height: 100px;
  transition: width 4s;
}

.box:hover {
  width: 200px;
}
```

js

```
const item = document.querySelector(".box");
item.addEventListener("transitionrun", () => {
  let animations = document.querySelector(".box").getAnimations();
  console.log(animations[0]);
});
```

## [Specifications](#specifications)

Specification
[CSS Transitions Level 2# the-CSSTransition-interface](https://drafts.csswg.org/css-transitions-2/#the-CSSTransition-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/CSSTransition/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/csstransition/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcsstransition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSTransition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcsstransition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
