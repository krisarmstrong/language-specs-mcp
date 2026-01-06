# VisualViewport

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨August 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVisualViewport&level=high)

The `VisualViewport` interface of the [CSSOM view API](/en-US/docs/Web/API/CSSOM_view_API) represents the visual viewport for a given window. For a page containing iframes, each iframe, as well as the containing page, will have a unique window object. Each window on a page will have a unique `VisualViewport` representing the properties associated with that window.

The mobile web contains two viewports, the layout viewport and the visual viewport. The layout viewport covers all the elements on a page and the visual viewport is what is actually visible on the screen. When the user pinch-zooms into the page, the visual viewport shrinks but the layout viewport is unchanged. User-interface features like the on-screen keyboard (OSK) can shrink the visual viewport without affecting the layout viewport.

What happens when a web page element needs to be visible on screen regardless of the visible portion of a web page? For example, what if you need a set of image controls to remain on screen regardless of the pinch-zoom level of the device? Current browsers vary in how they handle this. The visual viewport lets web developers solve this by positioning elements relative to what's shown on-screen.

You can get a window's visual viewport using [Window.visualViewport](/en-US/docs/Web/API/Window/visualViewport).

Note: Only the top-level window has a visual viewport that's distinct from the layout viewport. Therefore, it's generally only the `VisualViewport` object of the top-level window that's useful. For an [<iframe>](/en-US/docs/Web/HTML/Reference/Elements/iframe), visual viewport metrics like [VisualViewport.width](/en-US/docs/Web/API/VisualViewport/width) always correspond to layout viewport metrics like [document.documentElement.clientWidth](/en-US/docs/Web/API/Element/clientWidth).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Getting visual viewport information during scrolling and zooming](#getting_visual_viewport_information_during_scrolling_and_zooming)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

[VisualViewport.offsetLeft](/en-US/docs/Web/API/VisualViewport/offsetLeft)Read only

Returns the offset of the left edge of the visual viewport from the left edge of the layout viewport in CSS pixels.

[VisualViewport.offsetTop](/en-US/docs/Web/API/VisualViewport/offsetTop)Read only

Returns the offset of the top edge of the visual viewport from the top edge of the layout viewport in CSS pixels.

[VisualViewport.pageLeft](/en-US/docs/Web/API/VisualViewport/pageLeft)Read only

Returns the x coordinate of the visual viewport relative to the initial containing block origin of the top edge in CSS pixels.

[VisualViewport.pageTop](/en-US/docs/Web/API/VisualViewport/pageTop)Read only

Returns the y coordinate of the visual viewport relative to the initial containing block origin of the top edge in CSS pixels.

[VisualViewport.width](/en-US/docs/Web/API/VisualViewport/width)Read only

Returns the width of the visual viewport in CSS pixels.

[VisualViewport.height](/en-US/docs/Web/API/VisualViewport/height)Read only

Returns the height of the visual viewport in CSS pixels.

[VisualViewport.scale](/en-US/docs/Web/API/VisualViewport/scale)Read only

Returns the pinch-zoom scaling factor applied to the visual viewport.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [EventTarget](/en-US/docs/Web/API/EventTarget).

## [Events](#events)

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the relevant `oneventname` property of this interface.

[resize](/en-US/docs/Web/API/VisualViewport/resize_event)

Fired when the visual viewport is resized. Also available via the `onresize` property.

[scroll](/en-US/docs/Web/API/VisualViewport/scroll_event)

Fired when the visual viewport is scrolled. Also available via the `onscroll` property.

[scrollend](/en-US/docs/Web/API/VisualViewport/scrollend_event)

Fired when a scrolling operation on the visual viewport ends. Also available via the `onscrollend` property.

## [Examples](#examples)

## [Getting visual viewport information during scrolling and zooming](#getting_visual_viewport_information_during_scrolling_and_zooming)

