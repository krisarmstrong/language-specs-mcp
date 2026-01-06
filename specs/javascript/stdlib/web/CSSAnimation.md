# CSSAnimation

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSAnimation&level=high)

The `CSSAnimation` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) represents an [Animation](/en-US/docs/Web/API/Animation) object.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface inherits properties from its parent, [Animation](/en-US/docs/Web/API/Animation).

[CSSAnimation.animationName](/en-US/docs/Web/API/CSSAnimation/animationName)Read only

Returns the animation name as a string.

## [Instance methods](#instance_methods)

This interface inherits methods from its parent, [Animation](/en-US/docs/Web/API/Animation).

## [Examples](#examples)

### [Inspecting the returned CSSAnimation](#inspecting_the_returned_cssanimation)

The animation in the following example is defined in CSS with the name `slide-in`. Calling [Element.getAnimations()](/en-US/docs/Web/API/Element/getAnimations) returns an array of all [Animation](/en-US/docs/Web/API/Animation) objects. In our case this returns a `CSSAnimation` object, representing the animation created in CSS.

css

```
.animate {
  animation: slide-in 0.7s both;
}

@keyframes slide-in {
  0% {
    transform: translateY(-1000px);
  }
  100% {
    transform: translateY(0);
  }
}
```

js

```
let animations = document.querySelector(".animate").getAnimations();
console.log(animations[0]);
```

## [Specifications](#specifications)

Specification
[CSS Animations Level 2# the-CSSAnimation-interface](https://drafts.csswg.org/css-animations-2/#the-CSSAnimation-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 30, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/CSSAnimation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/cssanimation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSAnimation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fcssanimation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FCSSAnimation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fcssanimation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4f5e90f47c518afd1e3c11a9fb32b933cc8434e9%0A*+Document+last+modified%3A+2023-03-30T18%3A07%3A14.000Z%0A%0A%3C%2Fdetails%3E)
