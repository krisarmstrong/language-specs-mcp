# ScrollTimeline

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScrollTimeline&level=not)

The `ScrollTimeline` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) represents a scroll progress timeline (see [CSS scroll-driven animations](/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) for more details).

Pass a `ScrollTimeline` instance to the [Animation()](/en-US/docs/Web/API/Animation/Animation) constructor or the [animate()](/en-US/docs/Web/API/Element/animate) method to specify it as the timeline that will control the progress of the animation.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ScrollTimeline()](/en-US/docs/Web/API/ScrollTimeline/ScrollTimeline)

Creates a new `ScrollTimeline` object instance.

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent, [AnimationTimeline](/en-US/docs/Web/API/AnimationTimeline).

[source](/en-US/docs/Web/API/ScrollTimeline/source)Read only

Returns a reference to the scrollable element (scroller) whose scroll position is driving the progress of the timeline and therefore the animation.

[axis](/en-US/docs/Web/API/ScrollTimeline/axis)Read only

Returns an enumerated value representing the scroll axis that is driving the progress of the timeline.

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [AnimationTimeline](/en-US/docs/Web/API/AnimationTimeline).

## [Examples](#examples)

### [Displaying the source and axis of a scroll progress timeline](#displaying_the_source_and_axis_of_a_scroll_progress_timeline)

In this example, we animate an element with a `class` of `box` along a view progress timeline — it animates across the screen as the document scrolls. We output the `source` element and scroll `axis` to an `output` element in the top-right corner.

#### HTML

The HTML for the example is shown below.

html

```
<div class="content"></div>
<div class="box"></div>
<div class="output"></div>
```

#### CSS

The CSS for the example looks like this:

css

```
.content {
  height: 2000px;
}

.box {
  width: 100px;
  height: 100px;
  border-radius: 10px;
  background-color: rebeccapurple;
  position: fixed;
  top: 20px;
  left: 0%;
}

.output {
  font-family: "Helvetica", "Arial", sans-serif;
  position: fixed;
  top: 5px;
  right: 5px;
}
```

#### JavaScript

In the JavaScript, we grab references to the `box` and `output``<div>`s, then create a new `ScrollTimeline`, specifying that the element that will drive the scroll timeline progress is the document ([<html>](/en-US/docs/Web/HTML/Reference/Elements/html)) element, and the scroll axis is the `block` axis. We then animate the `box` element with the Web Animations API. Last of all, we display the source element and axis in the `output` element.

js

```
const box = document.querySelector(".box");
const output = document.querySelector(".output");

const timeline = new ScrollTimeline({
  source: document.documentElement,
  axis: "block",
});

box.animate(
  {
    rotate: ["0deg", "720deg"],
    left: ["0%", "100%"],
  },
  {
    timeline,
  },
);

output.textContent = `Timeline source element: ${timeline.source.nodeName}. Timeline scroll axis: ${timeline.axis}`;
```

#### Result

Scroll to see the box being animated.

## [Specifications](#specifications)

Specification
[Scroll-driven Animations# scrolltimeline-interface](https://drafts.csswg.org/scroll-animations/#scrolltimeline-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Animations API](/en-US/docs/Web/API/Web_Animations_API)
- [CSS scroll-driven animations](/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
- [AnimationTimeline](/en-US/docs/Web/API/AnimationTimeline), [ViewTimeline](/en-US/docs/Web/API/ViewTimeline)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ScrollTimeline/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/scrolltimeline/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScrollTimeline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fscrolltimeline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScrollTimeline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fscrolltimeline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
