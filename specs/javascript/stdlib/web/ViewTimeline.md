# ViewTimeline

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTimeline&level=not)

The `ViewTimeline` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) represents a view progress timeline (see [CSS scroll-driven animations](/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) for more details).

Pass a `ViewTimeline` instance to the [Animation()](/en-US/docs/Web/API/Animation/Animation) constructor or the [animate()](/en-US/docs/Web/API/Element/animate) method to specify it as the timeline that will control the progress of the animation.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ViewTimeline()](/en-US/docs/Web/API/ViewTimeline/ViewTimeline)

Creates a new `ViewTimeline` object instance.

## [Instance properties](#instance_properties)

This interface also inherits the properties of its parent, [ScrollTimeline](/en-US/docs/Web/API/ScrollTimeline).

[subject](/en-US/docs/Web/API/ViewTimeline/subject)Read only

Returns a reference to the subject element whose visibility within its nearest ancestor scrollable element (scroller) is driving the progress of the timeline and therefore the animation.

[startOffset](/en-US/docs/Web/API/ViewTimeline/startOffset)Read only

Returns a [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue) representing the starting (0% progress) scroll position of the timeline as an offset from the start of the overflowing section of content in the scroller.

[endOffset](/en-US/docs/Web/API/ViewTimeline/endOffset)Read only

Returns a [CSSNumericValue](/en-US/docs/Web/API/CSSNumericValue) representing the ending (100% progress) scroll position of the timeline as an offset from the start of the overflowing section of content in the scroller.

## [Instance methods](#instance_methods)

This interface inherits the methods of its parent, [ScrollTimeline](/en-US/docs/Web/API/ScrollTimeline).

## [Examples](#examples)

### [Displaying the subject and offsets of a view progress timeline](#displaying_the_subject_and_offsets_of_a_view_progress_timeline)

In this example, we animate an element with a `class` of `subject` along a view progress timeline — it animates when moved upwards through the document as it scrolls. We also output the `subject`, `startOffset`, and `endOffset` values to an output element in the top-right corner.

#### HTML

The HTML for the example is shown below.

html

```
<div class="content">
  <h1>Content</h1>

  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Risus quis varius quam
    quisque id. Et ligula ullamcorper malesuada proin libero nunc consequat
    interdum varius. Elit ullamcorper dignissim cras tincidunt lobortis feugiat
    vivamus at augue.
  </p>

  <p>
    Dolor sed viverra ipsum nunc aliquet. Sed risus pretium quam vulputate
    dignissim. Tortor aliquam nulla facilisi cras. A erat nam at lectus urna
    duis convallis convallis. Nibh ipsum consequat nisl vel pretium lectus.
    Sagittis aliquam malesuada bibendum arcu vitae elementum. Malesuada bibendum
    arcu vitae elementum curabitur vitae nunc sed velit.
  </p>

  <div class="subject animation"></div>

  <p>
    Adipiscing enim eu turpis egestas pretium aenean pharetra magna ac. Arcu
    cursus vitae congue mauris rhoncus aenean vel. Sit amet cursus sit amet
    dictum. Augue neque gravida in fermentum et. Gravida rutrum quisque non
    tellus orci ac auctor augue mauris. Risus quis varius quam quisque id diam
    vel quam elementum. Nibh praesent tristique magna sit amet purus gravida
    quis. Duis ultricies lacus sed turpis tincidunt id aliquet. In egestas erat
    imperdiet sed euismod nisi. Eget egestas purus viverra accumsan in nisl nisi
    scelerisque. Netus et malesuada fames ac.
  </p>

  <div class="output"></div>
</div>
```

#### CSS

The CSS for the example looks like this:

css

```
.subject {
  width: 300px;
  height: 200px;
  margin: 0 auto;
  background-color: deeppink;
}

.content {
  width: 75%;
  max-width: 800px;
  margin: 0 auto;
}

.output {
  position: fixed;
  top: 5px;
  right: 5px;
}

p,
h1,
div {
  font-family: "Helvetica", "Arial", sans-serif;
}

h1 {
  font-size: 3rem;
}

p {
  font-size: 1.5rem;
  line-height: 1.5;
}
```

#### JavaScript

In the JavaScript, we grab references to the `subject` and `output``<div>`s, then create a new `ViewTimeline`, associating it with the `subject` element to specify that the timeline progress is based on this element's visibility through its scrolling ancestor, setting a `block` axis, and setting `inset` values to adjust the position of the box in which the subject is deemed to be visible.

We then animate the `subject` element with the Web Animations API. Last of all, we display the `subject`, `startOffset`, and `endOffset` values in the `output` element.

js

```
const subject = document.querySelector(".subject");
const output = document.querySelector(".output");

const timeline = new ViewTimeline({
  subject,
  axis: "block",
  inset: [CSS.px("200"), CSS.px("300")],
});

subject.animate(
  {
    opacity: [0, 1],
    transform: ["scaleX(0)", "scaleX(1)"],
  },
  {
    fill: "both",
    timeline,
  },
);

output.textContent += `Subject element: ${timeline.subject.nodeName}, `;
output.textContent += `start offset: ${timeline.startOffset}, `;
output.textContent += `end offset: ${timeline.endOffset}.`;
```

#### Result

Scroll to see the subject element being animated.

## [Specifications](#specifications)

Specification
[Scroll-driven Animations# viewtimeline-interface](https://drafts.csswg.org/scroll-animations/#viewtimeline-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Animations API](/en-US/docs/Web/API/Web_Animations_API)
- [CSS scroll-driven animations](/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
- [AnimationTimeline](/en-US/docs/Web/API/AnimationTimeline), [ScrollTimeline](/en-US/docs/Web/API/ScrollTimeline)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/ViewTimeline/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/viewtimeline/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTimeline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fviewtimeline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FViewTimeline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fviewtimeline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
