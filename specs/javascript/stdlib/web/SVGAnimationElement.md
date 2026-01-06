# SVGAnimationElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨January 2020⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimationElement&level=high)

The `SVGAnimationElement` interface is the base interface for all of the animation element interfaces: [SVGAnimateElement](/en-US/docs/Web/API/SVGAnimateElement), [SVGSetElement](/en-US/docs/Web/API/SVGSetElement), [SVGAnimateColorElement](/en-US/docs/Web/API/SVGAnimateColorElement), [SVGAnimateMotionElement](/en-US/docs/Web/API/SVGAnimateMotionElement) and [SVGAnimateTransformElement](/en-US/docs/Web/API/SVGAnimateTransformElement).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGAnimationElement.requiredExtensions](/en-US/docs/Web/API/SVGAnimationElement/requiredExtensions)Read only

An [SVGStringList](/en-US/docs/Web/API/SVGStringList) reflecting the [requiredExtensions](/en-US/docs/Web/SVG/Reference/Attribute/requiredExtensions) attribute of the given element.

[SVGAnimationElement.systemLanguage](/en-US/docs/Web/API/SVGAnimationElement/systemLanguage)Read only

An [SVGStringList](/en-US/docs/Web/API/SVGStringList) reflecting the [systemLanguage](/en-US/docs/Web/SVG/Reference/Attribute/systemLanguage) attribute of the given element.

[SVGAnimationElement.targetElement](/en-US/docs/Web/API/SVGAnimationElement/targetElement)Read only

An [SVGElement](/en-US/docs/Web/API/SVGElement) representing the element which is being animated. If no target element is being animated (for example, because the [href](/en-US/docs/Web/SVG/Reference/Attribute/href) specifies an unknown element) the value returned is `null`.

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [SVGElement](/en-US/docs/Web/API/SVGElement).

[SVGAnimationElement.getStartTime()](/en-US/docs/Web/API/SVGAnimationElement/getStartTime)

Returns a float representing the begin time, in seconds, for this animation element's current interval, if it exists, regardless of whether the interval has begun yet. If there is no current interval, then a [DOMException](/en-US/docs/Web/API/DOMException) with code `INVALID_STATE_ERR` is thrown.

[SVGAnimationElement.getCurrentTime()](/en-US/docs/Web/API/SVGAnimationElement/getCurrentTime)

Returns a float representing the current time in seconds relative to time zero for the given time container.

[SVGAnimationElement.getSimpleDuration()](/en-US/docs/Web/API/SVGAnimationElement/getSimpleDuration)

Returns a float representing the number of seconds for the simple duration for this animation. If the simple duration is undefined (e.g., the end time is indefinite), then a [DOMException](/en-US/docs/Web/API/DOMException) with code `NOT_SUPPORTED_ERR` is raised.

[SVGAnimationElement.beginElement()](/en-US/docs/Web/API/SVGAnimationElement/beginElement)

Creates a begin instance time for the current time. The new instance time is added to the begin instance times list. The behavior of this method is equivalent to `beginElementAt(0)`.

[SVGAnimationElement.beginElementAt()](/en-US/docs/Web/API/SVGAnimationElement/beginElementAt)

Creates a begin instance time for the current time plus the specified offset. The new instance time is added to the begin instance times list.

[SVGAnimationElement.endElement()](/en-US/docs/Web/API/SVGAnimationElement/endElement)

Creates an end instance time for the current time. The new instance time is added to the end instance times list. The behavior of this method is equivalent to `endElementAt(0)`.

[SVGAnimationElement.endElementAt()](/en-US/docs/Web/API/SVGAnimationElement/endElementAt)

Creates an end instance time for the current time plus the specified offset. The new instance time is added to the end instance times list.

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `on...` handler property of this interface.

[beginEvent](/en-US/docs/Web/API/SVGAnimationElement/beginEvent_event)

Fired when the element local timeline begins to play.

[endEvent](/en-US/docs/Web/API/SVGAnimationElement/endEvent_event)

Fired when at the active end of the animation is reached.

[repeatEvent](/en-US/docs/Web/API/SVGAnimationElement/repeatEvent_event)

Fired when the element's local timeline repeats. It will be fired each time the element repeats, after the first iteration.

## [Specifications](#specifications)

Specification
[SVG Animations Level 2# InterfaceSVGAnimationElement](https://svgwg.org/specs/animations/#InterfaceSVGAnimationElement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 19, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/SVGAnimationElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/svganimationelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimationElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsvganimationelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSVGAnimationElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsvganimationelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F226ac33eb70ed5411dd2d68bd602c80cafd780b6%0A*+Document+last+modified%3A+2023-02-19T08%3A53%3A53.000Z%0A%0A%3C%2Fdetails%3E)
