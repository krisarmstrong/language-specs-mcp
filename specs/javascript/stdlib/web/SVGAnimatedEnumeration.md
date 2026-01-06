# SVGAnimatedEnumeration

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimatedEnumeration&level=high)

The `SVGAnimatedEnumeration` interface describes attribute values which are constants from a particular enumeration and which can be animated.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[baseVal](/en-US/docs/Web/API/SVGAnimatedEnumeration/baseVal)

An integer that is the base value of the given attribute before applying any animations.

[animVal](/en-US/docs/Web/API/SVGAnimatedEnumeration/animVal)

If the given attribute or property is being animated, it contains the current animated value of the attribute or property. If the given attribute or property is not currently being animated, it contains the same value as `baseVal`.

## [Instance methods](#instance_methods)

The `SVGAnimatedEnumeration` interface do not provide any specific methods.

## [Examples](#examples)

Considering this snippet with a [<clipPath>](/en-US/docs/Web/SVG/Reference/Element/clipPath) element: Its [clipPathUnits](/en-US/docs/Web/SVG/Reference/Attribute/clipPathUnits) is associated with a `SVGAnimatedEnumeration` object.

html

```
<svg viewBox="0 0 100 100" width="200" height="200">
  <clipPath id="clip1" clipPathUnits="userSpaceOnUse">
    <circle cx="50" cy="50" r="35" />
  </clipPath>

  <!-- Some reference rect to materialized to clip path -->
  <rect id="r1" x="0" y="0" width="45" height="45" />
</svg>
```

This snippet gets the element, and logs the `baseVal` and `animVal` of the [SVGClipPathElement.clipPathUnits](/en-US/docs/Web/API/SVGClipPathElement/clipPathUnits) property. As no animation is happening, they have the same value.

js

```
const clipPathElt = document.getElementById("clip1");
console.log(clipPathElt.clipPathUnits.baseVal); // Logs 1 that correspond to userSpaceOnUse
console.log(clipPathElt.clipPathUnits.animVal); // Logs 1 that correspond to userSpaceOnUse
```

## [Specifications](#specifications)

Specification
[Scalable Vector Graphics (SVG) 2# InterfaceSVGAnimatedEnumeration](https://svgwg.org/svg2-draft/types.html#InterfaceSVGAnimatedEnumeration)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 13, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/SVGAnimatedEnumeration/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svganimatedenumeration/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimatedEnumeration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvganimatedenumeration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimatedEnumeration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvganimatedenumeration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbb48907e64eb4bf60f17efd7d39b46c771d220a0%0A*+Document+last+modified%3A+2024-08-13T13%3A25%3A16.000Z%0A%0A%3C%2Fdetails%3E)
