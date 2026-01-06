# Web Animations API

The Web Animations API allows for synchronizing and timing changes to the presentation of a Web page, i.e., animation of DOM elements. It does so by combining two models: the Timing Model and the Animation Model.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Web Animations interfaces](#web_animations_interfaces)
- [Extensions to other interfaces](#extensions_to_other_interfaces)
- [Specifications](#specifications)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

The Web Animations API provides a common language for browsers and developers to describe animations on DOM elements. To get more information on the concepts behind the API and how to use it, read [Using the Web Animations API](/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API).

## [Web Animations interfaces](#web_animations_interfaces)

[Animation](/en-US/docs/Web/API/Animation)

Provides playback controls and a timeline for an animation node or source. Can take an object created with the [KeyframeEffect()](/en-US/docs/Web/API/KeyframeEffect/KeyframeEffect) constructor.

[KeyframeEffect](/en-US/docs/Web/API/KeyframeEffect)

Describes sets of animatable properties and values, called keyframes and their timing options. These can then be played using the [Animation()](/en-US/docs/Web/API/Animation/Animation) constructor.

[AnimationTimeline](/en-US/docs/Web/API/AnimationTimeline)

Represents the timeline of animation. This interface exists to define timeline features (inherited by [DocumentTimeline](/en-US/docs/Web/API/DocumentTimeline) and future timeline objects) and is not itself accessed by developers.

[AnimationEvent](/en-US/docs/Web/API/AnimationEvent)

Part of the [CSS Animations](/en-US/docs/Web/CSS/Guides/Animations) module, capturing the animation name and elapsed time.

[DocumentTimeline](/en-US/docs/Web/API/DocumentTimeline)

Represents animation timelines, including the default document timeline (accessed using the [Document.timeline](/en-US/docs/Web/API/Document/timeline) property).

## [Extensions to other interfaces](#extensions_to_other_interfaces)

The Web Animations API adds features to [document](/en-US/docs/Web/API/Document) and [element](/en-US/docs/Web/API/Element).

### [Extensions to the Document interface](#extensions_to_the_document_interface)

[document.timeline](/en-US/docs/Web/API/Document/timeline)

The `DocumentTimeline` object representing the default document timeline.

[document.getAnimations()](/en-US/docs/Web/API/Document/getAnimations)

Returns an Array of [Animation](/en-US/docs/Web/API/Animation) objects currently in effect on elements in the `document`.

### [Extensions to the Element interface](#extensions_to_the_element_interface)

[Element.animate()](/en-US/docs/Web/API/Element/animate)

A shortcut method for creating and playing an animation on an element. It returns the created [Animation](/en-US/docs/Web/API/Animation) object instance.

[Element.getAnimations()](/en-US/docs/Web/API/Element/getAnimations)

Returns an Array of [Animation](/en-US/docs/Web/API/Animation) objects currently affecting an element or which are scheduled to do so in the future.

## [Specifications](#specifications)

Specification[Web Animations](https://drafts.csswg.org/web-animations/)

## [See also](#see_also)

- CSS [animation](/en-US/docs/Web/CSS/Reference/Properties/animation) shorthand property
- CSS [animation-timeline](/en-US/docs/Web/CSS/Reference/Properties/animation-timeline) property
- [Using the Web Animations API](/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)
- [Using CSS animations](/en-US/docs/Web/CSS/Guides/Animations/Using)
- [CSS animations](/en-US/docs/Web/CSS/Guides/Animations) module
- [CSS scroll-driven animations](/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) module

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Web_Animations_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/web_animations_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Animations_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fweb_animations_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWeb_Animations_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fweb_animations_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