Our [visual viewport](https://mdn.github.io/dom-examples/visual-viewport-api/) example provides a basic demonstration of how the different visual viewport features work, including the three event types. Load the page in supporting desktop and mobile browsers and try scrolling around the page and pinch-zooming. On `resize` and `scroll`, the information box is repositioned to keep the same position relative to the visual viewport, and the viewport and scroll information it shows is updated. Also, on `resize` and `scroll` we change the box color to indicate something is happening, changing it back on `scrollend`.

You'll find that on desktop browsers the [Window.scrollX](/en-US/docs/Web/API/Window/scrollX) and [Window.scrollY](/en-US/docs/Web/API/Window/scrollY) values are updated as the window is scrolled — the visual viewport position does not change. On mobile browsers, however, the [VisualViewport.offsetLeft](/en-US/docs/Web/API/VisualViewport/offsetLeft) and [VisualViewport.offsetTop](/en-US/docs/Web/API/VisualViewport/offsetTop) values are generally updated — it is usually the visual viewport that changes rather than the window position.

In the example, the HTML information box is represented by a [<div>](/en-US/docs/Web/HTML/Reference/Elements/div) with an `id` of `output` while the CSS is hidden for the sake of brevity.

html

```
<p id="instructions">
  Try scrolling around and pinch-zooming to see how the reported values change.
</p>
<div id="output">
  <p id="visual-info"></p>
  <hr />
  <p id="window-info"></p>
</div>
```

In the JavaScript, we start by getting references to the information box we'll be updating as the page is zoomed and scrolled, as well as the two paragraphs contained within it. The first one will contain reported [VisualViewport.offsetLeft](/en-US/docs/Web/API/VisualViewport/offsetLeft) and [VisualViewport.offsetTop](/en-US/docs/Web/API/VisualViewport/offsetTop) values, while the second one will contain reported [Window.scrollX](/en-US/docs/Web/API/Window/scrollX) and [Window.scrollY](/en-US/docs/Web/API/Window/scrollY) values.

js

```
const output = document.getElementById("output");
const visualInfo = document.getElementById("visual-info");
const windowInfo = document.getElementById("window-info");
```

Next, we define the two key functions we'll run when the events fire:

- The `scrollUpdater()` function will be executed on `resize` and `scroll`: this function updates the position of the information box relative to the visual viewport by querying the [VisualViewport.offsetTop](/en-US/docs/Web/API/VisualViewport/offsetTop) and [VisualViewport.offsetLeft](/en-US/docs/Web/API/VisualViewport/offsetLeft) properties and using their values to update the values of the relevant [inset properties](/en-US/docs/Glossary/Inset_properties). We also change the information box's background color to indicate that something is happening, and run the `updateText()` function to update the values shown in the box.
- The `scrollEndUpdater()` function will fire on `scrollend`: this returns the information box to its original color and runs the `updateText()` function to make sure the latest values are shown on `scrollend`.

js

```
const scrollUpdater = () => {
  output.style.top = `${visualViewport.offsetTop + 10}px`;
  output.style.left = `${visualViewport.offsetLeft + 10}px`;
  output.style.background = "yellow";
  updateText();
};

const scrollendUpdater = () => {
  output.style.background = "lime";
  updateText();
};
```

The `updateText()` function sets the [HTMLElement.innerText](/en-US/docs/Web/API/HTMLElement/innerText) of the first paragraph to show the current `VisualViewport.offsetLeft` and `VisualViewport.offsetTop` values, and the `HTMLElement.innerText` of the second paragraph to show the current `Window.scrollX` and `Window.scrollY` values. After defining `updateText()`, we immediately invoke it so that the information box displays correctly on page load.

js

```
function updateText() {
  visualInfo.innerText = `Visual viewport left: ${visualViewport.offsetLeft.toFixed(2)}
    top: ${visualViewport.offsetTop.toFixed(2)}`;
  windowInfo.innerText = `Window scrollX: ${window.scrollX.toFixed(2)}
    scrollY: ${window.scrollY.toFixed(2)}`;
}

updateText();
```

We truncated all values to two decimal places using the [Number.toFixed()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) method because some browsers render subpixel values, potentially with a large number of decimal places.

Now we set event handler properties on both the visual viewport and the [Window](/en-US/docs/Web/API/Window) object to run the key functions at the appropriate times on both mobile and desktop:

- We set the handlers on `window` so that the information box position and contents will update on conventional window scrolling operations, for example when you scroll the page on a desktop browser.
- We set the handlers on `visualViewport` so that the information box position and contents will update on visual viewport scrolling/zooming operations, for example when you scroll and pinch-zoom the page on a mobile browser.

js

```
visualViewport.onresize = scrollUpdater;
visualViewport.onscroll = scrollUpdater;
visualViewport.onscrollend = scrollendUpdater;
window.onresize = scrollUpdater;
window.onscroll = scrollUpdater;
window.onscrollend = scrollendUpdater;
```

The `scrollUpdater()` function will fire on `resize` and `scroll`, while `scrollEndUpdater()` will fire on `scrollend`.

### [Hiding an overlaid box on zoom](#hiding_an_overlaid_box_on_zoom)

This example, taken from the [Visual Viewport README](https://github.com/WICG/visual-viewport), shows how to write a bit of code that will hide an overlaid box (which might contain an advert, say) when the user zooms in. This is a nice way to improve the user experience when zooming in on pages. A [live sample](https://wicg.github.io/visual-viewport/examples/hide-on-zoom.html) is also available.

js

```
const bottomBar = document.getElementById("bottom-bar");
const viewport = window.visualViewport;

function resizeHandler() {
  bottomBar.style.display = viewport.scale > 1.3 ? "none" : "block";
}

window.visualViewport.addEventListener("resize", resizeHandler);
```

### [Simulating position: device-fixed](#simulating_position_device-fixed)

This example, also taken from the [Visual Viewport README](https://github.com/WICG/visual-viewport), shows how to use this API to simulate `position: device-fixed`, which fixes elements to the visual viewport. A [live sample](https://wicg.github.io/visual-viewport/examples/fixed-to-viewport.html) is also available.

js

```
const bottomBar = document.getElementById("bottom-bar");
const viewport = window.visualViewport;
function viewportHandler() {
  const layoutViewport = document.getElementById("layoutViewport");

  // Since the bar is position: fixed we need to offset it by the visual
  // viewport's offset from the layout viewport origin.
  const offsetLeft = viewport.offsetLeft;
  const offsetTop =
    viewport.height -
    layoutViewport.getBoundingClientRect().height +
    viewport.offsetTop;

  // You could also do this by setting style.left and style.top if you
  // use width: 100% instead.
  bottomBar.style.transform = `translate(${offsetLeft}px, ${offsetTop}px) scale(${
    1 / viewport.scale
  })`;
}
window.visualViewport.addEventListener("scroll", viewportHandler);
window.visualViewport.addEventListener("resize", viewportHandler);
```

Note: This technique should be used with care; emulating `position: device-fixed` in this way can result in the fixed element flickering during scrolling.

## [Specifications](#specifications)

Specification
[CSSOM View Module# the-visualviewport-interface](https://drafts.csswg.org/cssom-view/#the-visualviewport-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Viewports Explainer](https://github.com/bokand/bokand.github.io/blob/master/web_viewports_explainer.md) — useful explanation of web viewports concepts, including the difference between visual viewport and layout viewport.

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/VisualViewport/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/visualviewport/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVisualViewport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvisualviewport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FVisualViewport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvisualviewport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F12b296d2b3937c45b2363f34ed8afadcf00ed166%0A*+Document+last+modified%3A+2025-11-21T10%3A04%3A44.000Z%0A%0A%3C%2Fdetails%3E)
